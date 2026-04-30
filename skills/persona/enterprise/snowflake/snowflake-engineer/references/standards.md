# Snowflake Engineer Standards Reference

## Performance Standards

### Query Performance Targets

| Metric | Acceptable | Good | Excellent |
|--------|-----------|------|-----------|
| Simple SELECT | < 1s | < 500ms | < 100ms |
| Complex JOIN | < 10s | < 5s | < 2s |
| Aggregation | < 30s | < 10s | < 5s |
| ETL Load (1M rows) | < 5min | < 2min | < 1min |
| BI Dashboard | < 3s | < 1s | < 500ms |

### Warehouse Sizing Guidelines

**By Workload Type:**

| Workload | Recommended Size | Scaling |
|----------|-----------------|---------|
| Development | X-Small | Static |
| Light Analytics | Small | 1-3 clusters |
| Standard ETL | Medium → Large | 1-5 clusters |
| Heavy Analytics | Large | 1-10 clusters |
| Data Science | X-Large | On-demand |
| Enterprise ETL | 2X-Large+ | Scheduled |

### Storage Efficiency Standards

- **Compression Ratio**: Target 5:1 minimum
- **Micro-partition Size**: 50-500MB uncompressed
- **Time Travel Retention**: 1 day (dev), 7 days (prod), 90 days (compliance)
- **Fail-safe Period**: 7 days (fixed)

## Code Quality Standards

### SQL Style Guide

```sql
-- Use uppercase for keywords
SELECT 
    column_a,
    column_b,
    column_c
FROM schema.table
WHERE condition = TRUE
    AND date_column >= '2024-01-01'
ORDER BY column_a DESC
LIMIT 100;

-- Use descriptive aliases
SELECT 
    c.customer_id,
    c.customer_name,
    SUM(s.sales_amount) AS total_sales
FROM customers c
LEFT JOIN sales s ON c.customer_id = s.customer_id
GROUP BY 1, 2;
```

### Snowpark Python Standards

```python
# Use type hints
def process_data(session: Session, table_name: str) -> DataFrame:
    """Process data with proper typing."""
    return session.table(table_name).filter(col("status") == "active")

# Vectorized operations preferred
def calculate_vectorized(prices: pd.Series, quantities: pd.Series) -> pd.Series:
    """Use vectorized operations for performance."""
    return prices * quantities  # Vectorized
    # NOT: [p * q for p, q in zip(prices, quantities)]  # Slow

# Error handling
def robust_etl(session: Session) -> dict:
    """ETL with comprehensive error handling."""
    try:
        result = run_transformation(session)
        return {"status": "success", "rows": result}
    except Exception as e:
        log_error(session, str(e))
        raise
```

## Security Standards

### Role Hierarchy

```
ACCOUNTADMIN (break-glass only)
    └── SYSADMIN
            └── SECURITYADMIN
                    ├── USERADMIN
                    ├── custom_roles
                    │       └── object_privileges
                    └── resource_monitors
```

### Network Security

| Feature | Dev | Staging | Production |
|---------|-----|---------|------------|
| IP Whitelisting | Optional | Required | Required |
| PrivateLink | Optional | Recommended | Required |
| Key Pair Auth | Optional | Required | Required |
| MFA | Recommended | Required | Required |

### Data Classification

```sql
-- Apply tags for data governance
ALTER TABLE customers 
SET TAG data_classification = 'PII';

ALTER TABLE customers 
SET TAG retention_days = '2555';  -- 7 years

-- Column-level masking
ALTER TABLE customers 
MODIFY COLUMN ssn 
SET MASKING POLICY ssn_mask;
```

## Operational Standards

### Monitoring Requirements

```sql
-- Essential monitoring queries

-- Credit consumption by warehouse
SELECT 
    WAREHOUSE_NAME,
    SUM(CREDITS_USED) as total_credits,
    AVG(CREDITS_USED) as avg_daily_credits
FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
WHERE START_TIME >= DATEADD(day, -7, CURRENT_TIMESTAMP())
GROUP BY 1
ORDER BY 2 DESC;

-- Long-running queries
SELECT 
    QUERY_ID,
    USER_NAME,
    EXECUTION_TIME / 1000 as seconds,
    QUERY_TEXT
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE EXECUTION_TIME > 300000  -- >5 min
  AND START_TIME >= DATEADD(day, -1, CURRENT_TIMESTAMP())
ORDER BY EXECUTION_TIME DESC;

-- Storage growth
SELECT 
    TABLE_SCHEMA,
    TABLE_NAME,
    BYTES / POWER(1024, 3) as gb,
    ROW_COUNT
FROM SNOWFLAKE.ACCOUNT_USAGE.TABLE_STORAGE_METRICS
WHERE DELETED = FALSE
ORDER BY BYTES DESC
LIMIT 20;
```

### Alert Thresholds

| Metric | Warning | Critical | Action |
|--------|---------|----------|--------|
| Daily Credits | 80% of budget | 100% of budget | Suspend/Notify |
| Query Time | > 5 min | > 15 min | Kill/Optimize |
| Queue Depth | > 10 | > 50 | Scale cluster |
| Storage | 80% of quota | 95% of quota | Archive/Delete |
| Failed Logins | > 10/hour | > 50/hour | Investigate/Block |

## Change Management

### Deployment Checklist

- [ ] Changes tested in dev environment
- [ ] Performance impact assessed
- [ ] Rollback plan documented
- [ ] Stakeholders notified
- [ ] Monitoring configured
- [ ] Runbooks updated

### Version Control

```bash
# Use semantic versioning for objects
# V1.0.0 - Initial release
# V1.1.0 - Feature addition
# V1.1.1 - Bug fix

# Naming convention
# Tables: domain_entity_v1
# Views: domain_purpose_v1
# Procedures: action_entity_v1
```

## Cost Management Standards

### Budget Allocation

| Environment | Budget % | Monitoring |
|-------------|----------|------------|
| Production | 70% | Daily review |
| Staging | 20% | Weekly review |
| Development | 10% | Monthly review |

### Optimization Requirements

1. **Auto-suspend**: ≤ 5 minutes on all warehouses
2. **Multi-cluster**: Economy policy for cost-sensitive
3. **Storage**: Review >90 days old data quarterly
4. **Time Travel**: Minimum required for compliance
5. **Clones**: Clean up after 30 days
