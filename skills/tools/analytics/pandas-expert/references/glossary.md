# Glossary

## Core DataFrame Terms

| Term | Definition |
|------|------------|
| **DataFrame** | 2D labeled data structure with rows and columns |
| **Series** | Single column of data with index |
| **Index** | Row labels for Series/DataFrame |
| **Column** | Vertical axis; contains data of one type |
| **dtype** | Data type (int64, float64, object, category, etc.) |

## Data Operations

| Term | Definition |
|------|------------|
| **Filter** | Select rows based on boolean conditions |
| **Select** | Choose specific columns |
| **Transform** | Apply function to modify values |
| **Aggregate** | Reduce rows via groupby (sum, mean, etc.) |
| **Join** | Combine DataFrames on common keys |
| **Concat** | Stack DataFrames vertically or horizontally |
| **Pivot** | Reshape from long to wide format |
| **Melt** | Reshape from wide to long format |

## Data Types

| Term | Definition |
|------|------------|
| **int64** | 64-bit integer |
| **float64** | 64-bit float (double precision) |
| **object** | Python object (strings, mixed types) |
| **category** | Categorical data with limited unique values |
| **bool** | True/False values |
| **datetime64** | Date and time values |
| **timedelta** | Duration between two datetimes |

## Aggregation Terms

| Term | Definition |
|------|------------|
| **groupby** | Group rows by one or more columns |
| **agg/aggregate** | Apply one or more functions to groups |
| **transform** | Return indexed object with same shape |
| **apply** | Apply arbitrary function to rows/columns |
| **pivot_table** | Create spreadsheet-style pivot table |
| **crosstab** | Compute cross-tabulation of two factors |

## Statistical Terms

| Term | Definition |
|------|------------|
| **describe** | Summary statistics (count, mean, std, min, 25%, 50%, 75%, max) |
| **quantile** | Value below which a given fraction falls |
| **z-score** | Standard score (value - mean) / std |
| **outlier** | Data point significantly different from others |
| **IQR** | Interquartile Range (Q3 - Q1) |
| **rolling** | Window function for time series |

## Performance Terms

| Term | Definition |
|------|------------|
| **Vectorization** | Operations applied to entire array without loops |
| **Copy-on-Write** | pandas 2.0+ optimization; avoids unnecessary copies |
| **Memory footprint** | Amount of RAM used by DataFrame |
| **Chunked processing** | Processing data in batches to reduce memory |
| **Method chaining** | Sequential .method().method() calls |

## Time Series Terms

| Term | Definition |
|------|------------|
| **DatetimeIndex** | Index with datetime values |
| **Resample** | Convert time series frequency |
| **Shift** | Move data backwards/forwards in time |
| **Rolling window** | Moving calculation across rows |
| **Lag** | Previous period value |
| **Period-over-period** | Comparison between adjacent periods |

## Common pandas Methods

| Method | Purpose |
|--------|---------|
| `read_csv()` | Load CSV files |
| `to_csv()` | Write to CSV |
| `head()` / `tail()` | First/last rows |
| `info()` | DataFrame summary |
| `describe()` | Statistical summary |
| `isnull()` | Detect missing values |
| `fillna()` | Replace missing values |
| `dropna()` | Remove missing values |
| `drop_duplicates()` | Remove duplicate rows |
| `sort_values()` | Sort by column(s) |
| `merge()` | SQL-style join |
| `concat()` | Concatenate DataFrames |
| `value_counts()` | Count unique values |
| `apply()` | Apply custom function |
| `corr()` | Correlation matrix |
