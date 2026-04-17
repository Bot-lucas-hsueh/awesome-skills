## § 10 Common Pitfalls

### Anti-Pattern 1 — Improving Before Measuring Baseline

❌ **BAD:**
```
// Implemented a new fixture to reduce defects
// Before: unknown defect rate
// After:  claimed 50% improvement
// Reality: No way to prove it — just perception
```

✅ **GOOD:**
```
// Baseline before improvement:
    // 1. Measure current state: Cpk = 0.89, DPMO = 2300
    // 2. Validate measurement system: GR&R = 22%
    // 3. Document with data: Pareto chart, trend chart
// After improvement:
    // 4. Measure new state: Cpk = 1.45, DPMO = 350
    // 5. Calculate improvement: 85% reduction confirmed
```

**Why it matters:** Without baseline data, there is no proof of improvement. Leadership will question the ROI, and the team cannot learn from failures.

