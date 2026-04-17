# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Fix |
|---|---------|----------|--------|-----|
| 1 | Confusing persistent vs in-memory | 🟡 Medium | Data loss | Understand connect modes |
| 2 | NULL handling in aggregations | 🟡 Medium | Wrong results | Use COALESCE/IFNULL |
| 3 | Missing file extension for glob | 🟡 Medium | No files matched | Include *.parquet not just * |
| 4 | Auto-detect fails on large files | 🟡 Medium | Slow loading | Specify schema explicitly |
| 5 | Forgetting ORDER BY for determinism | 🟡 Medium | Inconsistent results | Always ORDER when needed |
| 6 | Timestamp vs Date confusion | 🟡 Medium | Filter issues | Match column types |

### Mistake 1: Persistent vs In-Memory

```python
import duckdb

# WRONG: In-memory by default - data lost after close
con = duckdb.connect()  # In-memory
con.execute("CREATE TABLE test AS SELECT 1 AS x")
con.close()
con = duckdb.connect()  # New connection, table gone!
print(con.execute("SELECT * FROM test").fetchall())  # Error!

# CORRECT: Use persistent database
con = duckdb.connect('my_data.duckdb')  # Persistent file
con.execute("CREATE TABLE test AS SELECT 1 AS x")
con.close()

con = duckdb.connect('my_data.duckdb')  # Table still exists
print(con.execute("SELECT * FROM test").fetchall())  # [(1,)]

# WRONG: Loading large file into memory twice
df = con.execute("SELECT * FROM 'big_file.parquet'").df()
df2 = con.execute("SELECT * FROM 'big_file.parquet'").df()  # Reloads!

# CORRECT: Reuse the result
df = con.execute("SELECT * FROM 'big_file.parquet'").df()
df2 = df  # Or filter from df
```

### Mistake 2: NULL Handling

```sql
-- WRONG: NULL breaks aggregations
SELECT 
    category,
    sum(amount) AS total,  -- NULL if any amount is NULL
    avg(amount) AS average  -- NULL if any amount is NULL
FROM sales;

-- CORRECT: Handle NULLs
SELECT 
    category,
    sum(COALESCE(amount, 0)) AS total,
    avg(IFNULL(amount, 0)) AS average,
    count(amount) AS non_null_count,  -- Counts non-NULL only
    count(*) AS total_rows
FROM sales;

-- NULL in WHERE
SELECT * FROM users WHERE age > 18;
-- Excludes NULL ages! Use explicit NULL handling:
SELECT * FROM users WHERE COALESCE(age, 0) > 18;

-- NULL comparison gotcha
SELECT NULL = NULL;  -- Returns NULL, not true!
SELECT NULL IS NULL;  -- Returns true
SELECT COALESCE(column, default_value) = 'value';
```

### Mistake 3: File Glob Patterns

```sql
-- WRONG: Missing extension
SELECT * FROM 'data/*';  -- Matches nothing or directories

-- CORRECT: Include file extension
SELECT * FROM 'data/*.parquet';
SELECT * FROM 'data/*.csv';
SELECT * FROM 'data/*.json';

-- Multi-level glob
SELECT * FROM 'data/**/*.parquet';  -- Recursive

-- Specific files
SELECT * FROM 'data/file1.parquet';
SELECT * FROM 'data/{file1,file2,file3}.parquet';
```

### Mistake 4: Schema Auto-Detection

```sql
-- WRONG: Auto-detect on large files is slow
SELECT * FROM read_csv_auto('huge_file.csv');  -- Scans entire file first

-- CORRECT: Specify schema
SELECT * FROM read_csv(
    'file.csv',
    columns = {
        'id': 'INTEGER',
        'name': 'VARCHAR',
        'date': 'DATE',
        'amount': 'DECIMAL(10,2)'
    }
);

-- For Parquet: explicit schema often faster
SELECT * FROM read_parquet(
    'file.parquet',
    schema = {'id': 'INTEGER', 'name': 'VARCHAR'}
);
```

### Mistake 5: ORDER BY Determinism

```sql
-- WRONG: No ORDER BY, results may vary
SELECT category, sum(amount) FROM orders GROUP BY category;
-- Returns rows in arbitrary order

-- CORRECT: Always ORDER when order matters
SELECT category, sum(amount) AS total 
FROM orders 
GROUP BY category
ORDER BY total DESC;

-- For TOP N queries
-- Without ORDER BY (WRONG)
SELECT * FROM users LIMIT 10;  -- Arbitrary 10 rows

-- With ORDER BY (CORRECT)
SELECT * FROM users ORDER BY created_at DESC LIMIT 10;  -- Top 10 most recent

-- Window functions need ORDER BY too
SELECT 
    name,
    department,
    salary,
    rank() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;
```

### Mistake 6: Timestamp vs Date

```sql
-- Type mismatch causes empty results
CREATE TABLE events (
    event_date DATE,
    event_time TIMESTAMP
);

INSERT INTO events VALUES ('2024-01-15', '2024-01-15 10:30:00');

-- WRONG: Comparing DATE to timestamp literal
SELECT * FROM events WHERE event_date = '2024-01-15 10:30:00';  -- Empty!

-- CORRECT: Match types
SELECT * FROM events WHERE event_date = DATE '2024-01-15';
SELECT * FROM events WHERE event_time = TIMESTAMP '2024-01-15 10:30:00';

-- Cast when needed
SELECT * FROM events WHERE event_date = CAST('2024-01-15' AS DATE);
SELECT * FROM events WHERE CAST(event_date AS TIMESTAMP) > '2024-01-15'::TIMESTAMP;
```

## 10.2 Performance Anti-Patterns

| # | Anti-Pattern | Severity | Fix |
|---|--------------|----------|-----|
| 1 | No indexes on large tables | 🔴 High | Create indexes on filter columns |
| 2 | Unoptimized JOINs | 🔴 High | Smaller table first, broadcast |
| 3 | Subqueries in loops | 🔴 High | Rewrite as JOIN/CTE |
| 4 | Loading full data unnecessarily | 🟡 Medium | Use predicate pushdown |
| 5 | Large CSV without schema | 🟡 Medium | Specify columns upfront |
| 6 | Multiple file glob passes | 🟡 Medium | Combine into single query |
| 7 | Cartesian products | 🔴 High | Always include JOIN conditions |

### Anti-Pattern 1: No Indexes on Large Tables

```sql
-- DuckDB is columnar, indexes work differently than row stores
-- Primary use: filtered lookups on large tables

-- WRONG: Full scan for single-row lookup
SELECT * FROM users WHERE email = 'user@example.com';

-- CORRECT: Create index for frequent lookups
CREATE INDEX idx_users_email ON users(email);

-- After index: O(1) lookup instead of O(n) scan
SELECT * FROM users WHERE email = 'user@example.com';

-- Index types (DuckDB 0.9+)
CREATE INDEX idx_name ON table(column) USING ZONEMAP;  -- For range queries
CREATE INDEX idx_name ON table(column) USING BTREE;    -- For equality
```

### Anti-Pattern 2: Unoptimized JOINs

```sql
-- WRONG: Large table first (broadcasts big table)
SELECT *
FROM large_table  -- 100M rows
JOIN small_table   -- 1K rows
ON large_table.id = small_table.id;

-- CORRECT: Small table first (broadcasts small table)
SELECT *
FROM small_table
JOIN large_table
ON small_table.id = large_table.id;

-- Explicit broadcast join
SELECT *
FROM small_table
INNER JOIN large_table ON small_table.id = large_table.id;

-- For hash join: disable probing optimization
SET disabled_optimizers = 'filter_pushdown';
```

### Anti-Pattern 3: Subqueries in Loops

```python
# WRONG: Subquery per row (very slow)
for user_id in user_ids:
    result = con.execute(f"""
        SELECT sum(amount) 
        FROM orders 
        WHERE user_id = {user_id}
    """).fetchone()

# CORRECT: Single query with GROUP BY
result = con.execute("""
    SELECT user_id, sum(amount) AS total
    FROM orders
    WHERE user_id IN ({','.join(str(id) for id in user_ids)})
    GROUP BY user_id
""").fetchall()
result_dict = {row[0]: row[1] for row in result}
```

### Anti-Pattern 4: Loading Full Data Unnecessarily

```sql
-- WRONG: Load everything, filter in Python
df = con.execute("SELECT * FROM large_table").df()  # Loads 10GB
filtered = df[df['date'] > '2024-01-01']  # Filters in memory

-- CORRECT: Filter in DuckDB
df = con.execute("""
    SELECT * 
    FROM large_table 
    WHERE date > '2024-01-01'
""").df()  # Only loads filtered data

-- Parquet predicate pushdown
SELECT * FROM 'large_file.parquet' WHERE date > '2024-01-01';
-- DuckDB reads only row groups matching predicate
```

### Anti-Pattern 5: Large CSV Without Schema

```sql
-- WRONG: Auto-detect is slow
df = con.execute("SELECT * FROM read_csv_auto('big.csv')").df()

-- CORRECT: Define schema upfront
df = con.execute("""
    SELECT * FROM read_csv(
        'big.csv',
        columns = {
            'id': 'INTEGER',
            'name': 'VARCHAR',
            'amount': 'DECIMAL(10,2)',
            'date': 'DATE'
        }
    )
""").df()
```

### Anti-Pattern 6: Multiple File Glob Passes

```sql
-- WRONG: Multiple glob queries
data1 = con.execute("SELECT * FROM '2024/*.parquet'").df()
data2 = con.execute("SELECT * FROM '2023/*.parquet'").df()
combined = pd.concat([data1, data2])  # Loads all data

-- CORRECT: Single query with combined glob
df = con.execute("""
    SELECT * FROM '*.parquet'
    UNION ALL
    SELECT * FROM 'archive/*.parquet'
""").df()

-- Or use recursive glob
df = con.execute("""
    SELECT * FROM 'data/**/*.parquet'
""").df()
```

### Anti-Pattern 7: Cartesian Products

```sql
-- WRONG: Missing JOIN condition
SELECT *
FROM users, orders;
-- Returns users × orders rows!

-- CORRECT: Always specify JOIN condition
SELECT *
FROM users u
JOIN orders o ON u.id = o.user_id;

-- Prevent accidental cross joins
SET enable_progress_bar = true;  -- Shows row count

-- If you need all combinations, be explicit
SELECT * FROM categories, products;  -- Intentional Cartesian product
```
