## § 7 · Standard Workflow

### Phase 1: Requirements & Source Analysis (Days 1-2)

```
├── Identify data sources (databases, APIs, files)
├── Understand data volume, velocity, variety
├── Define SLA requirements (freshness, latency)
├── Document schema and quality expectations
└── [✓ Done]: Source catalog, requirements documented
    [✗ FAIL]: Unknown schema → discover before design
```

### Phase 2: Architecture Design (Days 3-5)

```
├── Choose batch vs streaming vs hybrid
├── Design data lake zones (raw, curated, consumption)
├── Define data models (dimensional, vault)
├── Plan data quality checks and lineage
└── [✓ Done]: Architecture diagram, tech stack chosen
    [✗ FAIL]: Scalability concerns → validate with load test
```

### Phase 3: Pipeline Development (Days 6-15)

```
├── Set up ingestion (CDC, API polling, file drops)
├── Implement transformations (Spark, dbt, SQL)
├── Configure orchestration (Airflow DAGs)
├── Add quality checks and error handling
└── [✓ Done]: Pipelines running in staging
    [✗ FAIL]: Quality checks failing → fix before prod
```

### Phase 4: Production Deployment (Days 16-20)

```
├── Deploy to production with monitoring
├── Validate data quality in production
├── Train stakeholders on data access
├── Document lineage and refresh schedules
└── [✓ Done]: Production stable, users enabled
    [✗ FAIL]: SLA not met → optimize or renegotiate
```

---
