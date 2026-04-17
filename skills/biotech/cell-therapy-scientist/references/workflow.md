# Standard Workflow

## 8.1 CAR Construct Design & Validation Workflow

```
Step 1: Target & Indication Definition
├── Antigen confirmed: tumor-specific surface antigen (flow, IHC, published data)
├── Indication: hematologic (ALL, DLBCL, MM) vs. solid tumor
├── Patient population: autologous (heavily pretreated) vs. allogeneic (off-the-shelf)
└── Clinical urgency: bridging therapy vs. primary treatment

Step 2: CAR Component Selection
├── scFv: VH-VL orientation; linker (G4S)3; affinity 1–30 nM; humanized (CDR-grafting)
├── Signal peptide: CD8α (standard); CD33 (if additional clearance needed)
├── Hinge/TM: CD8α (heme) vs. CD28 (solid tumor); reduces tonic signaling
├── Co-stim: 4-1BB (persistence, memory, heme-ALL/DLBCL) vs. CD28 (rapid kill, solid)
├── Signaling: CD3ζ (3 ITAMs); standard
└── Safety switch: EGFRt, iCasp9, or RQR8 for allogeneic; none for autologous

Step 3: Sequence Design & Cloning
├── Codon optimization for human expression
├── Check for restriction sites (BsaI for Golden Gate)
├── Verify Kozak: GCCACC before ATG
├── Signal peptide cleavage prediction (SignalP 6.0)
├── Golden Gate assembly: CAR → lentiviral plasmid
└── Sequence verification: full plasmid sequencing (Sanger)

Step 4: Lentiviral Vector Production
├── 3rd-generation SIN lentiviral system: gag/pol, Rev, VSV-G (4 plasmids)
├── Producer cell line: HEK-293T (transient) or stable producer cell line
├── Titer optimization: harvest timing (48–72h), concentration method
├── Batch release testing: titer, VCN, RCR, sterility, endotoxin
└── Store at -80°C; avoid freeze-thaw cycles

Step 5: Functional Validation (in vitro)
├── Transduce Jurkat or HEK293 cells: confirm CAR surface expression (flow)
├── Cytotoxicity assay: E:T 5:1, 24h, LDH or xCELLigence
├── Target antigen specificity: test on antigen+ and antigen- cell lines
├── Cytokine release: IFN-γ ELISA, E:T 2:1, 24h
└── Co-stim domain comparison: 4-1BB vs. CD28 head-to-head in T cells

Step 6: T Cell Engineering (research scale)
├── PBMC activation: anti-CD3/CD28 beads or TransAct, IL-7/IL-15
├── Transduction: MOI 5–10, spinoculation optional
├── Expansion: 10–14 days, G-REX or flask
├── CAR expression: target ≥ 30% CD3+CAR+ by flow
└── Phenotype: CD4/CD8 ratio, exhaustion markers (PD-1, LAG-3, TIM-3)
```

## 8.2 GMP Manufacturing Workflow (Autologous CAR-T)

```
Day -7 to Day -1: Patient Apheresis & Leukapheresis
├── Apheresis collection: target ≥ 1×10⁹ PBMC, CD3 ≥ 30%, viability ≥ 70%
├── Fresh shipment to GMP facility (or cryopreserve if delayed manufacturing)
└── QC: cell count, viability, CD3%, sterility, mycoplasma

Day 0: T Cell Isolation & Activation
├── PBMC receipt: verify COA against acceptance criteria
├── Optional: CD4/CD8 selection (Miltenyi) for defined ratio product
├── T cell activation: anti-CD3/CD28 TransAct (1:100) or bead-based (1:4)
├── Culture: TexMACS GMP medium + IL-7 (10 ng/mL) + IL-15 (5 ng/mL)
└── Seed: 1–2×10⁶ CD3+ T cells/mL in G-REX 10M or CliniMACS Prodigy

Day 2: Transduction
├── Verify activation: CD25+CD69+ ≥ 70% by flow
├── Transduce: add lentiviral vector at MOI 5–10
├── Spinoculation (optional): 800×g, 90 min, 32°C, for efficiency boost
└── Return to incubator: 37°C, 5% CO₂

Day 5: Expansion & Media Exchange
├── 50% media exchange: fresh TexMACS + cytokines
├── CAR expression check: flow (anti-idiotype or Protein L)
├── Target: ≥ 30% CAR+ within CD3+ population
└── If < 20%: evaluate transduction conditions; do not proceed to harvest

Day 7–9: Bead Removal & Transfer
├── Remove activation beads: DynaMag magnetic separation
├── If TransAct used: no bead removal needed (biodegradable)
├── Transfer to G-REX 100M or bioreactor for final expansion
└── Daily monitoring: cell count, viability (trypan blue / Vi-CELL), glucose, lactate

Day 10–14: Harvest & Formulation
├── Harvest trigger: glucose < 2 mM OR cell density > 2×10⁶/mL OR Day 14
├── Cell wash: CliniMACS Prodigy or centrifugation × 3 in PBS + 2% HSA
├── Formulation: CryoStor CS10 at 10×10⁶ CAR+ T cells/mL
├── Fill: 50 mL cryobags or vials per patient dose
└── Controlled-rate freezing: -1°C/min to -80°C → transfer to LN₂ vapor phase

Day 14+: Quality Release Testing
├── Sterility (USP <71>): negative at 14 days
├── Mycoplasma: negative
├── CAR expression: flow (≥ 20% CAR+)
├── Viability: ≥ 70%
├── VCN: 0.5–5 copies/diploid genome (ddPCR)
├── RCR: not detected
├── Potency: cytotoxicity (≥ 20% at E:T 5:1) + IFN-γ (≥ 200 pg/mL)
└── Certificate of Analysis: review and sign-off before patient release
```

## 8.3 Analytical Development Workflow

```
Flow Cytometry Panel Design:
├── CAR expression: anti-idiotype, Protein L, or Fab staining
├── Phenotype: CD3, CD4, CD8, CD45RA, CCR7 (TN/TCM/TEM/TEMRA)
├── Exhaustion: PD-1, LAG-3, TIM-3, TIGIT, CD57
├── Activation: CD25, CD69, CD71
└── Live/dead: 7-AAD, DAPI, Zombie dyes

VCN Quantification (ddPCR):
├── DNA extraction: QIAamp DNA Blood Mini Kit from CAR-T product
├── Reaction: HIV-1 gag primers/probe + PTBP2 reference gene
├── Controls: negative donor T cells, positive plasmid standard curve
└── Report: VCN = gag copies / (PTBP2 copies / 2) = copies/diploid genome

Potency Assay (Cytotoxicity):
├── Target cells: antigen+ tumor cell line (e.g., Raji for CD19 CAR)
├── Effector cells: patient CAR-T product (thawed, rested 4h)
├── E:T ratios: 10:1, 5:1, 2.5:1, 1:1
├── Detection: LDH release (Promega) or xCELLigence (real-time)
├── Analysis: % specific lysis = (E - S - M) / (T - M) × 100
└── EC50: report E:T ratio for 50% specific lysis

Tumor Antigen Cross-Reactivity:
├── Panel: normal tissue cDNA or cells (heart, liver, lung, kidney)
├── Method: flow cytometry (cell lines) or IHC (tissue arrays)
├── Risk threshold: any binding at relevant tissue requires mitigation
└── Mitigation: lower-affinity scFv, logic-gated CAR, tandem design
```

## 8.4 IND-Enabling Study Design Workflow

```
Phase 1: Product Characterization (Months 1–3)
├── Full construct characterization: sequencing, CAR expression, binding affinity
├── Vector characterization: titer, VCN, RCR, sterility, endotoxin
├── In vitro potency: cytotoxicity (multiple E:T ratios), cytokine release
├── Target antigen: expression in tumor vs. normal tissue (cross-reactivity)
└── Comparability plan: if manufacturing process changes post-IND

Phase 2: In Vivo Pharmacology (Months 4–8)
├── xenograft model: immunodeficient mice (NSG/NOG), tumor inoculation
├── CAR-T dosing: single dose escalation
├── Endpoints: tumor volume, survival, CAR-T persistence (qPCR blood)
├── PD markers: cytokine levels (IL-6, IFN-γ, TNF-α), tumor biopsy
└── Safety: body weight, clinical observation, histopathology

Phase 3: Toxicology & Biodistribution (Months 8–14)
├── Species: immunodeficient mice with human PBMC (GLP optional)
├── Doses: low (clinical dose equiv.), mid, high
├── Endpoints: toxicokinetics, CAR-T distribution (qPCR), histology
├── Safety: CBC, clinical chemistry, organ weights, histopathology
├── Recovery group: 28-day recovery to assess reversibility
└── Biodistribution: qPCR in blood, bone marrow, spleen, tumor, major organs

Phase 4: IND Submission (Months 14–18)
├── CMC section: construct, vector, product characterization, manufacturing process
├── Pharmacology: in vitro and in vivo data
├── Toxicology: GLP toxicology report
├── Clinical protocol: Phase I dose escalation (3+3 design)
└── Investigator's brochure: CAR-T mechanism, preclinical data, CRS/ICANS management
```

## 8.5 Allogeneic CAR-T / iPSC-NK Engineering Workflow

```
Gene Editing Targets:
├── TRAC KO: prevent GvHD; target exon 1, Cas9 + sgRNA; ≥ 90% KO by flow
├── B2M KO: eliminate HLA-I; prevent host T cell rejection; ≥ 90% by flow
├── PDCD1 KO: remove PD-1 checkpoint; enhance TME infiltration
├── NKG2A KO (NK): remove inhibitory signal; enhance NK killing
└── CAR knock-in (KI): insert CAR at TRAC locus via HDR (reduces tonic signaling)

CRISPR RNP Electroporation:
├── sgRNA synthesis: chemically synthesized (Alt-R, IDT)
├── RNP assembly: SpCas9 protein + sgRNA (1:3 molar ratio)
├── Electroporation: Lonza 4D-Nucleofector, pulse code EN-138 (NK/T cells)
├── Post-electroporation: recovery in complete media + cytokines
└── KO validation: flow cytometry at 48–72h post-electroporation

iPSC-Derived NK Cell Manufacturing:
├── iPSC maintenance: mTeSR Plus, daily media change, passaging at 80% confluence
├── Differentiation: embryoid body formation OR monolayer differentiation protocol
├── NK cell expansion: IL-15 + IL-2 on feeder cells (irradiated K562-mbIL15)
├── CAR transduction: lentiviral at Day 14–21 of NK differentiation
└── CAR-NK harvest: Day 28–35, CD56+CD3- NK phenotyping by flow

Off-the-Shelf Product Considerations:
├── HLA-matching: consider HLA-typed donor iPSC bank or universal donor (β2M-free)
├── "Don't eat me" signal: CD47 overexpression to prevent macrophage phagocytosis
├── "Don't kill me" signal: HLA-E overexpression to prevent NK attack
└── Safety: RCR testing on iPSC-derived product (extended culture × 3 passages)
```
