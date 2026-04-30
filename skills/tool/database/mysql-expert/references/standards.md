# Standards & Reference

## 7.1 Official Documentation

- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
- [MySQL 8.0 SQL Statements](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [InnoDB Storage Engine](https://dev.mysql.com/doc/refman/8.0/en/innodb-storage-engine.html)
- [MySQL Indexes](https://dev.mysql.com/doc/refman/8.0/en/optimization.html#indexes)
- [Replication](https://dev.mysql.com/doc/refman/8.0/en/replication.html)
- [MySQL Performance Schema](https://dev.mysql.com/doc/refman/8.0/en/performance-schema.html)
- [MySQL Optimizer](https://dev.mysql.com/doc/refman/8.0/en/optimization.html)
- [JSON Functions](https://dev.mysql.com/doc/refman/8.0/en/json.html)
- [Partitioning](https://dev.mysql.com/doc/refman/8.0/en/partitioning.html)

## 7.2 Configuration Reference

### my.cnf / my.ini

```ini
[mysqld]
# Basic settings
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
pid_file=/var/run/mysqld/mysqld.pid
port=3306

# InnoDB settings
innodb_buffer_pool_size=4G
innodb_log_file_size=1G
innodb_flush_log_at_trx_commit=1
innodb_flush_method=O_DIRECT
innodb_file_per_table=1

# Connection settings
max_connections=200
wait_timeout=600
interactive_timeout=600

# Query cache (MySQL 8.0 removed, just for reference)
# query_cache_type=0

# Logging
slow_query_log=1
slow_query_log_file=/var/log/mysql/slow.log
long_query_time=2
log_queries_not_using_indexes=1

# Binary logging (replication)
server_id=1
log_bin=/var/log/mysql/mysql-bin
binlog_format=ROW
expire_logs_days=7

# Character set
character_set_server=utf8mb4
collation_server=utf8mb4_unicode_ci
```

### User Management

```sql
-- Create user
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'password';
CREATE USER 'appuser'@'%' IDENTIFIED BY 'password';

-- Grant privileges
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'appuser'@'localhost';
GRANT ALL PRIVILEGES ON mydb.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;

-- Role (MySQL 8.0+)
CREATE ROLE 'app_read', 'app_write';
GRANT SELECT ON mydb.* TO 'app_read';
GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'app_write';
```

## 7.3 Common Commands

### Index Operations

```sql
-- Create indexes
CREATE INDEX idx_name ON table(column);
CREATE UNIQUE INDEX idx_email ON users(email);
CREATE INDEX idx_composite ON orders(customer_id, order_date DESC);

-- Invisible index (MySQL 8.0+)
CREATE INDEX idx_test ON table(col) INVISIBLE;

-- Functional index (MySQL 8.0+)
CREATE INDEX idx_lower_email ON users((LOWER(email)));

-- Drop index
DROP INDEX idx_name ON table;
```

### Table Operations

```sql
-- Create table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Alter table
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users DROP COLUMN phone;
ALTER TABLE users MODIFY COLUMN email VARCHAR(500);
ALTER TABLE users ADD INDEX idx_email(email);
ALTER TABLE users RENAME TO app_users;
```

## 7.4 Version Compatibility

| Version | Status | Key Features |
|---------|--------|--------------|
| 8.4 LTS | Current | Instant ADD COLUMN, JSON TABLE, CTE improvements |
| 8.0 | Maintenance | Window functions, CTEs, JSON, roles |
| 5.7 | Security fixes only | JSON support, InnoDB improvements |
| 5.6 | EOL | Full-text indexes, GTID replication |

### Feature Availability

```sql
-- Check version
SELECT VERSION();

-- Check features
SHOW VARIABLES LIKE 'have_%';
SHOW ENGINES;

-- Check optimizer switches
SHOW VARIABLES LIKE 'optimizer_switch';
```
