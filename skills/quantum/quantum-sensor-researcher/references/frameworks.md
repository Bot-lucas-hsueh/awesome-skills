## § 7 — Standards & Reference

**Key Sensitivity Limits and Metrics**

- **Standard Quantum Limit (projection noise)**: δφ_SQL = 1/√N per measurement. For gravimetry: δg = δφ/(k_eff·T²) where k_eff = 2×(2π/λ) and T is free-fall time.
- **Heisenberg Limit**: δφ_HL = 1/N. Only achievable with maximally entangled (GHZ) states. Realistic squeezing provides δφ_sq = ξ/√N where ξ² < 1 is the Wineland spin squeezing parameter.
- **Quantum Fisher Information**: F_Q bounds sensitivity: δφ ≥ 1/√(n·F_Q) where n is number of measurements. For pure states, F_Q = 4·Var(Ĥ)/ℏ² where Ĥ is the generator.

**Metrics Table**

| Metric | Formula / Definition | Target
|--------|---------------------|------------------------|-------|
| Gravimeter sensitivity | δg = δφ/(k_eff·T²) | 10^−9 g/√Hz (lab), 10^−7 g/√Hz (portable) | T = free-fall time; k_eff = 2×2π/780nm for Rb |
| Gravity gradiometer | Γ = (g₁−g₂)/Δz | 1–10 E/√Hz (1 E = 10^−9 s^−2) | Rejects common-mode laser noise and vibration |
| SQUID field sensitivity | δB = √(S_Φ/A²_eff) | 1–10 fT/√Hz (SQUID + flux concentrator) | S_Φ: flux noise PSD; A_eff: effective loop area |
| NV-center DC sensitivity | δB_DC = 1/(γ_e·C·√(N·T₂)) | 1–100 nT/√Hz (single NV), 1 pT/√Hz (ensemble) | γ_e = 28 GHz/T; C = contrast; N = NV number |
| Optical clock instability | σ_y(τ) = (1/Q)·(1/(SNR·√τ)) | 10^−18 at τ = 10^4 s (Sr, Yb lattice clocks) | Q = ν/Δν; SNR limited by atom shot noise |
| Allan deviation (white noise) | σ_y(τ) = σ_0/√τ | σ_0 = white noise floor | Slope −1/2 on log-log plot |
| Ramsey fringe contrast | C = (P_max − P_min)/(P_max + P_min) | >0.9 in optimized systems | Contrast loss: decoherence, detection noise, inhomogeneous broadening |
| Spin squeezing parameter | ξ² = N·Var(Jz_min)/⟨Jx⟩² | ξ² < 1 for squeezing; >−10 dB achieved | Wineland parameter; sets factor of improvement below SQL |
| Atom shot noise | δN/N = 1/√N | N ~ 10^6 atoms: δN/N ~ 10^−3 | Fundamental Poissonian counting noise |

---
