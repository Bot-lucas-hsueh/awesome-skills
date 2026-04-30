# Troubleshooting Guide

## 8.1 Common Failures

### Checkpoint & State Failures

| Error | Cause | Fix |
|-------|-------|-----|
| `CheckpointExponentialBackoffNano - Checkpoint Coordinator received` | Checkpoint timeout, TM overloaded | Increase `execution.checkpointing.timeout`, check state size |
| `Could not materialize checkpoint stream` | RocksDB write buffer full | Increase `state.backend.rocksdb.writebuffer.size`, enable incremental checkpoint |
| `java.io.IOException: Too many open files` | File descriptor limit on TM | Increase `ulimit -n`, check RocksDB `max_open_files` |
| `Exception in RPC` | TM lost, network partition | Increase `taskmanager.network.memory.fraction`, check network |
| `State migration error after savepoint` | Schema changed incompatible | Use `state.schemaEvolution` or restart from latest checkpoint |

```bash
# Check checkpoint history
curl http://jobmanager:8081/jobs/<job-id>/checkpoints

# Restart from checkpoint
./bin/flink run -s checkpoint_path ./job.jar

# Restart from savepoint
./bin/flink run -d -s s3://bucket/savepoints/<path> ./job.jar
```

### Watermark & Late Data Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| Late events silently dropped | Watermark too aggressive | Increase watermark grace period: `ts - INTERVAL '5' MINUTE` |
| Aggregation never fires | Watermark not advancing | Check timestamp extraction; events may be out of order |
| Late data in metrics | `allowedLateness` not set | Set `allowedLateness` on window |

```sql
-- Set proper watermark and allowed lateness
CREATE TABLE events (
    user_id STRING,
    ts TIMESTAMP(3),
    WATERMARK FOR ts AS ts - INTERVAL '5' SECOND
) WITH ('connector' = 'kafka', ...);

-- In DataStream API
TumblingEventTimeWindows.of(Time.minutes(5))
    .allowedLateness(Time.minutes(1))  -- Keep state for late data
    .sideOutputLateData(lateOutputTag)  -- Capture late events
```

### Memory & Resource Issues

| Error | Cause | Fix |
|-------|-------|-----|
| `OutOfMemoryError: RocksDB` | State too large | Enable `state.backend.rocksdb.memory.managed`, increase TM memory |
| `Native memory allocation failure` | Off-heap memory limit | Increase `taskmanager.memory.task.heap.size`, use `state.backend.rocksdb.memory.managed` |
| `TaskManager JVM heap exhausted` | Too many parallel tasks | Reduce `parallelism.default`, increase TM heap |
| `TM OOMKilled (exit 137)` | K8s memory limit exceeded | Increase container memory: `taskmanager.memory.process.size` |

```yaml
# Kubernetes TM resource config
taskmanager.memory.process.size: 4g
taskmanager.memory.managed.size: 2g
taskmanager.numberOfTaskSlots: 4
```

### Job Failure & Restart

| Error | Cause | Fix |
|-------|-------|-----|
| `Job submitted but status became FAILED` | JAR version mismatch | Re-upload JAR, check Flink version compatibility |
| `No resources available to schedule tasks` | Not enough TM slots | Add TMs, reduce parallelism, increase slots per TM |
| `Deployment failed: OOMKilled` | K8s memory limit | Increase memory limits in deployment |
| `Slot request not satisfiable` | TM slots exhausted | Check active job slots, wait for resource |

## 8.2 Performance Tuning

### State Backend Selection

```yaml
# HashMap (for small state, fastest)
state.backend: hashmap
# Best for: < 100MB state, stateless-ish jobs, state access heavy

# RocksDB (for large state, persistent)
state.backend: rocksdb
state.backend.incremental: true
state.backend.rocksdb.memory.managed: true
state.backend.rocksdb.writebuffer.size: 64mb
state.backend.rocksdb.writebuffer.count: 4
state.backend.rocksdb.compaction.level.maxsize-level-base: 320MB

# TTL for state cleanup
state TTL:
  time_characteristics: EventTime
  default_szie: 128
  cleanup_in_rdbstate_handle_increment_filter_nanos: 60000000000
```

### Parallelism & Resource Allocation

```java
// Optimal parallelism formula
// parallelism = max_throughput / (records_per_second_per_slot)
int sourceParallelism = Math.min(sourcePartitionCount, maxParallelism);
int operatorParallelism = Math.max(numTaskSlots, desiredThroughput / recordsPerSecond);

// Set per-operator parallelism
env.fromSource(kafka, watermarkStrategy, "Kafka Source")
    .setParallelism(4)
    .keyBy(...)
    .process(new Processor())
    .setParallelism(8)
    .sinkTo(kafkaSink)
    .setParallelism(4);

// Or via SQL
INSERT INTO sink SELECT ... FROM source
/*+ OPTIONS('sink.parallelism'='8') */;
```

### Network Buffer Tuning

```yaml
# flink-conf.yaml - high-throughput jobs
taskmanager.network.memory.fraction: 0.15
taskmanager.network.memory.min: 256mb
taskmanager.network.memory.max: 1gb

# For high-cardinality keyBy (> 10K keys)
taskmanager.network.memory.fraction: 0.25

# Boundedness
execution.checkpointing.mode: EXACTLY_ONCE
execution.checkpointing.interval: 1min
execution.checkpointing.timeout: 10min
execution.checkpointing.max-concurrent-checkpoints: 1
execution.checkpointing.min-pause: 30s
```

### RocksDB Tuning

```yaml
# High-throughput state access
state.backend.rocksdb.memory.managed: true
state.backend.rocksdb.memory.managed.fraction: 0.4
state.backend.rocksdb.checkpoint.transfer.thread.num: 4

# Compact state access (for frequent updates)
state.backend.rocksdb.state-backend-config:
  "state.backend.rocksdb.log.file":
    "state.backend.rocksdb.log.file"
  "state.backend.rocksdb.db.options":
    "state.backend.rocksdb.db.options"

# Bloom filters for point lookups
state.backend.rocksdb.bloom.filters.enabled: true
```

## 8.3 Monitoring & Debugging

### Key Metrics

| Metric | Alert | Description |
|--------|-------|-------------|
| `currentInputWatermark` | Lagging behind `currentEventTime` | Watermark stagnation |
| `numRecordsOutPerSecond` | Zero on healthy path | Throughput drop |
| `lateRecordsDropped` | > 0 consistently | Late data issue |
| `checkpointAlignmentDuration` | > 100ms | Checkpoint alignment delay |
| `lastCheckpointDuration` | > 5min for incremental | Checkpoint too slow |
| `fullRestarts` | Any | Job restarted |

### Debug with REST API

```bash
# Job details
curl http://jm:8081/jobs/<job-id>

# Exceptions
curl http://jm:8081/jobs/<job-id>/exceptions

# Vertices (operators)
curl http://jm:8081/jobs/<job-id>/vertices

# Task manager metrics
curl http://jm:8081/taskmanagers

# Backpressure (since Flink 1.13)
curl http://jm:8081/jobs/<job-id>/vertices/<vertex-id>/backpressure
```

### Logging

```java
import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

// Enable debug logging for specific operators
public class MyProcessor extends KeyedProcessFunction<String, Event, Result> {
    private static final Logger LOG = LoggerFactory.getLogger(MyProcessor.class);
    
    @Override
    public void processElement(Event e, Context ctx, Collector<Result> out) {
        LOG.debug("Processing event: key={}, ts={}", e.getKey(), e.getTimestamp());
        // ...
    }
}
```

## 8.4 Known Issues & Fixes

| Issue | Versions | Fix |
|-------|----------|-----|
| `Checkpoint declined: not enough slots` | All | Reduce parallelism, increase `taskmanager.numberOfTaskSlots` |
| `RocksDB snapshot failed: native memory` | 1.14-1.18 | Enable `state.backend.rocksdb.memory.managed` |
| `Table/SQL join on non-equal keys causes full shuffle` | Pre-1.17 | Upgrade to 1.17+ for broadcast join support |
| `Kafka source doesn't commit offsets` | 1.15-1.16 | Use Flink checkpointing for offset management |
| `State size exceeds RocksDB max size` | All | Use `state.backend.rocksdb.memory.managed=true` |
| `PyFlink memory leak in loops` | 1.15-1.17 | Disable Python object reuse: `python.fn-execution.memory.managed=false` |
| `Savepoint with state deleted after resume` | Pre-1.18 | Upgrade to 1.18+ with improved savepoint compatibility |
