## § 8 · Scenario Examples

### Example 1: Real-time Analytics Platform

**Context**: Build platform processing 1M events/sec for live dashboards.

**Architecture**:
```
Pipeline:
├── Ingestion: Kafka (100 partitions)
├── Processing: Flink for windowed aggregations
├── Storage: ClickHouse for sub-second queries
├── Serving: Grafana for visualization

Optimizations:
├── 10-second tumbling windows for metrics
├── Exactly-once semantics for accuracy
├── Partitioning by event time for efficiency
```

---

### Example 2: Data Warehouse Migration

**Context**: Migrate from legacy warehouse to Snowflake.

**Migration Plan**:
```
Phases:
├── Phase 1: Dual-write to old and new
├── Phase 2: Migrate historical data (bulk)
├── Phase 3: Switch reads to Snowflake
├── Phase 4: Decommission old system

Validation:
├── Row count parity checks
├── Sample data comparison
├── Query result matching
├── Performance benchmarking
```

---

### Example 3: ML Feature Platform

**Context**: Build feature store for ML model serving.

**Implementation**:
```
Components:
├── Offline store: Delta Lake for training data
├── Online store: Redis for low-latency serving
├── Feature engineering: Spark for transformations
├── Registry: Feast for feature discovery

Features:
├── Point-in-time correctness for training
├── Consistency between training and serving
├── Feature versioning and lineage
```

---

### Example 4: GDPR Compliance Implementation

**Context**: Implement right to deletion across data lake.

**Solution**:
```
Approach:
├── PII tagging at ingestion
├── Automated detection with ML
├── Deletion orchestration across systems
├── Audit trail for compliance

Challenges:
├── Immutable data lakes vs. deletion
├── Propagation to derived tables
├── Backup retention policies
```

---

### Example 5: Cost Optimization Project

**Context**: Reduce BigQuery spend by 50%.

**Optimizations**:
```
Actions:
├── Partition pruning (date filters)
├── Clustering on frequently filtered columns
├── Materialized views for common aggregations
├── Query caching optimization
├── Storage lifecycle policies

Results:
├── 60% cost reduction
├── Query performance improved 3×
├── Better user experience
```

---
