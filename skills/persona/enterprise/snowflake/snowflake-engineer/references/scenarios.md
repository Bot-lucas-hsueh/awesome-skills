# Snowflake Engineer Scenario Examples

## Scenario 1: Data Migration from On-Premises

**Context:** Migrate 50TB Oracle data warehouse to Snowflake with minimal downtime.

**Solution Approach:**

```python
# migration_oracle_to_snowflake.py
from snowflake.snowpark import Session
import concurrent.futures

def migrate_table(session: Session, oracle_table: str, snowflake_table: str):
    """
    Migrate single table from Oracle to Snowflake.
    """
    # 1. Extract DDL
    oracle_ddl = get_oracle_ddl(oracle_table)
    
    # 2. Convert to Snowflake DDL
    snowflake_ddl = convert_ddl(oracle_ddl)
    session.sql(snowflake_ddl).collect()
    
    # 3. Create Snowpipe for continuous load
    session.sql(f"""
        CREATE PIPE {snowflake_table}_pipe
        AS
        COPY INTO {snowflake_table}
        FROM @oracle_stage/{oracle_table}
        FILE_FORMAT = (TYPE = CSV)
    """).collect()
    
    # 4. Initial bulk load
    session.sql(f"""
        COPY INTO {snowflake_table}
        FROM @oracle_stage/{oracle_table}/initial
        FILE_FORMAT = (TYPE = CSV)
        ON_ERROR = 'CONTINUE'
    """).collect()
    
    return {"table": snowflake_table, "status": "migrated"}

def run_parallel_migration(tables: list, max_workers: int = 5):
    """
    Migrate multiple tables in parallel.
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(migrate_table, session, tbl, tbl) 
            for tbl in tables
        ]
        results = [f.result() for f in futures]
    return results

# Execution
large_tables = ["sales", "customers", "products", "inventory"]
results = run_parallel_migration(large_tables)
```

**Key Considerations:**
- Use parallel extraction for large tables
- Implement CDC for ongoing sync
- Validate row counts post-migration
- Test query performance before cutover

---

## Scenario 2: Real-Time Fraud Detection

**Context:** Build real-time fraud detection using streaming transactions.

**Solution Approach:**

```sql
-- 1. Create stream on transactions
CREATE OR REPLACE STREAM transaction_stream 
ON TABLE raw.transactions 
APPEND_ONLY = TRUE;

-- 2. Create fraud detection function
CREATE OR REPLACE FUNCTION fraud_score(
    amount NUMBER,
    merchant STRING,
    customer_id STRING,
    transaction_time TIMESTAMP
)
RETURNS NUMBER
LANGUAGE PYTHON
RUNTIME_VERSION = '3.10'
HANDLER = 'calculate_fraud_score'
AS $$
def calculate_fraud_score(amount, merchant, customer_id, transaction_time):
    score = 0
    
    # Rule 1: High amount
    if amount > 10000:
        score += 30
    
    # Rule 2: Off-hours transaction
    hour = transaction_time.hour
    if hour < 6 or hour > 23:
        score += 20
    
    # Rule 3: New merchant
    if merchant in high_risk_merchants:
        score += 25
    
    return min(score, 100)
$$;

-- 3. Create task for real-time scoring
CREATE OR REPLACE TASK fraud_detection_task
  WAREHOUSE = 'fraud_wh'
  SCHEDULE = '1 MINUTE'
  WHEN SYSTEM$STREAM_HAS_DATA('transaction_stream')
AS
  INSERT INTO analytics.fraud_alerts
  SELECT 
    t.transaction_id,
    t.customer_id,
    t.amount,
    fraud_score(t.amount, t.merchant, t.customer_id, t.transaction_time) as risk_score,
    CASE 
      WHEN risk_score >= 80 THEN 'HIGH'
      WHEN risk_score >= 50 THEN 'MEDIUM'
      ELSE 'LOW'
    END as risk_level,
    CURRENT_TIMESTAMP() as detected_at
  FROM transaction_stream t
  WHERE fraud_score(t.amount, t.merchant, t.customer_id, t.transaction_time) >= 50;

-- 4. Enable task
ALTER TASK fraud_detection_task RESUME;
```

**Alert Integration:**
```python
def send_fraud_alert(transaction_id: str, risk_score: int):
    """Send alert for high-risk transactions."""
    if risk_score >= 80:
        # Block transaction immediately
        block_transaction(transaction_id)
        send_sms_alert(f"HIGH RISK: Transaction {transaction_id} blocked")
    elif risk_score >= 50:
        # Flag for review
        add_to_review_queue(transaction_id)
        send_email_alert(f"MEDIUM RISK: Transaction {transaction_id} flagged")
```

---

## Scenario 3: Cross-Region Data Replication

**Context:** Maintain active-active setup across US and EU with data residency compliance.

**Solution Approach:**

```sql
-- US Primary Account

-- 1. Enable replication
CREATE DATABASE global_operations;
ENABLE REPLICATION TO ACCOUNTS aws_us_east;

-- 2. Create replicated tables
CREATE TABLE global_operations.shared.customers (
    customer_id STRING,
    region STRING,
    data_residency STRING,
    -- Other columns
);

-- 3. Apply row-level security for residency
CREATE ROW ACCESS POLICY residency_policy AS (residency STRING) RETURNS BOOLEAN ->
  CASE
    WHEN CURRENT_REGION() = 'AWS_US_EAST_1' AND residency IN ('US', 'GLOBAL') THEN TRUE
    WHEN CURRENT_REGION() = 'AZURE_WESTEUROPE' AND residency IN ('EU', 'GLOBAL') THEN TRUE
    ELSE FALSE
  END;

ALTER TABLE global_operations.shared.customers 
ADD ROW ACCESS POLICY residency_policy ON (data_residency);

-- EU Secondary Account

-- 1. Create replica
CREATE DATABASE global_operations 
AS REPLICA OF aws_us_east.global_operations;

-- 2. Refresh on schedule
CREATE TASK refresh_replica
  SCHEDULE = '5 MINUTE'
AS
  ALTER DATABASE global_operations REFRESH;
```

**Failover Procedure:**
```python
def execute_failover(primary_region: str, target_region: str):
    """
    Execute region failover.
    """
    if primary_region == "US":
        # Promote EU replica to primary
        eu_session.sql("""
            ALTER DATABASE global_operations PRIMARY
        """).collect()
        
        # Update DNS/load balancers
        update_routing(target_region)
        
        # Notify stakeholders
        send_alert(f"Failover complete: {primary_region} -> {target_region}")
    
    return {"status": "failover_complete", "new_primary": target_region}
```

---

## Scenario 4: Data Lakehouse Architecture

**Context:** Implement Iceberg tables for open data lakehouse with Snowflake.

**Solution Approach:**

```sql
-- 1. Create external volume for Iceberg
CREATE OR REPLACE EXTERNAL VOLUME iceberg_volume
  STORAGE_LOCATIONS = (
    (
      NAME = 's3_iceberg'
      STORAGE_PROVIDER = 'S3'
      STORAGE_BASE_URL = 's3://my-data-lake/iceberg/'
      STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::123456789:role/snowflake-iceberg-role'
    )
  );

-- 2. Create Iceberg table
CREATE OR REPLACE ICEBERG TABLE raw_events (
    event_id STRING,
    event_type STRING,
    user_id STRING,
    event_timestamp TIMESTAMP_NTZ,
    properties VARIANT
)
  EXTERNAL_VOLUME = 'iceberg_volume'
  CATALOG = 'SNOWFLAKE'
  BASE_LOCATION = 'events/';

-- 3. Query with Snowflake, share with other engines
INSERT INTO raw_events
SELECT 
    UUID_STRING() as event_id,
    'page_view' as event_type,
    user_id,
    CURRENT_TIMESTAMP() as event_timestamp,
    OBJECT_CONSTRUCT('page', page_url, 'referrer', referrer) as properties
FROM staging.web_events;

-- 4. External tools can read same Iceberg files
-- Athena, Spark, Trino, etc.
```

**Performance Optimization:**
```python
def optimize_iceberg_table(session: Session, table_name: str):
    """
    Optimize Iceberg table for query performance.
    """
    # 1. Rewrite data files for optimal size
    session.sql(f"""
        ALTER ICEBERG TABLE {table_name}
        REWRITE DATA USING BIN_PACK
        WHERE event_timestamp < CURRENT_DATE() - 30
    """).collect()
    
    # 2. Expire old snapshots
    session.sql(f"""
        ALTER ICEBERG TABLE {table_name}
        EXECUTE EXPIRE_SNAPSHOTS
        RETAIN 7 DAYS
    """).collect()
    
    # 3. Remove orphan files
    session.sql(f"""
        ALTER ICEBERG TABLE {table_name}
        EXECUTE REMOVE_ORPHAN_FILES
        RETAIN 7 DAYS
    """).collect()
    
    return {"status": "optimized", "table": table_name}
```

---

## Scenario 5: Dynamic Data Masking

**Context:** Implement column-level security for sensitive PII data.

**Solution Approach:**

```sql
-- 1. Create masking policies
CREATE OR REPLACE MASKING POLICY email_mask AS (val STRING) RETURNS STRING ->
  CASE
    WHEN CURRENT_ROLE() IN ('ADMIN', 'SECURITY_ADMIN') THEN val
    WHEN CURRENT_ROLE() = 'SUPPORT_AGENT' THEN REGEXP_REPLACE(val, '.+@', '***@')
    ELSE '***@***.***'
  END;

CREATE OR REPLACE MASKING POLICY ssn_mask AS (val STRING) RETURNS STRING ->
  CASE
    WHEN CURRENT_ROLE() IN ('ADMIN', 'HR_ADMIN') THEN val
    ELSE CONCAT('XXX-XX-', RIGHT(val, 4))
  END;

CREATE OR REPLACE MASKING POLICY credit_card_mask AS (val STRING) RETURNS STRING ->
  CASE
    WHEN CURRENT_ROLE() IN ('ADMIN', 'BILLING_ADMIN') THEN val
    ELSE CONCAT('****-****-****-', RIGHT(REPLACE(val, '-', ''), 4))
  END;

-- 2. Apply to table
CREATE TABLE customers_secure (
    customer_id STRING,
    email STRING MASKING POLICY email_mask,
    ssn STRING MASKING POLICY ssn_mask,
    credit_card STRING MASKING POLICY credit_card_mask,
    name STRING,
    created_at TIMESTAMP
);

-- 3. Test with different roles
-- As ADMIN: See full data
-- As ANALYST: See masked data
SELECT * FROM customers_secure LIMIT 5;
```

**Row-Level Security:**
```sql
-- Add row-level policy for multi-tenancy
CREATE OR REPLACE ROW ACCESS POLICY tenant_isolation AS (tenant_id STRING) 
RETURNS BOOLEAN ->
  CASE
    WHEN CURRENT_ROLE() = 'ADMIN' THEN TRUE
    WHEN CURRENT_ROLE() = 'TENANT_A_ADMIN' AND tenant_id = 'A' THEN TRUE
    WHEN CURRENT_ROLE() = 'TENANT_B_ADMIN' AND tenant_id = 'B' THEN TRUE
    ELSE FALSE
  END;

ALTER TABLE customers_secure 
ADD ROW ACCESS POLICY tenant_isolation ON (tenant_id);
```

---

## Scenario 6: Cost Optimization Analysis

**Context:** Reduce Snowflake spend by 40% while maintaining performance.

**Solution Approach:**

```python
# cost_analysis.py
from snowflake.snowpark import Session

def analyze_cost_optimization_opportunities(session: Session) -> dict:
    """
    Comprehensive cost optimization analysis.
    """
    recommendations = []
    
    # 1. Identify oversized warehouses
    warehouse_usage = session.sql("""
        SELECT 
            WAREHOUSE_NAME,
            WAREHOUSE_SIZE,
            AVG(EXECUTION_TIME) as avg_exec_time,
            AVG(QUEUED_TIME) as avg_queue_time,
            SUM(CREDITS_USED) as total_credits
        FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY qh
        JOIN SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY wm
          ON qh.WAREHOUSE_ID = wm.WAREHOUSE_ID
        WHERE qh.START_TIME >= DATEADD(day, -30, CURRENT_TIMESTAMP())
        GROUP BY 1, 2
    """).collect()
    
    for wh in warehouse_usage:
        if wh['AVG_QUEUE_TIME'] < 1 and wh['WAREHOUSE_SIZE'] != 'X-SMALL':
            recommendations.append({
                "type": "downsize",
                "warehouse": wh['WAREHOUSE_NAME'],
                "current_size": wh['WAREHOUSE_SIZE'],
                "reason": "Low queue time suggests over-provisioning"
            })
    
    # 2. Find unused warehouses
    unused = session.sql("""
        SELECT 
            WAREHOUSE_NAME,
            MAX(START_TIME) as last_used
        FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY
        WHERE START_TIME >= DATEADD(day, -30, CURRENT_TIMESTAMP())
        GROUP BY 1
        HAVING last_used < DATEADD(day, -7, CURRENT_TIMESTAMP())
    """).collect()
    
    for wh in unused:
        recommendations.append({
            "type": "suspend",
            "warehouse": wh['WAREHOUSE_NAME'],
            "last_used": wh['LAST_USED'],
            "reason": "Not used in 7+ days"
        })
    
    # 3. Storage optimization
    storage = session.sql("""
        SELECT 
            TABLE_SCHEMA,
            TABLE_NAME,
            BYTES / POWER(1024, 3) as gb,
            ROW_COUNT,
            LAST_ALTERED
        FROM SNOWFLAKE.ACCOUNT_USAGE.TABLE_STORAGE_METRICS
        WHERE DELETED = FALSE
          AND LAST_ALTERED < DATEADD(day, -90, CURRENT_TIMESTAMP())
        ORDER BY BYTES DESC
        LIMIT 20
    """).collect()
    
    for tbl in storage:
        if tbl['GB'] > 100:  # > 100GB
            recommendations.append({
                "type": "archive",
                "table": f"{tbl['TABLE_SCHEMA']}.{tbl['TABLE_NAME']}",
                "size_gb": tbl['GB'],
                "reason": "Large table not modified in 90+ days"
            })
    
    return {
        "recommendations": recommendations,
        "estimated_savings": calculate_savings(recommendations)
    }

def implement_optimizations(session: Session, recommendations: list):
    """
    Implement approved optimizations.
    """
    for rec in recommendations:
        if rec['type'] == 'downsize':
            new_size = get_next_smaller_size(rec['current_size'])
            session.sql(f"""
                ALTER WAREHOUSE {rec['warehouse']} 
                SET WAREHOUSE_SIZE = '{new_size}'
            """).collect()
            
        elif rec['type'] == 'suspend':
            session.sql(f"""
                ALTER WAREHOUSE {rec['warehouse']} SUSPEND
            """).collect()
            
        elif rec['type'] == 'archive':
            # Move to cheaper storage or external stage
            session.sql(f"""
                CREATE TABLE {rec['table']}_archive CLONE {rec['table']}
            """).collect()
            session.sql(f"""
                DROP TABLE {rec['table']}
            """).collect()
    
    return {"status": "implemented", "count": len(recommendations)}
```

---

## Scenario 7: ML Model Deployment

**Context:** Deploy customer lifetime value (CLV) prediction model.

**Solution Approach:**

```python
# clv_model.py
from snowflake.snowpark import Session
from snowflake.ml.modeling.xgboost import XGBRegressor
from snowflake.ml.registry import Registry

def train_clv_model(session: Session):
    """
    Train CLV prediction model.
    """
    # 1. Feature engineering
    features = session.sql("""
        SELECT 
            customer_id,
            DATEDIFF(day, first_purchase, CURRENT_DATE()) as customer_tenure_days,
            total_orders,
            total_revenue,
            avg_order_value,
            days_since_last_order,
            number_of_categories,
            total_items,
            -- Target variable
            future_12m_revenue as clv_12m
        FROM features.customer_features
        WHERE first_purchase < DATEADD(day, -365, CURRENT_DATE())
    """)
    
    # 2. Split data
    train_data, test_data = features.random_split(weights=[0.8, 0.2], seed=42)
    
    # 3. Train model
    model = XGBRegressor(
        input_cols=[
            'customer_tenure_days', 'total_orders', 'total_revenue',
            'avg_order_value', 'days_since_last_order', 
            'number_of_categories', 'total_items'
        ],
        label_cols=['clv_12m'],
        max_depth=6,
        learning_rate=0.1,
        n_estimators=100
    )
    
    model.fit(train_data)
    
    # 4. Evaluate
    predictions = model.predict(test_data)
    mae = predictions.select(
        abs(col('clv_12m') - col('predicted_clv_12m')).alias('error')
    ).agg(avg('error')).collect()[0][0]
    
    print(f"Model MAE: {mae}")
    
    # 5. Register model
    registry = Registry(session)
    registry.log_model(
        model=model,
        model_name="clv_predictor",
        version="v1",
        sample_input_data=train_data.limit(100),
        metrics={"mae": mae}
    )
    
    return model

def deploy_clv_predictions(session: Session):
    """
    Deploy predictions to production.
    """
    # Load model
    registry = Registry(session)
    model = registry.get_model("clv_predictor").version("v1")
    
    # Score all active customers
    customers = session.table("features.customer_features").filter(
        col("is_active") == True
    )
    
    predictions = model.run(
        customers,
        function_name="predict"
    )
    
    # Create segments
    segmented = predictions.withColumn(
        "clv_segment",
        when(col("predicted_clv_12m") > 1000, "HIGH")
        .when(col("predicted_clv_12m") > 500, "MEDIUM")
        .otherwise("LOW")
    )
    
    # Store for marketing use
    segmented.write.mode("overwrite").save_as_table("marketing.clv_predictions")
    
    return {"status": "deployed", "customers_scored": segmented.count()}
```

---

## Scenario 8: Compliance and Auditing

**Context:** Implement comprehensive audit trail for SOX compliance.

**Solution Approach:**

```sql
-- 1. Create audit log table
CREATE TABLE audit.data_access_log (
    log_id NUMBER AUTOINCREMENT,
    event_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    user_name STRING,
    role_name STRING,
    database_name STRING,
    schema_name STRING,
    object_name STRING,
    object_type STRING,
    action STRING,
    query_id STRING,
    rows_accessed NUMBER,
    ip_address STRING,
    session_id STRING
);

-- 2. Create access history view
CREATE VIEW audit.comprehensive_access_history AS
SELECT 
    ah.QUERY_ID,
    ah.QUERY_START_TIME,
    ah.USER_NAME,
    ah.ROLE_NAME,
    ah.DIRECT_OBJECTS_ACCESSED,
    ah.BASE_OBJECTS_ACCESSED,
    qh.QUERY_TEXT,
    qh.EXECUTION_TIME,
    qh.WAREHOUSE_NAME
FROM SNOWFLAKE.ACCOUNT_USAGE.ACCESS_HISTORY ah
LEFT JOIN SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY qh
    ON ah.QUERY_ID = qh.QUERY_ID
WHERE ah.QUERY_START_TIME >= DATEADD(day, -90, CURRENT_TIMESTAMP());

-- 3. Create alert for suspicious access
CREATE OR REPLACE ALERT suspicious_access_alert
  WAREHOUSE = 'audit_wh'
  SCHEDULE = '1 HOUR'
IF (
    SELECT COUNT(*) 
    FROM audit.comprehensive_access_history
    WHERE QUERY_START_TIME >= DATEADD(hour, -1, CURRENT_TIMESTAMP())
      AND (DIRECT_OBJECTS_ACCESSED LIKE '%PII%' 
           OR DIRECT_OBJECTS_ACCESSED LIKE '%SSN%')
      AND ROLE_NAME NOT IN ('ADMIN', 'COMPLIANCE_OFFICER')
) > 10
THEN CALL SYSTEM$SEND_EMAIL(
    'security@company.com',
    'Suspicious Data Access Alert',
    'High volume of PII access detected'
);
```

**Audit Report Generation:**
```python
def generate_compliance_report(session: Session, start_date: str, end_date: str):
    """
    Generate SOX compliance report.
    """
    # Data access summary
    access_summary = session.sql(f"""
        SELECT 
            USER_NAME,
            ROLE_NAME,
            COUNT(*) as access_count,
            COUNT(DISTINCT OBJECT_NAME) as unique_objects
        FROM audit.comprehensive_access_history
        WHERE QUERY_START_TIME BETWEEN '{start_date}' AND '{end_date}'
        GROUP BY 1, 2
        ORDER BY access_count DESC
    """).to_pandas()
    
    # Schema changes
    schema_changes = session.sql(f"""
        SELECT 
            QUERY_TEXT,
            USER_NAME,
            QUERY_START_TIME
        FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
        WHERE QUERY_TYPE IN ('CREATE', 'ALTER', 'DROP')
          AND QUERY_START_TIME BETWEEN '{start_date}' AND '{end_date}'
        ORDER BY QUERY_START_TIME
    """).to_pandas()
    
    # Generate report
    report = {
        "period": f"{start_date} to {end_date}",
        "access_summary": access_summary.to_dict(),
        "schema_changes": schema_changes.to_dict(),
        "compliance_status": "PASS" if len(schema_changes) < 100 else "REVIEW"
    }
    
    return report
```
