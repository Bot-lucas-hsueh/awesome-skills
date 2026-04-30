# Troubleshooting Guide

## 8.1 Common R Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `Error: unexpected '>'` | Missing parenthesis or quote | Check syntax; use RStudio indent |
| `object 'x' not found` | Variable not in scope | Load library or check spelling |
| `non-numeric argument to binary operator` | Type mismatch | Convert with `as.numeric()`, `as.Date()` |
| `Error in select()` | Column doesn't exist | Use `names(df)` to check; check quotes |
| `Error in mutate()` | Invalid transformation | Check expression syntax |
| `!obj is TRUE` | Unexpected FALSE | Check condition logic |
| `cannot open file` | File path issue | Use `file.choose()` or full path |

## 8.2 Package Issues

### Installation Failures
```r
# Update R and all packages
install.packages("updateR")

# Fix common issues
install.packages("remotes")
remotes::install_github("owner/repo")  # GitHub packages

# Binary vs source
install.packages("pkg", type = "binary")  # Windows/Mac

# Missing system dependency (Linux)
sudo apt-get install libcurl4-openssl-dev
sudo apt-get install libssl-dev
```

### Namespace Conflicts
```r
# Explicit namespace
dplyr::filter(df, condition)
stats::filter(df, condition)

# Check what's loaded
search()

# Detach conflicting package
detach("package:pkgname", unload = TRUE)
```

## 8.3 Data Issues

### tibble Printing Issues
```r
# Show all columns
print(df, width = Inf)

# Show all rows
print(df, n = Inf)

# Set global option
options(tibble.print_min = 50, tibble.width = Inf)
```

### Type Conversion Problems
```r
# Detect types
str(df)
typeof(df$column)
class(df$column)

# Safe conversion
df$column <- as.numeric(as.character(df$column))
df$date <- lubridate::ymd(df$date)

# Handle NAs in conversion
df$column <- suppressWarnings(as.numeric(df$column))
```

### Handling Missing Values
```r
# Detect NAs
is.na(df)
sum(is.na(df))
colSums(is.na(df))

# Filter NAs
df %>% filter(!is.na(column))
df %>% drop_na(column)

# Replace NAs
df %>% replace_na(list(column = 0, other = "unknown"))

# Fill NAs
df %>% fill(column, .direction = "down")

# Impute with median
df %>% mutate(column = coalesce(column, median(column, na.rm = TRUE)))
```

## 8.4 Performance Issues

### Slow Data Manipulation
```r
# Use data.table for large data
library(data.table)
dt <- fread("large.csv")  # 10x faster than read_csv

# Fast grouping
dt[, .(total = sum(amount)), by = category]

# Convert back to tibble if needed
df <- as_tibble(dt)
```

### Memory Issues
```r
# Check memory
gc()
memory.size()

# Clear objects
rm(large_df)
gc()

# Use on-disk data
library(arrow)
df <- open_dataset("data.parquet")
```

### Slow ggplot2
```r
# For millions of points, sample first
df_sample <- df %>% sample_n(10000)

# Disable legend recalculation
ggplot(df_sample, aes(...)) + 
  guides(color = "none") +
  theme(legend.position = "none")
```

## 8.5 join Troubleshooting

### join Issues
```r
# Check for type mismatch in keys
df1$id <- as.character(df1$id)
df2$id <- as.character(df2$id)

# Handle NA in keys
df1 %>% 
  filter(!is.na(key)) %>%
  left_join(df2, by = "key")

# Multiple keys
left_join(df1, df2, by = c("key1", "key2"))

# Rename conflicting columns
left_join(df1, df2, by = c("id" = "id2", "key" = "key2"))
```

### Unexpected Row Count
```r
# Many-to-many join causes row explosion
# Check cardinality first
count(df1, key) %>% filter(n > 1)
count(df2, key) %>% filter(n > 1)

# Deduplicate before join
df1_unique <- df1 %>% distinct(key, .keep_all = TRUE)
```

## 8.6 Statistical Issues

### Model Convergence
```r
# Check for perfect separation
table(df$outcome, df$predictor)

# Scale predictors
df <- df %>% mutate_at(vars(x1, x2), scale)

# Try different optimizer
glm(outcome ~ ., data = df, family = binomial(), control = glm.control(maxit = 100))
```

### Heteroscedasticity
```r
# Detect
plot(model, which = 1)

# Robust standard errors
library(sandwich)
library(lmtest)
coeftest(model, vcov = vcovHC(model))
```

## 8.7 RStudio Debugging

```r
# Browser for interactive debugging
browser()

# Trace error
traceback()

# Print statements
message("Debug: x = ", x)
cat("Value:", value, "\n")

# Options
options(error = recover)  # Enter debugger on error
```
