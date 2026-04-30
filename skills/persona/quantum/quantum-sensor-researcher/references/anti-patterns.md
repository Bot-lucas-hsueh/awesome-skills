# Anti-Pattern Code Examples

## Anti-Pattern 1: Allan Deviation Analysis

❌ BAD:
```
"Our gravimeter achieves 10^-9 g sensitivity."
# Single-measurement number. No integration time stated.
# No long-term stability characterization.
```

✅ GOOD:
```python
import allantools
import numpy as np

# Compute Allan deviation from time series of gravity measurements
def analyze_sensor_stability(g_measurements, rate_Hz):
    """Full stability characterization via Allan deviation."""
    tau_values, adev, adev_err, n = allantools.oadev(
        g_measurements, rate=rate_Hz, data_type="freq", taus="octave"
    )
    min_idx = np.argmin(adev)
    print(f"White noise floor: σ_0 = {adev[0] * np.sqrt(tau_values[0]):.2e} g/√Hz")
    print(f"Flicker floor at τ = {tau_values[min_idx]:.0f} s: σ_y = {adev[min_idx]:.2e} g")
    return tau_values, adev

print("Gravimeter performance:")
print(f"  Single-shot: 10^-9 g (1 s integration)")
print(f"  Stability floor: 10^-11 g at τ = 1000 s (flicker limited)")
```

## Anti-Pattern 2: Heisenberg Limit with Detection Loss

❌ BAD:
```python
delta_phi_claimed = 1 / 1000  # GHZ N=1000
print(f"Heisenberg-limited: {delta_phi_claimed:.4f} rad")
# Ignores detector efficiency η = 0.3, decoherence, state preparation
```

✅ GOOD:
```python
N = 1000
eta_detection = 0.30     # 30% detection efficiency
F_GHZ = 0.85             # GHZ state fidelity
decoherence_factor = 0.70

delta_phi_HL_realistic = 1 / (np.sqrt(eta_detection) * F_GHZ * decoherence_factor * N)
delta_phi_SQL_realistic = 1 / np.sqrt(eta_detection * N)

print(f"Realistic Heisenberg: {delta_phi_HL_realistic:.5f} rad")
print(f"Realistic SQL: {delta_phi_SQL_realistic:.5f} rad")
print(f"Improvement: {delta_phi_SQL_realistic/delta_phi_HL_realistic:.1f}x")
```

## Anti-Pattern 3: Systematic Error Budget

→ See `code-block-3.md` for full systematic error budget implementation.

## Anti-Pattern 4: NV T2* vs T2

→ See `code-block-2.md` for NV T2* vs T2 sensitivity code.

## Anti-Pattern 5: Vibration Coupling

→ See `code-block-3.md` for portable gravimeter vibration analysis.
