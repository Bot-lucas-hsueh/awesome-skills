# Troubleshooting Guide

## 8.1 Common Failures

### OutOfMemoryError

| Error | Cause | Fix |
|-------|-------|-----|
| `ExecutorLostFailure: OOM` | Data too large for executor heap | Reduce `spark.executor.memory`, increase `memoryOverhead` |
| `GC overhead limit exceeded` | Excessive garbage collection | Increase executor memory, tune GC: `-XX:+UseG1GC` |
| `Container killed by YARN/K8s` | Memory limit exceeded | Increase `spark.executor.memoryOverhead` to 20-30% of memory |
| `Shuffle fetch failed: OOM` | Too many shuffle partitions | Reduce `spark.sql.shuffle.partitions`, use `coalesce` |
| `Unable to acquire 256MB buffer` | Too many concurrent shuffle readers | Reduce partition count |

```python
# Diagnose memory issues
# Check storage memory vs execution memory
df.cache()
spark.sparkContext._conf.getAll()

# Avoid OOM with sampling
df = spark.read.parquet("s3://data/large_table")
sample_df = df.sample(withReplacement=False, fraction=0.001)
```

### Shuffle Failures

| Error | Cause | Fix |
|-------|-------|-----|
| `ShuffleMapStage failed` | Executor lost during shuffle | Increase `spark.shuffle.service.enabled`, check network |
| `Too many open files` | File descriptor limit | `ulimit -n 65536`, check `spark.sql.files.openCostInBytes` |
| `FetchFailedException` | Partition fetch timeout | Increase `spark.network.timeout`, `spark.executor.heartbeatInterval` |

```bash
# Increase file descriptors
# /etc/security/limits.conf
* soft nofile 65536
* hard nofile 65536

# Increase shuffle partition timeout
spark.conf.set("spark.network.timeout", "600s")
spark.conf.set("spark.executor.heartbeatInterval", "30s")
```

### Serialization Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Task not serializable` | Closure capturing non-serializable object | Move objects outside closure, use broadcast |
| `Kryo serialization failed` | Non-registered class | Register class: `spark.kryo.classesToRegister` |

```python
# BAD
def process(df):
    db_conn = create_db_connection()  # Not serializable!
    return df.map(lambda x: db_conn.query(x))

# GOOD
db_conn = create_db_connection()  # Created on driver
broadcast_conn = spark.sparkContext.broadcast(db_conn)

def process(x):
    return broadcast_conn.value.query(x)

df.map(process)  # Broadcast object sent to executors

# Or use foreachPartition
def process_partition(partition):
    conn = create_db_connection()  # Created per partition
    for row in partition:
        conn.insert(row)
    conn.close()

df.foreachPartition(process_partition)
```

### Data Type Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Cannot up cast` | Type coercion not allowed | Use `.cast()` explicitly |
| `Null value in join key` | NULL in join columns | Filter nulls: `.filter("key IS NOT NULL")` |
| `Integral literal overflow` | Number too large for Int | Use Long: `lit(1L)` |
| `DateException` | Invalid date format | Parse with `to_date(col, "yyyy-MM-dd")` |

## 8.2 Performance Tuning

### Partition & Parallelism Tuning

```python
# Target: 128-256MB per partition
# Formula: partitions = ceil(data_size_bytes / 128_000_000)

data_size_gb = 50
target_mb_per_partition = 256
partitions = int(data_size_gb * 1024 / target_mb_per_partition)

df = spark.read.parquet("s3://data/large_table")
df = df.repartition(partitions)  # Before expensive operations

# Coalesce to reduce partitions (no shuffle)
df_coalesced = df.coalesce(10)  # Only reduces

# Partition by join key (co-locate related data)
df.repartition(100, "customer_id")  # Same customer on same partition

# After filter (many partitions may be empty)
df.filter(col("region") == "US").coalesce(10)
```

### Join Optimization

```python
from pyspark.sql.functions import broadcast

# Broadcast small dimension tables (< 100MB)
large_df.join(
    broadcast(small_dim_df),
    "join_key"
)

# Configure auto-broadcast threshold
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", 104857600)  # 100MB

# Sort-merge join vs broadcast
# Spark uses broadcast when one side < threshold
# Use broadcast hint explicitly:
df1.join(broadcast(df2), "key", "left")

# Shuffle join with partitioned data
df1.repartition(100, "key").join(
    df2.repartition(100, "key"),
    "key"
)

# Avoid skew join
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", True)
spark.conf.set("spark.sql.adaptive.skewJoin.skewedPartitionFactor", 5)
```

### Caching Strategy

```python
# Cache only what you reuse
# Level: MEMORY_AND_DISK (default), MEMORY_ONLY, DISK_ONLY

# Cache a DataFrame reused multiple times
df_processed = df.filter(...).select(...)
df_processed.cache()  # Or df_processed = df_processed.unpersist(); df_processed.cache()

# Persist with specific level
from pyspark.storagelevel import StorageLevel

df_processed.persist(StorageLevel.MEMORY_AND_DISK_DESER)

# Always unpersist when done
df_processed.unpersist()
```

### SQL Performance

```python
# Predicate pushdown - filter early
df = spark.read.parquet("s3://data/orders")
df = df.filter(col("order_date") >= "2024-01-01")  # Push down to Parquet reader
df = df.filter(col("status") == "completed")  # Push down
df = df.select("order_id", "customer_id", "total")  # Column pruning

# Avoid SELECT *
df = df.select("needed", "columns", "only")

# Use Spark SQL functions over Python UDFs
from pyspark.sql.functions import col, upper, length, regexp_extract

# BAD
def clean_name(name):
    return name.strip().upper() if name else None

df.withColumn("clean_name", udf(clean_name)(col("name")))

# GOOD
df.withColumn("clean_name", upper(trim(col("name"))))
```

## 8.3 Debugging Techniques

### Reading Spark UI

```
Spark UI: http://driver:4040

Stages Tab:
  - Shuffle Read/Write size (watch for skew)
  - GC time (indicates memory pressure)
  - Task distribution (look for stragglers)

SQL Tab:
  - DAG visualization
  - Exchange nodes (shuffles)
  - Physical plan vs logical plan

Executors Tab:
  - Memory usage per executor
  - Active tasks

Storage Tab:
  - Cached RDDs/DataFrames
  - Size vs deserialized size
```

### Explain Plan

```python
# Logical plan
df.explain( mode="simple" )

# Physical plan
df.explain( mode="formatted" )

# Parsed and optimized logical plan
df.explain( mode="extended" )
```

### Logging & Metrics

```python
import logging
from pyspark.sql.functions import col

# Set log level
spark.sparkContext.setLogLevel("INFO")

# Structured logging
logger = logging.getLogger(__name__)
logger.info(f"Processing {df.count()} rows")

# Custom metrics
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setJobGroup("etl_job", "Daily ETL")

try:
    spark.sparkContext.setJobDescription("Reading source")
    df = spark.read.parquet("s3://data/source")
    
    spark.sparkContext.setJobDescription("Transforming")
    result = df.filter(col("active") == True).groupBy("category").count()
    
    spark.sparkContext.setJobDescription("Writing output")
    result.write.mode("overwrite").parquet("s3://data/output")
finally:
    spark.sparkContext.clearJobGroup()
```

## 8.4 Known Issues & Fixes

| Issue | Versions | Fix |
|-------|----------|-----|
| `Arrow optimization failed` | 3.2-3.4 | Disable: `spark.sql.execution.arrow.pyspark.enabled=false` |
| `Py4J error during Python worker restart` | 3.3-3.4 | Set `spark.python.worker.reuse=false`, increase memory |
| `Delta time travel query fails` | 3.0-3.2 | Check `spark.databricks.delta.retentionDurationCheck.enabled` |
| `S3 commit protocol failure` | All | Use `s3a://` instead of `s3://`, enable multipart |
| `Hive Metastore connection timeout` | All | Tune `hive.metastore.thrift.connection.max.wait.ms` |
| `Adaptive Query Execution breaking query` | 3.2-3.3 | Disable AQE: `spark.sql.adaptive.enabled=false` |
| `Spark Kubernetes: executor pod not found` | 3.4-3.5 | Check RBAC permissions for pod delete |
