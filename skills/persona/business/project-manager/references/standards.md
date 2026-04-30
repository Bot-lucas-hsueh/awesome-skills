## § 7 · Standards & Reference

### RAID Log Template

```
RISKS (potential future issues):
ID | Description | Probability (H/M/L) | Impact (H/M/L) | Score | Response | Owner

ASSUMPTIONS (things treated as true without verification):
ID | Assumption | Impact If Wrong | Verification Date | Status

ISSUES (current active problems):
ID | Description | Date Raised | Impact | Resolution Plan | Owner | Target Date

DEPENDENCIES (what the project needs from others):
ID | Dependency | Provider | Required By | Status | Risk If Late
```

### Earned Value Analysis

```
Key formulas:
  PV = Planned Value (budgeted cost of scheduled work)
  EV = Earned Value (budgeted cost of completed work)
  AC = Actual Cost (actual spend for completed work)

  SPI = EV
    SPI < 1.0: Behind schedule
    SPI > 1.0: Ahead of schedule

  CPI = EV
    CPI < 1.0: Over budget
    CPI > 1.0: Under budget

  EAC = BAC
    If BAC = $1M and CPI = 0.85 → EAC = $1.18M (18% overrun projected)

  VAC = BAC - EAC  (Variance at Completion)
    Negative = projected overrun; positive = projected savings
```

### Agile Sprint Ceremonies

```
Sprint Planning (2 hours per week of sprint):
  Input: Prioritized backlog; team velocity
  Output: Sprint goal; committed backlog; task breakdown

Daily Standup (15 minutes):
  Yesterday / Today
  PM: Listen for blockers; resolve externally after standup

Sprint Review (1 hour per sprint week):
  Demo completed work; accept/reject stories
  PM: Invite stakeholders; capture feedback as backlog items

Retrospective (45-90 minutes):
  Start / Stop
  Output: ≥1 committed improvement action for next sprint
```

---
