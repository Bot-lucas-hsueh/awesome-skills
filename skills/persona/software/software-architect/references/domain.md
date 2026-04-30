## § 6 · Domain Knowledge

### 6.1 Architectural Pattern Decision Matrix

| Pattern | Team Size | Traffic Threshold | When to Choose | Cost |
|---------|-----------|-------------------|----------------|------|
| **Monolith** | 1-10 | < 1K req/s | New product, unknown domain, fast iteration | Low |
| **Modular Monolith** | 5-25 | < 5K req/s | Known bounded contexts, deployment simplicity | Low-Med |
| **Microservices** | 20+ | > 1K req/s with independent scaling | Multiple autonomous teams, different scaling needs | High |
| **Event-Driven** | Any | Variable, spike-tolerant | Audit requirements, loose coupling | Medium |
| **CQRS** | 10+ | Read:Write > 10:1 | Separate read/write scaling, complex projections | Med-High |
| **Serverless** | Any | Variable, intermittent | Cost optimization, rapid scaling, event triggers | Variable |

### 6.2 CAP Theorem Reference

| Property | Behavior | Examples |
|----------|----------|----------|
| **CP** | Consistency over availability on partition | PostgreSQL sync, etcd, ZooKeeper |
| **AP** | Availability over consistency on partition | Cassandra, DynamoDB, Couchbase |
| **PACELC** | Normal: Latency vs. Consistency; Partition: A vs. C | Design choice documentation required |

### 6.3 Quality Attributes Tactics

| Attribute | Tactics | Metrics |
|-----------|---------|---------|
| **Availability** | Redundancy (N+1), health checks, circuit breakers | 99.9% / 99.99% / 99.999% |
| **Scalability** | Stateless services, horizontal sharding, read replicas | Linear cost scaling with load |
| **Performance** | Caching, CDN, async processing, connection pooling | p50/p95/p99 latency |
| **Security** | Zero trust, mTLS, encryption, RBAC | Security audit score |
| **Maintainability** | Clear bounded contexts, ADRs, contract tests | Deployment frequency, MTTR |

📄 **Deep Dives**: [references/domain-knowledge.md](references/domain-knowledge.md)

---
