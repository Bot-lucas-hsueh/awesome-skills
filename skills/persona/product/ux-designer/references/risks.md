## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| Accessibility Non-Compliance | 🟡 High | WCAG failures create legal risk (ADA/Section 508 lawsuits) and exclude users | Audit against WCAG 2.1 AA before launch; use automated checkers + manual review |
| Design Without Research | 🟡 High | Designing based on assumptions leads to low usability and adoption | Minimum: 5 user interviews OR review of existing research before designing |
| Skipping Error States | 🟡 High | Happy-path-only design breaks in production when edge cases occur | Design all error states, empty states, and loading states |
| Inconsistent Component Use | 🟢 Medium | Ad-hoc design choices fragment UX and increase engineering cost | Use design system components; document exceptions |
| HiPPO-Driven Design | 🟢 Medium | Highest Paid Person's aesthetic preference overrides user needs | Present design decisions anchored to user research, not personal taste |

---
