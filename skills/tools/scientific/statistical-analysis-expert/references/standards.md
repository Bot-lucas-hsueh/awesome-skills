# Standards & Reference

## 7.1 Official Documentation

- [SPSS Statistics Documentation](https://www.ibm.com/docs/en/spss-statistics)
- [SAS Documentation](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.5/home.htm)
- [SPSS Syntax Reference](https://www.ibm.com/docs/en/spss-statistics/29.0.0)
- [SAS/STAT Procedures](https://www.ibm.com/docs/en/spss-statistics/29.0.0)
- [G*Power Manual](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower)
- [APA Style Guidelines](https://apastyle.apa.org/)

## 7.2 Reference Tables

### Common Statistical Tests

| Test | When to Use | Assumptions | Effect Size |
|------|-------------|-------------|-------------|
| Independent t-test | 2 independent groups | Normal, equal variance | Cohen's d |
| Paired t-test | Matched/paired data | Normal differences | Cohen's d_z |
| One-way ANOVA | 3+ independent groups | Normal, equal variance | η², ω² |
| Repeated measures ANOVA | Within-subjects design | Sphericity | η²_p |
| Chi-square (χ²) | Categorical variables | Expected ≥ 5 per cell | Cramér's V, φ |
| Pearson correlation | Linear relationship | Bivariate normal | r |
| Spearman correlation | Ranked/ordinal data | Monotonic relationship | ρ |
| Mann-Whitney U | Non-normal 2 groups | Ordinal/continuous | r (rank-biserial) |
| Kruskal-Wallis H | Non-normal 3+ groups | Ordinal/continuous | ε² |
| Wilcoxon signed-rank | Non-normal paired | Symmetric differences | r |

### Regression Models

| Model | Outcome | Predictors | SAS Procedure |
|-------|---------|------------|---------------|
| Linear regression | Continuous | Continuous/Categorical | PROC REG |
| Logistic regression | Binary | Mixed | PROC LOGISTIC |
| Poisson regression | Count | Mixed | PROC GENMOD |
| Cox regression | Time-to-event | Mixed | PROC PHREG |
| Mixed models | Repeated | Nested | PROC MIXED |
| GEE | Correlated | Mixed | PROC GENMOD |

### Effect Size Interpretation

| Effect Size | Small | Medium | Large |
|-------------|-------|--------|-------|
| Cohen's d | 0.2 | 0.5 | 0.8 |
| r (correlation) | 0.1 | 0.3 | 0.5 |
| η² (eta-squared) | 0.01 | 0.06 | 0.14 |
| η²_p (partial eta²) | 0.06 | 0.14 | 0.20 |
| ω² (omega-squared) | 0.01 | 0.06 | 0.14 |
| f (Cohen's) | 0.10 | 0.25 | 0.40 |
| Cramér's V (2×2) | 0.1 | 0.3 | 0.5 |
| Cramér's V (4×4) | 0.07 | 0.21 | 0.35 |

## 7.3 Common Patterns

### SPSS: Independent Samples T-Test
```spss
T-TEST GROUPS=condition(0,1)
  /VARIABLES=score
  /CRITERIA=CI(.95).
```

### SPSS: One-Way ANOVA with Post-Hoc
```spss
ONEWAY score BY group
  /STATISTICS=DESCRIPTIVES HOMOGENEITY
  /POSTHOC=TUKEY BONFERRONI
  /CRITERIA=ALPHA(.05).
```

### SPSS: Linear Regression
```spss
REGRESSION
  /DEPENDENT outcome
  /METHOD=ENTER predictor1 predictor2
  /STATISTICS=COEFF OUTS R ANOVA COLLIN TOL
  /SCATTERPLOT=(*ZRESID,*ZPRED).
```

### SAS: Logistic Regression
```sas
PROC LOGISTIC DATA=mydata;
  MODEL event(IN='1') = age treatment dose / CTABLE PPROB=(0.5);
  ODDSRATIO 'Treatment Effect' DIFF=REF;
RUN;
```

### SAS: Mixed Model
```sas
PROC MIXED DATA=longitudinal;
  CLASS subject time condition;
  MODEL y = time condition time*condition / SOLUTION;
  REPEATED time / TYPE=AR(1) SUBJECT=subject;
RUN;
```

## 7.4 Version Compatibility

| SPSS Version | SAS Version | Key Features |
|--------------|-------------|--------------|
| 28.0 | 9.4 M7 | Updated GLM, enhanced output |
| 29.0 | 9.4 M8 | New charts, Python integration |
| 30.0 | 9.4 M9 | Mixed models improvements |
| 31.0 | 9.4 M10 | Enhanced Bayesian |

| Procedure | Min SPSS | Min SAS | Notes |
|-----------|----------|---------|-------|
| GENLINMIXED | 25 | 9.3 | Mixed models |
| Bayesian T-tests | 26 | 9.4 | Bayesian statistics |
| Robust standard errors | 27 | 9.4 | Eicker-Huber-White |
| Exact tests | 25 | 9.4 | EXACT procedure |
