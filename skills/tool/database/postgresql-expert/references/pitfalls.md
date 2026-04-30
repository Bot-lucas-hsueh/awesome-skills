# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern| Severity| Quick Fix|
|---|----------------------|-----------------|---------------------|
| 1 | **Missing indexes on WHERE columns** | 🔴 High | Add indexes for filter columns |
| 2 | **Using SELECT *** | 🔴 High | Select only needed columns |
| 3 | **No connection pooling** | 🔴 High | Use pgBouncer |
| 4 | **Long-running transactions** | 🔴 High | Keep transactions short |
| 5 | **Ignoring VACUUM** | 🟡 Medium | Configure autovacuum properly |
| 6 | **No pagination** | 🟡 Medium | Use LIMIT/OFFSET or cursor |
| 7 | **Ignoring NULL handling** | 🟡 Medium | Use COALESCE/IFNULL |
| 8 | **Copy-on-write too large** | 🟡 Medium | Increase shared_buffers |
| 9 | **No partition strategy** | 🟡 Medium | Consider partitioning large tables |
| 10 | **Ignoring plan caching** | 🟡 Medium | Use prepared statements |

## 10.2 Query Anti-Patterns

| # | Anti-Pattern| Impact| Solution|
|---|-------------|-------|----------|
| 1 | SELECT * | Full scans | Specify columns |
| 2 | No WHERE clause | Full table scan | Always filter |
| 3 | Function on indexed column | Index not used | Use expression index |
| 4 | OR in WHERE | Poor performance | Use IN or UNION |
| 5 | Nested subqueries in loops | N+1 problem | Use JOIN |

### N+1 Query Problem

```sql
-- BAD: Query per user
-- Run: SELECT * FROM orders WHERE user_id = ?

-- GOOD: Single query
SELECT o.*, u.name
FROM orders o
JOIN users u ON o.user_id = u.id;
```

### Index Not Used

```sql
-- BAD: Function on column
SELECT * FROM users WHERE LOWER(email) = 'test@example.com';

-- GOOD: Expression index
CREATE INDEX idx_users_email_lower ON users(LOWER(email));
SELECT * FROM users WHERE LOWER(email) = 'test@example.com';

-- BAD: Type conversion
SELECT * FROM orders WHERE order_id = '123';

-- GOOD: Match types
SELECT * FROM orders WHERE order_id = 123;
```

## 10.3 Schema Anti-Patterns

| # | Anti-Pattern| Fix|
|---|-------------|-----|
| 1 | Over-normalized schema | Denormalize for read performance |
| 2 | Storing JSON without indexing | Use GIN index on JSONB |
| 3 | No primary key | Always use PRIMARY KEY |
| 4 | Using TEXT for short strings | Right-size VARCHAR |
| 5 | No foreign key constraints | Use FK for integrity |

### JSON Storage

```sql
-- BAD: Stored as TEXT, can't query efficiently
CREATE TABLE events (
    data TEXT
);

-- GOOD: Use JSONB with GIN index
CREATE TABLE events (
    data JSONB
);
CREATE INDEX idx_events_data ON events USING GIN(data);
```

## 10.4 Configuration Anti-Patterns

| # | Anti-Pattern| Fix|
|---|-------------|-----|
| 1 | shared_buffers too small | Set to 25% of RAM |
| 2 | work_mem too small | Increase for complex sorts |
| 3 | max_connections too high | Use connection pooling |
| 4 | No autovacuum | Tune autovacuum parameters |
| 5 | wal_level minimal | Set for replication needs |

## 10.5 Security Anti-Patterns

| # | Anti-Pattern| Fix|
|---|-------------|-----|
| 1 | Trust authentication locally | Use scram-sha-256 |
| 2 | No SSL connections | Enable TLS |
| 3 | Superuser for apps | Create app-specific users |
| 4 | Wildcard in pg_hba.conf | Restrict to specific networks |
| 5 | No password policy | Enforce strong passwords |

## 10.6 Performance Checklist

- [ ] shared_buffers = 25% RAM
- [ ] effective_cache_size set appropriately
- [ ]Indexes on WHERE/JOIN columns
- [ ] Connection pooling (pgBouncer)
- [ ] Slow query log enabled
- [ ] pg_stat_statements active
- [ ] Autovacuum running
- [ ] WAL configured for durability needs
- [ ] Appropriate max_connections
- [ ] Query plans reviewed with EXPLAIN ANALYZE
