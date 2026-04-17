## § 9 Scenario Examples

### Scenario 1 — Designing InP/ZnSe Quantum Dot Synthesis (Cd-Free, High QY)

**User:** We need to replace CdSe QDs with a non-toxic alternative for display applications. We need green emission at 530 nm, FWHM < 35 nm, and QY > 80%. How do I synthesize InP/ZnSe core/shell QDs?

**Expert:** InP/ZnSe is the leading Cd-free alternative for displays. The key challenge is controlling InP size (for 530 nm emission, target ~2.5 nm diameter) and growing a high-quality ZnSe shell to suppress surface trap emission. Here is the validated hot-injection protocol:

```python
# InP/ZnSe QD synthesis parameter calculator
import numpy as np

# Brus equation approximation for InP quantum confinement
# E_g(r) = E_g,bulk + hbar^2*pi^2 / (2*r^2) * (1/m_e + 1/m_h)
# For practical use, empirical sizing curve from Yu et al.

def inp_diameter_from_wavelength(lambda_nm):
    """
    Empirical sizing curve for InP QDs (InP core before shell)
    Based on Xie et al., JACS 2009 and Reiss et al., Nano Lett 2002
    lambda_nm: first exciton absorption peak in nm
    Returns: core diameter in nm
    """
    # Fit to literature data points for InP
    # lambda_1s = 490 + 55*(d - 2.0) for d in nm, rough linear fit 2-4 nm
    d = 2.0 + (lambda_nm - 490)
    return d

# For 530 nm emission, first exciton absorption is ~510-515 nm
lambda_abs = 512  # nm (Stokes shift ~18 nm for InP)
d_core = inp_diameter_from_wavelength(lambda_abs)
print(f"Target InP core diameter: {d_core:.2f} nm")

# Shell thickness calculation
# For ZnSe shell: each monolayer = 0.283 nm (a/2 for zinc blende ZnSe)
n_monolayers = 3  # target: 3 ML ZnSe shell
ML_thickness = 0.283  # nm per monolayer
d_total = d_core + 2 * n_monolayers * ML_thickness
print(f"Core/shell total diameter: {d_total:.2f} nm")
print(f"Expected ZnSe shell thickness: {n_monolayers * ML_thickness:.2f} nm")
```

**Synthesis protocol (glove-box safe, Ar atmosphere):**

Step 1 — InP core synthesis:
- Precursors: InCl₃ (0.2 mmol), tris(trimethylsilyl)phosphine (P(TMS)₃, 0.2 mmol), zinc stearate (0.4 mmol as co-shell precursor), ODE (octadecene) at 300°C.
- Inject P(TMS)₃ solution at 300°C; nucleation burst occurs in 30–60 s.
- Monitor first exciton absorption by UV-Vis aliquots every 5 min; stop at 510 nm.
- Expected QY at this stage: 30–50% (surface traps dominant).

Step 2 — ZnSe shell growth (SILAR method):
- Alternately inject Zn-oleate (0.1 mmol/ML) and Se-TOP (0.1 mmol/ML) at 230°C.
- 3 full SILAR cycles; each cycle takes 30 min at temperature.
- After shell: QY should reach 75–90%.

[RISK] P(TMS)₃ is air-sensitive and reacts violently with moisture. All operations must be conducted in a Schlenk line or N₂ glove box. Waste P(TMS)₃ must be quenched with isopropanol before disposal. Never open P(TMS)₃ vials in air.

Characterization targets: TEM diameter 3.0–3.5 nm; FWHM < 35 nm by PL; QY > 80% vs Rhodamine 6G standard; XPS confirms Zn:Se ratio ~1:1 at surface.

---

### Scenario 2 — CVD Graphene Growth and Raman Quality Assessment

**User:** We are growing graphene by CVD on Cu foil for transparent electrode applications. Our Raman D/G ratio is 0.4 and the 2D peak is weak. How do I diagnose and fix the quality issues?

**Expert:** Raman D/G = 0.4 indicates significant defect density — likely grain boundaries, point defects, or residual PMMA contamination. Here is the systematic diagnosis:

```python
import numpy as np
import matplotlib.pyplot as plt

# Raman quality analysis for CVD graphene
# D/G ratio to defect density: Tuinstra-Koenig relation
# L_D (nm) = (1.8e-9 / lambda_laser^4) * (I_D/I_G)^-1
# lambda_laser in nm

def defect_spacing_from_DG(DG_ratio, lambda_laser_nm=532):
    """
    Lucchese et al. Carbon 2010: defect spacing L_D from D/G ratio
    Valid for L_D > 4 nm (low defect density regime)
    """
    lambda_m = lambda_laser_nm * 1e-9
    L_D_nm = (1.8e-9 / lambda_m**4) * (1.0
    return L_D_nm

def defect_density(L_D_nm):
    """Defect density n_D (cm^-2) from average defect spacing L_D (nm)"""
    L_D_cm = L_D_nm * 1e-7
    return 1.0

DG = 0.4
L_D = defect_spacing_from_DG(DG)
n_D = defect_density(L_D)
print(f"D/G = {DG:.2f}")
print(f"Average defect spacing L_D = {L_D:.1f} nm")
print(f"Defect density n_D = {n_D:.2e} cm⁻²")

# Target: D/G < 0.1 for device-grade graphene
DG_target = 0.1
L_D_target = defect_spacing_from_DG(DG_target)
print(f"\nTarget D/G < 0.1 requires L_D > {L_D_target:.1f} nm")
```

Expected output: D/G = 0.4 corresponds to L_D ≈ 25 nm defect spacing and n_D ≈ 5×10¹⁰ cm⁻², which is too high for transparent electrode use (target < 10¹⁰ cm⁻²).

**Diagnostic checklist and fixes:**

| Symptom | Root Cause | Fix |
|---------|------------|-----|
| D/G = 0.4 (high defects) | H₂ etch rate insufficient; too-fast cooling | Increase H₂:CH₄ ratio to 1000:1; slow cool at <10°C/min |
| Weak 2D peak (I(2D)/I(G) < 1) | Multilayer graphene growth | Reduce CH₄ partial pressure; use 25 µm Cu foil annealed at 1000°C in H₂ for 60 min before growth |
| D' peak visible at 1620 cm⁻¹ | Edge defects or oxidative damage | Avoid ambient air exposure after growth; transfer immediately |
| PMMA residue (broad D peak) | Incomplete PMMA removal | Anneal transferred graphene at 350°C in H₂/Ar for 2h; use hot acetone + IPA sequential wash |

Target Raman signature for device-grade graphene: I(D)/I(G) < 0.1; I(2D)/I(G) > 2.0 (single-layer); 2D peak FWHM < 30 cm⁻¹ at 532 nm excitation; sheet resistance < 500 Ω/sq by 4-probe van der Pauw.

---

### Scenario 3 — ALD Al2O3 Passivation for Perovskite Solar Cells

**User:** We want to deposit 5 nm Al2O3 by ALD on perovskite to improve stability. What are the process conditions and how do I verify film quality?

**Expert:** ALD Al2O3 at 5 nm is 50 cycles of TMA/H2O process. The challenge on perovskite is that standard water-based ALD can damage the halide perovskite surface — use H2O plasma or ozone-based ALD at the lowest acceptable temperature (< 80°C).

```python
# ALD process design for Al2O3 on perovskite
# TMA = trimethylaluminum; oxidant = H2O (or O3 for low-T)

def ald_cycles_for_thickness(target_nm, GPC_angstrom=1.1):
    """
    Calculate number of ALD cycles for target Al2O3 thickness
    GPC (growth per cycle) = 1.0-1.2 Å/cycle for TMA/H2O at 80-200°C
    """
    target_angstrom = target_nm * 10
    n_cycles = target_angstrom
    return int(np.ceil(n_cycles))

target_thickness_nm = 5.0
GPC = 1.05  # Å/cycle for TMA/H2O at 80°C on oxide surface
n_cycles = ald_cycles_for_thickness(target_thickness_nm, GPC)
print(f"Target: {target_thickness_nm} nm Al2O3")
print(f"GPC at 80°C: {GPC} Å/cycle")
print(f"Required cycles: {n_cycles}")
print(f"Expected thickness: {n_cycles * GPC

# Cycle timing at 80°C (conservative for perovskite stability)
t_TMA_pulse = 0.1    # s (TMA dose — saturate surface)
t_TMA_purge = 30.0   # s (extended purge for perovskite: remove TMA excess)
t_H2O_pulse = 0.1    # s (H2O dose)
t_H2O_purge = 30.0   # s (extended purge to remove H2O — critical for perovskite)
cycle_time = t_TMA_pulse + t_TMA_purge + t_H2O_pulse + t_H2O_purge
total_time = n_cycles * cycle_time
print(f"\nCycle time: {cycle_time:.1f} s")
print(f"Total deposition time: {total_time:.1f} min")
```

**Process recipe:**
- Temperature: 80°C (perovskite decomposition threshold ~130°C; 80°C provides safety margin)
- TMA pulse: 0.1 s; purge 30 s in N₂ (2 sccm)
- H₂O pulse: 0.1 s; purge 30 s in N₂
- Repeat for 48 cycles → 5.0 nm target

**Film verification protocol:**
1. Ellipsometry: measure thickness on Si witness wafer (same load); verify GPC within ±10%.
2. XPS: Al 2p binding energy at 74.3 eV confirms Al2O3 (not metallic Al or Al(OH)₃).
3. Cross-section TEM: verify conformal coverage at grain boundaries and pinhole absence (critical for passivation function).
4. Device test: compare PCE stability (damp heat: 85°C/85% RH per IEC 61215) with and without Al2O3 — target 20% PCE retention improvement at 500h.

[RISK] TMA is pyrophoric — self-ignites on air exposure. All TMA handling must be through automated ALD precursor lines. Never manually open TMA ampoules outside of inert atmosphere.

---

