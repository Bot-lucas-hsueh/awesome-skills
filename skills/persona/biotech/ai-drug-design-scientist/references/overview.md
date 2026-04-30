## § 2 What This Skill Does

This skill enables 6 specific, measurable capabilities for AI-assisted drug design:

1. **Target Structure Analysis**: Interprets AlphaFold2/3 and experimental structures, identifies binding pockets with fpocket/SiteMap, assesses druggability scores (Dscore > 0.5), and maps key pharmacophore features with uncertainty quantification from pLDDT scores.

2. **De Novo Molecular Generation**: Runs and interprets outputs from DiffSBDD, TargetDiff, REINVENT 4, and LIMO for pocket-conditioned molecular generation; filters by Lipinski/Veber rules, synthetic accessibility (SA score < 4), and novelty against known databases.

3. **ADMET Profile Prediction & Risk Stratification**: Predicts and interprets ADMET endpoints across absorption, distribution, metabolism, excretion, and toxicity; assigns risk tiers (LOW/MEDIUM/HIGH) across 12+ endpoints with structural alert detection (PAINS, Brenk, NIH).

4. **GNN-QSAR Model Building**: Designs and validates graph neural network QSAR models using AttentiveFP, MPNN, or SchNet on ChEMBL/BindingDB data; reports R2, RMSE, and applicability domain; flags extrapolation predictions.

5. **Hit-to-Lead Optimization**: Conducts systematic SAR analysis, proposes bioisosteres and scaffold hops, performs multi-parameter optimization using weighted desirability functions, and tracks compound evolution through ADMET/potency space.

6. **Active Learning & Synthesis Prioritization**: Implements Bayesian optimization and uncertainty-aware acquisition functions (EI, UCB, Thompson sampling) to rank compound proposals for synthesis, minimizing experimental cycles to reach candidate quality.

---
