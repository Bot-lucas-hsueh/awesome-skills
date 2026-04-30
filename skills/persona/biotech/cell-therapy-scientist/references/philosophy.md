## § 4 · Core Philosophy

**CAR-T vs. Other Cell Therapy Modality — Selection Framework:**

```
Gate 1: Target antigen expression profile?
  ├── Tumor-specific surface antigen (CD19, BCMA, GD2, HER2, Mesothelin)
  │   └── → CAR-T therapy (direct MHC-independent recognition)
  ├── Intracellular neoantigen
  │   └── → TCR-T therapy (requires HLA matching) or cancer vaccine
  └── ADCC/natural killer ligands (NKG2D ligands, DNAM-1 ligands)
      └── → CAR-NK or NK cell therapy (MHC-independent, lower CRS risk)

Gate 2: Autologous vs. allogeneic?
  ├── Patient has sufficient T cells (TIL >500/μL, CD3 >30%)
  │   ├── Non-urgent → Autologous CAR-T (gold standard, no alloreactivity)
  │   └── Urgent or refractory → Allogeneic CAR-T from healthy donor
  └── Patient is lymphopenic, pediatric, or fraile → Allogeneic preferred

Gate 3: Co-stimulatory domain?
  ├── Hematologic malignancy (ALL, DLBCL, MM) → 4-1BB (CD137): sustained persistence, memory T cells
  ├── Solid tumor (rapid killing priority) → CD28: faster activation, higher peak expansion
  └── Dual co-stimulation: CD28+4-1BB or novel OX40 (investigational, enhanced exhaustion resistance)

Gate 4: Solid tumor consideration?
  ├── Immunosuppressive TME? → Armored CAR (IL-15/IL-21 secreting, PD-1 dominant negative)
  ├── Antigen heterogeneity? → Tandem CAR (bivalent), logic-gated AND-gate CAR
  └── Physical barrier? → Local delivery (intra-tumoral injection, CAR-T + oncolytic virus)

Gate 5: Manufacturing scale?
  ├── Autologous (one patient per run) → Closed-system: Miltenyi CliniMACS Prodigy, Lonza Cocoon
  └── Allogeneic (batch for 10–100 patients) → Stirred-tank bioreactor (Sartorius ambr 250, Wave)
```

**Potency Assay Philosophy:** Cytotoxicity (E:T ratio curve, LDH/xCELLigence) is the gold-standard CAR-T potency surrogate. Always run E:T ratios 1:1, 2.5:1, 5:1, 10:1. Report EC50 (E:T for 50% killing). A product passing VCN and transduction rate but failing potency must not be released regardless of other attributes.
