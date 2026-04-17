## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Overfitting** | 🔴 Critical | Model memorizes training data | Cross-validation, regularization, holdout |
| **Selection Bias** | 🔴 Critical | Non-representative sample | Random sampling, propensity matching |
| **P-Hacking** | 🟠 High | Multiple testing, cherry-picking | Pre-registration, Bonferroni correction |
| **Data Leakage** | 🟠 High | Future information in training | Time-aware splits, feature inspection |
| **Confounding Variables** | 🟠 High | Unmeasured factors explain correlation | Causal inference, randomization |
| **Algorithmic Bias** | 🟡 Medium | Model discriminates unfairly | Fairness metrics, disparate impact |

---
