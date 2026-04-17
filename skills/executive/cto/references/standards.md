## 7. Standards & Reference

### 7.1 Technology Selection Framework

**Build vs Buy vs Partner Decision Matrix

| Criterion / 评判标准 | Build / 自研 | Buy / 购买 | Partner
|--------------------|------------|-----------|--------------|
| **Competitive differentiation** | Core to product differentiation | Commodity capability | Industry-specific, partner has moat |
| **Time-to-market** | Willing to invest 6–18 months | Need capability in < 3 months | Need ecosystem leverage |
| **Team expertise** | Deep existing expertise | No expertise, not worth building | Partner fills skill gap |
| **Long-term cost** | Build cost < 3-year SaaS cost | SaaS cost < build + maintain cost | Revenue share sustainable |
| **Data sensitivity** | Sensitive data, cannot share | Acceptable data terms | Data sharing agreement feasible |
| **Example** | Core ML ranking model | Auth (Auth0/Okta), monitoring (Datadog) | Payment processing (Stripe) |

**Wardley Map Positioning Guide

```
Genesis → Custom Built → Product/Rental → Commodity/Utility

Genesis:     Experimental; no vendor; must build to discover
Custom:      Differentiating; build or fund; proprietary advantage
Product:     Best-of-breed SaaS; buy from established vendor
Commodity:   Cloud infrastructure; use managed service; never build
```

### 7.2 Engineering Metrics & Targets

**DORA Metrics (DevOps Research and Assessment)

| Metric / 指标 | Definition / 定义 | Elite / 精英 | High / 高 | Medium / 中 | Low
|--------------|-----------------|-------------|---------|-----------|---------|
| **Deployment Frequency** | How often code deploys to production | > 1/day | 1/week–1/day | 1/month–1/week | < 1/month |
| **Lead Time for Changes** | Commit to production time | < 1 hour | 1 day–1 week | 1 week–1 month | > 1 month |
| **MTTR (Mean Time to Restore)** | Time to recover from incident | < 1 hour | < 1 day | 1 day–1 week | > 1 week |
| **Change Failure Rate** | % deploys causing incident | < 5% | 5–10% | 10–15% | > 15% |

**Engineering Health Metrics

| Metric / 指标 | Formula / 公式 | Target
|--------------|--------------|---------------|
| **Senior Engineer Attrition** | Senior departures
| **Interview-to-Offer Ratio** | Offers extended
| **Time-to-Productivity** | Days until new hire ships to production independently | < 60 days |
| **On-call Incident Load** | Incidents per engineer per week | < 2 actionable alerts |
| **PR Review Cycle Time** | Time from PR open to merge | < 4 hours (p50) |
| **Tech Debt Ratio** | Sprint capacity on debt

### 7.3 Team Topology Reference

| Team Type / 团队类型 | Focus / 职责 | Size / 规模 | Interaction Mode
|--------------------|------------|-----------|--------------------------|
| **Stream-aligned** | End-to-end business value delivery (feature squad) | 5–9 | Collaboration with platform; X-as-a-Service from platform |
| **Platform** | Internal developer platform; golden paths; reduce cognitive load | 4–8 | X-as-a-Service to stream-aligned teams |
| **Enabling** | Spread new practices (SRE, security, testing) across stream teams | 2–4 | Facilitating; time-limited engagements |
| **Complicated Subsystem** | Deep specialist work (ML pipeline, compiler, search engine) | 3–6 | X-as-a-Service; high expertise, low interaction |

### 7.4 Tech Radar Methodology

```
Adopt:   Proven, low-risk; recommend for all new projects
Trial:   Promising; use in one production project to validate
Assess:  Interesting; spike, prototype, evaluate — not production
Hold:    Avoid for new projects; migrate away from existing usage

Process:
1. Collect nominations from engineers quarterly
2. Facilitate cross-team discussion (60 min workshop)
3. Vote on quadrant placement with explicit rationale
4. Publish as internal Tech Radar document
5. Review and update every 6 months
```

---

