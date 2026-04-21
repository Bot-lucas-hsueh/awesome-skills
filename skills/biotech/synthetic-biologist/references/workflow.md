## § 8 — Standard Workflow

### Phase 1: Design & In Silico Modeling
```
Step 1: Define objective and success metrics
  → Titer target (g/L), yield (% theoretical), timeline, biosafety level
  → [✓ Done]: 1-page brief with KPIs signed off by PI/team lead

Step 2: Chassis selection
  → E. coli BL21(DE3) for protein production; MG1655 for metabolic engineering;
    S. cerevisiae CEN.PK for eukaryotic products
  → [✓ Done]: Chassis rationale documented with ≥3 comparison criteria

Step 3: Pathway/circuit design (in silico)
  → Run FBA with COBRApy: identify flux-limiting reactions and knockout targets
  → Design genetic parts list: promoter strength (RPU), RBS TIR, codon optimization
  → Simulate circuit with ODE model if toggle switch/oscillator
  → [✓ Done]: FBA analysis exported; parts list complete with BBa_IDs or synthesis specs

Step 4: Biosafety and IP review
  → Classify NIH risk group; check export control (EAR/ITAR) for dual-use sequences
  → [✓ Done]: IBC protocol number assigned
```

### Phase 2: Build / DNA Construction
```
Step 5: DNA synthesis and assembly
  → Order gene synthesis (Twist, IDT, Azenta) for sequences >100 bp
  → Gibson Assembly: 40 bp overlaps, 50–100 ng/fragment, 50°C/1h
  → Verify by Sanger sequencing (>99.9% accuracy required)
  → [✓ Done]: Sequence-verified constructs in stock glycerol at -80°C

Step 6: Transformation and strain construction
  → Electroporation (E. coli): 1.8 kV, 25 µF, 200 Ω, 0.1 cm cuvette
  → Colony PCR to confirm insertion; restriction digest pattern matches design
  → [✓ Done]: ≥3 correct transformants cryopreserved; plasmid map deposited in ELN

[✗ FAIL Action]: If <10% correct colonies → check ligation/Gibson overlap length;
re-sequence vector backbone for cryptic mutations before repeating.
```

### Phase 3: Test & Characterize
```
Step 7: Small-scale expression/production screening
  → 96-well deep-well plate screening: 600 µL, 30°C, 300 rpm, 24h
  → Measure: OD600 (growth), product titer (HPLC/LC-MS), fluorescence (GFP reporter)
  → [✓ Done]: >3× improvement over baseline OR mechanistic explanation for failure

Step 8: Shake flask characterization
  → 250 mL baffled flask, 50 mL LB + defined medium, 37→30°C shift at induction
  → Sample at 0, 2, 4, 8, 24h: OD600, residual glucose, product titer, acetate
  → [✓ Done]: Time-course data fits kinetic model; specific productivity ≥0.1 g/gDCW/h

Step 9: Learn and iterate
  → Compare model predictions vs experimental data; update kinetic parameters
  → Identify top-3 hypotheses for next DBTL cycle (e.g., bottleneck enzyme, toxic byproduct)
  → [✓ Done]: Next cycle design brief with ranked interventions by predicted impact
```
