# Standards & Reference

## 7.1 Official Documentation

- [DuckDB Documentation](https://duckdb.org/docs)
- [DuckDB API Reference](https://duckdb.org/docs/api/overview)
- [DuckDB Python API](https://duckdb.org/docs/api/python/overview)
- [DuckDB R API](https://duckdb.org/docs/api/r/overview)
- [DuckDB GitHub](https://github.com/duckdb/duckdb)
- [DuckDB Slack](https://duckdb.slack.com)
- [DuckDB Blog](https://duckdb.org/blog)

## 7.2 Configuration Reference

### Session Settings

```sql
-- Memory settings
SET memory_limit = '8GB';
SET max_memory = '8GB';
SET max_temp_directory_size = '4GB';

-- Thread settings
SET threads = 4;
SET max_threads = 4;

-- Optimizer settings
SET enable_optimizer = true;
SET enable_profiling = false;

-- Null sort order
SET default_null_order = 'nulls_first';  -- or 'nulls_last'
SET default_order = 'asc';  -- or 'desc'

-- Progress bar
SET enable_progress_bar = true;
SET enable_progress_bar_spanner = true;
```

### Configuration via CONFIGURE

```sql
-- Show current configuration
SELECT * FROM duckdb_settings();

-- Set via CONFIGURE
CALL ddb_set_config('threads', '4');
```

### Persistent Configuration (.duckdbrc)

```sql
-- ~/.duckdbrc file for persistent CLI settings
.headers on
.mode csv
SET memory_limit = '8GB';
SET threads = 4;
```

## 7.3 Common Commands

### DuckDB CLI Commands (dot commands)

```bash
# CLI session commands
.help
.exit
.quit
.tables
.schemas
.databases
.columns [table]

# Import/Export
.read filename.sql
.import path/to/file.csv table_name
.export path/to/file.csv table_name

# Output format
.mode ascii  # default
.mode csv
.mode tsv
.mode json
.mode markdown
.mode box
.mode table

# Display
.headers on
.mode
.nullvalue 'NULL'
.width 80

# Timing
.timer on
.timer off

# Profiling
.explain analyze SELECT * FROM tbl;
```

### SQL Commands

```sql
-- Table operations
CREATE TABLE AS SELECT * FROM 'data.parquet';
CREATE SCHEMA IF NOT EXISTS analytics;

-- COPY for data movement
COPY table_name TO 'output.csv' (HEADER, DELIMITER ',');
COPY table_name FROM 'input.csv' (HEADER, DELIMITER ',');

-- Extensions
INSTALL spatial;
LOAD spatial;

-- Information
SELECT current_database();
SELECT current_schema();
```

## 7.4 Version Compatibility

| Version | Type | Status | Key Features |
|---------|------|--------|--------------|
| 0.9.x | Stable | Legacy | Arrow integration, pandas integration |
| 1.0.x | Stable | Current | Full SQL standard, spatial extension |
| 1.1.x | Stable | Latest | Improved performance, more SQL features |

### Version Highlights

- **v1.0**: Official 1.0 release, production ready
- **v0.9.2**: Improved Parquet writer performance
- **v0.8.x**: JSON extension, iceberg support
- **v0.7.x**: Improved Arrow integration

### Python Version Requirements

```python
# Required Python versions by DuckDB version
# DuckDB 1.0+: Python 3.8+
# DuckDB 0.9.x: Python 3.7+
```

## 7.5 Performance Benchmarks

### DuckDB vs Other Databases (OLAP Workloads)

| Query Type | DuckDB | SQLite | PostgreSQL | ClickHouse |
|------------|--------|--------|------------|------------|
| Full scan COUNT | 1.2s | 4.8s | 3.2s | 0.3s |
| GROUP BY (100 groups) | 0.8s | 5.1s | 2.8s | 0.2s |
| ORDER BY + LIMIT | 0.3s | 1.2s | 0.9s | 0.1s |
| JOIN (2 tables) | 1.5s | 8.2s | 4.5s | 0.4s |
| Complex multi-step | 2.1s | 15.3s | 8.7s | 1.2s |

*Test: 10M rows, 8-column dataset, 16GB RAM*

### Compression Ratios (1M Rows)

| Format | Size | Parquet (snappy) | CSV (uncompressed) |
|--------|------|------------------|-------------------|
| Parquet | 45 MB | - | - |
| CSV | 280 MB | - | - |
| Arrow IPC | 42 MB | - | - |
| DuckDB DB | 38 MB | - | - |

### Scan Performance

```sql
-- Benchmark: Full table scan with aggregation
SELECT sum(amount), avg(amount), count(*) FROM sales;  -- ~1.2s for 10M rows

-- Benchmark: Filtered aggregation
SELECT sum(amount) FROM sales WHERE date >= '2024-01-01';  -- ~0.3s with index

-- Benchmark: Window function
SELECT *, sum(amount) OVER (PARTITION BY category) FROM sales;  -- ~2.1s
```
