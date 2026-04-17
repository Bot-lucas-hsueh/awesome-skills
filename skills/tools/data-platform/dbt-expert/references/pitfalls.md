# Examples

## 10.1 Staging Models

### Basic Staging

```sql
-- models/staging/stripe/stg_stripe_orders.sql
{{ config(
    materialized='view',
    tags=['staging', 'stripe'],
) }}

SELECT
    o.id AS order_id,
    o.customer_id,
    o.status,
    o.currency,
    o.amount AS total_amount,
    o.created_at,
    o.updated_at,
    -- Flatten nested fields
    o.shipping_address->>'city' AS shipping_city,
    o.shipping_address->>'country' AS shipping_country,
    -- Normalize status
    CASE
        WHEN o.status = 'succeeded' THEN 'completed'
        WHEN o.status IN ('pending', 'requires_payment_method') THEN 'pending'
        WHEN o.status IN ('canceled', 'void') THEN 'cancelled'
        ELSE 'other'
    END AS order_status,
    -- Deduplicate based on latest update
    ROW_NUMBER() OVER (
        PARTITION BY o.id
        ORDER BY o.updated_at DESC
    ) AS _rn
FROM {{ source('stripe', 'orders') }} o
QUALIFY _rn = 1
```

### CDC Staging with Airbyte / Fivetran

```sql
-- models/staging/postgres/cdc/stg_postgres_orders.sql
{{ config(
    materialized='incremental',
    unique_key='order_id',
    tags=['staging', 'postgres', 'cdc'],
) }}

SELECT
    _airbyte_ab_id,
    _airbyte_emitted_at,
    _airbyte_data->>'id' AS order_id,
    _airbyte_data->>'customer_id' AS customer_id,
    (_airbyte_data->>'total_amount')::NUMERIC AS total_amount,
    (_airbyte_data->>'created_at')::TIMESTAMP AS created_at,
    _airbyte_data->'_airbyte_normalized_at' AS normalized_at
FROM {{ source('postgres_replica', 'orders') }}

{% if is_incremental() %}
WHERE _airbyte_emitted_at > (
    SELECT MAX(_airbyte_emitted_at)
    FROM {{ this }}
)
{% endif %}
```

## 10.2 Intermediate Models

### Reusable Business Logic

```sql
-- models/intermediate/int_order_items_enriched.sql
{{ config(materialized='ephemeral', tags=['intermediate']) }}

SELECT
    oi.order_id,
    oi.line_item_id,
    oi.product_id,
    oi.quantity,
    oi.unit_price,
    oi.unit_price * oi.quantity AS gross_revenue,
    oi.unit_price * oi.quantity * (1 - COALESCE(d.discount_pct, 0)) AS net_revenue,
    p.category AS product_category,
    p.brand AS product_brand,
    p.is_organic,
    o.created_at AS order_created_at,
    o.customer_id,
    o.order_status,
    c.customer_tier,
    c.lifetime_value_segment
FROM {{ ref('stg_order_items') }} oi
JOIN {{ ref('stg_orders') }} o ON oi.order_id = o.order_id
JOIN {{ ref('stg_products') }} p ON oi.product_id = p.product_id
LEFT JOIN {{ ref('stg_discounts') }} d ON oi.product_id = d.product_id
    AND o.created_at BETWEEN d.start_date AND d.end_date
LEFT JOIN {{ ref('dim_customers') }} c ON o.customer_id = c.customer_id
```

## 10.3 Mart Models

### Incremental Fact Table

```sql
-- models/marts/facts/fct_orders.sql
{{ config(
    materialized='incremental',
    unique_key='order_id',
    partition_by=['order_date'],
    cluster_by=['customer_id', 'product_category'],
    incremental_strategy='merge',
    grants={
        'select': ['analyst_role', 'bi_service'],
    },
    tags=['facts', 'orders'],
) }}

SELECT
    order_id,
    customer_id,
    order_date,
    product_id,
    product_category,
    product_brand,
    quantity,
    net_revenue,
    gross_revenue,
    discount_amount,
    shipping_cost,
    order_status,
    customer_tier,
    customer_lifetime_value_segment,
    is_first_order,
    days_since_previous_order,
    '{{ run_started_at }}'::TIMESTAMP AS run_started_at
FROM {{ ref('int_order_items_enriched') }}
WHERE 1=1

{% if is_incremental() %}
    AND order_created_at > (
        SELECT COALESCE(MAX(order_date), '1900-01-01')
        FROM {{ this }}
    )
    AND order_status = 'completed'
{% endif %}
```

### Snapshot / Slowly Changing Dimension

```sql
-- models/marts/dimensions/dim_customers.sql
{{ config(
    materialized='snapshot',
    strategy='timestamp',
    updated_at='updated_at',
    tags=['dimensions', 'scd'],
) }}

SELECT
    customer_id,
    email,
    first_name,
    last_name,
    customer_tier,
    signup_date,
    updated_at,
    current_flag
FROM {{ source('crm', 'customers') }}
```

### Metric Definitions (dbt Semantic Layer)

```yaml
# models/marts/_metrics/revenue_metrics.yml
metrics:
  - name: total_revenue
    label: Total Revenue
    model: ref('fct_orders')
    description: Sum of net revenue for completed orders
    calculation_method: sum
    expression: net_revenue
    filters:
      - field: order_status
        operator: '='
        value: completed
    meta:
      tier: 1
      owner: finance

  - name: order_count
    label: Order Count
    model: ref('fct_orders')
    calculation_method: count
    expression: order_id
    filters:
      - field: order_status
        operator: '='
        value: completed

  - name: customer_count
    label: Unique Customers
    model: ref('fct_orders')
    calculation_method: count_distinct
    expression: customer_id
```

## 10.4 Generic & Custom Tests

### Generic Test (Reusable)

```sql
-- tests/generic/positive_value.sql
-- Returns zero rows if all values are > 0
SELECT
    {{ entity_id }} AS id,
    COUNT(*) AS failures
FROM {{ model }}
WHERE {{ value_column }} <= 0
GROUP BY {{ entity_id }}
HAVING COUNT(*) > 0
```

### Custom Test (Singular)

```sql
-- tests/orders/no_duplicates.sql
SELECT
    order_id,
    COUNT(*) AS duplicate_count
FROM {{ ref('stg_orders') }}
GROUP BY order_id
HAVING COUNT(*) > 1
```

### Schema Test Definitions

```yaml
# models/marts/facts/fct_orders.yml
version: 2

models:
  - name: fct_orders
    description: Order-level fact table with revenue and customer attribution
    tests:
      - dbt_utils.unique_combination_of_columns:
          combination_of_columns:
            - order_id
            - product_id
    columns:
      - name: order_id
        tests:
          - not_null
          - unique
          - relationships:
              to: ref('dim_customers')
              field: customer_id
              config:
                where: current_flag = true

      - name: net_revenue
        tests:
          - not_null
          - dbt_utils.accepted_range:
              min_value: 0
              max_value: 1000000

      - name: order_date
        tests:
          - not_null
          - dbt_utils.recency:
              datepart: day
              interval: 1
              config:
                where: order_status = 'completed'
```

## 10.5 Macros

### Surrogate Key

```sql
-- macros/surrogate_key.sql
{% macro generate_surrogate_key(columns, algorithm='MD5') %}
    {%- if algorithm == 'MD5' -%}
        MD5(CONCAT(
            {% for col in columns %}
                CAST({{ col }} AS STRING){% if not loop.last %}, '|', {% endif %}
            {% endfor %}
        ))
    {%- elif algorithm == 'SHA256' -%}
        SHA2(CONCAT(
            {% for col in columns %}
                CAST({{ col }} AS STRING){% if not loop.last %}, '|', {% endif %}
            {% endfor %}
        ), 256)
    {%- endif -%}
{% endmacro %}
```

### Date Helpers

```sql
-- macros/date_helpers.sql
{% macro date_range(start_date, end_date) %}
    GENERATE_SERIES(
        DATE '{{ start_date }}',
        DATE '{{ end_date }}',
        INTERVAL '1 day'
    )::DATE AS date_key
{% endmacro %}

{% macro fiscal_quarter(date_expr) %}
    CONCAT(
        YEAR(DATE_TRUNC('quarter', {{ date_expr }})),
        '-Q',
        QUARTER({{ date_expr }})
    )
{% endmacro %}
```

## 10.6 Exposures

```yaml
# models/marts/_exposures.yml
exposures:
  - name: weekly_revenue_dashboard
    description: Executive dashboard showing weekly revenue KPIs
    type: dashboard
    maturity: high
    owner:
      name: Finance Team
      email: finance@example.com
    depends_on:
      - ref('fct_orders')
      - ref('dim_customers')
    meta:
      priority: P1
      sla: 9am daily

  - name: revenue_api
    description: Internal API for revenue data
    type: application
    maturity: high
    owner:
      name: Data Platform
      email: data-platform@example.com
    depends_on:
      - ref('fct_orders')
```
