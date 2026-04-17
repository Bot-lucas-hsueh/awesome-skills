# Standards & Reference

## 7.1 Analytical Method Standards

- [ICH Q2(R2) Validation of Analytical Procedures](https://database.ich.org/sites/default/files/ICH_Q2-R2_Document_S1_Step2.pdf) — Pharmaceutical method validation guideline
- [ICH Q2(R1)](https://database.ich.org/sites/default/files/ICH_Q2R1__Error.pdf) — Original validation guideline (still referenced)
- [USP <1225> Validation of Compendial Procedures](https://www.usp.org/) — US Pharmacopeia method validation
- [FDA Guidance for Industry: Analytical Procedures and Methods Validation](https://www.fda.gov/guidance) — Regulatory expectations
- [AOAC International Guidelines](https://www.aoac.org/) — Standard method validation requirements

## 7.2 Laboratory Quality Standards

| Standard | Scope | Key Requirements |
|----------|-------|-----------------|
| **ISO/IEC 17025:2017** | Testing and calibration laboratories | Competence, quality management, traceability |
| **ISO 15189** | Medical laboratories | Quality and competence for medical testing |
| ** GLP (21 CFR Part 58)** | Non-clinical studies | FDA regulatory requirements for lab studies |
| **EPA Method 8000** | Environmental analysis | SW-846 method validation |
| **AOAC Appendix K** | Standard method performance requirements | Method validation criteria |

## 7.3 Instrument Calibration Standards

| Instrument | Calibration Standard | Frequency | Acceptance Criteria |
|------------|--------------------|-----------|-------------------|
| **HPLC UV/VIS** | NIST SRM or certified reference | Daily/weekly | ±2% at check concentration |
| **GC-FID** | Certified reference mix | Daily | ±5% response factor |
| **ICP-MS** | NIST multi-element solution | Weekly | ±10% at all masses |
| **UV-Vis Spectrophotometer** | NIST filter or holmium oxide | Monthly | ±0.005 AU at 1.0 |
| **Balance** | Class S or E weights | Daily | ±1 digit or ±0.1 mg |
| **pH Meter** | NIST buffer pH 4, 7, 10 | Daily | ±0.02 pH units |

## 7.4 Method Validation Parameters

| Parameter | Definition | Acceptance Criteria | Calculation |
|-----------|-----------|-------------------|------------|
| **Specificity** | Ability to assess analyte in presence of interferences | Resolution Rs ≥1.5 from nearest peak | Peak purity >0.99 |
| **Linearity** | Proportional response over range | R² ≥ 0.999 | Least squares regression |
| **Accuracy** | Closeness to true value | Recovery 85-115% | (Measured/Spiked) × 100% |
| **Precision** | Reproducibility of measurements | RSD ≤ 2% | (SD/Mean) × 100% |
| **Repeatability** | Same conditions, same analyst | RSD ≤ 1% | Within-run precision |
| **Intermediate Precision** | Different days/analysts | RSD ≤ 2% | Between-run precision |
| **LOD** | Limit of detection | S/N ≥ 3:1 | 3 × SD(b)/slope |
| **LOQ** | Limit of quantitation | S/N ≥ 10:1 | 10 × SD(b)/slope |
| **Robustness** | Method tolerance to changes | No significant effect | Plackett-Burman design |
| **Range** | LOQ to upper concentration | Validated linear range | LOQ to 120% of target |

## 7.5 QC Sample Requirements

| QC Type | Purpose | Frequency | Acceptance Criteria |
|---------|---------|-----------|-------------------|
| **Method blank** | Contamination check | Every batch | <LOQ or <1/3 action limit |
| **Instrument blank** | System cleanliness | Start/end of run | Zero response |
| **Calibration blank** | Calibration verification | After calibration | ±20% of nominal |
| **CRM/LCS** | Accuracy verification | Every batch | 85-115% recovery |
| **Duplicate/Duplicate** | Precision check | Every 10 samples | RPD ≤ 20% |
| **Matrix spike** | Matrix interference check | Every 20 samples | 75-125% recovery |
| **Surrogate** | Recovery for complex matrices | Per method | 70-120% |
| **ICV (Initial Calibration Verification)** | Second-source verification | After calibration | ±10% of true |

## 7.6 Sample Handling & Preservation

| Sample Type | Container | Preservation | Hold Time |
|------------|----------|---------------|-----------|
| Aqueous (metals) | HDPE bottle, HNO3 to pH <2 | 4°C | 180 days |
| Aqueous (organics) | Glass with Teflon cap | 4°C, dark | 7 days |
| Soil/sediment | Glass jar | Freeze (-20°C) | 14 days (organics), 180 days (metals) |
| Tissue | Polypropylene | Freeze (-80°C) | 90 days |
| Blood/serum | Vacutainer | Freeze (-80°C) | 30 days (serum), 7 days (whole blood) |
| Air particulates | Filter (GF or PM) | 4°C | 30 days |

## 7.7 Chromatographic Performance Checks

| Parameter | HPLC | GC | Acceptance |
|-----------|------|----|-----------|
| **Resolution** | Rs ≥ 2.0 between critical pairs | Rs ≥ 2.0 | Rs ≥ 2.0 |
| **Tailing factor** | T ≤ 2.0 | T ≤ 2.0 | T ≤ 2.0 |
| **Theoretical plates** | N ≥ 2000 | N ≥ 3000 | Method-specific |
| **Capacity factor** | 2 ≤ k' ≤ 10 | 2 ≤ k' ≤ 10 | Depends on method |
| **Precision (%RSD)** | <1% for peak area | <5% for peak area | Method-specific |
