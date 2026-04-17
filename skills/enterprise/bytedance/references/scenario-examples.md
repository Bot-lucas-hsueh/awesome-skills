## §5. Scenario Examples

### Example 1: TikTok Feed Ranking — Algorithm Iteration

**Context:** Feed engagement declining 3% week-over-week for 18-24 demographic.

**User:** "How do we diagnose and fix this?"

**ByteDance Engineer Response:**

> **1. Granularity Drill (1 day):**
> ```
> Overall: -3% engagement
> → Age: 18-24: -8% ❌ | 25-34: -1% | 35+: +1%
> → Geography: US: -12% ❌ | UK: -3% | Brazil: +2%
> → Content type: Short form: -5% | Long form: -2%
> → Creator tier: New (<10K): -15% ❌ | Mid: -3% | Top: +1%
> Signal: New creator visibility algorithm underperforming for US 18-24
> ```
>
> **2. Root Cause Hypothesis:**
> Recent change to "discoverability boost" for new creators may be backfiring for US 18-24 users who prefer established creators.
>
> **3. AB Test Design (3 days):**
> - Control: Current algorithm
> - Treatment: Segment-specific creator quality weighting
> - Target: Engagement +5% for US 18-24, no regression for others
> - Sample: 10M per arm
>
> **4. Result After 2 weeks:**
> ```
> Metric        | Control | Treatment | Δ      | p-value |
> US 18-24 Eng  | 100     | 107       | +7%    | 0.001   ✅
> Overall Eng   | 100     | 101       | +1%    | 0.12    ✅
> Creator count | 100     | 103       | +3%    | 0.03    ✅
> ```
> **Decision: Ship 100%.** Algorithm updated, monitoring for 30 days.

---

### Example 2: APP Factory — CapCut Mobile Launch Decision

**Context:** CapCut mobile app in "growth" stage at week 12. Kill metric: DAU/WAU ratio.

**User:** "What do we do with CapCut?"

**ByteDance Engineer Response:**

> **1. Kill Metric Analysis:**
> ```
> Target: DAU/WAU > 0.35 (monthly)
> Current: 0.28 ❌ (declining 4 weeks)
> Projected: 0.22 in 4 weeks if trend continues
> ```
>
> **2. Deep Dive:**
> ```
> Retention curve:
> Day 1: 45% (target: 50%)
> Day 7: 22% (target: 30%)
> Day 30: 8% (target: 15%)
> Signal: Users try once, don't return
> ```
>
> **3. Hypothesis:**
> App too complex for casual users. Need simpler "first video" experience.
>
> **4. Decision Tree:**
> ```
> Option A: Kill app            → Lose 500M users, $100M investment
> Option B: Pivot to template    → Simpler UX, 6-week experiment
> Option C: Double down          → Double eng, risk more investment
> ```
>
> **5. Decision: Option B — Pivot.** Ship "CapCut Lite" in 6 weeks. Simpler interface, 3-step video creation. 30-day kill metric review. If DAU/WAU improves to 0.32+, continue; else kill.
>
> **6. Outcome:** CapCut Lite launched → Day 7 retention improved to 28%. CapCut survived with focused positioning.

---

### Example 3: Context Not Control — Lark Meeting Scheduler Conflict

**Context:** Lark team has conflicting priorities: enterprise features vs. SMB features.

**User:** "How do we decide with Context Not Control?"

**ByteDance Engineer Response:**

> **1. Context Provision (not Control):**
> Present data, not directives:
> ```
> Market data:
> - Enterprise: $500M ARR potential, 10% market share
> - SMB: $100M ARR potential, 40% market share
> - Our position: Enterprise 15% share, SMB 5% share
> 
> Team capability:
> - Team A (Enterprise): 30 engineers, 12-month runway
> - Team B (SMB): 10 engineers, 6-month runway
> 
> Company OKR:
> - Q1: +$50M ARR
> - H1: 2x enterprise logo retention
> ```
>
> **2. Let Teams Decide (after shared context):**
> Bring both teams together with same data.
> Ask: "Given this context, what's your recommendation?"
>
> **3. Consensus Output:**
> Team A recommends: Focus enterprise, partner with SMB.
> Team B recommends: Focus SMB, use Team A partnership.
>
> **4. Mediator Role (not Decider):**
> Highlight: Enterprise OKR is non-negotiable. SMB is growth opportunity.
>
> **5. Final Decision (by consensus):**
> - Q1-Q2: 80% Team A on Enterprise OKR
> - Q3: Reassess, 30% Team B on SMB pilot
> - Shared context enabled autonomous decision.
>
> **Key: Leaders provided context, teams made the call.**

---

### Example 4: Data Granularity — Douyin E-commerce Conversion

**Context:** Douyin e-commerce conversion rate declining. Total: 2.1% → 1.9%.

**User:** "Where is the problem?"

**ByteDance Engineer Response:**

> **1. Funnel Granularity Drill:**
> ```
> Overall CVR: 2.1% → 1.9% (-9.5%)
> 
> Step 1: Impressions → Click
>   18% → 17.5% (-2.8%)
>   
> Step 2: Click → Add to Cart
>   12% → 10% (-16.7%) ❌ Primary issue
>   
> Step 3: Add to Cart → Purchase
>   85% → 84% (-1.2%)
> ```
>
> **2. Add-to-Cart Granularity:**
> ```
> By price range:
> - $0-20: 15% → 14% (-7%)
> - $20-50: 12% → 8% (-33%) ❌ Major drop
> - $50-100: 10% → 9% (-10%)
> - $100+: 8% → 7.5% (-6%)
> 
> By category:
> - Fashion: 11% → 7% (-36%) ❌
> - Electronics: 13% → 12% (-8%)
> - Food: 18% → 17% (-6%)
> 
> Signal: Fashion $20-50 price point broken
> ```
>
> **3. Root Cause:**
> Douyin recently increased payment friction for fashion items in $20-50 range (new fraud prevention). Legitimate users abandoning.
>
> **4. AB Test:**
> - Control: Current fraud prevention
> - Treatment: ML-based fraud scoring, reduced friction for low-risk users
>
> **5. Result:** Fashion CVR recovered to 10.5%. Overall CVR: 2.0%.
>
> **Key: Drill until you see the signal. Never trust aggregate data alone.**

---

### Example 5: CICD Speed — TikTok Video Upload Pipeline

**Context:** Video upload success rate dropping 2% during peak hours (8-10pm China time).

**User:** "How do we diagnose and fix at speed?"

**ByteDance Engineer Response:**

> **1. Immediate Triage (15 minutes):**
> ```
> Metric: Upload success rate
> Baseline: 99.5%
> Current: 97.5% ❌
> Impact: ~1M failed uploads/hour = ~10K users affected
> ```
>
> **2. Correlation Hunt (30 minutes):**
> ```
> - Upload volume: +40% (peak)
> - Processing time: 3min → 8min (2.7x)
> - Queue depth: 10K → 150K
> - Error type: 408 (timeout) increasing
> Signal: Processing pipeline bottleneck
> ```
>
> **3. Fast Rollback Assessment:**
> Was there a change in last 24 hours?
> Yes: New video processing codec deployed 4 hours ago.
>
> **4. Decision: Fast Rollback (within 30 min target):**
> ```
> Rollback process:
> - Feature flag: Disable new codec
> - Target: 10% traffic → Success rate: 99.4% ✅
> - Full rollback → Success rate: 99.5% ✅
> - Total time: 25 minutes
> ```
>
> **5. Post-Incident (Context Not Control):**
> Root cause: New codec not load tested at 2x peak.
> Fix: Mandatory load test 2x peak before codec rollout.
> Tech debt KR added to OKR.
>
> **Key: Speed to rollback > Speed to fix. CICD enables fast recovery.**

---
