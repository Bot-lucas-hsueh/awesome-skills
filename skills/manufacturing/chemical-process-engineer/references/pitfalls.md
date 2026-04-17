## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Ignoring Thermodynamic Validation**

```markdown
❌ BAD: Using Raoult's Law for polar systems (ethanol-water), getting 40% error in
distillation, oversizing column by 50% → massive CAPEX waste.

✅ GOOD: Use activity coefficient model (NRTL, UNIQUAC) for non-ideal mixtures;
validate against VLE data from NIST or DDBST.
```

**Anti-Pattern 2: No Safety Margin on Relief Sizing**

```markdown
❌ BAD: Calculating PSV based on ideal gas only, ignoring two-phase flow.
During fire, vessel fills with liquid → PSV undersized → catastrophic failure.

✅ GOOD: Use DIERS methodology for two-phase relief; size for worst-case
overpressure scenario, not just calculated rate.
```

**Anti-Pattern 3: Design Without P&ID**

```markdown
❌ BAD: Sizing heat exchanger without knowing if it's thermosiphon or
pumped circulation → LMTD wrong by 2× → equipment wrong size.

✅ GOOD: Require P&ID before equipment design; understand process flow
configuration before sizing.
```

### 🟡 Medium Severity

**Anti-Pattern 4: Ignoring Heat Integration**

```markdown
❌ BAD: Adding steam heater and cooling tower without evaluating waste heat
recovery. 30% higher utility costs for plant life → $5M extra OPEX.

✅ GOOD: Mandatory Pinch Analysis for plants >5 MW heating duty;
specify heat recovery between process streams.
```

**Anti-Pattern 5: Oversizing Without Justification**

```markdown
❌ BAD: "Let's oversize the reactor by 50% for safety" → 50% more catalyst cost,
more inventory, larger footprint → no technical basis = waste.

✅ GOOD: Size based on process requirement + appropriate safety factor
(typically 10-20% for volumetric, 0% for heat transfer).
```

**Anti-Pattern 6: Ignoring Corrosion**

```markdown
❌ BAD: Specifying carbon steel for 10% HCl service → 5 mm/year corrosion →
leak in 18 months → unplanned shutdown, potential fire.

✅ GOOD: Reference NACE/AMPP for material selection; specify 316L SS,
glass-lined, or rubber-lined equipment for corrosive service.
```

