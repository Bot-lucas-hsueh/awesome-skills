## § 9 · Common Pitfalls

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Small Files Problem** | Slow queries, high overhead | File compaction, optimal sizing |
| **Full Table Scans** | Expensive, slow | Partitioning, clustering, indexes |
| **No Data Quality Checks** | Garbage in, garbage out | Validation at ingestion |
| **Tight Coupling** | Schema changes break everything | Schema registry, contracts |
| **Ignoring Late Data** | Incomplete aggregations | Watermarks, allowed lateness |
| **No Cost Monitoring** | Surprise bills | Budgets, alerts, optimization |

---
