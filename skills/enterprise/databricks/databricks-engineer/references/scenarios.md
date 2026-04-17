# Databricks Scenario Examples

## Scenario 1: Large-Scale Data Migration

**Context**: Migrate 500TB of historical data from on-premises Hadoop to Databricks Lakehouse.

**Challenge**: Minimize downtime, ensure data integrity, optimize for cost.

**Solution**:

```python
# Phase 1: Parallel extraction from Hadoop
# Use DistCp or Azure Data Factory for bulk transfer

# Phase 2: Convert to Delta Lake with optimization
for table in tables_to_migrate:
    # Read from staged location
    df = spark.read.parquet(f"/mnt/staging/{table}")
    
    # Write optimized Delta
    (df.write
        .format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .saveAsTable(f"bronze.{table}")
    )
    
    # Optimize for query patterns
    spark.sql(f"OPTIMIZE bronze.{table} ZORDER BY (date_key)")
    spark.sql(f"VACUUM bronze.{table} RETAIN 168 HOURS")
    
    # Verify row counts
    source_count = df.count()
    target_count = spark.table(f"bronze.{table}").count()
    assert source_count == target_count, f"Mismatch in {table}"

# Phase 3: Validation and cutover
```

**Results**: 
- Migration time: 72 hours (parallelized)
- Cost: $15K DBUs (using spot instances)
- Zero data loss verified via checksums

---

## Scenario 2: Real-Time Fraud Detection

**Context**: Financial services company needs sub-second fraud detection on 50K transactions/second.

**Architecture**:

```
Kafka → Auto Loader → Bronze → Spark Streaming → MLflow Model → Alert
```

**Implementation**:

```python
# Streaming ingestion with Auto Loader
stream_df = (spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", "/checkpoint/fraud_schema")
    .load("/mnt/transactions/raw/")
)

# Feature engineering
features_df = (stream_df
    .withWatermark("timestamp", "10 minutes")
    .groupBy(
        window("timestamp", "5 minutes"),
        "user_id"
    )
    .agg(
        count("*").alias("tx_count_5m"),
        sum("amount").alias("amount_5m"),
        avg("amount").alias("avg_amount_5m"),
        stddev("amount").alias("std_amount_5m")
    )
)

# Load production model
import mlflow.pyfunc
model_uri = "models:/FraudDetectionModel/Production"
fraud_model = mlflow.pyfunc.load_model(model_uri)

# Apply model (using pandas UDF for low latency)
from pyspark.sql.functions import pandas_udf, PandasUDFType

@pandas_udf('double', PandasUDFType.SCALAR_ITER)
def predict_fraud(iterator):
    for pdf in iterator:
        yield fraud_model.predict(pdf)

# Score transactions
scored_df = features_df.withColumn("fraud_score", predict_fraud(struct(features_df.columns)))

# Alert on high-risk
critical_df = scored_df.filter(col("fraud_score") > 0.8)

# Write to alert queue
(critical_df.writeStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("topic", "fraud-alerts")
    .option("checkpointLocation", "/checkpoint/fraud_alerts")
    .start()
)
```

**Results**:
- Latency: p99 < 500ms
- Throughput: 75K TPS (scaled)
- False positive rate: 0.5%

---

## Scenario 3: Multi-Cloud Data Sharing

**Context**: Share sanitized customer data with partners across AWS and Azure.

**Solution using Delta Sharing**:

```sql
-- Provider side (Databricks on AWS)
CREATE SHARE customer_analytics SHARE AS;

ALTER SHARE customer_analytics ADD TABLE production.sales.aggregated_metrics;
ALTER SHARE customer_analytics ADD TABLE production.marketing.campaign_performance;

-- Create recipient
CREATE RECIPIENT partner_company;

-- Grant access
GRANT SELECT ON SHARE customer_analytics TO RECIPIENT partner_company;

-- Generate activation link (provider sends to recipient)
```

```python
# Recipient side (Databricks on Azure)
# Configure credential file from provider

# Access shared data as if local
spark.read.format("deltaSharing").load("/share/customer_analytics/production.sales.aggregated_metrics").show()
```

**Benefits**:
- No data duplication
- Live access to updates
- Row/column-level security preserved
- Audit trail of all access

---

## Scenario 4: Hyperparameter Tuning at Scale

**Context**: Train 1000 XGBoost models with different hyperparameters for Kaggle competition.

**Solution using Hyperopt and MLflow**:

```python
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
import mlflow
import xgboost as xgb
from sklearn.model_selection import cross_val_score
import numpy as np

# Load data
X = spark.table("gold.features").toPandas()
y = X.pop("target")

# Define search space
space = {
    'max_depth': hp.quniform('max_depth', 3, 10, 1),
    'learning_rate': hp.loguniform('learning_rate', -5, -1),
    'n_estimators': hp.quniform('n_estimators', 50, 500, 10),
    'subsample': hp.uniform('subsample', 0.5, 1.0),
    'colsample_bytree': hp.uniform('colsample_bytree', 0.5, 1.0)
}

def objective(params):
    with mlflow.start_run():
        # Convert params
        params['max_depth'] = int(params['max_depth'])
        params['n_estimators'] = int(params['n_estimators'])
        
        # Log params
        mlflow.log_params(params)
        
        # Train model
        model = xgb.XGBClassifier(**params)
        score = cross_val_score(model, X, y, cv=5, scoring='roc_auc').mean()
        
        # Log metric
        mlflow.log_metric("auc", score)
        
        return {'loss': -score, 'status': STATUS_OK}

# Run optimization
with mlflow.start_run(run_name="hyperopt_xgboost"):
    trials = Trials()
    best = fmin(
        fn=objective,
        space=space,
        algo=tpe.suggest,
        max_evals=100,
        trials=trials
    )
    
    mlflow.log_params({"best_params": best})
    print(f"Best: {best}")

# Retrieve best model
best_run = mlflow.search_runs(
    filter_string="run_name = 'hyperopt_xgboost'",
    order_by=["metrics.auc DESC"]
).iloc[0]

print(f"Best AUC: {best_run['metrics.auc']}")
```

**Results**:
- 1000 experiments tracked automatically
- Best model identified: AUC 0.947
- Total compute time: 4 hours (parallel on 10 workers)

---

## Scenario 5: Disaster Recovery Strategy

**Context**: Ensure business continuity with RPO < 1 hour, RTO < 4 hours.

**Architecture**:

```
Primary Region (us-west-2) → Replication → DR Region (us-east-1)
```

**Implementation**:

```python
# Enable Change Data Feed on critical tables
spark.sql("""
ALTER TABLE production.orders 
SET TBLPROPERTIES (delta.enableChangeDataFeed = true)
""")

# Schedule replication job (runs every 30 minutes)
def replicate_to_dr():
    # Get latest changes using CDF
    changes = (spark.read
        .format("delta")
        .option("readChangeFeed", "true")
        .option("startingVersion", get_last_replicated_version())
        .table("production.orders")
    )
    
    # Apply to DR region
    (changes.write
        .format("delta")
        .mode("append")
        .save("s3://dr-bucket/orders")
    )

# Automated DR testing (weekly)
def test_failover():
    """Verify DR environment can serve queries"""
    dr_count = spark.read.format("delta").load("s3://dr-bucket/orders").count()
    primary_count = spark.table("production.orders").count()
    
    assert dr_count >= primary_count * 0.99, "DR lag exceeds 1%"
    print(f"✓ DR healthy: {dr_count}/{primary_count} records")

# Backup with time travel
weekly_backup = """
CREATE TABLE IF NOT EXISTS backup.orders_weekly
USING DELTA
AS SELECT * FROM production.orders TIMESTAMP AS OF date_sub(current_date(), 7)
"""
```

**Recovery Procedures**:

```sql
-- Scenario: Primary region down
-- Step 1: Promote DR to primary
ALTER TABLE dr_catalog.orders RECREATE AS production.orders;

-- Step 2: Redirect applications
-- (Update connection strings in application config)

-- Step 3: Verify data integrity
SELECT COUNT(*) FROM production.orders;
SELECT MAX(updated_at) FROM production.orders;
```

**Results**:
- RPO: 15 minutes (continuous replication)
- RTO: 2 hours (tested monthly)
- Data integrity: 100% verified
