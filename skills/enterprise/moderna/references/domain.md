## §2 · Domain Knowledge

### §2.1 · mRNA Technology Fundamentals

```
mRNA STRUCTURE & FUNCTION
┌─────────────────────────────────────────────────────────────────────────────┐
│ 5' Cap ──► 5' UTR ──► Coding Sequence ──► 3' UTR ──► Poly(A) Tail          │
│   (Cap1)    (Kozak)    (Protein code)    (Stability)    (100-150 nt)       │
└─────────────────────────────────────────────────────────────────────────────┘

SEQUENCE DESIGN PRINCIPLES:
1. Cap Structure: CleanCap (TriLink) for Cap1 - increases translation efficiency 10%
2. 5' UTR: Kozak sequence GCCGCCRCCatgG + Moderna proprietary elements
3. CDS Optimization:
   • Codon optimization for human expression
   • GC content: 45-55%
   • Avoid cryptic splice sites, internal TATA boxes
   • Minimize secondary structure in 5' region
4. 3' UTR: Alpha-globin UTRs for stability + Moderna proprietary elements
5. Poly(A): Precise 100-150 nt length, no heterogeneity

LIPID NANOPARTICLE (LNP) FORMULATION:
┌─────────────────────────────────────────────────────────────────────────────┐
│ Component          │ Typical %   │ Function                                │
├────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ionizable Lipid    │ 50%         │ Encapsulation, endosomal escape         │
│   (SM-102, ALC-0315)             │   (pH-dependent charge)                 │
├────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Helper Phospholipid│ 38.5%       │ Bilayer structure (DSPC)                │
├────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Cholesterol        │ 10%         │ Membrane stability, fluidity            │
├────────────────────┼─────────────┼─────────────────────────────────────────┤
│ PEG-Lipid          │ 1.5%        │ Particle longevity, reduced clearance   │
│   (DMG-PEG 2000)                 │   (PEG shields from immune system)      │
└─────────────────────────────────────────────────────────────────────────────┘

LNP QUALITY ATTRIBUTES:
• Particle Size: 80-100 nm (Dynamic Light Scattering)
• Polydispersity Index (PDI): <0.2 (monodisperse)
• Zeta Potential: Neutral to slightly negative (-10 to +10 mV)
• Encapsulation Efficiency: >90%
• Endotoxin: <0.5 EU/mL
```

### §2.2 · Therapeutic Areas & Pipeline

```
RESPIRATORY FRANCHISE (Commercial Priority)
┌─────────────────────────────────────────────────────────────────────────────┐
│ Program           │ Phase   │ Indication              │ Status             │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ mRNA-1283         │ BLA     │ Next-gen COVID          │ PDUFA: May 31, 2025│
│                   │         │ (Freeze-dried stable)   │                    │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ mRNA-1083         │ BLA     │ Flu + COVID combo       │ Filed (50+ adults) │
│                   │         │                         │                    │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ mRNA-1010         │ Phase 3 │ Seasonal Influenza      │ Data readout 2025  │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ mRNA-1345         │ BLA     │ RSV (18-59 high-risk)   │ Filed              │
│ (mRESVIA label)   │         │                         │                    │
└─────────────────────────────────────────────────────────────────────────────┘

ONCOLOGY FRANCHISE (High Growth Potential)
┌─────────────────────────────────────────────────────────────────────────────┐
│ Program           │ Phase   │ Indication              │ Key Data           │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ mRNA-4157 (V940)  │ Phase 3 │ Adjuvant Melanoma       │ 49% recurrence     │
│ + Keytruda        │         │ + NSCLC, other tumors   │ reduction (Ph2b)   │
│ (Merck partner)   │         │                         │ 8 trials ongoing   │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ mRNA-4359         │ Phase 2 │ Metastatic Melanoma,    │ IDO1/TAA/PD-L1     │
│                   │         │ NSCLC (wholly owned)    │ target             │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ mRNA-5671         │ Phase 1 │ KRAS-mutant cancers     │ Pan-KRAS approach  │
│                   │         │ (lung, colorectal, panc)│                    │
└─────────────────────────────────────────────────────────────────────────────┘

RARE DISEASE FRANCHISE (Regulatory Momentum)
┌─────────────────────────────────────────────────────────────────────────────┐
│ Program           │ Phase   │ Indication              │ Status             │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ mRNA-3705         │ Phase 3 │ Methylmalonic Acidemia  │ FDA START pilot    │
│                   │         │ (MMA)                   │ program            │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ mRNA-3745         │ Phase 3 │ Propionic Acidemia (PA) │ Pivotal study 2025 │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ mRNA-6231         │ Phase 2 │ Autoimmune (IL-2 mutein)│ Immune tolerance   │
└─────────────────────────────────────────────────────────────────────────────┘

LATENT & OTHER VACCINES
┌─────────────────────────────────────────────────────────────────────────────┐
│ Program           │ Phase   │ Indication              │ Notes              │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ CMV               │ Phase 3 │ Cytomegalovirus         │ Pivotal trial      │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ Norovirus         │ Phase 3 │ mRNA-1403               │ GI infection       │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ Zika              │ Phase 1 │ Traveler's vaccine      │ Public health      │
├───────────────────┼─────────┼─────────────────────────┼────────────────────┤
│ HIV               │ Phase 1 │ mRNA-1644               │ IAVI collaboration │
└─────────────────────────────────────────────────────────────────────────────┘
```

### §2.3 · Manufacturing & Operations

```
MANUFACTURING FOOTPRINT
┌─────────────────────────────────────────────────────────────────────────────┐
│ Facility              │ Location           │ Capability                    │
├───────────────────────┼────────────────────┼───────────────────────────────┤
│ MTC - Norwood         │ Massachusetts, USA │ Drug substance, clinical,     │
│ (Moderna Technology   │                    │ commercial (purchased Dec     │
│  Center)              │                    │ 2024), expansion 2027         │
├───────────────────────┼────────────────────┼───────────────────────────────┤
│ Marlborough Facility  │ Massachusetts, USA │ INT (personalized cancer)     │
│                       │                    │ manufacturing, operational    │
│                       │                    │ 2025                          │
├───────────────────────┼────────────────────┼───────────────────────────────┤
│ Laval                 │ Quebec, Canada     │ Drug product, fully           │
│                       │                    │ operational (Health Canada    │
│                       │                    │ license granted 2024)         │
├───────────────────────┼────────────────────┼───────────────────────────────┤
│ UK Strategic Reserves │ UK                 │ Pandemic preparedness         │
├───────────────────────┼────────────────────┼───────────────────────────────┤
│ Australia Facility    │ Australia          │ Regional supply               │
└─────────────────────────────────────────────────────────────────────────────┘

$140M NORWOOD EXPANSION (2025-2027):
• Onshore drug product manufacturing to complete full US manufacturing loop
• End-to-end mRNA production under one roof
• Hundreds of skilled biomanufacturing jobs
• Supports clinical and commercial supply
• Target completion: H1 2027

COST REDUCTION INITIATIVES:
┌─────────────────────────────────────────────────────────────────────────────┐
│ Initiative                    │ Target           │ Progress (as of 2025)     │
├───────────────────────────────┼──────────────────┼───────────────────────────┤
│ Workforce reduction           │ 10% (~800 roles) │ In progress               │
│ Manufacturing efficiency      │ $400M savings    │ Process optimization      │
│ R&D spend reduction           │ $4.1B (2025)     │ Respiratory trials        │
│                               │                  │ winding down              │
├───────────────────────────────┼──────────────────┼───────────────────────────┤
│ Total Cost Reduction Target   │ $1.5B by 2027    │ ~$4B of $5B plan achieved │
│ Break-even target             │ Cash 2028        │ On track                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### §2.4 · Regulatory & Commercial Strategy

```
REGULATORY MILESTONES (2025-2027)
┌─────────────────────────────────────────────────────────────────────────────┐
│ Product                │ Market    │ Timing              │ Notes           │
├────────────────────────┼───────────┼─────────────────────┼─────────────────┤
│ mRNA-1283 (COVID)      │ US        │ PDUFA May 31, 2025  │ Next-gen,       │
│                        │           │                     │ freeze-dried    │
├────────────────────────┼───────────┼─────────────────────┼─────────────────┤
│ mRNA-1083 (Combo)      │ US        │ 2025-2026           │ Flu + COVID     │
├────────────────────────┼───────────┼─────────────────────┼─────────────────┤
│ mRNA-1345 (RSV 18-59)  │ US        │ Filed               │ Label expansion │
├────────────────────────┼───────────┼─────────────────────┼─────────────────┤
│ mRNA-4157 (Cancer)     │ US/EU     │ 2026-2027           │ Ph3 melanoma    │
│                        │           │                     │ data pending    │
└─────────────────────────────────────────────────────────────────────────────┘

COMMERCIAL STRATEGY PILLARS:
1. Seasonal Respiratory Franchise
   • Spikevax: Transition to endemic/seasonal market
   • mRESVIA: Build RSV awareness and uptake
   • Combination vaccines: Simplify annual immunization

2. Oncology Launch Preparation
   • mRNA-4157 manufacturing at Marlborough
   • Personalized medicine infrastructure
   • HCP education on individualized neoantigen therapy

3. Geographic Expansion
   • EU: Full regulatory approvals and reimbursement
   • Emerging markets: Partner-led distribution
   • Japan: Regulatory pathway establishment

4. Market Access & Pricing
   • Value-based contracts with health systems
   • CMS negotiation strategy
   • International pricing tiers
```

---
