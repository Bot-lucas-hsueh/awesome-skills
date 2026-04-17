# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | Large outputs in cells | 🔴 High | Clear outputs before committing |
| 2 | Hardcoded paths | 🟡 Medium | Use relative paths or environment variables |
| 3 | Not restarting kernel | 🟡 Medium | Restart and run all before sharing |
| 4 | Execution order dependency | 🔴 High | Use "Restart & Run All" to verify |
| 5 | Forgetting %matplotlib inline | 🟡 Medium | Add at top of notebook |
| 6 | Large data in Git | 🔴 High | Use .gitignore and data versioning |
| 7 | Out-of-order cell execution | 🔴 High | Number cells logically |
| 8 | Not clearing outputs | 🟡 Medium | Run `jupyter nbconvert --clear-output` |
| 9 | Missing imports | 🟡 Medium | Put imports in first cell |
| 10 | Using ! for shell commands | 🟡 Medium | Use %bash or %sx |

## 10.2 Kernel & Runtime Issues

### Kernel Dies / Crashes

```python
# Check memory usage
%memit  # Before running heavy computation

# Reduce batch size
del large_variable  # Free memory

# Force garbage collection
import gc
gc.collect()

# Check kernel specs
!jupyter kernelspec list
```

### Slow Notebook Performance

```python
# Profile notebook execution
%load_ext line_profiler

# Check for large outputs
# Edit -> Clear All Outputs

# Use %%writefile instead of pasting large code
%%writefile my_module.py
# large code here
```

## 10.3 Git Best Practices

```bash
# .gitignore for notebooks
cat >> .gitignore << EOF
.ipynb_checkpoints/
*.ipynb_checkpoints
.DS_Store
EOF

# Install nbstripout to clean outputs on commit
pip install nbstripout
git nbstripout --install

# Track data files separately (DVC, Git LFS)
pip install dvc
dvc init
```

## 10.4 Notebook Quality Checklist

- [ ] Clear cell structure with markdown headers
- [ ] No execution counts in final version (clear outputs)
- [ ] All imports at the top
- [ ] No hardcoded paths (use variables)
- [ ] Descriptive variable names
- [ ] Comments for complex operations
- [ ] Test cells produce expected output
- [ ] Run "Restart Kernel and Run All Cells"
- [ ] Remove %debug and %pdb after debugging

## 10.5 Performance Tips

```python
# Avoid loops when vectorizing is possible
# BAD:
for i in range(len(df)):
    df.loc[i, 'new_col'] = df.loc[i, 'a'] + df.loc[i, 'b']

# GOOD:
df['new_col'] = df['a'] + df['b']

# Use chunking for large file reading
chunk_size = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    process(chunk)

# Profile specific lines
%timeit df.groupby('col').mean()

# Memory-efficient data types
df['int_col'] = df['int_col'].astype('int32')  # Instead of int64
```

## 10.6 Widget Performance Issues

```python
# For large datasets, avoid redrawing entire plot
# Use Output widget to prevent flickering

output = widgets.Output()

def update_plot(change):
    with output:
        clear_output(wait=True)
        # Only plot new data
        
# Debounce rapid updates
from functools import debounce

@debounce(0.5)  # Wait 500ms after last change
def slow_update(change):
    ...
```
