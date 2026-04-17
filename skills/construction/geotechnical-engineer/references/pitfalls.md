## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Designing Without Site Investigation**

```markdown
❌ BAD: Proposing pile foundation without any site investigation data →
guessing soil parameters → either massive over-design or catastrophic failure.

✅ GOOD: Require minimum 3-5 boreholes depending on building size;
obtain SPT and lab test data; specify groundwater conditions.
```

**Anti-Pattern 2: Ignoring Settlement**

```markdown
❌ BAD: Checking bearing capacity only, ignoring settlement →
building settles 300mm, cracks, becomes uninhabitable.

✅ GOOD: Calculate both total and differential settlement;
compare to performance criteria; design foundation to meet both.
```

**Anti-Pattern 3: Applying Wrong Soil Parameters**

```markdown
❌ BAD: Using peak strength (c', φ') for long-term settlement →
underpredicts consolidation, foundation fails over time.

✅ GOOD: Use effective stress parameters (c', φ') for long-term;
use undrained parameters (Su) for short-term stability.
```

### 🟡 Medium Severity

**Anti-Pattern 4: Not Considering Groundwater**

```markdown
❌ BAD: Designing foundation ignoring groundwater →
buoyancy reduces effective bearing, or dewatering required for excavation.

✅ GOOD: Always note groundwater depth; consider its effect on design
and construction; include dewatering in construction planning if needed.
```

**Anti-Pattern 5: Over-Designing for Peace of Mind**

```markdown
❌ BAD: Adding 50% to pile length "just to be safe" → massive
unnecessary cost, but doesn't address actual risks.

✅ GOOD: Apply appropriate safety factors (3 for bearing, 1.5 for slope);
don't add arbitrary margins; let risk assessment drive design.
```

**Anti-Pattern 6: Ignoring Group Effects for Piles**

```markdown
 ❌ BAD: Designing piles as if isolated → ignoring interaction,
efficiency drops, settlement increases unexpectedly.

✅ GOOD: Consider pile group effects; check efficiency factor;
use software to analyze group behavior for >4 piles.
```

