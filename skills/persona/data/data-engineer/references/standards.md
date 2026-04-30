## § 7 · Standards & Reference

### dbt Layer Architecture

```
models/
├── staging/          # Raw source cleaning; 1:1 with source tables
│   ├── stg_orders.sql
│   └── stg_customers.sql
├── intermediate/     # Business logic; reusable; no direct BI access
│   ├── int_order_items_joined.sql
│   └── int_customer_lifetime_value.sql
└── marts/           # Business-facing; fact & dimension tables
    ├── fct_orders.sql
    └── dim_customers.sql

Naming conventions:
  stg_ = staging; int_ = intermediate; fct_ = fact; dim_ = dimension
  Materializations: staging=view, intermediate=view, marts=table/incremental

dbt test template (schema.yml):
  - name: customer_id
    tests:
      - not_null
      - unique
      - relationships:
          to: ref('dim_customers')
          field: customer_id
```

### Incremental Model Pattern (dbt)

```sql
-- models/marts/fct_events.sql
{{ config(
    materialized='incremental',
    unique_key='event_id',
    incremental_strategy='merge',
    partition_by={'field': 'event_date', 'data_type': 'date'},
    cluster_by=['user_id', 'event_type']
) }}

SELECT
    event_id,
    user_id,
    event_type,
    event_date,
    properties,
    CURRENT_TIMESTAMP() AS _dbt_updated_at
FROM {{ ref('stg_events') }}

{% if is_incremental() %}
    WHERE event_date >= (
        SELECT DATE_SUB(MAX(event_date), INTERVAL 3 DAY)
        FROM {{ this }}
    )  -- 3-day lookback for late-arriving events
{% endif %}
```

### Airflow DAG Best Practices

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-eng',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'retry_exponential_backoff': True,
    'email_on_failure': True,
    'email': ['data-alerts@company.com'],
}

with DAG(
    dag_id='daily_revenue_pipeline',
    default_args=default_args,
    schedule_interval='0 6 * * *',  # 6 AM UTC daily
    start_date=datetime(2025, 1, 1),
    catchup=False,  # Don't backfill by default
    tags=['finance', 'daily'],
    max_active_runs=1,  # Prevent concurrent runs
) as dag:
    pass
    # Tasks: extract → validate → transform → load → test → alert
```

---
