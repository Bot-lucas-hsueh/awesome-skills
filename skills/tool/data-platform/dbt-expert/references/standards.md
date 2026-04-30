# Standards & Reference

## 7.1 Official Documentation

- [dbt Core Documentation](https://docs.getdbt.com/docs/core)
- [dbt Cloud Documentation](https://docs.getdbt.com/docs/cloud/about-cloud)
- [dbt Project Structure](https://docs.getdbt.com/reference/project-configs/project-configs)
- [dbt Models](https://docs.getdbt.com/docs/build/models)
- [dbt Tests](https://docs.getdbt.com/docs/build/tests)
- [dbt Macros](https://docs.getdbt.com/docs/build/jinja-macros)
- [dbt Semantic Layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl)
- [dbt Explorer](https://docs.getdbt.com/docs/collaborate/explore-projects)
- [dbt Core Installation](https://docs.getdbt.com/docs/core/install)
- [dbt Adapter Overview](https://docs.getdbt.com/docs/supported-adapters)
- [dbt Metrics](https://docs.getdbt.com/docs/build/metrics)
- [dbt Exposures](https://docs.getdbt.com/docs/collaborate/govern/project-governance#exposures)
- [dbt Contract](https://docs.getdbt.com/docs/contracts)

## 7.2 Project Structure

```
dbt_project/
├── dbt_project.yml           # Project configuration
├── packages.yml              # External packages (dbt-utils, etc.)
├── profiles.yml              # Database connections (~/.dbt/ or project root)
├── logs/                     # dbt debug logs
├── target/                   # Compiled SQL, run artifacts
├── docs/
│   └── manifest.json         # Generated documentation
├── models/
│   ├── marts/
│   │   ├── finance/
│   │   │   ├── orders.sql
│   │   │   └── customers.sql
│   │   ├── marketing/
│   │   │   └── ad_metrics.sql
│   │   └── _metrics/
│   │       └── revenue_metric.yml
│   ├── intermediate/
│   │   ├── int_order_items.sql
│   │   └── int_customer_lifetime_value.sql
│   └── staging/
│       ├── stripe/
│       │   ├── stg_stripe_orders.sql
│       │   └── stg_stripe_payments.sql
│       └── salesforce/
│           ├── stg_salesforce_contacts.sql
│           └── stg_salesforce_opportunities.sql
├── seeds/                    # CSV files loaded as tables
├── macros/
│   ├── cross_db/
│   │   └── date_diff.sql
│   └── email_validation.sql
├── tests/
│   └── generic_tests/
│       └── positive_value.sql
└── assets/
    └── taxonomy.csv
```

## 7.3 Configuration Reference

### dbt_project.yml

```yaml
name: analytics_project
version: 1.0.0
config-version: 2

vars:
  payment_status: ['completed', 'refunded']
  app_env: prod

on-run-start:
  - "{{ log('Starting dbt run', info=True) }}"

on-run-end:
  - "{{ log('dbt run complete', info=True) }}"

models:
  +database: "{{ target.database }}"
  +schema: "{{ target.schema }}"
  +materialized: table
  +grants:
    select: ['analyst_role', 'bi_service']

  marts:
    +tags: ["marts"]
    finance:
      +schema: finance
      +materialized: incremental
    marketing:
      +schema: marketing
      +materialized: view

  intermediate:
    +tags: ["intermediate"]
    +materialized: ephemeral

  staging:
    +tags: ["staging"]
    +materialized: view
```

### profiles.yml

```yaml
config:
  send_usage_metrics: false
  partial_parse: true

your_profile:
  target: prod
  outputs:
    dev:
      type: snowflake
      account: xy12345.us-east-1
      user: "{{ env_var('DBT_USER') }}"
      password: "{{ env_var('DBT_PASSWORD') }}"
      role: transformer
      database: analytics_dev
      warehouse: xsmall_wh
      schema: dbt_{{ target.name }}
      threads: 4
      client_session_keep_alive: true

    prod:
      type: snowflake
      account: xy12345.us-east-1
      user: "{{ env_var('DBT_USER') }}"
      password: "{{ env_var('DBT_PASSWORD') }}"
      role: transformer
      database: analytics_prod
      warehouse: medium_wh
      schema: dbt_{{ target.name }}
      threads: 8
      query_tag: dbt_run
```

## 7.4 Model Configuration Reference

### Materialization Types

| Type | Description | Use Case |
|------|-------------|----------|
| `view` | SQL stored in DB | Base/staging layers, frequently changing |
| `table` | Physical table | Aggregated marts, stable large data |
| `incremental` | Upsert into table | Large fact tables, append-only data |
| `ephemeral` | CTAS, not stored | Intermediate reusable logic |
| `external` | External table (e.g., Iceberg) | Unstructured / lakehouse |

### Model Config Block

```sql
{{ config(
    materialized='incremental',
    unique_key='order_id',
    partition_by=['date_key'],
    cluster_by=['customer_region', 'product_category'],
    incremental_strategy='merge',
    merge_exclude_columns=['processed_at'],
    grants={
        'select': ['analyst_role'],
        'insert': ['etl_service'],
    },
    tags=['finance', 'daily'],
    meta={
        'owner': 'finance-team',
        'tier': 1,
    },
    post-hook=[
        'GRANT SELECT ON {{ this }} TO analyst_role',
    ],
    pre-hook=[
        'ALTER TABLE {{ this }} SWAP WITH {{ target.schema }}.{{ this.name }}_staging',
    ],
) }}
```

### Schema.yml (Model Tests & Documentation)

```yaml
version: 2

models:
  - name: int_order_items
    description: >
      Intermediate model joining orders with line items and products.
      Includes calculated revenue after discounts.
    meta:
      owner: data-platform
      expires: 2024-12-31
    tests:
      - dbt_utils.recency:
          datepart: hour
          field: created_at
          interval: 4
          config:
            where: status = 'completed'
      - dbt_utils.unique_combination_of_columns:
          combination_of_columns:
            - order_id
            - line_item_id
    columns:
      - name: order_id
        description: Unique order identifier
        meta:
          pii: false
        tests:
          - not_null
          - unique

      - name: customer_id
        tests:
          - not_null
          - relationships:
              to: ref('dim_customers')
              field: customer_id
              config:
                where: status = 'active'

      - name: revenue
        description: Line item revenue after discount
        tests:
          - not_null
          - dbt_utils.accepted_range:
              min_value: 0
              max_value: 1000000

      - name: created_at
        tests:
          - not_null
          - dbt_utils.recency:
              datepart: hour
              interval: 4
```

## 7.5 dbt Commands Reference

```bash
# Development
dbt deps                          # Install packages from packages.yml
dbt debug                         # Verify connection and project setup
dbt init project_name             # Initialize new project

# Running models
dbt run                           # Run all models
dbt run --select tag:staging       # Run models with specific tag
dbt run --select +marts.orders     # Run orders and all upstream
dbt run --select mart:*            # Run all models in marts directory
dbt run --select package.model     # Run specific model from package
dbt run --fails-fast              # Stop on first failure
dbt run --full-refresh           # Full refresh (recreate tables)

# Incremental
dbt run --select my_model --full-refresh   # Force full rebuild
dbt run --vars '{"lookback_days": 90}'     # Pass variables

# Testing
dbt test                          # Run all tests
dbt test --select model_name      # Test specific model
dbt test --exclude tag:unit       # Exclude specific tests
dbt build                         # Run + test + seed (combined)

# Documentation
dbt docs generate                 # Build documentation
dbt docs serve --port 8080        # Serve docs locally

# Lineage
dbt ls --select +model            # List upstream dependencies
dbt ls --select model+           # List downstream dependents
dbt ls --select package:*         # List all models in package

# Seeds & Sources
dbt seed                          # Load CSV files from seeds/
dbt source freshness              # Check source data freshness
dbt compile                       # Compile without running

# Projects
dbt clean                         # Remove target/ directory
dbt retry                         # Retry last failed run
```

## 7.6 Version Compatibility

| dbt Core | Python | Key Features |
|----------|--------|--------------|
| 1.3.x | 3.7+ | Python models, semantic layer alpha |
| 1.4.x | 3.8+ | Python models GA, dbt build command |
| 1.5.x | 3.8+ | dbt Cloud governance, model access |
| 1.6.x | 3.8+ |敏 Contracts GA, access patterns |
| 1.7.x | 3.8+ | Semantic layer v2, metrics, exposures |
| 1.8.x | 3.8+ | Adapter v2, Python 3.12 support |
| 1.9.x | 3.9+ | dbt-native pipelines, test configs |
