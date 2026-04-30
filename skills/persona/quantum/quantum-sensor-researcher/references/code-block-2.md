# Code Block 2: Python Code Examples

## Scenario A: Atom Interferometer Gravity Gradiometer

```python
import numpy as np

# Gravity gradiometer sensitivity analysis
N_atoms = 1e6  # Number of atoms
T_interrogation = 0.5  # Free-fall time (s)
lambda_laser = 780e-9  # Wavelength for Rb (m)
k_eff = 4 * np.pi / lambda_laser  # Effective wavevector

# Standard Quantum Limit phase sensitivity
delta_phi_SQL = 1 / np.sqrt(N_atoms)

# Convert to gravity sensitivity
# δg = δφ / (k_eff * T²)
delta_g_SQL = delta_phi_SQL / (k_eff * T_interrogation**2)
print(f"SQL gravity sensitivity: {delta_g_SQL:.2e} g/√Hz")

# Heisenberg Limit
delta_phi_HL = 1 / N_atoms
delta_g_HL = delta_phi_HL / (k_eff * T_interrogation**2)
print(f"Heisenberg limit: {delta_g_HL:.2e} g/√Hz")

# Practical spin squeezing improvement (ξ² = 0.1 = -10 dB)
xi_squared = 0.1  # Wineland squeezing parameter
delta_phi_sq = np.sqrt(xi_squared) / np.sqrt(N_atoms)
delta_g_sq = delta_phi_sq / (k_eff * T_interrogation**2)
print(f"Squeezed sensitivity (ξ²=0.1): {delta_g_sq:.2e} g/√Hz")
print(f"Improvement over SQL: {delta_g_SQL/delta_g_sq:.1f}x")

# Allan deviation for averaging time
tau_averaging = 3600  # 1 hour averaging
sigma_g_SQL = delta_g_SQL / np.sqrt(tau_averaging)
print(f"SQL after 1 hour averaging: {sigma_g_SQL:.2e} g")
```

## Scenario B: SQUID Magnetometer Design

```python
import numpy as np

# MEG sensitivity requirements: < 5 fT/√Hz
target_sensitivity = 5e-15  # T/√Hz

# SQUID parameters
S_Phi_goal = 2e-6  # Flux noise (Φ₀/√Hz)
Phi_0 = 2.07e-15  # Flux quantum (Wb)
A_eff_goal = S_Phi_goal / target_sensitivity  # Effective area

print(f"Required flux noise: {S_Phi_goal:.1e} Φ₀/√Hz")
print(f"Required effective area: {A_eff_goal*1e6:.1f} mm²")

# LTS SQUID parameters
T_operating = 4.2  # K
gamma = 1e-10  # Gallium arsenide parameter
rho_normalized = 100  # Resistance parameter
f_flux = 1e9  # Operating frequency (Hz)

# DC SQUID energy resolution
epsilon = gamma * rho_normalized * np.sqrt(S_Phi_goal) / (2 * np.pi * np.sqrt(f_flux))
print(f"Energy resolution: {epsilon:.1e} J/Hz")

# Flux concentrator gain
G_fc = 50  # Typical flux concentrator gain
B_min = S_Phi_goal / (A_eff_goal * G_fc)
print(f"Field sensitivity with flux concentrator: {B_min:.2e} T/√Hz")
```

## Anti-Pattern 4: NV T2 vs T2 Sensitivity

```python
f_signal = 1000  # Hz, target AC signal frequency
T2_star = 1e-6   # s, from Ramsey (DC, inhomogeneous broadening limited)
T2_echo = 100e-6  # s, from Hahn echo (DC noise refocused)
T2_CPMG = 500e-6  # s, from CPMG-16 (further extends for kHz signals)

protocols = {
    "Ramsey (DC)": T2_star,
    "Hahn Echo (DC noise rejection)": T2_echo,
    "CPMG-16 (kHz band)": T2_CPMG,
}

N_NV = 1e10; C = 0.2; gamma = 28e9
for name, T2 in protocols.items():
    delta_B = 1 / (gamma * C * np.sqrt(N_NV * T2))
    print(f"{name}: T2={T2*1e6:.0f} μs → δB = {delta_B*1e12:.1f} pT/√Hz")

print("\nFor kHz neural signals, use CPMG synchronized to signal frequency!")
print(f"Sensitivity improvement: {np.sqrt(T2_CPMG/T2_star):.0f}× vs Ramsey")
```
