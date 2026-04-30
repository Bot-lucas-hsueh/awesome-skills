# Troubleshooting

## 8.1 Connection Issues

### Connection Refused

```bash
# Check if PostgreSQL is running
pg_isready -h hostname -p 5432

# Check pg_hba.conf allows connection
# Edit and reload
sudo -u postgres psql -c "SELECT pg_reload_conf();"
```

**Common causes:**
- PostgreSQL not running: `sudo systemctl start postgresql`
- Firewall blocking port 5432
- Wrong host in connection string
- Authentication method mismatch

### Too Many Connections

```sql
-- Check current connections
SELECT count(*), state FROM pg_stat_activity GROUP BY state;

-- Kill idle connections
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE state = 'idle' 
AND state_change < NOW() - INTERVAL '10 minutes';

-- Increase connections (postgresql.conf)
ALTER SYSTEM SET max_connections = 300;
SELECT pg_reload_conf();
```

## 8.2 Performance Issues

### Slow Queries

```sql
-- Enable pg_stat_statements
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Find slowest queries
SELECT query, calls, total_exec_time, mean_exec_time, rows
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 20;

-- Find most frequent
SELECT query, calls, total_exec_time
FROM pg_stat_statements
ORDER BY calls DESC
LIMIT 20;
```

### Missing Indexes

```sql
-- Find unused indexes
SELECT schemaname, tablename, indexname, idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
AND indexname NOT LIKE '%pkey'
ORDER BY schemaname, tablename;

-- Find tables with seq scans
SELECT relname, seq_scan, idx_scan
FROM pg_stat_user_tables
WHERE seq_scan > 1000
ORDER BY seq_scan DESC;

-- Create index from query
CREATE INDEX CONCURRENTLY idx_name ON table(column);
```

### Locking Issues

```sql
-- Check blocking
SELECT 
    pid,
    usename,
    pg_blocking_pids(pid) as blocked_by,
    query,
    state,
    wait_event_type,
    wait_event
FROM pg_stat_activity
WHERE cardinality(pg_blocking_pids(pid)) > 0;

-- Find waiting queries
SELECT * FROM pg_stat_activity WHERE wait_event IS NOT NULL;

-- Kill blocking query
SELECT pg_cancel_backend(pid);  -- graceful
SELECT pg_terminate_backend(pid);  -- forceful
```

## 8.3 Replication Issues

### Streaming Replication Lag

```sql
-- On primary
SELECT client_addr, state, sent_lsn, write_lsn, flush_lsn, replay_lsn
FROM pg_stat_replication;

-- Check lag
SELECT 
    client_addr,
    (sent_lsn - replay_lsn) / 1024 / 1024 AS lag_mb
FROM pg_stat_replication;

-- On replica
SELECT now() - pg_last_xact_replay_timestamp() AS replication_lag;
```

### Switchover/Failover

```bash
# Graceful switchover (primary -> replica)
pg_ctl promote -D /var/lib/postgresql/data

# Promote replica manually
su - postgres -c "pg_ctl promote -D /var/lib/postgresql/replica"
```

## 8.4 Storage/Disk Issues

### Table Bloat

```sql
-- Check table size
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS total_size
FROM pg_tables
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Check bloated tables
SELECT 
    schemaname, tablename,
    pg_size_pretty(pg_relation_size(schemaname||'.'||tablename)) AS size,
    n_dead_tup, n_live_tup
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC;
```

### VACUUM Issues

```sql
-- Check vacuum progress
SELECT * FROM pg_stat_progress_vacuum;

-- Cancel stuck vacuum
SELECT pg_cancel_backend(pid);

-- Force aggressive vacuum
VACUUM (VERBOSE, FREEZE, ANALYZE) tablename;
```

## 8.5 Backup/Restore

```bash
# pg_dump
pg_dump -U postgres -Fc database > backup.dump
pg_dump -U postgres -Fd database -f backup_dir

# pg_basebackup
pg_basebackup -h primary -U repl -D /var/lib/postgresql/replica -P -Xs

# Point-in-time recovery
pg_restore -U postgres -d database --jobs=4 backup.dump
pg_restore -U postgres -d database -1 backup.dump  # single transaction
```

## 8.6 Upgrades

```bash
# pg_upgrade
pg_upgrade -b oldbindir -B newbindir -d olddatadir -D newdatadir

# Logical replication upgrade
# Create publication/subscription on new cluster
# Wait for sync, promote new primary
```
