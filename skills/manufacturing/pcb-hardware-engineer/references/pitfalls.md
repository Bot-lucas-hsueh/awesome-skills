## § 10 Common Pitfalls

### Anti-Pattern 1 — Split Ground Planes for "Noise Isolation"

❌ **BAD:**
```
// Split ground plane into "digital ground" and "analog ground"
// Route analog signals across the split
// Result: Uncontrolled impedance, increased EMI, ground loop
```

✅ **GOOD:**
```
// Keep solid continuous ground plane
// Use star grounding at power entry point instead
// Isolate analog circuits by component placement, not by splitting planes
// If split required: route signals perpendicular to split, add caps across
```

**Why it matters:** Splitting ground planes creates impedance discontinuities and disrupts return currents. The "split" approach was used in older analog designs but causes more problems in modern mixed-signal boards.

