# CMC Development Guide

> **Scope:** Chemistry, Manufacturing, and Controls  
> **Standards:** ICH Q8-Q12, FDA Guidance for Industry

---

## CMC Development Lifecycle

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CMC DEVELOPMENT PHASES                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Phase 1 (IND-Enabling)                                                 │
│  ├── Drug Substance: Non-GMP or early GMP, fit-for-purpose quality      │
│  ├── Drug Product: Clinical trial material (CTM)                        │
│  ├── Specifications: Limited, focused on safety                         │
│  └── Stability: Initial data to support clinical hold                   │
│                              ↓                                          │
│  Phase 2 (Dose-Ranging)                                                 │
│  ├── Drug Substance: GMP, defined process                               │
│  ├── Drug Product: Registration-enabling formulation                    │
│  ├── Specifications: Expanding based on batch history                   │
│  └── Stability: ICH conditions initiated                                │
│                              ↓                                          │
│  Phase 3 (Pivotal)                                                      │
│  ├── Drug Substance: Commercial-ready process                           │
│  ├── Drug Product: Final commercial formulation                         │
│  ├── Specifications: Full release criteria                              │
│  └── Stability: Primary stability batches                               │
│                              ↓                                          │
│  Registration (PPQ)                                                     │
│  ├── Process Performance Qualification (PPQ) batches                    │
│  ├── Validation protocol execution                                      │
│  ├── Tech transfer to commercial site                                   │
│  └── Commercial supply chain qualification                              │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Drug Substance (API) Development

### Synthetic Route Selection

**Criteria for Selection:**
| Factor | Phase 1 | Phase 3/Commercial |
|--------|---------|-------------------|
| **Scalability** | Gram to 100g | kg to metric tons |
| **Number of Steps** | Fewer critical | Optimized, cost-effective |
| **Raw Materials** | Available | Commercially viable, dual sourcing |
| **Impurity Profile** | Understood | Controlled, specifications set |
| **Yields** | Acceptable | Optimized (>80% typical) |
| **Environmental** | Considered | Green chemistry principles |

### Process Development Stages

```
Stage 1: Route Scouting
• Literature review
• Multiple synthetic approaches evaluated
• Patent landscape analysis
• Key: Identify viable route to API

Stage 2: Process Optimization
• Reaction condition optimization
• Workup and isolation refinement
• Crystallization development
• Key: Define Design Space (QbD)

Stage 3: Scale-Up
• Lab scale (g) → Pilot scale (kg) → Commercial (MT)
• Equipment matching
• Heat/mass transfer considerations
• Key: Demonstrate process control

Stage 4: Process Validation
• Process Performance Qualification (PPQ)
• Three consecutive successful batches
• Statistical process control
• Key: Confirm process capability
```

### Quality Attributes

**Critical Quality Attributes (CQAs):**
| CQA | Test Method | Acceptance Criteria | Risk |
|-----|-------------|---------------------|------|
| **Identity** | IR, NMR, MS | Matches reference | Critical |
| **Purity** | HPLC | ≥98.0% | Critical |
| **Impurities** | HPLC | Total ≤2.0%, Individual ≤0.15% | High |
| **Residual Solvents** | GC | ICH Q3C limits | High |
| **Chirality** | HPLC/chiral | Enantiomeric excess ≥99.5% | Critical |
| **Particle Size** | Laser diffraction | D90 < X μm | Medium |
| **Polymorph** | XRPD | Form [X] only | High |
| **Residual Metals** | ICP-MS | ICH Q3D limits | High |

---

## Drug Product Development

### Formulation Development by Phase

**Phase 1 (First in Human):**
```
Primary Considerations:
• Speed to clinic (formulation simplicity)
• Solubility enhancement (if BCS Class II/IV)
• Stability through clinical duration
• Ease of manufacture

Typical Formulations:
• Simple capsules with API + filler
• Solutions/suspensions
• Basic tablet if high dose
• Minimal excipient screening
```

**Phase 2 (Proof of Concept):**
```
Development Activities:
• Preformulation characterization complete
• Excipient compatibility studies
• Forced degradation studies
• Container closure selection
• In vitro dissolution method development

Formulation Goals:
• Registration-enabling formulation identified
• Stability data initiated
• PK bridging to Phase 1
• Manufacturing process defined
```

**Phase 3 (Pivotal/Commercial):**
```
Finalization Activities:
• Commercial formulation locked
• Process Design Space defined
• Bioequivalence to Phase 2 formulation
• Primary stability batches
• Process validation protocol

Commercial Readiness:
• Tech transfer to commercial site
• Equipment qualification
• PPQ batch execution
• Regulatory filing preparation
```

### Dosage Form Selection

| Factor | Oral Solid | Oral Liquid | Parenteral | Topical |
|--------|-----------|-------------|------------|---------|
| **API Properties** | Stable, acceptable solubility | Poor stability, dosing flexibility | Insoluble, immediate effect needed | Local effect |
| **Patient Population** | Adults, chronic therapy | Pediatric, geriatric | Hospital, acute | Localized |
| **Dose** | Medium-high | Variable | Low-medium | Low |
| **Manufacturing** | Well-established, scalable | Moderate complexity | High complexity, aseptic | Moderate |
| **Stability** | Generally good | Shorter shelf life | Often frozen/lyophilized | Variable |

### Manufacturing Process

**Tablet Manufacturing:**
```
Wet Granulation Route:
API + Excipients → Pre-blending → Granulation (binder solution)
    → Wet sizing → Drying → Dry sizing → Final blending
    → Compression → Coating (optional) → Packaging

Direct Compression Route (if flow compressibility acceptable):
API + Excipients → Blending → Compression → Coating → Packaging

Critical Process Parameters (CPPs):
• Granulation endpoint (torque/power)
• Drying temperature/residence time
• Blend uniformity (RSD < 5%)
• Compression force/hardness
• Disintegration/dissolution
```

**Sterile Manufacturing:**
```
Routes:
1. Terminal Sterilization (if API heat-stable)
   Fill → Seal → Autoclave → Inspection

2. Aseptic Processing (most biologics, heat-sensitive)
   API sterilization (filtration) → Aseptic fill → Aseptic seal
   → Inspection

Critical Controls:
• Grade A environment (ISO 5) for fill/finish
• Grade B background (ISO 7)
• Media fill validation (simulated runs)
• Container closure integrity testing
• Endotoxin control
```

---

## Quality by Design (QbD)

### ICH Q8-Q12 Framework

```
Quality Target Product Profile (QTPP)
                ↓
Critical Quality Attributes (CQAs)
                ↓
Risk Assessment (ICH Q9)
                ↓
Critical Process Parameters (CPPs)
                ↓
Design of Experiments (DoE)
                ↓
Control Strategy
                ↓
Continual Improvement (ICH Q10)
```

### Design Space

**Definition:** Multidimensional region of process parameters where the process can operate while still assuring quality.

**Example - Tablet Compression:**
```
Design Space:
┌──────────────────────────────────────────────────────┐
│ Compression Force: 8-15 kN                           │
│ Tablet Hardness: 50-100 N                            │
│ Disintegration: <15 minutes                          │
│ Friability: <1%                                      │
└──────────────────────────────────────────────────────┘

Normal Operating Range (NOR):
  Compression Force: 10-12 kN (subset of Design Space)

Proven Acceptable Range (PAR):
  Compression Force: 8-15 kN (edge of Design Space)
```

### Control Strategy Elements

| Control | Method | Frequency | Specification |
|---------|--------|-----------|---------------|
| **Input Materials** | COA verification | Each lot | Vendor qualification |
| **In-Process** | Blend uniformity | Each batch | RSD < 5% |
| **In-Process** | Tablet weight | Continuous | ±5% of target |
| **In-Process** | Hardness | Continuous | 50-100 N |
| **Release Testing** | Assay | Each batch | 95.0-105.0% |
| **Release Testing** | Dissolution | Each batch | Q=80% in 30 min |
| **Stability** | Long-term | Annual | Trend analysis |

---

## Stability Studies

### ICH Stability Conditions

| Study | Condition | Duration | Batch Requirement |
|-------|-----------|----------|-------------------|
| **Long-term** | 25°C ± 2°C / 60% RH ± 5% | Through shelf life | Minimum 3 batches |
| **Intermediate** | 30°C ± 2°C / 75% RH ± 5% | 12 months | If significant change |
| **Accelerated** | 40°C ± 2°C / 75% RH ± 5% | 6 months | Minimum 3 batches |
| **Freeze-thaw** | -20°C to 25°C | 3 cycles | For frozen products |
| **Light** | ICH Q1B | As appropriate | Photostability |

### Stability Protocol

```
Stability Study Design:

Primary Batches (3 commercial scale):
├─ Long-term (25°C/60%RH): 0, 3, 6, 9, 12, 18, 24, 36 months
├─ Accelerated (40°C/75%RH): 0, 3, 6 months
└─ Intermediate (30°C/75%RH): If needed

Testing Schedule:
T0 (Initial):
  ├─ Appearance
  ├─ Assay
  ├─ Degradation products
  ├─ Dissolution (drug product)
  ├─ Moisture (if applicable)
  └─ Microbial limits (if applicable)

T3, T6, T9, T12, etc.:
  ├─ All T0 tests
  └─ Additional as defined in protocol

Significant Change Criteria:
• 5% change in assay from initial
• Failure to meet dissolution specification
• Failure to meet physical specification
• Failure to meet microbial specification
```

### Stability Data Analysis

**Shelf Life Determination:**
```
Statistical Methods:
1. Zero-order kinetics: t90 = (Initial - 90%) / Rate

2. Arrhenius equation (for extrapolation):
   k = A × exp(-Ea/RT)
   Where: k = rate constant, Ea = activation energy

3. Regression analysis:
   - 95% confidence interval of regression line
   - Shelf life = time to intersection with acceptance criteria
```

---

## Tech Transfer

### Technology Transfer Phases

```
Phase 1: Planning
├─ Transfer protocol development
├─ Gap analysis (sending vs receiving site)
├─ Equipment comparison
└─ Risk assessment

Phase 2: Pre-transfer Activities
├─ Raw material qualification at receiving site
├─ Equipment qualification
├─ Analytical method transfer
└─ Personnel training

Phase 3: Transfer Execution
├─ Engineering batches (process verification)
├─ Comparative analysis (sending vs receiving)
├─ Process adjustment if needed
└─ Documentation updates

Phase 4: Post-transfer
├─ PPQ batch execution
├─ Validation report
├─ Commercial supply qualification
└─ Knowledge management
```

### Analytical Method Transfer

**Acceptance Criteria (per USP <1224>):**
| Parameter | Acceptance | Method |
|-----------|-----------|--------|
| **Accuracy** | 98-102% recovery | Spike recovery |
| **Precision** | RSD ≤ 2% | Repeatability |
| **Intermediate Precision** | RSD ≤ 3% | Different days, analysts |
| **Specificity** | No interference | Placebo, degradation |
| **Detection Limit** | S/N ≥ 3 | LOD |
| **Quantitation Limit** | S/N ≥ 10 | LOQ |

**Transfer Types:**
- **Comparative Testing:** Both sites test same samples
- **Co-validation:** Both sites participate in validation
- **Validation at receiving site:** Full validation repeated
- **Transfer waiver:** Justification for no transfer needed

---

## Regulatory Filing Requirements

### CMC Section Checklist (NDA/BLA)

**Module 3.2.S - Drug Substance:**
- [ ] S.1.1: Nomenclature (INN, CAS, etc.)
- [ ] S.1.2: Structure (molecular formula, weight)
- [ ] S.1.3: General properties (solubility, pKa)
- [ ] S.2.1: Manufacturer name and address
- [ ] S.2.2: Detailed manufacturing process
- [ ] S.2.3: Control of starting materials
- [ ] S.2.4: Control of intermediates
- [ ] S.2.5: Process validation summary
- [ ] S.3.1: Structure elucidation data
- [ ] S.3.2: Impurity profile and qualification
- [ ] S.4: Specifications and analytical procedures
- [ ] S.5: Reference standard characterization
- [ ] S.6: Container closure description
- [ ] S.7: Stability data and protocol

**Module 3.2.P - Drug Product:**
- [ ] P.1: Composition (all components)
- [ ] P.2: Pharmaceutical development summary
- [ ] P.3: Manufacturing process and validation
- [ ] P.4: Excipient specifications
- [ ] P.5: Drug product specifications
- [ ] P.6: Reference standard
- [ ] P.7: Container closure
- [ ] P.8: Stability data and protocol

---

*Reference: ICH Q8(R2) Pharmaceutical Development, ICH Q11 Development and Manufacture of Drug Substances*
