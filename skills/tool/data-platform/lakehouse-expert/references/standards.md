# Standards & Reference

## 7.1 Official Documentation

- [Delta Lake Documentation](https://docs.delta.io/latest/delta-introduction.html)
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
- [Apache Hudi Documentation](https://hudi.apache.org/docs/latest/)
- [Databricks Delta Lake Best Practices](https://docs.databricks.com/delta/best-practices.html)
- [Iceberg Java API Reference](https://iceberg.apache.org/javadoc/latest/)
- [Delta Lake Rust SDK](https://docs.delta.io/latest/delta-rust.html)
- [Apache Hudi DeltaStreamer](https://hudi.apache.org/docs/next/hoodie_deltastreamer)
- [Unity Catalog](https://docs.databricks.com/data-governance/unity-catalog/index.html)

## 7.2 Configuration Reference

### Delta Lake (databricks-connect / delta-spark)

```python
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

builder = SparkSession.builder.appName("lakehouse-app") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.databricks.delta.autoCompact.enabled", "true") \
    .config("spark.databricks.delta.properties.defaults.autoOptimize.autoCompact", "true") \
    .config("spark.delta.logStore.class", "org.apache.spark.sql.delta.storage.S3SingleDriverLogStore") \
    .config("spark.delta.merge.enableLowShuffle", "true")

spark = configure_spark_with_delta_pip(builder).getOrCreate()
```

### Iceberg (PyIceberg / spark-bigquery-connector pattern)

```python
# Iceberg on AWS Glue / EMR
from pyspark import SparkConf
from pyspark.sql import SparkSession

conf = SparkConf() \
    .set("spark.sql.catalog.demo", "org.apache.iceberg.spark.SparkCatalog") \
    .set("spark.sql.catalog.demo.warehouse", "s3://your-bucket/iceberg-warehouse/") \
    .set("spark.sql.catalog.demo.s3.endpoint", "https://s3.us-east-1.amazonaws.com") \
    .set("spark.sql.catalog.demo.io-impl", "org.apache.iceberg.aws.s3.S3FileIO")

spark = SparkSession.builder.config(conf=conf).getOrCreate()
```

### Hudi (Spark DataSource)

```python
hoodie_options = {
    'hoodie.table.name': 'hudi_table',
    'hoodie.datasource.write.recordkey.field': 'id',
    'hoodie.datasource.write.partitionpath.field': 'date',
    'hoodie.datasource.write.precombine.field': 'timestamp',
    'hoodie.datasource.write.table.type': 'MERGE_ON_READ',
    'hoodie.datasource.write.operation': 'upsert',
    'hoodie.datasource.write.hoodieimpl': 'spark',
    'hoodie.upsert.shuffle.parallelism': '200',
    'hoodie.insert.shuffle.parallelism': '200',
    'hoodie.metadata.enable': 'true',
    'hoodie.metadata.index.column.stats.enable': 'true',
}
```

### Table Formats DDL

```sql
-- Delta Lake
CREATE TABLE delta.`s3://bucket/tables/orders` (
    order_id STRING,
    customer_id STRING,
    total_amount DECIMAL(10,2),
    created_at TIMESTAMP,
    status STRING
) USING delta
PARTITIONED BY (status, days(created_at))
TBLPROPERTIES (
    'delta.autoOptimize.optimizeWrite' = 'true',
    'delta.dataSkippingNumIndexedCols' = '10'
);

-- Iceberg
CREATE TABLE iceberg_catalog.db.events (
    event_id STRING NOT NULL,
    event_type STRING,
    user_id STRING,
    properties MAP<STRING, STRING>,
    event_time TIMESTAMP NOT NULL
) USING iceberg
PARTITIONED BY (days(event_time), bucket(16, user_id))
TBLPROPERTIES (
    'format-version' = '2',
    'write.delete.mode' = 'merge-on-read',
    'write.merge.mode' = 'merge-on-read'
);

-- Hudi
CREATE TABLE hudi_db.products (
    product_id STRING,
    category STRING,
    price DECIMAL(10,2),
    updated_at TIMESTAMP
) USING hudi
PARTITIONED BY (category)
OPTIONS (
    'primaryKey' = 'product_id',
    'preCombineField' = 'updated_at'
);
```

## 7.3 Common Commands / Operations

### Delta Lake Operations

```bash
# Vacuum old files (remove snapshots beyond retention)
spark.sql("VACUUM delta.`s3://bucket/tables/orders` RETAIN 168 HOURS")

# Show table history
spark.sql("DESCRIBE HISTORY delta.`s3://bucket/tables/orders`").show()

# Time travel to specific version
df = spark.read.format("delta").option("versionAsOf", 42).load("s3://bucket/tables/orders")

# Optimize table (coalesce small files)
spark.sql("OPTIMIZE delta.`s3://bucket/tables/orders` ZORDER BY (customer_id, created_at)")

# Clone table (shallow clone for dev/staging)
spark.sql("CREATE TABLE delta.`s3://bucket/tables/orders_clone` SHALLOW CLONE delta.`s3://bucket/tables/orders`")
```

### Iceberg Operations

```bash
# Expire snapshots (remove old data)
spark.sql("ALTER TABLE iceberg_catalog.db.events EXECUTE EXPIRE_SNAPSHOTS")

# Rewrite data files (compaction)
spark.sql("ALTER TABLE iceberg_catalog.db.events EXERCISE REWRITE DATA")

# Rewrite manifest files
spark.sql("ALTER TABLE iceberg_catalog.db.events EXECUTE REWRITE MANIFESTS")

# Migrate Parquet to Iceberg
spark-sql --conf spark.sql.iceberg.handle-timestamp-with-timezone=true \
  --conf "spark.sql.catalog.demo.warehouse=s3://bucket/iceberg/" \
  -f migration.hql

# Rollback to snapshot
spark.sql("ALTER TABLE iceberg_catalog.db.events SET TBLPROPERTIES ('previous-version' = '1234567890')")
```

### Hudi Operations (DeltaStreamer)

```bash
# Run Hudi DeltaStreamer (CDC from Kafka)
spark-submit \
  --class org.apache.hudi.utilities.deltastreamer.HoodieDeltaStreamer \
  /usr/lib/spark/examples/jars/hudi-utilities-scala.jar \
  --table-type COPY_ON_WRITE \
  --source-class org.apache.hudi.utilities.sources.JsonKafkaSource \
  --source-ordering-field timestamp \
  --hoodie-conf hoodie.datasource.write.recordkey.field=id \
  --hoodie-conf hoodie.datasource.write.partitionpath.field=date \
  --hoodie-conf hoodie.datasource.write.precombine.field=timestamp \
  --hoodie-conf hoodie.datasource.write.operation=upsert \
  --hoodie-conf hoodie.deltastreamer.source.kafka.topic=cdc-events \
  --hoodie-conf bootstrap.servers=kafka:9092 \
  --hoodie-conf hoodie.datasource.write.markers.type=http \
  --target-base-path s3://bucket/hudi/tables/orders \
  --target-table orders
```

## 7.4 Version Compatibility

| Component | Version | Notes |
|-----------|---------|-------|
| Delta Lake | 3.0+ | Spark 3.5+, Rust support |
| Delta Lake | 2.4.x | Spark 3.3-3.4, most widely deployed |
| Delta Lake | 2.3.x | Spark 3.2, legacy |
| Apache Iceberg | 1.5.x | Latest stable, Spark 3.5 support |
| Apache Iceberg | 1.4.x | Spark 3.3-3.4, wide adoption |
| Apache Iceberg | 1.3.x | Spark 3.2-3.3 |
| Apache Hudi | 0.14.x | Spark 3.5, Flink 1.18, Hive 3.1 |
| Apache Hudi | 0.13.x | Spark 3.3-3.4 |
| Apache Hudi | 0.12.x | Spark 3.2-3.3 |

| Engine | Iceberg Support | Delta Support | Hudi Support |
|--------|----------------|---------------|--------------|
| Spark 3.5 | Native | Native | Native |
| Flink 1.19+ | flink-connector-iceberg | Delta flink-connector | Hudi flink |
| Trino | Native | delta lake connector | Hudi connector |
| Presto | Iceberg 1.3 | delta lake connector | Hudi connector |
| DuckDB | Iceberg extension | Delta extension | - |
