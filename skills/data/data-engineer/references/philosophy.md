## § 4 · Core Philosophy

1. **Idempotency is the Foundation** — Every pipeline should be re-runnable with the same result. Design for replay from the start.
2. **Fail Fast, Recover Gracefully** — Detect failures at ingestion; don't let bad data poison downstream systems. Circuit breakers and DLQ (dead letter queues) are mandatory.
3. **Make Data Quality Explicit** — Data contracts, dbt tests, and Great Expectations checks are not optional extras — they are part of the pipeline.
4. **Cost is an Engineering Problem** — A query that costs $500/run is a bug. Partition pruning, materialization strategy, and compression are performance optimizations.
5. **Schema-on-Read Has Limits** — Data lakes without schemas become data swamps. Impose structure at the earliest practical point.
6. **Observability Enables Trust** — Stakeholders trust pipelines they can see. SLA dashboards, data freshness indicators, and quality dashboards build trust.

---

