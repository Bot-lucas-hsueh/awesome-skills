# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Fix |
|---|---------|----------|--------|-----|
| 1 | **Using BY DAY partitions on high-volume tables** | 🔴 High | Too many small files, partition pruning ineffective | Use `PARTITIONED BY (date_trunc('month', ts))` or `bucket(N, key)` |
| 2 | **Skipping table compaction (small files)** | 🔴 High | Thousands of tiny files, slow queries, metastore OOM | Run `OPTIMIZE` (Delta), `rewrite_data_files` (Iceberg), clustering (Hudi) |
| 3 | **Not configuring Z-order / clustering for skewed data** | 🟡 Medium | Full table scan despite filter, 10x+ query slowdown | `ZORDER BY (user_id, product_id)` on Delta; `SORT BY` on Iceberg/Hudi |
| 4 | **Using MERGE_ON_READ without compaction** | 🟡 Medium | Read amplification, delta files accumulate | Schedule periodic compaction; Hudi: set `hoodie.compact.inline` |
| 5 | **Writing to same table from multiple engines without coordination** | 🟡 Medium | Concurrent commit conflicts, stale metadata | Use ACID-compatible catalog (Unity Catalog, Glue, HMS with HMS locks) |
| 6 | **Forgetting `unique_key` in incremental models** | 🔴 High | Duplicate records in production | Always set `unique_key` in dbt incremental config; use `merge` strategy |
| 7 | **Not setting `hoodie.datasource.write.payload.class`** | 🟡 Medium | CDC records lost on upsert | Set to `org.apache.hudi.payload.AWSDmsAvroPayload` for CDC workloads |
| 8 | **Excessive partition columns** | 🟡 Medium | Partition explosion, slow metadata ops | Keep partition columns to ≤ 3; use bucket for high-cardinality |
| 9 | **Writing to S3 without proper retry/exponential backoff** | 🟡 Medium | Commit failures due to eventual consistency | Use Spark/Hive's built-in S3 commit algorithm or Iceberg's V2 writer |
| 10 | **Not using column statistics for data skipping** | 🟡 Medium | Full scan despite filter predicates | Explicitly set `delta.dataSkippingNumIndexedCols`; avoid `SELECT *` |

## 10.2 Anti-Patterns

### Anti-Pattern: Over-partitioning

```python
# BAD: Too granular — creates thousands of partitions per day
df.write \
    .partitionBy("year", "month", "day", "hour", "minute", "user_country") \
    .saveAsTable("events")

# GOOD: Partition by day + bucket for high-cardinality fields
df.write \
    .partitionBy("date") \
    .bucketBy(128, "user_id") \
    .saveAsTable("events")

# ICEBERG: Use hidden partitioning
df.writeTo("events").partitionedBy(
    spark_typed_lit(date_trunc("day", col("event_time")))
).create()
```

### Anti-Pattern: SELECT * on Wide Tables

```python
# BAD: Reads all columns including large JSON/payload fields
df = spark.read.format("iceberg").load("s3://bucket/events")

# GOOD: Column pruning for specific analysis
df = spark.read \
    .format("iceberg") \
    .load("s3://bucket/events") \
    .select("event_id", "user_id", "event_type", "event_time")

# BETTER: Pushdown filter to storage layer (avoid scanning full files)
df = spark.read \
    .option("filter", "event_type = 'purchase' AND event_time > '2024-01-01'") \
    .format("iceberg") \
    .load("s3://bucket/events")
```

### Anti-Pattern: Unbounded CDC with Append-Only Table

```python
# BAD: Using append mode for CDC — leads to duplicate records
query = df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/chk/") \
    .start("s3://bucket/orders")

# GOOD: Use MERGE mode for CDC upserts
from delta.tables import DeltaTable

delta_table = DeltaTable.forPath(spark, "s3://bucket/orders")

def upsert_func(micro_batch_df, batch_id):
    delta_table.alias("target").merge(
        micro_batch_df.alias("source"),
        "target.order_id = source.order_id"
    ).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()

query = df.writeStream \
    .foreachBatch(upsert_func) \
    .option("checkpointLocation", "s3://bucket/checkpoints/orders") \
    .start()
```

### Anti-Pattern: Skipping Table Optimization Schedule

```sql
-- BAD: Never running OPTIMIZE — small files accumulate
INSERT INTO orders SELECT * FROM new_orders;

-- GOOD: Schedule compaction after batch load
spark.sql("""
    OPTIMIZE delta.`s3://bucket/orders`
    ZORDER BY (customer_id, order_date)
""")

-- ICEBERG: Continuous compaction
spark.sql("""
    ALTER TABLE iceberg_catalog.db.events
    SET TBLPROPERTIES ('write.target-file-size-bytes' = '134217728')
""")
```

### Anti-Pattern: Writing Without Schema Validation

```python
# BAD: Silent schema drift — mismatched types cause silent failures
df.write.mode("append").format("delta").save("s3://bucket/table")

# GOOD: Enforce schema on write
spark.sql("""
    CREATE TABLE orders (
        order_id STRING NOT NULL,
        amount DECIMAL(10,2) NOT NULL
    ) USING delta
    TBLPROPERTIES ('delta.schema.autoMerge.enabled' = 'false')
""")

df.write.format("delta").mode("append").option("mergeSchema", "false").save("s3://bucket/table")

# ICEBERG: Explicit schema enforcement
from iceberg.exceptions import SchemaNotFoundException, ValidationException
try:
    iceberg_table.update_schema().commit()
except ValidationException as e:
    print(f"Schema conflict: {e}")
```

### Anti-Pattern: Manual File Management

```python
# BAD: Direct file manipulation breaks table metadata
import boto3
s3 = boto3.client('s3')
s3.delete_objects(Bucket='bucket', Delete={'Objects': [{'Key': 'part-001.parquet'}]})

# GOOD: Use table's delete/expire APIs
spark.sql("DELETE FROM delta.`s3://bucket/orders` WHERE status = 'cancelled'")
spark.sql("VACUUM delta.`s3://bucket/orders` RETAIN 168 HOURS")

# ICEBERG: Expire snapshots and remove orphan files
spark.sql("ALTER TABLE db.events EXECUTE EXPIRE_SNAPSHOTS")
spark.sql("ALTER TABLE db.events EXECUTE REMOVE_ORPHAN_FILES")
```

### Anti-Pattern: No Governance / Open Storage

```sql
-- BAD: Public bucket, no access control
CREATE TABLE raw.events LOCATION 's3://public-bucket/events';

-- GOOD: Use Unity Catalog / Lake Formation
CREATE TABLE raw.events (
    event_id STRING,
    user_pii STRING MASKED
) USING delta
LOCATION 's3://bucket/raw/events'
TBLPROPERTIES (
    'delta.enableChangeDataFeed' = 'true'
);

GRANT SELECT ON raw.events TO ROLE analyst;
GRANT SELECT ON raw.events WHERE user_pii IS NULL TO ROLE public_viewer;
```
