# Standards & Reference

## 7.1 Official Documentation

- [pandas Documentation](https://pandas.pydata.org/docs/) - Official pandas docs
- [pandas API Reference](https://pandas.pydata.org/docs/reference/index.html) - All functions and classes
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html) - Tutorials and guides
- [PyData YouTube](https://www.youtube.com/c/PyData) - Conference talks and tutorials

## 7.2 Essential Configuration

### dtype Optimization Standards
```python
import pandas as pd
import numpy as np

# Memory-efficient dtypes
def optimize_dtypes(df):
    for col in df.select_dtypes(include=['int64']).columns:
        if df[col].min() >= 0:
            if df[col].max() < 65535:
                df[col] = df[col].astype('uint16')
        elif df[col].min() > -32768 and df[col].max() < 32767:
            df[col] = df[col].astype('int16')
    for col in df.select_dtypes(include=['float64']).columns:
        df[col] = df[col].astype('float32')
    return df

# Categorical for low-cardinality strings
df['status'] = df['status'].astype('category')

# String dtype (pandas 2.0+)
df['name'] = df['name'].astype('string')
```

### Display Settings
```python
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 100)
pd.set_option('future.infer_string', True)
```

## 7.3 Common Operations Reference

### Read Operations
```python
# CSV with dtype specs
df = pd.read_csv('data.csv', dtype={'id': 'int32', 'code': 'category'})

# Excel with parsing
df = pd.read_excel('data.xlsx', parse_dates=['date'], date_format='%Y-%m-%d')

# Parquet (recommended for large data)
df = pd.read_parquet('data.parquet', columns=['col1', 'col2'])

# SQL database
df = pd.read_sql('SELECT * FROM orders', connection, parse_dates=['date'])

# Chunked reading
for chunk in pd.read_csv('large.csv', chunksize=10000):
    process(chunk)
```

### Filter & Select
```python
# Boolean indexing
filtered = df[(df['age'] >= 25) & (df['status'] == 'active')]

# Query method
filtered = df.query('age >= 25 and status == "active"')

# Column selection
cols = ['id', 'name', 'revenue']
selected = df[cols]

# loc (label-based) and iloc (position-based)
df.loc['row_label', 'col_label']
df.iloc[0:10, 1:5]
```

### GroupBy & Aggregate
```python
# Single aggregation
grouped = df.groupby('category')['revenue'].sum()

# Multiple aggregations
result = df.groupby('category').agg({
    'revenue': ['sum', 'mean', 'std'],
    'quantity': ['count', 'max']
})

# Named aggregations (recommended)
result = df.groupby('category').agg(
    total_revenue=('revenue', 'sum'),
    avg_revenue=('revenue', 'mean'),
    order_count=('order_id', 'count')
)
```

### Merge & Join
```python
# Merge
merged = pd.merge(left, right, on='key', how='left')

# Concat
stacked = pd.concat([df1, df2, df3], ignore_index=True)

# Join on index
result = df1.join(df2, how='left')
```

### Pivot & Reshape
```python
# Pivot table
pivot = pd.pivot_table(df, index='category', columns='region', 
                        values='revenue', aggfunc='sum', fill_value=0)

# Melt
long = df.melt(id_vars=['id'], value_vars=['jan', 'feb', 'mar'], 
              var_name='month', value_name='sales')

# Stack/Unstack
stacked = df.stack()
unstacked = df.unstack()
```

## 7.4 Time Series Operations
```python
# Datetime conversion
df['date'] = pd.to_datetime(df['date'])
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', unit='s')

# Set index and resample
df.set_index('date').resample('D')['revenue'].sum()

# Rolling windows
df['ma_7'] = df['revenue'].rolling(window=7).mean()
df['ma_30'] = df['revenue'].rolling(window=30).mean()

# Shifts for period comparisons
df['prev_month'] = df['revenue'].shift(1)
df['yoy'] = df['revenue'] / df['revenue'].shift(12) - 1
```

## 7.5 Version Compatibility

| pandas Version | Python Version | Key Features |
|----------------|----------------|---------------|
| 2.2.x | 3.9+ | PyArrow backend, copy-on-write |
| 2.1.x | 3.9+ | Styler caching, improvements |
| 2.0.x | 3.8+ | Nullable dtypes, PyArrow strings |
| 1.5.x | 3.8+ | PyArrow strings, NaN deprecation |
| 1.4.x | 3.8+ | DataFrame.attrs, concat behavior |
