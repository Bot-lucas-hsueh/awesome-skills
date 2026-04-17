# Scenario Examples

## 9.1 Basic Usage

**User:** "How do I get started with PostgreSQL?"

**Expert:**
> **Getting Started:**
>
> 1. Install PostgreSQL
> 2. Start the PostgreSQL service
> 3. Connect with psql client
>
> ```bash
> # Install on Ubuntu
> sudo apt install postgresql
> sudo systemctl start postgresql
> sudo systemctl enable postgresql
>
> # Connect
> psql -U postgres
>
> # Create database
> CREATE DATABASE myapp;
> ```

## 9.2 Production Setup

**User:** "How do I configure PostgreSQL for production?"

**Expert:**
> **Production Checklist:**
>
> - [ ] Configure shared_buffers (25% of RAM)
> - [ ] Set work_mem appropriately
> - [ ] Configure wal_level for replication
> - [ ] Enable pg_stat_statements extension
> - [ ] Set up connection pooling (pgBouncer)
> - [ ] Configure WAL archiving
> - [ ] Enable autovacuum
> - [ ] Set up backup strategy (pg_dump or pg_basebackup)

> **Example postgresql.conf for production:**
> ```ini
> shared_buffers = 4GB
> work_mem = 64MB
> maintenance_work_mem = 512MB
> effective_cache_size = 12GB
> wal_level = replica
> max_connections = 200
> random_page_cost = 1.1
> ```

## 9.3 Troubleshooting

**User:** "My query is running slow. How do I debug?"

**Expert:**
> **Troubleshooting Steps:**
>
> 1. Enable pg_stat_statements extension
> 2. Use EXPLAIN ANALYZE to analyze query plan
> 3. Check for missing indexes
> 4. Review table bloat
> 5. Check for locks
>
> ```sql
> -- Enable extension
> CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
>
> -- Find slow queries
> SELECT query, calls, mean_time, total_time
> FROM pg_stat_statements
> ORDER BY mean_time DESC
> LIMIT 10;
>
> -- Analyze query
> EXPLAIN (ANALYZE, BUFFERS, TIMING)
> SELECT * FROM orders WHERE customer_id = 123;
>
> -- Check for locks
> SELECT * FROM pg_locks WHERE NOT GRANTED;
>
> -- Check table size and bloat
> SELECT schemaname, tablename, pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename))
> FROM pg_tables
> ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;
> ```

## 9.4 Replication Setup

**User:** "How do I set up PostgreSQL streaming replication?"

**Expert:**
> **Streaming Replication:**
>
> **On Primary:**
> ```ini
> wal_level = replica
> max_wal_senders = 3
> wal_keep_size = 1GB
> ```
>
> ```sql
> CREATE USER repl REPLICATION LOGIN PASSWORD 'password';
> ```
>
> **pg_hba.conf:**
> ```
> host replication repl 10.0.0.0/8 scram-sha-256
> ```
>
> **On Replica:**
> ```bash
> pg_basebackup -h primary -U repl -D /var/lib/postgresql/15/main -P -Xs
> ```
>
> **recovery.conf:**
> ```
> standby_mode = on
> primary_conninfo = 'host=primary port=5432 user=repl password=password'
> ```

## 9.5 Backup and Recovery

**User:** "How do I backup and restore PostgreSQL?"

**Expert:**
> **Backup:**
>
> ```bash
> # Logical backup
> pg_dump -U postgres mydb > backup.sql
>
> # All databases
> pg_dumpall -U postgres > full_backup.sql
>
> # Custom format (parallel)
> pg_dump -U postgres -Fd mydb -j 4 -f backup_dir
>
> # Binary backup
> pg_basebackup -h localhost -U repl -D /backup -Ft -z -P
> ```
>
> **Restore:**
> ```bash
> psql -U postgres mydb < backup.sql
>
> # Restore custom format
> pg_restore -U postgres -d mydb --jobs=4 backup_dir
>
> # Restore full backup
> pg_restore -U postgres -d postgres full_backup.sql
>
> # Point in time recovery
> pg_restore -d mydb --target-time="2024-01-15 10:00:00" backup.dump
> ```

## 9.6 Performance Optimization

**User:** "How do I optimize PostgreSQL performance?"

**Expert:**
> **Key Optimization Areas:**
>
> 1. **Index Strategy**
> ```sql
> -- B-tree for equality/range
> CREATE INDEX idx_customer ON orders(customer_id);
>
> -- Partial index
> CREATE INDEX idx_active ON users(last_login)
> WHERE deleted_at IS NULL;
>
> -- Expression index
> CREATE INDEX idx_email_lower ON users(LOWER(email));
>
> -- GIN for JSONB
> CREATE INDEX idx_payload ON events USING GIN(payload);
> ```
>
> 2. **Query Optimization**
> ```sql
> EXPLAIN (ANALYZE, BUFFERS, TIMING)
> SELECT * FROM orders WHERE status = 'pending';
>
> -- Use LIMIT early
> SELECT * FROM (
>     SELECT * FROM large_table ORDER BY score DESC LIMIT 1000
> ) ORDER BY score DESC LIMIT 10;
> ```
>
> 3. **Configuration Tuning**
> ```ini
> shared_buffers = 4GB
> work_mem = 64MB
> effective_cache_size = 12GB
> max_connections = 200
> ```

## 9.7 Security Hardening

**User:** "How do I secure PostgreSQL?"

**Expert:**
> **Security Checklist:**
>
> 1. **Configure pg_hba.conf**
> ```
> local   all             postgres                                peer
> local   all             all                                     scram-sha-256
> host    all             all             127.0.0.1/32            scram-sha-256
> host    all             all             ::1/128                 scram-sha-256
> ```
>
> 2. **Set password encryption**
> ```ini
> password_encryption = scram-sha-256
> ```
>
> 3. **Create read-only user**
> ```sql
> CREATE USER readonly WITH PASSWORD 'password';
> GRANT CONNECT ON DATABASE mydb TO readonly;
> GRANT USAGE ON SCHEMA public TO readonly;
> GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
> ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO readonly;
> ```
>
> 4. **Enable SSL**
> ```ini
> ssl = on
> ssl_cert_file = '/etc/ssl/certs/ssl-cert-snakeoil.pem'
> ssl_key_file = '/etc/ssl/private/ssl-cert-snakeoil.key'
> ```

## 9.8 High Availability

**User:** "How do I set up PostgreSQL HA?"

**Expert:**
> **Options:**
>
> 1. **Streaming Replication** (primary + replicas)
> 2. **pgBouncer** (connection pooling)
> 3. **Patroni** (automatic failover)
> 4. **Citus** (horizontal scaling)
> 5. **Pgpool-II** (load balancing + HA)
>
> **Patroni Setup:**
> ```yaml
> # patroni.yml
> scope: mycluster
> name: node1
>
> restapi:
>   listen: 8008
>   connect_address: node1:8008
>
> etcd:
>   hosts: etcd1:2379,etcd2:2379,etcd3:2379
>
> postgresql:
>   data_dir: /data/postgresql
>   parameters:
>     max_connections: 200
>     shared_buffers: 4GB
> ```

## 9.9 Extensions

**User:** "What PostgreSQL extensions should I use?"

**Expert:**
> **Essential Extensions:**
>
> 1. **pg_stat_statements** - Query performance analysis
> 2. **pg_trgm** - Trigram similarity for text search
> 3. **uuid-ossp** - UUID generation
> 4. **postgis** - Geospatial data
> 5. **pgvector** - Vector embeddings for ML
> 6. **hstore** - Key-value store
> 7. **pgcrypto** - Encryption functions
>
> ```sql
> CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
> CREATE EXTENSION IF NOT EXISTS pg_trgm;
> CREATE EXTENSION IF NOT EXISTS uuid-ossp;
> CREATE EXTENSION IF NOT EXISTS vector;
> ```
