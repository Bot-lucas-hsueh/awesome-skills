# Glossary

## Core Kafka Concepts

### Broker
A Kafka server that stores messages and serves producers and consumers. A Kafka cluster consists of multiple brokers. Each broker is identified by its integer ID.

### Topic
A named stream of records. Producers write to topics, consumers read from topics. Topics are divided into partitions for scalability and parallelism.

### Partition
A unit of parallelism in Kafka. Each partition is an ordered, immutable sequence of records. Partitions are replicated across brokers for fault tolerance. Records within a partition are ordered by offset.

### Offset
A monotonically increasing integer assigned to each record within a partition. Offsets are the primary mechanism for consumer position tracking. Not reused across segments.

### Producer
An application that publishes records to Kafka topics. Producers choose which partition to write to (by key or round-robin) and handle serialization.

### Consumer
An application that subscribes to topics and processes records. Consumers belong to consumer groups and track their position via offsets.

### Consumer Group
A set of consumers cooperating to consume messages from a topic. Partitions are distributed among consumers in the group. Each record is delivered to exactly one consumer in the group.

### Replication Factor
The number of copies of each partition across brokers. A replication factor of 3 means 3 copies: 1 leader + 2 followers. Default in production is typically 3.

### ISR (In-Sync Replicas)
The set of replicas that are fully caught up with the leader. Consists of the leader and all followers that have fully replicated records. `min.insync.replicas` defines the minimum required.

### Leader / Follower
Leader handles all reads/writes for a partition. Followers replicate records from the leader. If leader fails, an in-sync follower becomes the new leader.

### Record (Message)
The basic unit of data in Kafka. Consists of:
- **Key** (optional): Used for partitioning
- **Value**: The payload
- **Headers**: Key-value metadata
- **Timestamp**: Producer or broker time
- **Offset**: Position in partition

### Timestamp
Either `CreateTime` (set by producer) or `LogAppendTime` (set by broker). Used for retention policy and windowed aggregations.

### Retention
How long Kafka retains messages. Configured per topic via `log.retention.hours`, `log.retention.bytes`. After retention, messages are deleted or compacted (for log-compacted topics).

### Log Compaction
A retention policy that retains only the latest message per key within a topic. Used for building materialized views and key-value state.

### Producer Transaction
A mechanism for exactly-once delivery from producer to Kafka. Uses `transactional.id` and `acks=all`. All messages in a transaction are committed atomically.

### Consumer Rebalance
The process of reassigning partition ownership among consumers in a group. Triggers when a consumer joins, leaves, or fails. During rebalance, no records are consumed.

### Exactly-Once Semantics (EOS)
Kafka supports exactly-once delivery:
- **Producer**: `enable.idempotence=true` prevents duplicate sends
- **Consumer**: Disable auto-commit, use manual commit with transactions
- **Kafka Streams**: `processing.guarantee=exactly_once_v2`

### Lag
The difference between the latest offset and the consumer's committed offset. High lag indicates the consumer is falling behind producers. Monitor via `consumer_lag_seconds` metric.

### KRaft
Kafka's native consensus protocol replacing ZooKeeper. Uses the Raft algorithm for controller election and metadata management. Became default in Kafka 3.4.

### ZooKeeper (Deprecated)
External coordination service used by Kafka pre-3.4 for controller election, access control, and metadata management. Deprecated in favor of KRaft.

### Schema Registry
A service for managing Avro/Protobuf/JSON schemas. Ensures producers and consumers agree on message formats. Key for schema evolution without breaking compatibility.

### Kafka Connect
A framework for integrating Kafka with external systems. Consists of **Source Connectors** (ingest) and **Sink Connectors** (egress). Runs as distributed workers.

### Debezium
An open-source CDC (Change Data Capture) platform that streams database changes into Kafka. Supports MySQL, PostgreSQL, MongoDB, SQL Server, and more.

### Kafka Streams
A client library for building stream processing applications. Provides stateful operators (join, aggregate, window), exactly-once semantics, and runs as a standard Kafka consumer.

### MirrorMaker 2
Kafka's cross-cluster replication tool. Replicates topics between clusters with support for topic renaming, offset mapping, and active-passive or active-active configurations.

### Connector Configuration

| Parameter | Description |
|-----------|-------------|
| `tasks.max` | Number of parallel connector tasks |
| `topics` | Topics to consume/produce |
| `connector.class` | FQN of the connector class |
| `transforms` | Chain of Single Message Transforms |
| `predicates` | Conditions for transforms |
| `errors.tolerance` | `none` or `all` for error handling |
| `errors.deadletterqueue` | Send failed records to DLQ topic |

## CLI Reference

| Command | Purpose |
|---------|---------|
| `kafka-topics.sh --create` | Create a topic |
| `kafka-topics.sh --describe` | List topic details |
| `kafka-topics.sh --alter` | Modify topic config |
| `kafka-topics.sh --delete` | Delete a topic |
| `kafka-console-producer.sh` | Produce from stdin |
| `kafka-console-consumer.sh` | Consume from stdin |
| `kafka-consumer-groups.sh` | Manage consumer groups |
| `kafka-dump-log.sh` | Inspect segment files |
| `kafka-producer-perf-test.sh` | Throughput benchmark |
| `kafka-consumer-perf-test.sh` | Consumer benchmark |
| `kafka-reassign-partitions.sh` | Move partitions |
| `kafka-leader-election.sh` | Trigger leader election |
| `kafka-configs.sh` | Update broker/topic configs |
