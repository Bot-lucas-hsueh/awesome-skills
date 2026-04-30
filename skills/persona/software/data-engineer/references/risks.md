## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Data Loss** | 🔴 Critical | Pipeline failure loses data | Exactly-once semantics, dead letter queues |
| **Schema Drift** | 🔴 Critical | Source changes break downstream | Schema registry, validation gates |
| **Pipeline Failures** | 🟠 High | Silent failures, stale data | Monitoring, alerting, SLAs |
| **Cost Overruns** | 🟠 High | Unoptimized queries burn budget | Query optimization, autoscaling limits |
| **Data Quality Issues** | 🟠 High | Bad data poisons analytics | Quality checks, anomaly detection |
| **PII Exposure** | 🟡 Medium | Unmasked sensitive data | Automated detection, masking policies |

---
