## §4. Standard Workflow

### §4.1 Five-Phase Engineering Workflow (ByteDance Style)

**Phase 1: CONTEXT ALIGNMENT (Days 1-3)**

1. Define problem context with data backing
2. Identify primary + guardrail kill metrics
3. Align all stakeholders on shared context
4. Set hard deadline in calendar
5. Scope check: MVP deliverable in <2 weeks?

**Phase 2: RAPID DESIGN (Days 4-7)**

1. Design MVP: simplest path to metric validation
2. Instrument data: metrics trackable from day 1
3. Design AB test: hypothesis + minimum sample size
4. Assess risks: failure modes + rollback plan

**Phase 3: ITERATE FAST (Weeks 2-6)**

1. Ship weekly: deploy to production every week
2. Monitor metrics: dashboard live, alerts configured
3. Iterate based on data: changes driven by signal
4. Decision gate at week 12: kill or scale?

**Phase 4: SCALE (If metrics support)**

1. Full rollout: 1% → 10% → 50% → 100%
2. Performance optimization: latency, cost at scale
3. Reliability hardening: SLA/SLO defined

**Phase 5: LEARN & RECYCLE (Continuous)**

1. Post-mortem: what worked? what didn't?
2. OKR update: results inform next quarter
3. Knowledge share: learnings shared org-wide

**Example: TikTok Feed Algorithm Iteration**
See §5 Example 1 for complete walkthrough.

**Template: Context Document**
```
Problem: [Clear statement with data]
Metrics: Primary [X], Guardrails [Y, Z]
Deadline: [Date]
Authority: [Who decides]
→ Your call.
```

**Decision Tree Pattern:**
```
IF context unclear → Align first
IF metric undefined → Define or stop
IF consensus not reached → Provide more context
IF deadline missed → Re-scope, not extend
IF guardrail breached → Rollback immediately
```

### §4.2 APP Factory Workflow

| Stage | Duration | Goal | Kill Criteria |
|-------|----------|------|----------------|
| **HYPOTHESIS** | 1-2 weeks | Validate user need with data | Clear problem statement |
| **MVP** | 2-4 weeks | Ship smallest thing to test | Core feature working |
| **GROWTH** | 8-12 weeks | Scale if metrics positive | Kill metric improving |
| **KILL** | <1 week | Terminate if criteria not met | Clear rationale documented |
| **SCALE** | Ongoing | Double down on winners | Dedicated team, full resources |

See references/app-factory.md for detailed product lifecycle management.

---
