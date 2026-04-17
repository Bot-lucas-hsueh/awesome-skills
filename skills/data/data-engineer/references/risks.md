## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| Data Loss on Pipeline Failure | 🔴 Critical | Non-idempotent pipelines can lose or duplicate records on retry | Implement exactly-once or at-least-once with deduplication |
| Schema Breaking Changes | 🟡 High | Upstream schema change breaks downstream pipelines without warning | Schema registry (Confluent/Glue); contract testing |
| Cost Explosion | 🟡 High | Full table scans on petabyte tables → $10K+ query costs | Partition pruning; clustering; query cost alerts |
| PII Data Exposure | 🟡 High | Sensitive data in data lake without access control = breach risk | Column-level encryption; row-level security; data masking in dev |
| Vendor Lock-in | 🟢 Medium | Platform-specific features reduce portability | Use open formats (Parquet/Delta); abstract platform-specific code |

---
