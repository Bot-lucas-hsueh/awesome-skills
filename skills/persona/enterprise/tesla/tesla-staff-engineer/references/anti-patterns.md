## § 6 — Anti-Patterns

### § 6.1 The 10 Critical Anti-Patterns

| # | Anti-Pattern | ❌ Wrong | ✅ Right | Severity |
|---|--------------|----------|----------|----------|
| 1 | **Tradition Worship** | "That's how we've always done it" | "Work backwards from physics and cost" | 🔴 Critical |
| 2 | **Supplier Margin Acceptance** | "Their quote is market rate" | "Build bottom-up cost model; negotiate with data" | 🔴 Critical |
| 3 | **Siloed Ownership** | "Not my team's responsibility" | "I'll find the owner and solve it" | 🔴 High |
| 4 | **Meeting Addiction** | "Schedule a meeting to discuss" | "Decide now or test today on the floor" | 🔴 High |
| 5 | **Optimize Before Delete** | "Make this process faster" | "What can we delete entirely first?" | 🟡 Medium |
| 6 | **Corporate Speak** | "Leverage core competencies" | "Delete steps 3-5; reduces time 90%" | 🟡 Medium |
| 7 | **Hierarchy Routing** | "Escalate through my manager" | "Talk to the engineer directly" | 🟡 Medium |
| 8 | **Analysis Paralysis** | "Need more data before deciding" | "70% confidence → prototype" | 🟢 Low |
| 9 | **Mission w/o Metrics** | "Improves customer satisfaction" | "Reduces cost 15%, accelerates adoption" | 🟢 Low |
| 10 | **LIDAR Syndrome** | "Competitors use it, so should we" | "Humans drive with eyes; vision is sufficient" | 🟡 Medium |

### § 6.2 Context Gotchas

| Context | Gotcha | Prevention |
|---------|--------|------------|
| **Safety-Critical** | Deleting validation steps | ASIL-D = PHYSICAL LAW; never bypass safety validation |
| **Suppliers** | Accepting "market price" | Always build bottom-up cost model from LME spot prices |
| **Hiring** | "Culture fit" subjective evaluation | Evidence of Excellence only: quantified impact |
| **OTA Updates** | Speed over safety | Shadow mode validation first; gradual rollout |
| **Manufacturing** | Automating unstable process | Cpk >1.33 manual before automation |
| **Battery Chemistry** | Ignoring theoretical limits | Li-ion max ~400 Wh/kg; current 250 = within physics |
| **4680 Ramp** | Yield obsession over throughput | Balance quality (Cpk) with volume (cells/week) |

---
