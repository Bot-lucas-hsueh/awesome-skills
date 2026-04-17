# Standards & Reference

## 7.1 Regulatory Standards & Guidance

| Standard | Title | Application |
|----------|-------|-------------|
| **FDA 21 CFR Part 1271** | Human cells, tissues, and cellular/tissue-based products (HCT/P) | Donor eligibility, screening, CGTP requirements |
| **FDA 21 CFR Part 600** | Biologics: general provisions, licensing | CMC, release testing, lot release |
| **FDA CMC Guidance (2020)** | Chemistry, Manufacturing, and Controls for Gene Therapy IND | Vector characterization, product release, comparability |
| **EMA ATMP Guidelines** | Advanced therapy medicinal products | Gene therapy, cell therapy, tissue-engineered products |
| **ICH Q8(R2)** | Pharmaceutical Development | Quality by Design (QbD), CQAs, CPPs |
| **ICH Q9** | Quality Risk Management | Risk assessment for manufacturing process |
| **ICH Q10** | Pharmaceutical Quality System | Process validation, change control, CAPA |
| **USP <1043>** | Ancillary Materials for Cell, Gene, Tissue-Engineered Products | Cytokine qualification, media additives |
| **USP <71>** | Sterility Tests | Product release, environmental monitoring |
| **FACT/JACIE 8th Edition** | Standards for Hematopoietic Cellular Therapy | Accreditation, manufacturing, clinical |
| **ASTCT CRS/ICANS Consensus (2019)** | Grading criteria for CAR-T toxicities | Clinical trial toxicity management |

## 7.2 CAR-T Construct Component Reference

| Component | Option | Use Case | Notes |
|-----------|--------|----------|-------|
| **scFv Orientation** | VH-linker-VL (preferred) | Standard | Lower tendency for aggregation |
| **Linker** | (G4S)₃ (15-mer) | All | Flexible; commonly used Whitlow linker |
| **Signal Peptide** | CD8α (MALPVTALLLPLALLLHAARP) | All | Cleaved on secretion |
| **Hinge** | CD8α (hematologic), CD28 (solid tumor) | By indication | CD8α reduces tonic signaling |
| **Co-stim Domain** | 4-1BB (heme-ALL, DLBCL), CD28 (solid tumor, aggressive) | By indication | 4-1BB → memory T cells; CD28 → rapid killing |
| **Signaling Domain** | CD3ζ (3 ITAMs) | All | Standard across all approved CARs |
| **Safety Switch** | EGFRt (cetuximab), iCasp9 (AP20187), RQR8 (rituximab) | Allogeneic | Enables depletion if needed |

## 7.3 Lentiviral Vector Release Criteria

| Test | Method | Acceptance Criterion |
|------|--------|---------------------|
| **Functional Titer** | TU assay on Jurkat cells | ≥ 5×10⁸ TU/mL |
| **VCN** | qPCR (HIV gag / PTBP2) | ≤ 5 copies/diploid genome |
| **RCR** | S+L⁻ assay or qPCR (VSV-G) | Not detected |
| **Sterility** | USP <71> (14-day culture) | Negative |
| **Mycoplasma** | PCR + culture (21 CFR 610.30) | Negative |
| **Endotoxin** | LAL kinetic turbidimetric | ≤ 5 EU/mL |
| **Residual Plasmid** | qPCR (ampicillin resistance gene) | ≤ 1 ng/dose |
| **pH** | Potentiometric | 7.0–7.4 |
| **Osmolality** | Osmometry | 280–320 mOsm/kg |

## 7.4 CAR-T Product Release Testing Panel

| Test | Method | Acceptance Criterion |
|------|--------|---------------------|
| **CAR Expression** | Flow: anti-idiotype / Protein L, gate on CD3+ | ≥ 20% CAR+ within viable CD3+ |
| **Viability** | 7-AAD / DAPI exclusion by flow | ≥ 70% viable (ideally ≥ 80%) |
| **CD4:CD8 Ratio** | Flow cytometry | Report; target 1:1 to 2:1 |
| **Sterility** | USP <71> (14-day culture) | Negative |
| **Mycoplasma** | PCR (Venor GeM) | Negative |
| **Endotoxin** | LAL kinetic turbidimetric | ≤ 5 EU/dose |
| **VCN** | ddPCR (gag / PTBP2) | 0.5–5 copies/diploid genome |
| **RCR** | S+L⁻ assay or qPCR | Not detected |
| **Potency (Cytotoxicity)** | xCELLigence / LDH, E:T 5:1, 24h | ≥ 20% specific lysis (or EC50 E:T ≤ 10:1) |
| **Potency (IFN-γ)** | ELISA, E:T 2:1, 24h co-culture | ≥ 200 pg/mL above background |

## 7.5 Manufacturing Platforms Reference

| Platform | Type | Scale | Closed System | Best For |
|----------|------|-------|---------------|----------|
| **Miltenyi CliniMACS Prodigy** | Automated GMP | 1 patient | Fully closed | Autologous CAR-T |
| **Lonza Cocoon** | Automated GMP | 1 patient | Fully closed | Autologous CAR-T |
| **G-REX 10M/100M** | Static flask | 10⁸–10⁹ cells | Semi-closed | Small-scale expansion |
| **Sartorius ambr 250** | Stirred-tank bioreactor | 10¹⁰ cells | Closed | Allogeneic scale-up |
| **Wave Bioreactor** | Rocking motion | Variable | Semi-closed | Allogeneic expansion |

## 7.6 CRS & ICANS Grading (ASTCT 2019)

| CRS Grade | Criteria | Management |
|-----------|----------|------------|
| **Grade 1** | Fever ≥38°C, no hypotension, no hypoxia | Supportive care; monitor |
| **Grade 2** | Fever + hypotension responding to fluids OR O₂ by low-flow NC | Tocilizumab 8 mg/kg IV; corticosteroids if no response |
| **Grade 3** | Hypotension needing vasopressors OR O₂ by high-flow/CPAP | Tocilizumab + dexamethasone 10 mg q6h; ICU |
| **Grade 4** | Life-threatening; intubation, shock | ICU; high-dose steroids (dexamethasone 10–20 mg q6h); siltuximab |

| ICANS Grade | Criteria | Management |
|-------------|----------|------------|
| **Grade 1** | ICE 3–7/10; no obtundation | Supportive; monitor q4h |
| **Grade 2** | ICE 0–2/10; obtunded | Dexamethasone 10 mg q6h; ICU monitoring |
| **Grade 3** | ICE 0; stuporous, seizures, focal edema | ICU; high-dose steroids; consider siltuximab |
| **Grade 4** | Coma, deep focal edema | ICU; mechanical ventilation; aggressive immunosuppression |
