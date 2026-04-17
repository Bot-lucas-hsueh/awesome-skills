# Common Pitfalls & Anti-Patterns

## 10.1 Common Statistical Mistakes

| # | Anti-Pattern | Severity | Impact | Quick Fix |
|---|--------------|----------|--------|-----------|
| 1 | **p-hacking** | 🔴 High | False positives | Pre-register hypotheses |
| 2 | **p-value only reporting** | 🔴 High | Incomplete evidence | Include effect size + CI |
| 3 | **Wrong test selection** | 🔴 High | Invalid conclusions | Use decision tree |
| 4 | **Ignoring assumptions** | 🔴 High | Inflated Type I/II error | Test assumptions first |
| 5 | **Multiple comparisons** | 🔴 High | Inflated α | Apply correction (Bonferroni, BH) |
| 6 | **Correlation = causation** | 🔴 High | Wrong interpretation | Control for confounders |
| 7 | **Ignoring effect size** | 🔴 High | Practical insignificance | Report and interpret |

### Examples

```spss
* WRONG: Report p only
GET FILE='study.sav'.
T-TEST GROUPS=group(1,2) /VARIABLES=outcome.
* Reports: t(48) = 2.14, p = .038

* CORRECT: Report with effect size and CI
* Cohen's d = (M1 - M2) / SD_pooled
* 95% CI using non-central t distribution
```

```python
# WRONG: Multiple t-tests on same data
from scipy import stats
for g1, g2 in combinations(groups, 2):
    t, p = stats.ttest_ind(data[g1], data[g2])
    if p < 0.05:
        print(f"Significant: {g1} vs {g2}")

# CORRECT: One-way ANOVA + post-hoc with correction
from scipy import stats
f, p_anova = stats.f_oneway(*[data[g] for g in groups])
# Post-hoc with Bonferroni
from statsmodels.stats.multicomp import pairwise_tukeyhsd
posthoc = pairwise_tukeyhsd(data, groups, alpha=0.05)
```

## 10.2 Assumption Violations

| # | Violation | Detection | Robust Alternative |
|---|-----------|-----------|-------------------|
| 1 | Non-normality | Shapiro-Wilk, KS test | Mann-Whitney U, Wilcoxon |
| 2 | Unequal variances | Levene's, Brown-Forsythe | Welch's t, Games-Howell |
| 3 | Non-sphericity | Mauchly's test | Greenhouse-Geisser correction |
| 4 | Outliers | Boxplot, z > 3.29 | Robust regression, trimming |
| 5 | Heteroscedasticity | Breusch-Pagan, residual plots | HC standard errors |

### Examples

```spss
* WRONG: Using standard t-test without checking
T-TEST GROUPS=group(1,2) /VARIABLES=outcome.

* CORRECT: Check assumptions first
EXAMINE VARIABLES=outcome BY group
  /PLOT BOXPLOT STEMLEAF NPPLOT
  /STATISTICS LEVENE
  /GROUPS=group.

* If violated, use robust alternative
NPAR TESTS MANN-WHITNEY=outcome BY group(1,2).
```

```python
# WRONG: Linear regression without checking
model = sm.OLS(y, X).fit()

# CORRECT: Check all assumptions
# 1. Normality of residuals
sm.qqplot(model.resid, line='45')
stat, p = shapiro(model.resid)

# 2. Heteroscedasticity
from statsmodels.stats.diagnostic import het_breuschpagan
stat, p, _, _ = het_breuschpagan(model.resid, model.exog)

# 3. Multicollinearity
vif = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

# If violations, use robust regression
from statsmodels.robust.robust_linear_model import RLM
robust_model = RLM(y, X, M=HubT()).fit()
```

## 10.3 Reporting Errors

| # | Anti-Pattern | Severity | Correct Format |
|---|--------------|----------|----------------|
| 1 | **Rounding errors** | 🟡 Medium | Round to 2-3 decimals |
| 2 | **df errors** | 🟡 Medium | Know when to use N-1 vs N-k |
| 3 | **Missing degrees of freedom** | 🔴 High | t(df), F(df1,df2), χ²(df) |
| 4 | **No CI reported** | 🔴 High | Always include 95% CI |
| 5 | **Exact p for large samples** | 🟡 Medium | p < .001 for p < 10⁻⁴ |

### APA 7th Edition Examples

```
❌ "The difference was significant (t = 2.5, p < .05)"
✅ "The treatment group scored significantly higher (M = 85.2, SD = 8.3) than 
    the control group (M = 76.8, SD = 9.1), t(58) = 3.45, p = .001, d = 0.89, 
    95% CI [4.2, 12.6]."

❌ "ANOVA showed significant results (F = 4.56, p = .02)"
✅ "A one-way ANOVA revealed a significant main effect of condition on task 
    performance, F(2, 87) = 4.56, p = .013, η² = .095, 95% CI [.012, .189]."

❌ "Chi-square test was significant (χ² = 12.5)"
✅ "A chi-square test of independence indicated a significant association 
    between education level and voting behavior, χ²(2, N = 245) = 12.45, 
    p = .002, Cramér's V = .22, 95% CI [.09, .35]."
```

## 10.4 Study Design Anti-Patterns

```
❌ Small sample + many tests = "fishing expedition"
✅ Power analysis → adequate sample → pre-registered tests

❌ Post-hoc grouping of continuous variable
✅ Theory-driven binning, or treat as continuous

❌ Dropping outliers without justification
✅ Report sensitivity analyses with/without outliers

❌ Ignoring missing data mechanism
✅ MCAR: listwise deletion acceptable
    MAR: multiple imputation recommended
    MNAR: sensitivity analysis required

❌ HARKing (Hypothesizing After Results are Known)
✅ Pre-register primary and secondary hypotheses
```
