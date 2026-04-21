## § 9 — Scenario Examples

### Scenario A — Atom Interferometer Gravity Gradiometer Design

**User**: I want to build a cold-atom gravity gradiometer for underground structure mapping. What sensitivity and integration time do I need?

**Expert**: Underground structure mapping requires resolving density contrasts at meter-scale. Here is a complete sensitivity analysis and design:

```python
import numpy as np

# Physical constants
hbar = 1.055e-34   # J·s
m_Rb = 1.443e-25   # kg, 87Rb mass
g = 9.8            # m/s²
lambda_780 = 780e-9  # m, Rb D2 line

# Atom interferometer parameters
k_eff = 2 * (2 * np.pi
T_interrogation = 0.5  # s, free-fall time (1s total sequence)
N_atoms = 1e6          # atoms per shot
cycle_rate = 1.0       # Hz

# Sensitivity calculation
# Gravity gradiometer: Γ = (g1 - g2)
# Phase from gravity gradient: Φ = k_eff * Γ * Δz * T²
# where Δz = baseline separation

delta_z = 1.0  # m, baseline separation

# SQL phase sensitivity per measurement
delta_phi_SQL = 1

# Gradiometer sensitivity (in Eötvös, 1 E = 10^-9 s^-2)
delta_Gamma_per_shot = delta_phi_SQL
delta_Gamma_Eotvos = delta_Gamma_per_shot / 1e-9  # in Eötvös/shot

# Integrate over time
tau = np.logspace(0, 5, 100)  # integration time in seconds
sigma_Gamma = delta_Gamma_per_shot

print(f"k_eff = {k_eff:.3e} m^-1")
print(f"Single-shot phase sensitivity (SQL): δφ = {delta_phi_SQL:.4f} rad")
print(f"Single-shot gradiometer sensitivity: {delta_Gamma_Eotvos:.1f} E/shot")
print(f"After 100s averaging: {delta_Gamma_Eotvos/np.sqrt(100):.2f} E")
print(f"After 3600s (1 hour): {delta_Gamma_Eotvos/np.sqrt(3600):.3f} E")

# Underground structure detectability
rho_contrast = 500  # kg/m³, density contrast (rock vs void)
G = 6.674e-11       # gravitational constant
depth = 10          # m depth to target
target_size = 3     # m, spherical void radius

# Bouguer anomaly from spherical void
delta_g_anomaly = (4/3) * np.pi * G * rho_contrast * target_size**3
delta_Gamma_anomaly = 2 * delta_g_anomaly

print(f"\nTarget gravity gradient anomaly: {delta_Gamma_anomaly/1e-9:.2f} E")
print(f"Required integration time: {(delta_Gamma_Eotvos/1e-9 / (delta_Gamma_anomaly/1e-9))**2:.0f} s")
```

**Design recommendations**:
- **Baseline**: 1 m (simultaneous dual-MOT gradiometer with shared laser) rejects >99.9% of laser phase noise and vibration common mode
- **Interrogation time**: T = 0.5 s requires 1 m free-fall height or trapped geometry (optical lattice)
- **Atom number**: N = 10^6 from BEC or cold thermal cloud (sub-μK launch temperature)
- **Key systematic**: Coriolis effect (Earth rotation) introduces bias — implement counter-propagating sequence or active rotation compensation

---

### Scenario B — SQUID Magnetometer Noise Floor Design

**User**: I need to design a SQUID-based magnetometer for MEG (magnetoencephalography) with < 5 fT/√Hz sensitivity. What are the design requirements?

**Expert**: MEG requires < 5 fT/√Hz sensitivity with bandwidth 1–1000 Hz. Here is the SQUID design chain:

```python
import numpy as np

# SQUID physical parameters
Phi_0 = 2.068e-15  # Wb, flux quantum

# DC-SQUID parameters
L_squid = 300e-12    # H, SQUID inductance
I_c = 10e-6          # A, junction critical current
R_n = 5              # Ω, shunt resistance

# Thermal flux noise in SQUID loop
T_operating = 4.2   # K (LHe) or 0.01 K (dilution fridge)
k_B = 1.381e-23     # J/K

# White flux noise spectral density (Tesche-Clarke limit)
# S_Phi = 16 k_B T L_sq
# Realistic: S_Phi^(1/2) ~ 1-5 μΦ_0/√Hz at 4.2 K
S_Phi_sqrt = 2e-6 * Phi_0  # 2 μΦ_0/√Hz flux noise (typical LTS SQUID at 4.2 K)

# Flux concentrator (pickup coil) design
# A_eff = M²
L_pickup = 2e-6      # H, pickup coil inductance
M_coupling = 15e-9   # H, mutual inductance (k ~ 0.7)
A_pickup = 5e-4      # m², pickup coil area (2.25 cm diameter)

# Effective field sensitivity
A_eff = M_coupling**2 / (L_squid + L_pickup)
delta_B = S_Phi_sqrt

print(f"SQUID flux noise: {S_Phi_sqrt/Phi_0*1e6:.1f} μΦ₀/√Hz")
print(f"Effective pickup area: {A_eff*1e4:.2f} cm²")
print(f"Field sensitivity: {delta_B*1e15:.2f} fT/√Hz")

# MEG signal levels
B_alpha_rhythm = 100e-15   # T, typical alpha rhythm (10 Hz) signal
B_evoked = 10e-15          # T, typical evoked response signal

SNR_alpha = B_alpha_rhythm
SNR_evoked = B_evoked
print(f"\nSNR for alpha rhythm (100 fT): {SNR_alpha:.0f}:1")
print(f"SNR for evoked response (10 fT): {SNR_evoked:.0f}:1")

# Magnetic shielding requirement
B_earth = 50e-6    # T, Earth's field
attenuation_required = B_earth
print(f"\nRequired shielding attenuation: {attenuation_required:.0e}")
print(f"Requires MSR (magnetically shielded room) with > {20*np.log10(attenuation_required):.0f} dB shielding")
```

**Design requirements for MEG < 5 fT/√Hz**:
- **SQUID type**: Low-temperature SQUID (Nb, 4.2 K) with S_Φ^(1/2) ≤ 2 μΦ₀/√Hz or HTS SQUID (YBCO, 77 K) with S_Φ^(1/2) ≤ 20 μΦ₀/√Hz (requires larger pickup area)
- **Pickup coil**: Gradiometer geometry (1st-order axial gradiometer, baseline 50–80 mm) rejects >99% of environmental noise from distant sources
- **Shielding**: Magnetically shielded room with > 80 dB attenuation at DC and > 100 dB at 10 Hz
- **Readout**: Flux-locked loop (FLL) with SQUID bandwidth > 100 kHz; 100 dB dynamic range at 1 kHz

---

### Scenario C — NV-Center Magnetometry Protocol for Single-Cell Imaging

**User**: How do I design an NV-center magnetometry experiment to image action potentials in individual neurons?

**Expert**: Single-neuron action potential imaging requires detecting ~1 nT magnetic fields at kHz bandwidth, 10–100 μm spatial resolution. Here is the complete NV protocol:

```python
import numpy as np
import matplotlib.pyplot as plt

# NV-center parameters
gamma_e = 28e9         # Hz/T, electron gyromagnetic ratio
T2_star_NV = 1e-6      # s, T2* for near-surface NV in typical diamond
T2_echo_NV = 100e-6    # s, T2 from Hahn echo (spin echo extends coherence)
B0_bias = 4e-3         # T, bias field to lift degeneracy (0.112 GHz at ~4 mT)

# Ramsey DC magnetometry sensitivity (single NV)
N_NV_single = 1        # single NV
contrast = 0.03        # typical contrast (ODMR contrast ~3% for single NV near surface)
detection_efficiency = 0.001  # photon collection efficiency (NA, diamond-air interface)

# Single-NV DC sensitivity
delta_B_single = 1
                                                     detection_efficiency))
print(f"Single NV DC sensitivity: {delta_B_single*1e9:.0f} nT/√Hz")

# Action potential target signal
B_action_potential = 1e-9  # T, ~1 nT at 10 μm from axon

# Required integration for SNR=3
tau_required_single = (3 * delta_B_single
print(f"Integration time for SNR=3 (single NV): {tau_required_single:.1f} s")

# Ensemble NV approach (better for imaging)
N_NV_ensemble = 1e10   # NVs in 10×10×10 μm cube at 1 ppm density
contrast_ensemble = 0.20   # higher contrast with optimized charge state
eta_ensemble = 0.05        # collection into multimode fiber

delta_B_ensemble = 1
                         np.sqrt(N_NV_ensemble * T2_star_NV * eta_ensemble))
print(f"\nEnsemble NV DC sensitivity ({N_NV_ensemble:.0e} centers): "
      f"{delta_B_ensemble*1e12:.1f} pT/√Hz")

# AC magnetometry with spin echo (CPMG for kHz action potential)
f_AP = 1000  # Hz, action potential frequency component
t_pi2 = 1

delta_B_AC_echo = 1
                        np.sqrt(N_NV_ensemble * T2_echo_NV * eta_ensemble))
print(f"AC sensitivity at 1 kHz (spin echo): {delta_B_AC_echo*1e15:.1f} fT/√Hz")

# Protocol design for action potential imaging
print("\n--- NV Action Potential Imaging Protocol ---")
print(f"1. Diamond: [100] surface, NV density 1-10 ppm, T2* > 1 μs")
print(f"2. Laser: 532 nm, > 1 mW for ensemble, < 1 μW for single NV")
print(f"3. Microwave: resonant to |0>→|-1> transition at {B0_bias*gamma_e/1e9:.3f} GHz")
print(f"4. Sequence: CPMG-N with N = {int(T2_echo_NV * f_AP * 2)} pulses at f = {f_AP} Hz")
print(f"5. Detection: SPAD/SNSPD in photon counting mode, gated to readout window")
print(f"6. Imaging: wide-field (camera) or confocal raster scan")
print(f"7. Standoff distance: < 50 nm (spin-coated NVs) to 5 μm (bulk diamond)")
```

**Key design choices for neural imaging**:
- **Diamond geometry**: Shallow NV implantation (< 10 nm from surface) for proximity to cell; requires surface passivation to maintain T2* > 1 μs
- **AC protocol**: CPMG-N dynamical decoupling synchronized to action potential frequency (100 Hz–10 kHz) extends effective T2 from 1 μs to 100 μs, gaining 10× sensitivity
- **Spatial resolution**: Limited by optical diffraction to ~300 nm (confocal) or 30 nm (STED-NV); not by NV-cell distance
- **Biocompatibility**: Diamond nanoparticles require surface functionalization; verify cell viability > 24 hours post-labeling

---
