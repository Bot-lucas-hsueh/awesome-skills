# Shape Up — Standard Workflow

## Workflow Overview

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  DISCOVERY  │────▶│  SHAPING    │────▶│  BETTING    │────▶│  BUILDING   │
│  (§8.1)     │     │  (§8.2)     │     │  (§8.3)     │     │  (§8.4)     │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                                                                    │
                                              ┌─────────────────────┘
                                              ▼
                                        ┌─────────────┐     ┌─────────────┐
                                        │  COOL-DOWN  │◀────│  REVIEW     │
                                        │  (§8.5)     │     │  (§8.6)     │
                                        └─────────────┘     └─────────────┘
```

---

## § 8.1 Discovery Phase

### Objective
Understand the problem deeply before shaping any solution.

### Activities

| Step | Action | Output |
|------|--------|--------|
| 1.1 | Problem Interview | "What's the specific frustration?" |
| 1.2 | User Context | "Who has this problem? When?" |
| 1.3 | Current Behavior | "What do they do instead?" |
| 1.4 | Desired Outcome | "What would success look like?" |

### Decision: Is This Shaped Work?

| Criteria | Go to Shaping | Don't Shape |
|----------|---------------|-------------|
| Problem is specific | ✓ | ✗ (too abstract) |
| Solution is unclear | ✓ | ✗ (obvious fix) |
| Requires unknowns exploration | ✓ | ✗ (known implementation) |
| Worth 1-6 weeks | ✓ | ✗ (too small/large) |

### Exit Criteria
- [ ] Problem statement is a specific scenario, not a feature request
- [ ] At least 3 specific user contexts identified
- [ ] Current behavior documented (what users do instead)
- [ ] Success metrics defined (what "solved" looks like)

---

## § 8.2 Shaping Phase

### Objective
Produce a pitch ready for betting—rough but clear enough to build from.

### Activities

| Step | Action | Output |
|------|--------|--------|
| 2.1 | Set Appetite | Choose: Small (1-2w) or Big (6w) |
| 2.2 | Narrow Problem | Specific scenario, not "build X" |
| 2.3 | Solution Sketch | Fat marker drawing, not wireframe |
| 2.4 | Call Rabbit Holes | What to avoid, hard parts to flag |
| 2.5 | Define No-Gos | What's explicitly out of scope |

### Shaping Rules

| Rule | Why |
|------|-----|
| **PM + Engineer together** | Shaping requires both perspectives |
| **Fat marker, not pixels** | Rough enough to invite collaboration |
| **Appetite, not estimate** |约束 scope, don't predict timeline |
| **Rabbit holes as gifts** | Flagging unknowns helps builders |

### Pitch Template

```
## Pitch: [Name]

### Problem
[A specific scenario where users are frustrated today]

### Appetite
[Small: 1-2 weeks | Big: 6 weeks]
[How many people: 1-3]

### Solution
[Fat marker sketch description - 2-3 key screens/flows]
[Core mechanism - what's the key interaction?]

### Rabbit Holes
- [Unknown 1 - what to avoid]
- [Unknown 2 - what needs exploration]

### No-Gos
- [Explicitly not included]
- [Out of scope for this cycle]
```

### Exit Criteria
- [ ] Appetite is set (S/M/L) - this is the constraint
- [ ] Problem is specific enough to solve
- [ ] Solution sketch shows the idea (not full design)
- [ ] At least 2 rabbit holes identified
- [ ] At least 2 no-gos defined
- [ ] Senior engineer approved the shaping

---

## § 8.3 Betting Phase

### Objective
Make real commitments, not backlog reshuffling.

### Activities

| Step | Action | Output |
|------|--------|--------|
| 3.1 | Present Pitches | Team reviews shaped work |
| 3.2 | Ask Questions | Clarify unknowns |
| 3.3 | Bet or Pass | Each pitch: bet or not this cycle |
| 3.4 | Track Capacity | Sum of bets ≤ available team time |
| 3.5 | Announce Cycle | Who's building what |

### Betting Rules

| Rule | Implication |
|------|-------------|
| **Bets are real** | No "we'll see how it goes" |
| **No interruptions** | Build time is protected |
| **Unfinished doesn't roll** | If it doesn't ship, it comes back to betting |
| **Circuit breaker only** | Only true emergencies stop work |

### Capacity Math

```
Team Capacity (per 6-week cycle):
- 1 person = ~4.5 weeks building time
- 2 people = ~9 weeks building time
- 3 people = ~13.5 weeks building time

(Account for: meetings, code review, bugs, etc.)
```

### Exit Criteria
- [ ] All pitches bet on have owners
- [ ] Total bet time ≤ team capacity
- [ ] Circuit breaker rules agreed
- [ ] Cycle start date announced

---

## § 8.4 Building Phase

### Objective
Execute the pitched work with autonomy and clarity.

### Activities

| Step | Action | Output |
|------|--------|--------|
| 4.1 | Kickoff | Builders read pitch, ask questions |
| 4.2 | Scope Tasks | Team breaks pitch into 4-9 tasks |
| 4.3 | Track Progress | Update Hill Chart daily |
| 4.4 | Handle Scope Creep | Renegotiate appetite OR cut scope |
| 4.5 | Signal Blockers | Hill Chart shows uphill struggles |

### Hill Chart Interpretation

| Position | Meaning | Action |
|----------|---------|--------|
| **Bottom of hill** | Starting, discovering the problem | Time for exploration |
| **Going uphill** | Working on unknowns, learning | Don't estimate completion |
| **Top of hill** | Unknowns resolved, ready to execute | Shift to building mode |
| **Going downhill** | Executing known solution | Ship it |
| **At flat ground** | Done, tested, ready to ship | Ship |

### Scope Creep Protocol

```
Team: "We want to add [new scope]"

Response:
1. What's the appetite? [Fixed]
2. What from the pitch will you cut?
3. OR: Bring to next betting table

NOT OK: Just add it without cutting
```

### Exit Criteria
- [ ] All pitched work shipped OR circuit breaker triggered
- [ ] Hill Chart reflects real progress, not theater
- [ ] No scope creep without renegotiation

---

## § 8.5 Cool-Down Phase

### Objective
Reset and recharge between cycles.

### Activities

| Step | Action | Output |
|------|--------|--------|
| 5.1 | No Scheduled Work | Team chooses what to work on |
| 5.2 | Bug Fixing | Pay down technical debt |
| 5.3 | Exploration | Investigate next cycle ideas |
| 5.4 | Personal Projects | Learning, experimentation |
| 5.5 | Rest | Genuine break from product work |

### Cool-Down Rules

| Rule | Why |
|------|-----|
| **No planned work** | This is not "extra sprint" time |
| **Team decides** | Individual choice, not manager assignment |
| **Protected** | Leadership must not encroach |

### Exit Criteria
- [ ] Full 2-week cool-down occurred
- [ ] No pressure to work on product features
- [ ] Team feels recharged

---

## § 8.6 Review Phase

### Objective
Capture learnings and plan improvements.

### Activities

| Step | Action | Output |
|------|--------|--------|
| 6.1 | Shipped Review | What shipped? What didn't? |
| 6.2 | Learning Capture | What worked? What didn't? |
| 6.3 | Process Review | How did Shape Up work? |
| 6.4 | Shout Outs | Recognize good work |

### Review Questions

| Question | Purpose |
|----------|---------|
| What from the pitch shipped? | Outcome focus |
| What didn't ship and why? | Learn about estimation |
| Was the appetite right? | Calibrate sizing |
| Were rabbit holes accurate? | Improve shaping |
| Any scope creep issues? | Check discipline |
| Hill Chart accurate? | Improve tracking |

### Exit Criteria
- [ ] Review completed and documented
- [ ] Improvements identified for next cycle
- [ ] Team acknowledges wins and learnings

---

## Phase Summary Checklist

| Phase | Entry Criteria | Exit Criteria |
|-------|----------------|---------------|
| Discovery | Problem identified | Problem is specific |
| Shaping | Problem shaped | Pitch ready |
| Betting | Pitches presented | Real commitments |
| Building | Cycle starts | Work shipped |
| Cool-Down | Cycle ends | Full break taken |
| Review | Cool-down done | Learnings captured |