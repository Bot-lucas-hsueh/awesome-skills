## § 6 · Domain Knowledge

### 6.1 Frontend Performance Targets

| Metric | Target | Measurement |
|--------|--------|-------------|
| **LCP** (Largest Contentful Paint) | < 2.5s | Real user monitoring |
| **FID** (First Input Delay) | < 100ms | Real user monitoring |
| **CLS** (Cumulative Layout Shift) | < 0.1 | Real user monitoring |
| **TTFB** (Time to First Byte) | < 600ms | Server response time |
| **Bundle Size** | < 200KB initial | gzip compressed |

### 6.2 API Design Standards

| Aspect | REST | GraphQL |
|--------|------|---------|
| **Best For** | CRUD operations | Complex queries, mobile |
| **Caching** | HTTP caching | Application-level |
| **Versioning** | URL or header | Schema evolution |
| **Documentation** | OpenAPI | Introspection |
| **Type Safety** | Codegen from OpenAPI | Generated from schema |

### 6.3 Database Optimization Checklist

- [ ] Indexes on foreign keys and query columns
- [ ] Query execution time < 100ms (p95)
- [ ] Connection pooling configured
- [ ] N+1 queries eliminated (DataLoader)
- [ ] Soft deletes implemented
- [ ] Audit columns (created_at, updated_at)
- [ ] Migration rollback tested

---
