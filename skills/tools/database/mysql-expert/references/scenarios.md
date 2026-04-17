# Scenario Examples

## 9.1 Basic Usage

**User:** "How do I get started with MySQL?"

**Expert:**
> **Getting Started:**
>
> 1. Install MySQL server
> 2. Start the MySQL service
> 3. Connect with mysql client
>
> ```bash
> # Install on Ubuntu
> sudo apt install mysql-server
> sudo systemctl start mysql
> sudo systemctl enable mysql
>
> # Connect
> mysql -u root -p
>
> # Create database
> CREATE DATABASE myapp;
> ```

## 9.2 Production Setup

**User:** "How do I configure MySQL for production?"

**Expert:**
> **Production Checklist:**
>
> - [ ] Configure InnoDB buffer pool (70-80% of available RAM)
> - [ ] Set appropriate max_connections
> - [ ] Enable slow query log
> - [ ] Configure binary logging for replication
> - [ ] Set character set to utf8mb4
> - [ ] Enable SSL/TLS connections
> - [ ] Configure backup strategy
> - [ ] Set up replication if needed

> **Example my.cnf for production:**
> ```ini
> [mysqld]
> innodb_buffer_pool_size = 8G
> max_connections = 300
> slow_query_log = 1
> long_query_time = 2
> binlog_format = ROW
> ssl_ca = ca.pem
> ssl_cert = server-cert.pem
> ssl_key = server-key.pem
> ```

## 9.3 Troubleshooting

**User:** "My query is running slow. How do I debug?"

**Expert:**
> **Troubleshooting Steps:**
>
> 1. Enable slow query log and identify slow queries
> 2. Use EXPLAIN to analyze query plan
> 3. Check for missing indexes
> 4. Review table statistics
> 5. Check for lock contention
>
> ```sql
> -- Enable slow query log
> SET GLOBAL slow_query_log = 'ON';
> SET GLOBAL long_query_time = 1;
>
> -- Analyze query
> EXPLAIN SELECT * FROM orders WHERE customer_id = 123;
>
> -- Check table statistics
> ANALYZE TABLE orders;
>
> -- View running queries
> SHOW PROCESSLIST;
> ```

## 9.4 Replication Setup

**User:** "How do I set up MySQL replication?"

**Expert:**
> **Master-Slave Replication:**
>
> **On Master:**
> ```ini
> [mysqld]
> server-id = 1
> log_bin = /var/log/mysql/mysql-bin
> binlog_format = ROW
> ```
>
> ```sql
> CREATE USER 'repl'@'%' IDENTIFIED BY 'password';
> GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';
> ```
>
> **On Slave:**
> ```ini
> [mysqld]
> server-id = 2
> relay_log = /var/log/mysql/mysql-relay-bin
> read_only = ON
> ```
>
> ```sql
> CHANGE MASTER TO
>   MASTER_HOST = 'master_host',
>   MASTER_USER = 'repl',
>   MASTER_PASSWORD = 'password',
>   MASTER_LOG_FILE = 'mysql-bin.000001',
>   MASTER_LOG_POS = 120;
>
> START SLAVE;
> SHOW SLAVE STATUS\G
> ```

## 9.5 Backup and Recovery

**User:** "How do I backup and restore MySQL?"

**Expert:**
> **Backup:**
>
> ```bash
> # Logical backup
> mysqldump -u root -p mydb > backup.sql
>
> # With all databases
> mysqldump -u root -p --all-databases > full_backup.sql
>
> # With transactions (for InnoDB)
> mysqldump -u root -p --single-transaction --routines --triggers mydb > backup.sql
>
> # Point-in-time recovery
> mysqlbinlog mysql-bin.000001 > backup.sql
> ```
>
> **Restore:**
> ```bash
> mysql -u root -p mydb < backup.sql
>
> # Restore specific table
> mysql -u root -p mydb -e "DROP TABLE IF EXISTS mytable;"
> mysqldump -u root -p mydb mytable | mysql -u root -p mydb
> ```

## 9.6 Performance Optimization

**User:** "How do I optimize MySQL performance?"

**Expert:**
> **Key Optimization Areas:**
>
> 1. **Index Optimization**
> ```sql
> CREATE INDEX idx_customer ON orders(customer_id);
> CREATE INDEX idx_status_date ON orders(status, order_date);
> ```
>
> 2. **Query Optimization**
> ```sql
> -- Use EXPLAIN ANALYZE (MySQL 8.0+)
> EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'pending';
>
> -- Avoid SELECT *
> SELECT order_id, customer_id, total FROM orders;
> ```
>
> 3. **InnoDB Tuning**
> ```ini
> innodb_buffer_pool_size = 8G
> innodb_log_file_size = 1G
> innodb_flush_log_at_trx_commit = 1
> innodb_flush_method = O_DIRECT
> ```
>
> 4. **Connection Pooling**
> ```ini
> max_connections = 300
> wait_timeout = 600
> ```

## 9.7 Security Hardening

**User:** "How do I secure MySQL?"

**Expert:**
> **Security Checklist:**
>
> 1. **Change root password**
> ```sql
> ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_strong_password';
> ```
>
> 2. **Create application user with minimal privileges**
> ```sql
> CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'password';
> GRANT SELECT, INSERT, UPDATE, DELETE ON mydb.* TO 'appuser'@'localhost';
> FLUSH PRIVILEGES;
> ```
>
> 3. **Enable SSL**
> ```ini
> require_secure_transport = ON
> ```
>
> 4. **Remove test database**
> ```sql
> DROP DATABASE IF EXISTS test;
> ```
>
> 5. **Disable remote root login**
> ```sql
> DROP USER 'root'@'%';
> ```

## 9.8 High Availability

**User:** "How do I set up MySQL HA?"

**Expert:**
> **Options:**
>
> 1. **Master-Slave Replication** (basic HA)
> 2. **MySQL Group Replication** (MySQL 8.0+)
> 3. **MySQL InnoDB Cluster** (MySQL Shell + Group Replication)
> 4. **ProxySQL** (read/write splitting)
> 5. **Orchestrator** (automatic failover)
>
> **InnoDB Cluster Setup:**
> ```sql
> -- On each node
> CREATE CLUSTER 'mycluster';
> -- Add instances
> cluster.addInstance('user@host2:3306');
> cluster.addInstance('user@host3:3306');
>
> -- Check status
> cluster.status();
> ```
