# Standards & Reference

## 7.1 Official Documentation

- [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-stable/)
- [Flink API Reference (Java)](https://nightlies.apache.org/flink/flink-docs-stable/api/java/)
- [Flink API Reference (Python)](https://nightlies.apache.org/flink/flink-docs-stable/api/python/)
- [Flink SQL Gateway](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/sql-gateway/overview/)
- [Flink Connectors](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/table/overview/)
- [DataStream API Guide](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/overview/)
- [Table API & SQL](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/table/overview/)
- [Flink Configuration Reference](https://nightlies.apache.org/flink/flink-docs-stable/docs/deployment/config/)

## 7.2 Configuration Reference

### flink-conf.yaml

```yaml
# JobManager
jobmanager.memory.process.size: 1600m
jobmanager.memory.flink.size: 1280m

# TaskManager
taskmanager.memory.process.size: 1728m
taskmanager.memory.flink.size: 1280m
taskmanager.numberOfTaskSlots: 8

# Parallelism
parallelism.default: 2
taskmanager.parallelism.default: 2

# State Backend
state.backend: rocksdb
state.checkpoints.dir: s3://your-bucket/flink-checkpoints
state.savepoints.dir: s3://your-bucket/flink-savepoints

# RocksDB Options
state.backend.incremental: true
state.backend.rocksdb.memory.managed: true

# High Availability
high-availability: kubernetes
high-availability.storageDir: s3://your-bucket/flink-ha

# REST API
rest.port: 8081
rest.bind-port: 8081

# Checkpointing
execution.checkpointing.interval: 60s
execution.checkpointing.mode: EXACTLY_ONCE
execution.checkpointing.timeout: 10min
execution.checkpointing.min-pause: 30s
execution.checkpointing.max-concurrent-checkpoints: 1

# Table API / SQL
table.exec.state-backend: rocksdb
table.exec.resource.default-parallelism: 2
```

### Table API Registration (Java)

```java
EnvironmentSettings settings = EnvironmentSettings.newInstance()
    .inStreamingMode()
    .build();

TableEnvironment tEnv = TableEnvironment.create(settings);

tEnv.executeSql("CREATE TABLE MySource (id BIGINT, name STRING, ts TIMESTAMP(3), WATERMARK FOR ts AS ts - INTERVAL '5' SECOND) WITH ('connector' = 'kafka', 'topic' = 'events', 'properties.bootstrap.servers' = 'kafka:9092', 'format' = 'json')");

tEnv.executeSql("CREATE TABLE MySink (id BIGINT, name STRING, event_count BIGINT, window_start TIMESTAMP(3)) WITH ('connector' = 'jdbc', 'url' = 'jdbc:postgresql://db:5432/events', 'table-name' = 'aggregates', 'username' = 'flink', 'password' = 'secret')");
```

## 7.3 Common Commands & SQL

### Flink SQL Gateway (REST)

```bash
# Start SQL Gateway
./bin/sql-gateway.sh start -Dsql-gateway.session.timeout: 30min

# Submit query via curl
curl -X POST http://localhost:8083/v1/sql-gateway/sessions/{sessionId}/statements \
  -H "Content-Type: application/json" \
  -d '{"statement": "SELECT * FROM MyTable LIMIT 10"}'
```

### SQL DDL Examples

```sql
-- Kafka source
CREATE TABLE kafka_source (
    user_id STRING,
    page_url STRING,
    ts TIMESTAMP(3),
    WATERMARK FOR ts AS ts - INTERVAL '5' SECOND
) WITH (
    'connector' = 'kafka',
    'topic' = 'user_events',
    'properties.bootstrap.servers' = 'kafka:9092',
    'properties.group.id' = 'flink-consumer',
    'format' = 'json',
    'json.fail-on-missing-field' = 'false'
);

-- PostgreSQL sink
CREATE TABLE pg_sink (
    user_id STRING,
    page_view_count BIGINT,
    PRIMARY KEY (user_id) NOT ENFORCED
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:postgresql://pg:5432/analytics',
    'table-name' = 'user_stats',
    'username' = 'flink_user',
    'password' = '${env:PG_PASSWORD}',
    'sink.parallelism' = '4'
);

-- Aggregation with window
INSERT INTO pg_sink
SELECT
    user_id,
    COUNT(*) AS page_view_count
FROM kafka_source
GROUP BY user_id;
```

### CLI Operations

```bash
# Submit a Flink job
./bin/flink run -d -p 4 ./path/to/your-job.jar

# List running jobs
./bin/flink list -r

# Cancel a job
./bin/flink cancel <job-id>

# Trigger savepoint
./bin/flink savepoint <job-id> s3://bucket/savepoints/

# Resume from savepoint
./bin/flink run -d -s s3://bucket/savepoints/<savepoint-path> ./path/to/your-job.jar
```

## 7.4 Version Compatibility

| Version | Status | Java | Scala | Key Features |
|---------|--------|------|-------|--------------|
| 1.14.x | EOL | 8, 11 | 2.11, 2.12 | Production stable |
| 1.15.x | EOL | 8, 11 | 2.12 | Unified memory config |
| 1.16.x | EOL | 8, 11 | 2.12 | Hive DDL, Kafka 3.x connector |
| 1.17.x | EOL | 8, 11, 17 | 2.12 | PyFlink improvements |
| 1.18.x | Stable | 8, 11, 17 | 2.12 | RocksDB 8.x, vectorized |
| 1.19.x | Stable | 8, 11, 17, 21 | 2.12 | Adaptive Scheduler |
| 1.20.x | Latest | 8, 11, 17, 21 | 2.12 | AI Trainingconnector, K8s operator 1.2 |

| Connector | Min Flink | Notes |
|-----------|-----------|-------|
| Kafka | 1.14+ | Use kafka-sql-connector |
| PostgreSQL | 1.14+ | JDBC connector |
| Delta Lake | 1.15+ | Use flink-connector-delta |
| Iceberg | 1.16+ | flink-connector-iceberg |
| S3 | 1.14+ | flink-s3-fs-presto |
