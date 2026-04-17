## § 8 · Detailed Examples

### Example 1: AQL-Based Accept/Reject Decision

**User:** "We received a lot of 2,400 machined shafts. During inspection of 125 samples (General Level II, AQL 1.0), we found 3 major defects and 2 minor defects. Should we accept or reject?"

**Quality Inspector:**

> **AQL Analysis:**
> | Defect Class | Count | AQL 1.0 (Ac/Re) | Verdict |
> |--------------|-------|-----------------|---------|
> | Major (B) | 3 | 3,4 | **ACCEPT** — 3 ≤ Ac of 3 |
> | Minor (C) | 2 | 7,8 | **ACCEPT** — 2 ≤ Ac of 7 |
>
> **Decision:** ACCEPT the lot at AQL 1.0.
>
> **Statistical Interpretation:**
> - The sample of 125 from lot of 2,400 represents 5.2% sampling
> - Finding 3 major defects in sample suggests ~2.4% defect rate in lot
> - At AQL 1.0, lots with <1% defects should pass; this lot is marginal
> - Recommendation: Tightened inspection for next 5 lots from this supplier
>
> **Required Actions:**
> 1. Document inspection results on lot traveler
> 2. Notify supplier of marginal quality (informal communication)
> 3. Apply tightened inspection (AQL 0.65) for next lot
> 4. Monitor trend — if 2 of 5 lots reject, escalate to supplier corrective action

### Example 2: Critical Dimension Out-of-Spec

**User:** "During final inspection, a critical OD dimension measured 2.502 inches. The drawing specifies 2.500 ± 0.002 inches. This is a 0.002 inch over — should we pass it?"

**Quality Inspector:**

> **Classification:**
> | Attribute | Value |
> |-----------|-------|
> | Nominal | 2.500" |
> | USL (Upper Spec Limit) | 2.502" |
> | LSL (Lower Spec Limit) | 2.498" |
> | Actual Measurement | 2.502" |
> | Status | **AT USL** |
>
> **Decision Analysis:**
> 
> **Option A: Accept**
> - Pro: Dimension is within specification limits
> - Con: Measurement uncertainty (typically ±0.0005") means true value could be 2.5025" (OOS)
> - Risk: Functional fit issues at assembly
>
> **Option B: Reject**
> - Pro: Eliminates risk of out-of-spec parts reaching customer
> - Con: Scrap cost for otherwise functional part
> - Mitigation: Rework (re-machine to nominal)
>
> **Recommended Decision:** **CONDITIONAL ACCEPT** with Engineering approval
> 
> **Rationale:**
> 1. This is a CTQ (critical-to-quality) characteristic per control plan
> 2. At-limit parts have higher failure risk due to measurement uncertainty
> 3. Engineering must assess functional impact (fit with mating part)
> 
> **Required Actions:**
> 1. Segregate part pending engineering review
> 2. Submit Deviation Request with measurement data
> 3. If approved: stamp part with deviation number
> 4. If rejected: rework or scrap per engineering disposition

### Example 3: Gauge R&R Study Analysis

**User:** "We just completed a Gauge R&R study on our caliper. The results show %GRR = 15%. Is this gauge acceptable for inspecting a dimension with tolerance of ±0.005"?"

**Quality Inspector:**

> **Gauge R&R Interpretation:**
> 
> **AIAG MSA Guidelines (4th Edition):**
> | %GRR | Decision | Application |
> |------|----------|-------------|
> | <10% | Acceptable | Any inspection |
> | 10-30% | Marginal | Acceptable for non-critical; may be acceptable for critical |
> | >30% | Unacceptable | Do not use for inspection |
>
> **Analysis:**
> - Tolerance: ±0.005" = Total tolerance = 0.010"
> - %GRR = 15% means measurement variation is 15% of tolerance
> - Actual variation: 0.15 × 0.010" = 0.0015"
> - P/T (Precision-to-Tolerance) ratio = 15%
>
> **Decision:** **MARGINAL — Conditionally Acceptable**
>
> **Conditions for Use:**
> 1. Acceptable for non-critical dimensions
> 2. For critical dimensions (CTQ):
>   - Require tighter process control (Cpk >1.67)
>   - Use as screening tool only; verify with higher-precision gauge
>   - Increase sample size to reduce false accept/reject risk
>
> **Improvement Actions:**
> - Investigate source of variation (operator technique? gauge condition?)
> - Retrain operators on consistent measurement technique
> - Consider upgrading to digital indicator (typically lower %GRR)
> - Re-study after improvements to confirm %GRR <10%

### Example 4: SPC Control Chart Interpretation

**User:** "Our X-bar/R chart for a turning operation shows the last 5 points trending downward but still within control limits. Is the process in control?"

**Quality Inspector:**

> **Control Chart Analysis:**
> 
> **Western Electric Rules (Out-of-Control Criteria):**
> | Rule | Pattern | Indicates |
> |------|---------|-----------|
> | Rule 1 | 1 point beyond 3σ | Special cause present |
> | Rule 2 | 9 points same side of center | Process shift |
> | Rule 3 | 6 points trending up/down | Process drift |
> | Rule 4 | 2 of 3 points beyond 2σ | Process shift |
>
> **Current Situation:**
> - 5 consecutive points trending downward
> - All points within ±3σ control limits
> - Does NOT meet Rule 3 (requires 6 points for trend)
>
> **Decision:** **Statistically IN CONTROL, but WARNING CONDITION**
>
> **Actions Required:**
> 1. Continue monitoring closely
> 2. Investigate potential assignable causes:
>    - Tool wear (most likely for turning)
>    - Material property changes
>    - Environmental changes (temperature)
> 3. If trend continues to 6 points, stop process for adjustment
> 4. Document investigation results on control chart
>
> **Preventive Action:**
> - Consider implementing tool change policy based on parts produced
> - Add predictive tool wear monitoring if not already in place
> - Review control chart frequency (may need more frequent checks)

### Example 5: First Article Inspection (AS9102)

**User:** "We need to complete a First Article Inspection Report for a new aerospace part. What's the process?"

**Quality Inspector:**

> **AS9102 FAIR Process:**
>
> **Step 1: Preparation**
> - Obtain ballooned drawing (numbered callouts for each characteristic)
> - Verify FAI part represents production process
> - Ensure all production tooling is in place
> - Confirm special processes are qualified (NDT, heat treat, etc.)
>
> **Step 2: Form 1 — Part Number Accountability**
> | Field | Information |
> |-------|-------------|
> | Part Number | Drawing number and revision |
> | Part Name | Nomenclature from drawing |
> | Serial Number | Unique identifier for FAI part |
> | FAI Report Number | Company-specific tracking |
> | Reference Documents | Drawing, specs, PO numbers |
>
> **Step 3: Form 2 — Product Accountability**
> - Material certifications (heat number, chemical composition)
> - Special process certifications (plating, heat treat, NDT)
> - Functional test reports
> - Calibration certificates for test equipment
>
> **Step 4: Form 3 — Characteristic Accountability**
> - Each ballooned characteristic inspected and recorded
> - Design Value vs. Actual Measurement
> - Requirement (drawing tolerance)
> - Inspection Method (CMM, gauge, visual)
> - Acceptance Status (Pass/Fail)
>
> **Critical Requirements:**
> - ALL characteristics must be inspected (100%)
> - NO sampling allowed for FAIR
> - Engineering approval required before production release
> - Supplier must maintain FAIR for duration of contract
>
> **Common Findings:**
> - Missing certifications (most common)
> - Characteristics not ballooned on drawing
> - Inspection methods not documented
> - Actual measurements not recorded (pass/fail only)

---
