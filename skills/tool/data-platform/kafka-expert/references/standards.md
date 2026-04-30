# Standards & Reference

## 7.1 Official Documentation

- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Kafka Core Concepts](https://kafka.apache.org/documentation/#intro_concepts)
- [Kafka Architecture](https://kafka.apache.org/documentation/#majordesignelements)
- [Kafka Protocol](https://kafka.apache.org/protocol)
- [Kafka Streams Documentation](https://kafka.apache.org/documentation/streams/)
- [Kafka Streams API](https://kafka.apache.org/documentation/streams/developer-guide/)
- [Kafka Connect Documentation](https://kafka.apache.org/documentation/#connect)
- [Kafka Security (SASL/SSL)](https://kafka.apache.org/documentation/#security)
- [Kafka Configuration Reference](https://kafka.apache.org/documentation/#configuration)
- [Confluent Documentation](https://docs.confluent.io/)
- [Amazon MSK Developer Guide](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html)

## 7.2 Architecture Patterns

### Topic Design Principles

```
┌─────────────────────────────────────────────────────────────┐
│                   TOPIC DESIGN RULES                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Topic per entity + event type                           │
│     orders.created, orders.updated, orders.cancelled        │
│                                                             │
│  2. Key = entity ID (for ordering)                        │
│     user_id for user events, order_id for orders           │
│                                                             │
│  3. Retention = consumer_lag_tolerance × throughput       │
│                                                             │
│  4. Partitions = max(consumer_count, throughput_target)   │
│                                                             │
│  5. Compact topics for entity state                        │
│     (latest value per key)                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Topic Naming Convention

| Type | Pattern | Example |
|------|---------|---------|
| Event streams | `{domain}.{entity}.{event}` | `orders.created`, `payments.charged` |
| CDC data | `{source}.{schema}.{table}` | `postgres.analytics.orders` |
| Config/state | `{domain}.{entity}.config` | `catalog.product.config` |
| Dead letter | `{original-topic}.dlq` | `orders.created.dlq` |
| Aggregations | `{metric}.{window}` | `revenue.1min`, `orders.5min` |

### Partitioning Strategy

```
Partition Count = ceil(max(throughput_producer / 5, num_consumers))

# Example: 100MB/s producer, 20 consumers
# Partition count = ceil(max(100/5, 20)) = ceil(20) = 20

# Rebalance threshold
# Consumer group rebalances when: new consumer joins, 
# partition count changes, or session.timeout expires
```

### Replication & Fault Tolerance

```
Replication Factor = 3 (minimum for production)
Min ISR = 2 (acknowledge from at least 2 replicas)

Failure Scenarios:
  - Broker failure: Leader election within ISR, < 5ms
  - Leader + follower down: Unavailable until ISR restored
  - Network partition: Broker removed from ISR after replica.lag.max.messages
```

## 7.3 Configuration Reference

### Broker Configuration (server.properties)

```properties
# Listeners
listeners=PLAINTEXT://kafka:9092,SSL://kafka:9093,INTERNAL://kafka:29092
advertised.listeners=PLAINTEXT://kafka.example.com:9092,SSL://kafka.example.com:9093
listener.security.protocol.map=PLAINTEXT:PLAINTEXT,SSL:SSL,INTERNAL:PLAINTEXT

# General
num.network.threads=8
num.io.threads=16
socket.send.buffer.bytes=102400
socket.receive.buffer.bytes=102400
socket.request.max.bytes=104857600

# Log storage
log.dirs=/var/lib/kafka/data
num.partitions=12
num.recovery.threads.per.data.dir=4
log.retention.hours=168
log.retention.bytes=-1
log.segment.bytes=1073741824
log.retention.check.interval.ms=300000
log.cleanup.policy=delete,compact

# Compaction (for entity state topics)
log.cleanup.policy=compact
segment.ms=3600000
min.cleanable.dirty.pct=50
min.compaction.lag.ms=3600000

# Replication
default.replication.factor=3
min.insync.replicas=2
replica.lag.time.max.ms=30000
replica.socket.timeout.ms=30000
replica.socket.receive.buffer.bytes=65536

# Compression
compression.type=producer

# Group coordinator
offsets.topic.replication.factor=3
offsets.topic.segment.bytes=104857600
group.initial.rebalance.delay.ms=3000
```

### Producer Configuration

```python
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    bootstrap_servers=['kafka-1:9092', 'kafka-2:9092', 'kafka-3:9092'],
    
    # Serialization
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: str(k).encode('utf-8'),
    
    # Reliability
    acks='all',               # Wait for all ISRs (strongest)
    retries=3,
    retry_backoff_ms=100,
    max_in_flight_requests_per_connection=5,
    
    # Performance
    compression_type='lz4',
    batch_size=16384,
    linger_ms=10,
    buffer_memory=33554432,
    
    # Idempotence (exactly-once semantics)
    enable_idempotence=True,
    max_in_flight_requests_per_connection=5,
    
    # Timeouts
    request_timeout_ms=30000,
    max_block_ms=60000,
    
    # Partitioning
    partitioner='org.apache.kafka.clients.producer.DefaultPartitioner',
    
    # Security
    security_protocol='SSL',
    ssl_cafile='/certs/ca.pem',
    ssl_certfile='/certs/cert.pem',
    ssl_keyfile='/certs/key.pem',
    ssl_password='secret',
)

# Send with callback
future = producer.send(
    'orders.created',
    key='user_123',
    value={
        'order_id': 'ord_abc',
        'total': 149.99,
        'currency': 'USD',
        'items': ['sku_1', 'sku_2'],
    },
    timestamp=None,      # Use broker time
    headers=[
        ('correlation-id', b'corr_xyz'),
        ('content-type', b'application/json'),
    ],
)

try:
    record_metadata = future.get(timeout=10)
    print(f"Offset: {record_metadata.offset}, "
          f"Partition: {record_metadata.partition}, "
          f"Topic: {record_metadata.topic}")
except KafkaError as e:
    print(f"Failed to send: {e}")
    raise

producer.flush()
producer.close()
```

### Consumer Configuration

```python
from kafka import KafkaConsumer
from kafka.errors import KafkaError

consumer = KafkaConsumer(
    'orders.created',
    bootstrap_servers=['kafka-1:9092', 'kafka-2:9092'],
    
    # Group management
    group_id='order-processor-v2',
    group_instance_id='worker-1',  # Static membership (Kafka 2.4+)
    
    # Offset management
    auto_offset_reset='earliest',     # 'earliest' or 'latest'
    enable_auto_commit=False,         # Manual commit for exactly-once
    auto_commit_interval_ms=5000,
    auto_commit_interval_ms=5000,
    
    # Fetch tuning
    fetch_min_bytes=1,
    fetch_max_bytes=52428800,    # 50MB
    fetch_max_wait_ms=500,
    max_partition_fetch_bytes=1048576,
    
    # Heartbeat & session
    heartbeat_interval_ms=3000,
    session_timeout_ms=45000,
    max_poll_interval_ms=300000,
    
    # Deserialization
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    key_deserializer=lambda k: k.decode('utf-8') if k else None,
    
    # Filtering
    # Use subscribe() for pattern: re.compile('orders\\..*')
    # Use assign() for specific partitions
    # subscribe(pattern='^orders\\..*', callback=on_rebalance)
    
    # Security
    security_protocol='SSL',
    ssl_cafile='/certs/ca.pem',
    ssl_certfile='/certs/cert.pem',
    ssl_keyfile='/certs/key.pem',
)

# Manual commit pattern
for message in consumer:
    try:
        process(message.value)
        consumer.commit()
    except Exception as e:
        send_to_dlq(message, e)
        consumer.commit()  # Commit even on DLQ to avoid blocking

consumer.close()
```

### Kafka Streams Configuration

```java
import org.apache.kafka.streams.StreamsConfig;
import org.apache.kafka.streams.Topology;
import org.apache.kafka.streams.StreamsBuilder;

Properties props = new Properties();
props.put(StreamsConfig.APPLICATION_ID_CONFIG, "order-processor-v1");
props.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "kafka-1:9092,kafka-2:9092");
props.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
props.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());
props.put(StreamsConfig.PROCESSING_GUARANTEE_CONFIG, StreamsConfig.EXACTLY_ONCE_V2);
props.put(StreamsConfig.NUM_STREAM_THREADS_CONFIG, 4);
props.put(StreamsConfig.STATE_DIR_CONFIG, "/var/lib/kafka/streams");
props.put(StreamsConfig.REPLICATION_FACTOR_CONFIG, 3);
props.put(StreamsConfig.COMMIT_INTERVAL_MS_CONFIG, 1000);
props.put(StreamsConfig.CACHE_MAX_BYTES_BUFFERING_CONFIG, 10485760);
props.put(StreamsConfig.MAX_TASK_IDLE_MS_CONFIG, 500);

StreamsBuilder builder = new StreamsBuilder();
KStream<String, Order> orders = builder.stream("orders.created", 
    Consumed.with(Serdes.String(), new OrderSerde()));

orders
    .filter((k, v) -> v.getTotal() > 100)
    .groupByKey()
    .windowedBy(TimeWindows.ofSizeAndGrace(Duration.ofMinutes(5), Duration.ofMinutes(1)))
    .aggregate(
        OrderAccumulator::new,
        (k, v, agg) -> agg.add(v),
        Materialized.as("order-totals"))
    .toStream()
    .to("order_totals_5min", Produced.with(Serdes.String(), new OrderAccumulatorSerde()));

Topology topology = builder.build();
KafkaStreams streams = new KafkaStreams(topology, props);
streams.start();
```

## 7.4 Kafka Connect Reference

### Source Connector (Debezium PostgreSQL CDC)

```json
{
  "name": "pg-orders-source",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "postgres.primary",
    "database.port": "5432",
    "database.user": "debezium",
    "database.password": "${secrets:PG_PASSWORD}",
    "database.dbname": "orders_db",
    "database.server.name": "orders",
    "table.include.list": "public.orders,public.order_items",
    "publication.autocreate.mode": "filtered",
    "slot.name": "debezium_slot",
    "plugin.name": "pgoutput",
    "snapshot.mode": "initial",
    "snapshot.lock.timeout.ms": "86400000",
    "decimal.handling.mode": "double",
    "time.precision.mode": "adaptive",
    "topic.prefix": "orders",
    "topic.per.table.prefix": "orders",
    "transforms": "unwrap,route",
    "transforms.unwrap.type": "io.debezium.transforms.ExtractNewRecordState",
    "transforms.unwrap.drop.tombstones": "false",
    "transforms.route.type": "org.apache.kafka.connect.transforms.RegexRouter",
    "transforms.route.regex": "orders.public.(.*)",
    "transforms.route.replacement": "$1",
    "errors.tolerance": "none",
    "errors.log.enable": "true",
    "errors.log.include.messages": "true"
  }
}
```

### Sink Connector (S3)

```json
{
  "name": "orders-s3-sink",
  "config": {
    "connector.class": "io.confluent.connect.s3.S3SinkConnector",
    "tasks.max": "4",
    "topics": "orders.created,orders.updated",
    "behavior.on.error": "LOG",
    "flush.size": "10000",
    "rotate.interval.ms": "300000",
    "timezone": "UTC",
    "format.class": "io.confluent.connect.s3.format.json.JsonFormat",
    "storage.class": "io.confluent.connect.s3.storage.S3Storage",
    "s3.bucket.name": "data-raw-orders",
    "s3.region": "us-east-1",
    "s3.part.size": "5242880",
    "s3.credentials.provider.class": "com.amazonaws.auth.DefaultInstanceMetadataProvider",
    "partitioner.class": "io.confluent.connect.storage.partitioner.TimeBasedPartitioner",
    "timestamp.extractor": "RecordField",
    "timestamp.field": "ts",
    "path.format": "YYYY/MM/dd/HH",
    "locale": "en-US",
    "store.url": "http://minio:9000",
    "s3.url.format": "http://minio-%d.example.com",
    "deduplicate": "true",
    "deduplication.field": "data.id"
  }
}
```

## 7.5 Version Compatibility

| Version | EOL Date | Key Features |
|---------|----------|--------------|
| 2.8.x | - | KRaft (controller), upgrade from ZK |
| 3.0.x | - | KRaft production-ready, Apache 3.0 protocol |
| 3.1.x | - | Kafka Streams Rack Awareness |
| 3.2.x | - | Scalable checkpointing, improved partition leader election |
| 3.3.x | - | KRaft controller quorum, partition reassignment |
| 3.4.x | - | Self-balanced clusters |
| 3.5.x | - | Tiered storage (preview), Exactly-once source connectors |
| 3.6.x | - | Tiered storage GA, partition balancing |
| 3.7.x | Latest | Partition splitting, Kafka Streams Rack ID |

| Component | Compatible Kafka Versions |
|-----------|--------------------------|
| Confluent Platform | 7.x (Kafka 3.x based) |
| Debezium | 0.10+ for Kafka 2.x, 2.x for Kafka 3.x |
| Kafka Connect | Matches broker version |
| Amazon MSK | Managed Kafka (versions aligned to open source) |
| Strimzi (K8s) | 3.4+ for Kafka 3.5 |
