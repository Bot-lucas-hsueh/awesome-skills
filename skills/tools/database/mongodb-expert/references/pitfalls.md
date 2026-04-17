# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern| Severity| Quick Fix|
|---|----------------------|-----------------|---------------------|
| 1 | **No index on query fields** | 🔴 High | Create indexes for WHERE/JOIN |
| 2 | **Using deprecated mongo shell** | 🟡 Medium | Use mongosh |
| 3 | **Large document without limit** | 🟡 Medium | Always use .limit() |
| 4 | **Not using projections** | 🟡 Medium | Select only needed fields |
| 5 | **Storing arrays that grow unbounded** | 🟡 Medium | Use separate collection |
| 6 | **No connection pooling** | 🟡 Medium | Use driver connection pool |
| 7 | **Ignoring write concern** | 🟡 Medium | Set appropriate w: |
| 8 | **Using findOne when find is enough** | 🟡 Medium | Use find() with limit |
| 9 | **Not using partial indexes** | 🟡 Medium | Filter index to needed docs |
| 10 | **Running on localhost only** | 🟡 Medium | Configure for production |

## 10.2 Query Anti-Patterns

| # | Anti-Pattern| Impact| Solution|
|---|-------------|-------|----------|
| 1 | No index on filter | Full collection scan | Add index |
| 2 | $where with slow JS | Performance | Use native operators |
| 3 | OR on different fields | No index use | Use $in |
| 4 | Unbounded result set | Memory issues | Use .limit() |
| 5 | Not using covered query | Extra lookups | Include all fields in index |

### Missing Index Example

```javascript
// BAD: Collection scan
db.orders.find({ status: "pending", customer_id: 123 });

// GOOD: With index
db.orders.createIndex({ status: 1, customer_id: 1 });
db.orders.find({ status: "pending", customer_id: 123 });
```

### $where Performance

```javascript
// BAD: $where with JavaScript
db.collection.find({ $where: function() { return this.field > 10; } });

// GOOD: Native operators
db.collection.find({ field: { $gt: 10 } });
```

## 10.3 Schema Anti-Patterns

| # | Anti-Pattern| Fix|
|---|-------------|-----|
| 1 | Embedding unbounded arrays | Reference pattern |
| 2 | Over-normalizing (too many collections) | Embed related data |
| 3 | Not using flexible schemas | Use schema validation |
| 4 | Storing binary in documents | Use GridFS |
| 5 | No schema design for access patterns | Denormalize for reads |

### Unbounded Arrays

```javascript
// BAD: Array grows without limit
{
  user: "user1",
  orders: [1, 2, 3, ...]  // Grows infinitely
}

// GOOD: Reference pattern
// orders collection with user_id field
// users collection with basic info only
```

## 10.4 Configuration Anti-Patterns

| # | Anti-Pattern| Fix|
|---|-------------|-----|
| 1 | Default port without auth | Enable authentication |
| 2 | No WiredTiger cache config | Set cacheSizeGB |
| 3 | No journaling | Ensure journal enabled |
| 4 | Using small oplog | Size oplog appropriately |
| 5 | No connection pool | Configure pool size |

## 10.5 Security Anti-Patterns

| # | Anti-Pattern| Fix|
|---|-------------|-----|
| 1 | No authentication | Enable auth |
| 2 | No TLS | Enable TLS |
| 3 | Wildcard bind IP | Bind to specific IP |
| 4 | User with all databases | Create scoped users |
| 5 | No role-based access | Use RBAC |

## 10.6 Performance Checklist

- [ ] Indexes on query filter fields
- [ ] Covered queries where possible
- [ ] Connection pooling configured
- [ ] Appropriate write concern
- [ ] Schema validation enabled
- [ ] Connection pool size tuned
- [ ] Slow query logging enabled
- [ ] Atlas or proper monitoring
