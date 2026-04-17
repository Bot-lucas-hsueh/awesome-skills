# Standards & Reference

## 7.1 Official Documentation

- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [PySpark API Reference](https://spark.apache.org/docs/latest/api/python/)
- [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Structured Streaming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
- [DataFrame Operations](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html)
- [Spark Configuration](https://spark.apache.org/docs/latest/configuration.html)
- [Spark Monitoring & Instrumentation](https://spark.apache.org/docs/latest/monitoring.html)
- [Spark Performance Tuning](https://spark.apache.org/docs/latest/tuning.html)
- [Spark on Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html)
- [Spark Structured Streaming Kafka Integration](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html)
- [Delta Lake Documentation](https://docs.delta.io/latest/delta-intro.html)
- [Apache Iceberg on Spark](https://iceberg.apache.org/docs/latest/spark-queries/)

## 7.2 Architecture Patterns

### Spark Application Architecture

```
Driver (JVM)
├── SparkContext
│   ├── DAGScheduler (stages, tasks)
│   └── TaskScheduler (task distribution)
└── SQLContext / SparkSession

Cluster Manager
├── Spark Standalone
├── YARN (ResourceManager)
├── Mesos
└── Kubernetes (scheduler backend)

Executors (JVMs per node)
├── Task slots (cores)
├── Cached partitions
└── Shuffle output
```

### Execution Plan

```
SQL / DataFrame
      │
      ▼
 Catalyst Optimizer
      │
  ┌───┴───┐
  │       │
 LogicalPlan   OptimizedLogicalPlan
  │       │
  ▼       ▼
 Physical Plan  ════════► SparkPlan
  │                   │
  └──── RDD DAG ──────┘
  │
  ▼
 DAGScheduler (stages)
  │
  ▼
 TaskScheduler (tasks per executor)
  │
  ▼
 shuffle: exchange(codegen_id=xx)
```

### Partitioning Strategy

```
DataFrame Partitioning:

1. Hash Partitioning: df.repartition(n, col)
   - Round-robin by hash of partition key
   - Even distribution

2. Range Partitioning: df.sortWithinPartitions(col)
   - Orders within partition, preserves range locality

3. Broadcast: broadcast(small_df)
   - Replicated to all executors
   - For small dimension tables (< 10MB)

4. Coalesce: df.coalesce(n)
   - Reduce partitions (no shuffle)
   - Use after filter to reduce tasks

Rule of thumb:
  - Partitions = 2-4x CPU cores
  - Target partition size: 128-256MB
  - Minimum: 10 partitions per TB of data
```

## 7.3 Configuration Reference

### SparkSession

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("etl-pipeline") \
    .master("k8s://https://kubernetes.default.svc:443") \
    .config("spark.submit.deployMode", "cluster") \
    .config("spark.kubernetes.namespace", "spark") \
    .config("spark.kubernetes.container.image", "spark:3.5.0") \
    .config("spark.executor.instances", 10) \
    .config("spark.executor.cores", 4) \
    .config("spark.executor.memory", "8g") \
    .config("spark.executor.memoryOverhead", "2g") \
    .config("spark.driver.cores", 2) \
    .config("spark.driver.memory", "4g") \
    .config("spark.driver.memoryOverhead", "1g") \
    .config("spark.sql.adaptive.enabled", True) \
    .config("spark.sql.adaptive.coalescePartitions.enabled", True) \
    .config("spark.sql.adaptive.skewJoin.enabled", True) \
    .config("spark.sql.shuffle.partitions", 200) \
    .config("spark.sql.autoBroadcastJoinThreshold", "100MB") \
    .config("spark.sql.files.maxPartitionBytes", "128MB") \
    .config("spark.sql.session.timeZone", "UTC") \
    .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .config("spark.kryoserializer.buffer.max", "512m") \
    .config("spark.eventLog.enabled", True) \
    .config("spark.eventLog.dir", "s3a://spark-history/") \
    .config("spark.history.fs.logDirectory", "s3a://spark-history/") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")
```

### spark-defaults.conf

```properties
# Cluster sizing
spark.executor.instances 10
spark.executor.cores 4
spark.executor.memory 8g
spark.executor.memoryOverhead 2g
spark.driver.cores 2
spark.driver.memory 4g
spark.default.parallelism 160

# SQL
spark.sql.adaptive.enabled true
spark.sql.adaptive.coalescePartitions.enabled true
spark.sql.adaptive.skewJoin.enabled true
spark.sql.adaptive.coalescePartitions.minPartitionSize 1MB
spark.sql.adaptive.skewJoin.skewedPartitionFactor 5
spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes 256MB
spark.sql.shuffle.partitions 200
spark.sql.autoBroadcastJoinThreshold 104857600
spark.sql.files.maxPartitionBytes 134217728
spark.sql.parquet.compression.codec snappy
spark.sql.session.timeZone UTC
spark.sql.datetimejava8API.enabled true

# Serialization
spark.serializer org.apache.spark.serializer.KryoSerializer
spark.kryo.registrationRequired false
spark.kryo.unsafe true

# Networking
spark.network.timeout 600s
spark.rpc.message.maxSize 256

# Shuffle
spark.shuffle.service.enabled true
spark.shuffle.service.port 7337
spark.sql.shuffle.service.db.enabled true

# Kubernetes specific
spark.kubernetes.namespace spark
spark.kubernetes.executor.deleteOnTermination false
spark.kubernetes.driver.pod.name ${HOSTNAME}
spark.kubernetes.container.image spark:3.5.0
```

## 7.4 Common Commands Reference

```bash
# Submit job
spark-submit \
    --master k8s://https://kubernetes.default.svc:443 \
    --deploy-mode cluster \
    --class com.example.pipeline \
    --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,io.delta:delta-core_2.12:3.0.0 \
    --conf spark.executor.instances=10 \
    --conf spark.executor.cores=4 \
    --conf spark.executor.memory=8g \
    --conf spark.kubernetes.container.image=spark:3.5.0 \
    s3a://code/jars/pipeline.jar

# Interactive shell
pyspark --master yarn --deploy-mode client
spark-shell --master k8s://... --conf spark.executor.instances=3

# PySpark with Delta Lake
pyspark --packages io.delta:delta-core_2.12:3.0.0 \
    --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension \
    --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog

# List running applications
spark-submit --status
yarn application -list -appStates RUNNING

# Kill application
yarn application -kill application_xxx
```

## 7.5 Version Compatibility

| Spark | Scala | Python | Java | Key Features |
|-------|-------|--------|------|--------------|
| 3.3.x | 2.12, 2.13 | 3.1+ | 8, 11 | ANSI SQL, Spark Connect (preview) |
| 3.4.x | 2.12 | 3.2+ | 8, 11, 17 | Spark Connect GA, Pandas API GA |
| 3.5.x | 2.12 | 3.2+ | 8, 11, 17 | Adaptive Query Execution improvements, Spark Connect |
| 3.6.x | 2.12 | 3.2+ | 8, 11, 17, 21 | PySpark vectorized UDF, Structured Streaming changes |

| Connector | Spark 3.5 | Notes |
|-----------|-----------|-------|
| Delta Lake | 3.0+ | Use matching Delta version |
| Apache Iceberg | 3.3+ | Use matching Iceberg version |
| Apache Hudi | 3.3+ | Spark 3.3+ supported |
| Kafka | 3.5 | spark-sql-kafka-0-10_2.12 |
| S3 / S3A | 3.5 | hadoop-aws package |
| BigQuery | 3.3+ | spark-bigquery-connector |
| Snowflake | 3.4+ | spark-snowflake |
