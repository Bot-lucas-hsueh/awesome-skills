# Scenario Examples

## 9.1 Analytics Dashboard

**Scenario:** Aggregating billions of events for real-time business metrics.

### Table Design for Analytics

```sql
CREATE TABLE raw_events (
    event_id UUID,
    org_id UInt32,
    user_id UInt32,
    session_id UUID,
    event_type LowCardinality(String),
    timestamp DateTime64(3),
    country LowCardinality(String),
    platform LowCardinality(String),
    revenue Nullable(Float64),
    payload String
) ENGINE = MergeTree()
ORDER BY (org_id, event_type, toDate(timestamp), timestamp)
PARTITION BY toYYYYMM(timestamp)
TTL timestamp + INTERVAL 13 MONTH;
```

### Pre-aggregated Materialized Views

```sql
-- Hourly user metrics
CREATE MATERIALIZED VIEW hourly_users
ENGINE = SummingMergeTree()
PARTITION BY toYYYYMM(hour)
ORDER BY (org_id, metric_hour, country, platform)
AS SELECT
    org_id,
    toStartOfHour(timestamp) AS metric_hour,
    country,
    platform,
    uniqExact(user_id) AS dau,
    uniqExact(session_id) AS sessions,
    countIf(event_type = 'purchase') AS purchases,
    sum(revenue) AS revenue,
    count() AS events
FROM raw_events
GROUP BY org_id, toStartOfHour(timestamp), country, platform;

-- Real-time funnel analysis
CREATE MATERIALIZED VIEW funnel_events
ENGINE = ReplacingMergeTree()
ORDER BY (org_id, session_id, step_order)
AS SELECT
    org_id,
    session_id,
    user_id,
    timestamp,
    multiMatchAny(event_type, ['page_view', 'signup_start', 'signup_complete', 'purchase']) AS step_name,
    arrayFind(['page_view', 'signup_start', 'signup_complete', 'purchase'], event_type) AS step_order
FROM raw_events
WHERE match(event_type, 'page_view|signup_start|signup_complete|purchase');

CREATE MATERIALIZED VIEW funnel_aggregated
ENGINE = SummingMergeTree()
ORDER BY (org_id, toDate(timestamp), step_name)
AS SELECT
    org_id,
    toDate(timestamp) AS date,
    step_name,
    count() AS count
FROM funnel_events
GROUP BY org_id, toDate(timestamp), step_name;
```

### Dashboard Queries

```sql
-- DAU trend for last 30 days
SELECT
    toDate(metric_hour) AS date,
    sum(dau) AS total_users
FROM hourly_users
WHERE org_id = 123
    AND metric_hour >= now() - INTERVAL 30 DAY
GROUP BY date
ORDER BY date;

-- Revenue by platform with conversion rate
SELECT
    platform,
    sum(revenue) AS total_revenue,
    sum(purchases) AS purchases,
    sum(purchases) * 100.0 / sum(sessions) AS conversion_rate
FROM hourly_users
WHERE org_id = 123
    AND metric_hour >= now() - INTERVAL 7 DAY
GROUP BY platform
ORDER BY total_revenue DESC;

-- Funnel conversion
SELECT
    step_name,
    count,
    lagInFrame(count) AS previous_step,
    count * 100.0 / lagInFrame(count) AS conversion_rate
FROM (
    SELECT step_name, sum(count) AS count
    FROM funnel_aggregated
    WHERE org_id = 123 AND date = today()
    GROUP BY step_name
)
ORDER BY arrayFind(['page_view', 'signup_start', 'signup_complete', 'purchase'], step_name);
```

## 9.2 Time-Series Data

**Scenario:** IoT sensor data with varying aggregation windows.

### Flexible Time-Series Schema

```sql
CREATE TABLE sensor_readings (
    sensor_id String,
    timestamp DateTime64(3),
    metric_name String,
    value Float64,
    quality UInt8  -- 0-100 quality score
) ENGINE = MergeTree()
ORDER BY (sensor_id, metric_name, timestamp)
PARTITION BY toYYYYMM(timestamp)
TTL timestamp + INTERVAL 3 MONTH;

-- Create rolling aggregates at multiple intervals
CREATE MATERIALIZED VIEW sensor_1min
ENGINE = AggregatingMergeTree()
ORDER BY (sensor_id, metric_name, minute)
AS SELECT
    sensor_id,
    metric_name,
    toStartOfMinute(timestamp) AS minute,
    avgState(value) AS avg_value,
    minState(value) AS min_value,
    maxState(value) AS max_value,
    countState() AS sample_count
FROM sensor_readings
WHERE quality >= 50
GROUP BY sensor_id, metric_name, toStartOfMinute(timestamp);

CREATE MATERIALIZED VIEW sensor_1hour
ENGINE = AggregatingMergeTree()
ORDER BY (sensor_id, metric_name, hour)
AS SELECT
    sensor_id,
    metric_name,
    toStartOfHour(timestamp) AS hour,
    avgState(value) AS avg_value,
    minState(value) AS min_value,
    maxState(value) AS max_value,
    countState() AS sample_count
FROM sensor_readings
WHERE quality >= 50
GROUP BY sensor_id, metric_name, toStartOfHour(timestamp);
```

### Query with Varying Aggregation

```sql
-- Dynamic aggregation: high resolution for recent, low for old
SELECT
    metric_name,
    toStartOfInterval(timestamp, INTERVAL 
        CASE
            WHEN ageInDays > 7 THEN 1 HOUR
            WHEN ageInDays > 1 THEN 15 MINUTE
            ELSE 1 MINUTE
        END) AS bucket,
    avg(value) AS avg_value
FROM (
    SELECT
        metric_name,
        timestamp,
        now() - timestamp AS age,
        dateDiff('day', timestamp, now()) AS ageInDays,
        value
    FROM sensor_readings
    WHERE sensor_id = 'sensor-001'
        AND timestamp >= now() - INTERVAL 30 DAY
)
GROUP BY metric_name, bucket
ORDER BY bucket;
```

## 9.3 Log Analysis

**Scenario:** Ingesting application logs and pre-aggregating for alerting.

### Log Ingestion Table

```sql
CREATE TABLE application_logs (
    timestamp DateTime64(3),
    level Enum8('DEBUG' = 1, 'INFO' = 2, 'WARN' = 3, 'ERROR' = 4, 'FATAL' = 5),
    service LowCardinality(String),
    host LowCardinality(String),
    trace_id Nullable(String),
    message String,
    exception Nullable(String),
    metadata String  -- JSON string for extra fields
) ENGINE = MergeTree()
ORDER BY (service, level, timestamp)
PARTITION BY toYYYYMM(timestamp)
TTL timestamp + INTERVAL 90 DAY;
```

### Pre-aggregation Views for Log Analysis

```sql
-- Error rate by service and severity
CREATE MATERIALIZED VIEW error_rate_1min
ENGINE = SummingMergeTree()
ORDER BY (service, level, minute)
AS SELECT
    service,
    level,
    toStartOfMinute(timestamp) AS minute,
    count() AS error_count
FROM application_logs
WHERE level >= 3  -- WARN and above
GROUP BY service, level, toStartOfMinute(timestamp);

-- Error grouping for pattern detection
CREATE MATERIALIZED VIEW error_patterns
ENGINE = SummingMergeTree()
ORDER BY (service, hour, error_hash)
AS SELECT
    service,
    toStartOfHour(timestamp) AS hour,
    cityHash64(exception) AS error_hash,
    exception,
    count() AS occurrence_count,
    uniqExact(trace_id) AS unique_traces
FROM application_logs
WHERE level >= 4 AND exception IS NOT NULL
GROUP BY service, toStartOfHour(timestamp), exception;

-- Slow query / error aggregator
CREATE MATERIALIZED VIEW log_summary
ENGINE = AggregatingMergeTree()
ORDER BY (service, period, metric)
AS SELECT
    service,
    toStartOfHour(timestamp) AS period,
    multiIf(
        level = 2, 'info_count',
        level = 3, 'warn_count',
        level >= 4, 'error_count',
        'other'
    ) AS metric,
    countState() AS cnt
FROM application_logs
GROUP BY service, toStartOfHour(timestamp), 
    multiIf(level = 2, 'info_count', level = 3, 'warn_count', level >= 4, 'error_count', 'other');
```

### Log Analysis Queries

```sql
-- Error rate in real-time
SELECT
    service,
    level,
    minute,
    error_count,
    error_count * 100.0 / (SELECT sum(error_count) FROM error_rate_1min WHERE minute = now() - INTERVAL 5 MINUTE) AS pct_of_total
FROM error_rate_1min
WHERE minute >= now() - INTERVAL 5 MINUTE
    AND service = 'api-gateway'
ORDER BY error_count DESC;

-- Recent error patterns
SELECT
    service,
    hour,
    exception,
    occurrence_count,
    unique_traces
FROM error_patterns
WHERE hour >= now() - INTERVAL 1 HOUR
    AND occurrence_count > 5
ORDER BY occurrence_count DESC;

-- Full-text search on logs (requires materialized view with tokenization)
SELECT timestamp, service, message
FROM application_logs
WHERE timestamp >= now() - INTERVAL 1 HOUR
    AND match(message, 'timeout|connection refused|failed to')
ORDER BY timestamp DESC
LIMIT 100;
```
