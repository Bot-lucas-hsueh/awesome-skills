## 8. Standard Workflow

### 8.1 New Service CI/CD Setup / 新服务 CI/CD 搭建

```
Phase 1: Pipeline Architecture (Day 1)
├── Define branch strategy: trunk-based (recommended) vs. gitflow
├── Map environments: dev → staging → production (with approval gates)
├── Identify secrets needed: DB credentials, API keys, registry auth
├── Choose deployment strategy: rolling (default), blue-green, canary
└── [✓ Done]: Pipeline architecture diagram approved; secrets strategy agreed
    [✗ FAIL]: Secrets hardcoded in any config file → STOP, remove before proceeding

Phase 2: Pipeline Implementation (Day 2-3)
├── Write CI workflow: lint → unit tests → docker build → image scan → push
├── Add path filtering for monorepo (only rebuild changed services)
├── Configure registry: GHCR or ECR with immutable tags (never overwrite :latest in prod)
├── Write CD: GitOps update to manifests repo OR Helm upgrade in pipeline
└── [✓ Done]: First green pipeline run in staging; image scan passes with 0 Critical CVEs
    [✗ FAIL]: Critical CVE in base image → update base image, re-scan before proceeding

Phase 3: Hardening & Observability (Day 4-5)
├── Add k6 load test step: baseline perf test in staging pipeline
├── Configure Prometheus alerts: error rate + p99 latency for new service
├── Write runbook: deployment, rollback, scaling, common failure modes
├── Add PodDisruptionBudget + topologySpreadConstraints to K8s manifests
└── [✓ Done]: SLO alerts configured; runbook linked in Alertmanager annotation
    [✗ FAIL]: No runbook for a P1 alert → create runbook before enabling alert
```

### 8.2 Incident Response

```
Step 1: Detect & Declare (< 5 min)
  → Acknowledge alert; open incident channel (#inc-<date>-<issue>)
  → Assign roles: Incident Commander, Communications, Tech Lead
  → Post status page: "Investigating" (never go silent)

Step 2: Mitigate First, Diagnose Second (< 15 min)
  → Is a recent deploy the cause? → kubectl rollout undo
  → Is traffic spiky? → kubectl scale deployment --replicas=N
  → Is a dependency down? → Circuit breaker

Step 3: Diagnose Root Cause
  → Layer-by-layer: Application → K8s → Database → Network → Node
  → Use Golden Signals: which of Latency/Traffic/Errors/Saturation changed first?
  → Correlate with recent deploys, config changes, traffic spikes

Step 4: Resolve & Restore
  → Apply minimal fix; validate with Prometheus (error rate returns to baseline)
  → Update status page: "Resolved"

Step 5: Postmortem (within 48h)
  → Timeline, contributing factors, action items with owners

[✓ Done]: Error rate at pre-incident baseline for 30min; status page updated
[✗ FAIL]: Root cause unknown after 30min → escalate to senior engineer + vendor support
```

---

