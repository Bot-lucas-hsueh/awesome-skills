# Consumer Config (Python)

Scalable consumer with proper offset management and exactly-once semantics.

```python
from confluent_kafka import Consumer, KafkaError, KafkaException

consumer = Consumer({
    'bootstrap.servers': 'kafka-1:9092,kafka-2:9092',
    'group.id': 'order-processor-v2',  # Consumer group
    'client.id': 'processor-1',
    
    # Offset management
    'auto.offset.reset': 'earliest',  # Start from beginning if no committed offset
    'enable.auto.commit': False,  # Manual commit for exactly-once
    
    # Processing configuration
    'max.poll.interval.ms': 300000,  # 5 minutes for long processing
    'session.timeout.ms': 30000,
    'heartbeat.interval.ms': 10000,
    'isolation.level': 'read_committed',  # Skip aborted transactions
    
    # Rebalance handling
    'group.instance.id': 'processor-1',  # Static membership (reduces rebalances)
})

consumer.subscribe(['orders.events'])

while True:
    msg = consumer.poll(timeout=1.0)
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            raise KafkaException(msg.error())

    try:
        # Process message
        process(msg.value())
        
        # Commit offset after successful processing
        consumer.commit(msg)
    except Exception as e:
        # Handle failure: don't commit, will reprocess
        log.error(f"Failed to process {msg.key()}: {e}")
        raise

consumer.close()

# Key points:
# - Manual commit for exactly-once semantics
# - isolation.level='read_committed' skips aborted transactions
# - Static membership reduces rebalance pauses
# - Always commit after successful processing
```
