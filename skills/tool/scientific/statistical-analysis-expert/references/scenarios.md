# Scenario Examples

## 9.1 Scientific Scenarios

### 9.1.1 Clinical Trial Analysis

**User:** "Analyze a randomized controlled trial comparing two treatments for blood pressure reduction"

**Statistical Analysis Expert:**
> **Independent Samples T-Test (or ANCOVA with baseline):**
> 
> **Assumptions:**
> 1. Normality: Shapiro-Wilk per group (n = 45 per group)
> 2. Equal variances: Levene's test
> 3. Independence: RCT design ensures
> 
> **SPSS Syntax:**
> ```spss
> T-TEST GROUPS=treatment(1,2)
>   /VARIABLES=bp_reduction
>   /CRITERIA=CI(.95).
> 
> * For ANCOVA controlling for baseline:
> UNIANOVA bp_reduction BY treatment WITH baseline_bp
>   /PRINT=DESCRIPTIVE PARAMETER ESTIMATE OMEGA
>   /DESIGN=treatment baseline_bp.
> ```
> 
> **Results:**
> Treatment A (M = -12.3 mmHg, SD = 6.2) vs Treatment B (M = -8.7 mmHg, SD = 5.8)
> t(88) = 2.84, p = .005, d = 0.60, 95% CI [-6.2, -1.1]
> Treatment A produced significantly greater BP reduction.

### 9.1.2 Survey Research Analysis

**User:** "Analyze survey data with weighted responses accounting for complex sampling design"

**Statistical Analysis Expert:**
> **Complex Samples Analysis:**
> 
> | Step | SPSS | Purpose |
> |-----|------|---------|
> | 1 | Define complex sample | Specify cluster, strata, weights |
> | 2 | Descriptives with weights | Population estimates |
> | 3 | Chi-square test | Association between categorical |
> | 4 | Logistic regression | Predict binary outcome |
> 
> ```spss
> CSPLAN ANALYSIS
>   /PLAN FILE='sample.csplan'
>   /PLAN VARS ADMINISTRATIVE = TRUE
>   /DESIGN CLUSTER=stratum*cluster
>   /WEIGHT WEIGHT=final_weight.
> 
> CSTABULATE
>   /TABLES VARIABLES=education BY satisfaction
>   /STATISTICS=COUNT ROWPCT
>   /MISSING SCOPE=TABLE CLASSMISSING=EXCLUDE.
> 
> CSLOGISTIC satisfaction WITH age income education
>   /PLAN FILE='sample.csplan'
>   /MODEL education income age
>   /ODDSRATIO COVB.
> ```

## 9.2 Data Analysis Workflows

### 9.2.1 Regression Analysis Pipeline
```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load data
df = pd.read_csv('research_data.csv')

# Prepare variables
X = df[['predictor1', 'predictor2', 'predictor3', 'covariate1']]
y = df['outcome']

# Check multicollinearity
vif = pd.DataFrame()
vif['VIF'] = [variance_inflation_factor(X.values, i) 
              for i in range(X.shape[1])]
vif['Variable'] = X.columns
print(vif)  # VIF > 10 indicates multicollinearity

# Add constant for intercept
X = sm.add_constant(X)

# Fit model
model = sm.OLS(y, X).fit()
print(model.summary())

# Check assumptions
residuals = model.resid
fitted = model.fittedvalues

# Normality of residuals
from scipy.stats import shapiro
stat, p = shapiro(residuals)
print(f"Shapiro-Wilk: W={stat:.3f}, p={p:.3f}")

# Heteroscedasticity (Breusch-Pagan)
from statsmodels.stats.diagnostic import het_breuschpagan
stat, p, f, fp = het_breuschpagan(residuals, X)
print(f"Breusch-Pagan: LM={stat:.3f}, p={p:.3f}")

# Report
print(f"\nRegression: R² = {model.rsquared:.3f}, "
      f"F({model.df_resid:.0f},{model.df_model:.0f}) = {model.fvalue:.2f}, "
      f"p < .001")
```

### 9.2.2 Repeated Measures Analysis
```python
import pingouin as pg

# Wide format for repeated measures
df_wide = df.pivot(index='subject', columns='time', values='measurement')

# Repeated measures ANOVA
aov = pg.rm_anova(data=df, dv='measurement', within='time', 
                   subject='subject', detailed=True)
print(aov)

# Pairwise comparisons with correction
pw = pg.pairwise_tests(data=df, dv='measurement', within='time',
                        subject='subject', padjust='bonf')
print(pw)

# Effect size (generalized eta-squared)
print(f"η²_G = {aov.loc[0, 'ng2']:.3f}")

# Mauchly's test for sphericity
sphericity = pg.sphercity_mauchly(data=df, dv='measurement', 
                                   within='time', subject='subject')
print(sphericity)
# If p < .05, use corrected values (Greenhouse-Geisser or Huynh-Feldt)
```

## 9.3 Publication Workflows

### 9.3.1 Power Analysis
```python
from statsmodels.stats.power import TTestIndPower, FTestPower

# Independent t-test power analysis
analysis = TTestIndPower()
n = analysis.solve_power(effect_size=0.5, alpha=0.05, power=0.80,
                          ratio=1, alternative='two-sided')
print(f"Required n per group: {n:.1f}")

# One-way ANOVA power analysis
from statsmodels.stats.power import FTestAnovaPower
anova_power = FTestAnovaPower()
n_total = anova_power.solve_power(effect_size=0.25, alpha=0.05, 
                                   power=0.80, k_groups=3)
print(f"Required total n: {n_total:.1f}")
```

### 9.3.2 Publication-Ready Tables

```python
# Create descriptive statistics table
def create_desc_table(df, group_var, dep_vars):
    rows = []
    for var in dep_vars:
        for group in df[group_var].unique():
            subset = df[df[group_var] == group][var]
            rows.append({
                'Variable': var,
                'Group': group,
                'n': len(subset),
                'M': subset.mean(),
                'SD': subset.std(ddof=1),
                'Mdn': subset.median(),
                'IQR': f"[{subset.quantile(0.25):.2f}, {subset.quantile(0.75):.2f}]"
            })
    return pd.DataFrame(rows)

desc_table = create_desc_table(df, 'condition', ['score', 'reaction_time'])
print(desc_table.to_markdown(index=False))
```

### 9.3.3 Multi-Study Reporting Template
```
Study 1 and Study 2 preregistered at OSF (https://osf.io/xxxxx).

Study 1: N = 120, power = .95, G*Power 3.1
Study 2: N = 85, sensitivity = .90 (Bentler & Chou, 1987)

Meta-analysis across studies (Study 1, 2, 3):
Random-effects model, k = 3, N = 412
Effect: r = .34, 95% CI [.21, .47], p < .001
Heterogeneity: Q(2) = 2.34, p = .31, I² = 14.5%
```
