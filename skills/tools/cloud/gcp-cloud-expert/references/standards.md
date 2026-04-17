# Standards & Reference

## 7.1 Official Documentation

- [Google Cloud Documentation](https://cloud.google.com/docs) — Full documentation for all GCP services
- [Google Cloud Architecture Center](https://cloud.google.com/architecture) — Reference architectures and patterns
- [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework) — Operational excellence, security, reliability, cost optimization
- [GCP IAM Documentation](https://cloud.google.com/iam/docs) — Identity and access management
- [GCP Regions](https://cloud.google.com/about/locations) — Available regions and zones
- [gcloud CLI Reference](https://cloud.google.com/sdk/gcloud/reference) — All gcloud commands
- [GCP REST API Reference](https://cloud.google.com/compute/docs/api) — REST API documentation
- [GCP Support Plans](https://cloud.google.com/support#section=support-plans) — Basic, Developer, Production, Enhanced

## 7.2 IAM Best Practices

### 7.2.1 Principle of Least Privilege

| Practice | Implementation |
|----------|----------------|
| **Use predefined roles** | Prefer `roles/storage.objectViewer` over `roles/owner` |
| **Create custom roles** | Only when predefined roles don't fit |
| **Service accounts** | Use for workloads, not user credentials |
| **Workload Identity** | For GKE/Kubernetes workloads |
| **MFA** | Enable for all users |

### 7.2.2 IAM Policy Structure

```json
{
  "bindings": [
    {
      "role": "roles/storage.objectViewer",
      "members": [
        "user:alice@example.com",
        "serviceAccount:my-app@my-project.iam.gserviceaccount.com",
        "group:devs@example.com"
      ]
    }
  ]
}
```

### 7.2.3 Service Account Best Practices

| Practice | Implementation |
|----------|----------------|
| **No static keys** | Use Workload Identity federation |
| **Rotation** | Rotate keys if needed, max 90 days |
| **Scoping** | Attach only needed roles |
| **Audit** | Enable Cloud Audit Logs |

### 7.2.4 Organization Policies

```bash
# List organization policies
gcloud org-policies list --project=my-project

# Set constraint (disable VM external IP)
gcloud org-policies set-policy my-policy.yaml --project=my-project

# my-policy.yaml example
# name: constraints/compute.vmExternalIp
# spec:
#   constraint: constraints/compute.vmExternalIp
#   listPolicy:
#     deniedValues:
#       - "true"
```

## 7.3 Region and Zone Selection

### 7.3.1 Key Factors

| Factor | Consideration |
|--------|---------------|
| **Latency** | Choose region closest to users |
| **Data residency** | Some data must stay in specific regions |
| **Service availability** | Not all services in all regions |
| **Price** | Same service varies 2-5x between regions |
| **Carbon** | Choose lower-carbon regions when possible |

### 7.3.2 Common GCP Regions

| Region | Location | Use Case |
|--------|----------|----------|
| us-central1 | Iowa | Default, most services, lowest cost |
| us-east1 | South Carolina | East coast, good availability |
| europe-west1 | Belgium | EU workloads, GDPR |
| asia-east1 | Taiwan | APAC workloads |
| asia-northeast1 | Tokyo | Japan, gaming |

### 7.3.3 Zone Architecture

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Single zone** | All resources in one zone | Dev/test, lowest cost |
| **Multi-zonal** | Resources spread across zones in region | Production |
| **Regional** | Resources replicated regionally | HA, critical workloads |

## 7.4 Cost Optimization

### 7.4.1 Cost Management Hierarchy

```
GCP Cost Optimization
├── Committed Use Discounts (30-57% savings)
├── Spot VMs / Preemptible (60-91% savings)
├── Sustained Use Discounts (automatic)
├── Right-sizing recommendations
├── Committed Use Reservations for memory/CPU
└── Labels for cost attribution
```

### 7.4.2 Committed Use Discounts

| Resource | 1-Year Commitment | 3-Year Commitment |
|----------|-------------------|------------------|
| Regular VMs | Up to 57% | Up to 70% |
| Memory-optimized | Up to 70% | Up to 83% |
| Compute-optimized | Up to 60% | Up to 76% |

### 7.4.3 Discount Types

| Type | Eligibility | Savings |
|------|-------------|---------|
| **Sustained Use** | >25% usage of month | Up to 30% |
| **Committed Use** | 1 or 3 year commitment | 30-70% |
| **Spot VMs** | Interruptible workloads | 60-91% |
| **Preemptible** | Similar to Spot | 60-91% |

### 7.4.4 Storage Tiers

| Storage Class | Cost/GB/mo | Min Storage Duration |
|---------------|------------|---------------------|
| Standard | $0.020 | None |
| Nearline | $0.010 | 30 days |
| Coldline | $0.004 | 90 days |
| Archive | $0.0012 | 365 days |

## 7.5 Resource Naming

### 7.5.1 Naming Conventions

| Resource | Pattern | Example |
|----------|---------|---------|
| Project | `{org}-{env}-{name}` | acme-prod-webapp |
| Compute Instance | `{env}-{role}-{##}` | prod-web-01 |
| GKE Cluster | `{env}-{name}` | prod-cluster |
| Cloud SQL | `{env}-{type}` | prod-postgres |
| Cloud Storage | `{project}-{env}-{type}` | acme-prod-static |
| Load Balancer | `{env}-{name}-lb` | prod-web-lb |

### 7.5.2 Label Standards

Required labels for cost tracking:
- `environment`: dev, staging, prod
- `team`: engineering, marketing, etc.
- `application`: webapp, api, etc.
- `cost-center`: department code

## 7.6 GCP Well-Architected Framework

| Pillar | Focus Areas |
|--------|-------------|
| **Operational Excellence** | Automation, monitoring, alerting |
| **Security** | IAM, encryption, network security |
| **Reliability** | Multi-zone, DR, backups |
| **Cost Optimization** | CUDs, right-sizing, labels |
| **Performance** | Right machine type, caching |
