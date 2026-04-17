## § 8 Standard Workflow

### Phase 1 — Measurement System Validation
- Identify critical-to-quality (CTQ) characteristics
- Design and execute Gage R&R study (10 parts, 3 operators, 3 trials)
- Calculate %GR&R and determine if measurement system is acceptable
- If %GR&R > 30%: Improve gauge or method before proceeding
- [✓ Done]: GR&R < 30%, measurement system validated
- [✗ FAIL]: GR&R > 30%, measurement system not validated

### Phase 2 — Process Capability Study
- Produce 100+ samples covering normal process variation
- Measure all samples using validated measurement system
- Calculate Cpk using subgroup statistics
- Compare to target (≥1.33 for production release)
- [✓ Done]: Cpk ≥ 1.33, process capable, release to production
- [✗ FAIL]: Cpk < 1.33, process not capable, improve before release

### Phase 3 — SPC Implementation
- Select appropriate control chart type (X-bar/R, X-bar/S, attribute)
- Define sampling frequency and sample size
- Train operators on chart interpretation and reaction plan
- Set up control chart in production with clear out-of-control actions
- [✓ Done]: SPC charts active, operators trained, reaction plan documented
- [✗ FAIL]: Charts not monitored, no reaction plan, operators not trained

### Phase 4 — Continuous Monitoring & Improvement
- Review SPC charts daily for out-of-control conditions
- Investigate root cause for each out-of-control signal
- Track DPMO and Cpk trends over time
- Initiate improvement projects for low Cpk characteristics
- [✓ Done]: Control maintained, improvement trending, defect rate decreasing
- [✗ FAIL]: Out-of-control ignored, no trend improvement, defects increasing

---

