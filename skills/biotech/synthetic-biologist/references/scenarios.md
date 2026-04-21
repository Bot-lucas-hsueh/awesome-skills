## § 9 — Scenario Examples

### Scenario 1: Designing a Lycopene Production Pathway in E. coli


**User:** I want to produce lycopene in E. coli. Where do I start?

**Expert:**
Great choice — lycopene is a well-studied model compound for carotenoid pathway engineering. Here's a systematic approach:

**Step 1: Pathway Overview**
Lycopene requires the MEP (methylerythritol phosphate) pathway (native in E. coli) + 3 heterologous genes:
- `crtE` (GGPP synthase, from *Erwinia herbicola*) — BBa_K118014
- `crtB` (phytoene synthase) — BBa_K118013
- `crtI` (phytoene desaturase, 4 desaturation steps → lycopene) — BBa_K118012

**Step 2: FBA Analysis (COBRApy)**
```python
import cobra
model = cobra.io.load_model("e_coli_core")
# Add lycopene demand reaction
model.add_boundary(model.metabolites.get_by_id("ipdp_c"), type="demand")
solution = model.optimize()
print(f"Theoretical max: {solution.objective_value:.4f} mmol/gDCW/h")
# → ~0.34 mmol/gDCW/h (~0.12 g/L in batch; limited by NADPH for MEP pathway)
```

**Step 3: Parts Assembly Strategy**
```
Construct design (pET28a backbone, ~5.4 kb):
T7lac promoter → RBS(BBa_B0034, TIR=1000) → crtE → RBS(0.3×) → crtB → RBS(0.1×) → crtI → T1 terminator

Rationale: Stagger RBS strengths to balance flux — high crtE (upstream), low crtI (downstream)
to prevent phytoene accumulation. Use pURI3-Cter for balanced expression.
```

**Step 4: Key metrics to track**
- Lycopene titer: HPLC at 472 nm (ε = 18,500 M⁻¹cm⁻¹ in hexane)
- Target: >50 mg/L in flask; >1 g/L with MEP pathway upregulation (dxs overexpression)
- Culture: BL21(DE3), 37→25°C at OD600=0.6, 0.1 mM IPTG, 24h

---

### Scenario 2: CRISPR Multiplex Knockout in S. cerevisiae


**User:** I need to knock out 4 genes (ARO7, TRP2, PDC1, PDC5) in yeast simultaneously. How?

**Expert:**
Multiplex CRISPR in yeast using Cas9 from *S. pyogenes* with 4 simultaneous gRNAs:

**gRNA Design (via CRISPOR):**
```
Gene    | 20-nt Spacer             | PAM | Off-target score | Efficiency
ARO7    | GCATACGGACTTGATCCTAA    | CGG | 82/100           | 68%
TRP2    | AATGGCATACTTCTGACGTA    | AGG | 91/100           | 71%
PDC1    | GTTCAATGGCATACGGACTT    | TGG | 88/100           | 74%
PDC5    | CGGACTTGATCCTAACGTAG    | CGG | 79/100           | 65%
```

**Multiplex delivery vector:**
Use pCAS2 backbone (CEN/ARS, HIS3 marker) with 4 × SNR52 promoter → gRNA → SUP4 terminator cassettes in tandem (total insert ~1.2 kb).

**Protocol:**
1. Transform with Cas9/gRNA plasmid + 4 × 120 bp repair oligos (40 bp homology each side, stop codon insertion)
2. Select on -His plates; screen by colony PCR with gene-specific primers
3. Expected efficiency: ~30–60% quadruple knockout per transformation
4. Validate by Sanger sequencing + phenotype (no ethanol from PDC knockouts in glucose)

**Scale-up tip:** For industrial strains, switch to CRISPR-AID (3-in-1 activation/interference/deletion) to avoid plasmid burden.

---

### Scenario 3: Troubleshooting Low Product Titer


**User:** My lycopene titer is stuck at 8 mg/L after 3 optimization rounds. What am I missing?

**Expert:**
Classic plateau — let's diagnose systematically using the diagnostic decision tree:

**Diagnosis Checklist:**
```
1. Is the pathway expressed?
   → RT-qPCR: check crtE/crtB/crtI mRNA levels (expect >5× over vector control)
   → If low: check T7 RNA polymerase induction, IPTG concentration

2. Is MEP pathway the bottleneck?
   → Overexpress dxs (DXP synthase): usually gives 3–5× titer increase
   → Add 0.5% glucose + limit aeration (MEP pathway is O2-sensitive)

3. Is precursor (IPP/DMAPP) being diverted?
   → Check squalene pathway competition: knock out ispA overexpression
   → Add MVA pathway from S. cerevisiae (heterologous, avoids MEP bottleneck)

4. Is lycopene being degraded?
   → Protect with antioxidants: add 0.1 mM ascorbic acid to medium
   → Check for carotenoid cleavage dioxygenase genes in genome

5. Metabolic burden too high?
   → Reduce plasmid copy number (p15A origin instead of pUC); use chromosomal integration
   → Two-stage fermentation: biomass accumulation (37°C) → production (25°C)
```

**Most likely fix:** Overexpress `dxs` + `idi` (IPP isomerase) — together typically yields 20–50 mg/L without other changes.
