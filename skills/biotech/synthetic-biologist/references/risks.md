## § 3 — Risk Disclaimer

> All genetic engineering work must be conducted under appropriate biosafety oversight. This skill provides scientific guidance only — regulatory compliance is the researcher's responsibility.
>

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Unintended horizontal gene transfer** | 🔴 High | Antibiotic resistance genes on plasmids can transfer to environmental microbes if organisms are released | Use non-standard antibiotic resistance markers or auxotrophic selection; never use clinical last-resort antibiotics (colistin, carbapenem) as selection markers |
| **Metabolic burden killing the host** | 🔴 High | Overexpressing 5+ heterologous genes can reduce growth rate >80%, causing culture collapse before any product is made | Monitor burden via OD600/h and specific productivity; use inducible promoters (T7-lac, arabinose) to decouple growth phase from production phase |
| **Off-target CRISPR edits** | 🔴 High | Cas9 with >3 mismatches can still cleave off-target sites, causing undetected mutations that confound results | Run CRISPOR off-target prediction; validate edited strains by whole-genome sequencing before phenotypic characterization |
| **Plasmid instability under selection pressure** | 🟡 Medium | Mutations in toxic gene products or promoters can cause plasmid segregation loss within 20 generations | Include stringent plasmid origin (ColE1 ~500 copies); verify construct integrity by restriction digest every 5 passages; use chromosomal integration for industrial strains |
| **Contamination masking true phenotype** | 🟡 Medium | A faster-growing contaminant can dominate a 5 L bioreactor within 8 hours, giving false productivity data | Implement sterility testing (Gram stain, 16S rRNA PCR) at inoculation, 24h, 48h; use defined minimal media with selective carbon sources |
| **Regulatory compliance gaps** | 🔴 High | GMO release or therapeutic protein production without IND/BLA filing violates FDA/EPA regulations; fines up to $1M/day | Classify organism under NIH Guidelines; notify EPA for Significant New Use Rules (SNUR); file IND for any human-use biological product |

---
