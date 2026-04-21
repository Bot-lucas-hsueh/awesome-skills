## § 10 — Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Ignoring Metabolic Burden


❌ **BAD:** Cloning 5 pathway genes on a single high-copy plasmid (ColE1) under constitutive strong promoters (J23119) in all genes.

✅ **GOOD:** Use inducible promoter (T7lac with IPTG) to decouple growth from production; balance expression levels with staggered RBS strengths (RBS Calculator TIR: upstream gene 10,000; downstream gene 1,000–3,000). Switch to low-copy origin (p15A) for toxic genes.

**Why it matters:** A 50% growth rate reduction means you need 2× more fermentation time and 2× higher production cost. Metabolic burden-induced plasmid loss can crash a 100 L bioreactor batch after 20 hours.

### Anti-Pattern 2: Context-Independent Parts Characterization


❌ **BAD:** Using a promoter characterized with a GFP reporter and expecting the same strength when driving a metabolic enzyme 10 kb downstream in a multi-gene operon.

✅ **GOOD:** Flank all genetic elements with insulator sequences (RiboJ ribozyme + B0032 RBS) to isolate each gene from upstream context effects. Always measure promoter strength in the final construct context using a quantitative assay (qRT-PCR, proteomics).

**Why it matters:** Context-dependent expression variation of 5–20× is well-documented in synthetic biology. One poorly-expressed enzyme can cut total pathway flux by >80%.

### Anti-Pattern 3: Skipping FBA Before Building Strains


❌ **BAD:** Directly cloning a 6-gene heterologous pathway without checking theoretical yield or flux distribution.

✅ **GOOD:** Run FBA (COBRApy) first to: (a) check theoretical max yield; (b) identify competing pathways; (c) predict which knockouts improve flux by >20%. This saves 2–4 DBTL cycles and $5,000–$20,000 in experimental costs.

**Why it matters:** Without FBA, teams routinely spend months engineering a pathway that has a 2% theoretical carbon yield — thermodynamically impossible to be commercially viable.

### Anti-Pattern 4: No Sterility Controls in Bioreactor


❌ **BAD:** Inoculating a 10 L bioreactor and only checking sterility at the end of the 72-hour run.

✅ **GOOD:** Take sterility samples at t=0, t=8h, t=24h (Gram stain + spread plate on LB). A contamination event at t=8h caught early saves $5,000–$50,000 in media and lost production time.

### Anti-Pattern 5: Using Clinical Antibiotics as Selectable Markers


❌ **BAD:** Using colistin or meropenem resistance as plasmid selection marker "because they're available in the freezer."

✅ **GOOD:** Use ampicillin, kanamycin, or chloramphenicol for standard lab work. For industrial strains, use auxotrophic markers (ΔtrpC + trpC plasmid) or non-antibiotic selection (sucrose sensitivity via sacB).
