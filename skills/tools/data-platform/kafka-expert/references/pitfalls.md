# Examples

## 10.1 Topic Design Examples

### E-commerce Event Topics

```bash
# Create topics with appropriate partition counts
kafka-topics.sh --create \
    --bootstrap-server kafka:9092 \
    --topic orders.created \
    --partitions 12 \
    --replication-factor 3 \
    --config retention.ms=604800000 \
    --config cleanup.policy=delete

kafka-topics.sh --create \
    --bootstrap-server kafka:9092 \
    --topic orders.updated \
    --partitions 12 \
    --replication-factor 3 \
    --config retention.ms=2592000000 \
    --config cleanup.policy=delete

# Log-compacted topic for product catalog (latest per key)
kafka-topics.sh --create \
    --bootstrap-server kafka:9092 \
    --topic catalog.products \
    --partitions 6 \
    --replication-factor 3 \
    --config cleanup.policy=compact \
    --config retention.ms=-1 \
    --config min.cleanable.dirty.pct=50

# CDC topic from PostgreSQL
kafka-topics.sh --create \
    --bootstrap-server kafka:9092 \
    --topic postgres.public.orders \
    --partitions 12 \
    --replication-factor 3 \
    --config retention.ms=604800000
```

## 10.2 Producer Examples

### Reliable Producer with DLQ

```python
import json
import logging
from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import KafkaError

logger = logging.getLogger(__name__)

class ReliableProducer:
    def __init__(self, bootstrap_servers):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            acks='all',
            enable_idempotence=True,
            retries=5,
            retry_backoff_ms=500,
            compression_type='lz4',
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8') if k else None,
            max_in_flight_requests_per_connection=5,
        )
        self.dlq_producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            acks='all',
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        )

    def send_with_dlq(self, topic, key, value):
        try:
            future = self.producer.send(topic, key=key, value=value)
            future.get(timeout=30)
        except KafkaError as e:
            logger.error(f"Failed to send to {topic}: {e}")
            self._send_to_dlq(topic, key, value, str(e))

    def _send_to_dlq(self, original_topic, key, value, error):
        dlq_topic = f"{original_topic}.dlq"
        dlq_message = {
            'original_topic': original_topic,
            'original_key': key,
            'original_value': value,
            'error': error,
        }
        self.dlq_producer.send(dlq_topic, key=key, value=dlq_message)
        self.dlq_producer.flush()

    def close(self):
        self.producer.flush()
        self.producer.close()
        self.dlq_producer.flush()
        self.dlq_producer.close()
```

### Transactional Producer (Exactly-Once)

```python
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    acks='all',
    enable_idempotence=True,
    transactional_id='order-processor-1',  # Unique per producer instance
    max_in_flight_requests_per_connection=5,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

# Wrap in transaction
try:
    producer.init_transactions()
    producer.begin_transaction()
    
    producer.send('orders.created', key='user_123', value={'order_id': 'ord_1', 'total': 99.99})
    producer.send('inventory.decrement', key='ord_1', value={'sku': 'ABC', 'qty': -1})
    
    # Commit both atomically
    producer.commit_transaction()
except Exception as e:
    producer.abort_transaction()
    raise
```

## 10.3 Consumer Examples

### Consumer with Graceful Shutdown

```python
import signal
import sys
from kafka import KafkaConsumer
from kafka.errors import KafkaError

running = True

def signal_handler(signum, frame):
    global running
    print("Shutdown signal received")
    running = False

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

consumer = KafkaConsumer(
    'orders.created',
    bootstrap_servers=['kafka:9092'],
    group_id='order-processor-v2',
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    max_poll_records=100,
    session_timeout_ms=30000,
    heartbeat_interval_ms=10000,
)

try:
    while running:
        batch = consumer.poll(timeout_ms=1000, max_records=100)
        
        for tp, records in batch.items():
            for record in records:
                try:
                    process_order(record.value)
                except Exception as e:
                    handle_failure(record, e)
            
            # Commit after each partition batch
            consumer.commit()
finally:
    consumer.close()
    print("Consumer closed")
```

### Interactive Query with Kafka Streams

```java
// Kafka Streams interactive query for service mesh
Properties props = new Properties();
props.put(StreamsConfig.APPLICATION_ID_CONFIG, "inventory-service");
props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "kafka:9092");
props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.Long().getClass());
props.put(StreamsConfig.PROCESSING_GUARANTEE_CONFIG, StreamsConfig.EXACTLY_ONCE_V2);

// State store with caching
StoreBuilder<KeyValueStore<String, Long>> storeBuilder =
    Stores.keyValueStoreBuilder(
        Stores.persistentCountStore("inventory-counts"),
        Serdes.String(),
        Serdes.Long()
    );

config.put(StreamsConfig.STATE_DIR_CONFIG, "/var/lib/kafka/streams");

StreamsBuilder builder = new StreamsBuilder();
builder.addStateStore(storeBuilder);

KStream<String, InventoryUpdate> updates = builder.stream("inventory.updates");

updates
    .groupByKey()
    .aggregate(
        () -> 0L,
        (k, v, total) -> total + v.getDelta(),
        Materialized.<String, Long>as("inventory-counts")
            .withKeySerde(Serdes.String())
            .withValueSerde(Serdes.Long())
            .withCachingEnabled()
    );

KafkaStreams streams = new KafkaStreams(builder.build(), props);
streams.start();

// Expose via REST for other services
RestService rest = new RestService(streams);
rest.start();
```

## 10.4 Kafka Connect Examples

### JDBC Source Connector (Poll-based)

```json
{
  "name": "jdbc-orders-source",
  "config": {
    "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
    "tasks.max": "4",
    "connection.url": "jdbc:postgresql://db:5432/orders?user=reader&password=secret",
    "table.whitelist": "orders,order_items",
    "mode": "timestamp+incrementing",
    "incrementing.column.name": "id",
    "timestamp.column.name": "updated_at",
    "poll.interval.ms": "10000",
    "batch.max.rows": "1000",
    "topic.prefix": "pg",
    "transforms": "addTopicSuffix",
    "transforms.addTopicSuffix.type": "org.apache.kafka.connect.transforms.RegexRouter",
    "transforms.addTopicSuffix.regex": "pg.(.*)",
    "transforms.addTopicSuffix.replacement": "$1"
  }
}
```

### Elasticsearch Sink Connector

```json
{
  "name": "orders-es-sink",
  "config": {
    "connector.class": "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
    "tasks.max": "3",
    "topics": "orders.created,orders.updated",
    "connection.url": "http://elasticsearch:9200",
    "connection.username": "elastic",
    "connection.password": "${secrets:ES_PASSWORD}",
    "type.name": "_doc",
    "key.ignore": "false",
    "schema.enable": "false",
    "behavior.on.null.values": "delete",
    "behavior.on.malformed.documents": "log",
    "write.method": "UPSERT",
    "index.name.pattern": "orders-${topic}",
    "bulk.size": "500",
    "flush.timeout.ms": "10000",
    "transforms": "extractId",
    "transforms.extractId.type": "org.apache.kafka.connect.transforms.HoistField$Key",
    "transforms.extractId.field": "order_id"
  }
}
```

## 10.5 ksqlDB / Kafka Streams SQL Examples

```sql
-- Create stream from topic
CREATE STREAM orders_created (
    order_id VARCHAR,
    customer_id VARCHAR,
    total DOUBLE,
    currency VARCHAR,
    items ARRAY<VARCHAR>,
    ts TIMESTAMP
) WITH (
    kafka_topic = 'orders.created',
    value_format = 'JSON',
    timestamp = 'ts'
);

-- Tumbling window aggregation
SELECT
    customer_id,
    COUNT(*) AS order_count,
    SUM(total) AS total_spent,
    EARLIEST_BY_OFFSET(total) AS first_order_value,
    WINDOWSTART AS window_start,
    WINDOWEND AS window_end
FROM orders_created
WHERE currency = 'USD'
GROUP BY customer_id
    EMIT CHANGES;

-- Session window for user behavior
SELECT
    customer_id,
    COUNT(*) AS page_views,
    COUNT_DISTINCT(page_url) AS unique_pages
FROM page_views
GROUP BY customer_id
    SESSION BY ts WITH (SESSION_GAP = '30 seconds')
    EMIT CHANGES;

-- Join streams
CREATE STREAM enriched_orders AS
SELECT
    o.order_id,
    o.customer_id,
    o.total,
    p.loyalty_tier,
    p.lifetime_value_segment
FROM orders_created o
    LEFT JOIN customers c
        ON o.customer_id = c.customer_id
    WITHIN 5 MINUTES
    ON o.customer_id = c.customer_id
EMIT CHANGES;

-- Table for materialized view
CREATE TABLE customer_metrics AS
SELECT
    customer_id,
    COUNT(*) AS total_orders,
    SUM(total) AS lifetime_value,
    MAX(ts) AS last_order_at
FROM orders_created
GROUP BY customer_id
EMIT CHANGES;
```

## 10.6 Capacity Planning Examples

```python
# Partition count calculator
def calculate_partitions(
    target_throughput_mbps: float,
    producer_count: int,
    consumer_count: int,
    records_per_second: int,
    avg_record_size_bytes: int,
) -> int:
    throughput_per_partition_mbps = 5  # conservative estimate
    
    partitions_by_throughput = int(
        target_throughput_mbps / throughput_per_partition_mbps
    )
    partitions_by_consumers = consumer_count
    partitions_by_producers = producer_count * 4  # 1-4 partitions per producer
    
    return max(
        partitions_by_throughput,
        partitions_by_consumers,
        partitions_by_producers,
    )

# Example: 1000 orders/s, avg 1KB each
# 1 producer, 20 consumers
# Target: 10MB/s throughput
import math
partitions = calculate_partitions(
    target_throughput_mbps=10,
    producer_count=1,
    consumer_count=20,
    records_per_second=1000,
    avg_record_size_bytes=1024,
)
print(f"Recommended partitions: {math.ceil(partitions)}")
```

### Retention Calculator

```python
def calculate_retention_bytes(
    throughput_mbps: float,
    retention_hours: int,
    replication_factor: int,
    partition_count: int,
) -> int:
    """
    Calculate required disk space for topic retention.
    
    Returns: total bytes per broker
    """
    bytes_per_second = throughput_mbps * 1_000_000 / 8
    total_seconds = retention_hours * 3600
    total_raw_bytes = bytes_per_second * total_seconds
    
    # Account for replication and partition overhead
    total_with_replication = total_raw_bytes * replication_factor
    overhead_factor = 1.10  # Index, segment alignment
    
    bytes_per_broker = (total_with_replication * overhead_factor) / partition_count
    
    return int(bytes_per_broker)

# Example: 5 MB/s, 7 days retention, RF=3, 12 partitions
retention = calculate_retention_bytes(
    throughput_mbps=5,
    retention_hours=168,
    replication_factor=3,
    partition_count=12,
)
print(f"Bytes per broker: {retention / 1e9:.1f} GB")
```
