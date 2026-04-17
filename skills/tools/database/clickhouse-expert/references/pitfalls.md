# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Fix |
|---|---------|----------|--------|-----|
| 1 | Wrong ORDER BY key | 🔴 High | 10-100x slower queries | Design key for primary access patterns |
| 2 | Too many parts | 🔴 High | Merge storms, ZK bottlenecks | Increase block size, reduce partitions |
| 3 | No TTL on large tables | 🟡 Medium | Disk bloat, slow queries | Add TTL immediately |
| 4 | Using Nullable unnecessarily | 🟡 Medium | 2x storage, slower reads | Avoid Nullable, use default values |
| 5 | Too many indexes | 🟡 Medium | Slow inserts, wasted space | Index only frequently filtered columns |
| 6 | Partition by day | 🟡 Medium | Too many parts | Partition by month or use dynamic |
| 7 | Ignoring parts settings | 🟡 Medium | Merge overhead | Tune max_bytes_to_merge, max_parts_to_merge |

### Mistake 1: Wrong ORDER BY Key

```sql
-- Wrong: timestamp first means index useless for user lookups
CREATE TABLE bad_order (
    user_id UInt32,
    timestamp DateTime,
    data String
) ENGINE = MergeTree()
ORDER BY (timestamp, user_id);

-- Query: SELECT * FROM bad_order WHERE user_id = 123
-- Result: Full scan despite user_id filter!

-- Right: Most selective column first
CREATE TABLE good_order (
    user_id UInt32,
    timestamp DateTime,
    data String
) ENGINE = MergeTree()
ORDER BY (user_id, timestamp);

-- Query: SELECT * FROM good_order WHERE user_id = 123
-- Result: Uses primary key index, 100x faster
```

### Mistake 2: Too Many Parts

```sql
-- Problem: Too many small parts cause merge storms
-- Symptoms in system.parts:
-- SELECT count(), sum(rows), avg(bytes_on_disk) FROM system.parts WHERE table = 'events';

-- Common causes:
-- 1. Inserting single rows repeatedly
INSERT INTO events VALUES ('id-1', now());  -- Bad
INSERT INTO events VALUES ('id-2', now());  -- Bad
INSERT INTO events VALUES ('id-3', now());  -- Bad

-- 2. Daily partitions with high-frequency inserts
-- Instead, use monthly partitions and batch inserts

-- Fix: Batch inserts to reach target block size (65K+ rows)
INSERT INTO events SELECT * FROM batch_source WHERE batch_id = 123;

-- Monitor parts count
SELECT 
    table,
    count() AS parts,
    sum(rows) AS total_rows,
    sum(bytes_on_disk) AS total_bytes,
    max(creation_time) AS last_part
FROM system.parts
WHERE database = 'default' AND active = 1
GROUP BY table
ORDER BY parts DESC;
```

### Mistake 3: No TTL Management

```sql
-- Large tables without TTL will grow indefinitely
-- Monitor table sizes
SELECT 
    table,
    formatReadableSize(sum(bytes_on_disk)) AS disk_size,
    min(min_time) AS oldest_data,
    max(max_time) AS newest_data
FROM system.parts
WHERE database = 'default' AND active = 1
GROUP BY table
ORDER BY disk_size DESC;

-- Add TTL to existing table
ALTER TABLE events MODIFY TTL timestamp + INTERVAL 3 MONTH;

-- For dependent tables (like materialized views)
-- The TTL must be added to both source and destination tables
```

### Mistake 4: Nullable Columns

```sql
-- Nullable adds overhead: separate file with NULLs + 1 byte per value
CREATE TABLE with_nullable (
    user_id UInt32,
    email Nullable(String),  -- Expensive!
    phone Nullable(String)    -- Double expensive!
) ENGINE = MergeTree() ORDER BY user_id;

-- Better: Use default values
CREATE TABLE without_nullable (
    user_id UInt32,
    email String DEFAULT '',
    phone String DEFAULT ''   -- Empty string instead of NULL
) ENGINE = MergeTree() ORDER BY user_id;
```

## 10.2 Performance Anti-Patterns

| # | Anti-Pattern | Severity | Fix |
|---|--------------|----------|-----|
| 1 | Mutations on large tables | 🔴 High | Avoid ALTER UPDATE/DELETE, use FINAL |
| 2 | No TTL management | 🔴 High | Add TTL to all time-series tables |
| 3 | SELECT * on wide tables | 🟡 Medium | Select only needed columns |
| 4 | Unoptimized JOINs | 🟡 Medium | Broadcast smaller table, use memory limits |
| 5 | No partition pruning | 🟡 Medium | Always filter partition column in queries |
| 6 | Global group by | 🟡 Medium | Use two-level aggregation |
| 7 | Large LIMIT without ORDER BY | 🟡 Medium | Add ORDER BY or use LIMIT n BY |

### Anti-Pattern 1: Mutations on Large Tables

```sql
-- DANGER: ALTER UPDATE/DELETE creates mutation log
-- For a table with 1B rows, this can take hours
ALTER TABLE events UPDATE value = 0 WHERE old_flag = 1;  -- BAD!

-- Better approaches:
-- 1. Use ReplacingMergeTree with version column
-- 2. INSERT only valid data, SELECT with FINAL
CREATE TABLE events_new (
    user_id UInt32,
    timestamp DateTime,
    value Float64
) ENGINE = ReplacingMergeTree()
ORDER BY (user_id, timestamp)
SETTINGS is_stale_retention = true;  -- New in v23.x

-- 3. Use FINAL clause (expensive but simpler)
-- SELECT * FROM events FINAL WHERE timestamp > yesterday;

-- 4. For deletes: insert only kept data
INSERT INTO events SELECT * FROM events WHERE _part_file NOT IN (SELECT ...) ;
```

### Anti-Pattern 2: No TTL Management

```sql
-- Time-series data grows forever without TTL
-- Set TTL immediately when creating table

CREATE TABLE metrics (
    timestamp DateTime,
    metric_name String,
    value Float64
) ENGINE = MergeTree()
ORDER BY (metric_name, timestamp)
TTL timestamp + INTERVAL 1 MONTH
    SET storage_policy = 'default';

-- Add TTL to existing table
ALTER TABLE metrics MODIFY TTL timestamp + INTERVAL 1 MONTH;

-- For dependent data (materialized views)
-- TTL must be set on BOTH source and destination
CREATE MATERIALIZED VIEW hourly_metrics
ENGINE = SummingMergeTree()
ORDER BY (metric_name, hour)
TTL hour + INTERVAL 1 MONTH  -- Don't forget!
AS SELECT metric_name, toStartOfHour(timestamp) AS hour, sum(value) AS total
FROM metrics
GROUP BY metric_name, toStartOfHour(timestamp);
```

### Anti-Pattern 3: SELECT * on Wide Tables

```sql
-- Bad: Transfers all columns, including unused ones
SELECT * FROM wide_events;  -- 100+ columns, 10MB per row

-- Good: Only select needed columns
SELECT user_id, timestamp, event_type
FROM events
WHERE timestamp > yesterday;
```

### Anti-Pattern 4: Unoptimized JOINs

```sql
-- Default hash join may fail on large tables
SELECT a.*, b.metadata
FROM events a
JOIN user_metadata b ON a.user_id = b.user_id;  -- May OOM

-- Better: Use smaller table as right side, broadcast
SET join_algorithm = 'broadcast';
SET max_block_size = 10000;

-- For very large joins: split into chunks
SELECT a.*, b.metadata
FROM events a
ANY LEFT JOIN (
    SELECT * FROM user_metadata WHERE created_date = today()
) b ON a.user_id = b.user_id;

-- Memory limits for joins
SET max_rows_in_join = 1000000;
SET join_overflow_mode = 'break';
```

### Anti-Pattern 5: No Partition Pruning

```sql
-- Bad: Full table scan
SELECT * FROM events WHERE timestamp > yesterday;  -- No partition prune

-- Good: Filter partition key explicitly
SELECT * FROM events 
WHERE timestamp > yesterday
  AND toYYYYMM(timestamp) = toYYYYMM(today());  -- Prunes partition

-- Dynamic partition pruning (v22.3+)
SET allow_execute_multiple_subqueries = 1;
SELECT * FROM events WHERE timestamp BETWEEN 
    (SELECT min(timestamp) FROM events) 
    AND now();
```

### Anti-Pattern 6: Global GROUP BY

```sql
-- Global GROUP BY can overflow memory
SELECT uniqExact(user_id) FROM events;  -- May OOM with many users

-- Two-level aggregation
SET group_by_two_level_threshold = 1000000;
SET group_by_two_level_threshold_bytes = 100000000;

-- Manual two-level approach
SELECT sum(cnt) FROM (
    SELECT uniqExact(user_id) AS cnt
    FROM events
    GROUP BY cityHash64(user_id) % 256
) t;
```

### Anti-Pattern 7: Large LIMIT Without ORDER BY

```sql
-- Without ORDER BY, ClickHouse may return arbitrary rows
SELECT * FROM events LIMIT 1000;  -- Random 1000 rows!

-- With ORDER BY, ClickHouse must sort, which is expensive
SELECT * FROM events ORDER BY timestamp DESC LIMIT 1000;  -- Sorted

-- Efficient alternative: LIMIT n BY
SELECT *
FROM events
LIMIT 10 BY event_type;  -- 10 per event_type, no full sort
```
