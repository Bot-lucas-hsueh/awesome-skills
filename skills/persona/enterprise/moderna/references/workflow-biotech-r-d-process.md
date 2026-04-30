## §3 · Workflow: Biotech R&D Process

### §3.1 · Design-Build-Test-Learn (DBTL) Cycle

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MODERNA DBTL CYCLE (8-12 weeks)                         │
└─────────────────────────────────────────────────────────────────────────────┘

PHASE 1: DESIGN (Weeks 1-2)
┌─────────────────────────────────────────────────────────────────────────────┐
│ INPUTS                          │ OUTPUTS                                  │
├─────────────────────────────────┼──────────────────────────────────────────┤
│ • Target protein sequence       │ • Optimized mRNA sequence                │
│ • Expression requirements       │ • LNP formulation design                 │
│ • Disease biology               │ • In silico immunogenicity report        │
│ • Platform precedents           │ • Manufacturing process outline          │
├─────────────────────────────────┼──────────────────────────────────────────┤
│ ACTIVITIES:                     │ DECISION GATE:                           │
│ • Codon optimization algorithm  │ Sequence approved by computational       │
│ • UTR selection from library    │ biology and immunology?                  │
│ • Secondary structure analysis  │ If NO → iterate design                   │
│ • Immunogenicity screening      │ If YES → proceed to Build                │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
PHASE 2: BUILD (Weeks 3-4)
┌─────────────────────────────────────────────────────────────────────────────┐
│ INPUTS                          │ OUTPUTS                                  │
├─────────────────────────────────┼──────────────────────────────────────────┤
│ • Approved sequence             │ • Research-grade mRNA                    │
│ • LNP formulation parameters    │ • LNP-mRNA formulation                   │
│ • Automated workflows           │ • QC release data                        │
├─────────────────────────────────┼──────────────────────────────────────────┤
│ ACTIVITIES:                     │ DECISION GATE:                           │
│ • Gene synthesis (API to Twist) │ Formulation meets CQAs?                  │
│ • IVT production (Tecan)        │ (Size, PDI, encapsulation, endotoxin)    │
│ • Microfluidic LNP formulation  │ If NO → reformulate                      │
│ • QC testing (DLS, HPLC, qPCR)  │ If YES → proceed to Test                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
PHASE 3: TEST (Weeks 5-8)
┌─────────────────────────────────────────────────────────────────────────────┐
│ INPUTS                          │ OUTPUTS                                  │
├─────────────────────────────────┼──────────────────────────────────────────┤
│ • Formulated mRNA-LNP           │ • Expression data (Western, Flow)        │
│ • In vitro models               │ • Immunogenicity profile                 │
│ • In vivo models (rodent)       │ • PK/PD parameters                       │
├─────────────────────────────────┼──────────────────────────────────────────┤
│ ACTIVITIES:                     │ DECISION GATE:                           │
│ • Cell-based expression assays  │ Does candidate meet success criteria?    │
│ • Flow cytometry analysis       │ If NO → kill or redesign                 │
│ • Rodent expression study       │ If YES → proceed to Learn                │
│ • Immunogenicity assessment     │                                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
PHASE 4: LEARN (Weeks 9-12)
┌─────────────────────────────────────────────────────────────────────────────┐
│ INPUTS                          │ OUTPUTS                                  │
├─────────────────────────────────┼──────────────────────────────────────────┤
│ • All experimental data         │ • Updated platform knowledge base        │
│ • Comparative analysis          │ • Design algorithm improvements          │
│ • Failure modes                 │ • Published insights (if appropriate)    │
├─────────────────────────────────┼──────────────────────────────────────────┤
│ ACTIVITIES:                     │ DECISION GATE:                           │
│ • Data integration & analysis   │ Advance to IND-enabling studies?         │
│ • Feedback to design algorithms │ If NO → archive learnings                │
│ • Platform model updates        │ If YES → initiate GLP tox, CMC scale-up  │
│ • Documentation in Benchling    │                                          │
└─────────────────────────────────────────────────────────────────────────────┘

CYCLE TIME TARGET: <4 weeks for respiratory programs
                   <8 weeks for novel targets
```

### §3.2 · Clinical Development Pathway

```
PRE-CLINICAL → IND → PHASE 1 → PHASE 2 → PHASE 3 → BLA → APPROVAL
   │           │        │         │         │        │       │
   │           │        │         │         │        │       └── Launch
   │           │        │         │         │        │          preparation
   │           │        │         │         │        └── Advisory
   │           │        │         │         │           committee
   │           │        │         │         │
   │           │        │         │         └── Pivotal efficacy
   │           │        │         │             (n=1000s)
   │           │        │         └── Dose selection,
   │           │        │             proof of concept
   │           │        │             (n=100s)
   │           │        └── Safety,
   │           │           immunogenicity
   │           │           (n=10s)
   │           └── Chemistry, Manufacturing,
   │               Controls (CMC) readiness
   └── GLP toxicology,
       GMP manufacture
       (6-12 months)

MODERNA PARALLEL TRACKING:
Unlike traditional pharma, Moderna runs CMC, preclinical, and regulatory in parallel:
┌─────────────────────────────────────────────────────────────────────────────┐
│ Traditional: Design → Build → Test → CMC → Toxicology → IND → Phase 1      │
│ Time: 3-5 years                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│ Moderna:                                                                     │
│   Design                                                                     │
│      ↓                                                                       │
│   ┌──────────┬──────────┬──────────┐                                        │
│   │ Build    │ CMC Dev  │ Tox Plan │  ← Parallel streams                    │
│   └────┬─────┴────┬─────┴────┬─────┘                                        │
│        ↓          ↓          ↓                                               │
│   ┌─────────────────────────────────┐                                        │
│   │ Integrated IND Package          │                                        │
│   └─────────────────────────────────┘                                        │
│ Time: 12-18 months for platform programs                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### §3.3 · Commercial Launch Workflow

```
LAUNCH READINESS CHECKPOINTS (L-18 to L-0)

L-18 Months (Clinical Data Lock)
┌─────────────────────────────────────────────────────────────────────────────┐
│ □ Topline Phase 3 data available                                           │
│ □ Regulatory strategy confirmed (FDA, EMA, others)                         │
│ □ Manufacturing capacity secured                                           │
│ □ Health economics & outcomes research (HEOR) initiated                    │
└─────────────────────────────────────────────────────────────────────────────┘

L-12 Months (Regulatory Submission)
┌─────────────────────────────────────────────────────────────────────────────┐
│ □ BLA/MAA submitted                                                        │
│ □ Payer engagement initiated                                               │
│ □ Medical affairs team trained                                             │
│ □ Distribution partnerships signed                                         │
└─────────────────────────────────────────────────────────────────────────────┘

L-6 Months (Approval Anticipated)
┌─────────────────────────────────────────────────────────────────────────────┐
│ □ Launch inventory manufactured and released                               │
│ □ Sales force trained and deployed                                         │
│ □ Marketing materials approved (MLR)                                       │
│ □ Patient support program established                                      │
└─────────────────────────────────────────────────────────────────────────────┘

L-0 (Launch)
┌─────────────────────────────────────────────────────────────────────────────┐
│ □ Product available for ordering                                           │
│ □ HCP education campaign active                                            │
│ □ Real-world evidence collection initiated                                 │
│ □ Pharmacovigilance system monitoring                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---
