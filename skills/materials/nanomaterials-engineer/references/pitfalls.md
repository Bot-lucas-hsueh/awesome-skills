## § 10 Common Pitfalls

### Anti-Pattern 1 — Skipping Size Histogram Statistics

❌ **BAD:**
```
"The TEM shows nanoparticles of approximately 5 nm."
(From visual inspection of 5–10 particles, no statistics)
```

✅ **GOOD:**
```python
# ImageJ automated particle measurement (>300 particles)
# Results: mean = 5.2 nm, std = 0.8 nm, n = 347 particles
# Coefficient of variation (CV) = 0.8/5.2 = 15.4%
# Conclusion: polydisperse (CV > 10%) — synthesis optimization needed
```

**Why it matters:** Single-particle visual inspection is scientifically invalid. Size distribution determines optical, electrical, and biological properties. A "5 nm" material with σ = 2 nm behaves fundamentally differently from one with σ = 0.3 nm.

---

### Anti-Pattern 2 — Measuring QY with Incorrect Optical Density

❌ **BAD:**
```python
# Measuring QY at OD = 0.8 — inner filter effect corrupts measurement
qy = measure_quantum_yield(sample_OD=0.8, reference_OD=0.05)
# Result artificially low: 45% (true QY: ~80%)
```

✅ **GOOD:**
```python
# Correct: both sample and reference at OD < 0.1 at excitation wavelength
# Dilute sample to OD = 0.05–0.1; use same OD for both sample and reference
# QY = QY_ref * (I_s/I_ref) * (A_ref/A_s) * (n_s/n_ref)^2
qy = measure_quantum_yield(sample_OD=0.07, reference_OD=0.07)
# Result: 78% (accurate)
```

**Why it matters:** Inner filter effect at OD > 0.1 causes reabsorption of emitted photons, systematically underestimating quantum yield by 30–60%.

---

### Anti-Pattern 3 — Sonication Damage During CNT Dispersion

❌ **BAD:**
```
Sonicate MWCNT in DMF for 60 minutes at 400 W probe sonicator
(Cuts nanotubes; shortens aspect ratio from 1000:1 to 20:1; degrades
conductivity; introduces sp³ defects — D/G ratio increases from 0.1 to 0.8)
```

✅ **GOOD:**
```
Bath sonication at 40 W for 30 min maximum; or mild shear mixing
(IKA T25 at 10,000 rpm for 20 min); verify aspect ratio by TEM
before and after dispersion. Use surfactant (SDS, 2 mg/mL) or
tip-functionalized COOH-MWCNT to enable dispersion at lower energy input.
```

**Why it matters:** Probe sonication above 200 W·min/mg of CNT shortens nanotubes by mechanical scission, destroying the high-aspect-ratio morphology that provides electrical percolation and mechanical reinforcement.

---

### Anti-Pattern 4 — Ignoring Nucleation Delay in ALD on Non-Oxide Surfaces

❌ **BAD:**
```
Assume 50 cycles × 1.0 Å/cycle = 5.0 nm Al2O3 on CNT or graphene surface
(Actual: 20-cycle nucleation delay → only 3.0 nm deposited; non-uniform coverage)
```

✅ **GOOD:**
```python
# Characterize nucleation delay with witness Si wafer and functionalized target
# Al2O3 on bare graphene: ~15-20 cycle nucleation delay
# Fix: NO2 functionalization at 120°C for 10 min before ALD
# OR UV-ozone treatment 5 min to create oxide seed sites

nucleation_delay = 18  # cycles (measured on graphene)
GPC_after = 1.05  # Å/cycle after nucleation
target_nm = 5.0
total_cycles = int(np.ceil(target_nm * 10
print(f"Total cycles needed: {total_cycles} (including {nucleation_delay} cycle delay)")
```

**Why it matters:** Unacknowledged nucleation delay produces films 30–40% thinner than calculated, with non-uniform coverage and pinholes that destroy passivation function.

---

### Anti-Pattern 5 — Using Cd-Containing QDs for Biological Applications Without Passivation

❌ **BAD:**
```
Apply bare CdSe QDs directly in cell culture at 10 nM
(Cd²⁺ leaching at physiological pH: ~0.5 µM Cd released;
IC50 for HeLa cells ~0.2 µM Cd²⁺ → acute cytotoxicity)
```

✅ **GOOD:**
```
Three-layer protection strategy:
1. ZnS shell (3 ML): reduces Cd²⁺ leaching 100-fold
2. Amphiphilic polymer coating (PMA or PEG-DSPE): additional barrier
3. Biocompatibility test: MTS/MTT assay at application concentration
   for 24h, 48h, 72h before any in vitro experiment
Alternatively: switch to InP/ZnSe or carbon dots for biomedical use
```

**Why it matters:** CdSe QDs release cytotoxic Cd²⁺ under oxidative or low-pH conditions. Using them without rigorous passivation in biological contexts violates both ethical standards and REACH biocide regulations.

---

### Anti-Pattern 6 — Reporting BET Surface Area Without Outgassing Validation

❌ **BAD:**
```
Run BET measurement on as-received CNT powder without outgassing
(Physisorbed water and solvent occupy micropores; measured BET = 180 m²/g;
true BET after proper outgassing = 320 m²/g)
```

✅ **GOOD:**
```
Outgas sample at 200°C under vacuum (<10⁻² mbar) for 12h before BET
Verify complete outgassing: check that degas pressure plateaus
Run multipoint BET (5+ pressure points, 0.05 < P/P₀ < 0.30)
Report: BET SA = 318 ± 8 m²/g (n=3 replicate measurements)
```

**Why it matters:** Inadequate outgassing understates BET surface area by 30–70%, leading to incorrect catalyst loading calculations, underestimation of active site density, and invalid structure-property relationships.

---

