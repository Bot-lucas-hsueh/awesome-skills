## § 8 — Standards & Reference

### 8.1 Research Frameworks

| Framework | When to Use | Key Steps |
|-----------|-------------|-----------|
| **AlphaZero Self-Play** | Games with known rules | Initialize → Self-play → Train → Evaluate → Iterate |
| **AlphaFold Structure Prediction** | Protein/biomolecule structure | MSA → Evoformer → Structure Module → Confidence |
| **Gemini Multimodal Training** | Native multimodal models | Tokenize all modalities → Pre-train → Fine-tune → RLHF |
| **SIMA Embodied Training** | Instruction-following agents | Human demos + language → Cross-modal fusion → Policy |

### 8.2 Evaluation Metrics

| Domain | Metric | Target |
|--------|--------|--------|
| Games | Elo rating | >3000 (superhuman) |
| Protein | GDT_TS / lDDT | >90 (high accuracy) |
| Protein | PAE | <5Å (confident prediction) |
| LLM | MMLU | >90% (expert level) |
| Math | IMO score | Gold medal (42/42) |
| Embodied | Task success rate | >70% (near-human) |

---
