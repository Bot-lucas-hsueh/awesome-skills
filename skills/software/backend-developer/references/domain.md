## § 6 · Domain Knowledge

### 6.1 REST API Best Practices

| Aspect | Best Practice | Example |
|--------|---------------|---------|
| **Resources** | Nouns, plural | `/users`, `/orders` |
| **Actions** | HTTP methods | `GET`, `POST`, `PUT`, `DELETE` |
| **Status Codes** | Appropriate codes | `200`, `201`, `400`, `404`, `500` |
| **Versioning** | URL or header | `/v1/users` |
| **Pagination** | Cursor or offset | `?cursor=xyz&limit=20` |
| **Filtering** | Query parameters | `?status=active&sort=-created` |

### 6.2 Database Index Strategy

| Query Pattern | Index Type | Example |
|---------------|------------|---------|
| Exact match | B-tree | `WHERE id = 1` |
| Range queries | B-tree | `WHERE created_at > '2024-01-01'` |
| Text search | GIN/GiST | `WHERE content @@ 'search'` |
| Full-text | Full-text index | `to_tsvector(content)` |
| Composite | Multi-column | `INDEX(a, b, c)` |

### 6.3 Microservices Patterns

| Pattern | Use Case | Implementation |
|---------|----------|----------------|
| **API Gateway** | Single entry point | Kong, Ambassador |
| **Circuit Breaker** | Fail fast on errors | Resilience4j, Polly |
| **Saga** | Distributed transactions | Orchestration/choreography |
| **CQRS** | Read/write optimization | Separate models |
| **Event Sourcing** | Audit trail | Event store |

---
