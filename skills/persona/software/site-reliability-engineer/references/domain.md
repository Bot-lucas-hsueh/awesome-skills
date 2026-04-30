## § 6 · Domain Knowledge

### 6.1 SLI/SLO/SLA Definitions

| Term | Definition | Example |
|------|------------|---------|
| **SLI** | Service Level Indicator | Request latency, error rate |
| **SLO** | Service Level Objective | 99.9% availability |
| **SLA** | Service Level Agreement | Contractual obligation |
| **Error Budget** | 100% - SLO | 0.1% = 43min/month downtime |

### 6.2 RED Method (Services)

| Metric | Description | Example |
|--------|-------------|---------|
| **Rate** | Requests per second | 1000 req/s |
| **Errors** | Error rate | 0.1% 5xx errors |
| **Duration** | Response time | p99 < 200ms |

### 6.3 USE Method (Resources)

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| **Utilization** | Resource busy time | CPU > 80% |
| **Saturation** | Queue length / backlog | Disk queue > 10 |
| **Errors** | Error count | Disk errors > 0 |

---
