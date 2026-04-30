## § 2 · Three-Layer Architecture

### Layer 1: Hybrid Cloud Foundation
```yaml
Hybrid Cloud Stack:
  Container Platform:
    - Red Hat OpenShift: #1 Enterprise Kubernetes platform
    - OpenShift AI: MLOps and model serving
    - IBM Cloud Satellite: Extend cloud services anywhere
  
  Infrastructure Automation:
    - Red Hat Ansible Automation Platform: 45M+ downloads/month
    - HashiCorp Terraform ($6.4B acquisition): IaC standard
    - HashiCorp Vault: Secrets management
    - HashiCorp Consul: Service mesh
  
  Integration & Middleware:
    - IBM API Connect: API management
    - IBM MQ: Enterprise messaging (used by 90% of Fortune 500)
    - IBM Event Streams: Kafka-based event streaming
    - IBM App Connect: Integration platform
  
  Cloud Infrastructure:
    - IBM Cloud: Public cloud with industry-specific capabilities
    - IBM Cloud for Financial Services: Compliance-ready
    - IBM Cloud for Healthcare: HIPAA/HITRUST certified
```

### Layer 2: AI & Data Platform
```yaml
watsonx Platform:
  watsonx.ai:
    - Foundation model development and deployment
    - Granite model family (open-source, enterprise-grade)
    - Prompt Lab for prompt engineering
    - Tuning Studio for model customization
    - Synthetic data generation
  
  watsonx.data:
    - Open lakehouse architecture
    - Query federation across data sources
    - Open formats (Iceberg, Parquet, Delta Lake)
    - Self-service data access
  
  watsonx.governance:
    - AI lifecycle management
    - Model risk management
    - Regulatory compliance (EU AI Act preparation)
    - Bias detection and mitigation
    - Explainability and drift monitoring
```

**Granite Model Family (Open Source)**:
| Model | Parameters | Best For | License |
|-------|------------|----------|---------|
| Granite 3.0 2B | 2B | Edge deployment, low latency | Apache 2.0 |
| Granite 3.0 8B | 8B | General enterprise tasks | Apache 2.0 |
| Granite 3.1 8B | 8B | Multilingual, code, reasoning | Apache 2.0 |
| Granite Code 20B | 20B | Code generation, analysis | Apache 2.0 |
| Granite Guardian | Variable | AI safety, content filtering | Apache 2.0 |

### Layer 3: Infrastructure & Quantum
```yaml
Infrastructure & Quantum:
  IBM Z (Mainframe):
    - z16: Telum AI processor, quantum-safe crypto
    - z17: Next-gen (2025+), enhanced AI inference
    - 99.99999% (7 nines) availability
    - Processes 70%+ of world's transaction value
  
  IBM Power:
    - Power10: AI inference acceleration
    - AIX, IBM i, Linux support
    - SAP HANA certified platforms
  
  Storage:
    - IBM FlashSystem: All-flash arrays
    - IBM Cloud Object Storage: Exabyte scale
    - IBM Storage Scale: High-performance computing
  
  Quantum Computing:
    - IBM Quantum Network: 300+ members
    - Qiskit: Open-source SDK
    - Heron processors: 133 qubits
    - Roadmap: Starling (200 logical qubits, 2029)
```

---
