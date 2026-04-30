# watsonx Platform Technical Reference

## Overview

watsonx is IBM's enterprise AI and data platform designed for regulated industries. It consists of three core components: watsonx.ai for AI development, watsonx.data for data management, and watsonx.governance for AI lifecycle management.

## watsonx.ai

### Foundation Models

| Model | Parameters | Context | Best For | License |
|-------|------------|---------|----------|---------|
| Granite 3.0 2B | 2B | 128K | Edge, latency-critical | Apache 2.0 |
| Granite 3.0 8B | 8B | 128K | General enterprise | Apache 2.0 |
| Granite 3.1 8B | 8B | 128K | Multilingual, code | Apache 2.0 |
| Granite Code 20B | 20B | Varied | Code generation | Apache 2.0 |
| Granite Guardian | Variable | — | Safety, content filtering | Apache 2.0 |

### Key Capabilities

```yaml
watsonx.ai Features:
  Prompt Lab:
    - Interactive prompt engineering
    - Few-shot prompting support
    - Prompt versioning and sharing
    
  Tuning Studio:
    - Fine-tuning with enterprise data
    - LoRA (Low-Rank Adaptation)
    - Instruction tuning
    
  Deployments:
    - Real-time inference endpoints
    - Batch processing
    - Model quantization
    
  Integration:
    - LangChain compatible
    - LlamaIndex compatible
    - REST API
    - SDK (Python, Node.js)
```

### Deployment Options

| Option | Description | Use Case |
|--------|-------------|----------|
| **SaaS** | Managed service on IBM Cloud | Quick start, variable workloads |
| **Software** | Deployed on CP4D or OpenShift | Data residency, compliance |
| **Dedicated** | Single-tenant cloud | Regulatory requirements |

## watsonx.data

### Lakehouse Architecture

```yaml
watsonx.data Components:
  Storage:
    - Object storage (IBM COS, S3, Azure Blob, GCS)
    - Open table formats (Iceberg, Delta Lake, Hudi)
    
  Query Engines:
    - Presto/Trino (SQL queries)
    - Spark (analytics, ML)
    - watsonx.ai (AI/ML workloads)
    
  Governance:
    - Unified data catalog
    - Data lineage
    - Access control (RBAC, ABAC)
    
  Connectors:
    - Databases: Db2, Oracle, PostgreSQL, MySQL
    - Data warehouses: Snowflake, BigQuery, Redshift
    - Streaming: Kafka, Event Streams
```

### Performance Characteristics

| Feature | Specification |
|---------|---------------|
| Query latency | Sub-second for cached data |
| Data volume | Petabyte scale |
| Concurrent users | 1000+ |
| Data formats | Parquet, ORC, Avro, JSON, CSV |

## watsonx.governance

### AI Lifecycle Management

```yaml
Governance Capabilities:
  Model Cards:
    - Purpose and intended use
    - Performance metrics
    - Limitations and risks
    - Training data summary
    
  Risk Management:
    - Risk scoring by use case
    - Approval workflows
    - Audit trails
    
  Monitoring:
    - Data drift detection
    - Model drift detection
    - Performance degradation alerts
    - Bias monitoring
    
  Compliance:
    - EU AI Act readiness
    - Industry regulations (FDA, FINRA)
    - Explainability reports
```

### Bias Detection

| Protected Attribute | Metrics |
|---------------------|---------|
| Gender | Disparate impact, equal opportunity |
| Age | Statistical parity, calibration |
| Race/Ethnicity | Demographic parity, predictive parity |
| Custom | Configurable attributes |

## Integration Patterns

### RAG (Retrieval-Augmented Generation)

```python
# watsonx RAG pattern
from watsonx import WatsonXAI, WatsonXData

# 1. Ingest documents to vector store
data = WatsonXData()
data.ingest_documents(
    source="s3://enterprise-docs/",
    vector_store="milvus",
    embedding_model="ibm/slate-125m-english-rtrvr"
)

# 2. Query with retrieval
ai = WatsonXAI(model="granite-3-8b")
response = ai.generate(
    query="What is our refund policy?",
    retrieval_context=data.search(query, top_k=5),
    temperature=0.1
)
```

### Multi-Modal AI

```yaml
Multi-Modal Use Cases:
  Document Understanding:
    - OCR + LLM for extraction
    - Layout preservation
    - Table extraction
    
  Visual Inspection:
    - Image classification
    - Defect detection
    - Quality assurance
```

## Pricing Model

| Component | Pricing Unit |
|-----------|--------------|
| watsonx.ai | Per token (input/output) |
| watsonx.data | Per TB stored + queries |
| watsonx.governance | Per model managed |
| Training/Tuning | Compute hours (GPU) |

## Best Practices

### Security
- Use private endpoints for sensitive workloads
- Enable encryption at rest and in transit
- Implement role-based access control
- Audit all model access and predictions

### Performance
- Use caching for common queries
- Implement batch processing for bulk operations
- Right-size GPU instances for training
- Monitor token usage for cost optimization

### Governance
- Create model cards before deployment
- Implement bias detection in staging
- Set up automated drift monitoring
- Document all AI decisions

---

*Source: IBM watsonx Documentation, IBM Developer, IBM Research Publications*
