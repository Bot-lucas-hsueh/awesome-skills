# Microsoft Azure Reference

## Global Infrastructure

### Regions & Datacenters
- **60+ Azure regions** globally (more than any cloud provider)
- **400+ datacenters** across six continents
- **170+ network POPs** (Points of Presence)
- **2+ gigawatts** of new capacity added in FY2025
- Every region is **AI-first** with liquid cooling support

### Special Regions
| Region Type | Purpose |
|-------------|---------|
| Azure Government | US government workloads (FedRAMP High, DoD IL5) |
| Azure China | Operated by 21Vianet, data stays in China |
| Azure Germany | Data trustee model for German data residency |
| Sovereign Clouds | Custom clouds for specific countries/industries |

## Core Services

### Compute
| Service | Best For | Pricing Model |
|---------|----------|---------------|
| Virtual Machines | Lift-and-shift, control | Per-second billing |
| AKS (Kubernetes) | Container orchestration | Per-node billing |
| Container Apps | Serverless containers | Per-use |
| Functions | Event-driven code | Per-execution |
| App Service | Web apps, APIs | Instance-based |

### AI/ML Services
| Service | Capabilities |
|---------|-------------|
| Azure OpenAI | GPT-4, GPT-4o, o1, o3 series |
| AI Foundry | 11,000+ models, deployment, fine-tuning |
| Azure ML | Custom model training, MLOps |
| AI Search | RAG, vector search, cognitive search |
| Speech Services | Transcription, translation, TTS |
| Vision Services | OCR, image analysis, face recognition |

### Storage
| Service | Use Case |
|---------|----------|
| Blob Storage | Unstructured data, backups |
| Files | SMB/NFS file shares |
| Disk Storage | VM disks |
| Data Lake | Big data analytics |
| NetApp Files | Enterprise NAS |

## Pricing & SLAs

### Compute Pricing (Sample)
| VM Type | Specs | Linux/hour | Windows/hour |
|---------|-------|------------|--------------|
| B2s | 2 vCPU, 4GB | $0.041 | $0.091 |
| D4s v5 | 4 vCPU, 16GB | $0.192 | $0.344 |
| E8s v5 | 8 vCPU, 64GB | $0.504 | $0.912 |
| F64s v2 | 64 vCPU, 128GB | $2.448 | $4.656 |

### Azure OpenAI Pricing
| Model | Input | Output |
|-------|-------|--------|
| GPT-4o | $2.50/m tokens | $10.00/m tokens |
| GPT-4o mini | $0.150/m tokens | $0.600/m tokens |
| o1 | $15.00/m tokens | $60.00/m tokens |
| o3-mini | $1.10/m tokens | $4.40/m tokens |

## Architecture Patterns

### Multi-Region Active-Active
```
Traffic Manager
├── Region 1 (Primary)
│   ├── App Service
│   ├── SQL Database (Primary)
│   └── Blob Storage (RA-GRS)
├── Region 2 (Secondary)
│   ├── App Service
│   ├── SQL Database (Secondary)
│   └── Blob Storage (RA-GRS)
└── Cosmos DB (Multi-region writes)
```

### Microservices on AKS
```
Ingress Controller (AGIC)
├── Frontend Pods
├── API Gateway
├── Service A (3 replicas)
├── Service B (5 replicas)
└── Background Workers
```

## Security Features

### Network Security
- NSGs (Network Security Groups)
- Azure Firewall
- DDoS Protection
- Private Link
- Application Gateway WAF

### Identity & Access
- Azure AD (Entra ID)
- Managed Identities
- Service Principals
- RBAC (Role-Based Access Control)
- PIM (Privileged Identity Management)

### Data Protection
- Azure Key Vault
- Customer-managed keys
- Private endpoints
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.3)

## Compliance Certifications

| Certification | Description |
|---------------|-------------|
| SOC 1/2/3 | Service Organization Control |
| ISO 27001 | Information security management |
| PCI DSS | Payment card industry |
| HIPAA | Healthcare data protection |
| FedRAMP | US federal cloud security |
| GDPR | EU data protection |

---

**Last Updated**: 2026-03-21
