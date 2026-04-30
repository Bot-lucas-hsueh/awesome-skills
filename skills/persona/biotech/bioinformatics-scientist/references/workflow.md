## § 9 · Workflow

| Phase | Objective | Done Criteria | Fail Criteria |
|-------|-----------|---------------|---------------|
| **1. Data Ingestion** | Receive and validate raw data | MD5 verified, metadata complete, FASTQ valid | Corrupt files, mismatched checksums |
| **2. QC Assessment** | Evaluate data quality | MultiQC report generated, metrics pass thresholds | Q30 < 80%, contamination detected |
| **3. Processing** | Execute analysis pipeline | Alignments complete, variants called, quantification done | > 5% samples fail QC |
| **4. Quality Control** | Validate intermediate results | Coverage targets met, alignment rates > 90% | Systematic biases detected |
| **5. Analysis** | Perform statistical analysis | Differential analysis complete, clustering converged | Batch effects unresolvable |
| **6. Interpretation** | Biological/clinical interpretation | Pathway enrichment, variant classification done | No significant findings explainable |
| **7. Reporting** | Generate deliverables | Final report, VCFs, visualizations delivered | Inconsistent with QC findings |

---
