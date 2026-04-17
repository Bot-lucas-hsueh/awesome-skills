## 8. Standard Workflow

### 8.1 CTO Engagement Workflow

```
Phase 1: Technical Assessment (Week 1–2)
├── Audit current state architecture: draw system diagram, identify seams and coupling
├── Run tech debt analysis: SonarQube scan + engineer interviews on pain points
├── Assess team capabilities: skill matrix, DORA metrics baseline, attrition trends
├── Review DORA metrics: deployment frequency, lead time, MTTR, change failure rate
├── Analyze incident history: P0/P1 count, MTTR, repeat incidents (systemic issues)
└── [✓ Done]: Written "Current State" assessment with quantified findings (not opinions)
    [✗ FAIL]: No baseline metrics → STOP, instrument observability before any strategy work

Phase 2: Strategy Design (Week 3–4)
├── Define target architecture: draw future state, identify migration path milestones
├── Build technology roadmap: prioritized by business value, not technical elegance
├── Design org structure: apply Team Topologies, align to target architecture domains
├── Make build/buy/partner decisions: Wardley Map each major platform component
├── Set engineering OKRs: connect to business objectives, include DORA targets
├── Define hiring plan: role sequencing, compensation bands, sourcing strategy
└── [✓ Done]: Roadmap with Q1–Q4 milestones approved by CEO; hiring plan with budget
    [✗ FAIL]: Roadmap not connected to business outcomes → iterate until CEO/CFO buy-in

Phase 3: Execution & Governance (Ongoing)
├── Sprint cadence: weekly engineering all-hands, bi-weekly architecture review
├── Engineering reviews: monthly DORA metrics review; quarterly tech radar update
├── Incident management: P0/P1 → 48h blameless postmortem → systemic fix within 30 days
├── Hiring execution: weekly pipeline review; calibration sessions before each loop
├── Tech debt repayment: 20% sprint allocation; monthly debt cost report to leadership
└── [✓ Done]: DORA metrics improving quarter-over-quarter; attrition < 10%; roadmap on track
    [✗ FAIL]: DORA metrics degrading → escalate to full-team retro; pause feature work if needed
```

---

