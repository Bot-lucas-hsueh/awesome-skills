## § 7 — Standards & Reference

### 7.1 Promoter Strength Standards

| Promoter / 启动子 | Strength (RPU) / 强度 | Application
|------------------|----------------------|----------------------|
| BBa_J23119 (constitutive) | 1.0 RPU (reference) | Highest constitutive expression in E. coli |
| BBa_J23101 | 0.36 RPU | Medium constitutive; low metabolic burden |
| BBa_J23105 | 0.07 RPU | Low constitutive; toxic genes, fine-tuning |
| T7lac (inducible, IPTG) | 5–20 RPU induced | High-level recombinant protein production |
| araBAD (inducible, arabinose) | 0.5–3 RPU induced | Titratable expression; avoids "all-or-none" effect |
| Trc (hybrid) | 2–5 RPU induced | Industrial E. coli expression; IPTG-inducible |

### 7.2 Key Metabolic Engineering Metrics

| Metric / 指标 | Formula / 公式 | Target / 目标范围 | Notes
|--------------|---------------|-----------------|-------------|
| **Titer** | g product / L culture | >1 g/L (lab), >50 g/L (industrial) | Final product concentration |
| **Yield (Y_P/S)** | g product / g substrate | >30% theoretical | Carbon conversion efficiency |
| **Productivity (q_p)** | g product / L / h | >0.5 g/L/h (lab) | Space-time yield for bioprocess |
| **Specific growth rate (μ)** | ln(X2/X1) / (t2-t1) | 0.1–0.5 h⁻¹ | Exponential phase rate |
| **Oxygen uptake rate (OUR)** | mmol O2 / L / h | <80 mmol/L/h (practical limit) | Constrains aerobic fermentation density |
| **Carbon molar yield (Cmol)** | Cmol product / Cmol substrate | >0.5 Cmol | Atom economy |

### 7.3 CRISPR Design Decision Tree

```
Target gene editing needed?
├── Simple knockout (loss-of-function)?
│   └── → CRISPR-Cas9 + NHEJ (bacteria: no NHEJ → use λ-Red recombination)
├── Precise knockin or point mutation?
│   └── → Cas9 + HDR with 800 bp homology arms; or Base Editor (C→T, A→G)
├── Transcriptional repression (no cutting)?
│   └── → dCas9-KRAB (CRISPRi); ~10–100× repression
├── Multiplex editing (3+ targets simultaneously)?
│   └── → Cas12a (Cpf1) array; single crRNA array drives multiple cuts
└── RNA knockdown?
    └── → Cas13d (CasRx); targets mRNA without DNA DSB
```
