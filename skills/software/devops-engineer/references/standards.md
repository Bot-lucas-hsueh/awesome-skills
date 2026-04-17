## 7. Standards & Reference

### 7.1 SRE Frameworks

| Framework / 框架 | When to Use / 使用场景 | Key Steps
|-----------------|----------------------|-------------------|
| **SLO Definition** | New service or existing service without SLO | 1. Identify key user journeys → 2. Define SLI (metric) → 3. Set SLO threshold → 4. Calculate error budget → 5. Set burn rate alerts |
| **Incident Response** | P1/P2 production outage | 1. Detect (<5min) → 2. Declare + assemble → 3. Mitigate (rollback/failover) → 4. Diagnose root cause → 5. Resolve → 6. Postmortem |
| **Blameless Postmortem** | After every P1, within 48h | 1. Timeline reconstruction → 2. Contributing factors → 3. What went well → 4. Action items with owners/dates |
| **Change Management** | Risky production changes | 1. Risk assessment (blast radius) → 2. Rollback plan → 3. Canary/blue-green → 4. Monitor burn rate 30min → 5. Full rollout or rollback |

### 7.2 SRE Metrics

| Metric / 指标 | Formula / 公式 | Target
|--------------|--------------|---------------|
| **Availability SLO** | (Good requests
| **Error Budget Remaining** | (1 - SLO) × period_minutes | >0% (monitor burn rate) |
| **MTTR (Mean Time to Restore)** | Sum(restore time)
| **Deployment Frequency** | Deploys per day (team-level) | Elite: >1/day; High: 1/week |
| **Change Failure Rate** | Failed deploys
| **P99 API Latency** | `histogram_quantile(0.99, rate(duration_bucket[5m]))` | Per-SLO (e.g., <500ms) |

### 7.3 CI/CD Pipeline Design Decision Guide / CI/CD 流水线设计决策指南

| Scenario / 场景 | Recommended Approach / 推荐方案 | Reason
|----------------|--------------------------------|--------------|
| Monorepo + multiple services | Path filtering + matrix builds | Only rebuild affected services |
| High-security (fintech, health) | Manual approval gate + SAST + SBOM | Compliance, audit trail |
| Feature flags required | Separate build from deploy; LaunchDarkly/Flagsmith | Ship code, control rollout |
| Multi-cloud deployment | Separate CD per cloud; shared Helm charts | Avoid blast radius coupling |
| Canary deployment needed | Argo Rollouts + Prometheus analysis | Automated traffic shifting with metric gates |

---

