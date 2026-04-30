# OKR Methodology at Google

> Objectives and Key Results — from Intel to Google to the world

## History: From Intel to Google

**The Origin:**
Andy Grove developed OKRs at Intel in the 1980s. Grove's insight: traditional management was too top-down and rigid. OKRs provided a framework for **ambitious goal-setting with measurable accountability**, without becoming a bureaucratic exercise.

**The Introduction to Google:**
John Doerr joined Intel in 1974 and later introduced OKRs to Google in 1999, shortly after Larry Page and Sergey Brin founded the company. At the time, Google had about 20 employees and was struggling to find focus. Doerr's pitch was simple: **write down what you want to achieve, then measure whether you did**.

**The Impact:**
Google's OKR system is widely credited as a key factor in the company's ability to scale from a startup to a global technology leader. The quarterly cadence allowed rapid iteration while maintaining alignment across thousands of employees.

## The Framework

### Anatomy of an OKR

**Objective (O):** A qualitative, inspirational, time-bound goal that answers: "Where do we want to go?"

- Written in plain language — a human should understand it without explanation
- Ambitious and motivating — inspires the team to stretch
- Time-bound — achieved within a quarter (or year)
- Not measured directly — the KRs do the measuring

**Key Results (KRs):** Quantitative metrics that answer: "How will we know if we got there?"

- Specific and measurable — "increase X from Y to Z by date"
- Outcome-based — not activities ("shipped feature X") but impact ("reduced latency by 30%")
- Challenging but achievable — target 0.7, not 1.0
- 2-5 KRs per objective — more than 5 dilutes focus

### Example OKR Structure

```yaml
Objective: Make Google Search the world's most helpful assistant

Key Results:
  KR1: Reduce median search latency from 180ms to 140ms by EOQ
       (Baseline: 180ms | Target: 140ms | Current: 145ms)
  KR2: Increase AI Overview coverage for "how-to" queries from 40% to 65% by EOQ
       (Baseline: 40% | Target: 65% | Current: 52%)
  KR3: Launch 3 new AI features to 100M+ users by EOQ
       (Baseline: 0 features | Target: 3 | Current: 2 shipped)
  KR4: Maintain 99.99% core infrastructure uptime
       (Baseline: 99.97% | Target: 99.99% | Current: 99.98%)
```

## The Grading Scale

### The 0.0-1.0 Scoring System

| Score | Meaning | Interpretation | Action |
|-------|---------|----------------|--------|
| **1.0** | Perfect achievement | Target was too easy; insufficient ambition | Raise next quarter's target |
| **0.8-0.9** | Excellent, stretch achieved | "Exceptional performance" | Celebrate, but check if ambition was right |
| **0.7-0.8** | Good, target met | "On track" — this is the typical target | Proceed; consider if more was possible |
| **0.6-0.7** | Acceptable | Some progress; not fully ambitious | Review; may indicate unclear scope or blockers |
| **0.4-0.6** | Missed, but learned | "Partially achieved" | Analyze why; understand if target was realistic |
| **0.0-0.4** | Failed | Significant gap between target and outcome | Root cause analysis; adjust approach |

### The Target: 0.7

The **Google OKR sweet spot is 0.7**. This means:
- The target was **stretch** (not easy)
- The team **made significant progress** (not trivial)
- There was **room to grow** (not sandbagged)

**A score of 1.0 is NOT celebrated** — it suggests the target wasn't ambitious enough. Google famously sets targets at "70% confidence" — meaning the team thinks there's a 70% chance of achieving it, not 100%.

### Common Misconceptions

| ❌ Misconception | ✅ Reality |
|-----------------|-----------|
| "1.0 = A grade = exceptional" | 1.0 = target was too easy = need to raise ambition |
| "Score below 0.7 = failure" | 0.5-0.7 = learning happened = valuable information |
| "OKRs = performance review" | OKRs measure outcomes; performance reviews assess behaviors + impact |
| "Everyone should hit 0.7" | Teams that consistently hit 1.0 are sandbagging |
| "KRs = tasks" | KRs = measurable outcomes; tasks are how you achieve them |

## OKR Cascading

### The Alignment Hierarchy

```
Company OKRs (CEO, Leadership — Annually + Quarterly)
    ↓
Product Area OKRs (VP — Quarterly)
    ↓
Team OKRs (Director/Manager — Quarterly)
    ↓
Individual OKRs (IC — Quarterly, optional)
```

**Key Principles:**
- Objectives cascade down; KRs don't need to
- Each level's OKR should ladder to the level above
- Cross-functional dependencies should be explicit
- Individuals can have personal OKRs but they're not required

### The Dependency Map

```yaml
# Company OKR (Q3)
O: Accelerate AI-first product transformation
KR1: 1B users engaging with AI features (from 500M)
KR2: Gemini adoption: 50M → 100M subscribers
KR3: AI infrastructure: 30% cost reduction per query

# Search OKRs (Q3)
O: Make Search the smartest AI assistant
KR1: AI Overview coverage: 60% → 80% of queries
KR2: Search latency: 150ms → 130ms (AI overhead budget)
KR3: User satisfaction: 4.2 → 4.5 (survey-based)
```

## The Quarterly Cycle

### Week 1: Set & Align

| Day | Activity | Output |
|-----|----------|--------|
| Monday | Read company/org OKRs | Understanding of top-level priorities |
| Tuesday-Wednesday | Draft team OKRs | First cut at objectives and KRs |
| Thursday | Cross-functional alignment | Dependencies identified |
| Friday | Manager calibration | OKRs reviewed and finalized |

**Alignment Meeting Template:**
```
Team: [Name]
Quarter: Q[X] 20XX
Owner: [Name]

OKR 1: [Objective]
  KR1: [Metric] from [X] to [Y] by [Date]
  KR2: [Metric] from [X] to [Y] by [Date]

OKR 2: [Objective]
  KR1: [Deliverable] by [Date]

Dependencies:
  - [Team/Person]: [What we need from them]
  - [Team/Person]: [What they need from us]

Risks:
  - [Risk 1]: [Mitigation]
```

### Week 6: Mid-Quarter Check-In

| Activity | Purpose |
|----------|---------|
| Review KR progress | Are we on track? What's moving? |
| Identify blockers | What's preventing progress? |
| Rebaseline if needed | Scope changed? Document why |
| Reallocate if needed | Priorities shift? Adjust explicitly |

**Rebaseline Rules:**
- Rebaselining is **acceptable** when scope genuinely changes
- Must document **why** the original target was no longer valid
- Repeated rebaselining signals poor planning, not agility
- Never rebaseline upward to make a miss look like a hit

### Week 10: Score & Retro

| Activity | Purpose |
|----------|---------|
| Self-score all KRs | Honest assessment: what did we actually achieve? |
| Manager calibration | Align on scores; discuss variance |
| Retro on OKR process | What worked? What should change? |
| Draft next quarter's OKRs | Start early; don't wait until Q-start |

**End-of-Quarter Reflection:**
```yaml
# Q3 Retrospective

What went well:
  - [What we did right]
  - [What we should keep doing]

What didn't go well:
  - [What we missed]
  - [What we'd do differently]

OKR Process Feedback:
  - [What worked about the OKR process]
  - [What we'd change]

Key Learnings:
  - [Insight 1]
  - [Insight 2]
```

## OKRs vs. Other Frameworks

| Dimension | OKRs | KPIs | Project Plans |
|-----------|------|------|---------------|
| **Focus** | Outcomes (impact) | Metrics (health) | Outputs (deliverables) |
| **Timeframe** | Quarterly | Ongoing | Project-based |
| **Ambition** | Stretch goals | Achievable targets | Scope-bound |
| **Connection** | Cascading alignment | Standalone health | Milestone-driven |
| **Scoring** | 0.0-1.0 | Traffic light (red/yellow/green) | % complete |
| **Revision** | Quarterly | Ongoing | As needed |

**KPIs vs. KRs:**
- A **KPI** is a metric you track to understand health (e.g., uptime, latency, retention)
- A **KR** is a metric you commit to moving in a quarter
- Not every KPI needs to be a KR; not every KR needs to be a KPI
- **Good KR:** "Reduce P99 latency from 200ms to 150ms" (outcome you commit to)
- **Bad KR:** "Monitor latency metrics" (activity, not outcome)

## Common Mistakes

### Mistake 1: Activities as KRs
```yaml
❌ Bad: "Conduct 20 user interviews by EOQ"
✅ Good: "Reduce user-reported confusion by 25% by EOQ (baseline: 40 reports/week)"
```

### Mistake 2: Too Many KRs
```yaml
❌ Bad: 8 KRs per objective
✅ Good: 2-4 KRs per objective
```
More than 4 KRs = diluted focus. If you have more, either merge related ones or accept that some won't get attention.

### Mistake 3: Sandbagging
```yaml
❌ Bad: "Achieve 80% of a 0.4 target" → scores 0.32 → "we hit our goal"
✅ Good: Target 0.7, achieve 0.65 → honest score → "we made strong progress, here's what we learned"
```

### Mistake 4: Disconnected from Company Priorities
```yaml
❌ Bad: Team OKRs that don't mention company OKRs
✅ Good: Every team OKR explicitly maps to a company/org OKR
```

### Mistake 5: OKRs as Performance Reviews
OKRs measure **what** was achieved, not **how**. A team that scores 0.8 because they made a strategic bet that didn't pan out may deserve more recognition than a team that scored 1.0 on easy targets.

**Keep OKRs and performance reviews separate.** Use OKRs for alignment and learning. Use performance reviews for compensation and growth discussions.

## Tooling

Google uses internal tools for OKR tracking, but the principles are tool-agnostic:

| Tool | Google Internal | External Equivalent |
|------|-----------------|--------------------|
| OKR Tracking | gOKR (internal) | Notion, Lattice, Asana, Awork |
| Goals Framework | Goals in gTeams | Perdoo, 15Five, Culture Amp |
| Performance | Perfcal | Lattice, Greenhouse, Lever |
| Dashboards | Looker | Tableau, Metabase, Hex |

## References

- [Measure What Matters — John Doerr](https://www.amazon.com/Measure-What-Matters-Happen-Results/dp/0525536221)
- [re:Work — OKR guide](https://rework.withgoogle.com/guides/goals-strategy-reviews/)
- [Andy Grove's High Output Management](https://www.amazon.com/High-Output-Management/dp/0679762884)
