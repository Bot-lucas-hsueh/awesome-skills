## § 7 · Standards & Reference

### RICE Prioritization Framework

```
RICE Score = (Reach × Impact × Confidence)

Reach: How many users affected per time period?
  (users/quarter, not unique users — consider repeat usage)

Impact: How much does this move the north star metric?
  3 = Massive (>5% change), 2 = High (1-5%), 1 = Medium (0.5-1%), 0.5 = Low (<0.5%), 0.25 = Minimal

Confidence: How confident are we in our estimates?
  100% = Strong research evidence
  80% = Some evidence (interviews + analytics)
  50% = Assumption-based
  20% = Pure guess

Effort: Person-weeks to ship
  (sum across all team members: eng + design + PM)

Higher RICE = higher priority
```

### PRD Template

```
# PRD: [Feature Name]
**PM:** [Name] | **Status:** Draft / In Review

## Problem Statement
When [user context/situation], [user type] wants to [motivation/job],
so they can [desired outcome]. Currently, [how they solve it today and why it's insufficient].

## Success Metrics
Primary: [Metric + target + timeframe, e.g., "↑ activation rate 15→20% in 90 days"]
Secondary: [Supporting metrics]
Guardrails: [Metrics that must NOT regress: e.g., "P95 latency stays <200ms"]

## Non-Goals (explicitly out of scope)
- [What we are NOT building in this iteration]
- [Adjacent problem we are not solving yet]

## User Stories
As a [persona], I want to [action] so that [benefit].
  Acceptance Criteria:
  - GIVEN [context] WHEN [action] THEN [observable outcome]
  - ...

## UX/Design Requirements
[Link to Figma] | Key flows: [describe critical paths]

## Technical Constraints
- [Dependencies, APIs, performance requirements]
- [Known technical risks]

## Launch Plan
Alpha: [date, audience] | Beta: [date, audience] | GA: [date, criteria]
GTM: [sales training, docs, marketing coordination]
```

### North Star Metric Framework

```
Properties of a good North Star Metric:
✓ Measures value delivered to users (not just business value)
✓ Leading indicator for long-term retention
✓ Understandable by the whole team
✓ Actionable — team can move it through product work
✗ Not a revenue metric (lagging indicator)
✗ Not a vanity metric (DAU with no quality signal)

Examples:
- Slack: "Messages sent between teams" (collaboration value)
- Airbnb: "Nights booked" (transaction value, both sides)
- Spotify: "Time spent listening" (content consumption)
- Notion: "Blocks created" (collaboration + content depth)
```

---
