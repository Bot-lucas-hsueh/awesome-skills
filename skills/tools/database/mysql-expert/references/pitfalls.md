# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern| Severity| Quick Fix|
|---|----------------------|-----------------|---------------------|
| 1 | **Using SELECT * in production** | 🔴 High | Specify only needed columns |
| 2 | **Missing indexes on foreign keys** | 🔴 High | Add indexes for JOIN performance |
| 3 | **No connection pooling** | 🔴 High | Use HikariCP or similar |
| 4 | **Long-running transactions** | 🔴 High | Keep transactions short |
| 5 | **Not using prepared statements** | 🟡 Medium | Use prepared statements for security |
| 6 | **Ignoring NULL handling** | 🟡 Medium | Use COALESCE/IFNULL |
| 7 | **Using MyISAM for transactional data** | 🔴 High | Use InnoDB |
| 8 | **No backup strategy** | 🔴 High | Implement regular backups |
| 9 | **Wrong data types** | 🟡 Medium | Use appropriate types (VARCHAR vs TEXT) |
| 10 | **Not analyzing tables** | 🟡 Medium | Run ANALYZE TABLE regularly |

## 10.2 Query Anti-Patterns

| # | Anti-Pattern| Impact| Solution|
|---|-------------|-------|----------|
| 1 | SELECT * | Full table scans | Specify columns |
| 2 | No WHERE clause | Full table scan | Always filter |
| 3 | Functions on indexed columns | Index not used | Use indexed column directly |
| 4 | OR in JOIN conditions | Poor performance | Use UNION or IN |
| 5 | Nested subqueries | Multiple scans | Use JOIN instead |

### N+1 Query Problem

```sql
-- BAD: Query inside loop
SELECT * FROM orders WHERE customer_id = ?;
-- Executed for each customer

-- GOOD: Single query with JOIN
SELECT o.*, c.name 
FROM orders o
JOIN customers c ON o.customer_id = c.id;
```

### Avoiding Full Table Scans

```sql
-- BAD: No index, full scan
SELECT * FROM users WHERE age > 18;

-- GOOD: With index
CREATE INDEX idx_users_age ON users(age);
SELECT * FROM users WHERE age > 18;

-- GOOD: Covering index
CREATE INDEX idx_users_age_name ON users(age, name);
SELECT name FROM users WHERE age > 18;
```

## 10.3 Schema Anti-Patterns

| # | Anti-Pattern| Fix|
|---|-------------|-----|
| 1 | Storing JSON in TEXT | Use JSON type (MySQL 5.7+) |
| 2 | No primary key | Always add AUTO_INCREMENT primary key |
| 3 | Using VARCHAR(255) for everything | Right-size based on data |
| 4 | No foreign key constraints | Use foreign keys for integrity |
| 5 | Storing dates as strings | Use DATE/DATETIME types |

### Denormalization Mistakes

```sql
-- BAD: Storing comma-separated values
-- users: "1,2,3"

-- GOOD: Normalized approach
CREATE TABLE user_roles (
    user_id INT,
    role_id INT,
    PRIMARY KEY (user_id, role_id)
);
```

## 10.4 Configuration Anti-Patterns

| # | Anti-Pattern| Fix|
|---|-------------|-----|
| 1 | Default max_connections too high | Tune based on memory |
| 2 | No query cache understanding | Note: removed in 8.0 |
| 3 | InnoDB buffer pool too small | Set to 70-80% RAM |
| 4 | No slow query log | Enable and monitor |
| 5 | Using query cache in 8.0+ | Removed - remove config |

## 10.5 Security Anti-Patterns

| # | Anti-Pattern| Fix|
|---|-------------|-----|
| 1 | Root access without password | Set root password |
| 2 | User with % wildcard host | Use specific hosts |
| 3 | No SSL for connections | Enable require_secure_transport |
| 4 | Granting ALL PRIVILEGES | Grant specific privileges |
| 5 | No firewall on MySQL port | Restrict port 3306 |

## 10.6 Best Practices

1. **Always use InnoDB** for transactional tables
2. **Use UTF8MB4** for proper Unicode support
3. **Set appropriate data types** - not everything is VARCHAR(255)
4. **Index strategically** - on WHERE, JOIN, ORDER BY columns
5. **Use connection pooling** - HikariCP recommended
6. **Monitor slow queries** - enable slow_query_log
7. **Backup regularly** - test restore procedures
8. **Use prepared statements** - prevent SQL injection
9. **Set appropriate TTLs** - for query cache (pre-8.0)
10. **Use EXPLAIN** - analyze query plans

## 10.7 Performance Checklist

- [ ] InnoDB buffer pool configured (70-80% RAM)
- [ ] Appropriate max_connections
- [ ] Slow query log enabled
- [ ] Indexes on foreign keys
- [ ] Connection pooling configured
- [ ] Query cache tuned or disabled (8.0+)
- [ ] Binary logging enabled for replication
- [ ] Regular ANALYZE TABLE runs
- [ ] Table partitions for large tables
- [ ] Read/Write splitting implemented if needed
