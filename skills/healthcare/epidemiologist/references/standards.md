# Standards & Reference

## 7.1 Official Documentation

- [WHO Disease Outbreak News](https://www.who.int/emergencies/disease-outbreak-news)
- [CDC MMWR Publications](https://www.cdc.gov/mmwr/)
- [WHO Field Epidemiology Manual](https://www.who.int/teams/immunization-vaccines-and-biologicals/immunization-analysis-and-insights/globalimmunization/field-epidemiology-training-program)
- [STROBE Statement (Reporting Guidelines)](https://www.strobe-statement.org/)
- [CONSORT Statement (Clinical Trials)](http://www.consort-statement.org/)
- [Epidemiologic Reviews (Oxford Academic)](https://academic.oup.com/epirev)

## 7.2 Key Epidemiological Measures

| Measure | Formula | Interpretation |
|---------|---------|----------------|
| Attack Rate | Cases/Population at risk × 1000 | Disease frequency in exposed group |
| Incidence Rate | New cases/Person-time at risk | Rate of new disease |
| Prevalence | Existing cases/Total population | Proportion with disease at a point |
| Relative Risk (RR) | Incidence exposed/Incidence unexposed | Risk ratio comparing groups |
| Odds Ratio (OR) | (a/c)/(b/d) | Approximation of RR for case-control |
| Vaccine Effectiveness | 1 - (Attack rate vaccinated/Attack rate unvaccinated) | VE % |

## 7.3 Reproductive Number Reference

| Parameter | Definition | Estimation Method |
|-----------|------------|-------------------|
| R0 | Basic reproduction number | Exponential growth method: R0 = e^(r×Tg) |
| Rt | Effective reproduction number | Wallinga-Teunis, EpiEstim (Cori method) |
| Tg | Generational time | Mean interval between infection and transmission |
| k | Dispersion parameter | Measures heterogeneity in transmission |

## 7.4 Statistical Significance Reference

| Test | Application | Assumptions |
|------|-------------|-------------|
| Chi-square | Categorical variables | Expected counts >5 per cell |
| Fisher's exact | 2×2 tables, small samples | No assumptions on expected counts |
| t-test | Comparing means | Normal distribution, equal variances |
| Mann-Whitney U | Non-parametric comparisons | Ordinal or non-normal data |
| Logistic regression | Adjusted OR for outcomes | No perfect separation |
| Cox PH regression | Survival analysis with covariates | Proportional hazards |

## 7.5 Key References

1. Giesecke J. *Modern Infectious Disease Epidemiology*. 3rd ed. CRC Press; 2022.
2. Rothman KJ, Greenland S, Lash TL. *Modern Epidemiology*. 4th ed. Wolters Kluwer; 2023.
3. WHO. *Response to Measles Outbreaks in WHO African Region, 2021-2022*. WER. 2023.
4. Cori A, et al. A new framework and software to estimate time-varying reproduction numbers during epidemics. *Am J Epidemiol*. 2013.
