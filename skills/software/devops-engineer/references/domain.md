## § 6 · Domain Knowledge

### 6.1 Kubernetes Resource Management

| Resource | Purpose | Best Practice |
|----------|---------|---------------|
| **Deployment** | Stateless apps | Rolling updates, health checks |
| **StatefulSet** | Stateful apps | Ordered deployment, PVCs |
| **DaemonSet** | Node agents | One per node (logging, monitoring) |
| **CronJob** | Scheduled tasks | Idempotent, resource limits |
| **Service** | Network access | ClusterIP internal, LB external |

### 6.2 CI/CD Pattern Comparison

| Pattern | Best For | Trade-off |
|---------|----------|-----------|
| **Push-based** | Simple pipelines | Less control, security concerns |
| **GitOps** | Kubernetes native | Eventual consistency |
| **Blue-Green** | Zero-downtime | 2× resource usage |
| **Canary** | Risk mitigation | Complex traffic management |
| **Feature Flags** | Decoupled release | Technical debt if not managed |

### 6.3 Terraform Best Practices

- [ ] Remote state with locking (S3 + DynamoDB)
- [ ] State encryption at rest
- [ ] Module-based organization
- [ ] Workspace per environment
- [ ] CI/CD validation (plan before apply)
- [ ] Drift detection scheduled

---
