## § 7 · Standards & Reference

### ITIL 4 Priority Matrix and SLA Targets

```
┌───────────┬──────────────────────────────┬──────────────┬────────────────┐
│ Priority  │ Definition                   │ Response SLA │ Resolution SLA │
├───────────┼──────────────────────────────┼──────────────┼────────────────┤
│ P1 – Crit │ Complete service outage;     │ 15 minutes   │ 4 hours        │
│           │ multiple users or business-  │              │                │
│           │ critical system down         │              │                │
├───────────┼──────────────────────────────┼──────────────┼────────────────┤
│ P2 – High │ Significant degradation;     │ 1 hour       │ 8 hours        │
│           │ single user fully blocked or │              │                │
│           │ group partially impacted     │              │                │
├───────────┼──────────────────────────────┼──────────────┼────────────────┤
│ P3 – Med  │ Partial impact; user can     │ 4 hours      │ 24 hours       │
│           │ work with workaround;        │              │                │
│           │ non-critical service         │              │                │
├───────────┼──────────────────────────────┼──────────────┼────────────────┤
│ P4 – Low  │ No immediate impact;         │ 8 hours      │ Next business  │
│           │ service request or           │              │ day            │
│           │ enhancement                  │              │                │
└───────────┴──────────────────────────────┴──────────────┴────────────────┘
```

### Service Desk KPI Targets

| Metric | Target | Definition |
|--------|--------|------------|
| First Contact Resolution (FCR) | > 80% | Tickets resolved without escalation or callback |
| Customer Satisfaction (CSAT) | > 4.2
| Ticket Backlog Age | < 3 business days | No open ticket older than 3 days without an update |
| Mean Time to Resolve – P1 | < 4 hours | Clock starts at ticket creation |
| Mean Time to Resolve – P2 | < 8 hours | Clock starts at ticket creation |
| Mean Time to Resolve – P3 | < 24 hours | Business hours only |
| Abandoned Call Rate | < 5% | Calls dropped before agent answer |
| Knowledge Base Utilization | > 40% | Tickets resolved by referencing a KB article |

### Network Diagnostic Command Reference

→ Bash/PowerShell command reference: [references/code-block-2.md](references/code-block-2.md)

---
