# Common Pitfalls & Anti-Patterns

## 10.1 Scheduling Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | Building the schedule before course requests are finalized | 🔴 High | Lock requests before building; verify all students can graduate |
| 2 | Ignoring prerequisite chains when placing courses | 🔴 High | Map all prerequisites before building; use SIS validation tools |
| 3 | Allowing unlimited schedule changes after deadline | 🔴 High | Enforce change windows strictly; document all requests |
| 4 | Placing students in courses without prerequisite verification | 🔴 High | Automate prerequisite checks; manual verification for edge cases |
| 5 | Scheduling without considering teacher certification | 🔴 High | Pre-map teachers to courses by credential before building |

## 10.2 Calendar & Capacity Anti-Patterns

- **Underestimating instructional minutes** → state compliance issues at audit time
- **Overloading certain periods** (teacher or room imbalance) → quality of instruction suffers
- **Scheduling all intervention courses at the end of the day** → stigma for students needing support
- **Ignoring facility constraints** (labs, shops, art rooms) when building sections
- **Failing to plan for staff absences/replacements in the schedule**

## 10.3 Communication Anti-Patterns

- Releasing the schedule without a transition period for families to review
- Not communicating course cancellation decisions to students before the semester starts
- Making unilateral schedule changes without notifying counselors
- Failing to document why a specific course was added/removed from the catalog

## 10.4 Best Practice Checklist

- [ ] All course prerequisites verified in SIS before schedule building
- [ ] Master schedule validated against graduation requirements for every student
- [ ] Schedule change requests processed within 5 business days
- [ ] Teacher certification map updated annually
- [ ] Minimum enrollment policy consistently applied
- [ ] Bell schedule aligned with state minimum instructional minutes
- [ ] Schedule published to families at least 2 weeks before school starts
- [ ] Alternative pathways communicated for cancelled courses
- [ ] Enrollment projections compared to actual enrollment after first week
- [ ] Post-schedule review conducted 30 days after semester start
