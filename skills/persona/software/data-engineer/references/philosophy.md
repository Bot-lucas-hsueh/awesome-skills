## § 4 · Core Philosophy

### 4.1 Data Architecture Model

```
┌─────────────────────────────────────────┐
│         Analytics / ML / BI             │  ← Tableau, Looker, Jupyter
├─────────────────────────────────────────┤
│        Data Warehouse / Mart            │  ← Snowflake, BigQuery, dbt models
├─────────────────────────────────────────┤
│         Data Lake (Curated)             │  ← Delta Lake, Iceberg tables
├─────────────────────────────────────────┤
│         Data Lake (Raw)                 │  ← Parquet, JSON, Avro in S3/ADLS
├─────────────────────────────────────────┤
│         Ingestion Layer                 │  ← Kafka, Kinesis, Event Hubs
├─────────────────────────────────────────┤
│         Data Sources                    │  ← Databases, APIs, Logs, IoT
└─────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Immutable Raw Data** — Never modify source data; transformations create new datasets
2. **Pipeline Idempotency** — Same input always produces same output; safe to retry
3. **Schema Evolution** — Handle changing data formats without breaking consumers
4. **Data Quality Gates** — Bad data stops at the door, never pollutes downstream
5. **Cost Transparency** — Track cost per dataset, optimize expensive operations

---
