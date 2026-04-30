# Google Cloud Platform Services Reference

Complete catalog of GCP services organized by category.

## Compute

### Virtual Machines
| Service | Description | Use Cases |
|---------|-------------|-----------|
| Compute Engine | IaaS VMs with persistent disks | Lift-and-shift, custom workloads |
| Sole-Tenant Nodes | Dedicated physical servers | Compliance, licensing requirements |
| Confidential VMs | Memory encryption (AMD SEV) | Sensitive workloads |

### Containers & Serverless
| Service | Description | Use Cases |
|---------|-------------|-----------|
| GKE | Managed Kubernetes | Container orchestration |
| GKE Autopilot | Serverless Kubernetes | Simplified ops, cost optimization |
| Cloud Run | Serverless containers | HTTP workloads, microservices |
| Cloud Functions | Event-driven functions | Triggers, lightweight processing |
| App Engine | Fully managed PaaS | Web apps, auto-scaling |

## Storage

### Object Storage
| Service | Class | Access Pattern | Min Duration |
|---------|-------|----------------|--------------|
| Standard | Hot | Frequent | None |
| Nearline | Cool | Monthly | 30 days |
| Coldline | Cold | Quarterly | 90 days |
| Archive | Archive | Yearly | 365 days |

### Block & File
| Service | Protocol | Performance | Use Cases |
|---------|----------|-------------|-----------|
| Persistent Disk | SCSI/NVMe | up to 1.2M IOPS | VM boot, databases |
| Hyperdisk | NVMe | up to 2.8M IOPS | High-performance DBs |
| Filestore | NFS v3 | 25 GB/s | Shared file storage |
| Parallelstore | POSIX | HPC-optimized | AI/ML training |

### Databases
| Service | Type | Consistency | Global? |
|---------|------|-------------|---------|
| Cloud SQL | PostgreSQL, MySQL, SQL Server | Strong | No |
| AlloyDB | PostgreSQL-compatible | Strong | No |
| Spanner | Distributed SQL | External | Yes |
| Bigtable | Wide-column | Eventual | Yes |
| Firestore | Document | Strong (regional) | Conditional |
| Memorystore | Redis, Valkey | Eventual | No |

## Networking

### Core Services
| Service | Purpose | Key Features |
|---------|---------|--------------|
| VPC | Virtual network | Global, shared, auto/custom modes |
| Cloud Load Balancing | Traffic distribution | Global, multi-region, health checks |
| Cloud CDN | Content delivery | 140+ locations, cache control |
| Cloud Armor | DDoS/WAF protection | ML-based, OWASP rules |
| Cloud NAT | Outbound connectivity | No public IPs required |
| Cloud Interconnect | Hybrid connectivity | Dedicated (10G-100G), Partner |

### Network Connectivity Center
- SD-WAN integration
- Private SaaS access
- Multi-cloud networking

## Data & Analytics

### Big Data
| Service | Purpose | Scale |
|---------|---------|-------|
| BigQuery | Data warehouse | Petabyte-scale, serverless |
| BigQuery BI Engine | In-memory analytics | Sub-second queries |
| Dataflow | Stream/batch processing | Apache Beam |
| Dataproc | Managed Hadoop/Spark | Autoscaling clusters |
| Pub/Sub | Message queue | Millions msg/sec |
| Data Fusion | Visual ETL | Code-free pipelines |
| Looker | BI/Analytics | Semantic modeling |

### Data Governance
| Service | Purpose |
|---------|---------|
| Dataplex | Data fabric |
| Data Catalog | Metadata management |
| Dataform | SQL-based transformations |
| Cloud DLP | Data loss prevention |

## AI & Machine Learning

### Vertex AI Platform
| Component | Purpose |
|-----------|---------|
| Vertex AI Workbench | Notebooks & IDEs |
| Vertex AI Training | Custom model training |
| Vertex AI Prediction | Model serving |
| Vertex AI Pipelines | MLOps orchestration |
| Vertex AI Feature Store | Feature management |
| Vertex AI Model Registry | Model versioning |
| Vertex AI Model Monitoring | Production monitoring |

### Pre-trained APIs
| API | Capability |
|-----|------------|
| Vision API | Image analysis |
| Video Intelligence API | Video analysis |
| Natural Language API | Text analysis |
| Speech-to-Text | Audio transcription |
| Text-to-Speech | Voice synthesis |
| Translation API | Language translation |
| Document AI | Document parsing |
| Dialogflow | Conversational AI |

### Foundation Models
| Model | Context | Best For |
|-------|---------|----------|
| Gemini 2.5 Pro | 1M tokens | Complex reasoning |
| Gemini 2.5 Flash | 1M tokens | Speed/cost balance |
| Gemini 2.0 Flash | 1M tokens | Real-time applications |
| Gemini 1.5 Pro | 2M tokens | Long documents |
| Imagen 3 | N/A | Image generation |
| Veo 2 | N/A | Video generation |

## Security

### Core Security
| Service | Purpose |
|---------|---------|
| IAM | Identity & access management |
| Cloud KMS | Key management (HSM available) |
| Secret Manager | Secret storage |
| Binary Authorization | Container security |
| Assured Workloads | Compliance environments |
| Security Command Center | Security analytics |
| Chronicle | SIEM/SOAR |
| Mandiant | Threat intelligence |

## Operations

### Monitoring & Management
| Service | Purpose |
|---------|---------|
| Cloud Monitoring | Metrics & dashboards |
| Cloud Logging | Log aggregation |
| Cloud Trace | Distributed tracing |
| Cloud Profiler | CPU/memory profiling |
| Cloud Debugger | Production debugging |
| Cloud Build | CI/CD |
| Artifact Registry | Container/artifact storage |
| Cloud Deploy | Continuous delivery |

## Migration & Hybrid

| Service | Purpose |
|---------|---------|
| Migrate for Compute Engine | VM migration |
| Migrate for Anthos | Container migration |
| Database Migration Service | Database migration |
| Transfer Appliance | Petabyte data transfer |
| Storage Transfer Service | Cloud-to-cloud transfer |
| Anthos | Hybrid/multi-cloud platform |
| GKE On-Prem | On-premises Kubernetes |

## Pricing Models

### Compute Pricing
| Model | Best For |
|-------|----------|
| On-demand | Variable workloads |
| Committed Use (1/3 year) | Predictable workloads |
| Spot/Preemptible | Fault-tolerant batch |
| SUD (Sustained Use) | Automatic discounts |

### Storage Pricing Components
- Storage capacity (per GB/month)
- Network egress
- Operations (class A/B)
- Retrieval (for cold storage)
