## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **SQL Injection** | 🔴 Critical | Unsanitized user input → data breach | Parameterized queries, ORM |
| **N+1 Queries** | 🔴 Critical | Unoptimized ORM → performance collapse | Eager loading, DataLoader |
| **Data Race** | 🔴 Critical | Concurrent access corrupts data | Transactions, optimistic locking |
| **Memory Leaks** | 🟠 High | Unclosed connections, unbounded caches | Resource cleanup, limits |
| **API Breaking Changes** | 🟠 High | Undocumented changes break clients | Versioning, deprecation |
| **Race Conditions** | 🟡 Medium | Timing-dependent bugs | Proper locking, idempotency |

---
