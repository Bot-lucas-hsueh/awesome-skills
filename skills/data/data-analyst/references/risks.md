## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| Correlation ≠ Causation | 🟡 High | Observed relationship may be spurious or driven by confounders | Explicitly state "correlation" vs. "causation"; use A/B test or quasi-experiments for causation |
| P-hacking | 🟡 High | Running multiple tests until one shows p<0.05 inflates false positive rate | Pre-register hypothesis; set stopping rules before test; Bonferroni for multiple tests |
| Data Quality Assumptions | 🟡 High | Analysis on dirty data produces misleading conclusions | Run data quality checks on every dataset before analysis |
| Survivorship Bias | 🟢 Medium | Analyzing only "survivors" (active users, completed orders) skews results | Include churned users, cancelled orders in retention/funnel analysis |
| Simpson's Paradox | 🟢 Medium | Aggregate trend can reverse within subgroups | Segment analysis; watch for confounding variables |

---
