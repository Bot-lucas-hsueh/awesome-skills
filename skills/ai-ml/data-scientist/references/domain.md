## § 6 · Domain Knowledge

### 6.1 Statistical Test Selection

| Scenario | Test | Assumptions |
|----------|------|-------------|
| Compare means (2 groups) | t-test | Normality, equal variance |
| Compare means (>2 groups) | ANOVA | Normality, homogeneity |
| Non-parametric | Mann-Whitney U | No distribution assumption |
| Categorical association | Chi-square | Expected counts > 5 |
| Correlation | Pearson/Spearman | Linear/monotonic relationship |

### 6.2 Model Selection Guide

| Problem | Algorithm | When to Use |
|---------|-----------|-------------|
| Tabular data | XGBoost/LightGBM | Interpretability, speed |
| Linear relationships | Linear/Logistic Regression | Baseline, explainability |
| Image/text | CNN/Transformer | Complex patterns |
| Small data | Random Forest | Robust, less overfitting |
| Time series | ARIMA, Prophet | Temporal patterns |

### 6.3 A/B Testing Checklist

- [ ] Randomization unit defined (user, session, request)
- [ ] Sample size calculated (power analysis)
- [ ] Success metric defined (primary, secondary)
- [ ] Running time covers business cycles
- [ ] Sanity checks on invariant metrics
- [ ] Multiple comparison correction if needed

---
