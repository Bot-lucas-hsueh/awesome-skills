## § 8 · Scenario Examples

### Scenario 1: Rare Disease WGS Analysis

**Context**: 5-year-old patient with undiagnosed neurodevelopmental disorder; trio WGS (proband + parents).

**Analysis Plan**:
1. **QC**: Confirm 30x coverage, Q30 > 85%
2. **Alignment**: BWA-MEM to GRCh38
3. **Variant Calling**: GATK HaplotypeCaller → DeepVariant ensemble
4. **Filtering**: 
   - MAF < 1% (gnomAD)
   - Impact: HIGH or MODERATE
   - Inheritance: de novo, compound heterozygous, or homozygous recessive
5. **Prioritization**: 
   - OMIM phenotype matching
   - Brain expression (GTEx)
   - Conservation (GERP++, PhyloP)
6. **Reporting**: Top 5 candidates with ACMG classification

**Key Findings Example**: 
- *SCN2A* de novo missense (p.R853Q) - ACMG Likely Pathogenic
- Known cause of early infantile epileptic encephalopathy
- Functional studies show gain-of-function sodium channel defect

---

### Scenario 2: Cancer Tumor-Normal Pairs

**Context**: Metastatic melanoma, need somatic mutation profile for targeted therapy selection.

**Analysis Plan**:
1. **Purity/Ploidy**: Estimate tumor cellularity (PurBayes, ASCAT)
2. **Somatic Variants**: Mutect2 + Strelka2 ensemble
3. **Copy Number**: GATK gCNV or CNVkit
4. **Annotation**: 
   - COSMIC cancer mutations
   - OncoKB actionable alterations
   - Clinical trial matching (TrialMatch)
5. **HRD Score**: Homologous recombination deficiency for PARP inhibitor eligibility
6. **TMB/MSI**: Tumor mutational burden, microsatellite instability

**Actionable Finding Example**:
- *BRAF* p.V600E (VAF 42%)
- Treatment: Dabrafenib + Trametinib combination
- Clinical benefit: 60% response rate in metastatic melanoma

---

### Scenario 3: Bulk RNA-seq Differential Expression

**Context**: Drug treatment vs. control in cell line model; 3 replicates per condition.

**Analysis Plan**:
1. **Quantification**: Salmon quasi-mapping with bias correction
2. **Import**: tximport → DESeq2
3. **QC**: PCA, sample clustering, outlier detection
4. **DE Analysis**: Wald test, shrunken LFC (apeglm)
   - FDR < 0.05
   - |log2FC| > 1
5. **Pathway Analysis**: 
   - GSEA (fgsea) with Hallmark gene sets
   - GO/KEGG over-representation
6. **Visualization**: Volcano plots, heatmaps, enrichment plots

**Key Results**:
- 847 DEGs (423 up, 424 down)
- Top pathway: Interferon gamma response (NES 2.3, FDR < 0.001)
- Lead genes: *STAT1*, *IRF1*, *CXCL10* (immune activation signature)

---

### Scenario 4: Single-Cell RNA-seq Analysis

**Context**: 10,000 cells from tumor biopsy; characterize tumor microenvironment.

**Analysis Plan**:
1. **Preprocessing**: Cell Ranger count → Seurat
2. **QC**: nFeature_RNA 200-5000, percent.mt < 10%
3. **Normalization**: SCTransform
4. **Integration**: Harmony (if multiple samples)
5. **Clustering**: Louvain (resolution 0.8)
6. **Annotation**: SingleR + marker gene manual curation
   - Malignant: *MKI67*, high CNV score
   - T cells: *CD3D*, *CD8A*/CD4
   - Macrophages: *CD68*, *CD163*
   - Fibroblasts: *COL1A1*, *ACTA2*
7. **Downstream**: 
   - Differential expression per cluster
   - Cell-cell communication (CellChat)
   - Trajectory analysis (Monocle3)

**Key Insights**:
- 8 cell clusters identified
- Exhausted CD8+ T cell subpopulation in tumor core
- Macrophage M2 polarization correlates with poor prognosis signature

---

### Scenario 5: Pharmacogenomic Clinical Report

**Context**: Pre-emptive pharmacogenomic testing for psychiatric medication selection.

**Genes Analyzed**: *CYP2D6*, *CYP2C19*, *CYP2C9*, *SLCO1B1*, *HLA-B*

**Analysis**:
1. **Star Allele Calling**: Cyrius (CYP2D6), Stargazer (other CYPs)
2. **Diplotype Translation**: Activity scores, predicted phenotypes
3. **Drug-Gene Interactions**: CPIC guidelines, FDA table
4. **Report Generation**: 
   - Current medications: impact assessment
   - Future prescribing: recommendations by drug class

**Example Finding**:
- *CYP2D6* genotype: *4/*10 (poor metabolizer, activity score 0.5)
- Impact: Reduced tramadol efficacy (prodrug), increased risk of amitriptyline toxicity
- Recommendation: Avoid tramadol; use alternatives; if TCAs needed, start at 50% dose

---
