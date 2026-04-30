# Examples

## 10.1 ETL Pipeline Examples

### Incremental ETL with Audit

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, lit, current_timestamp, to_date, when, coalesce, greatest
)
from pyspark.sql.window import Window
import delta

spark = SparkSession.builder \
    .appName("order-etl") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Configuration
INPUT_PATH = "s3a://data/raw/orders"
OUTPUT_PATH = "s3a://data/warehouse/orders"
CHECKPOINT_PATH = "s3a://spark/checkpoints/orders"

# Read incremental data
def extract(batch_id, batch):
    df = spark.read.format("delta").load(f"{INPUT_PATH}/_rescued")
    
    last_processed = (
        spark.read.format("delta")
        .load(f"{OUTPUT_PATH}/_metadata")
        .filter(col("table_name") == "orders")
        .select(coalesce(max("last_processed_at"), lit("1900-01-01")))
        .first()[0]
    )
    
    new_records = df.filter(col("updated_at") > lit(last_processed))
    return new_records

# Transform
def transform(df):
    return df \
        .withColumn("order_date", to_date(col("created_at"))) \
        .withColumn("order_year", col("order_date").substr(0, 4)) \
        .withColumn("order_month", col("order_date").substr(0, 7)) \
        .withColumn("is_valid", 
            when(col("total") > 0, True)
            .when(col("status") == "refunded", True)
            .otherwise(False)
        ) \
        .withColumn("processed_at", current_timestamp()) \
        .select(
            "order_id", "customer_id", "order_date",
            "order_year", "order_month",
            "status", "total", "currency",
            "item_count", "is_valid", "processed_at"
        )

# Load with SCD Type 1 (overwrite)
def load(df, output_path):
    df.write \
        .mode("overwrite") \
        .partitionBy("order_year", "order_month") \
        .format("delta") \
        .option("overwriteSchema", "true") \
        .save(output_path)

# Update metadata
def update_metadata(output_path, last_processed):
    metadata_df = spark.createDataFrame([{
        "table_name": "orders",
        "last_processed_at": last_processed,
        "processed_at": current_timestamp(),
    }])
    
    metadata_df.write \
        .mode("merge") \
        .format("delta") \
        .option("mergeSchema", "true") \
        .save(f"{output_path}/_metadata")

# Main
if __name__ == "__main__":
    # Read
    new_data = spark.read.parquet(INPUT_PATH)
    
    # Transform
    transformed = transform(new_data)
    
    # Write
    load(transformed, OUTPUT_PATH)
    
    # Update metadata
    max_updated = transformed.agg({"updated_at": "max"}).first()[0]
    update_metadata(OUTPUT_PATH, max_updated)
```

### Slowly Changing Dimension (SCD) Type 2

```python
from pyspark.sql.functions import col, row_number, max as spark_max

def scd_type2(
    spark: SparkSession,
    source_df: "DataFrame",
    target_path: str,
    primary_key: str,
    change_cols: list,
    effective_from: str = "updated_at",
):
    """
    SCD Type 2: Keep full history of changes.
    """
    # Read existing
    try:
        target_df = spark.read.format("delta").load(target_path)
    except Exception:
        # First run - load all as new
        return source_df.withColumn("version", lit(1)) \
            .withColumn("is_current", lit(True)) \
            .withColumn("effective_from", col(effective_from)) \
            .withColumn("effective_to", lit(None).cast("timestamp"))
    
    # Find changed and new rows
    changes = source_df.alias("s").join(
        target_df.filter("is_current = True").alias("t"),
        col(f"s.{primary_key}") == col(f"t.{primary_key}"),
        "left"
    ).where(
        f"t.{primary_key} IS NULL OR { ' OR '.join([f's.{c} <> t.{c}' for c in change_cols]) }"
    ).select("s.*")
    
    # Close out old versions
    closed_out = target_df.alias("t").join(
        changes.select(col(primary_key)).alias("c"),
        col(f"t.{primary_key}") == col(f"c.{primary_key}"),
    ).where("t.is_current = True") \
     .withColumn("is_current", lit(False)) \
     .withColumn("effective_to", current_timestamp())
    
    # New versions
    max_version = target_df.agg(spark_max("version")).first()[0] or 0
    new_versions = changes \
        .withColumn("version", lit(max_version + 1)) \
        .withColumn("is_current", lit(True)) \
        .withColumn("effective_from", col(effective_from)) \
        .withColumn("effective_to", lit(None).cast("timestamp"))
    
    # Combine
    return target_df.unionByName(closed_out).unionByName(new_versions)
```

## 10.2 Streaming Examples

### Structured Streaming from Kafka

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, from_json, window, count, sum as spark_sum,
    avg, current_timestamp, to_timestamp
)
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

spark = SparkSession.builder \
    .appName("realtime-analytics") \
    .config("spark.sql.streaming.checkpointLocation", "s3a://spark/checkpoints") \
    .getOrCreate()

# Schema
order_schema = StructType([
    StructField("order_id", StringType(), False),
    StructField("customer_id", StringType(), False),
    StructField("total", DoubleType(), False),
    StructField("currency", StringType(), True),
    StructField("ts", StringType(), False),
])

# Read from Kafka
orders = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "orders.created,orders.updated") \
    .option("startingOffsets", "latest") \
    .option("failOnDataLoss", "false") \
    .load() \
    .select(
        from_json(col("value").cast("string"), order_schema).alias("data"),
        col("timestamp").alias("event_time"),
        col("topic"),
    ) \
    .select("data.*", "event_time", "topic")

# Tumbling window aggregation
revenue_stream = orders \
    .withWatermark("event_time", "30 seconds") \
    .filter(col("currency") == "USD") \
    .groupBy(
        window(col("event_time"), "5 minutes"),
        col("topic")
    ) \
    .agg(
        count("*").alias("order_count"),
        spark_sum("total").alias("total_revenue"),
        avg("total").alias("avg_order_value"),
    ) \
    .select(
        col("window.start").alias("window_start"),
        col("window.end").alias("window_end"),
        "topic",
        "order_count",
        "total_revenue",
        "avg_order_value",
    )

# Write to Delta
query = revenue_stream.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "s3a://spark/checkpoints/revenue") \
    .trigger(processingTime="1 minute") \
    .start("s3a://data/analytics/revenue_5min")

query.awaitTermination()
```

### Streaming Join with Late Arrival Handling

```python
# Orders stream with watermark
orders = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "orders") \
    .load() \
    .select(
        from_json(col("value").cast("string"), order_schema).alias("data"),
        col("timestamp").alias("order_time"),
    ) \
    .select("data.*", "order_time") \
    .withWatermark("order_time", "30 minutes")

# Customer dimension (static, broadcast)
customers = spark.read.parquet("s3a://data/dimensions/customers")

# Streaming join
enriched = orders.join(
    broadcast(customers),
    orders.customer_id == customers.customer_id,
    "left"
)

# Handle late arrivals with append mode + watermark
late_orders = orders \
    .filter(col("order_time") < current_timestamp() - expr("INTERVAL 2 HOURS"))
```

## 10.3 Performance Examples

### Broadcast Join Pattern

```python
from pyspark.sql.functions import broadcast

# Small dimension table (< 100MB)
# Auto-detected and broadcast, but explicit is clearer
large_df = spark.read.parquet("s3a://data/facts/orders")
dim_products = spark.read.parquet("s3a://data/dimensions/products")

result = large_df.join(
    broadcast(dim_products),
    "product_id",
    "left"
)

# Write with broadcast
result.write \
    .mode("overwrite") \
    .option("spark.sql.adaptive.coalescePartitions.enabled", True) \
    .parquet("s3a://data/output")

# Explicit broadcast hint in SQL
spark.sql("""
    SELECT /*+ BROADCAST(p) */ o.*, p.category
    FROM orders o
    JOIN products p ON o.product_id = p.id
""")
```

### Optimize for Skewed Joins

```python
# Detect skew
# In Spark UI, check for stages with one task much larger than others

# Solution 1: Broadcast smaller side
skewed.join(
    broadcast(small_df),
    "key"
)

# Solution 2: Add salting
from pyspark.sql.functions import expr

SALT_FACTOR = 100

# Salt the large side
salted_large = large_df.withColumn(
    "salt", 
    expr(f"floor(rand() * {SALT_FACTOR})")
).withColumn(
    "key_salted",
    expr("CONCAT(key, '-', salt)")
)

# Duplicate small side
small_exploded = small_df.withColumn(
    "salt_range", 
    expr(f"explode(array(range({SALT_FACTOR})))")
).withColumn(
    "key_salted",
    expr("CONCAT(key, '-', salt_range)")
)

# Join
result = salted_large.join(
    small_exploded,
    "key_salted",
    "left"
).drop("salt", "key_salted")
```

### Partition Management

```python
# Before aggregation - optimize partition count
df = spark.read.parquet("s3a://data/large_table")

# Current partitions
print(f"Partitions before: {df.rdd.getNumPartitions()}")

# Repartition by join key for better shuffle
df_repartitioned = df.repartition(200, "customer_id")

# Coalesce after filtering to reduce overhead
df_filtered = df_repartitioned.filter(col("status") == "active")
df_coalesced = df_filtered.coalesce(50)  # Reduce without shuffle

# Write with controlled partition count
df.write \
    .mode("overwrite") \
    .partitionBy("year", "month", "day") \
    .option("maxRecordsPerFile", 1000000) \
    .parquet("s3a://data/output/")

# Dynamic partition overwrite (Spark 3.2+)
df.write \
    .mode("overwrite") \
    .partitionBy("year", "month") \
    .option("partitionOverwriteMode", "dynamic") \
    .parquet("s3a://data/output/")
```

## 10.4 Testing Examples

```python
import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType

@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder \
        .master("local[2]") \
        .appName("pytest") \
        .config("spark.sql.shuffle.partitions", 4) \
        .getOrCreate()

def test_order_aggregation(spark):
    schema = StructType([
        StructField("order_id", StringType(), False),
        StructField("customer_id", StringType(), False),
        StructField("total", DoubleType(), False),
        StructField("status", StringType(), False),
    ])
    
    data = [
        ("o1", "c1", 100.0, "completed"),
        ("o2", "c1", 50.0, "completed"),
        ("o3", "c2", 200.0, "cancelled"),
        ("o4", "c1", 75.0, "completed"),
    ]
    
    df = spark.createDataFrame(data, schema)
    
    result = df.filter(col("status") == "completed") \
        .groupBy("customer_id") \
        .agg(
            count("*").alias("order_count"),
            sum("total").alias("lifetime_value"),
        )
    
    assert result.count() == 2
    
    c1_row = result.filter(col("customer_id") == "c1").first()
    assert c1_row["order_count"] == 3
    assert c1_row["lifetime_value"] == 225.0
```
