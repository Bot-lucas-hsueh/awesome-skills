## § 7 · Standards & Reference

### Statistical Method Selection Guide

| Data Type | Groups | Design | Method |
|-----------|--------|--------|--------|
| Continuous, normal | 2 | Independent | Two-sample t-test |
| Continuous, normal | 2 | Paired | Paired t-test |
| Continuous, non-normal | 2 | Independent | Mann-Whitney U |
| Continuous, normal | >2 | Independent | One-way ANOVA + post-hoc |
| Continuous | >2 | Repeated measures | Repeated measures ANOVA or LME |
| Continuous | — | Predictor relationship | Linear regression |
| Binary outcome | — | Predictor relationship | Logistic regression |
| Count data | — | Predictor relationship | Poisson/Negative Binomial |
| Time-to-event | 2+ | Survival comparison | Kaplan-Meier + log-rank |
| Time-to-event | — | Predictor effect | Cox proportional hazards |
| Hierarchical/clustered | — | Nested observations | Mixed-effects model (lme4) |
| Bayesian estimation | Any | Any | Bayesian model (brms/PyMC) |

### Multiple Testing Correction

```r
# Bonferroni (FWER control) — conservative; use when any false positive is costly
p_bonferroni <- p.adjust(p_values, method = "bonferroni")
# Threshold: p_bonferroni < 0.05 → family-wise error rate controlled at 0.05

# Benjamini-Hochberg FDR — less conservative; use in discovery/screening contexts
p_fdr <- p.adjust(p_values, method = "BH")
# Threshold: p_fdr < 0.05 → expected false discovery rate = 5%

# When to use which:
# Bonferroni: confirmatory tests; any single false positive has consequences
# BH-FDR: exploratory screening (gene expression, GWAS, metabolomics)
# Holm: step-down method; less conservative than Bonferroni; use for pairwise comparisons
```

### Common Effect Sizes

| Test | Effect Size | Interpretation |
|------|-------------|---------------|
| t-test
| ANOVA (η²) | eta-squared | 0.01 = small, 0.06 = medium, 0.14 = large |
| Correlation | r | 0.1 = small, 0.3 = medium, 0.5 = large |
| Chi-square | Cramér's V | 0.1 = small, 0.3 = medium, 0.5 = large |
| Logistic regression | Odds Ratio | OR=1.5 modest, OR=2 moderate, OR>3 strong |
| Survival | Hazard Ratio | HR>1 increases risk; HR<1 is protective |

---
