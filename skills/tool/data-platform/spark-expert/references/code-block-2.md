# python Example

```
from pyspark.sql.functions import *

streaming_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "orders.events") \
    .option("startingOffsets", "latest") \
    .load()

parsed = streaming_df \
    .select(from_json(col("value").cast("string"), order_schema).alias("data")) \
    .select("data.*")

# Tumbling window aggregation with watermark
agg = parsed \
    .withWatermark("created_at", "5 minutes") \
    .groupBy(
        window("created_at", "5 minutes"),
        "customer_id"
    ) \
    .agg(
        count("*").alias("order_count"),
        sum("amount").alias("total_amount"),
    )

# Write to console for testing, or Delta for production
query = agg.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "s3://checkpoints/orders_agg/") \
    .table("analytics.orders_5min")
```
