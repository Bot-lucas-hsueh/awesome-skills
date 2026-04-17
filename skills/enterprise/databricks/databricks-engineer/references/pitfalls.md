# Databricks Common Pitfalls & Anti-Patterns

## Anti-Pattern 1: The Small Files Problem

### ❌ Wrong
```python
# Streaming with frequent micro-batches creating tiny files
stream.writeStream \
    .format("delta") \
    .trigger(processingTime="10 seconds") \
    .start("/path/to/table")  # Creates 8,640 files per day!
```

### ✅ Right
```python
# Use auto-optimization or schedule compaction
spark.conf.set("spark.databricks.delta.optimizeWrite.enabled", "true")
spark.conf.set("spark.databricks.delta.autoCompact.enabled", "true")

# Or batch triggers for higher throughput
stream.writeStream \
    .format("delta") \
    .trigger(availableNow=True) \
    .start("/path/to/table")

# Schedule daily OPTIMIZE
# In job: spark.sql("OPTIMIZE table_name")
```

**Impact**: Small files cause query slowdowns (10-100x) and excessive metadata operations.

---

## Anti-Pattern 2: Over-Partitioning

### ❌ Wrong
```sql
-- Partitioning by high-cardinality column
CREATE TABLE events (
    user_id STRING,
    event_type STRING,
    timestamp TIMESTAMP
) USING DELTA
PARTITIONED BY (user_id);  -- Millions of partitions!
```

### ✅ Right
```sql
-- Partition by date for time-series data
CREATE TABLE events (
    user_id STRING,
    event_type STRING,
    timestamp TIMESTAMP,
    event_date DATE
) USING DELTA
PARTITIONED BY (event_date);

-- Z-order by high-cardinality columns for filtering
OPTIMIZE events ZORDER BY (user_id);
```

**Impact**: Over-partitioning causes metadata explosion and slow directory listing.

---

## Anti-Pattern 3: Disabling Adaptive Query Execution

### ❌ Wrong
```python
# Turning off AQE for "predictability"
spark.conf.set("spark.sql.adaptive.enabled", "false")
```

### ✅ Right
```python
# Enable all AQE features
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.sql.adaptive.localShuffleReader.enabled", "true")
```

**Impact**: AQE can improve performance by 2-10x through dynamic optimization.

---

## Anti-Pattern 4: Ignoring Schema Evolution

### ❌ Wrong
```python
# Hard-coding schema, failing on new columns
df = spark.read.schema(hardcoded_schema).json("/path")
df.write.format("delta").mode("append").save("/table")
```

### ✅ Right
```python
# Enable schema evolution
(df.write
    .format("delta")
    .mode("append")
    .option("mergeSchema", "true")
    .save("/table")
)

# Or set at table level
spark.sql("""
ALTER TABLE table_name SET TBLPROPERTIES (
    'delta.columnMapping.mode' = 'name',
    'delta.enableDeletionVectors' = 'true'
)
""")
```

**Impact**: Schema mismatches cause pipeline failures and data loss.

---

## Anti-Pattern 5: Dangerous VACUUM Operations

### ❌ Wrong
```sql
-- Immediate deletion of all old versions
VACUUM table_name RETAIN 0 HOURS;  -- DANGEROUS!
```

### ✅ Right
```sql
-- Safe retention period (minimum 7 days)
VACUUM table_name RETAIN 168 HOURS;  -- 7 days

-- Or use default retention
SET spark.databricks.delta.retentionDurationCheck.enabled = true;
VACUUM table_name;  -- Uses default 7 days
```

**Impact**: Aggressive VACUUM prevents time travel recovery and can break concurrent queries.

---

## Anti-Pattern 6: Hardcoded Secrets

### ❌ Wrong
```python
# Embedding credentials in code
spark.conf.set("fs.azure.account.key", "abc123...")
db_password = "super_secret_password"
```

### ✅ Right
```python
# Use Databricks secrets
db_password = dbutils.secrets.get(scope="prod", key="db-password")

# Or Unity Catalog credentials
spark.conf.set("fs.azure.account.oauth2.client.secret", 
    dbutils.secrets.get("azure", "client-secret"))
```

**Impact**: Hardcoded secrets are security risks and compliance violations.

---

## Anti-Pattern 7: Interactive Clusters for Production

### ❌ Wrong
```python
# Running production jobs on all-purpose clusters
# (More expensive, no auto-termination guarantees)
```

### ✅ Right
```python
# Use job clusters via Workflows API or UI
# Key differences:
# - Job clusters: 30-40% cheaper
# - Auto-terminate guaranteed
# - Purpose-built for reliability

# In Databricks job configuration:
{
    "new_cluster": {
        "spark_version": "13.3.x-scala2.12",
        "node_type_id": "i3.xlarge",
        "num_workers": 2,
        "autoscale": {
            "min_workers": 1,
            "max_workers": 10
        }
    }
}
```

**Impact**: Interactive clusters for jobs waste 30-40% on compute costs.

---

## Anti-Pattern 8: Skipping Data Quality

### ❌ Wrong
```python
# No validation between layers
df.write.format("delta").mode("overwrite").save("/silver/table")
```

### ✅ Right
```python
# Delta constraints
spark.sql("""
ALTER TABLE silver.table ADD CONSTRAINT valid_id CHECK (id IS NOT NULL);
ALTER TABLE silver.table ADD CONSTRAINT positive_amount CHECK (amount > 0);
""")

# Or with Delta Live Tables expectations
@dlt.table
@dlt.expect_all({
    "valid_id": "id IS NOT NULL",
    "valid_amount": "amount > 0",
    "valid_date": "created_at < current_timestamp()"
})
def silver_table():
    return dlt.read("bronze_table")
```

**Impact**: Bad data propagates downstream, causing cascading failures.

---

## Anti-Pattern 9: Ignoring Data Skew

### ❌ Wrong
```python
# Joining without addressing skew
df1.join(df2, "user_id")  # Some users have millions of rows
```

### ✅ Right
```python
# Enable skew join optimization
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.skewedPartitionFactor", "5")

# Or salt the keys manually
from pyspark.sql.functions import rand, lit, concat, col

salt = 10
df1_salted = df1.withColumn("salted_key", concat("user_id", lit("_"), (rand() * salt).cast("int")))
df2_salted = df2.withColumn("salted_key", concat("user_id", lit("_"), explode([lit(i) for i in range(salt)])))

result = df1_salted.join(df2_salted, "salted_key")
```

**Impact**: Skew causes stragglers, extending job runtime by 10-100x.

---

## Anti-Pattern 10: Not Using Time Travel

### ❌ Wrong
```python
# Manual backup strategy
# Creating full copies for versioning
spark.table("production.data").write.parquet("/backups/data_v1.parquet")
```

### ✅ Right
```python
# Delta Lake time travel (built-in)
# Query previous versions
old_data = (spark.read
    .format("delta")
    .option("versionAsOf", 100)
    .load("/production/data")
)

# Restore to previous version
spark.sql("RESTORE TABLE production.data TO VERSION AS OF 100")

# Configure retention
spark.sql("ALTER TABLE production.data SET TBLPROPERTIES ('delta.logRetentionDuration' = 'interval 30 days')")
```

**Impact**: Manual backups waste storage and are error-prone.

---

## Anti-Pattern 11: Suboptimal File Formats

### ❌ Wrong
```python
# Reading CSV at scale
df = spark.read.csv("/large/dataset/*.csv")  # Slow parsing

# Writing to non-columnar format
df.write.json("/output/")  # Poor compression, slow reads
```

### ✅ Right
```python
# Use Parquet or Delta Lake
df = spark.read.parquet("/dataset/")

# For CSV sources, convert once
df.write.format("delta").save("/delta/table/")

# Use Auto Loader for efficient ingestion
(spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", "/schema")
    .load("/input/csv/")
    .writeStream
    .format("delta")
    .start("/delta/table/")
)
```

**Impact**: CSV/JSON are 10-100x slower than Parquet/Delta for analytics.

---

## Anti-Pattern 12: Over-Caching Data

### ❌ Wrong
```python
# Caching everything
df.cache()  # Uses memory unnecessarily
df.count()
df.show()
df.write.save("/output/")
```

### ✅ Right
```python
# Cache only when data is reused
df = expensive_transformation()
df.cache()
df.count()  # Materialize cache

# Use in multiple places
analytics = df.groupBy("category").agg(sum("amount"))
ml_features = df.select("user_id", "features")

# Unpersist when done
df.unpersist()
```

**Impact**: Unnecessary caching causes OOM errors and cluster instability.
