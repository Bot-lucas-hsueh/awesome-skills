## § 6 · Domain Knowledge

### 6.1 Batch vs Streaming Decision Matrix

| Factor | Batch | Streaming |
|--------|-------|-----------|
| **Latency** | Minutes to hours | Milliseconds to seconds |
| **Throughput** | Very high | High |
| **Complexity** | Lower | Higher |
| **Cost** | Lower | Higher |
| **Use Case** | Reporting, ML training | Monitoring, recommendations |

### 6.2 Data Warehouse Schema Patterns

| Pattern | Best For | Example |
|---------|----------|---------|
| **Star Schema** | Simple analytics | Sales by date/product |
| **Snowflake Schema** | Normalized dimensions | Complex hierarchies |
| **Data Vault** | Enterprise scale | Auditability, flexibility |
| **One Big Table** | BigQuery optimization | Event analytics |

### 6.3 File Format Comparison

| Format | Compression | Query Perf | Schema Evolution | Best For |
|--------|-------------|------------|------------------|----------|
| **Parquet** | Excellent | Excellent | Limited | Analytics |
| **ORC** | Excellent | Excellent | Limited | Hive/Spark |
| **Avro** | Good | N/A | Excellent | Streaming |
| **JSON** | Poor | Poor | N/A | Nested data |
| **Delta Lake** | Excellent | Excellent | Excellent | Lakehouse |

---
