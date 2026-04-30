## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| Method Misspecification | 🟡 High | Wrong statistical method → invalid conclusions | Always verify assumptions; choose method based on data structure |
| P-hacking
| Overfitting | 🟡 High | Model fits sample perfectly but generalizes poorly | Cross-validation; regularization; report out-of-sample performance |
| Confounding in Observational Studies | 🟡 High | Observed association may be caused by third variable | Control for confounders; use causal inference methods; disclose limitations |
| Misinterpretation of p-value | 🟢 Medium | p-value ≠ probability hypothesis is true; p-value ≠ effect size | Always pair with effect size and CI; educate collaborators on correct interpretation |

---
