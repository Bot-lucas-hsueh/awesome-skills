# Glossary

## Core Concepts

**OLAP (Online Analytical Processing)** — Analytical workloads with complex queries, aggregations, and scans. DuckDB is optimized for OLAP.

**HTAP (Hybrid Transactional/Analytical Processing)** — Combined OLTP and OLAP workloads.

**Embedded Database** — Database that runs in the same process as the application, no separate server needed.

**Vectorized Execution** — Processing columns in batches (vectors) for faster analytical queries.

## Data Types

**Parquet** — Columnar storage format, ideal for analytics. DuckDB reads Parquet directly.

**Arrow (IPC)** — Apache Arrow columnar format for in-memory data exchange.

**CSV** — Delimited text format, requires parsing but widely compatible.

**JSON** — Semi-structured data format, DuckDB supports JSON as VARCHAR and can parse with `json_extract`.

## DuckDB Concepts

**Database File (.duckdb)** — Single-file SQLite-like database containing all data.

**Schema** — Namespace for tables and views, default is `main`.

**Append-Only** — New data can be appended, existing data cannot be updated (like most OLAP databases).

**Out-of-Core Processing** — Ability to process data larger than RAM using disk as overflow.

## Query Concepts

**Window Functions** — Functions that operate on a set of rows related to the current row (e.g., `SUM() OVER (PARTITION BY ...)`).

**CTE (Common Table Expression)** — Named temporary result set using `WITH` clause.

**Prepared Statements** — Pre-compiled SQL for repeated execution with different parameters.

**Streaming** — Processing results incrementally without loading all data into memory.

## File Formats

**DuckDB Database** — Single `.duckdb` file or directory-based `.db` directory.

**Parquet** — Columnar storage with compression, predicate pushdown support.

**Arrow IPC** — Zero-copy format for Arrow data sharing.

**Iceberg** — Open table format for analytic datasets, supported via extension.

## Configuration Terms

**memory_limit** — Maximum RAM DuckDB can use.

**threads** — Number of CPU cores for parallel query execution.

**temp_directory** — Disk location for spilling data when memory is exceeded.

**access_mode** — `automatic` (default), `read-only`, or `duckdb_write` for writes.
