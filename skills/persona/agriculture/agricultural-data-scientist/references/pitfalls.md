## 10. Common Pitfalls & Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|----------------------|-----------------|---------------------|
| 1 | **Building models without enough data** | 🔴 High | Need 5+ years data for robust models; collect more before modeling |
| 2 | **Ignoring spatial autocorrelation** | 🔴 High | Neighboring points are similar; use spatial statistics |
| 3 | **Overly complex models** | 🔴 High | Simple models with good data beat complex; start simple |
| 4 | **No validation** | 🔴 High | Always hold out test data; validate on new seasons |
| 5 | **Analysis without delivery** | 🟡 Medium | Build for delivery from start; notebooks have no impact |
| 6 | **Ignoring farmer input** | 🟡 Medium | Combine model predictions with farmer knowledge |

```
❌ BAD: "Let's use deep learning - it's the most advanced"
✅ GOOD: "Start with random forest or linear regression. 
        More complex models require more data and are harder to interpret.
        Simple models that work are better than complex models that fail."

❌ BAD: "Here are predictions - good luck!"
✅ GOOD: "Predictions have 85% accuracy (±10%).
        Here's a dashboard where you can explore by field.
        Set up alerts for when predictions change significantly.
        We'll validate against actual harvest data."
```
