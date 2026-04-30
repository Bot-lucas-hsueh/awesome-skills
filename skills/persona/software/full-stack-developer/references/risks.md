## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **N+1 Queries** | 🔴 Critical | Unoptimized ORM queries kill performance | Eager loading, DataLoader pattern, query logging |
| **XSS/SQL Injection** | 🔴 Critical | Unsanitized user input → security breach | Parameterized queries, input validation, CSP |
| **Memory Leaks** | 🟠 High | Unclosed connections, event listeners | Connection pooling, cleanup in useEffect |
| **API Breaking Changes** | 🟠 High | Undocumented changes break clients | Versioning, deprecation periods, OpenAPI |
| **Frontend Bloat** | 🟡 Medium | Large bundles slow initial load | Code splitting, lazy loading, tree shaking |
| **Database Locks** | 🟡 Medium | Long transactions block other queries | Short transactions, optimistic locking |

---
