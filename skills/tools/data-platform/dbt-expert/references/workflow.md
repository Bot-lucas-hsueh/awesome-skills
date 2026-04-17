# Troubleshooting Guide

## 8.1 Common Failures

### Connection & Authentication

| Error | Cause | Fix |
|-------|-------|-----|
| `Credential retrieval failed` | Missing env vars | Set `DBT_USER`, `DBT_PASSWORD` or use key-pair |
| `Database error: invalid connection` | Wrong account/region | Check `account` in profiles.yml |
| `Permission denied on schema` | Role lacks privileges | Grant `USAGE` on database, `CREATE` on schema |
| `Query timeout exceeded` | Long-running model | Set `query_comment` timeout or split model |

```bash
# Debug connection
dbt debug --target prod
dbt debug --profile your_profile

# Test with verbose output
export DBT_TARGET=prod
export DBT_LOG_LEVEL=debug
dbt run --debug --select model_name
```

### Model Compilation & Execution

| Error | Cause | Fix |
|-------|-------|-----|
| `Compilation error: 'ref' is undefined` | Missing `ref()` or wrong model name | Use `ref('model_name')` with matching name in yml |
| `Runtime error: relation already exists` | View/table already exists, wrong materialization | Use `dbt run --full-refresh` for tables |
| `Catalog error: column not found` | Column renamed in source | Update schema.yml, use `dbt source freshness` |
| `Merge error: column has type mismatch` | Type conflict in merge | Cast explicitly in SELECT |
| `No columns returned` | Empty source data | Add `{% if adapter.get_relation(...) %} {% endif %}` guard |

```sql
-- Guard against empty source in incremental
{{ config(materialized='incremental') }}

SELECT
    order_id,
    MAX(created_at) AS last_updated
FROM {{ ref('stg_orders') }}
{% if is_incremental() %}
WHERE created_at > (SELECT MAX(last_updated) FROM {{ this }})
{% endif %}
GROUP BY order_id
HAVING COUNT(*) > 0
```

### Incremental Model Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Duplicate rows after incremental | No `unique_key` or wrong key | Set `unique_key='order_id'`, deduplicate source |
| Merge silently skipping records | Type mismatch on key column | Cast key to consistent type |
| Full table scan on each run | `is_incremental()` not filtering | Add WHERE clause with `{{ this }}` |
| `unique_key` column has NULLs | NULL key values | Coalesce key: `unique_key='COALESCE(id, run_id)'` |

```sql
-- Safe incremental with surrogate key
{{ config(
    materialized='incremental',
    unique_key='id',
    incremental_strategy='merge',
) }}

SELECT
    {{ dbt_utils.generate_surrogate_key(['order_id', 'line_item_id']) }} AS id,
    order_id,
    line_item_id,
    revenue
FROM {{ ref('stg_order_items') }}

{% if is_incremental() %}
WHERE _airbyte_extracted_at > (SELECT MAX(_airbyte_extracted_at) FROM {{ this }})
{% endif %}
```

### Test Failures

| Test | Failure Cause | Fix |
|------|--------------|-----|
| `not_null` | Null values in column | Investigate upstream null handling |
| `unique` | Duplicate keys | Remove duplicates in staging |
| `relationships` | Orphaned foreign keys | Fix upstream data or use `warn_if` |
| `accepted_range` | Outlier values | Clamp extremes or adjust threshold |
| `recency` | Stale source data | Alert on source pipeline delay |

```bash
# Run tests with verbose output
dbt test --select model_name --store-failures
dbt test --select tag:critical

# Check failure logs
cat target/manifest.json | jq '.results'
```

## 8.2 Performance Tuning

### Model Build Performance

```sql
-- For large fact tables, partition by date
{{ config(
    materialized='incremental',
    partition_by=['date_key'],
    cluster_by=['customer_id', 'product_id'],
    partition_exclude_columns=['raw_payload'],
) }}

-- Use selective columns early
SELECT
    order_id,       -- Only needed columns
    customer_id,
    created_at,
    revenue
FROM wide_source_table   -- Instead of SELECT *

{% if is_incremental() %}
WHERE created_at > (SELECT MAX(created_at) FROM {{ this }})
{% endif %}
```

### Warehouse Optimization

```sql
-- Reduce cost with limit in development
{{ config(
    materialized='table',
    limits:
      dev: 10000
      prod: none
) }}

-- Use pushdown optimization
{{ config(
    materialized='incremental',
    incremental_strategy='delete+insert',
) }}
```

### Common Commands

```bash
# Profile a slow model
dbt run --select slow_model --explain

# Use Slim CI for faster builds
dbt list --select config.materialized:table --output json | jq -r '.[].unique_id' > changed_models.txt
dbt run --select changed_models.txt

# Cache expensive computations
dbt run --select +int_expensive_agg  # Parent dependencies run too

# Parallel execution
dbt run --threads 8
```

## 8.3 Debugging Techniques

### View Compiled SQL

```bash
dbt compile
cat target/compiled/project_name/models/path/model.sql
```

### Use dbt Debug Logging

```bash
# Enable debug logging
export DBT_LOG_LEVEL=debug
dbt run --log-level debug --log-format json

# Check logs
tail -f logs/dbt.log
```

### Source Freshness Issues

```yaml
# sources.yml
sources:
  - name: stripe
    freshness:
      warn_after: {count: 12, period: hour}
      error_after: {count: 24, period: hour}
    loaded_at_field: _airbyte_extracted_at
    tables:
      - name: orders
```

```bash
# Check source freshness
dbt source freshness
dbt source freshness --select source:stripe
```

## 8.4 Known Issues & Fixes

| Issue | Versions | Fix |
|-------|----------|-----|
| `partial_parse` causing stale model graphs | 1.3-1.5 | Set `partial_parse: false` or run `dbt rebuild` |
| `--full-refresh` recreates views | All | Only for `table`/`incremental`; views need `dbt run` |
| `dbt source freshness` timeout on large tables | All | Use `loaded_at_field` with indexed column |
| Cross-database `ref()` in dbt Core | Pre-1.8 | Use `database` in model config |
| Slow `dbt deps` with many packages | 1.4+ | Use `packages.yml` with specific version pins |
| Python models fail on Snowflake | 1.3-1.4 | Pin `dbt-snowflake` to matching minor version |
