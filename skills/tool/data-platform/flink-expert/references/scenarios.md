# Glossary

## Core Flink Concepts

### JobManager
The master process that coordinates Flink applications. Responsibilities: scheduling tasks, coordinating checkpoints, managing task executors, recovering from failures. Contains the ResourceManager and Dispatcher.

### TaskManager
Worker node that executes tasks (subtasks). Registers with JobManager, reports slot availability, and executes dataflow operators. Multiple TMs per cluster.

### Slot
A unit of resource allocation on a TaskManager. Each slot represents a fixed amount of memory and a fraction of CPU. Number of slots per TM = `taskmanager.numberOfTaskSlots`.

### Parallelism
The number of parallel instances of an operator. Set per-operator or globally via `parallelism.default`. Total tasks = parallelism × operator count.

### DataStream
The core API for building unbounded stream processing pipelines. Supports transformations: map, filter, flatMap, keyBy, window, union.

### Table API / SQL
Declarative relational API for streaming and batch data. Unified for both batch and stream processing. Operates on Tables and uses Catalyst-like optimization.

### State
The data maintained by stateful operators across events. Managed state is handled by Flink; operator state is managed by the user. State is checkpointed for fault tolerance.

### Keyed State
State scoped to a key (from keyBy). Maintained per key, automatically partitioned by Flink. Types: ValueState, ListState, MapState, AggregatingState.

### Operator State
State shared across all instances of an operator (no key). Types: ListState, UnionListState, BroadcastState.

### Checkpoint
A consistent snapshot of Flink state (operator state + keyed state) stored in a configured storage (S3, HDFS, etc.). Enables exactly-once processing and recovery from failures.

### Savepoint
A manually triggered, user-named checkpoint. Used for planned upgrades, job migration, and blue-green deployments. Does not expire automatically.

### Exactly-Once Semantics
Flink's strongest processing guarantee. Every event is processed exactly once, even in the presence of failures. Achieved via distributed snapshots (Chandy-Lamport algorithm).

### At-Least-Once Semantics
Events may be processed more than once (duplicates possible) but no events are lost. Achieved by checkpointing sources with periodic offsets.

### Watermark
A marker that declares all events with timestamp < watermark are considered "on time". Used to handle out-of-order events in event time processing.

### Event Time
Processing time based on the timestamp embedded in the event itself. Requires watermarks to handle late data. Deterministic and reproducible.

### Processing Time
Processing time based on the wall clock of the Flink operator. Non-deterministic, but simpler. Not suitable for billing or compliance.

### Window
A grouping of events for aggregation over time or count. Types: Tumbling (fixed size, non-overlapping), Sliding (overlapping), Session (gap-based), Global (single per key).

### Allowed Lateness
The amount of time a window continues to accept late events after the watermark passes the window end. Late events within this window trigger late-fire; after, they are dropped or side-output.

### Side Output
A secondary output stream for late events, errors, or out-of-band data. Allows capturing events that would otherwise be dropped.

### ProcessFunction
The low-level operator API providing fine-grained control over time and state. Extends `KeyedProcessFunction`, `CoProcessFunction`, etc.

### CEP (Complex Event Processing)
Pattern matching over event streams. Uses `CEP.pattern()` API to detect sequences, alternations, and quantifiers in event flows.

### RocksDB State Backend
An embedded key-value store for large state. Persists to local disk/network storage. Supports incremental checkpoints. Default for production stateful jobs.

### HashMap State Backend
In-memory state backend. Faster than RocksDB but limited by heap size. Best for small state and fast access requirements.

### Broadcast State
Special operator state that is replicated to all parallel instances. Used for broadcasting rules, configurations, or reference data to all operators.

### Flink SQL Gateway
REST API server for executing Flink SQL queries interactively. Supports session management, statement execution, and result retrieval.

### Catalog
A metadata store for tables, views, and functions. Flink ships with in-memory catalog; supports HiveCatalog, JDBCCatalog, GenericInMemoryCatalog.

### Table Factory
A pluggable mechanism for creating TableSource and TableSink based on string identifiers and properties. Used by connectors.

### Watermark Strategy
Defines how watermarks are extracted from events and how out-of-orderliness is handled. Configured via `WatermarkStrategy`.

### Chandy-Lamport Algorithm
The distributed snapshot algorithm used by Flink for consistent checkpoints. Coordinates barriers from sources through the DAG.

### Kubernetes Operator (Flink Operator)
K8s-native operator for managing Flink deployments. Handles pod creation, savepoints, upgrades, and scaling declaratively.

### Reactive Mode
Autoscaling mode where TaskManagers are added/removed based on job load. Available in Kubernetes deployments.

## CLI Reference

| Command | Purpose |
|---------|---------|
| `./bin/flink run` | Submit a Flink job |
| `./bin/flink list` | List running jobs |
| `./bin/flink cancel` | Cancel a running job |
| `./bin/flink savepoint` | Trigger a savepoint |
| `./bin/flink stop` | Stop gracefully (with savepoint) |
| `./bin/flink modify` | Rescale or reconfigure job |
| `./bin/flink historyserver` | Start history server |
| `./bin/sql-gateway.sh start` | Start SQL Gateway |
| `./bin/start-cluster.sh` | Start local cluster |
| `./bin/stop-cluster.sh` | Stop local cluster |

## Key Metrics

| Metric | Description |
|--------|-------------|
| `currentInputWatermark` | Lowest watermark received from upstream |
| `currentProcessingTime` | Current processing time |
| `numRecordsInPerSecond` | Input throughput |
| `numRecordsOutPerSecond` | Output throughput |
| `numLateRecordsDropped` | Late records dropped |
| `lastCheckpointDuration` | Last checkpoint time |
| `lastCheckpointSize` | Last checkpoint size |
| `numberOfInProgressCheckpoints` | Concurrent checkpoints |
| `numberOfCompletedCheckpoints` | Completed checkpoint count |
| `numberOfFailedCheckpoints` | Failed checkpoint count |
