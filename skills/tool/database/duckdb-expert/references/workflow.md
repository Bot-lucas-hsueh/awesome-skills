# Standard Workflow

## 8.1 Installation & Setup

### Python Installation

```bash
# pip
pip install duckdb

# conda
conda install -c conda-forge duckdb

# Verify installation
python -c "import duckdb; print(duckdb.__version__)"
```

### Python Quick Start

```python
import duckdb

# In-memory database (default)
con = duckdb.connect()

# Persistent database
con = duckdb.connect('my_database.duckdb')

# Run queries
result = con.execute("SELECT 1 AS num").fetchdf()
print(result)

# With pandas
import pandas as pd
df = con.execute("SELECT * FROM 'data.parquet' LIMIT 10").df()

# Close connection
con.close()
```

### R Installation & Usage

```r
# Install from CRAN
install.packages("duckdb")

# Install development version
remotes::install_github("duckdb/duckdb-r")

library(DBI)
con <- dbConnect(duckdb::duckdb())
dbExecute(con, "SELECT 42")

# With dplyr
library(dplyr)
tbl(con, "my_table") %>% filter(x > 10) %>% collect()
```

### Extension Loading

```sql
-- Install and load extensions
INSTALL spatial;
LOAD spatial;

INSTALL httpfs;
LOAD httpfs;

INSTALL delta;
LOAD delta;

-- Check available extensions
SELECT * FROM duckdb_extensions();

-- Load all bundled extensions
LOAD ALL;

-- Extension-specific setup for S3
SET s3_access_key_id = 'your_key';
SET s3_secret_access_key = 'your_secret';
SET s3_region = 'us-east-1';
SET s3_endpoint = 's3.amazonaws.com';
```

## 8.2 Data Loading

### Parquet Files

```sql
-- Read single Parquet file
SELECT * FROM 'data.parquet';

-- Read multiple files with glob
SELECT * FROM 's3://bucket/data/*.parquet';

-- Create table from Parquet
CREATE TABLE my_table AS SELECT * FROM 'large_file.parquet';

-- Parquet with predicate pushdown
SELECT * FROM 'data.parquet' WHERE date = '2024-01-01';
-- Only reads rows matching predicate from Parquet metadata
```

### CSV Files

```sql
-- Basic import
CREATE TABLE tbl AS SELECT * FROM read_csv('data.csv');

-- With options
CREATE TABLE tbl AS SELECT * FROM read_csv(
    'data.csv',
    header = true,
    delim = ',',
    columns = {
        'id': 'INTEGER',
        'name': 'VARCHAR',
        'date': 'DATE'
    }
);

-- Auto-detect types
SELECT * FROM read_csv_auto('data.csv');

-- Import with COPY
COPY table_name FROM 'data.csv' (HEADER, DELIMITER ',');
```

### Arrow Integration

```python
import duckdb
import pyarrow as pa

# Arrow to DuckDB
table = pa.table({'a': [1, 2, 3], 'b': ['x', 'y', 'z']})
con = duckdb.connect()
con.execute("CREATE TABLE t AS SELECT * FROM table")

# DuckDB to Arrow
result = con.execute("SELECT * FROM t").arrow()
# result is a PyArrow Table
```

### JSON Loading

```sql
-- Read JSON
SELECT * FROM read_json('data.json');

-- Read JSON Lines (newline-delimited JSON)
SELECT * FROM read_json_auto('data.jsonl');

-- Nested JSON
SELECT json_extract_string(data, '$.field.nested') FROM json_table;
```

### Creating Views

```sql
-- Create view over external file
CREATE VIEW sales_2024 AS
SELECT * FROM 'sales/*.parquet'
WHERE year = 2024;

-- View with aggregation
CREATE VIEW monthly_sales AS
SELECT 
    date_trunc('month', sale_date) AS month,
    category,
    sum(amount) AS total
FROM 'sales/*.parquet'
GROUP BY 1, 2;
```

## 8.3 Query Optimization

### EXPLAIN ANALYZE

```sql
-- Get query plan with timing
EXPLAIN ANALYZE SELECT * FROM large_table WHERE id > 1000;

-- Output:
-- ┌─────────────────────────────┐
-- │     Query Profile          │
-- ├─────────────────────────────┤
-- │ Total Time: 0.245s         │
-- │ Planning: 0.012s           │
-- │ Execution: 0.233s          │
-- └─────────────────────────────┘

-- Just plan (no execution)
EXPLAIN SELECT * FROM table WHERE condition;
```

### Statistics & Indexes

```sql
-- Update statistics (helps optimizer)
UPDATE STATISTICS table_name;
UPDATE STATISTICS table_name (column_name);

-- Create index
CREATE INDEX idx_user_id ON users(user_id);

-- Show statistics
PRAGMA table_info('users');

-- Force specific join order
EXPLAIN SELECT * FROM a JOIN b ON a.id = b.a_id;

-- With hints (DuckDB 1.0+)
EXPLAIN SELECT * FROM a HASH JOIN b ON a.id = b.a_id;
```

### Common Optimizations

```sql
-- Filter early to reduce rows
-- Bad:
SELECT sum(amount) FROM orders, customers WHERE orders.cust_id = customers.id;

-- Good:
SELECT sum(amount) 
FROM (SELECT * FROM orders WHERE date >= '2024-01-01') o
JOIN customers c ON o.cust_id = c.id;

-- Use LIMIT early if you only need top N
-- Bad:
SELECT * FROM large_table ORDER BY score DESC LIMIT 10;

-- Good:
SELECT * FROM (
    SELECT * FROM large_table ORDER BY score DESC LIMIT 1000
) ORDER BY score DESC LIMIT 10;

-- Parallel query execution
SET threads = 8;  -- Use 8 threads
```

### Monitoring Query Performance

```sql
-- Enable profiling
SET enable_profiling = true;
SET profiling_output = '/tmp/query.log';

-- Run query
SELECT complex_aggregation FROM big_table;

-- View profile
SELECT * FROM duckdb_query_profiling_information();
```
