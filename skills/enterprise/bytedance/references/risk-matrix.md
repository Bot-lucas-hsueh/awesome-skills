## §3. Risk Matrix

| # | Risk | Severity | Escalation Trigger | Consequence | Mitigation |
|---|------|----------|-------------------|-------------|------------|
| 1 | **Context Not Control Misuse** | 🔴 High | Leaders provide no context, just commands | Autonomy dies, speed collapses | Train leaders on context provision |
| 2 | **Data Overdose** | 🟡 Medium | Analysis paralysis from too many metrics | Slows decisions unnecessarily | Define 1-2 key metrics per decision |
| 3 | **APP Factory Waste** | 🟡 Medium | Too many experiments, no focus | Spreads resources thin | Strict OKR alignment for experiments |
| 4 | **Algorithm Tunnel Vision** | 🔴 High | Optimizing engagement over wellbeing | Regulatory risk, user churn | Balance engagement with satisfaction |
| 5 | **Speed Over Quality** | 🔴 High | Ship fast, break things repeatedly | Tech debt, reliability issues | CICD gates, rollback capability |
| 6 | **Granularity Anonymity** | 🟡 Medium | Aggregate data hides individual patterns | Miss key user segments | Always segment metrics |
| 7 | **Consensus Slowdown** | 🟡 Medium | Endless alignment meetings | Speed dies | Time-box decisions, default to action |
| 8 | **China/Global Divergence** | 🟡 Medium | Features diverge too much | Platform fragmentation | Shared core, localized surface |
| 9 | **Kill Metric Gaming** | 🔴 High | Teams optimize kill metric unethically | Wrong product decisions | Multi-metric balance, ethics review |
| 10 | **Microservices Complexity** | 🟡 Medium | 5000+ services hard to maintain | Deployment risk, debugging difficulty | Service mesh, observability |

### Escalation Protocol

| Severity | Response Time | Escalate To | Action Required |
|----------|---------------|-------------|----------------|
| 🔴 Critical | Immediate (<30min) | On-call lead + Tech Lead | Rollback if needed, assess damage |
| 🔴 High | <2 hours | Tech Lead + Product Lead | Root cause, corrective action |
| 🟡 Medium | <24 hours | Team Lead | Resolution plan, follow-up |
| 🟢 Low | Next sprint | Team Lead | Document, monitor |

---
