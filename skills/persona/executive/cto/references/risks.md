## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Over-Engineering** | 🔴 High | Building Kubernetes + service mesh + event sourcing for a 10-person team adds 6+ months of delay for a feature that needed 2 weeks — missed market window, competitor ships first | Validate actual scale requirements with real traffic data; start with Modular Monolith; introduce complexity only when a specific bottleneck is proven |
| **Vendor Lock-in** | 🔴 High | Deep coupling to AWS-specific services (Step Functions, DynamoDB streams, Lambda@Edge) makes migration to Azure or GCP cost $2M+ and 18+ months; discovered only when AWS raises prices or fails compliance | Use abstraction layers for all vendor-specific integrations; score each dependency by switching cost × vendor risk before adopting |
| **Technical Debt Accumulation** | 🔴 High | Skipping tests, ignoring code review standards, and deferring refactoring compounds to a 50% engineering velocity drop within 2 years — new features take 3× longer, engineers leave out of frustration | Institutionalize 20% sprint capacity for debt repayment; quantify debt in dollars monthly; make debt visible to CEO/CFO as a business cost |
| **Wrong Microservices Migration** | 🔴 High | Splitting a monolith along technical layers (not business domains) creates 30+ services with constant cross-service dependencies, 3× ops cost, and no independent deployability — all the cost, none of the benefit | Follow Domain-Driven Design bounded contexts; migrate strangler-fig pattern; measure independent deployability before declaring success |
| **Underpaying Engineers** | 🔴 High | Salary below P50 market drives 30%+ annual attrition; each senior engineer departure costs 6–12 months to backfill (recruiting + ramp time) and destroys team knowledge continuity | Benchmark quarterly against Levels.fyi, Radford; budget for annual merit + retention grants; exit interview tracking |
| **Security Vulnerability** | 🔴 High | Deferring auth hardening, secret rotation, or dependency patching ("we'll add it later") leads to production data breach → regulatory fines (GDPR: up to 4% global revenue) + customer churn + reputational damage | Embed security scanning in CI/CD; treat CVE remediation as P1; conduct quarterly threat modeling sessions |
| **Hero Engineering Culture** | 🟡 Medium | One engineer who "knows everything" fixes all incidents but blocks vacation, creates bus-factor-1 risk, and masks systemic observability failures — organization is fragile, not resilient | Enforce runbook documentation; mandate on-call rotation across 3+ engineers per system; penalize hero behavior in performance reviews |

**⚠️ IMPORTANT
- Technology strategy guidance provided here is based on general industry best practices as of 2026. Your specific regulatory environment (SOC2, HIPAA, PCI-DSS, GDPR), industry vertical, and existing system constraints must be assessed by your engineering leads and legal/compliance team before implementation.

- Build vs buy decisions and cost estimates are illustrative; validate against current vendor pricing, your team's skill set, and your specific traffic/data profile.

---
