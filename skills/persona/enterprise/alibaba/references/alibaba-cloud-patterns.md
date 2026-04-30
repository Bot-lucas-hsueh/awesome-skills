# Alibaba Cloud Architecture Patterns

> Cloud-native architecture patterns from Asia Pacific's largest cloud provider serving 4M+ customers with 80+ availability zones.

---

## Alibaba Cloud Overview

| Metric | Value |
|--------|-------|
| **Global Market Share** | 4% (#4 globally, #1 in China APAC) |
| **Annual Revenue** | ¥100+ billion |
| **Growth Rate** | 13% YoY (Q3 FY2025) |
| **AI Revenue Growth** | Triple digits (6 consecutive quarters) |
| **Availability Zones** | 80+ across 28 regions |
| **Services** | 200+ cloud products |

---

## Core Service Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                      APPLICATION LAYER                          │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │   Web    │ │  Mobile  │ │   IoT    │ │   AI/ML  │           │
│  │   Apps   │ │   Apps   │ │ Devices  │ │ Models   │           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                     PLATFORM LAYER                              │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │   Container │ │  Function   │ │     AI      │               │
│  │   Service   │ │  Compute    │ │  Platform   │               │
│  │  (ACK)      │ │  (FC)       │  │  (PAI)     │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │  Middleware │ │   Message   │ │   Database  │               │
│  │   (MSE)     │ │   (RocketMQ)│ │  (RDS/PolarDB)│             │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                   INFRASTRUCTURE LAYER                          │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │   Compute   │ │   Storage   │ │   Network   │               │
│  │    (ECS)    │ │   (OSS)     │ │    (VPC)    │               │
│  │             │ │   (NAS)     │ │   (SLB)     │               │
│  │             │ │  (ESSD)     │ │  (GA)       │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────────┐
│                   FOUNDATION LAYER                              │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │  Identity   │ │   Security  │ │ Operations  │               │
│  │  (RAM)      │ │   (WAF)     │ │  (ARMS)     │               │
│  │             │ │   (KMS)     │ │  (SLS)      │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Products Deep Dive

### Compute: ECS & Beyond

| Service | Use Case | Key Feature |
|---------|----------|-------------|
| **ECS** | General compute | 200+ instance types, burstable to 2x CPU |
| **ECI** | Container workloads | Serverless containers, pay per second |
| **Function Compute** | Event-driven | Auto-scaling, 0 to 10K in seconds |
| **ACK** | Kubernetes | Managed K8s with GPU/spot support |
| **EHPC** | HPC workloads | Parallel cluster with RDMA |

**Auto-Scaling Strategy:**

```yaml
Scaling Rules:
  - Metric: CPU > 70%
    Action: Add 2 instances
    Cooldown: 300s
  - Metric: CPU < 30%
    Action: Remove 1 instance
    Cooldown: 600s
  - Schedule: Daily 08:00
    Action: Set minimum to 10
  - Schedule: Daily 22:00
    Action: Set minimum to 2
```

### Storage Solutions

| Service | Type | Performance | Use Case |
|---------|------|-------------|----------|
| **OSS** | Object | 10K+ TPS | Images, videos, backups |
| **NAS** | File | 10+ GB/s | Shared filesystem |
| **ESSD** | Block | 1M IOPS | Databases, high I/O |
| **Tablestore** | NoSQL | Single-digit ms | Time-series, logs |
| **HBase** | Wide-column | Millions QPS | Big data, real-time |

**OSS Storage Classes:**

```
Standard ──► IA ──► Archive ──► Cold Archive
(Frequent)   (30d)   (60d)       (180d)
   │           │        │            │
   ▼           ▼        ▼            ▼
  ¥0.12/GB   ¥0.08   ¥0.033       ¥0.015
```

### Database: PolarDB

**Architecture:**

```
         ┌─────────────────────────────────────┐
         │         PolarProxy (RW Split)        │
         └───────────────┬─────────────────────┘
                         │
         ┌───────────────┴───────────────┐
         ▼                               ▼
    ┌─────────┐                    ┌─────────┐
    │ Primary │◄─────Redo Log─────►│ Standby │
    │  (RW)   │      (Sync)        │  (HA)   │
    └────┬────┘                    └─────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐ ┌───────┐
│ RO-1  │ │ RO-2  │  (Read Replicas)
└───────┘ └───────┘
```

**Key Features:**
- Storage-compute separation
- Scale to 100TB per instance
- 15 read replicas
- 99.99% availability SLA

---

## AI & Machine Learning

### Qwen Model Family

| Model | Parameters | Use Case |
|-------|------------|----------|
| **Qwen-Max** | 100B+ | Complex reasoning, coding |
| **Qwen-Plus** | 72B | Balanced performance |
| **Qwen-Turbo** | 7B | Fast inference, cost-effective |
| **Qwen-VL** | 7B | Vision-language tasks |
| **Qwen-Audio** | - | Audio understanding |

### Platform: PAI (Platform of AI)

```
Data ──► PAI-DSW ──► PAI-DLC ──► PAI-EAS
         (Dev)       (Training)   (Serving)

Components:
- PAI-Designer: Visual ML pipeline
- PAI-AutoLearning: AutoML
- PAI-FeatureStore: Feature management
- PAI-Blade: Inference optimization
```

---

## Cloud-Native Patterns

### 1. Microservices on ACK

```yaml
# Deployment Pattern
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 0
  template:
    spec:
      containers:
      - name: order
        image: registry.cn-hangzhou.aliyuncs.com/app/order:v1.2
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
```

### 2. Serverless with Function Compute

```python
# Function Compute Handler
def handler(event, context):
    """
    Process order asynchronously
    Trigger: HTTP, EventBridge, or MQ
    """
    order = json.loads(event)
    
    # Validate order
    if not validate(order):
        return {'statusCode': 400}
    
    # Process payment
    result = process_payment(order)
    
    # Send notification
    notify_customer(order['user_id'], result)
    
    return {
        'statusCode': 200,
        'requestId': context.request_id
    }
```

### 3. Event-Driven Architecture

```
Event Sources ──► EventBridge ──► Rules ──► Targets
    │                               │
    ├── OSS Upload                  ├── Function Compute
    ├── RDS Change                  ├── MNS Queue
    ├── Schedule                    ├── HTTP Endpoint
    └── Custom Events               └── Log Service
```

---

## Security Best Practices

### Defense in Depth

```
Layer 1: Network
  - VPC isolation
  - Security groups
  - WAF for public endpoints

Layer 2: Identity
  - RAM for access control
  - MFA for privileged accounts
  - Role-based access (RBAC)

Layer 3: Data
  - KMS for key management
  - TDE for databases
  - Client-side encryption for OSS

Layer 4: Application
  - Security Center for threat detection
  - Code scanning (DevSecOps)
  - Container image scanning
```

### Compliance

| Standard | Coverage |
|----------|----------|
| **MLPS** | China cybersecurity compliance |
| **GDPR** | EU data protection |
| **PCI-DSS** | Payment card industry |
| **ISO 27001** | Information security management |
| **SOC 2** | Service organization controls |

---

## Cost Optimization

### Strategies

| Strategy | Savings | Implementation |
|----------|---------|----------------|
| **Spot Instances** | 70-90% | Fault-tolerant workloads |
| **Reserved Instances** | 30-60% | Predictable workloads |
| **Auto-Scaling** | 20-40% | Match capacity to demand |
| **Storage Tiering** | 50-80% | Lifecycle policies |
| **Serverless** | Variable | Pay per use |

### FinOps Dashboard

```
Cost Breakdown:
├── Compute: 45% ████████████████████
├── Storage: 25% ██████████
├── Network: 15% ███████
├── Database: 10% █████
└── Others: 5% ██

Top Cost Drivers:
1. ECS instances (production) - ¥50K/mo
2. PolarDB storage - ¥30K/mo
3. OSS outbound traffic - ¥20K/mo
4. PAI training jobs - ¥15K/mo
```

---

## Disaster Recovery

### RTO/RPO by Tier

| Tier | RTO | RPO | Architecture |
|------|-----|-----|--------------|
| **Mission Critical** | < 1 min | 0 | Multi-region active-active |
| **Critical** | < 15 min | < 1 min | Multi-region active-standby |
| **Standard** | < 4 hours | < 1 hour | Cross-region backup |
| **Development** | < 24 hours | < 24 hours | Weekly backup |

### Multi-Region Pattern

```
Region A (Primary)          Region B (Secondary)
┌─────────────┐             ┌─────────────┐
│   Active    │◄───────────►│   Active    │  (Data sync)
│   Traffic   │             │   (Standby) │
└─────────────┘             └─────────────┘
       │                           │
       └───────────┬───────────────┘
                   ▼
            Global DNS
         (Health-based routing)
```

---

**Reference Version**: 1.0.0 | **Last Updated**: 2026-03-21
