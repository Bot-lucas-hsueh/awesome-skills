# Standard Workflow

## 8.1 Table Creation Workflow

### MergeTree Family Table Creation

```sql
-- Basic MergeTree
CREATE TABLE page_views (
    user_id UInt32,
    page_url String,
    timestamp DateTime,
    duration UInt32,
    country FixedString(2)
) ENGINE = MergeTree()
ORDER BY (user_id, timestamp)
PARTITION BY toYYYYMM(timestamp)
TTL timestamp + INTERVAL 6 MONTH;

-- Choosing ORDER BY (critical for performance)
-- Rule: Most selective filter first, then timestamp for locality
CREATE TABLE events (
    org_id UInt32,
    event_type String,
    user_id UInt32,
    timestamp DateTime64(3),
    payload String
) ENGINE = MergeTree()
ORDER BY (org_id, event_type, timestamp);  -- For WHERE org_id = X AND event_type = Y

-- For time-series with heavy writes:
CREATE TABLE metrics (
    metric_name String,
    labels Map(String, String),
    value Float64,
    timestamp DateTime
) ENGINE = MergeTree()
ORDER BY (metric_name, timestamp)  -- Timestamp last for append-only
TTL timestamp + INTERVAL 30 DAY;
```

### Primary Key vs ORDER BY

ClickHouse does not have a traditional primary key. The ORDER BY key determines:
- Data sorting on disk
- Index effectiveness
- Compression efficiency

```sql
-- Wrong: treating it like PostgreSQL
CREATE TABLE bad_example (
    id UInt32 PRIMARY KEY,  -- Ignored, creates no index
    data String
) ENGINE = MergeTree()
ORDER BY id;

-- Right: put the primary lookup column first in ORDER BY
CREATE TABLE good_example (
    id UInt32,
    user_id UInt32,
    timestamp DateTime,
    data String
) ENGINE = MergeTree()
ORDER BY (user_id, timestamp);  -- For WHERE user_id = X queries
```

### Materialized View Creation

```sql
-- For pre-aggregated analytics
CREATE MATERIALIZED VIEW hourly_stats
ENGINE = SummingMergeTree()
PARTITION BY toYYYYMM(timestamp)
ORDER BY (metric_name, hour)
AS SELECT
    metric_name,
    toStartOfHour(timestamp) AS hour,
    sum(value) AS total_value,
    count() AS event_count
FROM metrics
GROUP BY metric_name, hour;
```

## 8.2 Data Ingestion

### INSERT Statements

```sql
-- Single row
INSERT INTO events VALUES ('uuid-123', 1001, 'page_view', now());

-- Multiple rows
INSERT INTO events VALUES
    ('uuid-1', 1001, 'click', now()),
    ('uuid-2', 1002, 'scroll', now()),
    ('uuid-3', 1003, 'submit', now());

-- From SELECT
INSERT INTO aggregated SELECT date, count() FROM source GROUP BY date;
```

### CSV/TSV Import

```bash
# Via clickhouse-client
clickhouse-client --query "INSERT INTO events FORMAT CSV" < events.csv
clickhouse-client --query "INSERT INTO events FORMAT TabSeparated" < events.tsv

# With header
clickhouse-client --query "INSERT INTO events FORMAT CSVWithNames" < events.csv
```

### JSONEachRow Format

```sql
-- Table structure
CREATE TABLE events (
    event_type String,
    user_id UInt32,
    timestamp DateTime,
    properties String  -- JSON as string, or use JSON type (v23.8+)
) ENGINE = MergeTree() ORDER BY (user_id, timestamp);

-- Import JSON
INSERT INTO events FORMAT JSONEachRow
{"event_type": "click", "user_id": 123, "timestamp": "2024-01-15 10:30:00", "properties": "{}"}
{"event_type": "view", "user_id": 456, "timestamp": "2024-01-15 10:31:00", "properties": "{\"page\": \"/home\"}"}
```

### S3 Integration

```sql
-- Create table backed by S3
CREATE TABLE s3_logs (
    timestamp DateTime,
    level String,
    message String
) ENGINE = S3('s3://bucket/logs/*.json', 'JSONEachRow');

-- Export to S3
INSERT INTO FUNCTION s3('s3://bucket/export/2024-01.csv', 'csv')
SELECT * FROM events WHERE timestamp >= '2024-01-01';

-- Export with compression
INSERT INTO FUNCTION s3('s3://bucket/export/2024-01.tsv.gz', 'TabSeparatedWithNamesAndTypes', 'gzip')
SELECT * FROM events;
```

### Kafka Integration

```sql
-- Create Kafka engine table
CREATE TABLE kafka_events (
    user_id UInt32,
    event_type String,
    timestamp DateTime,
    payload String
) ENGINE = Kafka()
SETTINGS kafka_broker_list = 'kafka:9092',
         kafka_topic_list = 'events',
         kafka_group_name = 'clickhouse-consumer',
         kafka_format = 'JSONEachRow';

-- Create materialized view to consume Kafka data
CREATE MATERIALIZED VIEW kafka_consumer TO events AS
SELECT * FROM kafka_events;
```

## 8.3 Query Optimization

### Important Settings

```sql
-- Set for current session
SET max_threads = 16;
SET max_memory_usage = 8589934592;  -- 8GB
SET max_rows_to_read = 1000000000;
SET max_bytes_to_read = 10737418240;
SET timeout = 300;

-- For aggregation-heavy queries
SET max_block_size = 65505;
SET group_by_two_level_threshold = 1000000;
SET group_by_two_level_threshold_bytes = 100000000;

-- For JOINs
SET join_algorithm = 'hash';
SET partial_merge_join_optimizations = 1;
SET max_rows_in_join = 1000000;

-- For ORDER BY with LIMIT
SET max_limit_optimisation_workspaces = 10;
```

### EXPLAIN Syntax

```sql
-- Query plan
EXPLAIN query SELECT count() FROM events WHERE timestamp > now() - INTERVAL 1 DAY;

-- AST (Abstract Syntax Tree)
EXPLAIN AST SELECT * FROM events;

-- Pipeline plan (shows parallelization)
EXPLAIN PIPELINE SELECT sum(value) FROM metrics GROUP BY metric_name;
```

### Reading Query Statistics

```sql
-- Enable query_log
SET send_logs_level = 'information';

-- View recent queries
SELECT query, query_duration_ms, read_rows, read_bytes
FROM system.query_log
WHERE type = 'QueryFinish'
ORDER BY event_time DESC
LIMIT 10;

-- Find slow queries
SELECT query, query_duration_ms, read_rows
FROM system.query_log
WHERE type = 'QueryFinish'
    AND query_duration_ms > 10000
ORDER BY query_duration_ms DESC;
```

### Data Skipping Indexes

```sql
-- MinMax index (good for range queries)
ALTER TABLE events ADD INDEX idx_timestamp (timestamp) TYPE minmax GRANULARITY 3;

-- Set index (good for equality filters on low cardinality)
ALTER TABLE events ADD INDEX idx_type (event_type) TYPE set(100) GRANULARITY 3;

-- Bloom filter (good for high cardinality strings)
ALTER TABLE events ADD INDEX idx_user_id (user_id) TYPE bloom_filter(0.001) GRANULARITY 1;
```
