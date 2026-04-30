# Glossary

## R Core Concepts

| Term | Definition |
|------|------------|
| **Object** | Data structure in R (vector, list, data.frame, etc.) |
| **Vector** | 1D sequence of same-type elements |
| **Factor** | Categorical data with levels |
| **Data frame** | 2D table with columns of potentially different types |
| **Tibble** | Modern data frame (tidyverse) |
| **Function** | Reusable code block |
| **Package** | Collection of functions and data |
| **Library** | Directory containing installed packages |
| **Namespace** | Package function scope |

## tidyverse Terms

| Term | Definition |
|------|------------|
| **Pipe (`%>%` / `\|>`)** | Pass output of one function as input to next |
| **Verb** | dplyr function (filter, mutate, summarize) |
| **Tidy data** | Each column is a variable, each row is an observation |
| **NSE** | Non-standard evaluation; bare column names |
| **Tidy evaluation** | Framework for NSE with `!!`, `{{}}`, `.data` |
| **Mask** | Search path for variable names |

## Data Manipulation Terms

| Term | Definition |
|------|------------|
| **Filter** | Keep rows matching condition |
| **Select** | Choose columns by name or pattern |
| **Mutate** | Add or transform columns |
| **Summarize** | Reduce to summary statistics |
| **Group** | Partition data for group-wise operations |
| **Arrange** | Sort rows |
| **Join** | Combine tables by matching keys |
| **Pivot** | Reshape between wide and long formats |

## Statistical Terms

| Term | Definition |
|------|------------|
| **Mean** | Average; sum divided by count |
| **Median** | Middle value when sorted |
| **Standard deviation** | Spread of values around mean |
| **Variance** | Square of standard deviation |
| **Correlation** | Linear relationship strength |
| **Regression** | Modeling relationship between variables |
| **Residual** | Difference between predicted and actual |
| **p-value** | Probability of observing data given null hypothesis |

## ggplot2 Terms

| Term | Definition |
|------|------------|
| **Aesthetic** | Visual property mapped to data (x, y, color, size) |
| **Geom** | Geometric object (point, line, bar) |
| **Facet** | Split into multiple plots |
| **Scale** | Map data values to aesthetic values |
| **Theme** | Non-data visual styling |
| **Layer** | Data + aesthetic + geom + stat |
| **Stat** | Statistical transformation |
| **Coordinate system** | Cartesian, polar, map projections |

## Statistical Tests

| Test | Purpose |
|------|---------|
| **t-test** | Compare means of two groups |
| **ANOVA** | Compare means of 3+ groups |
| **Chi-square** | Test independence of categorical variables |
| **Correlation** | Measure linear relationship |
| **Linear regression** | Model continuous outcome |
| **Logistic regression** | Model binary outcome |
| **Wilcoxon/Mann-Whitney** | Non-parametric comparison |
| **Kruskal-Wallis** | Non-parametric ANOVA |

## Modeling Terms

| Term | Definition |
|------|------------|
| **Formula** | `y ~ x1 + x2` notation |
| **Predictor** | Independent variable (x) |
| **Response** | Dependent variable (y) |
| **Coefficient** | Estimated effect size |
| **Intercept** | Expected value when predictors = 0 |
| **R-squared** | Variance explained by model |
| **AIC/BIC** | Model selection criteria |
| **Cross-validation** | Model validation technique |

## Programming Terms

| Term | Definition |
|------|------------|
| **Function** | Reusable code block |
| **Argument** | Input to function |
| **Return value** | Output of function |
| **Loop** | Repeat code (for, while) |
| **Conditional** | Branch on condition (if/else) |
| **Vectorization** | Apply function to vector element-wise |
| **List** | Container for mixed objects |
| **S3/S4/R6** | Object systems in R |

## String Manipulation Terms

| Term | Definition |
|------|------------|
| **str_detect** | Test if pattern exists |
| **str_extract** | Pull out matched pattern |
| **str_replace** | Replace matched pattern |
| **str_split** | Split string into parts |
| **str_c** | Concatenate strings |
| **Regex** | Pattern for text matching |

## Date/Time Terms

| Term | Definition |
|------|------------|
| **POSIXct** | Date-time as numeric |
| **Date** | Date without time |
| **ymd/hms** | Parse year-month-day, hour-minute-second |
| **interval** | Period between two dates |
| **duration** | Exact time span |
| **period** | Human-readable time span |
| **lag** | Previous value |
| **lead** | Next value |
