# Glossary

## Core Concepts

| Term | Definition |
|------|------------|
| **Broker** | Kafka server that stores messages |
| **Topic** | Named stream of messages |
| **Partition** | Ordered, immutable sequence within topic |
| **Replica** | Partition copy for redundancy |
| **Leader** | Broker handling reads/writes |
| **Follower** | Replica syncing from leader |
| **ISR** | In-Sync Replicas |

## Producer & Consumer

| Term | Definition |
|------|------------|
| **Producer** | Client that publishes messages |
| **Consumer** | Client that reads messages |
| **Consumer Group** | Group of consumers sharing load |
| **Offset** | Position in partition |
| **Commit** | Save consumer position |
| **Rebalance** | Reassign partitions to consumers |

## Message & Storage

| Term | Definition |
|------|------------|
| **Message** | Key-value pair with timestamp |
| **Segment** | File storing messages |
| **Log** | Partition storage directory |
| **Retention** | How long messages kept |
| **Compaction** | Deduplication by key |

## Configuration

| Term | Definition |
|------|------------|
| **acks** | Wait for replicas confirmation |
| **retries** | Retry failed sends |
| **batch.size** | Batch messages together |
| **linger.ms** | Wait before sending batch |
| **max.in.flight.requests** | Parallel in-flight |

## Kafka Ecosystem

| Term | Definition |
|------|------------|
| **Kafka Streams** | Stream processing library |
| **Kafka Connect** | Connect to external systems |
| **MirrorMaker** | Replicate between clusters |
| **Schema Registry** | Store Avro/Protobuf schemas |
| **KSQL/k sqlDB** | SQL interface to Kafka |