# Standards & Reference

## 7.1 Official Documentation

- [NumPy Documentation](https://numpy.org/doc/stable/)
- [SciPy Documentation](https://docs.scipy.org/doc/scipy/)
- [NumPy API Reference](https://numpy.org/doc/stable/reference/)
- [SciPy Reference Guide](https://docs.scipy.org/doc/scipy/reference/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [SciPy Tutorial](https://docs.scipy.org/doc/scipy/tutorial/)

## 7.2 Reference Tables

### NumPy Array Operations

| Operation | Function | Description |
|-----------|----------|-------------|
| Create array | `np.array()`, `np.zeros()`, `np.arange()` | Initialize arrays |
| Reshape | `arr.reshape()`, `arr.flatten()` | Change dimensions |
| Indexing | `arr[::2]`, `arr[:, 1]` | Slice and select |
| Math | `np.sum()`, `np.mean()`, `np.std()` | Aggregations |
| Linear algebra | `np.dot()`, `np.linalg.eig()` | Matrix operations |
| FFT | `np.fft.fft()`, `np.fft.rfft()` | Fourier transforms |

### SciPy Optimization Methods

| Problem Type | Function | Use Case |
|--------------|----------|----------|
| Unconstrained | `scipy.optimize.minimize` | General optimization |
| Curve fitting | `scipy.optimize.curve_fit` | Fit data to model |
| Root finding | `scipy.optimize.fsolve` | Solve f(x)=0 |
| Linear programming | `scipy.optimize.linprog` | Linear constraints |
| Least squares | `scipy.optimize.leastsq` | Minimize residual squares |

### Scientific Constants (scipy.constants)

| Constant | Value | Unit |
|----------|-------|------|
| c (speed of light) | 299792458 | m/s |
| h (Planck) | 6.62607015e-34 | J·s |
| e (electron charge) | 1.602176634e-19 | C |
| N_A (Avogadro) | 6.02214076e23 | mol⁻¹ |
| k_B (Boltzmann) | 1.380649e-23 | J/K |
| g (gravitational) | 9.80665 | m/s² |

## 7.3 Common Patterns

### Array Creation
```python
import numpy as np

a = np.arange(10)                    # [0, 1, 2, ..., 9]
b = np.linspace(0, 1, 5)             # [0., 0.25, 0.5, 0.75, 1.]
c = np.zeros((3, 3))                 # 3x3 zeros
d = np.eye(3)                         # Identity matrix
e = np.random.rand(3, 4)             # Random [0,1)
```

### Broadcasting Example
```python
a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])
c = a + b  # [[2,3,4], [3,4,5], [4,5,6]]
```

### Linear Algebra
```python
from scipy import linalg
import numpy as np

A = np.array([[1, 2], [3, 4]])
P, L, U = linalg.lu(A)        # LU decomposition
eigenvalues, eigenvectors = linalg.eig(A)
x = linalg.solve(A, b)        # Ax = b
```

### Optimization
```python
from scipy.optimize import minimize, curve_fit

# Minimize function
result = minimize(lambda x: x**2 + np.sin(x), x0=0)
print(result.x, result.fun)

# Curve fitting
def model(x, a, b): return a * np.exp(-b * x)
popt, pcov = curve_fit(model, xdata, ydata)
```

## 7.4 Version Compatibility

| NumPy | SciPy | Python | Key Features Added |
|-------|-------|--------|-------------------|
| 1.20+ | 1.7+ | 3.8+ | SIMD optimizations, typing improvements |
| 1.22+ | 1.8+ | 3.8+ | np.random.Generator, improved FFT |
| 1.24+ | 1.10+ | 3.8+ | dtype deprecations, improved cuPy support |
| 1.26+ | 1.12+ | 3.9+ | New random generator API, better error messages |
| 2.0+ | 1.14+ | 3.9+ | dtype changes, array API standard |

| Feature | Min NumPy | Min SciPy | Notes |
|---------|-----------|-----------|-------|
| `np.linalg.norm` with ord parameter | 1.0 | - | All norm orders |
| `scipy.signal` filtfilt | - | 0.1 | Signal filtering |
| `scipy.stats.permutation_test` | - | 1.10 | Statistical tests |
| `np.concatenate` axis warning | 1.24 | - | Improved error messages |
