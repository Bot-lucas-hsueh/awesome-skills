## § 9 Scenario Examples

### Scenario 1 — Gage R&R Study Interpretation

**User:** Our Gage R&R study shows 35% total Gage R&R. The operator says the gauge is fine because "most of the variation is from the parts, not the gauge." Is this acceptable?

**Expert:** No — 35% GR&R is NOT acceptable. Let me explain why:

**Gage R&R Results:**
```
Total Gauge R&R:  35%
  - Repeatability (equipment):  18%
  - Reproducibility (operator): 17%
Part-to-Part:    65%
```

**The Operator's Misconception:**
The operator is confusing *variance* with *capability*. Yes, most of the variance (65%) is from parts, but 35% is still too high for quality decisions.

**Why 35% is Unacceptable:**
```
Gauge R&R = 35% means:
- 35% of observed variation is measurement error
- Two "identical" parts could measure differently by up to 35% of the spread
- For a critical characteristic with Cpk = 1.33, this means:
  - We cannot reliably distinguish good parts from bad parts
  - False rejects: ~15% of good parts fail inspection
  - False accepts: ~15% of bad parts pass inspection
```

**Required Actions:**
```
If GR&R > 30%:
  1. [IMMEDIATE] Do not use for production decisions
  2. [SHORT-TERM] Investigate:
     - Gauge resolution (need ≤ 1/10 of tolerance)
     - Gauge stability (warm-up, fixturing)
     - Operator technique (standardize procedure)
  3. [MEDIUM-TERM] Improve:
     - Upgrade gauge to higher precision
     - Add fixturing to reduce positioning error
     - Train operators on proper technique
  4. [VERIFY] Re-run Gage R&R after improvements
     Target: < 20% (ideally < 10%)
```

[NC] A Cpk calculated with 35% GR&R is meaningless — the true process capability cannot be determined.

---

### Scenario 2 — Cpk Improvement for Critical Characteristic

**User:** Our critical bore diameter (ø10.000 ± 0.015mm) has Cpk = 0.95. Customer requires Cpk ≥ 1.33 before PPAP approval. How do we improve?

**Expert:** To achieve Cpk ≥ 1.33, we need to either reduce variation (make sigma smaller) or center the process (move mean to target). Let me calculate:

**Current State:**
```
Specification: 9.985 - 10.015 mm
Current Mean:   10.008 mm (shifted high)
Current Sigma:  0.008 mm
Current Cpk:    min[(10.015-10.008)/(3×0.008), (10.008-9.985)/(3×0.008)]
              = min[0.29, 0.96] = 0.95 (not capable)
```

**Improvement Options:**

| Strategy | Action | Expected Cpk |
|----------|--------|-------------|
| Center the process | Adjust machine offset from 10.008 to 10.000 | 1.30 |
| Reduce variation | Improve tooling (new inserts, better rigidity) | 1.28 |
| Both | Center + reduce variation | 1.67+ |

**Recommended Path:**

**Step 1: Center Immediately**
```
Adjust machine offset: Target -0.008mm
New mean: 10.000mm
New Cpk: min[0.62, 0.62] = 0.62 (still not enough)
```

**Step 2: Reduce Variation (within 2 weeks)**
```
Root cause of variation (from FMEA):
  - Tool wear: 40% contribution
  - Material hardness: 30% contribution
  - Temperature: 20% contribution
  - Measurement: 10% contribution

Countermeasures:
  - Tool life management: Replace every 50 pieces (was 100)
  - Incoming material verification: Sort to hardness 60-62 HRC
  - Coolant temperature control: Install chiller ±1°C
```

**Step 3: Verify Capability**
```
After improvements:
  - New sigma: 0.005 mm (reduced from 0.008)
  - New mean: 10.000 mm (centered)
  - New Cpk: min[(10.015-10.000)/(3×0.005), (10.000-9.985)/(3×0.005)]
          = min[1.00, 1.00] = 1.00 (closer but still < 1.33)
```

**Additional Reduction Needed:**
```
To reach Cpk = 1.33:
  σ_required = (USL-LSL)
             = 0.030
             = 0.0038 mm
Current: 0.005 mm → Need 24% more reduction
```

**Action Plan:**
```
Week 1-2:  Center process to 10.000mm
Week 3-4:  Implement tool life management
Week 5-6:  Add incoming material verification
Week 7:    Re-run capability study
Expected:  Cpk ≥ 1.33 achieved
```

[RISK] Document all adjustments in Control Plan. Any process change requires re-validation.

---

### Scenario 3 — 8D Root Cause Analysis for Field Failure

**User:** We received a customer complaint: 3 field failures on our motor assembly (seized bearing). The root cause was "contaminated lubricant." How do I conduct an 8D to prevent recurrence?

**Expert:** "Contaminated lubricant" is a symptom, not a root cause. Let me guide you through proper 8D:

**8D Report Template:**

**D0: Initial Response (Immediate)**
```
- Contain field affected units: 2,500 units in field
- Sort at customer: 100% inspection of returned units
- Interim action: Clean and relubricate all field units at no cost
- Cost impact: $50,000
```

**D1: Team Formation**
```
Team Leader: Quality Manager
Members: Process Engineer, Manufacturing Engineer, Supplier Quality, Design Engineer
```

**D2: Problem Description**
```
What: Bearing seizure in motor assembly
Where: Customer location, 3 failures out of 2,500 deployed (0.12%)
When: First failure at 6 months, last at 11 months
How detected: Customer reported motor noise/failure
```

**D3: Interim Containment Actions**
```
- 100% inspection of WIP and FG for lubricant contamination
- Enhanced storage protection for lubricant
- Added visual inspection point at assembly
```

**D4: Root Cause Analysis (5 Whys):**

```
Why 1: Why did bearing seize?
→ Contaminated lubricant (metal particles)

Why 2: Why was lubricant contaminated?
→ Particles entered during assembly

Why 3: Why did particles enter during assembly?
→ Assembly tool had metal shavings (not cleaned properly)

Why 4: Why were metal shavings not cleaned?
→ Cleaning procedure was not in work instructions

Why 5: Why was cleaning procedure not documented?
→ "It was always done" — tribal knowledge, not standardized
```

**Root Cause:** Assembly tool cleaning procedure not standardized or documented

**D5: Permanent Corrective Action**
```
1. Create Standard Work: Document tool cleaning procedure (SOP-123)
2. Add to Control Plan: Tool cleaning as critical process step
3. Visual Standard: Create photos showing clean vs. contaminated
4. Training: Certify all operators on new procedure
5. Audit: Weekly audit of tool cleaning compliance
```

**D6: Implement and Verify Action**
```
- Implemented: All operators trained, SOP posted
- Verification: Zero defects in 90 days (6,000 units)
- Effectiveness: Defect rate reduced from 0.12% to 0%
```

**D7: Prevent Recurrence (Systemic Fix)**
```
- Update APQP/Control Plan for all assemblies
- Add cleaning verification to PFMEA
- Update ISO 9001 procedures: All cleaning must be documented
- Share lessons learned with other product lines
```

**D8: Recognize Team and Close**
```
- Team recognition: Quality bonus approved
- Document closed: 8D-2026-0342
- Customer: PPAP resubmitted and approved
```

---

