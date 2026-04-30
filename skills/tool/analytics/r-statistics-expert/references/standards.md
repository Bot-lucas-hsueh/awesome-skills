# Standards & Reference

## 7.1 Official Documentation

- [R Documentation](https://cran.r-project.org/manuals.html) - CRAN manuals
- [tidyverse](https://www.tidyverse.org/) - Core package documentation
- [ggplot2 Reference](https://ggplot2.tidyverse.org/reference/) - Visualization guide
- [dplyr Reference](https://dplyr.tidyverse.org/reference/) - Data manipulation
- [tidyr Reference](https://tidyr.tidyverse.org/reference/) - Data tidying
- [RStudio Cheatsheets](https://rstudio.github.io/cheatsheets/) - Quick reference cards
- [Advanced R](https://adv-r.hadley.nz/) - Programming concepts
- [R for Data Science](https://r4ds.had.co.nz/) - Comprehensive guide by Wickham

## 7.2 tidyverse Core Packages

### Installation
```r
# Install tidyverse (includes dplyr, tidyr, ggplot2, readr, purrr, tibble, stringr, forcats)
install.packages("tidyverse")

# Load all
library(tidyverse)
```

### Core Functions Reference
| Function | Package | Purpose |
|----------|---------|---------|
| `filter()` | dplyr | Subset rows |
| `select()` | dplyr | Select columns |
| `mutate()` | dplyr | Add/transform columns |
| `summarize()` | dplyr | Aggregate data |
| `group_by()` | dplyr | Group operations |
| `arrange()` | dplyr | Sort rows |
| `join_*()` | dplyr | Merge tables |
| `pivot_*()` | tidyr | Reshape data |
| `separate()` | tidyr | Split columns |
| `unite()` | tidyr | Combine columns |

## 7.3 Data Import Standards

```r
library(readr)
library(haven)

# CSV (recommended)
df <- read_csv("data.csv")
df <- read_csv("data.csv", col_types = cols(
  id = col_integer(),
  date = col_date(format = "%Y-%m-%d"),
  amount = col_double()
))

# Excel
library(readxl)
df <- read_excel("data.xlsx", sheet = "Sales", range = "A1:D100")

# SPSS/StATA/SAS
df <- read_spss("data.sav")
df <- read_dta("data.dta")
df <- read_sas("data.sas7bdat")

# Database
library(DBI)
con <- dbConnect(RPostgres::Postgres(), dbname = "sales")
df <- tbl(con, "sales") %>% collect()
```

## 7.4 Data Transformation Standards

```r
# Chained operations (magrittr/dplyr)
df %>%
  filter(status == "active") %>%
  select(id, date, amount) %>%
  mutate(
    year = year(date),
    amount_usd = amount / exchange_rate
  ) %>%
  group_by(year, category) %>%
  summarize(
    total = sum(amount_usd),
    avg = mean(amount_usd),
    .groups = "drop"
  ) %>%
  arrange(desc(total))
```

### Window Functions
```r
df %>%
  group_by(customer_id) %>%
  arrange(date) %>%
  mutate(
    running_total = cumsum(amount),
    lag_1 = lag(amount, 1),
    lead_1 = lead(amount, 1),
    pct_change = (amount - lag_1) / lag_1
  ) %>%
  ungroup()
```

## 7.5 ggplot2 Standards

```r
library(ggplot2)

# Layered grammar of graphics
ggplot(data = df, mapping = aes(x = date, y = revenue, color = category)) +
  geom_line() +
  geom_point() +
  facet_wrap(~region, scales = "free_y") +
  scale_color_brewer(palette = "Set2") +
  labs(
    title = "Revenue by Region",
    subtitle = "2024 YTD",
    x = "Date",
    y = "Revenue (USD)",
    caption = "Source: Sales Database"
  ) +
  theme_minimal() +
  theme(legend.position = "bottom")
```

### Common Geoms
| Geom | Use Case |
|------|----------|
| `geom_point()` | Scatter plots |
| `geom_line()` | Line charts |
| `geom_bar()` | Bar charts |
| `geom_histogram()` | Histograms |
| `geom_boxplot()` | Box plots |
| `geom_density()` | Density plots |
| `geom_area()` | Area charts |
| `geom_smooth()` | Trend lines |
| `geom_text()` | Labels |
| `geom_tile()` | Heatmaps |

## 7.6 Statistical Modeling Standards

```r
library(broom)

# Linear regression
model <- lm(revenue ~ age + income + education, data = df)
summary(model)

# Tidy output
tidy(model)           # coefficients
glance(model)        # model stats
augment(model)       # predictions + residuals

# Multiple models
df %>%
  group_by(category) %>%
  nest() %>%
  mutate(model = map(data, ~lm(revenue ~ age, data = .))) %>%
  mutate(tidied = map(model, tidy)) %>%
  unnest(tidied)
```

## 7.7 R Version Compatibility

| R Version | tidyverse | Key Changes |
|-----------|-----------|-------------|
| 4.4.x | 2.1.x+ | Native pipe stable |
| 4.3.x | 2.0.x+ | Lifecycle changes |
| 4.2.x | 1.8.x+ | UTF-8 improvements |
| 4.1.x | 1.7.x+ | Native pipe introduced |
| 4.0.x | 1.5.x+ | stringsAsFactors = FALSE |
