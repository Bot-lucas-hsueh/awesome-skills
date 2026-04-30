# Scenario Examples

## 9.1 Basic Usage

**User:** "How do I get started with DuckDB?"

**Expert:**
> **Getting Started:**
>
> 1. Install DuckDB (Python, CLI, or R)
> 2. Connect to database or use in-memory
> 3. Run queries on Parquet/CSV files
>
> ```python
> # Python
> import duckdb
> con = duckdb.connect('analytics.duckdb')
> con.execute("SELECT 1").fetchall()
>
> # Query Parquet directly
> con.execute("SELECT * FROM 'data.parquet' LIMIT 10").df()
> ```

> **CLI:**
> ```bash
> duckdb
> .mode csv
> SELECT * FROM 'data.csv';
> ```

## 9.2 Production Setup

**User:** "How do I configure DuckDB for production analytics?"

**Expert:**
> **Production Checklist:**
>
> - [ ] Configure memory_limit based on available RAM
> - [ ] Set threads for parallel processing
> - [ ] Use persistent database for caching
> - [ ] Configure temp_directory for large queries
> - [ ] Enable progress_bar for long queries
>
> ```python
> con.execute("SET memory_limit = '8GB'")
> con.execute("SET threads = 4")
> con.execute("SET max_temp_directory_size = '4GB'")
> ```

## 9.3 ETL Pipeline

**User:** "How do I build an ETL pipeline with DuckDB?"

**Expert:**
> **ETL Pipeline:**
>
> ```python
> import duckdb
> import pandas as pd
>
> con = duckdb.connect('etl.duckdb')
>
> # EXTRACT: Read from multiple sources
> con.execute("""
>     CREATE TABLE raw_sales AS
>     SELECT * FROM 's3://bucket/raw/sales_2024.parquet'
> """)
>
> # TRANSFORM: Clean and aggregate
> con.execute("""
>     CREATE TABLE daily_sales AS
>     SELECT
>         DATE_TRUNC('day', sale_date) AS date,
>         category,
>         SUM(amount) AS revenue,
>         COUNT(*) AS transactions
>     FROM raw_sales
>     WHERE status = 'completed'
>     GROUP BY 1, 2
> """)
>
> # LOAD: Export to target
> con.execute("""
>     COPY daily_sales TO 's3://bucket/analytics/daily_sales.parquet'
>     (FORMAT PARQUET, COMPRESSION SNAPPY)
> """)
> ```

## 9.4 Data Analysis

**User:** "How do I analyze large datasets with DuckDB?"

**Expert:**
> **Analysis Patterns:**
>
> **Time Series Analysis:**
> ```sql
> SELECT
>     DATE_TRUNC('month', order_date) AS month,
>     SUM(total) AS revenue,
>     COUNT(*) AS orders,
>     AVG(total) AS avg_order_value
> FROM orders
> WHERE order_date >= '2024-01-01'
> GROUP BY 1
> ORDER BY 1;
> ```
>
> **Cohort Analysis:**
> ```sql
> WITH first_purchase AS (
>     SELECT customer_id, MIN(order_date) AS first_date
>     FROM orders
>     GROUP BY customer_id
> ),
> cohorts AS (
>     SELECT
>         DATE_TRUNC('month', first_date) AS cohort,
>         customer_id
>     FROM first_purchase
> )
> SELECT
>     cohort,
>     COUNT(*) AS customers,
>     COUNT(DISTINCT customer_id) AS retained
> FROM orders o
> JOIN cohorts c ON o.customer_id = c.customer_id
> GROUP BY cohort;
> ```
>
> **Moving Average:**
> ```sql
> SELECT
>     date,
>     value,
>     AVG(value) OVER (
>         ORDER BY date
>         ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
>     ) AS moving_avg_7d
> FROM metrics;
> ```

## 9.5 Performance Optimization

**User:** "How do I optimize DuckDB queries?"

**Expert:**
> **Optimization Techniques:**
>
> 1. **Filter Early:**
> ```sql
> -- BAD: Load all, filter in Python
> df = con.execute("SELECT * FROM large_table").df()
> filtered = df[df['date'] > '2024-01-01']
>
> -- GOOD: Filter in DuckDB
> df = con.execute("""
>     SELECT * FROM large_table
>     WHERE date > '2024-01-01'
> """).df()
> ```
>
> 2. **Use Predicate Pushdown (Parquet):**
> ```sql
> -- DuckDB automatically pushes down
> SELECT * FROM 'large_file.parquet' WHERE region = 'US'
> -- Only reads matching row groups
> ```
>
> 3. **Create Indexes:**
> ```sql
> CREATE INDEX idx_customer ON orders(customer_id);
> ```
>
> 4. **Parallel Processing:**
> ```sql
> SET threads = 8;
> SET memory_limit = '16GB';
> ```

## 9.6 Integration with ML

**User:** "How do I use DuckDB with machine learning?"

**Expert:**
> **ML Integration:**
>
> ```python
> import duckdb
> from sklearn.model_selection import train_test_split
>
> con = duckdb.connect()
>
> # Load training data
> df = con.execute("""
>     SELECT * FROM 'training_data.parquet'
>     WHERE target IS NOT NULL
> """).df()
>
> X = df[['feature1', 'feature2', 'feature3']]
> y = df['target']
>
> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
>
> # Train model
> model.fit(X_train, y_train)
> score = model.score(X_test, y_test)
>
> # Batch prediction
> new_data = con.execute("""
>     SELECT feature1, feature2, feature3
>     FROM 'prediction_data.parquet'
> """).df()
>
> predictions = model.predict(new_data)
> ```

## 9.7 Working with External Data

**User:** "How do I query data from S3?"

**Expert:**
> **S3 Integration:**
>
> ```sql
> INSTALL httpfs;
> LOAD httpfs;
>
> SET s3_access_key_id = 'AKIA...';
> SET s3_secret_access_key = '...';
> SET s3_region = 'us-east-1';
>
> -- Query directly from S3
> SELECT * FROM 's3://bucket/data/*.parquet'
> WHERE date > '2024-01-01';
> ```
>
> **Multiple Data Sources:**
> ```sql
> SELECT *
> FROM 's3://bucket/raw/transactions.parquet' t
> JOIN 's3://bucket/lookup/customers.parquet' c
> ON t.customer_id = c.id;
> ```

## 9.8 Migration from SQL

**User:** "I know SQL, how do I use DuckDB?"

**Expert:**
> **Key Differences:**
>
> | SQL Feature | DuckDB |
> |--------------|--------|
> | LIMIT | LIMIT (same) |
> | String concatenation | CONCAT or \|\| |
> | Date functions | DATE_TRUNC, DATE_DIFF |
> | Window functions | FULL support |
> | CTEs | WITH clause (same) |
> | CTAS | CREATE TABLE AS (same) |
>
> ```sql
> -- Example: All standard SQL works
> WITH monthly AS (
>     SELECT
>         strftime(order_date, '%Y-%m') AS month,
>         SUM(amount) AS revenue
>     FROM orders
>     GROUP BY 1
> )
> SELECT * FROM monthly
> WHERE revenue > 10000
> ORDER BY revenue DESC;
> ```
