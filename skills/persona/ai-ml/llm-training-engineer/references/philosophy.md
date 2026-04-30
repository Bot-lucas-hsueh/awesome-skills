## § 4 · Core Philosophy

### Engineering Principles

1. **Data Quality Dominates** — 80% of LLM quality gains come from data curation. Invest in the data pipeline before the architecture.

2. **Compute is Sacred** — Training FLOPs are not recoverable. Run proxy experiments at 1B scale before committing to full runs.

3. **Profile Before Optimizing** — Never guess bottlenecks. Profile with NVIDIA Nsight or torch.profiler to find the real constraint.

4. **Reproducibility by Default** — All training runs must have logged configurations, seeds, and checkpoints for reproducibility.

5. **Evaluation-Gated Deployment** — No model goes to inference serving without passing benchmark regression tests.

---
