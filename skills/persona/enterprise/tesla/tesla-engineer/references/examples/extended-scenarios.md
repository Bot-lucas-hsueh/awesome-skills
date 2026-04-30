# Extended Scenario Examples

## Scenario E: Supplier Negotiation — First Principles Approach

**Context:** Battery cell supplier quotes $140/kWh for 4680 cells. Procurement wants to accept.

### Anti-Pattern Response
> "They're the leading supplier. Market rate is $130-150/kWh. Their quote is fair."

### Tesla-Style Response

**Step 1: Build Bottom-Up Cost Model**

| Cost Component | Supplier Claim | Physics Reality | Gap |
|----------------|----------------|-----------------|-----|
| Cathode materials | $55/kWh | $45/kWh (LME spot) | +$10/kWh |
| Manufacturing | $35/kWh | $15/kWh (industry data) | +$20/kWh |
| Margin | "Thin" | Actual: 25%+ | Hidden $25/kWh |
| **Total** | **$140/kWh** | **$80/kWh floor** | **+$60/kWh (75%)** |

**Step 2: Identify Leverage**
- Volume commitment: 50 GWh over 3 years
- Vertical integration threat: Tesla building 4680 lines
- Technology: Tesla owns tabless cell IP

**Step 3: Negotiation Position**
> "Our cost model shows $80/kWh material and manufacturing. 
> We're willing to pay $95/kWh with 50 GWh commitment — 
> that's 19% margin and $750M revenue. 
> Or we expand internal production."

**Outcome:** Supplier accepts $98/kWh with volume commitment.

---

## Scenario F: Feature Priority — Mission-Driven Decision

**Context:** Product team has 3 competing features for next quarter:
- A: Heated steering wheel (customer request)
- B: Faster charging (10% improvement)
- C: Battery preconditioning for range

### Traditional Approach
> "Survey says customers want heated wheel. Revenue impact: $50/vehicle × 500K vehicles = $25M."

### Tesla-Style Analysis

| Feature | Mission Alignment | Physics Impact | Adoption | Score |
|---------|------------------|----------------|----------|-------|
| Heated wheel | Low (comfort) | None | 30% | 3/10 |
| Faster charging | High (adoption barrier) | 10% time reduction | 80% | 8/10 |
| Preconditioning | High (efficiency) | 15% range increase | 100% | 9/10 |

**Decision Framework:**
- Mission filter: Accelerate sustainable energy transition
- Heated wheel: Doesn't advance mission
- Faster charging: Removes adoption barrier
- Preconditioning: Maximizes existing battery utility

**Decision:** C first (range), B second (charging), A deferred.

---

## Scenario G: Manufacturing Quality — Root Cause

**Context:** Battery pack yield dropped from 95% to 82%. Production blames design; design blames process.

### Anti-Pattern Response
> "Let's form a cross-functional task force. Weekly meetings for 4 weeks to analyze."

### Tesla-Style Response

**Hour 0-2: Direct Observation**
- Go to production line, not conference room
- Observe 10 consecutive failures
- Document: When exactly does defect occur?

**Hour 2-4: Physics Analysis**

| Hypothesis | Test | Result |
|------------|------|--------|
| Cell variance | Measure 20 cells | All within spec |
| Adhesive cure | Thermal imaging | Cold spot in zone 3 |
| Pressure uniformity | Pressure film test | 40% variance across fixture |

**Root Cause:** Fixture pressure uneven due to worn locator pins.

**Fix:** Replace pins ($200), add wear indicator.

**Timeline:** 4 hours from problem to fix.

**Anti-bureaucracy win:** No meetings, no task force, no blame — physics decided.

---

## Scenario H: Hiring Decision — Evidence of Excellence

**Context:** Evaluating two candidates for senior engineer role.

### Candidate A (Traditional Background)
- 10 years at established automaker
- "Led cross-functional initiative to optimize infotainment system"
- "Improved user satisfaction scores 15%"

### Candidate B (Tesla-Style Profile)
- "Reduced battery management latency from 500ms to 10ms (50×)"
- "Owned end-to-end: prototype → validation → production"
- "Result: Enabled real-time Autopilot feedback, deployed to 1M vehicles"

### Tesla-Style Evaluation

| Criterion | Candidate A | Candidate B |
|-----------|-------------|-------------|
| Quantified impact | ❌ Vague | ✅ Specific metrics |
| Ownership | ❌ "Led initiative" | ✅ "Owned end-to-end" |
| First principles | ❌ Satisfaction scores | ✅ Latency reduction |
| Mission link | ❌ None stated | ✅ Autopilot enablement |
| Scale | ❌ Unknown | ✅ 1M vehicles |

**Decision:** Candidate B demonstrates Evidence of Excellence.

---

## Scenario I: Crisis Response — Production Stop

**Context:** 3 AM: Safety-critical firmware bug detected in fleet. 50K vehicles affected.

### Anti-Pattern Response
> "Schedule emergency meeting tomorrow morning with all stakeholders to discuss options."

### Tesla-Style Response

**T+0 minutes: Alert**
- Owner identified: Firmware team lead
- Severity: Safety-critical = immediate action

**T+15 minutes: Decision**
- Options:
  1. OTA rollback (2 hours, minimal impact)
  2. Feature disable (30 minutes, partial function)
  3. Full recall (days, brand damage)

- Decision: Option 2 immediately, Option 1 in parallel

**T+30 minutes: Execute**
- Feature disabled via OTA
- Customer notification sent
- Fix development begins

**T+4 hours: Resolve**
- Root cause identified
- Patch developed and tested
- Deployed to validation fleet

**T+24 hours: Complete**
- Patch deployed to production fleet
- Feature re-enabled
- Post-mortem scheduled

**Key:** Speed of iteration applies to crisis response. No meetings until after fix deployed.
