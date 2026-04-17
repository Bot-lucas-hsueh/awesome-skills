# Standards & Reference

## 7.1 Official Documentation

- [ClickHouse Docs](https://clickhouse.com/docs/en)
- [ClickHouse GitHub](https://github.com/ClickHouse/ClickHouse)
- [ClickHouse Blog](https://clickhouse.com/blog)
- [ClickHouse Slack Community](https://clickhouse.com/slack)
- [ClickHouse Forum](https://clickhouse.com/forum)

## 7.2 Configuration Reference

### Server Configuration (clickhouse-server)

Main config file: `/etc/clickhouse-server/config.xml`

```xml
<clickhouse>
    <!-- Network -->
    <listen_host>::</listen_host>
    <http_port>8123</http_port>
    <tcp_port>9000</tcp_port>

    <!-- Users -->
    <users_config>users.xml</users_config>

    <!-- Logging -->
    <log>/var/log/clickhouse-server/clickhouse-server.log</log>
    <errorlog>/var/log/clickhouse-server/clickhouse-error.log</errorlog>

    <!-- Paths -->
    <path>/var/lib/clickhouse/</path>
    <tmp_path>/var/lib/clickhouse/tmp/</tmp_path>
    <user_files_path>/var/lib/clickhouse/user_files/</user_files_path>

    <!-- Keep alive -->
    <keep_alive_timeout>3</keep_alive_timeout>
</clickhouse>
```

### Keeper Configuration (for replicated tables)

Config file: `/etc/clickhouse-keeper/keeper_config.xml`

```xml
<keeper_server>
    <tcp_port>9181</tcp_port>
    <server_id>1</server_id>
    <log_storage_path>/var/lib/clickhouse/coordination/log</log_storage_path>
    <snapshot_storage_path>/var/lib/clickhouse/coordination/snapshots</snapshot_storage_path>

    <coordination_settings>
        <operation_timeout_ms>10000</operation_timeout_ms>
        <session_timeout_ms>30000</session_timeout_ms>
        <raft_settings>
            <min_session_timeout_ms>10000</min_session_timeout_ms>
        </raft_settings>
    </coordination_settings>

    <macros>
        <shard>01</shard>
        <replica>01</replica>
    </macros>
</keeper_server>
```

### Memory & Resource Limits

```xml
<clickhouse>
    <max_server_memory_usage>0</max_server_memory_usage>  <!-- 0 = auto -->
    <max_thread_pool_size>10000</max_thread_pool_size>
</clickhouse>
```

## 7.3 Common Commands

### Client Commands

```bash
# Connect to ClickHouse
clickhouse-client --host localhost --port 9000
clickhouse-client --user default --password your_password
clickhouse-client --secure

# With query
clickhouse-client --query "SELECT 1"
clickhouse-client --multiquery --queries-file queries.sql

# Interactive mode
clickhouse-client
```

### DDL Commands

```sql
-- Create database
CREATE DATABASE IF NOT EXISTS analytics;

-- Create table with MergeTree engine
CREATE TABLE events (
    event_id UUID,
    user_id UInt32,
    event_type String,
    timestamp DateTime,
    properties Map(String, String),
    value Float64
) ENGINE = MergeTree()
ORDER BY (user_id, timestamp)
PARTITION BY toYYYYMM(timestamp)
TTL timestamp + INTERVAL 3 MONTH;

-- Create replicated table
CREATE TABLE events_replicated (
    event_id UUID,
    user_id UInt32,
    event_type String,
    timestamp DateTime
) ENGINE = ReplicatedMergeTree('/clickhouse/tables/{shard}/events', '{replica}')
ORDER BY (user_id, timestamp);

-- Alter table
ALTER TABLE events ADD COLUMN platform String DEFAULT 'web';
ALTER TABLE events MODIFY COLUMN value Decimal(18, 4);
ALTER TABLE events DROP COLUMN legacy_field;
ALTER TABLE events ADD INDEX idx_type (event_type) TYPE set(1000) GRANULARITY 3;

-- Optimize table
OPTIMIZE TABLE events FINAL;
OPTIMIZE TABLE events PARTITION 202401;

-- System commands
SYSTEM STOP MERGES;
SYSTEM START MERGES;
SYSTEM FLUSH LOGS;
SYSTEM RELOAD CONFIG;
SYSTEM RESTORE REPLICA events;
```

## 7.4 Version Compatibility

| Version | Type | Status | Notes |
|---------|------|--------|-------|
| 21.x | LTS | EOL | Last version with 32-bit support |
| 22.x | LTS | Security Only | Recommended for legacy deployments |
| 23.x | LTS | Current LTS | Default, 24.x soon |
| 24.x | Stable | Latest | Current stable release |

### Feature Compatibility by Version

- **v23.8+**: Native JSON type, better Lambda functions
- **v23.3+**: Improved S3 queue table engine
- **v22.8+**: Keeper native authentication
- **v21.8+**: Projection improvements

## 7.5 Performance Benchmarks

### MergeTree Engine Comparison

| Engine | Write Speed | Read Speed | Compression | Use Case |
|--------|-------------|------------|-------------|----------|
| MergeTree | 10M rows/s | Fast | Medium | General purpose |
| ReplacingMergeTree | 8M rows/s | Fast | Medium | Deduplication |
| SummingMergeTree | 6M rows/s | Very Fast | High | Pre-aggregated sums |
| AggregatingMergeTree | 5M rows/s | Fast | High | Pre-aggregated counts |
| CollapsingMergeTree | 7M rows/s | Medium | Medium | Slowly changing dimensions |

### Compression Ratios by Data Type

| Data Type | LZ4 | ZSTD(1) | ZSTD(22) | Delta |
|-----------|-----|---------|----------|-------|
| Float64 | 2.1x | 3.4x | 4.8x | - |
| DateTime | 4.2x | 8.1x | 12.3x | 15.2x |
| UUID | 1.1x | 1.2x | 1.3x | 50.0x |
| String (low cardinality) | 5.0x | 12.0x | 18.0x | - |
| FixedString | 3.0x | 6.0x | 9.0x | - |

### Query Performance Baselines

- **Simple COUNT**: ~100M rows/sec on 8-core server
- **GROUP BY 10M groups**: ~50M rows/sec
- **Join 1B x 100K**: ~10M rows/sec
- **INSERT batch 1M rows**: ~5M rows/sec
