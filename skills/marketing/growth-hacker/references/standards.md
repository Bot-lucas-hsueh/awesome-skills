## § 6 · Standards & Reference

### Growth Model Template

```
GROWTH MODEL — [Product/Company]

NORTH STAR METRIC:
[Metric that captures core value delivery]

GROWTH LOOPS:

Loop 1: [Name]
[Diagram of loop with conversion rates]
- Input: [Metric]
- Step 1: [Action] ([X%] conversion)
- Step 2: [Action] ([Y%] conversion)
- Output: [Metric]
- Reinvestment: [How output drives more input]

UNIT ECONOMICS:
| Metric | Value | Target |
|--------|-------|--------|
| CAC | $[X] | <$[Y] |
| LTV | $[A] | >$[B] |
| LTV/CAC | [X] | >3 |
| Payback Period | [Y] months | <12 |
| Gross Margin | [Z%] | >[W%] |

COHORT RETENTION:
| Cohort | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| Jan 24 | 60% | 45% | 35% | 28% |

PROJECTIONS:
| Month | Users | Revenue | CAC | LTV |
|-------|-------|---------|-----|-----|
| [M1] | [X] | $[Y] | $[Z] | $[W] |

KEY ASSUMPTIONS:
- [Assumption 1]: [Value and rationale]
- [Assumption 2]: [Value and rationale]
```

### Experiment Template

```
GROWTH EXPERIMENT — [Name]

Status: [Planned/Running/Complete]

HYPOTHESIS:
We believe that [change]
Will result in [outcome]
As measured by [metric]

RATIONALE:
[Why we think this will work]

DESIGN:
- Type: [A/B test, funnel test, email test, etc.]
- Control: [Current state]
- Treatment: [Change being tested]
- Target: [Segment or % of traffic]
- Duration: [X days/weeks]

SUCCESS CRITERIA:
- Primary: [Metric] improves by [X%] with [Y%] confidence
- Secondary: [Metric] improves by [X%]
- Guardrail: [Metric] does not decline by more than [Y%]

RESULTS:
| Metric | Control | Treatment | Lift | P-Value |
|--------|---------|-----------|------|---------|
| [M1]   | [X]     | [Y]       | [Z%] | [P]     |

LEARNINGS:
- [Key insight 1]
- [Key insight 2]

DECISION:
[Ship/Don't Ship/Iterate]

NEXT STEPS:
- [Action item 1]
- [Action item 2]
```

### Funnel Analysis Template

```
FUNNEL ANALYSIS — [Date]

USER JOURNEY MAP:
| Step | Users | Conversion | Drop-off | Time |
|------|-------|------------|----------|------|
| Visit| 100%  | —          | —        | —    |
| Signup| 15%  | 15%        | 85%      | 2 min|
| Activation| 8%| 53%       | 47%      | 1 day|
| Retention D7| 4%| 50%      | 50%      | 7 days|
| Paid | 1%    | 25%        | 75%      | 14 days|

TOP DROP-OFF ANALYSIS:

Step 1: Visit → Signup (85% drop)
- Hypothesis: Value prop unclear
- Evidence: Heatmaps show no scroll, exit surveys
- Test: New headline + social proof
- Priority: P0

Step 2: Signup → Activation (47% drop)
- Hypothesis: Onboarding too complex
- Evidence: Session recordings show confusion
- Test: Simplified onboarding flow
- Priority: P1

OPPORTUNITY SIZING:
| Improvement | Current | Target | Impact |
|-------------|---------|--------|--------|
| Signup CVR  | 15%     | 20%    | +33% users |
| Activation  | 53%     | 65%    | +23% activated |
| Total Impact| —       | —      | +64% bottom |
```

### Referral Program Design

```
REFERRAL PROGRAM — [Program Name]

MECHANICS:
- Referrer reward: [Incentive]
- Referee reward: [Incentive]
- Trigger: [When is user prompted?]
- Channels: [Email, in-app, social]

VIRAL CALCULATION:
- Invitations per user (i): [X]
- Conversion rate (c): [Y%]
- Viral coefficient (K): i × c = [Z]
- Target: K > 0.7 sustained

PROGRAM METRICS:
| Metric | Current | Target |
|--------|---------|--------|
| Referral rate | [X%] | [Y%] |
| Referral CAC | $[A] | <$[B] |
| Referral quality | [C%] | >[D%] |

OPTIMIZATION TESTS:
1. Incentive amount (test 2-3 levels)
2. Referral messaging (test copy)
3. Timing (when to ask)
4. Channel (email vs. in-app vs. social)
5. Friction (one-click vs. manual)

EXAMPLES BY MODEL:
- Dropbox: Free storage (both sides)
- Uber: Ride credits (both sides)
- PayPal: Cash bonus (both sides)
- Airbnb: Travel credits (both sides)
```

---
