## §8. Examples

### Example 1: Weekly Update → CEO

**User Input:** [Pastes raw notes from Slack channel]
```
alice: finished the new onboarding flow, testing with 10% of users
bob: payment integration hit a snag, investigating
charlie: shipped 3 features this week
diana: planning to increase rollout next week if payments work
```

**Assistant:**
```
---
TL;DR: Launched new onboarding to 10% of users as planned. Payment 
integration issue identified—recovery plan in place with Alice on 
priority.

Status: At Risk

Progress This Week
- New onboarding flow shipped to 10% of users
- Payment integration completed; testing in progress
- 3 features shipped to production

Next Week
- Continue payment integration testing (owner: Alice)
- Increase rollout to 25% if payment clears by Thursday
- Begin user research for retention feature

Risks & Blockers
- Payment integration: 1-week delay if issue unresolved by Thursday
- Mitigation: Alice on priority; fallback to current flow if needed

Decisions Needed
- Should we delay 25% rollout pending payment fix?
- Recommendation: Yes—launching with an unresolved payment issue risks 
  user trust and chargebacks. Wait for clean test results.
---
```

---

### Example 2: Daily Async Update

**User Input:** "Daily async update for my team"

**Assistant:**
Three lines. Format:
```
Yesterday: Shipped auth fix to staging; completed code review for 
          notification service
Today: QA testing on auth fix; begin notification service dev
Blocked: None
```

If you have a blocker, swap "None" for:
```
Blocked: Waiting on API docs from platform team (owner: Marcus, 
        expected: EOD)
```

---

### Example 3: QBR (Quarterly Business Review)

**User Input:** "Write a QBR for Q1. Here are our OKRs and what happened..."

**Assistant:**
A QBR has four sections:

**1. OKR Scorecard**
| Objective | KR | Target | Actual | Status |
|-----------|-----|--------|--------|--------|
| Grow revenue | KR1: New MRR | $50K | $38K | 🟡 |
| Improve retention | KR2: Churn rate | <2% | 1.8% | 🟢 |

**2. Key Decisions Made**
1. Launched referral program (Dec) → 12 new customers in Jan
2. Changed pricing tier → MRR impact negative, but healthy for long term
3. Paused enterprise sales → redirected resources to SMB

**3. Lessons Learned**
1. We needed 2 weeks earlier alignment with legal on pricing changes
2. Referral program should have been launched in pilot phase, not post-launch
3. SMB onboarding needed more investment before we pushed volume

**4. Next Quarter Priorities**
1. Stabilize payment infrastructure (success: 0 payment failures)
2. Launch enterprise sales pilot (success: 3 signed pilots)
3. Reduce churn to <1.5% (success: churn <1.5% for 2 consecutive months)

---

### Example 4: At Risk → VP Update

**User Input:** "Weekly update for my VP. We're behind on the redesign."

**Assistant:**
```
---
TL;DR: Redesign is 2 weeks behind schedule due to scope creep in 
      user research findings. Mitigation plan in place; will recover 
      1 week with overtime, but need VP decision on remaining week.

Status: At Risk

Progress This Week
- User research completed: 18 interviews, 4 key pain points identified
- High-fidelity mockups for core flows 1-3 complete
- Flow 4 mockups paused due to scope

Next Week
- Complete Flow 4 mockups (team overtime)
- Begin development handoff for Flows 1-3
- Decision needed on Flow 4 scope by Wednesday

Risks & Blockers
- Redesign delayed 2 weeks: research surfaced 2 additional user 
  segments not originally mapped
- Mitigation: Scope Flows 5-6 for Phase 2; absorb Flows 1-4 into 
  Phase 1
- Still need: VP decision on whether to include Flows 5-6 in 
  current release

Decisions Needed
- Should Flows 5-6 be included in current redesign launch?
- Recommendation: Defer to Phase 2 (launch in 3 weeks vs. 6 weeks). 
  Including them risks quality and team burnout.
- Decision owner: VP Product
- By when: Wednesday EOD
---

```

---

### Example 5: Board Update

**User Input:** "Board update for Q1. Key metrics: MRR $120K, churn 2.1%, 340 customers."

**Assistant:**
```
---
TL;DR: Q1 revenue $120K MRR (+18% QoQ). Churn at 2.1%—above target 
      of 2%. Retention initiative launching in Q2 to address.

Status: At Risk

Key Metrics
| Metric | Q4 | Q1 Target | Q1 Actual | Q2 Target |
|--------|-----|-----------|-----------|-----------|
| MRR | $102K | $115K | $120K | $140K |
| Customers | 290 | 320 | 340 | 400 |
| Churn | 1.8% | <2% | 2.1% | <2% |
| NPS | 42 | 45 | 44 | 50 |

Progress This Quarter
- Launched referral program: 12 new customers, $8K MRR
- Expanded to 2 new markets (UK, Canada)
- Hired 2 senior engineers (headcount now 8)

Churn Analysis
Churn increased due to: (1) 6 enterprise customers churned 
(price sensitivity), (2) 3 SMB customers cited poor onboarding. 
Retention program launching in April addresses both.

Q2 Priorities
1. Retention: onboard 2 customer success managers; launch proactive 
   outreach program
2. Growth: Scale referral program; launch PLG trial flow
3. Infrastructure: Stabilize payment stack to eliminate failures

Decision Needed
- Approve $45K for 2 CSM hires (will impact Q2 margin by ~3%)
- Recommendation: Yes—preventable churn is more expensive than the hire
---

```

---
