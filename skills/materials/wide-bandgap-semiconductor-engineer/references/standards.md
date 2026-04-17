## § 7 Standards & Reference

**Frameworks:**
- **AEC-Q101** — Stress test qualification for discrete semiconductor devices (automotive grade)
- **IEC 60747** — Semiconductor devices; discrete device testing standards
- **JEDEC JESD24** — High Temperature Reverse Bias and related semiconductor reliability tests

| Metric | Formula | Target Range |
|--------|---------|--------------|
| Breakdown Voltage | V_BR = E_crit × t_drift
| Specific On-Resistance | R_on,sp = (4 × V_BR²)
| Threshold Voltage (Vth) | From I_D–V_GS linear extrapolation | 2–4 V for SiC MOSFET |
| Channel Mobility | μ_ch from I_D = μ_ch × C_ox × (W/L) × (V_GS−Vth) × V_DS | 10–40 cm²/V·s (SiC MOS) |
| Baliga Figure of Merit | BFOM = ε₀ × ε_r × μ_n × E_crit³ | SiC: 400× Si; GaN: 1000× Si |
| 2DEG Sheet Density | n_s from C-V integration or Hall | 0.8–1.2 × 10¹³ cm⁻² (GaN HEMT) |
| Schottky Barrier Height | φ_B from I-V: J = A** × T² × exp(−qφ_B/kT) | 1.0–1.5 eV (Ni on 4H-SiC) |
| Thermal Resistance (die) | R_th,jc = ΔT_jc / P_diss | < 0.5 K/W for TO-247 SiC |
| Switching Losses | E_sw = E_on + E_off from double-pulse test | < 0.5 mJ per cycle at 600 V, 20 A |
| HTGB Pass Criterion | ΔV_th < ±0.5 V; ΔBVDSS < 5%; ΔI_DSS < 5× | Per AEC-Q101 Table 3 |

---

## Phase 1 — Material & Device Design
- Define V_BR, I_D, R_ds(on) targets from system specification
- Calculate drift layer: N_D and t_drift using ionization integral
- Run TCAD (Silvaco ATLAS) to verify breakdown profile and electric field crowding at termination
- [✓ Done]: TCAD BV matches target ±5%; field crowding < 90% of E_crit at termination edge
- [✗ FAIL]: BV < 90% of target; E-field peaks at surface without termination (JTE/FGR design required)

### Phase 2 — Epitaxial Growth & Process
- Specify CVD conditions: temperature, C/Si ratio (=1.0 for 4H-SiC), growth rate, N or Al doping
- Define implantation schedule: p-well (Al), source (N), JFET (N), JTE (Al)
- Activate implants at 1650°C, 30 min in Ar; inspect surface by SEM/AFM
- [✓ Done]: Epitaxial thickness ±3%, doping ±10%; RMS roughness < 1 nm post-anneal
- [✗ FAIL]: BPD density > 1000 cm⁻²; step bunching visible by Nomarski; n-type compensation

### Phase 3 — Gate Oxide & Metallization
- Grow gate oxide by dry O₂ at 1150°C; anneal in NO at 1175°C for 2 h to reduce D_it
- Deposit Ni/Ti source and drain ohmic contacts; anneal at 950°C in Ar
- [✓ Done]: C-V flatband voltage shift < 1 V; contact resistivity < 10⁻⁵ Ω·cm²
- [✗ FAIL]: Oxide fixed charge density > 5×10¹¹ cm⁻²; contact resistivity > 10⁻⁴ Ω·cm²

### Phase 4 — Characterization & Qualification
- Measure V_th, R_ds(on), BV, I_GSS on every die; sort by bin
- Package selected dice; run AEC-Q101: HTGB (1000h, 150°C), HTRB (1000h), TC (−55 to 150°C, 1000 cycles)
- [✓ Done]: All AEC-Q101 criteria met; R_ds(on) shift < 10%, V_th shift < ±0.5 V
- [✗ FAIL]: Any unit fail on BV, I_DSS, or V_th shift exceeding limits

---

