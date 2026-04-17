# Databricks Standards & Reference

## 7.1 Official Documentation

- [Databricks Documentation](https://docs.databricks.com/)
- [Delta Lake Documentation](https://docs.delta.io/)
- [MLflow Documentation](https://mlflow.org/docs/latest/)
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [Unity Catalog Guide](https://docs.databricks.com/en/data-governance/unity-catalog/index.html)

## 7.2 Delta Lake Best Practices

### File Size Optimization
```sql
-- Target 128MB-1GB per file
OPTIMIZE table_name ZORDER BY (column1, column2);

-- Set auto-optimization
ALTER TABLE table_name SET TBLPROPERTIES (
    'delta.autoOptimize.optimizeWrite' = 'true',
    'delta.autoOptimize.autoCompact' = 'true'
);
```

### Time Travel Queries
```sql
-- Query as of version
SELECT * FROM table_name VERSION AS OF 10;

-- Query as of timestamp
SELECT * FROM table_name TIMESTAMP AS OF '2025-01-01';

-- Restore table to version
RESTORE TABLE table_name TO VERSION AS OF 10;
```

### Constraints and Validation
```sql
-- Add check constraint
ALTER TABLE table_name ADD CONSTRAINT valid_price CHECK (price > 0);

-- Add NOT NULL constraint
ALTER TABLE table_name ALTER COLUMN id SET NOT NULL;

-- View constraints
DESCRIBE EXTENDED table_name;
```

## 7.3 Spark Configurations for Databricks

### Performance Tuning
```python
# Adaptive Query Execution
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

# Shuffle optimization
spark.conf.set("spark.sql.shuffle.partitions", "400")
spark.conf.set("spark.sql.adaptive.advisoryPartitionSizeInBytes", "128MB")

# Broadcast joins
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "100MB")

# Off-heap memory (for large shuffles)
spark.conf.set("spark.memory.offHeap.enabled", "true")
spark.conf.set("spark.memory.offHeap.size", "20g")
```

### Photon Engine
```python
# Photon is enabled by default on DBR 9.1+
# Verify Photon usage in Spark UI SQL tab (look for "Photon" indicator)

# Disable if needed (not recommended)
spark.conf.set("spark.databricks.photon.enabled", "false")
```

## 7.4 Unity Catalog SQL Reference

### Catalog Management
```sql
-- Create catalog
CREATE CATALOG IF NOT EXISTS production;

-- Set default catalog
USE CATALOG production;

-- Show all catalogs
SHOW CATALOGS;

-- Describe catalog
DESCRIBE CATALOG EXTENDED production;
```

### Schema and Table Management
```sql
-- Create schema
CREATE SCHEMA IF NOT EXISTS production.sales
COMMENT 'Sales data schema'
WITH DBPROPERTIES ('team' = 'revenue');

-- Create managed table
CREATE TABLE production.sales.transactions (
    id STRING,
    amount DECIMAL(18,2),
    created_at TIMESTAMP
) USING DELTA;

-- Create external table
CREATE TABLE production.sales.external_data
USING DELTA
LOCATION 's3://bucket/path/';
```

### Access Control
```sql
-- Grant privileges
GRANT SELECT ON TABLE production.sales.transactions TO DATA_ANALYSTS;
GRANT ALL PRIVILEGES ON SCHEMA production.sales TO DATA_ENGINEERS;

-- Row-level security
CREATE FUNCTION production.sales.region_filter()
RETURN BOOLEAN
RETURN CASE 
    WHEN current_user() IN ('admin@company.com') THEN TRUE
    ELSE region = current_region()
END;

ALTER TABLE production.sales.transactions 
SET ROW FILTER production.sales.region_filter ON (region);
```

## 7.5 MLflow on Databricks

### Experiment Tracking
```python
import mlflow

# Set experiment
mlflow.set_experiment("/Shared/experiments/fraud-detection")

# Start run with context manager
with mlflow.start_run(run_name="xgboost_model") as run:
    # Log parameters
    mlflow.log_params({
        "max_depth": 6,
        "learning_rate": 0.1,
        "n_estimators": 100
    })
    
    # Log metrics
    mlflow.log_metrics({
        "accuracy": 0.95,
        "precision": 0.92,
        "recall": 0.89
    })
    
    # Log model
    mlflow.sklearn.log_model(model, "model")
    
    # Log artifacts
    mlflow.log_artifact("confusion_matrix.png")
```

### Model Registry
```python
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Register model
model_uri = f"runs:/{run.info.run_id}/model"
model_details = mlflow.register_model(model_uri, "FraudDetectionModel")

# Transition stages
client.transition_model_version_stage(
    name="FraudDetectionModel",
    version=model_details.version,
    stage="Staging"
)

# Add model description
client.update_model_version(
    name="FraudDetectionModel",
    version=model_details.version,
    description="XGBoost model for fraud detection with 95% accuracy"
)
```

## 7.6 Cost Optimization Queries

### Monitor Usage
```sql
-- Check billable usage
SELECT 
    usage_date,
    sku_name,
    SUM(usage_quantity) as dbu_consumed,
    SUM(usage_quantity * list_price) as estimated_cost
FROM system.billing.usage
WHERE usage_date >= current_date() - 30
GROUP BY 1, 2
ORDER BY 1 DESC;

-- Top expensive queries
SELECT 
    query_id,
    user_name,
    execution_time_ms / 1000 as execution_time_sec,
    total_task_time_ms / 1000 as total_task_time_sec,
    read_bytes / 1024 / 1024 / 1024 as read_gb
FROM system.query.history
WHERE start_time >= current_date() - 7
ORDER BY total_task_time_ms DESC
LIMIT 20;
```

### Cluster Efficiency
```sql
-- Cluster utilization
SELECT 
    cluster_id,
    cluster_name,
    AVG(executor_cores * num_executors) as avg_cores,
    AVG(memory_bytes / 1024 / 1024 / 1024) as avg_memory_gb
FROM system.compute.cluster_events
WHERE event_time >= current_date() - 7
GROUP BY 1, 2;
```
