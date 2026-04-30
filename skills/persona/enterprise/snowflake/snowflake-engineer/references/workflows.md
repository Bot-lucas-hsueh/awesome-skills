# Snowflake Engineer Workflows

## Standard ETL Workflow

### Phase 1: Data Ingestion

```python
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col, to_timestamp

def ingest_raw_data(session: Session, source_path: str, target_table: str) -> dict:
    """
    Standard raw data ingestion workflow.
    """
    # 1. Scale up for ingestion
    session.sql("ALTER WAREHOUSE etl_wh SET WAREHOUSE_SIZE = LARGE").collect()
    
    # 2. Read source data
    raw_df = session.read.option("compression", "gzip").parquet(source_path)
    
    # 3. Add metadata columns
    enriched_df = raw_df.withColumn("_ingested_at", current_timestamp()) \
                       .withColumn("_source_file", input_file_name())
    
    # 4. Write to raw layer
    enriched_df.write.mode("append").save_as_table(f"raw.{target_table}")
    
    # 5. Scale down
    session.sql("ALTER WAREHOUSE etl_wh SET WAREHOUSE_SIZE = SMALL").collect()
    
    return {
        "status": "success",
        "rows_inserted": enriched_df.count(),
        "target_table": target_table
    }
```

### Phase 2: Data Transformation

```python
def transform_to_clean(session: Session, source_table: str, target_table: str) -> dict:
    """
    Transform raw data to clean layer with validation.
    """
    # 1. Read raw data
    raw_df = session.table(f"raw.{source_table}")
    
    # 2. Apply transformations
    clean_df = raw_df.select(
        col("transaction_id").cast("STRING").alias("transaction_id"),
        to_timestamp(col("timestamp")).alias("event_timestamp"),
        col("amount").cast("DECIMAL(18,4)").alias("amount"),
        upper(col("currency")).alias("currency"),
        col("_ingested_at")
    ).filter(
        col("transaction_id").is_not_null() &
        col("amount").is_not_null()
    )
    
    # 3. Data quality checks
    quality_metrics = session.sql(f"""
        SELECT 
            COUNT(*) as total_rows,
            COUNT(DISTINCT transaction_id) as unique_ids,
            SUM(CASE WHEN amount < 0 THEN 1 ELSE 0 END) as negative_amounts
        FROM clean.{target_table}
    """).collect()[0]
    
    if quality_metrics['NEGATIVE_AMOUNTS'] > 0:
        raise ValueError("Data quality check failed: Negative amounts found")
    
    # 4. Write to clean layer
    clean_df.write.mode("overwrite").save_as_table(f"clean.{target_table}")
    
    return {
        "status": "success",
        "rows_processed": quality_metrics['TOTAL_ROWS'],
        "unique_ids": quality_metrics['UNIQUE_IDS']
    }
```

### Phase 3: Aggregation

```sql
-- Create materialized view for aggregated metrics
CREATE OR REPLACE MATERIALIZED VIEW curated.daily_metrics AS
SELECT 
    date_trunc('day', event_timestamp) as day,
    currency,
    COUNT(*) as transaction_count,
    SUM(amount) as total_amount,
    AVG(amount) as avg_amount,
    MIN(amount) as min_amount,
    MAX(amount) as max_amount
FROM clean.transactions
GROUP BY 1, 2;

-- Schedule refresh
CREATE OR REPLACE TASK refresh_daily_metrics
  WAREHOUSE = 'etl_wh'
  SCHEDULE = 'USING CRON 0 6 * * * UTC'  -- 6 AM daily
AS
  ALTER MATERIALIZED VIEW curated.daily_metrics RESUME;
```

## Development Workflow

### Local Development

```python
# development.py - Local development helper
from snowflake.snowpark import Session
import os

def get_dev_session() -> Session:
    """Create development session with X-Small warehouse."""
    connection_parameters = {
        "account": os.getenv("SNOWFLAKE_ACCOUNT"),
        "user": os.getenv("SNOWFLAKE_USER"),
        "password": os.getenv("SNOWFLAKE_PASSWORD"),
        "role": "DEVELOPER",
        "warehouse": "DEV_WH",
        "database": "DEV_DB",
        "schema": "EXPERIMENTAL"
    }
    return Session.builder.configs(connection_parameters).create()

def test_transformation(session: Session, query: str) -> DataFrame:
    """Test transformation with sample data."""
    # Use LIMIT for quick testing
    return session.sql(query).limit(100)
```

### Testing Workflow

```python
# test_etl.py - Unit tests for ETL
import pytest
from snowflake.snowpark import Session

class TestETLTransforms:
    @pytest.fixture
    def session(self):
        return get_dev_session()
    
    def test_data_quality(self, session):
        """Test data quality rules."""
        df = session.table("clean.transactions")
        
        # No null transaction IDs
        null_count = df.filter(col("transaction_id").is_null()).count()
        assert null_count == 0, "Found null transaction IDs"
        
        # Amounts should be positive
        negative_count = df.filter(col("amount") < 0).count()
        assert negative_count == 0, "Found negative amounts"
    
    def test_transformation_logic(self, session):
        """Test business logic."""
        result = session.sql("""
            SELECT SUM(amount) as total
            FROM clean.transactions
            WHERE event_timestamp >= '2024-01-01'
        """).collect()
        
        assert result[0]['TOTAL'] > 0, "Total amount should be positive"
```

### Deployment Workflow

```bash
#!/bin/bash
# deploy.sh - Deployment script

ENV=$1
VERSION=$2

if [ -z "$ENV" ] || [ -z "$VERSION" ]; then
    echo "Usage: deploy.sh <env> <version>"
    exit 1
fi

# Run tests
echo "Running tests..."
pytest tests/ --env=$ENV
if [ $? -ne 0 ]; then
    echo "Tests failed!"
    exit 1
fi

# Deploy objects
echo "Deploying to $ENV..."
snowsql -f deploy/$ENV/schema_changes.sql
snowsql -f deploy/$ENV/procedures.sql

# Verify deployment
echo "Verifying deployment..."
snowsql -f deploy/$ENV/verification.sql

echo "Deployment complete!"
```

## Incident Response Workflow

### Detection

```sql
-- Monitor for anomalies
CREATE OR REPLACE TASK incident_detection
  WAREHOUSE = 'monitoring_wh'
  SCHEDULE = '5 MINUTE'
AS
DECLARE
  avg_credits NUMBER;
  current_credits NUMBER;
BEGIN
  -- Get average credits for this hour over past 7 days
  SELECT AVG(CREDITS_USED) INTO avg_credits
  FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
  WHERE START_TIME >= DATEADD(day, -7, CURRENT_TIMESTAMP())
    AND HOUR(START_TIME) = HOUR(CURRENT_TIMESTAMP());
  
  -- Get current hour credits
  SELECT SUM(CREDITS_USED) INTO current_credits
  FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
  WHERE START_TIME >= DATEADD(hour, -1, CURRENT_TIMESTAMP());
  
  -- Alert if 3x normal
  IF (current_credits > avg_credits * 3) THEN
    -- Send alert (integrate with PagerDuty/Slack)
    CALL SYSTEM$SEND_EMAIL(
      'alert@company.com',
      'Snowflake Credit Spike',
      'Credits usage is ' || current_credits || ' vs avg ' || avg_credits
    );
  END IF;
END;
```

### Response

```python
# incident_response.py
def handle_credit_spike(session: Session, warehouse_name: str):
    """
    Automated incident response for credit spike.
    """
    # 1. Identify culprit queries
    culprit_queries = session.sql(f"""
        SELECT 
            QUERY_ID,
            USER_NAME,
            EXECUTION_TIME / 1000 as seconds,
            CREDITS_USED,
            QUERY_TEXT
        FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
        WHERE WAREHOUSE_NAME = '{warehouse_name}'
          AND START_TIME >= DATEADD(minute, -30, CURRENT_TIMESTAMP())
        ORDER BY CREDITS_USED DESC
        LIMIT 10
    """).collect()
    
    # 2. Kill long-running queries if necessary
    for query in culprit_queries:
        if query['SECONDS'] > 600:  # > 10 minutes
            session.sql(f"SELECT SYSTEM$CANCEL_QUERY('{query['QUERY_ID']}')").collect()
    
    # 3. Suspend warehouse temporarily
    session.sql(f"ALTER WAREHOUSE {warehouse_name} SUSPEND").collect()
    
    # 4. Notify team
    send_alert("Credit spike detected", culprit_queries)
    
    return {"action": "warehouse_suspended", "queries_killed": len(culprit_queries)}
```

### Post-Incident

```sql
-- Generate incident report
CREATE OR REPLACE PROCEDURE generate_incident_report(
    start_time TIMESTAMP,
    end_time TIMESTAMP
)
RETURNS STRING
LANGUAGE SQL
AS
$$
DECLARE
    report STRING;
BEGIN
    SELECT 
        'Incident Report\n' ||
        '==============\n\n' ||
        'Duration: ' || :start_time || ' to ' || :end_time || '\n' ||
        'Total Queries: ' || COUNT(*) || '\n' ||
        'Failed Queries: ' || SUM(CASE WHEN ERROR_CODE IS NOT NULL THEN 1 ELSE 0 END) || '\n' ||
        'Total Credits: ' || ROUND(SUM(CREDITS_USED), 2) || '\n' ||
        'Top User: ' || USER_NAME
    INTO report
    FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
    WHERE START_TIME BETWEEN :start_time AND :end_time;
    
    RETURN report;
END;
$$;
```

## Data Sharing Workflow

### Provider Setup

```sql
-- 1. Create share
CREATE SHARE customer_analytics_share;

-- 2. Grant privileges
GRANT USAGE ON DATABASE analytics TO SHARE customer_analytics_share;
GRANT USAGE ON SCHEMA analytics.public TO SHARE customer_analytics_share;
GRANT SELECT ON VIEW analytics.customer_summary TO SHARE customer_analytics_share;

-- 3. Add consumer
ALTER SHARE customer_analytics_share 
ADD ACCOUNTS = partner_snowflake_account;

-- 4. Secure view with row filtering
CREATE SECURE VIEW analytics.customer_summary AS
SELECT 
    customer_id,
    region,
    total_spend,
    last_purchase_date
FROM internal.customers
WHERE region IN (SELECT allowed_regions FROM user_permissions 
                 WHERE user_name = CURRENT_USER());
```

### Consumer Setup

```sql
-- 1. Create database from share
CREATE DATABASE partner_analytics 
FROM SHARE provider_account.customer_analytics_share;

-- 2. Grant access
GRANT IMPORTED PRIVILEGES ON DATABASE partner_analytics TO ROLE analyst;

-- 3. Query shared data
SELECT * FROM partner_analytics.public.customer_summary;
```

## Performance Tuning Workflow

### Identify Slow Queries

```sql
-- Find queries to optimize
SELECT 
    QUERY_ID,
    QUERY_TEXT,
    EXECUTION_TIME / 1000 as seconds,
    BYTES_SCANNED / POWER(1024, 3) as gb_scanned,
    PARTITIONS_SCANNED,
    PARTITIONS_TOTAL,
    (PARTITIONS_SCANNED / NULLIF(PARTITIONS_TOTAL, 0)) * 100 as scan_pct
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
WHERE EXECUTION_TIME > 60000  -- > 1 minute
  AND BYTES_SCANNED > 0
  AND START_TIME >= DATEADD(day, -7, CURRENT_TIMESTAMP())
ORDER BY EXECUTION_TIME DESC
LIMIT 20;
```

### Optimization Steps

```python
def optimize_table(session: Session, table_name: str):
    """
    Systematic table optimization workflow.
    """
    # 1. Analyze current clustering
    clustering_info = session.sql(f"""
        SELECT 
            SYSTEM$CLUSTERING_INFORMATION('{table_name}')
    """).collect()[0][0]
    
    # 2. Check partition pruning effectiveness
    pruning_ratio = session.sql(f"""
        SELECT 
            AVG(PARTITIONS_SCANNED / PARTITIONS_TOTAL) as avg_scan_ratio
        FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
        WHERE TABLE_NAME = '{table_name}'
          AND START_TIME >= DATEADD(day, -7, CURRENT_TIMESTAMP())
    """).collect()[0]['AVG_SCAN_RATIO']
    
    recommendations = []
    
    # 3. Recommend clustering if needed
    if pruning_ratio and pruning_ratio > 0.5:
        recommendations.append(f"Add clustering key to {table_name}")
    
    # 4. Check table size for materialized view
    table_size = session.sql(f"""
        SELECT BYTES / POWER(1024, 3) as gb
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_NAME = '{table_name}'
    """).collect()[0]['GB']
    
    if table_size > 100:  # > 100GB
        recommendations.append(f"Consider materialized views for {table_name}")
    
    return recommendations
```
