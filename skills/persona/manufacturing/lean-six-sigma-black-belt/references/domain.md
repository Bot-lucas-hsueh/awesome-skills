## § 4 · Domain Knowledge

### Sigma Levels & DPMO

| Sigma | DPMO | Yield | Cpk |
|-------|------|-------|-----|
| 1σ | 691,462 | 30.85% | 0.33 |
| 2σ | 308,538 | 69.15% | 0.67 |
| 3σ | 66,807 | 93.32% | 1.00 |
| 4σ | 6,210 | 99.38% | 1.33 |
| 5σ | 233 | 99.977% | 1.67 |
| 6σ | 3.4 | 99.99966% | 2.00 |

```
Process Capability:
Cp = (USL - LSL) / (6 × σ)
Cpk = min[(USL - μ), (μ - LSL)] / (3 × σ)

Target: Cp ≥ 1.33, Cpk ≥ 1.33
World-class: Cpk ≥ 2.0 (6σ)
```

### Statistical Tools

```
DESCRIPTIVE:
├── Mean, median, mode
├── Standard deviation, variance
├── Histograms, box plots
└── Normal probability plot

INFERENTIAL:
├── Confidence intervals
├── Hypothesis tests (t-test, ANOVA)
├── Chi-square, proportion tests
└── Non-parametric tests

ADVANCED:
├── Regression (linear, logistic)
├── Design of Experiments (DOE)
├── Control charts (SPC)
└── Measurement systems (Gage R&R)
```

📄 **Full Details**: [references/08-domain-knowledge.md](references/08-domain-knowledge.md)

---
