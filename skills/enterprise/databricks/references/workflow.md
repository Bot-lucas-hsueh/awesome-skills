## 8. Standard Workflow

### Phase 1: Lakehouse Design

| Step | Action | Output | ✓ Done When | ✗ FAIL If |
|------|--------|--------|-------------|-----------|
| 1.1 | Assess data sources | Source inventory | All sources documented | Missing CDC sources |
| 1.2 | Design medallion layers | Architecture diagram | Bronze→Silver→Gold mapped | No data quality gates |
| 1.3 | Define Delta Lake config | Table properties | OPTIMIZE/VACUUM scheduled | Default retention only |
| 1.4 | Configure Unity Catalog | Access policies | Row/column security set | No lineage tracking |

### Phase 2: Pipeline Implementation

| Step | Action | Output | ✓ Done When | ✗ FAIL If |
|------|--------|--------|-------------|-----------|
| 2.1 | Ingest with Auto Loader | Bronze tables | Schema evolution handled | Manual file listing |
| 2.2 | Transform with DLT | Silver tables | Data quality constraints | No validation rules |
| 2.3 | Build Gold aggregates | Business tables | Incremental refresh | Full rebuild required |
| 2.4 | Optimize performance | Z-ordered tables | Query <10s on gold | Full scans on large tables |

### Phase 3: AI & Governance

| Step | Action | Output | ✓ Done When | ✗ FAIL If |
|------|--------|--------|-------------|-----------|
| 3.1 | Set up MLflow tracking | Experiment registry | All runs logged | Manual model versioning |
| 3.2 | Deploy Model Serving | REST endpoints | <100ms p99 latency | Batch inference for real-time |
| 3.3 | Configure Vector Search | Search indexes | Auto-sync enabled | Stale embeddings |
| 3.4 | Enable data sharing | Delta Sharing | Cross-org access | Manual data copies |

---
