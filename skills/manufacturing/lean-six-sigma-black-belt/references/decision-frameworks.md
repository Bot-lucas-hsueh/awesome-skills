## § 5 · Decision Frameworks

### Project Selection Matrix

| Criteria | Weight | Score 1-5 |
|----------|--------|-----------|
| Financial Impact | 25% | $ savings |
| Customer Impact | 20% | CTQ alignment |
| Strategic Alignment | 20% | Business goals |
| Feasibility | 20% | Data availability |
| Urgency | 15% | Pain level |

### Hypothesis Testing Decision Tree

```
Data Type?
├── Continuous → t-test, ANOVA, regression
└── Discrete → Chi-square, proportion test

Number of Groups?
├── 2 groups → 2-sample t-test, paired t-test
└── 3+ groups → ANOVA, chi-square

Paired Data?
├── Yes → Paired t-test
└── No → 2-sample test

Normal Distribution?
├── Yes → Parametric tests
└── No → Non-parametric (Mann-Whitney, Kruskal-Wallis)
```

📄 **Full Details**: [references/09-decision-frameworks.md](references/09-decision-frameworks.md)

---
