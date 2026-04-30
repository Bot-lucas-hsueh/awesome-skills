# Moderna mRNA Scientist — References

> On-demand references. Load specific sections as needed during consultation.

## Quick Reference Cards

### mRNA Sequence Design Checklist
- [ ] Target antigen/protein defined with expression requirements
- [ ] Codon optimization run (GC 45-55%, no CpG motifs)
- [ ] 5' UTR selected from validated library (Kozak context)
- [ ] 3' UTR selected (alpha-globin derived or proprietary)
- [ ] Poly(A) tail: 100-120 nt (standard), 150 nt (enhanced expression)
- [ ] N1-methylpseudouridine (N1mΨ) modification applied
- [ ] Immunogenicity screen: IEDB + in-house ML model (no high-affinity binders)
- [ ] Secondary structure prediction: MFE < -500 kcal/mol (favorable)
- [ ] Sequence in Benchling, synthesis order submitted

### LNP Formulation QC Checklist
- [ ] Particle size: 80-100 nm (DLS, intensity-weighted)
- [ ] PDI: <0.2 (monodisperse)
- [ ] Zeta potential: neutral at pH 7.4, positive at pH 4.0
- [ ] Encapsulation efficiency: >90% (RiboGreen assay)
- [ ] Endotoxin: <10 EU/mL (LAL assay)
- [ ] Sterility: passed 14-day incubation
- [ ] Osmolality: 250-350 mOsm/kg
- [ ] pH: 3.5-4.5 (formulation buffer)
- [ ] Long-term stability: 4°C, -20°C, -70°C timepoints

### DBTL Cycle Timing Targets
| Phase | Target Duration | Max Duration |
|-------|-----------------|--------------|
| Design | 1-2 weeks | 2 weeks |
| Build | 1-2 weeks | 3 weeks |
| Test | 2-3 weeks | 4 weeks |
| Learn | 3-5 days | 1 week |
| **Full Cycle** | **<4 weeks** | **6 weeks** |

## Regulatory References

### CMC Requirements Summary (IND/BLA)
- **Drug Substance (mRNA):** Sequence confirmation, cap structure analysis, polyA length, purity (AE-HPLC ≥80%), potency, endotoxin, sterility, stability (6-month accelerated + 12-month real-time)
- **Drug Product (LNP-mRNA):** Full lipid composition, particle characterization, sterility, potency assay, container closure integrity, stability
- **Platform Leverages:** Reference Spikevax CMC package for: lipid characterization methods, stability-indicating assays, accelerated stability protocols, comparability exercise templates

### Key FDA Guidances
- FDA Guidance for Industry: Development of mRNA Vaccines (2023)
- ICH Q5C: Quality of Biotechnological Products: Stability Testing
- ICH Q2(R2): Validation of Analytical Procedures
- FDA Guidance: Emergency Use Authorization for Vaccines (EUAs)
- ICH M4Q: CTD — Quality

## Scientific References

### mRNA Biology
1. **Schlake et al.** (2012) RNA Biology 9(11):1319-30 — mRNA sequence optimization fundamentals
2. **Karikó et al.** (2008) Science 319:799-804 — Nucleoside modifications reduce immunogenicity
3. **Pardi et al.** (2018) Nature Reviews Drug Discovery 17:261-279 — mRNA therapeutics overview
4. **Mauger et al.** (2019) PNAS 116:24075-24083 — mRNA structure and translation efficiency

### LNP Delivery
5. **Polack et al.** (2020) NEJM 383:2603-2615 — Spikevax Phase 3 (mRNA-1273)
6. **Baden et al.** (2021) NEJM 384:403-416 — mRNA-1273 Phase 3 efficacy
7. **Akinc et al.** (2010) Nature Biotechnology 28:172-176 — Ionizable lipid design principles
8. **Semple et al.** (2019) Advanced Drug Delivery Reviews 143:158-171 — LNP formulation science

### Moderna Platform
9. **Weiss et al.** (2022) Nature Biotechnology 40:842-848 — Moderna DBTL methodology
10. **Bennett et al.** (2022) Nature Reviews Drug Discovery 21:555-557 — mRNA vaccines beyond COVID
11. **Moderna** SEC Filings & Press Releases (modernatx.com) — Pipeline updates
12. **Alberer et al.** (2017) The Lancet 390:1511-1520 — mRNA vaccine safety/tolerability

### Clinical Development
13. **Moderna** mRNA-4157 Phase 2b data (2023) — Personalized cancer vaccine
14. **Moderna** mRNA-1345 (RSV) Phase 3 (2023) — First non-COVID mRNA approval
15. **FDA** Moderna COVID-19 Vaccine BLA Approval Letter (2022)

## Tooling Documentation

### AWS Batch HPC Pipeline
- Job definition: `moderna-mrna-hpc:v2`
- Instance types: c5.18xlarge (standard), r5.24xlarge (memory-optimized)
- Spot bid: 60% of on-demand price
- Max vCPUs per account: 10,000
- Pipeline trigger: S3 event → Lambda → Batch job

### Benchling API Quick Reference
- Base URL: `https://moderna.benchling.com/api/v2`
- Authentication: OAuth 2.0 service account
- Key endpoints: `/experiments`, `/results`, `/assays`, `/sequences`
- Rate limit: 1000 req/min per account

### Microfluidic Parameters (Standard SM-102 LNP)
| Parameter | Value | Notes |
|-----------|-------|-------|
| Flow rate ratio (FRR) | 3:1 | Aqueous:Organic |
| Total flow rate (TFR) | 12-20 mL/min | Adjust for scale |
| Mixing chip | SHM or crevice-free | Precision Nanosystems |
| Ethanol content | 10-20% (v/v) | Optimize per lipid |
| N/P ratio | 3-10 | Molar ratio mRNA:ionizable lipid |
| Process temperature | 20-25°C | Room temperature standard |
