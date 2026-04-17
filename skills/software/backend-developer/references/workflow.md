## 8. Standard Workflow

### 8.1 API Feature Development

```
Phase 1: Contract Design (Day 1)
├── Identify consumers: internal service / web / mobile
├── Define resource model: nouns, relationships, access patterns
├── Write OpenAPI spec (YAML) including: request schema, response schema, error codes
├── Define SLO: p99 latency target + availability target
└── [✓ Done]: OpenAPI spec reviewed and approved by consumer team + tech lead
    [✗ FAIL]: Misaligned on response schema → iterate on spec before any code

Phase 2: Implementation (Day 2-4)
├── Scaffold 3-layer architecture: Route handler → Service → Repository
├── Add schema validation middleware (Zod/Pydantic) at route layer
├── Implement business logic in Service layer (no DB access directly)
├── Repository layer: parameterized queries only (never string interpolation)
├── Add structured logging: request_id, user_id, latency_ms on every response
└── [✓ Done]: Unit tests for Service layer + integration test for Repository
    [✗ FAIL]: Missing input validation → STOP, add Zod schema before proceeding

Phase 3: Hardening & Deployment (Day 5)
├── Load test with k6/Locust at 2× expected peak RPS
├── Add rate limiting at API gateway (per-user and per-IP)
├── Verify EXPLAIN ANALYZE on all new queries: no Seq Scans in hot paths
├── Add circuit breaker for any new downstream service calls
└── [✓ Done]: p99 within SLO at 2× peak; zero Seq Scans; rollback tested
    [✗ FAIL]: p99 >2× SLO → profile with APM, add index, re-test before release
```

### 8.2 Database Performance Optimization

```
Step 1: Diagnose
  → Run EXPLAIN (ANALYZE, BUFFERS) on slow queries
  → Identify: Seq Scan, Hash Join without index, high rows_removed
  → Check connection pool metrics: active vs. idle vs. waiting

Step 2: Identify Root Cause
  → Seq Scan → Missing index on WHERE/JOIN/ORDER BY columns
  → N+1 Query → ORM lazy loading → Add .include() or batch with DataLoader
  → Lock contention → Long transactions holding row locks → Reduce tx scope
  → OFFSET pagination → Full table scan → Switch to cursor-based pagination

Step 3: Apply & Verify
  → CREATE INDEX CONCURRENTLY (non-blocking in production)
  → Re-run EXPLAIN ANALYZE: confirm Index Scan replaces Seq Scan
  → Monitor p99 latency for 24h post-change

[✓ Done]: p99 < 100ms; no Seq Scans in hot paths; connection pool < 80%
```

---

