## § 4 · Core Philosophy

**Material Class Selection — 5-Gate Decision Tree:**

```
Gate 1: Load-bearing requirement?
  ├── High (cortical bone equiv., E > 10 GPa) → Metal (Ti-6Al-4V, CoCr) or PEEK
  ├── Moderate (cancellous equiv., E 0.1–5 GPa) → Porous Ti, PEEK/HA composite, dense HA/TCP
  └── Low (soft tissue, E < 0.1 GPa) → Hydrogel, silicone, ePTFE, electrospun PCL

Gate 2: Biodegradation required?
  ├── Yes, controlled timeline → PLGA (weeks–months), PCL (1–3 years), PLA (6–24 months)
  ├── Yes, very slow → PEEK (non-degradable, radiolucent) → reconsider Gate 2
  └── No (permanent implant) → Ti alloy, CoCr, PEEK, medical silicone

Gate 3: Drug/growth factor delivery?
  ├── Yes, burst + sustained → PLGA microspheres (50:50 for burst, 75:25 for sustained)
  ├── Yes, long-term → PCL or PLGA/PCL blend; osmotic pump; hydrogel reservoir
  └── No → Focus on mechanical and surface properties

Gate 4: Clinical location?
  ├── Bone/orthopedic → HA/TCP ceramic scaffold, porous Ti, PEEK/HA
  ├── Cardiovascular → ePTFE, Dacron, bioresorbable PLA stent, heparin-coated materials
  ├── Neural → PEG/collagen hydrogel, PLGA conduit, conductive PEDOT coatings
  └── Skin/wound → Collagen/chitosan hydrogel, electrospun PCL-gelatin membrane

Gate 5: Additive manufacturing feasible?
  ├── Yes → FDM (PCL, PLGA), SLA (PEGDA hydrogel), SLS (PEEK, HA/TCP), inkjet bioprinting
  └── No (complex chemistry) → Salt leaching, freeze-drying, electrospinning, solvent casting
```

**Degradation Philosophy:** Always design to the degradation-mechanical property curve, not just initial properties. A PLGA 50:50 scaffold at t=0 may have compressive strength 2 MPa, but at 3 weeks (50% Mn loss) it may be ≤0.5 MPa — tissue ingrowth must compensate. Run parallel degradation + mechanical testing at 2, 4, 8, 12 weeks.

**Biocompatibility Philosophy:** ISO 10993-1 requires risk-based testing — not every test for every device. Start with material characterization and toxicological risk assessment (TRA) on all chemical constituents; this may eliminate need for certain in vivo tests and accelerate approval timelines.
