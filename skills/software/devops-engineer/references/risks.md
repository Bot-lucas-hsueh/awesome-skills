## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Terraform State Corruption** | 🔴 Critical | State loss requires manual recovery | Remote state with locking, backups |
| **Kubernetes Misconfiguration** | 🔴 Critical | Exposed services, privilege escalation | Policy enforcement (OPA), scanning |
| **Secrets in Git** | 🔴 Critical | Credentials exposed in history | git-secrets, Vault, scanning |
| **Pipeline Compromise** | 🟠 High | Malicious code through CI/CD | Signed commits, approval gates |
| **Drift from Desired State** | 🟠 High | Manual changes bypass IaC | Drift detection, GitOps enforcement |
| **Cost Overruns** | 🟡 Medium | Uncontrolled cloud spending | Budgets, quotas, cost alerts |

---
