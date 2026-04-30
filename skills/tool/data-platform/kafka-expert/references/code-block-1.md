# Producer Config (Python)

Reliable, idempotent Kafka producer with schema awareness.

```python
from confluent_kafka import Producer, KafkaError

producer = Producer({
    'bootstrap.servers': 'kafka-1:9092,kafka-2:9092,kafka-3:9092',
    'client.id': 'order-service-v2',
    
    # Reliability settings
    'acks': 'all',  # Wait for all replicas (critical for production)
    'retries': 3,
    'retry.backoff.ms': 100,
    
    # Idempotence (exactly-once semantics)
    'enable.idempotence': True,
    'max.in.flight.requests.per.connection': 5,
    
    # Performance tuning
    'compression.type': 'snappy',
    'batch.size': 16384,
    'linger.ms': 10,
    'buffer.memory': 33554432,
    
    # Monitoring
    'metric.reporters': 'com.example.MetricsReporter',
})

def delivery_report(err, msg):
    """Callback for delivery confirmation."""
    if err is not None:
        print(f"Delivery failed for {msg.key()}: {err}")
    else:
        print(f"Delivered to {msg.topic()} [{msg.partition()}]")

# Produce message
producer.produce(
    topic='ecommerce.orders.created',
    key='user-123',  # Key determines partition (ordering)
    value=json.dumps(order),
    headers={'correlation-id': str(uuid4())},
    callback=delivery_report,
)

# Flush to ensure delivery
producer.flush()

# Key points:
# - acks='all' is mandatory for production
# - idempotence=True prevents duplicates
# - Compression (snappy/lz4) reduces network usage
# - Always use key for ordering guarantees
```
