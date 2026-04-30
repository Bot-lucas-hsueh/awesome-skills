# python Example

```
import pandas as pd
import numpy as np

# Reading with explicit dtypes
df = pd.read_csv('data.csv', dtype={'category': 'category', 'count': 'Int64'}, parse_dates=['date'])

# Filtering
df[df['revenue'] > 1000]
df.query('revenue > 1000 & status == "active"')

# Selecting columns
df[['name', 'revenue']]  # list
df.filter(regex='^revenue')  # regex filter
df.loc[:, 'name':'revenue']  # slice by column name

# Creating columns (assign/chaining)
df = df.assign(
    profit=df['revenue'] - df['cost'],
    margin_pct=lambda x: x['profit'] / x['revenue'] * 100,
    quarter=lambda x: x['date'].dt.quarter
)

# Transform with groupby
df['revenue_rank'] = df.groupby('region')['revenue'].rank(ascending=False)
df['pct_of_group'] = df['revenue'] / df.groupby('region')['revenue'].transform('sum')

# Sort
df.sort_values(['region', 'date'], ascending=[True, False], na_position='last')
```
