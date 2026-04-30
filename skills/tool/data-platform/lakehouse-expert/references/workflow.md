# Standard Workflow

## 8.1 Development Workflow (Local → Cloud)

```
Local Lakehouse Development
├── 1. Choose Table Format
│   ├── Delta Lake: Best for Databricks/spark-heavy shops
│   ├── Iceberg: Best for multi-engine (Spark/Flink/Trino/Presto)
│   └── Hudi: Best for incremental streaming pipelines
│
├── 2. Local Environment Setup
│   ├── Docker: minio (S3-compatible) + Spark/Jupyter
│   ├── Or: AWS Athena local sandbox
│   └── Or: DuckDB with Iceberg/Delta extensions
│
├── 3. Schema Design & Migration
│   ├── Define schema with explicit partitioning
│   ├── Set up Z-order / clustering keys
│   └── Plan evolution strategy (add columns, rename)
│
├── 4. Data Ingestion Testing
│   ├── Small batch writes via Spark/Pandas
│   ├── Validate schema enforcement
│   └── Test time travel queries
│
└── 5. Deploy to Cloud
    ├── Upload to S3/GCS/ABFS
    ├── Register table in Hive Metastore / Glue / Unity Catalog
    └── Verify cross-engine readability (Spark → Trino → Flink)
```

### Local Dev with Docker

```yaml
# docker-compose.yml
version: '3'
services:
  minio:
    image: minio/minio
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    command: server /data --console-address ":9001"

  spark:
    image: bitnami/spark:3.5
    ports:
      - "8080:8080"
    environment:
      SPARK_MODE: master
      SPARK_WAREHOUSE_DIR: /spark-warehouse
    volumes:
      - ./warehouse:/spark-warehouse
      - ./notebooks:/opt/bitnami/spark/examples/src/main/python
    depends_on:
      - minio
```

### DuckDB (Local Iceberg Development)

```python
-- Load Iceberg extension
INSTALL iceberg FROM community_contributions;
LOAD iceberg;

-- Query Iceberg table locally
SELECT * FROM iceberg_scan(
    's3://bucket/db/table',
    region => 'us-east-1',
    endpoint => 'http://localhost:9000',
    access_key_id => 'minioadmin',
    secret_access_key => 'minioadmin'
) LIMIT 10;

-- Write to Iceberg
CREATE TABLE iceberg.'s3://bucket/db/new_table' AS
SELECT * FROM source_table;
```

## 8.2 Deployment / Production Workflow

```
Production Deployment
├── 1. Storage Layer
│   ├── S3: Use Delta Lake with S3-optimized LogStore
│   ├── GCS: Use Delta Lake with GCS LogStore
│   ├── ADLS Gen2: Use Delta Lake with ADLS-specific configs
│   └── Configure lifecycle policies (transition to Glacier)
│
├── 2. Table Registration
│   ├── Unity Catalog (Databricks)
│   ├── AWS Glue Data Catalog
│   ├── Hive Metastore (CDP / EMR)
│   └── Apache Polaris / Nessie for Git-like versioning
│
├── 3. Ingestion Pipeline
│   ├── Option A: Spark Structured Streaming → Delta/Iceberg
│   ├── Option B: Flink CDC → Iceberg/Delta
│   ├── Option C: Debezium + Kafka + Hudi DeltaStreamer
│   └── Option D: dbt + lakehouse (dbt-lakehouse plugin)
│
├── 4. Optimization
│   ├── Auto-compaction (Delta autoOptimize.write)
│   ├── Iceberg: Rewrite data + manifest compaction
│   ├── Hudi: Clustering via hoodie.clustering.strategy
│   └── ZORDER / SORT BY on frequently filtered columns
│
└── 5. Access Control
    ├── Row-level security via Unity Catalog / Polaris
    ├── Column masking (PII columns)
    └── Row filter expressions
```

### Production Ingestion (Spark Structured Streaming → Iceberg)

```python
query = (spark
    .readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "events")
    .option("startingOffsets", "latest")
    .load()
    .selectExpr("CAST(value AS STRING)")
    .select(from_json(col("value"), schema).alias("data"))
    .select("data.*")
    .writeStream
    .format("iceberg")
    .outputMode("append")
    .option("path", "s3://bucket/db/events")
    .option("fanout-enabled", "true")
    .option("checkpointLocation", "s3://bucket/checkpoints/events/")
    .trigger(processingTime="1 minute")
    .start())

query.awaitTermination()
```

### dbt + Lakehouse

```yaml
# dbt_project/models/analytics/schema.yml
models:
  - name: daily_revenue
    config:
      materialized: iceberg
      partition_by: ["date_trunc('day', created_at)"]
      table_properties:
        format-version: "2"
        write.delete.mode: merge-on-read
```

```sql
-- dbt model: models/analytics/daily_revenue.sql
{{ config(materialized='incremental', unique_key='date') }}

SELECT
    DATE(created_at) AS date,
    SUM(amount) AS total_revenue,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM {{ source('raw', 'orders') }}
{% if is_incremental() %}
    WHERE created_at > (SELECT MAX(date) FROM {{ this }})
{% endif %}
GROUP BY DATE(created_at)
```

## 8.3 Monitoring & Observability

```
Lakehouse Observability Stack
├── Table Statistics (automatic)
│   ├── Delta: dataSkipping stats (min/max/null count per column)
│   ├── Iceberg: manifest file statistics
│   └── Hudi: bloom filter index, column stats index
│
├── Storage Metrics
│   ├── File count and size per partition
│   ├── Small file alerts (configurable threshold)
│   └── Last commit timestamp / data lag
│
└── Query Performance
    ├── Trino / Spark: EXPLAIN ANALYZE
    ├── Metadata table queries (Iceberg: SELECT * FROM my_table.history)
    └── Partition prune validation
```

### Monitoring Queries

```sql
-- Delta Lake: Table statistics
spark.sql("DESCRIBE DETAIL delta.`s3://bucket/tables/orders`").show(truncate=False)

-- Iceberg: Table history and snapshots
spark.sql("SELECT * FROM iceberg_catalog.db.events.history").show()
spark.sql("SELECT * FROM iceberg_catalog.db.events.files").show()

-- Iceberg: Find large partitions
spark.sql("""
    SELECT partition, file_count, total_size_bytes, spec_id
    FROM iceberg_catalog.db.events.partitions
    ORDER BY total_size_bytes DESC
""").show(20)

-- Hudi: Table status
spark.sql("SELECT * FROM hudi_db.orders_commits").orderBy(col("begin_instant_time").desc()).show(10)
```

### Alerting on Table Health

```python
# Check for stale tables (no updates in 24h)
alert_rules = [
    ("stale_table", "No commits in 24h",
     lambda t: (datetime.now() - t.last_commit_time).days > 1),
    ("excessive_files", "More than 1000 files in partition",
     lambda t: t.file_count > 1000),
    ("small_files", "Files smaller than 10MB",
     lambda t: t.avg_file_size < 10 * 1024 * 1024),
]
```
