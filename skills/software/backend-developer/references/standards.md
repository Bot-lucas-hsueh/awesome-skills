## 7. Standards & Reference

### 7.1 API Design Frameworks

| Framework / 框架 | When to Use / 使用场景 | Key Steps
|-----------------|----------------------|-------------------|
| **REST + OpenAPI** | Public APIs, multi-client (web/mobile/partner) | 1. Define resources (nouns) → 2. Map HTTP verbs → 3. Design error schema → 4. Add pagination + versioning |
| **GraphQL + DataLoader** | Frontend-driven flexible queries; multiple data sources aggregated | 1. Schema-first (SDL) → 2. Resolvers per field → 3. DataLoader batching → 4. Query complexity limits |
| **gRPC + Protobuf** | Internal service-to-service; latency-sensitive; streaming | 1. .proto contract → 2. Generate stubs → 3. Implement server → 4. Add interceptors for auth/tracing |
| **Event-Driven (Kafka)** | Async decoupled processing; audit logs; event sourcing | 1. Define events (nouns, past tense) → 2. Schema registry → 3. Consumer groups → 4. Dead letter queue |

### 7.2 Database Metrics

| Metric / 指标 | Formula / 公式 | Target
|--------------|--------------|---------------|
| **OLTP Query Latency** | p99 of SELECT/INSERT/UPDATE | p99 < 100ms |
| **Connection Pool Utilization** | Active connections
| **Slow Query Rate** | Queries >500ms
| **Cache Hit Rate** | Redis hits
| **Replication Lag** | Replica WAL position vs. Primary | < 1s for read replicas |
| **Index Coverage** | Queries using index

### 7.3 Database Selection Guide

| Use Case / 使用场景 | Recommended / 推荐 | Reason / 原因 | Avoid When
|--------------------|-------------------|--------------|---------------------|
| Transactional data | PostgreSQL | ACID, complex joins, JSONB, extensions | Massive write throughput >500k/s |
| User sessions | Redis | Sub-millisecond, TTL native, atomic ops | Persistence required (use Redis AOF) |
| Event log
| Product catalog | MongoDB | Flexible schema, nested docs, Atlas Search | Complex multi-document transactions |
| Full-text search | Elasticsearch | Full-text, fuzzy, faceting, geo queries | Primary data store (use as read replica) |
| Time-series metrics | InfluxDB, TimescaleDB | Time-ordered inserts, downsampling | Complex relational queries |

---

