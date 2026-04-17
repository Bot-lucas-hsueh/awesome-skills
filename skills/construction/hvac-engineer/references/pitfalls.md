## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Oversizing Equipment**

```markdown
❌ BAD: Using "add 20% for safety" on load calculation → 400-ton
chiller for 320-ton load → chiller short-cycles, inefficient, poor dehumidification.

✅ GOOD: Size at calculated load × 1.10 (for turndown). Use Variable Speed
Drives for part-load, not oversizing.
```

**Anti-Pattern 2: No Commissioning**

```markdown
❌ BAD: Installing systems without testing → discover problems at
occupancy → complaints, rework, warranty claims.

✅ GOOD: Specify full commissioning per ASHRAE; include acceptance
testing of all controls; witness by owner representative.
```

**Anti-Pattern 3: Inadequate Controls Integration**

```markdown
 ❌ BAD: HVAC and controls specified by different parties, not
coordinated → incompatible systems, sequence doesn't work.

✅ BEST: Single spec for HVAC + controls; integrated design team
from day one; sequence of operation drives controls selection.
```

### 🟡 Medium Severity

**Anti-Pattern 4: Ignoring Diversity**

```markdown
❌ BAD: Designing all VAV boxes at max → oversized duct,
wasted energy, poor control.

✅ GOOD: Use diversity factor (0.8-0.9) for peak design; load
profile shows all zones at peak simultaneously is rare.
```

**Anti-Pattern 5: Wrong Outdoor Air Strategy**

```markdown
❌ BAD: Economizer without proper control → brings in hot humid
air → system can't dehumidify → comfort failure.

✅ GOOD: Specify differential enthalpy control for economizer;
include limit on outdoor air conditions.
```

**Anti-Pattern 6: Ignoring Maintainability**

```markdown
❌ BAD: Equipment in inaccessible location → filters not changed,
coils not cleaned → performance degrades over time.

✅ GOOD: Design for maintainability: access space, serviceability,
filter replacement access.
```

