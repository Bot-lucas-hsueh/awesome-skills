# Standard Workflow

## 8.1 Development Workflow

```
Phase 1: Environment Setup
├── Create virtual environment: python -m venv env
├── Install dependencies: pip install numpy scipy matplotlib
├── Set up IDE with NumPy support (PyCharm, VS Code)
└── Configure IPython/Jupyter for interactive work

Phase 2: Code Development
├── Import conventions: import numpy as np, from scipy import signal
├── Use type hints: def process(arr: np.ndarray) -> np.ndarray
├── Write unit tests: pytest with numpy.testing
└── Profile performance: %timeit, line_profiler

Phase 3: Optimization
├── Vectorize loops (NumPy broadcasting)
├── Use in-place operations: a *= 2
├── Leverage scipy.linalg over numpy.linalg for speed
└── Consider numba for custom loops
```

### Code Quality Checklist
- [ ] Use `np.asarray()` to handle list/array input
- [ ] Specify dtype explicitly: `np.array(data, dtype=np.float64)`
- [ ] Prefer `np.empty_like()` over `np.zeros_like()` when initializing
- [ ] Use `np.isclose()` for floating-point comparison

## 8.2 Scientific Computing Workflow

```
Phase 1: Data Acquisition
├── Load data: np.loadtxt(), np.genfromtxt(), pandas
├── Handle missing: np.nan_to_num(), np.ma.array
└── Validate shapes: assert arr.shape == expected

Phase 2: Preprocessing
├── Normalization: (arr - mean) / std
├── Filtering: scipy.signal.medfilt(), butter()
├── Interpolation: scipy.interpolate.griddata()
└── Smoothing: scipy.ndimage.gaussian_filter()

Phase 3: Analysis
├── Statistical: scipy.stats.ttest_ind(), linregress()
├── Signal: scipy.signal.periodogram(), welch()
├── Optimization: scipy.optimize.minimize()
└── Integration: scipy.integrate.quad(), odeint()

Phase 4: Visualization
├── Line plots: matplotlib.pyplot.plot()
├── Images: matplotlib.pyplot.imshow()
├── Subplots: fig, axes = plt.subplots(2, 2)
└── Export: plt.savefig('figure.png', dpi=300)
```

### Example: Signal Processing Pipeline
```python
import numpy as np
from scipy import signal, stats
import matplotlib.pyplot as plt

# Generate sample signal
t = np.linspace(0, 1, 1000)
noise = np.random.normal(0, 0.1, len(t))
signal_clean = 3 * np.sin(2 * np.pi * 10 * t)  # 10 Hz
signal_noisy = signal_clean + noise

# Design filter
sos = signal.butter(4, 15, btype='low', fs=1000, output='sos')
filtered = signal.sosfilt(sos, signal_noisy)

# Analyze
freqs, psd = signal.welch(filtered, fs=1000)
peak_freq = freqs[np.argmax(psd)]
```

## 8.3 Numerical Computation Workflow

```
Phase 1: Problem Formulation
├── Identify mathematical problem type
├── Choose appropriate algorithm
└── Determine convergence criteria

Phase 2: Implementation
├── Use established routines (don't reinvent)
├── Set tolerance: tol = 1e-8
├── Set max iterations: maxiter=1000
└── Implement fallback for non-convergence

Phase 3: Validation
├── Test known solutions (analytical when possible)
├── Check conservation laws (energy, momentum)
├── Verify asymptotic behavior
└── Compare with reference implementations

Phase 4: Performance
├── Profile bottlenecks: cProfile
├── Vectorize: replace Python loops
├── Use compiled backends: numba, Cython
└── Parallelize: multiprocessing for independent ops
```

### Example: Solving ODE System
```python
from scipy.integrate import solve_ivp
import numpy as np

def lorenz(t, xyz, sigma=10, rho=28, beta=8/3):
    x, y, z = xyz
    return [sigma*(y - x), x*(rho - z) - y, x*y - beta*z]

sol = solve_ivp(lorenz, [0, 50], [1, 0, 0], 
                 dense_output=True, max_step=0.01)
t_eval = np.linspace(0, 50, 1000)
y_eval = sol.sol(t_eval)
```
