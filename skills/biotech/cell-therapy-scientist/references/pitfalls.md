# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Releasing product that fails potency** | 🔴 Critical | Potency is a CQA. A product passing VCN but failing cytotoxicity must not be released. Investigate root cause; manufacture new batch. |
| 2 | **Using unqualified ancillary materials** | 🔴 Critical | All GMP cytokines and reagents must be USP <1043> qualified or GMP-grade. Unqualified materials → IND clinical hold. |
| 3 | **RCR-positive vector without disclosure** | 🔴 Critical | FDA notification required within 3 business days. Quarantine all affected product. |
| 4 | **Proceeding without lymphodepletion regimen** | 🔴 High | Flu/Cy is required for CAR-T expansion. Without it, AUC(0-28d) will be inadequate. |
| 5 | **Ignoring T cell starting material quality** | 🔴 High | Heavily pretreated patients often have exhausted T cells. Set minimum criteria: CD3 ≥ 15%, viability ≥ 70%. |
| 6 | **VCN "average" masking high-VCN subclones** | 🔴 High | Report VCN distribution (% cells > VCN 5). High-VCN clones = insertional mutagenesis risk. |
| 7 | **Skipping genotoxicity for novel polymers/materials** | 🟡 Medium | ISO 10993-3 (Ames + chromosomal aberration) required for any material without regulatory history. |
| 8 | **Switching fresh → cryopreserved without bridging study** | 🟡 Medium | Cryopreservation changes viability and phenotype. Head-to-head potency comparison required. |
| 9 | **Over-relying on surrogate markers (VCN) instead of function (potency)** | 🟡 Medium | VCN is a process parameter, not a quality attribute. Function over numbers always. |
| 10 | **Administering CAR-T without CRS/ICANS management protocol in place** | 🔴 High | Tocilizumab must be at bedside before infusion. Clinical team trained on grading and management. |

## 10.2 Best Practices

1. **Potency is non-negotiable** — Cytotoxicity and cytokine release are the gold-standard CQAs. A product passing every parameter except potency must not be released. Ever.

2. **Model the degradation-mechanical property curve** — Not just initial properties. Tissue ingrowth takes 4–8 weeks minimum for bone. Your scaffold must hold its load for that duration.

3. **Sterilization effects on polymers must be validated** — Gamma causes chain scission (20–40% Mn drop). Use EtO when possible; always test post-sterilization properties.

4. **Regulatory endpoint first** — Build the Biological Evaluation Plan (BEP) before manufacturing. Every material decision must be traceable to an ISO 10993 test or predicate comparison.

5. **Quantify everything** — Porosity %, pore size, Mn, E, drug loading, heparin density. "Looks good" is not engineering data.

6. **Match your animal model to clinical application** — Rat subcutaneous ≠ rabbit femoral condyle ≠ ovine spine. Each has different bone healing rates and surgical constraints.

7. **T cell exhaustion is the #1 product failure mode** — Heavily pretreated patients, long expansion, high-affinity scFv with tonic signaling. Address at design and manufacturing level.

8. **RCR monitoring is a continuous process** — Test at vector production, at T cell transduction, and at final product. Never skip.

9. **CRS/ICANS protocols must be in place before first patient dose** — Tocilizumab at bedside, steroids ready, ICU escalation pathway clear, investigator's brochure distributed to clinical team.

10. **Clinical translation requires a comparability plan** — Any manufacturing change (site, process, equipment) requires bridging studies per FDA guidance. Plan for this from Day 1.

## 10.3 Quality Checklist

**Pre-Manufacturing:**
- [ ] CAR construct sequenced and verified
- [ ] Lentiviral vector: RCR-negative, titer ≥ 5×10⁸ TU/mL
- [ ] Apheresis QC: CD3 ≥ 30%, viability ≥ 70%, no pathogen detected
- [ ] Ancillary materials: GMP-grade cytokines, USP <1043> qualified reagents
- [ ] Regulatory: IND active, IRB approved, patient consent obtained
- [ ] CRS/ICANS protocol: tocilizumab at bedside, clinical team trained

**During Manufacturing (Day 0–14):**
- [ ] Activation efficiency: CD25+CD69+ ≥ 70% at Day 2
- [ ] Transduction efficiency: ≥ 30% CAR+ at Day 5
- [ ] Daily: cell count, viability, glucose, lactate
- [ ] Harvest criteria met: glucose < 2 mM or Day 14
- [ ] Sterility samples taken at harvest (to 14-day incubation)

**Product Release:**
- [ ] CAR expression ≥ 20% (flow)
- [ ] Viability ≥ 70% (flow)
- [ ] VCN 0.5–5 copies/diploid genome (ddPCR)
- [ ] Sterility: negative at 14 days
- [ ] Mycoplasma: negative
- [ ] Endotoxin ≤ 5 EU/dose
- [ ] RCR: not detected
- [ ] Potency: ≥ 20% specific lysis at E:T 5:1 AND ≥ 200 pg/mL IFN-γ
- [ ] Certificate of Analysis signed by QP

**Post-Infusion Follow-Up:**
- [ ] CAR-T PK: qPCR at Days 7, 14, 28, 90, 180
- [ ] CRS/ICANS monitoring: daily × 7 days, then weekly × 3 weeks
- [ ] Clinical response: PET-CT at Day 28, Day 90, then per protocol
- [ ] B-cell aplasia monitoring (CD19 CAR-T): monthly immunoglobulin levels
- [ ] RCR testing in patient blood at 3, 6, 12, 24 months

## 10.4 Red Flags That Signal Critical Failure

| Red Flag | Indicates | Action |
|----------|-----------|--------|
| Potency test fails despite passing VCN | T cell exhaustion or CAR dysfunction | Hold product; investigate; don't release |
| RCR positive on vector or product | Contamination; regulatory violation | Quarantine; notify FDA; investigate |
| Sterility positive at 14 days | Microbial contamination | Destroy product; investigate manufacturing |
| VCN > 5 copies/genome in > 5% cells | Clonal expansion risk | Re-design transduction; investigate producer cell |
| Cytokine storm within 24h of infusion | Uncontrolled CAR-T activation | Tocilizumab + steroids; ICU escalation |
| No CAR-T expansion in patient by Day 14 | No engraftment; product or patient issue | Check lymphodepletion; patient immune status |
| CD19-negative relapse < Day 60 | Antigen escape | Switch to bivalent CAR; test CD22/CD20 |
| Mycoplasma positive in culture | Contamination | Destroy product; audit aseptic technique |
