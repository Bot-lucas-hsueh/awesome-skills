# Standards & Reference

## 7.1 Official Documentation

- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/)
- [SQL Reference](https://www.postgresql.org/docs/current/sql.html)
- [Server Administration](https://www.postgresql.org/docs/current/admin.html)
- [Performance Tips](https://www.postgresql.org/docs/current/performance-tips.html)
- [High Availability](https://www.postgresql.org/docs/current/high-availability.html)
- [Postgres Full Text Search](https://www.postgresql.org/docs/current/textsearch.html)
- [PostgreSQL Extensions](https://www.postgresql.org/docs/current/contrib.html)
- [pgvector Documentation](https://github.com/pgvector/pgvector)
- [PostGIS Documentation](https://postgis.net/documentation/)

## 7.2 Configuration Reference

### postgresql.conf

```ini
# Memory
shared_buffers = 4GB
work_mem = 64MB
maintenance_work_mem = 512MB
effective_cache_size = 12GB

# Write Performance
wal_buffers = 64MB
checkpoint_completion_target = 0.9
max_wal_size = 2GB
min_wal_size = 1GB

# Parallelism
max_worker_processes = 8
max_parallel_workers_per_gather = 4
max_parallel_workers = 8

# Connection
max_connections = 200
password_encryption = scram-sha-256

# Logging
log_destination = 'stderr'
logging_collector = on
log_directory = 'log'
log_filename = 'postgresql-%Y-%m-%d.log'
log_statement = 'none'
log_min_duration_statement = 1000

# Autovacuum
autovacuum_max_workers = 4
autovacuum_naptime = 1min
```

### pg_hba.conf

```ini
# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   all             postgres                                peer
local   all             all                                     scram-sha-256
host    all             all             127.0.0.1/32            scram-sha-256
host    all             all             ::1/128                 scram-sha-256
host    replication     repl_user       10.0.0.0/8              scram-sha-256
host    all             app_user        10.0.0.0/8              scram-sha-256
```

## 7.3 Common Commands

### Vacuum and Analyze

```sql
-- Vacuum (reclaim space)
VACUUM;
VACUUM (VERBOSE, ANALYZE) tablename;

-- Full vacuum (requires exclusive lock)
VACUUM FULL tablename;

-- Cluster table (reorder by index)
CLUSTER tablename USING idx_tablename;
```

### EXPLAIN Analysis

```sql
-- Basic explain
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';

-- With timing
EXPLAIN (ANALYZE, BUFFERS, TIMING) SELECT * FROM users;

-- Format options
EXPLAIN (FORMAT JSON) SELECT * FROM users;
EXPLAIN (FORMAT YAML) SELECT * FROM users;
```

### Extensions

```sql
-- Enable extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";        -- trigram search
CREATE EXTENSION IF NOT EXISTS "pg_stat_statements";
CREATE EXTENSION IF NOT EXISTS "postgis";
CREATE EXTENSION IF NOT EXISTS "vector";          -- pgvector
```

## 7.4 Version Compatibility

| Version | Status | EOL | Key Features |
|---------|--------|-----|--------------|
| 17 | Current | 2029 | Bloom filters, parallel query improvements |
| 16 | Current | 2028 | Logical replication improvements, SQL/JSON |
| 15 | Maintenance | 2027 | MERGE, unlogged tables replication |
| 14 | Maintenance | 2026 | LZ4 compression, parallel query improvements |
| 13 | Security only | 2025 | B-tree dedup, incremental sort |

### psql Commands

```bash
psql -U username -d database -h hostname -p 5432
psql -c "SELECT * FROM table"        # single command
psql -f script.sql                   # execute file
psql -X -c "\d+ tablename"          # disable readline

# Meta commands
\d          -- list tables
\d+         -- table details
\di         -- indexes
\df         -- functions
\dv         -- views
\du         -- users
\l          -- databases
\x          -- expanded display
\copy       -- copy data
\watch      -- repeat query
```
