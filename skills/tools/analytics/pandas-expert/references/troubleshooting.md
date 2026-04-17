# Troubleshooting Guide

## 8.1 Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `SettingWithCopyWarning` | Chained assignment on slice | Use `.loc[row_filter, col] = value` or `.copy()` |
| `ValueError: cannot merge on a column with NaN` | NaN in merge key | Fill or drop NaN before merge |
| `KeyError` | Column not found | Check column names for typos, case sensitivity |
| `AttributeError: 'DataFrame' object has no attribute 'iteritems'` | Deprecated method | Use `.items()` instead |
| `ParserError: Error tokenizing data` | CSV parsing issue | Adjust `sep`, `quotechar`, `skiprows` |
| `OutOfBoundsDatetime` | Dates outside Timestamp range | Use `pd.to_datetime(..., errors='coerce')` |

## 8.2 SettingWithCopyWarning

**Problem:** Modifying a slice without explicit copy.

```python
# Wrong
df[df['score'] > 50]['normalized'] = df['score'] / 100

# Correct - single assignment
df.loc[df['score'] > 50, 'normalized'] = df.loc[df['score'] > 50, 'score'] / 100

# Correct - explicit copy
subset = df[df['score'] > 50].copy()
subset['normalized'] = subset['score'] / 100
```

## 8.3 Performance Issues

### MemoryError on Large DataFrames
```python
# Profile memory usage
df.info(memory_usage='deep')

# Free memory
del unnecessary_df
gc.collect()

# Reduce dtype sizes
df = optimize_dtypes(df)

# Use chunked processing
chunk_size = 100000
for chunk in pd.read_csv('large.csv', chunksize=chunk_size):
    process(chunk)
```

### Slow Merge Operations
```python
# Pre-sort for faster merge
left.sort_values('key', inplace=True)
right.sort_values('key', inplace=True)

# Convert to categorical for join keys
left['key'] = left['key'].astype('category')
right['key'] = right['key'].astype('category')

# Use index merge
left.set_index('key', inplace=True)
right.set_index('key', inplace=True)
merged = left.join(right, how='left')
```

### Slow GroupBy
```python
# Use observed=True to limit categories
df.groupby('category', observed=True)['value'].sum()

# Sort groups only if needed
df.groupby('category', sort=False)['value'].sum()

# Consider agg() with single function
df.groupby('category')['value'].agg('sum')  # faster than .sum()
```

## 8.4 Data Quality Issues

### Handling Mixed Types in Column
```python
# Detect
print(df['col'].apply(type).value_counts())

# Convert with coercion
df['col'] = pd.to_numeric(df['col'], errors='coerce')

# Parse mixed format
df['col'] = df['col'].apply(lambda x: float(x) if isinstance(x, (int, float)) else np.nan)
```

### Datetime Parsing Failures
```python
# Find problematic values
bad_dates = df[pd.to_datetime(df['date'], errors='coerce').isna()]

# Parse with format hint
df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=False)

# Handle timezone
df['date'] = pd.to_datetime(df['date']).dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
```

### Duplicate Rows
```python
# Find duplicates
duplicates = df[df.duplicated(subset=['id'], keep=False)]

# Remove (keep first/last)
df.drop_duplicates(subset=['id'], keep='first', inplace=True)

# Remove all duplicates of a subset
df = df.drop_duplicates(keep=False)
```

## 8.5 Debugging DataFrame State

```python
# Shape
print(f"Shape: {df.shape}")

# Data types
print(df.dtypes)

# Missing values
print(df.isnull().sum())
print(df.isnull().mean())

# Sample
print(df.sample(5))

# Stats
print(df.describe())
```

## 8.6 Performance Checklist

- [ ] Use `observed=True` in groupby with categorical columns
- [ ] Avoid `apply()` when vectorized alternatives exist
- [ ] Use `inplace=True` only when memory is constrained
- [ ] Prefer `query()` for complex boolean filters
- [ ] Use `named_tuple()` for function returns
- [ ] Enable PyArrow backend for string operations (pandas 2.0+)
- [ ] Consider `pd.eval()` for large expressions
