## 3. Risk Disclaimer

⚠️ **CRITICAL LIMITATIONS**

| Risk | Severity | Mitigation | Escalation |
|------|----------|------------|------------|
| **DBU Cost Explosion** | 🔴 High | Enable autoscaling with bounds; set budget alerts | Cost >$10K/day without approval |
| **Small Files Problem** | 🔴 High | Schedule OPTIMIZE/VACUUM; use Auto Loader | Query performance degradation >50% |
| **Concurrent Write Conflicts** | 🔴 High | Use optimistic concurrency; implement retry logic | Data corruption in production |
| **Vector Search Sync Lag** | 🔴 High | Monitor index freshness; enable continuous sync | RAG responses with stale data |
| **Model Serving Latency** | 🟡 Medium | Use provisioned throughput; enable route optimization | p99 latency >500ms |
| **Schema Drift** | 🟡 Medium | Enable schema enforcement; use schema evolution | Pipeline failures on upstream changes |
| **Over-Partitioning** | 🟡 Medium | Target 1GB+ per partition; avoid high-cardinality columns | Excessive metadata overhead |

---
