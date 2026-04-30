# Databricks Standard Workflows

## 8.1 Medallion Architecture Implementation

### Bronze Layer (Raw Ingestion)

```python
# Auto Loader for cloud file ingestion
bronze_df = (spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", "/checkpoint/bronze_schema")
    .option("cloudFiles.inferColumnTypes", "true")
    .option("cloudFiles.schemaEvolutionMode", "rescue")
    .load("/mnt/raw/events/")
    .withColumn("_ingestion_timestamp", current_timestamp())
    .withColumn("_source_filename", input_file_name())
)

# Write to Bronze Delta table
(bronze_df.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", "/checkpoint/bronze_events")
    .trigger(availableNow=True)
    .table("bronze.events")
)
```

### Silver Layer (Cleaned & Validated)

```python
from pyspark.sql.functions import *
from delta.tables import DeltaTable

# Read Bronze
bronze_df = spark.readStream.table("bronze.events")

# Clean and validate
silver_df = (bronze_df
    .filter(col("user_id").isNotNull())  # Remove invalid records
    .withColumn("event_date", to_date(col("timestamp")))
    .withColumn("cleaned_json", from_json(col("payload"), schema))
    .dropDuplicates(["event_id"])  # Deduplication
    .select(
        "event_id",
        "user_id",
        "event_type",
        "event_date",
        "timestamp",
        "cleaned_json.*",
        "_ingestion_timestamp"
    )
)

# Merge to Silver (CDC pattern)
def upsert_to_silver(microBatchDF, batchId):
    microBatchDF.createOrReplaceTempView("silver_updates")
    
    microBatchDF._jdf.sparkSession().sql("""
        MERGE INTO silver.events t
        USING silver_updates s
        ON t.event_id = s.event_id
        WHEN MATCHED THEN UPDATE SET *
        WHEN NOT MATCHED THEN INSERT *
    """)

(silver_df.writeStream
    .foreachBatch(upsert_to_silver)
    .option("checkpointLocation", "/checkpoint/silver_events")
    .trigger(availableNow=True)
    .start()
)
```

### Gold Layer (Business Aggregates)

```python
# Daily user activity summary
daily_summary = (spark.table("silver.events")
    .groupBy(
        col("user_id"),
        col("event_date")
    )
    .agg(
        count("*").alias("event_count"),
        countDistinct("event_type").alias("unique_event_types"),
        sum(when(col("event_type") == "purchase", 1).otherwise(0)).alias("purchases"),
        max("timestamp").alias("last_activity")
    )
)

# Write to Gold with OPTIMIZE
(daily_summary.write
    .format("delta")
    .mode("overwrite")
    .partitionBy("event_date")
    .saveAsTable("gold.daily_user_activity")
)

# Z-order for query performance
spark.sql("OPTIMIZE gold.daily_user_activity ZORDER BY (user_id)")
```

## 8.2 Delta Live Tables Pipeline

```python
import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Bronze layer with DLT
@dlt.table(
    name="bronze_orders",
    comment="Raw orders from source systems"
)
@dlt.expect("valid_order_id", "order_id IS NOT NULL")
def bronze_orders():
    return (spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load("/mnt/raw/orders/")
        .withColumn("_ingestion_time", current_timestamp())
    )

# Silver layer with quality expectations
@dlt.table(
    name="silver_orders",
    comment="Cleaned and validated orders"
)
@dlt.expect_all({
    "valid_amount": "amount > 0",
    "valid_customer": "customer_id IS NOT NULL",
    "valid_status": "status IN ('pending', 'completed', 'cancelled')"
})
def silver_orders():
    return (dlt.read("bronze_orders")
        .filter(col("_ingestion_time") > current_date() - 30)
        .dropDuplicates(["order_id"])
        .select(
            "order_id",
            "customer_id",
            "amount",
            "status",
            "created_at",
            "_ingestion_time"
        )
    )

# Gold layer aggregation
@dlt.table(
    name="gold_daily_revenue",
    comment="Daily revenue summary"
)
def gold_daily_revenue():
    return (dlt.read("silver_orders")
        .groupBy(
            date_trunc("day", "created_at").alias("date")
        )
        .agg(
            sum("amount").alias("total_revenue"),
            count("*").alias("order_count"),
            countDistinct("customer_id").alias("unique_customers")
        )
    )
```

## 8.3 MLflow Model Development Workflow

```python
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd

# Load feature data
features_df = spark.table("gold.customer_features").toPandas()
X = features_df.drop("churned", axis=1)
y = features_df["churned"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Set experiment
mlflow.set_experiment("/Shared/churn-prediction")

# Start run
with mlflow.start_run(run_name="rf_baseline") as run:
    # Log parameters
    params = {
        "n_estimators": 100,
        "max_depth": 10,
        "random_state": 42
    }
    mlflow.log_params(params)
    
    # Train model
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)
    
    # Evaluate
    predictions = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "f1_score": f1_score(y_test, predictions)
    }
    mlflow.log_metrics(metrics)
    
    # Log feature importance
    importance_df = pd.DataFrame({
        "feature": X.columns,
        "importance": model.feature_importances_
    }).sort_values("importance", ascending=False)
    
    importance_df.to_csv("feature_importance.csv", index=False)
    mlflow.log_artifact("feature_importance.csv")
    
    # Log model with signature
    from mlflow.models.signature import infer_signature
    signature = infer_signature(X_train, model.predict(X_train))
    
    mlflow.sklearn.log_model(
        model,
        "model",
        signature=signature,
        input_example=X_train.iloc[:5],
        registered_model_name="ChurnPredictionModel"
    )
    
    print(f"Run ID: {run.info.run_id}")
    print(f"Metrics: {metrics}")
```

## 8.4 Unity Catalog Migration Workflow

### Step 1: Discovery
```python
# List all tables in Hive metastore
tables = spark.catalog.listTables("default")
for table in tables:
    print(f"Table: {table.name}, Type: {table.tableType}")

# Analyze table sizes
for table in tables:
    df = spark.table(f"default.{table.name}")
    size_gb = df.count() * len(df.columns) * 100 / 1024**3  # Rough estimate
    print(f"{table.name}: ~{size_gb:.2f} GB")
```

### Step 2: Create Catalog Structure
```sql
-- Create environment catalogs
CREATE CATALOG IF NOT EXISTS production COMMENT 'Production workloads';
CREATE CATALOG IF NOT EXISTS staging COMMENT 'Pre-production testing';
CREATE CATALOG IF NOT EXISTS development COMMENT 'Development and experimentation';

-- Create schemas
CREATE SCHEMA IF NOT EXISTS production.sales;
CREATE SCHEMA IF NOT EXISTS production.marketing;
CREATE SCHEMA IF NOT EXISTS production.operations;
```

### Step 3: Sync External Tables
```sql
-- Create external table pointing to existing Delta files
CREATE TABLE IF NOT EXISTS production.sales.transactions
USING DELTA
LOCATION 's3://company-data-lake/production/sales/transactions/';

-- Verify data
SELECT COUNT(*) FROM production.sales.transactions;
```

### Step 4: Set Up Governance
```sql
-- Create groups (via admin console or API)
-- Apply access controls

GRANT USAGE ON CATALOG production TO GROUP data_analysts;
GRANT SELECT ON SCHEMA production.sales TO GROUP data_analysts;

GRANT ALL PRIVILEGES ON CATALOG production TO GROUP data_engineers;

-- Row-level security for sensitive data
CREATE FUNCTION production.sales.region_access()
RETURN BOOLEAN
RETURN CASE 
    WHEN is_member('global_admins') THEN TRUE
    ELSE region = current_region()
END;

ALTER TABLE production.sales.transactions 
SET ROW FILTER production.sales.region_access ON (region);
```

## 8.5 Cost Monitoring Workflow

```python
# Weekly cost report
weekly_costs = spark.sql("""
SELECT 
    date_trunc('week', usage_date) as week,
    sku_name,
    SUM(usage_quantity) as dbu_consumed,
    SUM(usage_quantity * list_price) as estimated_cost_usd
FROM system.billing.usage
WHERE usage_date >= current_date() - 90
GROUP BY 1, 2
ORDER BY 1 DESC, 4 DESC
""")

weekly_costs.display()

# Alert on anomalous spend
anomalies = spark.sql("""
WITH daily_costs AS (
    SELECT 
        usage_date,
        SUM(usage_quantity * list_price) as daily_cost
    FROM system.billing.usage
    WHERE usage_date >= current_date() - 30
    GROUP BY 1
),
stats AS (
    SELECT 
        AVG(daily_cost) as avg_cost,
        STDDEV(daily_cost) as stddev_cost
    FROM daily_costs
)
SELECT 
    d.*,
    s.avg_cost,
    (d.daily_cost - s.avg_cost) / s.stddev_cost as z_score
FROM daily_costs d
CROSS JOIN stats s
WHERE d.daily_cost > s.avg_cost + 2 * s.stddev_cost
ORDER BY d.usage_date DESC
""")

if anomalies.count() > 0:
    print("⚠️ Anomalous spend detected!")
    anomalies.display()
```
