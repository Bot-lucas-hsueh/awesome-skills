# Standard Workflow

## 8.1 Development Workflow

```
Phase 1: Analysis Planning
├── Define research questions/hypotheses
├── Identify variables (IV, DV, covariates)
├── Select statistical tests (pre-registration recommended)
└── Perform power analysis (G*Power)
    └── Effect size estimate, α = 0.05, power = 0.80

Phase 2: Data Preparation
├── Import data (SPSS .sav, SAS .sas7bdat, CSV)
├── Verify variable coding (dummy variables)
├── Check for missing values (MCAR, MAR, MNAR)
│   └── Imputation if MAR: multiple imputation preferred
├── Detect outliers (boxplot, z > 3.29)
└── Assess normality (Shapiro-Wilk, Kolmogorov-Smirnov)

Phase 3: Assumption Checking
├── Normality: Shapiro-Wilk (n < 50), Kolmogorov-Smirnov (n ≥ 50)
├── Homogeneity of variance: Levene's test, Brown-Forsythe
├── Sphericity: Mauchly's test (repeated measures)
├── Independence: Durbin-Watson (regression)
├── Linearity: scatterplot matrices
├── Multicollinearity: VIF < 10, tolerance > 0.1
└── Normality of residuals (regression)

Phase 4: Analysis Execution
├── Run selected test(s)
├── Check assumption violations
│   └── Consider robust alternatives if violated
├── Report effect sizes and confidence intervals
└── Document all tests run (not just significant)

Phase 5: Reporting
├── APA 7th edition format
├── Include: statistic, df, p-value, effect size, 95% CI
└── Interpretation in plain language
```

## 8.2 Scientific Computing Workflow

### Python Statistical Analysis Pipeline
```
Phase 1: Environment Setup
├── pip install pandas scipy statsmodels pingouin
├── JupyterLab or VS Code notebooks
└── Load libraries: pandas, scipy.stats, statsmodels

Phase 2: Data Loading
├── pd.read_spss(), pd.read_sas()
├── df.describe() for initial summary
└── df.info() for data types

Phase 3: Statistical Tests
├── scipy.stats.ttest_ind() - independent t
├── scipy.stats.ttest_rel() - paired t
├── scipy.stats.f_oneway() - one-way ANOVA
├── statsmodels.stats.anova() - multi-way ANOVA
├── scipy.stats.pearsonr(), scipy.stats.spearmanr()
└── statsmodels.formula.api - regression

Phase 4: Effect Sizes
├── cohens_d from pingouin
├── eta_squared, partial_eta_squared from pingouin
└── compute_effsize() for various metrics

Phase 5: Multiple Testing Correction
├── Bonferroni: α / m
├── Benjamini-Hochberg ( FDR control)
└── Holm-Bonferroni (step-down)
```

### Example: Complete Analysis Pipeline
```python
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import pingouin as pg

# Load data
df = pd.read_spss('experiment.sav')

# Assumption checking
print("Normality (Shapiro-Wilk):")
for group in df['condition'].unique():
    subset = df[df['condition'] == group]['outcome']
    stat, p = stats.shapiro(subset)
    print(f"  {group}: W={stat:.3f}, p={p:.3f}")

# Levene's test
stat, p = stats.levene(*[df[df['condition']==g]['outcome'] 
                          for g in df['condition'].unique()])
print(f"\nLevene's test: F={stat:.3f}, p={p:.3f}")

# ANOVA with effect size
aov = pg.anova(data=df, dv='outcome', between='condition')
print(aov[['Source', 'F', 'p-unc', 'np2']])  # partial eta-squared

# Post-hoc tests (Bonferroni corrected)
posthoc = pg.pairwise_tests(data=df, dv='outcome', within='condition',
                             padjust='bonf')
print(posthoc)

# Report
print(f"\nOne-way ANOVA: F({aov['ddof1']},{aov['ddof2']}) = {aov['F'].values[0]:.2f}, "
      f"p = {aov['p-unc'].values[0]:.4f}, η²_p = {aov['np2'].values[0]:.3f}")
```

## 8.3 Document Preparation Workflow

```
Phase 1: Results Template
├── Table 1: Descriptive Statistics (M, SD, N)
├── Table 2: Correlation Matrix (if applicable)
├── Table 3: Main Analysis Results
└── Table 4: Post-hoc/Follow-up Tests

Phase 2: APA 7th Edition Formatting
├── Font: 12pt Times New Roman (or equivalent)
├── Margins: 1 inch all sides
├── Double-space throughout
├── Align left (ragged right)
├── Number pages consecutively
└── Reference style: Author, Date

Phase 3: Results Section Structure
├── Descriptive statistics first
├── State test name, variables, effect
├── Report exact statistics (not just p)
├── Include effect sizes with CIs
├── Report violations and corrections
└── Brief interpretation

Phase 4: Figure Preparation
├── Captions below figures
├── Clear axis labels with units
├── Error bars (SE or CI, specify)
├── Statistical annotations (*, **, ***)
└── High resolution (300+ dpi)
```

### APA Results Template
```
Results were analyzed using [test name]. [Variable(s)] served as the 
[dependent variable(s)], with [factor(s)] as the [independent variable(s)].

Descriptive statistics indicated that [group M] (M = X.XX, SD = X.XX) 
was [higher/lower] than [group Y] (M = X.XX, SD = X.XX).

[Test name] revealed a [significant/non-significant] [main/interaction] 
effect of [variable], F(df1, df2) = X.XX, p = .XXX, η² = .XX, 95% CI [.XX, .XX]. 
[Post-hoc/follow-up] tests indicated that [specific comparisons].
```
