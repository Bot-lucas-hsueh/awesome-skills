## 7. Standards & Reference

### 7.1 Architectural Pattern Decision Matrix

| Pattern / 模式 | Team Size / 团队规模 | Traffic Threshold / 流量阈值 | When to Choose / 适用场景 | Cost
|--------------|-------------------|---------------------------|------------------------|------------|
| **Monolith** | 1–8 engineers | < 1,000 req/s | New product, unknown domain, fast iteration needed | Low |
| **Modular Monolith** | 5–20 engineers | < 5,000 req/s | Known bounded contexts, single-team org, deployment simplicity valued | Low–Medium |
| **Microservices** | 20+ engineers (≥2 per service) | > 1,000 req/s with independent scaling needs | Multiple autonomous teams, different scaling profiles, independent deploy cadences | High |
| **Event-Driven** | Any | Variable, spike-tolerant | Audit requirements, loose coupling across domains, async processing | Medium |
| **CQRS** | 10+ engineers | Read:Write ratio > 10:1 | Separate read/write scaling, complex projections, event sourcing | Medium–High |

### 7.2 Architecture Quality Attributes

| Quality Attribute / 质量属性 | Tactics / 策略 | Key Metrics / 关键指标 | Trade-offs
|-----------------------------|--------------|----------------------|-----------------|
| **Scalability** | Stateless services, horizontal sharding, read replicas, async processing | Requests/s at p99 SLO, linear cost scaling | Session management complexity, data partitioning overhead |
| **Reliability** | Redundancy (N+1), health checks, circuit breakers, bulkheads | Availability %, MTTR, error budget | Cost (2×–3× infrastructure), operational complexity |
| **Maintainability** | Clear bounded contexts, ADRs, contract tests, module boundaries | Deployment frequency, lead time, change failure rate | Upfront design investment, slower initial delivery |
| **Security** | Zero trust, encryption at rest/transit, RBAC, mTLS | Security audit score, pen test findings | Latency overhead (5–15ms for mTLS), development cost |
| **Performance** | Caching, CDN, async processing, connection pooling, indexing | p50/p95/p99 latency, throughput | Caching consistency lag, increased system complexity |
| **Cost** | Right-sizing, autoscaling, spot instances, data tiering | Monthly infra cost

### 7.3 Architecture Decision Record (ADR) Template

```markdown
# ADR-[number]: [Short Decision Title]

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Deprecated | Superseded by ADR-[N]
**Deciders:** [Names and roles]

## Context
[What is the issue? What forces are at play?
Include: business context, technical constraints, team size, traffic profile, budget.]

## Decision
[What is the architectural change we are making?]

## Options Considered

| Option | Pros | Cons | Estimated Cost |
|--------|------|------|---------------|
| A: ... | ... | ... | ... |
| B: ... | ... | ... | ... |

## Consequences

**Positive:**
- [What becomes easier, faster, cheaper?]

**Negative:**
- [What becomes harder? What technical debt is accepted?]

**Risks:**
- [What could go wrong? How do we detect it? How do we mitigate?]
```

### 7.4 C4 Model Notation

```
Level 1: System Context
  Shows: your system + external users + external systems
  Audience: non-technical stakeholders, product managers

Level 2: Container
  Shows: deployable units (web app, API, database, message queue)
  Audience: developers, architects, ops

Level 3: Component
  Shows: major structural components inside a container
  Audience: developers implementing that container

Level 4: Code
  Shows: classes, functions, relationships
  Audience: developers (auto-generate from code where possible)

Rule: Each level zooms into one element from the level above.
      Never skip levels. Never put Level 3 detail in a Level 1 diagram.
```

### 7.5 CAP Theorem Practical Guide

```
CAP Theorem: In a distributed system, choose 2 of 3:
  C: Consistency (every read gets the most recent write)
  A: Availability (every request gets a response, even if not the latest)
  P: Partition Tolerance (system works even if network partitions occur)

In practice: Network partitions always happen. So you choose C or A under partition.

CP Systems (consistency over availability):
  → Financial transactions, inventory counts, leader election
  → Examples: PostgreSQL (with synchronous replication), ZooKeeper, etcd
  → Behavior on partition: return error rather than stale data

AP Systems (availability over consistency):
  → User sessions, product catalogs, search indexes, caching
  → Examples: Cassandra, DynamoDB, CouchDB
  → Behavior on partition: serve potentially stale data, reconcile later

PACELC (more nuanced for normal operation):
  Under Partition → choose A or C
  Else (normal)   → choose Latency or Consistency
  PostgreSQL: PC/EC (consistent, higher latency)
  DynamoDB:   PA/EL (available, lower latency)
```

### 7.6 SOLID Principles at Architecture Level

| Principle / 原则 | System-Level Meaning / 系统级含义 | Anti-Pattern
|-----------------|--------------------------------|---------------------|
| **Single Responsibility** | Each service owns one bounded context; one team, one domain | User service that also handles billing and notifications |
| **Open/Closed** | New behavior via extension (new service, new event type), not modification of shared components | Changing a shared library for every new feature request |
| **Liskov Substitution** | Service implementations must honor published contracts; behavior must be predictable | Auth service that silently drops permissions on upgrade |
| **Interface Segregation** | Narrow, purpose-specific APIs; clients depend only on what they use | Fat GraphQL schema where mobile clients ignore 80% of fields |
| **Dependency Inversion** | Business logic depends on abstractions (interfaces, events), not concrete infrastructure | Order service directly importing payment SDK instead of using a payment event |

---
