## § 8 · Standard Workflow

### Phase 1: Pipeline Design

| Step | Activity | Done Criteria | Fail Criteria |
|------|----------|---------------|---------------|
| 1 | Requirements gathering | Source, destination, SLA, volume, freshness, access needs documented | "Build a pipeline for X" without specifics |
| 2 | Architecture decision | Batch vs. streaming decision documented with rationale | Default to streaming without evaluating if batch sufficient |
| 3 | Data modeling | Dimensional or Data Vault model designed; grain defined | Build before modeling; retrofit schema later |
| 4 | Quality contract | dbt tests + Great Expectations rules for key assertions | No data quality checks defined |
| 5 | Cost estimate | Estimated compute and storage cost per run | Build without cost projection |

### Phase 2: Implementation & Production

| Step | Activity | Done Criteria | Fail Criteria |
|------|----------|---------------|---------------|
| 1 | Idempotency verified | Pipeline can be run twice; produces same result (no duplicates) | Assume pipelines won't fail |
| 2 | Error handling | Dead letter queue or error table for bad records | Silent failures; bad records dropped |
| 3 | Monitoring + alerting | SLA alert if pipeline misses window; data quality alert on test failure | No monitoring; discover failures from analyst complaints |
| 4 | Backfill tested | Historical backfill run without duplication | "We'll figure out backfill when needed" |
| 5 | Documentation | README with: source → destination, schedule, owner, runbook | Undocumented pipeline = future incident |

---

