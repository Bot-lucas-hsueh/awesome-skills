# Common Pitfalls & Anti-Patterns

## 10.1 Numerical Precision Mistakes

| # | Anti-Pattern | Severity | Impact | Quick Fix |
|---|--------------|----------|--------|-----------|
| 1 | **Float comparison** `a == b` | 🔴 High | Incorrect equality checks | `np.isclose(a, b)` or `np.allclose(a, b)` |
| 2 | **Integer overflow** `np.array([2**31])` | 🔴 High | Silent wraparound | Use `np.int64` or check bounds |
| 3 | **Cumulative sum instability** | 🔴 High | Large errors in summation | Use `np.sum` or `scipy.integrate.cumtrapz` |
| 4 | **NaN propagation** | 🔴 High | Results become NaN | Check with `np.isnan()`, use `np.nansum()` |
| 5 | **Inf handling** | 🟡 Medium | Cascading issues | Use `np.isfinite()` to filter |

### Examples

```python
# WRONG: Direct float comparison
if 0.1 + 0.2 == 0.3:
    print("Equal")  # Never executes!

# CORRECT: Use tolerance
if np.isclose(0.1 + 0.2, 0.3, rtol=1e-9):
    print("Approximately equal")

# WRONG: Integer overflow
arr = np.array([2**30, 2**30], dtype=np.int32)
print(arr * 3)  # Shows wrong values due to overflow

# CORRECT: Use int64
arr = np.array([2**30, 2**30], dtype=np.int64)
print(arr * 3)  # Correct result
```

## 10.2 Array Manipulation Errors

| # | Anti-Pattern | Severity | Impact | Quick Fix |
|---|--------------|----------|--------|-----------|
| 1 | **View vs copy** | 🔴 High | Modified source unexpectedly | `arr.copy()`, check with `.base` |
| 2 | **Broadcast shape mismatch** | 🔴 High | Wrong results silently | Print shapes during debugging |
| 3 | **Axis confusion** | 🔴 High | Operation on wrong dimension | Explicit axis parameter |
| 4 | **In-place vs new** | 🟡 Medium | Memory corruption | Know when methods return copies |
| 5 | **Contiguous memory** | 🟡 Medium | Slow operations | Use `np.ascontiguousarray()` |

### Examples

```python
# WRONG: Modifying view affects original
a = np.array([1, 2, 3, 4, 5])
b = a[::2]      # b is a VIEW, not a copy
b[:] = 0        # Modifies a!
print(a)       # [0, 2, 0, 4, 0]

# CORRECT: Explicit copy
a = np.array([1, 2, 3, 4, 5])
b = a[::2].copy()
b[:] = 0
print(a)       # [1, 2, 3, 4, 5]

# WRONG: Axis confusion
arr = np.array([[1, 2], [3, 4], [5, 6]])
print(np.sum(arr, axis=2))  # ERROR: axis out of bounds

# CORRECT: axis=1 sums each row
print(np.sum(arr, axis=1))  # [3, 7, 11]
```

## 10.3 SciPy Algorithm Mistakes

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Wrong optimizer** | 🔴 High | Match algorithm to problem type |
| 2 | **Poor initial guess** | 🔴 High | Use reasonable bounds, try multiple starts |
| 3 | **Ignoring convergence** | 🔴 High | Check `result.success` and message |
| 4 | **Numerical derivatives** | 🟡 Medium | Provide Jacobian when possible |
| 5 | **Units mismatch** | 🔴 High | Verify consistent units in fitting |

### Examples

```python
# WRONG: Using Nelder-Mead for bounded problems
result = minimize(lambda x: rosenbrock(x), x0=[0,0], method='Nelder-Mead')

# CORRECT: Use L-BFGS-B with bounds
result = minimize(lambda x: rosenbrock(x), x0=[0,0], 
                  method='L-BFGS-B', bounds=[(-5,5), (-5,5)])

# WRONG: Ignoring convergence status
result = minimize(objective, x0)
# Use result.x, result.fun without checking

# CORRECT: Check convergence
if not result.success:
    print(f"Warning: {result.message}")
```

## 10.4 Performance Anti-Patterns

```python
# WRONG: Loop over array elements
for i in range(len(arr)):
    result[i] = arr[i] * 2 + 1

# CORRECT: Vectorized operation
result = arr * 2 + 1

# WRONG: Repeated array creation
for _ in range(1000):
    A = np.random.rand(100, 100)
    B = A @ A.T

# CORRECT: Pre-allocate or use einsum
B = np.einsum('ij,jk->ik', A, A.T)  # More memory efficient

# WRONG: Unnecessary Python lists
data_list = [np.sin(i) for i in range(1000)]

# CORRECT: Keep as NumPy array
data = np.sin(np.arange(1000))
```
