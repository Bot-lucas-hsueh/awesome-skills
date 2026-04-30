# python Example

```
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("ETL Pipeline") \
    .config("spark.sql.shuffle.partitions", 200) \
    .config("spark.sql.adaptive.enabled", True) \
    .config("spark.sql.adaptive.coalescePartitions.enabled", True) \
    .getOrCreate()

# Read with explicit schema (never infer)
schema = StructType([
    StructField("order_id", StringType(), False),
    StructField("customer_id", StringType(), False),
    StructField("amount", DoubleType(), False),
    StructField("status", StringType(), True),
    StructField("created_at", TimestampType(), False),
])

df = spark.read \
    .schema(schema) \
    .parquet("s3://data/orders/")

# Transform with filter-early pattern
result = df \
    .filter(col("status") == "completed") \
    .filter(col("created_at") >= lit("2024-01-01")) \
    .groupBy("customer_id", "status") \
    .agg(
        sum("amount").alias("total_spent"),
        count("*").alias("order_count"),
        avg("amount").alias("avg_order_value"),
    )

# Broadcast join for small dimension
result = result.join(
    broadcast(dim_customers.select("customer_id", "customer_name")),
    "customer_id"
)

# Write with partitioning and compression
result.write \
    .mode("overwrite") \
    .option("compression", "snappy") \
    .partitionBy("year", "month") \
    .parquet("s3://output/analytics/orders_summary/")
```
