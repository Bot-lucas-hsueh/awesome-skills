# Scenario Examples

## 9.1 Signal Processing

**User:** "Filter a noisy ECG signal at 250 Hz sampling rate to remove 60 Hz powerline interference"

**NumPy/SciPy Expert:**
> **ECG Signal Filtering:**
> 
> 1. Design notch filter at 60 Hz
> 2. Apply bandpass to keep 0.5-50 Hz (clinical range)
> 
> ```python
> from scipy import signal
> import numpy as np
> 
> fs = 250  # Hz
> 
> # Notch filter for 60 Hz interference
> b_notch, a_notch = signal.iirnotch(60, Q=30, fs=fs)
> 
> # Bandpass: 0.5-50 Hz for clinical ECG
> sos_bp = signal.butter(4, [0.5, 50], btype='band', fs=fs, output='sos')
> 
> # Apply filters
> filtered = signal.sosfilt(sos_bp, noisy_ecg)
> filtered = signal.lfilter(b_notch, a_notch, filtered)
> 
> # Powerline removal: also consider harmonic notch at 120 Hz
> b_harm, a_harm = signal.iirnotch(120, Q=30, fs=fs)
> filtered = signal.lfilter(b_harm, a_harm, filtered)
> ```

## 9.2 Data Analysis Workflows

### Time Series Analysis
```python
import numpy as np
from scipy import stats, signal

# Load time series data
data = np.loadtxt('timeseries.csv', delimiter=',')

# Detrend
detrended = signal.detrend(data)

# Find peaks
peaks, properties = signal.find_peaks(detrended, height=2, distance=50)

# Spectral analysis
freqs, psd = signal.welch(detrended, fs=100, nperseg=256)
dominant_freq = freqs[np.argmax(psd)]

# Statistical test for stationarity
result = stats.adfuller(data)
# Augmented Dickey-Fuller: p < 0.05 indicates stationarity
```

### Curve Fitting
```python
from scipy.optimize import curve_fit
import numpy as np

def exp_decay(t, A, tau, C):
    return A * np.exp(-t / tau) + C

# Experimental data
t = np.linspace(0, 10, 100)
y = 3 * np.exp(-t / 2.5) + 0.5 + 0.1 * np.random.randn(100)

# Fit with initial guess
popt, pcov = curve_fit(exp_decay, t, y, p0=[2, 1, 0], maxfev=5000)
perr = np.sqrt(np.diag(pcov))  # Standard errors

print(f"A = {popt[0]:.3f} ± {perr[0]:.3f}")
print(f"τ = {popt[1]:.3f} ± {perr[1]:.3f} s")
```

## 9.3 Publication Workflows

### Figure Generation for Papers
```python
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Publication-quality settings
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

# Create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3))

# Left: Raw vs filtered
ax1.plot(t, noisy, alpha=0.5, label='Raw')
ax1.plot(t, filtered, label='Filtered')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude (mV)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Right: Power spectrum
ax2.semilogy(freqs, psd)
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('PSD (V²/Hz)')
ax2.set_xlim([0, 50])
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figure1.png', format='png')
plt.savefig('figure1.pdf', format='pdf')  # Vector format
```

### Statistical Summary Table
```python
import pandas as pd
from scipy import stats
import numpy as np

def generate_stats_table(data, group_names):
    """Generate publication-ready statistics table."""
    rows = []
    for name, values in zip(group_names, data):
        n = len(values)
        mean, std = np.mean(values), np.std(values, ddof=1)
        sem = std / np.sqrt(n)
        rows.append({
            'Group': name,
            'n': n,
            'Mean': f'{mean:.2f}',
            'SD': f'{std:.2f}',
            'SEM': f'{sem:.2f}',
            '95% CI': f'[{mean - 1.96*sem:.2f}, {mean + 1.96*sem:.2f}]'
        })
    return pd.DataFrame(rows)

# Example: Three experimental groups
control = np.array([23.5, 24.1, 22.8, 25.2, 24.0])
low_dose = np.array([26.1, 27.4, 25.8, 28.0, 26.5])
high_dose = np.array([31.2, 32.5, 30.8, 33.1, 31.9])

table = generate_stats_table([control, low_dose, high_dose],
                               ['Control', 'Low Dose', 'High Dose'])
print(table.to_markdown(index=False))

# ANOVA
f_stat, p_val = stats.f_oneway(control, low_dose, high_dose)
print(f'\nOne-way ANOVA: F(2,12) = {f_stat:.2f}, p = {p_val:.4f}')
```
