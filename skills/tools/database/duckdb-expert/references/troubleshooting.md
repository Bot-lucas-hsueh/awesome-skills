# Standards & Reference

## 8.1 Common Issues

### Memory Issues

```sql
-- DuckDB runs out of memory
SET memory_limit = '4GB';
SET max_temp_directory_size = '2GB';

-- Check current memory usage
SELECT * FROM duckdb_memory_usage();
```

### Query Performance

```sql
-- Enable profiling
SET enable_profiling = true;
SET profiling_output = '/tmp/profile.json';

-- Run query
SELECT ... FROM large_table;

-- View profile
.output json
SELECT * FROM query_profile();
```

### Extension Loading

```sql
-- Install and load extensions
INSTALL spatial;
LOAD spatial;

INSTALL httpfs;
LOAD httpfs;

INSTALL parquet;
LOAD parquet;
```

## 8.2 Connection & CLI Issues

### CLI Not Responding

```bash
# Press Ctrl+C to cancel long-running query
# Use .timer off to disable timing
.timer off

# Increase timeout for long queries
SET execution_timeout = '10min';
```

### Python API Issues

```python
import duckdb

# Connection refused - use correct path
con = duckdb.connect('/path/to/database.duckdb')

# Memory issues - set limits
con.execute("SET memory_limit = '4GB'")

# Read-only mode for Parquet
con.execute("SET access_mode = 'read-only'")
```

## 8.3 Data Import/Export Issues

### CSV Import Failures

```sql
-- Auto-detect CSV format
COPY table_name FROM 'data.csv' (AUTO_DETECT TRUE);

-- Specify delimiter
COPY table_name FROM 'data.tsv' (DELIMITER '\t', HEADER TRUE);

-- Handle null values
COPY table_name FROM 'data.csv' (DELIMITER ',', NULL 'NA', HEADER TRUE);
```

### Parquet File Issues

```sql
-- List Parquet files
SELECT * FROM read_parquet('/path/*.parquet', filename=true);

-- Force schema
SELECT * FROM read_parquet('data.parquet', columns={'col1': 'BIGINT', 'col2': 'VARCHAR'});
```

## 8.4 Performance Troubleshooting

### Slow JOINs

```sql
-- Enable hash join probe side cache
SET enable_hash_join_probe_side_cache = true;

-- Parallel query execution
SET threads = 8;
SET force_index_join = false;
```

### Large Result Sets

```sql
-- Stream results instead of collecting
PRAGMA enable_progress_bar;

-- Limit early
SELECT * FROM large_table LIMIT 1000;
```

## 8.5 Extension-Specific Issues

### Spatial Extension

```sql
-- ST_* functions not found
INSTALL spatial;
LOAD spatial;

-- Run spatial query
SELECT ST_Distance(ST_Point(0, 0), ST_Point(1, 1));
```

### HTTPFS (Remote Files)

```sql
-- Access S3 buckets
INSTALL httpfs;
LOAD httpfs;

SET s3_region = 'us-east-1';
SELECT * FROM 's3://bucket/path/to/file.parquet';
```
