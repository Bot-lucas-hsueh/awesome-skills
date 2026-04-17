## § 7 · Standards & Reference

### NIH R01 Specific Aims Structure

```
Specific Aims (1 page) — the most important page in the application

Paragraph 1 — Hook (2-3 sentences):
  "Cancer kills X Americans annually. [Your area] is the least understood aspect."

Paragraph 2 — State of the field (2-3 sentences):
  What is known? What critical gap exists?

Paragraph 3 — Your approach (2-3 sentences):
  What is your unique expertise/resource? What is your overall hypothesis?

Aims (typically 3, each ~2 sentences):
  Aim 1: [Verb] [outcome] using [approach]. [Rationale for feasibility].
  Aim 2: ...
  Aim 3: ...

Final paragraph — Innovation and Impact:
  "This research will [transform/establish/reveal] by..."
  "Expected outcomes: [specific, measurable deliverables]"

Writing rules:
  - 1 page maximum; no exceptions
  - Each aim must be independently testable (if Aim 1 fails, Aims 2 and 3 still proceed)
  - Avoid "we will show that..." (presupposes the conclusion)
  - Use "we will TEST THE HYPOTHESIS THAT..." (proper falsifiable framing)
```

### Power Analysis Quick Reference

```python
from scipy import stats
import numpy as np

# Two-sample t-test (comparing two group means)
def power_t_test(effect_size_d, alpha=0.05, power=0.80):
    """
    effect_size_d: Cohen's d (small=0.2, medium=0.5, large=0.8)
    Returns: n per group
    """
    from statsmodels.stats.power import TTestIndPower
    analysis = TTestIndPower()
    n = analysis.solve_power(effect_size=effect_size_d, alpha=alpha, power=power)
    return int(np.ceil(n))

# Examples:
# Small effect (d=0.2): n=394/group
# Medium effect (d=0.5): n=64/group
# Large effect (d=0.8): n=26/group
# Always round UP; add 10-20% for anticipated dropout
```

### CONSORT Reporting Checklist (RCT)

```
Key items researchers commonly miss:
□ CONSORT flow diagram (enrollment → allocated → analyzed with numbers at each step)
□ Allocation concealment method (not just "randomized")
□ Blinding: who was blinded (participants, providers, outcome assessors) and how
□ Primary outcome pre-specified (matches registration); secondary outcomes labeled as exploratory
□ ITT (intention-to-treat) analysis as primary
□ Effect size with 95% CI for primary outcome (not just p-value)
□ Harms and adverse events reported
□ Trial registration number and registry
```

---
