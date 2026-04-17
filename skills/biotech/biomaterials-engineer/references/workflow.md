# Standard Workflow

## 8.1 Biomaterials Development Pipeline

```
Phase 1: Clinical Requirements & Material Selection (Weeks 1–3)
├── Clinical application defined: anatomy, load, duration, degradation target
├── Host tissue properties documented: E, σ_y, σ_UTS, site-specific requirements
├── Material class selected: polymer / ceramic / metal / composite / hydrogel
├── Specific polymer/metal grade identified: trade name, supplier, CAS number
├── Degradation timeline established: initial mechanical support + resorption rate
└── Regulatory pathway determined: FDA 510(k) predicate, De Novo, or PMA

Phase 2: Scaffold Design & Fabrication (Weeks 3–8)
├── Pore architecture: porosity (60–80%), pore size (200–500 μm), interconnectivity
├── Permeability calculation: Kozeny-Carman, target ≥ 10⁻¹¹ m²
├── Fabrication method selected: AM (FDM/SLA/SLS) or conventional (salt leaching/freeze-dry)
├── Build parameters optimized: layer resolution, annealing, post-processing
└── Prototype batch: minimum 5 samples per test condition

Phase 3: Characterization — Baseline (Weeks 6–10)
├── Morphology: SEM, microCT (porosity, pore size, strut thickness)
├── Surface chemistry: XPS, water contact angle
├── Mechanical: compressive / tensile / flexural per ASTM standards
├── Degradation: Mn (GPC) and weight loss vs. time in PBS (pH 7.4, 37°C)
└── Sterilization (if applicable): pre- and post-sterilization comparison

Phase 4: Biocompatibility Testing (Weeks 9–16)
├── Extract preparation: ISO 10993-12 (surface area 6 cm²/mL, 37°C, 24h)
├── Cytotoxicity: L929 MTT assay (ISO 10993-5), ≥70% viability at 100% extract
├── Sensitization: LLNA or GPMT (ISO 10993-10) if implant > 30 days
├── Implantation: rat subcutaneous or relevant site model (ISO 10993-6), 4 + 12 weeks
└── Genotoxicity (if novel material): Ames test + chromosomal aberration (ISO 10993-3)

Phase 5: Regulatory Submission & Validation (Weeks 16–24)
├── Chemical characterization report: all materials, processing aids, residual solvents
├── Toxicological risk assessment: AET threshold, TTC for unidentified peaks
├── Sterilization validation: SAL 10⁻⁶ per ISO 11135 or ISO 11137
├── Shelf-life / accelerated aging: ASTM F1980 (55°C / 50% RH equivalent)
└── 510(k) or De Novo submission preparation
```

## 8.2 Material Selection Decision Workflow

```
Step 1: Define clinical requirements
├── Anatomical site: bone / cartilage / vascular / neural / dermal
├── Load requirement: high (>10 GPa), moderate (0.1–10 GPa), low (<0.1 GPa)
├── Degradation need: degradable (weeks–months–years) or permanent
├── Drug/growth factor delivery: yes/no; burst vs. sustained profile
└── Sterilization compatibility: EtO, gamma, e-beam, autoclave

Step 2: Screen material candidates
├── Match E_modulus to host tissue (modulus-match for stress shielding avoidance)
├── Match degradation rate to tissue regeneration timeline
├── Verify biocompatibility: check ISO 10993 history for similar materials
└── Check regulatory precedent: is there a cleared predicate with this material?

Step 3: Validate with fabrication constraints
├── Does the material process well with your chosen method?
│   ├── FDM: PCL, PLGA, PLA (thermoplastic)
│   ├── SLA: PEGDA, photo-crosslinkable polymers
│   ├── SLS: PEEK, HA/TCP (powder-based)
│   ├── Electrospinning: PCL, PLGA (solution-based)
│   ├── Salt leaching: any solvent-soluble polymer
└── Sterilization effect on properties: gamma vs. EtO vs. e-beam trade-offs

Step 4: Risk assessment
├── Toxicological risk assessment for all processing chemicals
├── Residual monomer / solvent risk
├── Degradation product risk (acidic PLGA products in avascular sites)
└── Metal ion release risk (Ti, Co, Cr for metal implants)
```

## 8.3 PLGA Scaffold Degradation Characterization Workflow

```
Week 0 (Baseline):
├── GPC: Mn0, Mw0, PDI0
├── Weight: W0
├── Mechanical: compressive modulus E0, strength σ0
└── Sterilize (EtO preferred; gamma only if validated)

Weeks 2, 4, 6, 8, 12 (Kinetic points):
├── Incubate in PBS pH 7.4, 37°C, gentle agitation
├── Retrieve samples: blot dry, weigh (W_t)
├── GPC: Mn_t, Mw_t, PDI_t
├── Mechanical: E_t, σ_t (same test conditions as Week 0)
└── pH measurement of immersion medium (acidification = degradation)

Analysis:
├── Weight loss % = (W0 - W_t) / W0 × 100
├── Mn retention % = Mn_t / Mn0 × 100
├── Mechanical retention % = E_t / E0 × 100
└── Plot: Mn(t), weight(t), E(t) on same timeline

Pass criteria:
├── No catastrophic loss of mechanical properties before Week 8 (bone ingrowth minimum)
├── Weight loss < 20% at Week 4 (maintains scaffold integrity)
└── pH drop < 1.0 unit from baseline (no excessive autocatalytic acidification)
```

## 8.4 ISO 10993 Biocompatibility Test Plan Workflow

```
For each device/material, build a Biological Evaluation Plan (BEP):

Step 1: Device categorization
├── Nature of body contact: surface / external communicating / implant
├── Duration of contact: limited (<24h) / prolonged (24h–30d) / permanent (>30d)
└── Intended anatomical location

Step 2: Risk-based test selection (per ISO 10993-1:2018 Table A.1)
├── Start with material characterization (ISO 10993-18) — always required
├── Conduct toxicological risk assessment (TRA) on all chemical constituents
├── Identify gaps: what endpoints are NOT covered by existing data?
└── Select only the tests that address remaining risks

Step 3: Extract preparation (ISO 10993-12)
├── Extraction ratios: 6 cm²/mL (solids), 3 cm²/mL (porous)
├── Extraction conditions: polar (serum-free DMEM or saline), non-polar (sesame oil)
├── Temperature: 37°C/24h (standard), 37°C/72h (aggressive), 50°C/72h (accelerated)
└── Document exact surface area measurement method

Step 4: Cytotoxicity testing (ISO 10993-5)
├── Cell line: L929 (murine fibroblast), ATCC CCL-1
├── Method: MTT or XTT assay, 24h exposure
├── Dilutions: 100%, 50%, 25%, 12.5%, 6.25% extract in culture medium
└── Pass criterion: ≥70% cell viability at 100% extract concentration

Step 5: Results interpretation
├── Grade 0 (≥70% viability): PASS — no cytotoxicity concern
├── Grade 1–2 (60–69%): Borderline — investigate, retest with fresh batch
├── Grade 3–4 (<50%): FAIL — reformulate material; investigate leachables
└── Document all findings in BEP; submit to regulatory
```

## 8.5 Scaffold Fabrication Methods Comparison

| Method | Materials | Porosity | Pore Size | Resolution | Notes |
|--------|-----------|----------|-----------|-----------|-------|
| **FDM (Fused Dep. Modeling)** | PCL, PLGA, PLA | 40–70% | 100–300 μm | ± 100 μm | Good forthermoplastics |
| **SLA (Stereolithography)** | PEGDA, photo-crosslinkable | 50–90% | 50–200 μm | ± 25 μm | High resolution; requires photoinitiator |
| **SLS (Selective Laser Sintering)** | PEEK, HA/TCP, PCL | 30–70% | 200–500 μm | ± 100 μm | No solvent; powder removal can be tricky |
| **Electrospinning** | PCL, PLGA, collagen | 60–90% | 0.5–10 μm | Fiber diameter | Nanofibers; good for skin/nerve |
| **Salt Leaching** | PLGA, PLA, collagen | 60–90% | 100–500 μm | ± 50 μm | Simple; salt removal can be incomplete |
| **Freeze-drying** | Collagen, chitosan, HA | 70–95% | 20–200 μm | Variable | Anisotropic pores; good for aerogels |
| **Bioplotting / 3D Printing** | Alginate, collagen, PEG | 40–80% | 200–800 μm | ± 50 μm | Cell-laden constructs possible |

## 8.6 Regulatory Submission Checklist (FDA 510(k))

- [ ] Device description: all materials, dimensions, manufacturing process
- [ ] Material characterization (ISO 10993-18): all constituent materials, processing aids
- [ ] Toxicological risk assessment: AET threshold, all identified extractables qualified
- [ ] Cytotoxicity (ISO 10993-5): L929, 24h extract, MTT assay, ≥70% viability
- [ ] Sensitization (ISO 10993-10): LLNA or GPMT, as required by risk
- [ ] Implantation (ISO 10993-6): 4-week and 12-week timepoints, histology scoring
- [ ] Genotoxicity (ISO 10993-3): Ames test (required for novel polymers)
- [ ] Sterilization validation (ISO 11135 or ISO 11137): SAL 10⁻⁶
- [ ] Shelf-life / accelerated aging (ASTM F1980): end-of-shelf-life testing
- [ ] Mechanical testing per intended use: ASTM F2077 (spinal), F543 (bone screws)
- [ ] Predicate device comparison: substantial equivalence table
- [ ] Labeling: intended use, contraindications, warnings, instructions for use
