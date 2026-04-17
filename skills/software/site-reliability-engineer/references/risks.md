## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Alert Fatigue** | 🔴 Critical | Too many alerts → real issues ignored | Alert on symptoms, page sparingly |
| **Missing Observability** | 🔴 Critical | Can't debug without logs/traces | OpenTelemetry, structured logging |
| **Automation Failure** | 🟠 High | Self-healing makes things worse | Circuit breakers on automation |
| **Chaos in Production** | 🟠 High | Uncontrolled failure injection | Safety checks, blast radius limits |
| **Toil Overload** | 🟠 High | Team drowning in manual work | Toil budget, automation investment |
| **SLO Misalignment** | 🟡 Medium | Wrong metrics drive wrong behavior | User-centric SLIs, regular review |

---
