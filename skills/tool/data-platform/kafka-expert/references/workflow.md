# Troubleshooting Guide

## 8.1 Common Failures

### Producer Failures

| Error | Cause | Fix |
|-------|-------|-----|
| `NotEnoughS replicasException` | ISR below `min.insync.replicas` | Increase ISR, check broker health, reduce `acks` to `1` |
| `RecordTooLargeException` | Message exceeds `max.message.bytes` | Split message, reduce batch size, increase broker limit |
| `TopicAuthorizationException` | ACL denies write | Grant `Write` on topic to producer principal |
| `ProducerFencedException` | Transactional producer fenced by another | Use unique `transactional.id`, ensure one producer per ID |
| `InvalidTopicException` | Topic name contains invalid chars | Use `[a-zA-Z0-9._-]` only |
| `TimeoutException` | Broker overloaded, network issue | Increase `request.timeout.ms`, check broker load |
| `CorruptRecordException` | Schema mismatch, bad deserializer | Use compatible deserializer |

```bash
# Check broker errors
kafka-server-start.sh server.properties 2>&1 | grep ERROR

# Check producer retries
# Enable debug logging:
# log4j.logger.org.apache.kafka.clients.producer=DEBUG
```

### Consumer Failures

| Error | Cause | Fix |
|-------|-------|-----|
| `OffsetOutOfRangeException` | No offset for requested offset | Set `auto.offset.reset=earliest` or `latest` |
| `CommitFailedException` | Rebalance during commit | Increase `session.timeout.ms`, reduce fetch size |
| `WakeupException` | `consumer.wakeup()` called | Expected during shutdown |
| `RebalanceInProgressException` | Consumer group rebalancing | Wait, use `ConsumerRebalanceListener` |
| `AuthenticationFailedException` | Wrong SASL/SSL credentials | Verify certs, keytabs, passwords |
| `NoOffsetForPartitionException` | No committed offset | Set `auto.offset.reset`, seek to beginning |
| `MemberIdRequiredException` | Consumer not yet joined group | Wait for `join` phase, check `session.timeout` |

```bash
# Reset consumer offset
kafka-consumer-groups.sh \
    --bootstrap-server kafka:9092 \
    --group order-processor \
    --topic orders.created \
    --reset-offset --to-earliest --execute

# Reset to specific offset
kafka-consumer-groups.sh \
    --bootstrap-server kafka:9092 \
    --group order-processor \
    --topic orders.created \
    --reset-offset --to-offset 1234567 \
    --execute

# Delete consumer group
kafka-consumer-groups.sh \
    --bootstrap-server kafka:9092 \
    --group order-processor \
    --delete
```

### Broker Failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| Leader not elected | Zookeeper/KRaft controller unavailable | Restart controller, check `controller.quorum.election.timeout.ms` |
| Under-replicated partitions | Broker down, network partition | Restart broker, check ISR |
| Disk full | Retention not aggressive enough | Increase disk, reduce retention, enable cleanup |
| GC pauses causing rebalances | Heap too large / small | Tune GC, set `-XX:+UseG1GC`, heap 8-16GB |
| Controller failover | Original controller down | Normal behavior; verify new controller elected |

```bash
# List under-replicated partitions
kafka-topics.sh --describe --under-replicated --bootstrap-server kafka:9092

# List offline partitions
kafka-topics.sh --describe --under-min-isr --bootstrap-server kafka:9092

# Preferred leader election
kafka-leader-election.sh --bootstrap-server kafka:9092 \
    --all -- election-type preferred

# Verify broker health
kafka-broker-api-versions.sh --bootstrap-server kafka:9092
```

## 8.2 Performance Tuning

### Producer Performance

```properties
# High-throughput producer settings
acks=1                          # For max throughput; use 'all' for durability
compression.type=lz4             # lz4 or zstd for speed; gzip for ratio
batch.size=131072                # 128KB batches
linger.ms=10-50                  # Wait up to 50ms to fill batch
buffer.memory=67108864           # 64MB buffer
max.in.flight.requests.per.connection=5  # With idempotence, prevents ordering

# Batching with batching
producer = KafkaProducer(
    batch_size=131072,
    linger_ms=50,
    compression_type='lz4',
)
```

### Consumer Performance

```properties
# Parallelism = number of partitions
# Tune for throughput

fetch.min.bytes=1               # Immediate fetch
fetch.max.wait.ms=500            # Max wait for fill
max.partition.fetch.bytes=1048576 # 1MB per partition
fetch.max.bytes=52428800         # 50MB total fetch

# Session tuning
session.timeout.ms=30000          # Faster rebalance detection
max.poll.interval.ms=300000      # Longer for slow processing
max.poll.records=500              # Fewer records per poll

# Parallelism tuning
num.network.threads=8             # On broker
num.io.threads=16                # On broker
```

### Broker Performance

```properties
# Sizing guidelines
# Threads: 6 × #disks for io.threads
# Network: 100MB/s per partition with replication

num.io.threads=16
num.network.threads=8
queued.max.requests=500
socket.send.buffer.bytes=102400
socket.receive.buffer.bytes=102400

# Log
log.segment.bytes=1073741824     # 1GB segments
log.index.size.max.bytes=10485760 # 10MB index
```

## 8.3 Monitoring & Observability

### Key Metrics

```bash
# Prometheus JMX Exporter (kafka.yml)
---
jmx_url: service:jmx:rmi:///jndi/rmi://localhost:9999/jmxrmi
lowercaseOutputName: true
lowercaseOutputLabelNames: true
whitelistObjectNames:
  - "kafka.server:*"
  - "kafka.network:*"
  - "kafka.producer:*"
  - "kafka.consumer:*"
rules:
  - pattern: "kafka.server<type=BrokerTopicMetrics, name=MessagesInPerSec>\\w*<>(Count)"
    name: kafka_broker_messages_in_total
```

| Metric | Alert Threshold | Description |
|--------|----------------|-------------|
| `kafka_server_BrokerTopicMetrics_MessagesInPerSec` | Rate > 10K/s normal |
| `kafka_server_BrokerTopicMetrics_BytesInPerSec` | > 100MB/s per broker |
| `kafka_server_KafkaRequestHandlerPool_RequestHandlerAvgIdlePercent` | < 0.1 = overloaded |
| `kafka_server_ReplicaFetcherManager_FollowerFetchLatencyMs_End` | > 100ms = slow follower |
| `kafka_cluster_Partition_Value` | Under-replicated > 0 |
| `kafka_consumer_ConsumerLag_Messages` | Lag > 100K events |
| `kafka_consumer_ConsumerCoordinator_LastGenerationId` | Non-increasing |

### Consumer Lag Monitoring

```python
from kafka import KafkaAdminClient, KafkaConsumer
from kafka.admin import ConfigResource, ConfigResourceType

def get_consumer_lag(bootstrap_servers, group_id):
    consumer = KafkaConsumer(
        bootstrap_servers=bootstrap_servers,
        group_id=group_id,
        enable_auto_commit=False,
    )
    
    partitions = consumer.assignment()
    consumer.end_offsets(partitions)
    
    lag_info = {}
    for tp in partitions:
        committed = consumer.committed(tp)
        end_offset = consumer.end_offsets([tp])[tp]
        
        if committed is not None:
            lag = end_offset - committed
        else:
            lag = None  # No committed offset
        
        lag_info[tp.topic] = {
            'partition': tp.partition,
            'committed_offset': committed,
            'end_offset': end_offset,
            'lag': lag,
        }
    
    consumer.close()
    return lag_info
```

## 8.4 Known Issues & Fixes

| Issue | Versions | Fix |
|-------|----------|-----|
| MirrorMaker2 lag accumulating | 2.8-3.3 | Increase MM2 consumer `fetch.max.bytes` |
| Consumer rebalance timeout | All | Increase `rebalance.timeout.ms`, decrease `max.poll.records` |
| KRaft controller not elected | 3.3-3.4 | Set `controller.quorum.voters` correctly |
| Producer retries causing duplicates | Pre-2.5 | Enable `enable.idempotence=true` |
| Zombie producer fencing | All | Use unique `transactional.id` per producer instance |
| Topic creation via CLI fails silently | 3.0-3.2 | Check `auto.create.topics.enable=true` |
| Offsets not committed on crash | All | Use manual commit with `commitSync()` / `commitAsync()` |
| Broker OOM from large fetch requests | Pre-2.6 | Set `max.partition.fetch.bytes` on consumers |
