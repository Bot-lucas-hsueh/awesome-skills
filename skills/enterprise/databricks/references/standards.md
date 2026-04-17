## 7. Standards & Reference

### 7.1 Delta Lake Operations

```python
# OPTIMIZE (file compaction)
spark.sql("OPTIMIZE delta.`/path/to/table` ZORDER BY (date, user_id)")

# VACUUM (remove old versions)
spark.sql("VACUUM delta.`/path/to/table` RETAIN 168 HOURS")

# Time Travel
spark.read.format("delta").option("versionAsOf", 5).load("/path/to/table")
spark.read.format("delta").option("timestampAsOf", "2025-01-01").load("/path")

# Liquid Clustering (alternative to partitioning)
spark.sql("ALTER TABLE table CLUSTER BY (date, region)")

# MERGE (upsert)
from delta.tables import DeltaTable
delta_table = DeltaTable.forPath(spark, "/path/to/table")
delta_table.alias("target").merge(
    updates_df.alias("source"),
    "target.id = source.id"
).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
```

### 7.2 Spark Optimization on Databricks

```python
# Photon engine (C++ vectorized execution)
spark.conf.set("spark.databricks.photon.enabled", "true")

# AQE (Adaptive Query Execution)
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")

# Predictive I/O for storage
spark.conf.set("spark.databricks.delta.predictiveIO.enabled", "true")

# Optimal shuffle partitions
data_size_gb = 100  # Estimate
spark.conf.set("spark.sql.shuffle.partitions", max(200, data_size_gb * 2))

# Broadcast join threshold
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "100MB")
```

### 7.3 Unity Catalog Setup

```sql
-- Create catalog
CREATE CATALOG IF NOT EXISTS production;

-- Create schema
CREATE SCHEMA IF NOT EXISTS production.sales;

-- Create table with governance
CREATE TABLE production.sales.transactions (
    transaction_id STRING,
    customer_id STRING,
    amount DECIMAL(18,2),
    transaction_date DATE
) USING DELTA;

-- Grant access
GRANT SELECT ON TABLE production.sales.transactions TO DATA_ANALYSTS;

-- Enable predictive optimization
ALTER TABLE production.sales.transactions SET TBLPROPERTIES (
    'delta.enablePredictiveOptimization' = 'true'
);
```

### 7.4 Mosaic AI Vector Search

```python
# Create vector search index
from databricks.vector_search.client import VectorSearchClient

client = VectorSearchClient()

# Create endpoint
client.create_endpoint(
    name="vs_endpoint",
    endpoint_type="STANDARD"
)

# Create delta sync index
client.create_delta_sync_index(
    endpoint_name="vs_endpoint",
    index_name="product_index",
    source_table_name="catalog.schema.products",
    primary_key="id",
    embedding_source_column="description",
    embedding_model_endpoint_name="databricks-gte-large-en"
)

# Query vector search
results = client.similarity_search(
    index_name="product_index",
    query_text="wireless headphones",
    num_results=10
)
```

### 7.5 Mosaic AI Model Serving

```python
# Deploy model for real-time serving
import mlflow
from mlflow.deployments import get_deploy_client

client = get_deploy_client("databricks")

# Deploy registered model
client.create_endpoint(
    name="fraud-detection",
    config={
        "served_entities": [{
            "entity_name": "FraudDetectionModel",
            "entity_version": "1",
            "workload_size": "Small",
            "scale_to_zero_enabled": True
        }]
    }
)

# Query endpoint
import requests
response = requests.post(
    f"{workspace_url}/serving-endpoints/fraud-detection/invocations",
    headers={"Authorization": f"Bearer {token}"},
    json={"inputs": [[1.0, 2.0, 3.0]]}
)
```

---
