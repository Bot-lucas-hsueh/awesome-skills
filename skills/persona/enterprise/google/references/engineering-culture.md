# Google Engineering Culture

> How Google builds, ships, and scales — the cultural and operational principles

## The 10 Things Google Believes

Based on internal culture documentation, widely shared practices, and executive communications:

1. **Focus on the user and all else will follow** — Every decision traces to user benefit
2. **It's best to do one thing really, really well** — Depth over breadth in execution
3. **Fast is better than slow** — Speed is a feature; ship and iterate
4. **Democracy on the web works** — Open systems beat closed ones
5. **You don't need to be at your desk to need an answer** — Information access anywhere
6. **You can make money without doing evil** — Ethical business is sustainable business
7. **There's always more information out there** — Information is never complete
8. **The need for information crosses all borders** — Global by default
9. **You can be serious without a suit** — Formal dress is irrelevant to great work
10. **Great just isn't good enough** — Relentless pursuit of excellence

## SRE: Site Reliability Engineering

### Origins

Google's SRE team was founded by Ben Treynor Sloss in 2003, originally as a "half DevOps" experiment. The insight: **operations is a software problem**. Instead of hiring ops teams who react to incidents, hire engineers who build systems that don't fail — and when they do, automate recovery.

### Core Principles

**1. SLOs Define "Reliable"**
```
SLI (Service Level Indicator): What we measure
  → Example: "99.95% of search queries return results within 100ms"

SLO (Service Level Objective): What we promise
  → Example: "99.95% availability, P99 latency < 100ms"
  → The SLO is the target; exceeding it means you've over-invested

SLA (Service Level Agreement): What we promised the customer
  → Example: "99.9% uptime with 1× SLA credit per hour of downtime"
  → SLAs are typically looser than SLOs; you never want to exceed the SLA
```

**2. Error Budgets: The Innovation Driver**

Error budget = `100% - SLO`

```
If SLO = 99.95% → Error budget = 0.05%
If monthly error budget = 21.6 minutes
  → If you've used 0 minutes of error budget: aggressively ship features
  → If you've used 10 minutes: slow down, focus on reliability
  → If you've used 20 minutes: pause all launches until resolved
```

**The key insight:** Error budgets convert "reliability vs. velocity" from a tradeoff into a **measurable decision**. You're not choosing between shipping and reliability — you're choosing how to spend your error budget.

**3. Toil: The Enemy of Scale**

Toil = manual, repetitive, automatable work that scales linearly with service growth.

```
Good Toil Ratio Target: < 50% of on-call time
If service grows 10×:
  - High toil: 10× the manual work → team burns out
  - Low toil: automated responses → team scales with product
```

**SRE Golden Signals (what to measure):**
- **Latency**: Is the system slowing down?
- **Traffic**: Are requests growing unexpectedly?
- **Errors**: Are requests failing?
- **Saturation**: Is the system at capacity?

**4. Blameless Postmortem**

The foundational SRE principle: **when incidents happen, fix the system, not the person**.

```
Postmortem Timeline:
  T+0: Incident detected
  T+15min: Severity assessed (SEV1/SEV2/SEV3)
  T+30min: Incident commander assigned
  T+48hrs: Postmortem draft complete
  T+1week: Postmortem published, action items assigned

Postmortem Structure:
  1. Summary (what happened, impact, duration)
  2. Timeline (minute-by-minute what happened)
  3. Root cause (the contributing factors)
  4. Resolution (what fixed it)
  5. Lessons learned (what we learned)
  6. Action items (who fixes what by when)

The blameless rule: The postmortem does NOT ask:
  - Who made the mistake?
  - Whose fault was it?
  - Who should be punished?

The postmortem DOES ask:
  - What allowed the mistake to happen?
  - What system changes would prevent recurrence?
  - How do we improve our detection and response?
```

## The Technical Ladder

### Individual Contributor Track (L1-L10)

| Level | Title | Expectation | Example Impact |
|-------|-------|-------------|---------------|
| **L3** | Junior SWE | Ships features; learns rapidly | Feature shipped to 10K users |
| **L4** | SWE | Owns features end-to-end; mentors L3 | Feature shipped to 1M users |
| **L5** | Senior SWE | Leads projects; designs systems | System serving 10M users |
| **L6** | Staff SWE | Leads across teams; technical strategy | Platform used by 100+ engineers |
| **L7** | Senior Staff SWE | Org-wide technical impact | Architecture adopted company-wide |
| **L8** | Principal SWE | Industry-level impact | Technology that defines a category |
| **L9** | Distinguished Engineer | Google-wide technical vision | Sets direction for 1000+ engineers |
| **L10** | Google Fellow / Senior Fellow | Company-wide impact | Fundamental contribution to Google's identity |

### Manager Track

| Level | Title | Expectation |
|-------|-------|-------------|
| **L5 M** | Engineering Manager | Manages 5-10 engineers; delivers team OKRs |
| **L6 M** | Senior EM | Manages managers or large team; drives org strategy |
| **L7 M** | Director of Engineering | Multi-team/org impact; strategy execution |
| **L8 M** | VP of Engineering | Function or large org leadership |

### Dual Ladder Philosophy

Google explicitly supports **dual ladders** — the manager track is not "above" the IC track. A Principal Engineer (L8 IC) is peers with a Director (L7 M). Compensation and prestige are comparable. Engineers choose based on what they're best at and what they enjoy.

**The key distinction:** IC track maximizes **technical depth and scope**. Manager track maximizes **organizational scope and people development**. Both require leadership, just different kinds.

## Decision-Making Framework

### Reversible vs. Irreversible Decisions

**Reversible (can be undone quickly):** Make them fast
- UI copy changes
- Feature flags
- Non-critical feature launches
- Internal tool choices

**Irreversible (hard or impossible to undo):** Make them slowly
- Public API changes
- Data schema changes
- Security architecture
- Customer contract terms

**The rule:** For reversible decisions, "done is better than perfect." For irreversible decisions, invest in getting them right.

### The 10× Test for Architecture

When evaluating technical approaches:
- Does this approach improve something by 10×, not 10%?
- If the current approach is "good enough," why change it?
- What's the cost of being wrong?

```
Example: Should we migrate from MySQL to Spanner?

Bad reasoning: "Spanner is the new thing; we should use it"
Good reasoning: 
  - Current MySQL setup handles 10K QPS; target is 100K QPS
  - Sharding MySQL: 6 months, 3 engineers, complex ops
  - Spanner: 3 months, 1 engineer, managed service
  - Decision: 10× capacity need → Spanner justified
```

### Tech Debt Framework

**Not all tech debt is bad.** Some debt is a conscious trade-off for speed. The question is: **is the debt slowing you down?**

```
Debt Assessment Matrix:

Severity: High (blocks major features)
  + Fix effort: Low  → Fix immediately
  + Fix effort: High → Allocate dedicated sprint

Severity: Medium (slows development)
  + Fix effort: Low  → Fix in next sprint
  + Fix effort: High → Allocate 20% of sprint

Severity: Low (minor inconvenience)
  + Fix effort: Low  → Fix when touching this area
  + Fix effort: High → Accept; address if it becomes high severity
```

**The OKR Connection:** Tech debt that blocks OKRs gets a KR. Tech debt that doesn't impact measurable goals is a "when convenient" activity.

## Performance Calibration

### The Process (Annual Cycle)

```
Timeline:
  Q4 (Nov): Goal setting for next year
  Ongoing:  Regular check-ins (monthly/quarterly)
  H1 (Jun): Mid-year review
  H2 (Nov): Year-end calibration + compensation

Steps:
  1. Self-assessment: "What did I achieve? What impact did I have?"
  2. Peer feedback: 3-5 peers provide structured feedback
  3. Manager review: Manager assesses against level expectations
  4. Calibration: Managers meet to align on ratings across teams
  5. Calibration review: Directors/VPs calibrate across org
  6. Delivery: Employee receives rating and compensation update
```

### Evidence of Excellence

Google evaluates performance based on **evidence**, not impressions:

| Dimension | Weak Evidence | Strong Evidence |
|-----------|--------------|-----------------|
| **Impact** | "I worked hard" | "Reduced latency 40%; team shipped 3 features; mentored 2 L3s" |
| **Scope** | "I helped with X" | "Led cross-team initiative with 20 stakeholders" |
| **Technical** | "I'm good at coding" | "Designed system serving 50M users; 3 teams adopted architecture" |
| **Leadership** | "I'm a team player" | "Resolved conflict between team A and B; led postmortem that changed team process" |

### The Calibration Curve

Google uses **forced distributions** at some levels to ensure consistency. The typical target:
- **Top tier (exceptional)**: 5-10%
- **Strong tier (meets and exceeds)**: 60-70%
- **Developing tier (needs improvement)**: 15-25%
- **Does Not Meet bar**: 0-5%

**Important:** The distribution is a guide, not a quota. Teams with genuinely exceptional performers get more top ratings. Teams with performance issues document them honestly.

## Key Engineering Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Deployment Frequency** | Multiple per day | DORA metrics |
| **Lead Time for Changes** | < 1 day | Commit to production time |
| **Change Failure Rate** | < 5% | % of deployments causing P1/P2 |
| **MTTR (Mean Time to Recovery)** | < 1 hour | Incident start → resolution |
| **Toil Ratio** | < 50% of on-call time | Manual work / total time |
| **Code Review Turnaround** | < 24 hours | CL submitted → approved |
| **Test Coverage** | > 80% | Lines covered by unit tests |
| **On-call pages per day** | Declining trend | P1/P2 alerts per shift |

## Code Review Culture

Google's code review is a **knowledge transfer and quality gate**, not a bureaucratic checkpoint.

**Key Principles:**
- Every CL (change list) requires **at least one reviewer approval**
- Reviewers respond within **24 hours** (SLA, not expectation)
- **Nits** (style issues, minor suggestions) are clearly marked as non-blocking
- **Blocking comments** must be addressed before merge
- **LGTM** (Looks Good To Me) = approved for merge

**What reviewers check:**
- Correctness: Does it do what it says?
- Design: Is it the right approach for the system?
- Readability: Can future engineers understand it?
- Testing: Are there adequate tests?
- Security: Are there vulnerabilities?
- Performance: Are there O(n²) or memory issues?

**What reviewers don't do:**
- Rewrite the code (that's the author's responsibility)
- Block on style (that's what linters are for)
- Gatekeep (if it's correct and tested, approve)

## The Monorepo: google3

Google's monolithic repository containing virtually all of Google's code:

| Stat | Value |
|------|-------|
| Files | 2B+ |
| Lines of code | 2B+ |
| Data size | 86TB+ |
| Commits/day | 86,000+ |
| Engineers | 50,000+ |

**Key implications:**
- **Atomic changes** across the entire codebase
- **OWNERS files** define who can approve changes to specific directories
- **Bazel** build system enables incremental builds at scale
- ** Tricorder** static analysis catches common bugs before review
- **Readability** certification required for each language

**Tradeoffs:**
- Pros: Atomic cross-project changes, easy code sharing, simple dependency management
- Cons: Huge build infrastructure, tooling complexity, potential for tight coupling

## References

- [Site Reliability Engineering — Betsy Beyer et al.](https://sre.google/sre-book/)
- [The Site Reliability Workbook](https://sre.google/workbook/)
- [Software Engineering at Google](https://www.amazon.com/Software-Engineering-Google-Lessons-Production/dp/1492082791)
- [re:Work — Google's practices](https://rework.withgoogle.com/)
- [SRE Classroom](https://sre.google/classroom/)
