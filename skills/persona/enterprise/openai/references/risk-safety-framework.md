## § 9 — Risk & Safety Framework

| Risk | Severity | Mitigation | Escalation |
|------|----------|------------|------------|
| Misaligned capabilities | 🔴 Critical | RLHF + Constitutional AI; red-teaming | Safety team review before training >100B |
| Jailbreak exploitation | 🔴 Critical | Classifier filters; refusal tuning | Immediate deployment halt if widespread |
| Deceptive alignment | 🔴 High | Interpretability research; evals | Safety committee review |
| Misuse (CBRN, cyber) | 🔴 Critical | Preparedness Framework; TEFP | Conditional deployment; external review |
| Reward hacking | 🔴 High | Diverse preference data; regularization | Pause training if detected |
| Emergent misbehavior | 🟠 High | Continuous evals; staged deployment | Immediate review; deployment halt |

**Preparedness Framework (Track, Evaluate, Forecast, Protect):**

| Risk Category | Low | Medium | High | Critical |
|--------------|-----|--------|------|----------|
| Cybersecurity | Standard measures | Enhanced monitoring | Conditional deployment | Deployment pause |
| CBRN | Standard measures | Specialist access | Strict controls | No deployment |
| Persuasion | Standard measures | Content labeling | Usage restrictions | Deployment pause |
| Model Autonomy | Standard measures | Capability ceilings | Strict constraints | No deployment |

---
