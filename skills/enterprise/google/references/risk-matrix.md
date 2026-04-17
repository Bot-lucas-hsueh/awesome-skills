## §3. Risk Matrix

| # | Risk | Severity | Escalation Trigger | Consequence | Mitigation |
|---|------|----------|-------------------|-------------|------------|
| 1 | **Data-Driven Overreach** | 🟡 Medium | >2 weeks building without validation | Wasted engineering cycles | Check: Is there an experiment or metric? |
| 2 | **OKR Sandbagging** | 🔴 High | KR target set at <0.5 historical rate | Culture of low ambition | Calibrate: Require 0.7 target with evidence |
| 3 | **20% Time Disguised as 100%** | 🟡 Medium | No core OKR delivery for >1 quarter | Team velocity impact | Manager oversight; honest time tracking |
| 4 | **A/B Test Invalid Results** | 🔴 Critical | p >0.05 or sample <10K | Wrong product decisions | Statistical review gate before launch |
| 5 | **Guardrail Regression** | 🔴 Critical | Guardrail metric drops below threshold | User experience degradation | Mandatory guardrail check in launch gate |
| 6 | **Tech Debt Accumulation** | 🟡 Medium | >30% of sprint on unplanned debt | Velocity decline, outage risk | Tech Debt Tuesday; debt KR in OKR |
| 7 | **Googliness Misuse** | 🔴 High | Culture assessment used for discrimination | Legal risk, bad hires | Evidence-based; job-relevant only |
| 8 | **SLO Error Budget Exhausted** | 🔴 Critical | Error budget <10% remaining | No launches until budget recovers | Monitor error budget; pause launches |
| 9 | **On-call Burnout** | 🟡 Medium | >50% toil ratio sustained | Talent attrition | Automate toil; SRE review |
| 10 | **Scope Creep in 20% Projects** | 🟡 Medium | Project grows >3× original scope | Never ships | Set hard boundaries; MVP focus |

### Escalation Protocol

| Severity | Response Time | Escalate To | Action Required |
|----------|---------------|-------------|----------------|
| 🔴 Critical | Immediate (<1hr) | On-call lead + Tech Lead | Stop work, assess, rollback |
| 🔴 High | <4 hours | Tech Lead + Engineering Manager | Root cause analysis, corrective action |
| 🟡 Medium | <24 hours | Tech Lead | Resolution plan, follow-up |
| 🟢 Low | Next sprint planning | Team Lead | Document, monitor |

---
