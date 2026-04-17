## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Secrets in Git

```markdown
❌ BAD:
# docker-compose.yml committed to git
DB_PASSWORD=prod-password-123
AWS_SECRET_KEY=AKIAIOSFODNN7EXAMPLE
# Result: GitHub/GitLab secret scanning or attacker fork = credential breach

✅ GOOD:
# Use external secrets injection
env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-credentials
        key: password
# Secrets stored in Vault or AWS Secrets Manager; rotated automatically
```

**Anti-Pattern 2: Single Replica in Production

```markdown
❌ BAD: replicas: 1 for any production service.
Rolling update kills the 1 pod → 100% downtime for 30-60 seconds.
Node failure → same result.

✅ GOOD:
replicas: 3  # minimum for HA
strategy:
  rollingUpdate:
    maxUnavailable: 0   # never bring down before new is ready
    maxSurge: 1         # one extra during rollout
+ Add PodDisruptionBudget: minAvailable: 2
```

**Anti-Pattern 3: No Resource Limits

```markdown
❌ BAD: No resources.limits on containers.
Memory leak in one pod → consumes all node memory → OOM kills ALL pods on node.
CPU-hungry job → starves critical services on same node.

✅ GOOD: Always set both requests and limits.
CPU limits: allow burst (2-4× request), CPU is compressible.
Memory limits: set 2× request; memory is NOT compressible → OOM if exceeded.
Use LimitRange at namespace level as default safety net.
```

### 🟡 Medium Severity

**Anti-Pattern 4: Terraform Without Remote State

```markdown
❌ BAD: terraform.tfstate stored locally.
Second engineer runs apply → overrides state → infrastructure drift.
Laptop stolen → state lost → must import every resource.

✅ GOOD: S3 + DynamoDB backend with encryption + versioning.
terraform {
  backend "s3" {
    bucket         = "mycompany-tfstate"
    key            = "prod/eks/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}
```

**Anti-Pattern 5: Deploying to Production Without Staging

```markdown
❌ BAD: Push to main → directly to production.
Schema migration bug affects all production users simultaneously.
Performance regression only discovered when revenue drops.

✅ GOOD: Always staging → canary → full production.
Staging validates correctness; canary validates performance under real traffic.
Canary: 5% traffic for 30min; auto-rollback if error rate > 1× SLO threshold.
```

**Anti-Pattern 6: Alert Without Runbook

```markdown
❌ BAD: Alert fires at 3am. On-call has no idea what to do.
Spends 30min reading code to understand the service.
Makes wrong decision under pressure → worsens outage.

✅ GOOD: Every alert has runbook_url annotation linking to:
- What the alert means (explain the metric)
- Impact on users
- Step-by-step diagnosis
- Recovery options (ordered by speed vs. risk)
- Escalation contacts
Enforce via alert validation lint in CI.
```

---

