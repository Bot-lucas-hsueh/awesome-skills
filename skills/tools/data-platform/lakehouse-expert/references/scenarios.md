# Scenario Examples

## 9.1 Real-World Use Cases

### Multi-Engine Analytics (Iceberg as the Single Source of Truth)

**User:** "Our data team uses Spark, Flink, Trino, and Presto. How do we avoid data silos?"

**Expert:**
```sql
-- Iceberg: Engine-agnostic table format
CREATE TABLE iceberg_catalog.analytics.user_events (
    event_id STRING NOT NULL,
    user_id STRING,
    event_type STRING,
    properties MAP<STRING, STRING>,
    event_time TIMESTAMP NOT NULL
) USING iceberg
PARTITIONED BY (days(event_time), bucket(16, user_id))
TBLPROPERTIES (
    'format-version' = '2',
    'write.distribution-mode' = 'hash',
    'write.metadata.delete-after-commit.enabled' = 'true',
    'write.metadata.previous-versions-max' = '100'
);

-- Spark (batch): Aggregation
spark.sql("""
    SELECT date_trunc('day', event_time) as day, event_type, COUNT(*) as cnt
    FROM iceberg_catalog.analytics.user_events
    WHERE event_time >= DATE_ADD(CURRENT_DATE, -7)
    GROUP BY 1, 2
    ORDER BY 1, 3 DESC
""").write.mode("overwrite").saveAsTable("analytics.daily_event_summary")

-- Trino (interactive): Ad-hoc queries
SELECT user_id, COUNT(*) as event_count
FROM iceberg_catalog.analytics.user_events
WHERE event_type = 'purchase'
  AND event_time >= CURRENT_DATE - INTERVAL '30' DAY
GROUP BY user_id
HAVING COUNT(*) > 10
ORDER BY event_count DESC
LIMIT 100;

-- Flink (streaming): Real-time enrichment
INSERT INTO iceberg_catalog.analytics.user_events_enriched
SELECT e.event_id, e.user_id, u.segment, e.event_type, e.event_time
FROM iceberg_catalog.analytics.user_events e
JOIN enriched_users u ON e.user_id = u.user_id;
```

### CDC Ingestion with Merge-on-Read (Iceberg)

**User:** "We need CDC from PostgreSQL with upsert support and efficient historical queries"

**Expert:**
```python
# Step 1: Initial batch load
spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://pg:5432/prod") \
    .option("dbtable", "customers") \
    .option("user", "spark") \
    .option("password", "secret") \
    .write \
    .mode("overwrite") \
    .format("iceberg") \
    .partitionBy("country") \
    .saveAsTable("raw.customers")

# Step 2: Incremental CDC with MERGE
spark.streams.awaitAnyTermination()

# CDC stream processing with merge
from delta.tables import DeltaTable

delta_customers = DeltaTable.forPath(spark, "s3://bucket/raw/customers")

def upsert_to_delta(micro_batch_df, batch_id):
    (delta_customers.alias("target")
        .merge(
            micro_batch_df.alias("source"),
            "target.customer_id = source.customer_id"
        )
        .whenMatchedUpdateAll()
        .whenNotMatchedInsertAll()
        .execute())

query = (spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "customers_cdc")
    .load()
    .writeStream
    .foreachBatch(upsert_to_delta)
    .option("checkpointLocation", "s3://bucket/checkpoints/customers/")
    .start())

# Step 3: Time travel for historical analysis
spark.read \
    .format("iceberg") \
    .option("as-of-timestamp", "2024-01-15T10:00:00") \
    .load("s3://bucket/raw/customers") \
    .createOrReplaceTempView("customers_snapshot")
```

### Hudi for Incremental Processing (Change Data Feed)

**User:** "We want to feed downstream pipelines only the changed records since last run"

**Expert:**
```python
hoodie_options = {
    'hoodie.table.name': 'orders',
    'hoodie.datasource.write.recordkey.field': 'order_id',
    'hoodie.datasource.write.precombine.field': 'updated_at',
    'hoodie.datasource.write.partitionpath.field': 'order_date',
    'hoodie.datasource.write.operation': 'upsert',
    'hoodie.datasource.write.table.type': 'MERGE_ON_READ',
    'hoodie.enable.change.data.capture': 'true',
}

# First run: Full load
spark.write.format("hudi") \
    .options(**hoodie_options) \
    .mode("overwrite") \
    .save("s3://bucket/hudi/orders")

# Subsequent runs: incremental (changed records only)
from pyspark.sql.functions import col

commit_times = spark.read.format("hudi") \
    .load("s3://bucket/hudi/orders/.hoodie") \
    .select("commit_time") \
    .orderBy(col("commit_time").desc()) \
    .limit(2) \
    .collect()

if len(commit_times) > 1:
    prev_commit = commit_times[1]["commit_time"]
    current_commit = commit_times[0]["commit_time"]

    changed_records = spark.read.format("hudi") \
        .option("hoodie.datasource.query.type", "incremental") \
        .option("hoodie.datasource.query.incremental.filter.end", current_commit) \
        .option("hoodie.datasource.query.incremental.filter.start", prev_commit) \
        .load("s3://bucket/hudi/orders")

    changed_records.write.mode("append").save("s3://bucket/hudi/order_changes")
```

## 9.2 Scaling Scenarios

### Scaling from GB → PB scale

| Scenario | Small (< 1TB) | Medium (1-100TB) | Large (100TB - 1PB) |
|----------|---------------|------------------|---------------------|
| **Format** | Delta | Iceberg | Iceberg |
| **Partitioning** | By date | By date + bucket | By date + bucket(128, pk) |
| **Compaction** | Auto-compact | Scheduled OPTIMIZE | Continuous background compaction |
| **Catalog** | Hive Metastore | AWS Glue | AWS Glue + Lake Formation |
| **Storage** | S3 Standard | S3 + Intelligent Tiering | S3 + Glacier for old partitions |
| **Query engine** | Single Spark | Multi-engine (Spark + Trino) | Trino + Spark + Flink |

### Partitioning Strategy Examples

```sql
-- High-cardinality, frequently filtered: bucket
CREATE TABLE events (
    event_id STRING,
    user_id STRING,
    event_type STRING
) USING iceberg
PARTITIONED BY (bucket(128, user_id));

-- Time-series with late-arriving data: time + hidden partition
CREATE TABLE events (
    event_id STRING,
    event_time TIMESTAMP,
    ingested_at TIMESTAMP
) USING iceberg
PARTITIONED BY (days(event_time));

-- Multi-dimensional access patterns: year/month/day explicit
CREATE TABLE events (
    event_id STRING,
    event_time TIMESTAMP
) USING iceberg
PARTITIONED BY (years(event_time), months(event_time), days(event_time));
```

## 9.3 Integration Scenarios

### Lakehouse + dbt + Airflow

```python
# airflow/dags/lakehouse_pipeline.py
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG('lakehouse_etl', default_args=default_args, schedule_interval='@hourly') as dag:

    ingest_cdc = SparkSubmitOperator(
        task_id='ingest_cdc_to_iceberg',
        application='/apps/ingest_cdc.py',
        conn_id='spark_conn',
        application_args=[
            '--source', 'kafka',
            '--target', 's3://bucket/raw/orders',
            '--checkpoint', 's3://bucket/checkpoints/orders',
        ]
    )

    run_dbt_models = BashOperator(
        task_id='dbt_transform',
        bash_command='cd /opt/dbt && dbt run --target prod --select tag:lakehouse'
    )

    optimize_table = SparkSubmitOperator(
        task_id='optimize_iceberg',
        application='/apps/optimize.py',
        conn_id='spark_conn',
        application_args=['--table', 'analytics.daily_orders']
    )

    ingest_cdc >> run_dbt_models >> optimize_table
```

### Lakehouse + Flink for Real-time Views

```sql
-- Iceberg SQL: Create materialized view equivalent
CREATE MATERIALIZED VIEW analytics.hourly_user_metrics AS
SELECT
    DATE_TRUNC('hour', event_time) AS hour,
    user_segment,
    COUNT(*) AS event_count,
    COUNT(DISTINCT user_id) AS unique_users,
    SUM(CASE WHEN event_type = 'purchase' THEN amount ELSE 0 END) AS revenue
FROM raw.user_events
WHERE event_time >= CURRENT_TIMESTAMP - INTERVAL '30' DAY
GROUP BY 1, 2;

-- Flink: Write to a rolling window table that backs the view
INSERT INTO analytics.hourly_user_metrics_stream
SELECT
    TUMBLE_START(event_time, INTERVAL '1' HOUR) AS hour,
    user_segment,
    COUNT(*) AS event_count,
    COUNT(DISTINCT user_id) AS unique_users
FROM raw.user_events
GROUP BY
    TUMBLE(event_time, INTERVAL '1' HOUR),
    user_segment;
```

### Schema Evolution

```sql
-- Safe schema evolution with defaults
ALTER TABLE analytics.user_events ADD COLUMNS (
    new_column STRING DEFAULT 'unknown',
    processed_v2 INT DEFAULT 0
);

-- Merge schema (Delta)
spark.write.format("delta") \
    .option("mergeSchema", "true") \
    .mode("append") \
    .save("s3://bucket/tables/events")

-- Iceberg: Evolve schema with metadata
ALTER TABLE iceberg_catalog.db.events ALTER COLUMN old_column DROP NOT NULL;
ALTER TABLE iceberg_catalog.db.events RENAME COLUMN old_name TO new_name;
```
