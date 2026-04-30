# Snowflake Engineer Common Pitfalls

## #EP1: Leaving Warehouses Running

**❌ Wrong:**
```sql
-- Warehouse runs 24/7
CREATE WAREHOUSE analytics_wh WITH
  WAREHOUSE_SIZE = 'LARGE'
  AUTO_SUSPEND = 0;  -- Never suspends!
```

**✅ Right:**
```sql
-- Auto-suspend after idle period
CREATE WAREHOUSE analytics_wh WITH
  WAREHOUSE_SIZE = 'LARGE'
  AUTO_SUSPEND = 300  -- 5 minutes
  AUTO_RESUME = TRUE;
```

**Impact:** Can waste 70%+ of compute costs.

---

## #EP2: Not Using Partition Pruning

**❌ Wrong:**
```sql
-- Function on column prevents pruning
SELECT * FROM sales 
WHERE YEAR(sale_date) = 2024;

-- Implicit conversion prevents pruning
SELECT * FROM sales 
WHERE sale_date = '2024-01-01';  -- String comparison
```

**✅ Right:**
```sql
-- Direct column comparison enables pruning
SELECT * FROM sales 
WHERE sale_date >= '2024-01-01' 
  AND sale_date < '2024-01-02';

-- Match data types
SELECT * FROM sales 
WHERE sale_date = TO_DATE('2024-01-01');
```

**Impact:** Scans all partitions instead of relevant ones—10x+ slower.

---

## #EP3: Using SELECT * in Production

**❌ Wrong:**
```sql
-- Retrieves all columns
SELECT * FROM large_table 
WHERE date_column = CURRENT_DATE();
```

**✅ Right:**
```sql
-- Only needed columns
SELECT 
    customer_id,
    order_amount,
    order_status
FROM large_table 
WHERE date_column = CURRENT_DATE();
```

**Impact:** Wastes bandwidth and processing, especially with VARIANT columns.

---

## #EP4: Row-by-Row Processing

**❌ Wrong:**
```python
# Row-by-row UDF (slow)
def calculate_tax(row):
    return row['amount'] * 0.08

for row in dataframe.collect():
    row['tax'] = calculate_tax(row)
```

**✅ Right:**
```python
# Vectorized UDF (fast)
@pandas_udf
def calculate_tax_vectorized(amounts: pd.Series) -> pd.Series:
    return amounts * 0.08

df = df.withColumn("tax", calculate_tax_vectorized(col("amount")))
```

**Impact:** 100x+ performance difference for large datasets.

---

## #EP5: Ignoring Query Result Cache

**❌ Wrong:**
```sql
-- Unique comment breaks cache
SELECT COUNT(*) FROM sales;
-- vs
SELECT COUNT(*) FROM sales; /* report run 1 */
```

**✅ Right:**
```sql
-- Identical queries use cache
SELECT COUNT(*) FROM sales;
-- Same query = cached result
SELECT COUNT(*) FROM sales;
```

**Impact:** Missing 24-hour result cache eliminates instant query responses.

---

## #EP6: Not Setting Resource Monitors

**❌ Wrong:**
```sql
-- No spending limits
CREATE WAREHOUSE etl_wh WITH
  WAREHOUSE_SIZE = '4X-LARGE';
-- Could run up huge bill if left running
```

**✅ Right:**
```sql
-- Spending controls in place
CREATE RESOURCE MONITOR etl_budget WITH
  CREDIT_QUOTA = 1000
  FREQUENCY = MONTHLY
  TRIGGERS
    ON 80 PERCENT DO NOTIFY
    ON 100 PERCENT DO SUSPEND;

ALTER WAREHOUSE etl_wh SET RESOURCE_MONITOR = etl_budget;
```

**Impact:** Unexpected $10K+ bills from runaway queries.

---

## #EP7: Using the Wrong Warehouse Size

**❌ Wrong:**
```sql
-- Oversized for small queries
USE WAREHOUSE large_wh;
SELECT COUNT(*) FROM small_lookup_table;
```

**✅ Right:**
```sql
-- Right-size for workload
USE WAREHOUSE xsmall_wh;
SELECT COUNT(*) FROM small_lookup_table;

-- Scale up only when needed
USE WAREHOUSE large_wh;
INSERT INTO large_table SELECT * FROM massive_join;
```

**Impact:** 8x cost for no performance benefit on small queries.

---

## #EP8: Not Using Multi-Cluster for Concurrency

**❌ Wrong:**
```sql
-- Single cluster, queries queue
CREATE WAREHOUSE bi_wh WITH
  WAREHOUSE_SIZE = 'LARGE'
  MIN_CLUSTER_COUNT = 1
  MAX_CLUSTER_COUNT = 1;  -- No scaling!
```

**✅ Right:**
```sql
-- Auto-scaling for concurrent users
CREATE WAREHOUSE bi_wh WITH
  WAREHOUSE_SIZE = 'LARGE'
  MIN_CLUSTER_COUNT = 1
  MAX_CLUSTER_COUNT = 5
  SCALING_POLICY = 'STANDARD';
```

**Impact:** Queries queue during peak times, degrading user experience.

---

## #EP9: Loading Data Without File Format

**❌ Wrong:**
```sql
-- Defaults may not match data
COPY INTO my_table
FROM @my_stage
FILE_FORMAT = (TYPE = CSV);  -- Defaults!
```

**✅ Right:**
```sql
-- Explicit file format
CREATE FILE_FORMAT my_csv_format
  TYPE = CSV
  FIELD_DELIMITER = ','
  SKIP_HEADER = 1
  NULL_IF = ('NULL', 'null', '')
  EMPTY_FIELD_AS_NULL = TRUE
  DATE_FORMAT = 'YYYY-MM-DD'
  TIME_FORMAT = 'HH24:MI:SS'
  TIMESTAMP_FORMAT = 'YYYY-MM-DD HH24:MI:SS';

COPY INTO my_table
FROM @my_stage
FILE_FORMAT = (FORMAT_NAME = 'my_csv_format')
ON_ERROR = 'CONTINUE'
PURGE = TRUE;
```

**Impact:** Load failures, data corruption, manual intervention.

---

## #EP10: Not Handling NULLs Properly

**❌ Wrong:**
```sql
-- NULL in calculations causes issues
SELECT 
    customer_id,
    total_amount / transaction_count as avg_transaction
FROM customers;  -- NULL transaction_count = NULL result
```

**✅ Right:**
```sql
-- Handle NULLs explicitly
SELECT 
    customer_id,
    total_amount / NULLIF(transaction_count, 0) as avg_transaction,
    COALESCE(transaction_count, 0) as safe_count
FROM customers;
```

**Impact:** Silent data errors in calculations and aggregations.

---

## #EP11: Using UDFs for Simple Operations

**❌ Wrong:**
```python
# UDF for simple SQL operation
@udf
def add_one(x: int) -> int:
    return x + 1

# Called for every row
df.select(add_one(col("value")))
```

**✅ Right:**
```python
# Use SQL expression instead
df.select((col("value") + 1).alias("value_plus_one"))
```

**Impact:** UDF overhead for simple operations is 10x+ slower.

---

## #EP12: Not Testing with Production Data Volumes

**❌ Wrong:**
```sql
-- Test on 1K rows, deploy to 1B rows
CREATE TABLE test_table AS 
SELECT * FROM production_table LIMIT 1000;

-- Query works fast on test
SELECT * FROM test_table 
WHERE complex_condition;
```

**✅ Right:**
```sql
-- Test with realistic data volume
CREATE TABLE test_table AS 
SELECT * FROM production_table 
WHERE date_column >= DATEADD(day, -30, CURRENT_DATE());

-- Analyze query profile
EXPLAIN USING JSON 
SELECT * FROM test_table 
WHERE complex_condition;
```

**Impact:** Queries that work in dev fail in production due to scale.

---

## #EP13: Ignoring Data Skew

**❌ Wrong:**
```sql
-- Poor distribution causes skew
CREATE TABLE events (
    event_id STRING,
    user_id STRING,
    event_type STRING  -- 90% are 'page_view'
) CLUSTER BY (event_type);
```

**✅ Right:**
```sql
-- Better distribution
CREATE TABLE events (
    event_id STRING,
    user_id STRING,
    event_type STRING,
    event_date DATE
) CLUSTER BY (event_date, event_type);

-- Monitor clustering depth
SELECT SYSTEM$CLUSTERING_INFORMATION('events');
```

**Impact:** Some micro-partitions become hotspots, slowing queries.

---

## #EP14: Using Transactions Incorrectly

**❌ Wrong:**
```sql
-- Long transaction holds locks
BEGIN;
INSERT INTO large_table SELECT * FROM source;  -- Hours!
UPDATE another_table SET ...;  -- Waits for first
COMMIT;
```

**✅ Right:**
```sql
-- Shorter transactions
BEGIN;
INSERT INTO large_table SELECT * FROM source WHERE partition = 1;
COMMIT;

BEGIN;
INSERT INTO large_table SELECT * FROM source WHERE partition = 2;
COMMIT;
```

**Impact:** Long transactions block other operations, cause timeouts.

---

## #EP15: Not Monitoring Credit Consumption

**❌ Wrong:**
```python
# Run queries without tracking
session.sql("CALL massive_procedure()").collect()
# How much did it cost? Unknown.
```

**✅ Right:**
```python
# Track credit consumption
def track_query_cost(session: Session, query: str):
    # Get query ID
    result = session.sql(query).collect()
    query_id = session.sql("SELECT LAST_QUERY_ID()").collect()[0][0]
    
    # Get cost
    cost_info = session.sql(f"""
        SELECT 
            EXECUTION_TIME / 1000 as seconds,
            CREDITS_USED,
            BYTES_SCANNED / POWER(1024, 3) as gb_scanned
        FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY
        WHERE QUERY_ID = '{query_id}'
    """).collect()[0]
    
    log_metric("query_cost", cost_info['CREDITS_USED'])
    return result
```

**Impact:** No visibility into costs, can't optimize spending.

---

## #EP16: Using IN with Large Lists

**❌ Wrong:**
```sql
-- Large IN list is inefficient
SELECT * FROM customers 
WHERE customer_id IN (
    'id1', 'id2', 'id3',  -- ... 10,000 IDs
    'id10000'
);
```

**✅ Right:**
```sql
-- Use JOIN with values table
SELECT c.* 
FROM customers c
JOIN (
    SELECT column1 as customer_id 
    FROM VALUES ('id1'), ('id2'), ('id3') -- ... more IDs
) ids ON c.customer_id = ids.customer_id;

-- Or use temporary table
CREATE TEMPORARY TABLE target_ids AS 
SELECT $1 as customer_id FROM @stage/id_list.csv;

SELECT c.* 
FROM customers c
JOIN target_ids t ON c.customer_id = t.customer_id;
```

**Impact:** Large IN lists cause compilation issues and poor performance.

---

## #EP17: Not Using Streams for CDC

**❌ Wrong:**
```sql
-- Full table scan for changes
SELECT * FROM source_table 
WHERE last_modified > '2024-01-15';
-- Last_modified might not be reliable
```

**✅ Right:**
```sql
-- Create stream for change tracking
CREATE STREAM source_changes ON TABLE source_table;

-- Query only changes
SELECT * FROM source_changes;

-- Consume changes
INSERT INTO target_table 
SELECT * FROM source_changes 
WHERE METADATA$ACTION = 'INSERT';
```

**Impact:** Reliable CDC without modifying source tables.

---

## #EP18: Ignoring Storage Costs

**❌ Wrong:**
```sql
-- Default 1-day Time Travel for all tables
CREATE TABLE temp_analysis (...);
-- Never cleaned up, kept for years
```

**✅ Right:**
```sql
-- Adjust retention for temporary data
CREATE TABLE temp_analysis (...) 
DATA_RETENTION_TIME_IN_DAYS = 1;

-- Drop when done
DROP TABLE IF EXISTS temp_analysis;

-- Use transient tables (no Fail-safe)
CREATE TRANSIENT TABLE staging_data (...);
```

**Impact:** Unnecessary storage costs for temporary/analytical data.

---

## #EP19: Not Using Materialized Views

**❌ Wrong:**
```sql
-- Repeated expensive aggregation
CREATE VIEW daily_sales AS
SELECT 
    date_trunc('day', sale_date) as day,
    SUM(amount) as total
FROM sales
GROUP BY 1;

-- Every query recomputes
SELECT * FROM daily_sales WHERE day = '2024-01-15';
```

**✅ Right:**
```sql
-- Materialized for performance
CREATE MATERIALIZED VIEW daily_sales AS
SELECT 
    date_trunc('day', sale_date) as day,
    SUM(amount) as total
FROM sales
GROUP BY 1;

-- Query uses pre-computed results
SELECT * FROM daily_sales WHERE day = '2024-01-15';
```

**Impact:** Repeated expensive computations waste credits.

---

## #EP20: Using VARCHAR for All String Data

**❌ Wrong:**
```sql
-- Generic string types
CREATE TABLE users (
    id VARCHAR,           -- UUID - fixed length
    status VARCHAR,       -- Enum - few values
    email VARCHAR(16777216),  -- Over-allocated
    country_code VARCHAR  -- Always 2 chars
);
```

**✅ Right:**
```sql
-- Appropriate types and sizes
CREATE TABLE users (
    id STRING,            -- Default VARCHAR
    status VARCHAR(20),   -- Limited values
    email VARCHAR(320),   -- RFC compliant
    country_code CHAR(2)  -- Fixed length
);
```

**Impact:** Larger storage, slower comparisons, less optimization.
