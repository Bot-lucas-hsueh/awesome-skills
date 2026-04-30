# Standard Workflow

## 8.1 Installation & Setup

### Install PostgreSQL

```bash
# Ubuntu
sudo apt update
sudo apt install postgresql postgresql-contrib

# macOS
brew install postgresql@15
brew services start postgresql@15

# Start service
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### Basic Connection

```bash
# Connect as postgres user
sudo -u postgres psql

# Connect as specific user
psql -U username -d database

# With connection parameters
psql -h localhost -p 5432 -U username -d database
```

### Create Database and User

```sql
-- Create user
CREATE USER myapp WITH PASSWORD 'secure_password';

-- Create database
CREATE DATABASE myapp OWNER myapp;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE myapp TO myapp;

-- Connect to database
\c myapp
```

## 8.2 Schema Operations

### Create Tables

```sql
-- Basic table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW()
);

-- With constraints
CREATE TABLE orders (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id),
    status VARCHAR(20) DEFAULT 'pending',
    total DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create index
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_orders_status ON orders(status);
```

### Modify Schema

```sql
-- Add column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Add constraint
ALTER TABLE orders ADD CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id);

-- Rename table
ALTER TABLE users RENAME TO app_users;

-- Add index
CREATE INDEX idx_users_email ON app_users(email);
```

## 8.3 Query Operations

### Basic Queries

```sql
-- Select
SELECT * FROM users;

-- With WHERE
SELECT * FROM users WHERE email = 'test@example.com';

-- Join
SELECT o.*, u.name 
FROM orders o
JOIN users u ON o.user_id = u.id;

-- Aggregation
SELECT status, COUNT(*) as count
FROM orders
GROUP BY status;
```

### Window Functions

```sql
-- Running total
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) as running_total
FROM sales;

-- Rank
SELECT 
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as dept_rank
FROM employees;
```

### CTEs (Common Table Expressions)

```sql
WITH monthly_sales AS (
    SELECT 
        DATE_TRUNC('month', order_date) as month,
        SUM(total) as revenue
    FROM orders
    GROUP BY 1
)
SELECT * FROM monthly_sales
WHERE revenue > 10000;
```

## 8.4 Transaction Operations

```sql
-- Begin transaction
BEGIN;

-- Or with isolation level
BEGIN ISOLATION LEVEL REPEATABLE READ;

-- Commit
COMMIT;

-- Rollback
ROLLBACK;

-- Savepoint
SAVEPOINT sp1;

-- Rollback to savepoint
ROLLBACK TO SAVEPOINT sp1;
```

## 8.5 Index Operations

```sql
-- Create index
CREATE INDEX idx_name ON table(column);

-- Unique index
CREATE UNIQUE INDEX idx_email ON users(email);

-- Composite index
CREATE INDEX idx_orders_status_date ON orders(status, created_at DESC);

-- Partial index
CREATE INDEX idx_active ON users(last_login)
WHERE deleted_at IS NULL;

-- Expression index
CREATE INDEX idx_lower_email ON users(LOWER(email));

-- Reindex
REINDEX TABLE users;

-- Analyze
ANALYZE users;
```

## 8.6 Maintenance Operations

```sql
-- Vacuum
VACUUM;
VACUUM (VERBOSE, ANALYZE) users;

-- Check table size
SELECT pg_size_pretty(pg_total_relation_size('users'));

-- Check index usage
SELECT indexrelname, idx_scan, idx_tup_read, idx_tup_fetch
FROM pg_stat_user_indexes
WHERE idx_scan = 0;

-- List locks
SELECT * FROM pg_locks WHERE NOT GRANTED;
```

## 8.7 User and Permission Operations

```sql
-- Create role
CREATE ROLE myapp LOGIN PASSWORD 'password';

-- Grant privileges
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO myapp;

-- Grant sequence privileges
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO myapp;

-- Default privileges
ALTER DEFAULT PRIVILEGES IN SCHEMA public 
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myapp;
```

## 8.8 Backup and Restore

```bash
# Backup single database
pg_dump -U postgres mydb > backup.sql

# Backup all databases
pg_dumpall -U postgres > full_backup.sql

# Restore
psql -U postgres mydb < backup.sql

# Point-in-time recovery
pg_restore -U postgres -d mydb --jobs=4 backup.dump
```
