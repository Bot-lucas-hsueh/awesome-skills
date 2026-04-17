## § 10 Common Pitfalls

### Anti-Pattern 1 — Calculating Cpk on Unstable Process

❌ **BAD:**
```
// Process has clear trends and shifts on control chart
// Calculated Cpk = 1.45
// Released to production
// Result: Defects spike within 1 week
```

✅ **GOOD:**
```
// Before Cpk calculation:
    // 1. Run SPC chart for 20+ subgroups
    // 2. Apply Western Electric rules to detect instability
    // 3. If any out-of-control: investigate cause first
    // 4. Only calculate Cpk on STABLE process
    
// Rule: Cpk requires process stability first
// A process with Cpk = 1.45 but out-of-control is NOT capable
```

**Why it matters:** Cpk on an unstable process is meaningless — the mean and sigma are not representative of future performance. Defects will occur.

---

### Anti-Pattern 2 — Using Cpk Instead of Ppk for Validation

❌ **BAD:**
```
// Initial process study: Cpk = 1.67 (passes)
// Released to production
// 1 month later: defect rate 5% (should be < 0.5%)
// What happened?
```

✅ **Correct Approach:
```
Two types of capability:

1. Cpk (Process Capability):
   - Short-term: Uses R-bar/d2 or S-bar/c4 to estimate σ
   - Indicates POTENTIAL capability
   - Use for: Process improvement, machine capability

2. Ppk (Process Performance):
   - Long-term: Uses overall standard deviation s
   - Indicates ACTUAL performance
   - Use for: Production release, customer PPAP

REQUIREMENT:
- BOTH Cpk ≥ 1.33 AND Ppk ≥ 1.67 before production release
- If Ppk < Cpk: process not stable (investigate)
```

**Why it matters:** Cpk measures what the process could do (short-term); Ppk measures what it actually does (long-term). Use both.

---

### Anti-Pattern 3 — Reacting to Common Cause Variation

❌ **BAD:**
```
// Operator sees 1 point outside 3σ control limits
// "Something is wrong, must adjust machine"
// Adjusts the process
// Variation actually increases (tampering)
```

✅ **Correct Response:
```
Control Chart Rules (Western Electric):
  1. One point outside 3σ → INVESTIGATE (not adjust)
  2. Two of three outside 2σ → INVESTIGATE  
  3. Four of five outside 1σ → INVESTIGATE
  4. Eight consecutive on one side → INVESTIGATE

INVESTIGATE means:
  - Check if special cause exists (material, tool, operator change)
  - If yes: remove cause and correct
  - If no: variation is common cause — DO NOT ADJUST

"Adjustment" of common cause = "tampering" = makes things worse
```

**Why it matters:** Tampering (adjusting for common cause) increases variation. Control charts help distinguish when to act vs. when to leave the process alone.

---

### Anti-Pattern 4 — Inadequate Sample Size for Capability Study

❌ **BAD:**
```
// Measured 10 parts to calculate Cpk
// Cpk = 1.45 (passes)
// Customer audits and rejects: "Need minimum 100 parts"
// What happened?
```

✅ **Correct Sample Size:
```
Minimum sample size for Cpk:
  - Short-term (machine capability): 30 parts minimum
  - Long-term (process capability): 100 parts minimum
  
Rationale:
  - 10 parts: Cannot capture normal process variation
  - 30 parts: 95% confidence on Cpk estimate
  - 100 parts: 99% confidence; reflects true Ppk

IATF 16949 Requirement:
  - Minimum 100 measurements for initial process study
  - Must include process startup, normal running, and changeover
```

**Why it matters:** Small samples give unreliable Cpk estimates. A Cpk from 10 parts could be off by ±0.5 or more.

---

### Anti-Pattern 5 — Setting Control Limits from Specification

❌ **BAD:**
```
// USL = 10.015, LSL = 9.985
// Control limits set at: UCL = 10.015, LCL = 9.985
// Using specification limits as control limits
// Process runs, many points outside but "in spec"
// Result: Late detection of process drift
```

✅ **Correct Control Limits:
```
Control limits (UCL/LCL) come from PROCESS data, not spec:

1. Calculate process mean (X-bar) and sigma
2. UCL = X-bar + 3σ
3. LCL = X-bar - 3σ
4. Specification limits are INDEPENDENT

Example:
  Process mean: 10.000
  Process sigma: 0.003
  UCL: 10.009
  LCL: 9.991
  
  USL: 10.015 (specification - NOT control limit!)
  LSL: 9.985 (specification - NOT control limit!)

Why:
  - Control limits: detect process CHANGES (stability)
  - Specification limits: detect if process meets REQUIREMENTS (capability)
  - Different purposes = different values
```

**Why it matters:** Using spec limits as control limits removes the ability to detect process drift before defects occur.

---

### Anti-Pattern 6 — Accepting Supplier Data Without Verification

❌ **BAD:**
```
// Supplier sends Cpk = 1.67 report for incoming parts
// Accept based on supplier certificate
// 2 months later: 15% defect rate on assembly line
// Supplier says: "Our process changed"
```

✅ **Correct Incoming Quality:
```
Supplier Data Verification:

1. REQUIRE PPAP (Production Part Approval Process):
   - Control Plan, FMEA, Process Flow, MSA, Capability Data
   - Full PPAP required for new parts and changes

2. INCOMING VERIFICATION:
   - First article inspection (first shipment)
   - Periodic capability verification (quarterly)
   - Risk-based inspection level (per ANSI Z1.4)

3. ONGOING MONITORING:
   - Supplier scorecard (quality, delivery, response)
   - Continuous monitoring of incoming defect rate
   - Escalation for degradation

4. IF SUPPLIER CHANGES PROCESS:
   - Requires new PPAP submission
   - Enhanced inspection until re-verified
```

**Why it matters:** Supplier capability is an assertion, not a fact. Verify with incoming inspection and ongoing monitoring.

---

