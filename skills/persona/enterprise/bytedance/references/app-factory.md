# APP Factory — Product Lifecycle Management

> ByteDance's factory-like approach to product development: ship fast, evaluate rigorously, kill losers early, double down on winners

---

## Overview

The APP Factory model is ByteDance's approach to product development, treating products as experiments with clear lifecycle stages, defined metrics, and explicit kill criteria. This approach enables rapid iteration across many products while maintaining focus on winners.

---

## The Philosophy

### Core Tenets

1. **Every product is an experiment**
   - Hypothesis → MVP → Data → Decision
   - No product is "too important to kill"
   - Winners get massive investment; losers get terminated

2. **Speed over perfection**
   - Ship MVP in 2-4 weeks
   - Evaluate at 8-12 weeks
   - Iterate or kill, don't linger

3. **Clear kill criteria**
   - Metrics defined upfront
   - Pass/fail thresholds established
   - No emotional attachment

4. **Resource mobility**
   - Engineers move between products
   - Failed products lose resources
   - Winners attract talent

---

## Product Lifecycle

### Stage 1: HYPOTHESIS (1-2 weeks)

**Purpose:** Validate that the problem is worth solving

**Activities:**
- User research and pain identification
- Market analysis
- Initial metric definition
- Team formation (3-5 people)

**Deliverables:**
- Problem statement with data backing
- Initial metric hypothesis
- MVP scope definition

**Kill Criteria:**
- No clear user pain identified
- Market too small (<$100M opportunity)
- Can't build MVP in 2 weeks

**Exit Gate:**
```
□ Problem validated with data?
□ Can we build MVP in 2 weeks?
□ Clear success metric defined?
□ Team aligned on scope?
→ Proceed to MVP
```

---

### Stage 2: MVP (2-4 weeks)

**Purpose:** Ship the smallest thing to test the hypothesis

**Activities:**
- Core feature development
- Basic analytics instrumentation
- Alpha testing (internal users)
- Beta testing (100-1000 external users)

**Deliverables:**
- Working product (core flow only)
- Metric tracking dashboard
- Initial user feedback

**Kill Criteria:**
- Core flow doesn't work reliably
- Users don't return after Day 1
- Metric trajectory negative

**Exit Gate:**
```
□ Core flow working (no P0 bugs)?
□ Users can complete core task?
□ Day 1 retention > 30%?
□ Can measure success metric?
→ Proceed to Growth
```

---

### Stage 3: GROWTH (8-12 weeks)

**Purpose:** Scale if metrics are positive; establish kill/focus decision

**Activities:**
- Feature iteration based on data
- AB testing at scale
- User acquisition campaigns
- Team expansion (5-15 people)

**Deliverables:**
- Refined product with data-driven improvements
- Growth metrics report
- Kill/Focus/Scale recommendation

**Kill Criteria:**
| Metric | Target | Current | Signal |
|--------|--------|---------|--------|
| DAU/WAU ratio | >0.35 | <0.25 | ❌ Kill candidate |
| Week 1 retention | >30% | <20% | ❌ Kill candidate |
| Week 4 retention | >15% | <8% | ❌ Kill candidate |
| Engagement trend | Growing | Declining | ⚠️ Pivot needed |

**Decision Framework:**
```
KILL: Metrics below threshold, no clear improvement path
PIVOT: Some metrics positive, iterate on weak areas
FOCUS: Mixed metrics, double down on strength
SCALE: All metrics positive, maximize investment
```

---

### Stage 4: DECISION

#### Kill Path

**When:** Metrics fail to meet thresholds after growth phase

**Process:**
1. Document kill rationale (1 day)
2. Communicate to stakeholders (1 day)
3. Transition team members to other products (1 week)
4. Archive codebase and assets (1 week)
5. Conduct blameless retro (1 day)

**What NOT to do:**
- Extend timeline "just in case"
- Shift kill metrics lower
- Assign more resources hoping for miracle

#### Scale Path

**When:** Metrics meet or exceed thresholds

**Process:**
1. Confirm scale decision with leadership (1 day)
2. Expand team (10→50+ engineers) (2 weeks)
3. Dedicated product manager, designer, ops (2 weeks)
4. Multi-year roadmap development (1 month)
5. Massive investment in growth

**Scale Characteristics:**
- Dedicated org structure
- Own infrastructure
- Independent roadmap
- Target: #1 in category

---

## Kill Metrics

### What Makes a Good Kill Metric?

**Characteristics:**
- Simple: One number to track
- Predictive: Correlates with long-term success
- Actionable: Team can influence it
- Early indicator: Signals within 2-4 weeks

**Examples by Product:**

| Product | Kill Metric | Threshold |
|---------|-------------|-----------|
| Social app | DAU/WAU ratio | >0.35 (monthly) |
| E-commerce | CVR (click to purchase) | >2% |
| Content app | Watch time per session | >15 min |
| Productivity | Weekly active users | >50% growth |
| Gaming | Day 7 retention | >25% |

### Kill Metric Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Vanity metrics | "Total installs" | Use engagement |
| Lagging indicators | "Revenue" | Use leading indicators |
| Too many metrics | "Track everything" | Pick 1-2 primary |
| Gameable metrics | "Clicks" | Balance with quality |

---

## Resource Allocation

### Allocation Framework

**Hypothesis/MVP Stage:**
- Small teams (3-5 people)
- Shared infrastructure
- Limited budget
- Maximum speed

**Growth Stage:**
- Medium teams (5-15 people)
- Dedicated resources
- Experiment budget
- Data-driven expansion

**Scale Stage:**
- Large teams (50-500+ people)
- Dedicated everything
- Growth budget
- Full investment

### Reallocation Triggers

| Signal | Action |
|--------|--------|
| Product killed | Reallocate to winners |
| Growth stalled | Reduce, test pivot |
| Momentum strong | Increase investment |
| Team burnout | Redistribute, rest |

---

## Case Studies

### Case 1: CapCut Mobile

**Timeline:**
- 2020: Hypothesis (3 people, 2 weeks)
- 2020: MVP (5 people, 4 weeks)
- 2020-2021: Growth (15 people, 12 weeks)
- 2021: Scale decision

**Kill Metrics at Growth:**
```
DAU/WAU: 0.28 ❌ (target 0.35)
Day 7 retention: 22% ❌ (target 30%)
Session length: 18 min ✅ (target 15 min)
```

**Decision:** Pivot, not kill

**Pivot Actions:**
- Simplified onboarding (3 steps vs. 8)
- Template-first experience
- Export optimization

**Result:**
```
DAU/WAU: 0.32 ✅
Day 7 retention: 28% ✅
→ Continued investment
```

**Today:** 500M+ users, #1 mobile video editor

---

### Case 2: Lemon8

**Timeline:**
- 2020: First launch (killed)
- 2021: Second launch (killed)
- 2022: Rebrand as lifestyle platform (growth)
- 2023: Scale decision

**Kill History:**
| Attempt | Kill Metric | Result |
|---------|-------------|--------|
| 2020 | DAU/WAU 0.15 | Killed |
| 2021 | DAU/WAU 0.18 | Killed |
| 2022 | DAU/WAU 0.31 | Scale |

**Learning:** Iteration beats giving up

---

### Case 3: Lark (Feishu)

**Timeline:**
- 2016: Development started
- 2018: Beta launch
- 2019: Growth phase
- 2020: COVID boost
- 2021: Scale decision

**Kill Metric Progression:**
```
2018: DAU/WAU 0.22 ❌
2019: DAU/WAU 0.28 ❌
2020: DAU/WAU 0.35 ✅ (COVID remote work)
```

**Key Insight:** External events can accelerate products

---

## Decision Framework: Kill or Scale

```
1. METRIC REVIEW
   - Primary kill metric: Above/below threshold?
   - Trend: Improving or declining?
   - Leading indicators: Positive signals?

2. EFFORT ASSESSMENT
   - What's the minimum change needed?
   - Can we pivot without killing?

3. RESOURCE CALCULATION
   - Current team size
   - Opportunity cost of continuing
   - Resource needs for pivot vs. kill

4. DECISION
   KILL: Metrics failed, no clear pivot path
   PIVOT: Metrics weak, clear improvement hypothesis
   FOCUS: Metrics mixed, narrow scope
   SCALE: Metrics strong, maximize investment

5. EXECUTION
   - Document rationale
   - Communicate timeline
   - Execute transition
   - Learn and share
```

---

## Metrics for APP Factory

| Metric | Target | Measurement |
|--------|--------|-------------|
| MVP cycle time | <4 weeks | Launch to MVP |
| Time to kill | <1 week | Decision to archive |
| Kill ratio | 60-70% | Products killed / total launched |
| Scale ratio | 10-20% | Products scaled / total launched |
| Iteration speed | <2 weeks | Between iterations |

---

## References

- ByteStyle → ./bytestyle.md
- Context Not Control → ./context-not-control.md
- Data-Driven → ./data-driven.md

---

## Further Reading

- "The Lean Startup" by Eric Ries
- "Zero to One" by Peter Thiel
- "The Hard Thing About Hard Things" by Ben Horowitz
