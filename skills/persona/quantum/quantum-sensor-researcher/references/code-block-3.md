# Code Block 3: Systematic Error & Vibration Analysis

## Anti-Pattern 3: Systematic Error Budget

```python
import numpy as np

def gravimeter_systematic_budget(T=0.5, lambda_laser=780e-9, N=1e6):
    """
    Systematic error budget for cold atom gravimeter.
    Compares statistical precision to systematic uncertainty.
    """
    k_eff = 4 * np.pi / lambda_laser
    
    # Statistical sensitivity (SQL)
    delta_phi = 1 / np.sqrt(N)
    delta_g_stat = delta_phi / (k_eff * T**2)
    
    # Systematic errors (typical values)
    systematics = {
        "Coriolis (Earth rotation)": {
            "value": 5e-9,  # g
            "uncertainty": 1e-10,  # g
            "dominates": True,
            "mitigation": "Counter-propagating beams, active rotation compensation"
        },
        "Second-order Zeeman": {
            "value": 1e-9,
            "uncertainty": 5e-11,
            "dominates": True,
            "mitigation": "Magnetic shielding, bias field stabilization"
        },
        "Wavefront aberration": {
            "value": 2e-10,
            "uncertainty": 5e-11,
            "dominates": False,
            "mitigation": "Optical quality, spatial filtering"
        },
        "Raman light shift": {
            "value": 1e-10,
            "uncertainty": 2e-11,
            "dominates": False,
            "mitigation": "Two-photon detuning optimization"
        }
    }
    
    # RSS of systematic uncertainties
    total_systematic_unc = np.sqrt(sum(s["uncertainty"]**2 for s in systematics.values()))
    
    print(f"Statistical sensitivity (1σ, 1s): {delta_g_stat:.2e} g")
    print(f"Statistical after 1000s avg: {delta_g_stat/np.sqrt(1000):.2e} g")
    print(f"\nSystematic uncertainty (RSS): {total_systematic_unc:.2e} g")
    
    for name, s in systematics.items():
        dom = " ← DOMINANT" if s["dominates"] else ""
        print(f"  {name}: {s['value']:.1e} ± {s['uncertainty']:.1e} g{dom}")
        print(f"    Mitigation: {s['mitigation']}")
    
    return delta_g_stat, total_systematic_unc

delta_g_stat, delta_sys = gravimeter_systematic_budget()
```

## Anti-Pattern 5: Vibration Coupling

```python
def portable_gravimeter_vibration(gamma_vibration=1e-4, delta_g_lab=1e-9):
    """
    Analyze vibration coupling for field-deployable gravimeters.
    
    Parameters:
    - gamma_vibration: Vehicle vibration amplitude (g RMS)
    - delta_g_lab: Lab gravimeter sensitivity (g/√Hz)
    """
    print("VIBRATION COUPLING ANALYSIS")
    print("=" * 50)
    
    # Vibration spectrum for typical ground vehicle
    vibration_amplitude = gamma_vibration  # g RMS
    
    print(f"Vehicle vibration level: {vibration_amplitude:.1e} g RMS")
    
    # Lab gravimeter achieves 1e-9 g/√Hz in quiet environment
    # But vibration dominates in vehicle
    delta_g_vibration = vibration_amplitude  # Direct coupling
    
    print(f"Vibration coupling to gravity channel: {delta_g_vibration:.1e} g")
    print(f"Lab sensitivity: {delta_g_lab:.1e} g/√Hz")
    print(f"Vibration degrades sensitivity by: {delta_g_vibration/delta_g_lab:.0e}x")
    
    # Mitigation strategies
    print("\nMitigation Options:")
    print("1. Vibration isolation platform (cost: $50K, attenuation: 100x)")
    print("2. Gravity gradiometer (rejects common-mode vibration)")
    print("3. Active vibration feedforward using seismometer")
    print("4. Stationary measurement (stop vehicle)")
    
    # Gradiometer rejection
    baseline = 1.0  # m
    gamma_gradient = gamma_vibration / baseline  # g/m
    rejection_factor = 0.01  # 1% common-mode rejection
    delta_g_gradiometer = rejection_factor * baseline * gamma_gradient
    
    print(f"\nGradiometer (baseline={baseline}m): {delta_g_gradiometer:.1e} g effective")
    print(f"Improvement over single gravimeter: {delta_g_vibration/delta_g_gradiometer:.0f}x")
```
