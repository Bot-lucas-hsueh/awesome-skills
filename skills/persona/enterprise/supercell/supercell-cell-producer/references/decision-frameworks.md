# § 5 · Decision Frameworks - Full Details

## Kill-or-Continue Framework

### The Core Question

"Should we kill this game or continue investing?"

### KILL Triggers (Celebrate These)

**Core Loop Issues**:
- Not fun after 3+ iterations
- Team doesn't play voluntarily
- "One more game" feeling absent
- Can't explain what's fun in one sentence

**Market Signals**:
- D1 Retention < 40% in soft launch
- D7 Retention < 15% in soft launch
- D30 Retention < 8% in soft launch
- Direct competitor launched similar (and better)
- Market size insufficient

**Team Factors**:
- Team has lost passion/belief
- Technical debt threatens scalability
- Key team member departure
- Team burnout

**Business Reality**:
- Clear path to profitability not visible
- Platform/policy changes invalidate concept
- Timing is wrong (market not ready)

### CONTINUE Triggers (Green Light)

**Engagement**:
- Team is passionate and playing daily
- Team plays voluntarily outside work hours
- External playtesters love it

**Metrics**:
- D1 Retention > 50%
- Clear path to D30 Retention > 10%
- ARPDAU on track for profitability

**Market**:
- Unique positioning vs. competitors
- Clear differentiation
- Right timing

**Technical**:
- Technical foundation solid and scalable
- Performance targets met
- Systems working well

### The Kill Meeting Process

**Step 1: Data Presentation** (15 min)
- Show all relevant metrics
- Compare to benchmarks
- Present team sentiment

**Step 2: External Feedback** (20 min)
- Show game to 2+ other cells
- Get honest opinions: "Should we kill this?"
- No defensiveness, just listening

**Step 3: Team Discussion** (15 min)
- Everyone shares perspective
- Game Lead listens, synthesizes

**Step 4: Decision** (5 min)
- Game Lead makes final call
- Kill: Schedule celebration, plan reassignment
- Continue: Define success metrics and timeline

**Step 5: Communication** (Ongoing)
- Announce decision company-wide
- Document learnings
- Execute decision without hesitation

---

## RICE Prioritization Framework

### Formula

```
Score = (Reach × Impact × Confidence) / Effort
```

### Factors

**Reach**: How many players will this affect?
- 1 = < 10% of players
- 2 = 10-50% of players
- 3 = > 50% of players
- 5 = All players

**Impact**: How much will this improve the player experience?
- 1 = Minor improvement
- 2 = Noticeable improvement
- 3 = Major improvement
- 5 = Game-changing

**Confidence**: How sure are we about the above estimates?
- 1 = Pure guess
- 2 = Some data/anecdotes
- 3 = Player research
- 5 = Proven in testing

**Effort**: How much team time will this take?
- 1 = Days
- 2 = 1-2 weeks
- 3 = 1 month
- 5 = 2+ months

### Prioritization Tiers

| Priority | Score | Action |
|----------|-------|--------|
| P0 (Must Have) | > 10 | Do immediately |
| P1 (Should Have) | 5-10 | Queue for next sprint |
| P2 (Could Have) | 2-5 | Backlog, review monthly |
| P3 (Won't Have) | < 2 | Kill, don't revisit |

### Example Calculation

**Feature**: Add daily login rewards

- Reach: 5 (all players)
- Impact: 3 (major improvement to retention)
- Confidence: 3 (player research shows this works)
- Effort: 2 (1-2 weeks)

**Score**: (5 × 3 × 3) / 2 = **22.5** → P0, do immediately

---

## Crisis Decision Framework

### Severity Assessment

**P0 (Critical)**:
- Game unplayable
- Data loss
- Security breach
- Major exploit affecting economy

**Response**: All hands, immediate action

**P1 (High)**:
- Major feature broken
- Significant player impact
- Revenue impact

**Response**: Dedicated team, fix within hours

**P2 (Medium)**:
- Minor issues
- Workarounds exist
- Limited player impact

**Response**: Scheduled fix, next deployment

**P3 (Low)**:
- Cosmetic issues
- No player impact

**Response**: Backlog for next sprint

### P0 Response Workflow

| Time | Action |
|------|--------|
| T+0 min | Issue detected via monitoring |
| T+5 min | Page on-call engineer |
| T+10 min | Assess scope and impact |
| T+15 min | Decision: Disable feature or emergency fix |
| T+30 min | Player communication (in-game, social) |
| T+1 hour | Hotfix deployed OR feature disabled |
| T+2 hours | Verify fix effectiveness |
| T+4 hours | Post-mortem scheduled |

### Communication Principles

**Be Transparent**:
- Acknowledge what happened
- Explain what you're doing to fix it
- Don't over-promise on timelines
- Follow up when resolved

**Speed Over Perfection**:
- Acknowledge quickly (within 30 min for P0)
- Fix can come later
- Silence is worse than imperfect communication

**Player First**:
- Compensate if appropriate
- Explain what you're doing to prevent recurrence
- Show you care about their experience
