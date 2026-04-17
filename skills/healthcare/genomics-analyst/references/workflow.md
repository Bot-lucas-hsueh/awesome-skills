## § 8 · Standard Workflow

### 8.1 Variant Interpretation

```
Phase 1: Variant Extraction
├── Identify variant(s) from sequencing data
├── Confirm variant call (IGV visualization)
├── Retrieve associated clinical information
└── Note gene, position, change (HGVS notation)

Phase 2: Evidence Gathering
├── Population databases: gnomAD, ExAC (minor allele frequency)
├── Disease databases: ClinVar, HGMD (previous classifications)
├── Literature: PubMed (functional studies, case reports)
├── In silico: SIFT, PolyPhen, REVEL (predictive scores)
└── Gene-disease: ClinGen (validity, inheritance)

Phase 3: ACMG Criteria Application
├── Apply pathogenic criteria (PVS1 > PS > PM > PP)
├── Apply benign criteria (BA > BS > LB)
├── Weight criteria per strength
├── Apply rules for combination of criteria
└── Document criteria used

Phase 4: Classification Decision
├── Calculate evidence balance
├── Apply classification rules
├── Determine final class: P/LP/VUS/LB/B
└── Document rationale with supporting evidence

Phase 5: Reporting
├── Prepare clinical report
├── Include variant classification and evidence
├── Add management recommendations
└── Recommend clinical correlation and family studies
```

### 8.2 NGS Data Quality Assessment

```
Step 1: Review QC metrics (coverage, Q30, on-target rate)
Step 2: Verify no systematic failures in target regions
Step 3: Confirm positive control variant detected
Step 4: Review any regions below minimum coverage
Step 5: Assess variant call quality scores
Step 6: Document analytical limitations
```

---
