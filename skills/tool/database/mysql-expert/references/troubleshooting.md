# Troubleshooting

## 8.1 Connection Issues

### Access Denied

```sql
-- Reset root password
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
FLUSH PRIVILEGES;

-- Check user host permissions
SELECT user, host FROM mysql.user WHERE user = 'username';

-- Skip-grant-tables (emergency)
mysqld --skip-grant-tables
```

**Common causes:**
- Wrong password
- User host mismatch (user@'%' vs user@'localhost')
- max_connections exceeded
- Firewall blocking port 3306

### Connection Pool Exhaustion

```sql
-- Check connections
SHOW STATUS LIKE 'Threads_connected';
SHOW STATUS LIKE 'Max_used_connections';

-- Increase limit
SET GLOBAL max_connections = 500;

-- Kill idle connections
SELECT GROUP_CONCAT(id) FROM information_schema.processlist 
WHERE Command = 'Sleep' AND Time > 300;

KILL <id_list>;
```

## 8.2 Performance Issues

### Slow Queries

```sql
-- Enable slow query log
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;

-- Analyze slow query log
mysqldumpslow -s t /var/log/mysql/slow.log

-- Use EXPLAIN
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';  -- MySQL 8.0+
```

### Table Scans

```sql
-- Check table statistics
ANALYZE TABLE users;
SHOW TABLE STATUS LIKE 'users';

-- Force index
SELECT * FROM users FORCE INDEX (idx_email) WHERE email LIKE 'a%';

-- Check index usage
SHOW STATUS LIKE 'Handler_read%';
```

### Lock Waits

```sql
-- Check locks
SHOW ENGINE INNODB STATUS;

-- Find blocking transactions
SELECT * FROM information_schema.INNODB_LOCK_WAITS;

-- Set lock timeout
SET innodb_lock_wait_timeout = 5;

-- Deadlock info
SHOW ENGINE INNODB STATUS;
-- Look for "LATEST DETECTED DEADLOCK" section
```

## 8.3 Replication Issues

### Replication Lag

```sql
-- Check slave status
SHOW SLAVE STATUS\G

-- On replica
SHOW VARIABLES LIKE 'read_only';
SHOW VARIABLES LIKE 'super_read_only';

-- Skip binary log event
STOP SLAVE;
SET GLOBAL sql_slave_skip_counter = 1;
START SLAVE;
```

### GTID Issues

```sql
-- Check GTID mode
SHOW VARIABLES LIKE 'gtid_mode';

-- Skip failed transaction
SET GTID_NEXT = 'uuid:number';
BEGIN; COMMIT;
SET GTID_NEXT = 'AUTOMATIC';
```

## 8.4 InnoDB Issues

### Tablespace Full

```sql
-- Check tablespace usage
SELECT 
    TABLE_SCHEMA,
    TABLE_NAME,
    ROUND(DATA_LENGTH / 1024 / 1024, 2) AS data_mb,
    ROUND(INDEX_LENGTH / 1024 / 1024, 2) AS index_mb
FROM information_schema.TABLES
ORDER BY DATA_LENGTH DESC;

-- Shrink InnoDB tablespace
OPTIMIZE TABLE mytable;

-- Check innodb_file_per_table
SHOW VARIABLES LIKE 'innodb_file_per_table';
```

### Corruption

```sql
-- Check tables
CHECK TABLE mytable;

-- Repair (if MyISAM, use myisamchk)
REPAIR TABLE mytable;

-- Recover from backup or dump
mysqldump database > backup.sql
```

## 8.5 Backup/Restore

```bash
# Hot backup with mysqldump
mysqldump --single-transaction --routines --triggers --all-databases > backup.sql

# Point-in-time recovery
mysqlbinlog --stop-datetime="2024-01-15 10:00:00" mysql-bin.000001 | mysql

# Restore specific database
mysql database < backup.sql

# Stream backup (compressed)
mysqldump --all-databases | gzip > backup.sql.gz
```

## 8.6 MySQL 8.0 Specific

### Default Changes

```sql
-- Caching_sha2_password default (compatibility)
ALTER USER 'user'@'host' IDENTIFIED WITH mysql_native_password BY 'password';

-- JSON defaults
CREATE TABLE t (data JSON DEFAULT (JSON_OBJECT()));

-- CTE recursive limit
SET cte_max_recursion_depth = 1000;
```
