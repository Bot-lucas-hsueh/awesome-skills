## § 4 — Workflow

### 4.1 Three-Phase Feature Development

#### PHASE 1: VALIDATION (Weeks 0-4)

| Task | ✓ Done When | ✗ FAIL If | Output |
|------|-------------|-----------|--------|
| Safety impact assessment | Documented risk analysis | Any unmitigated critical risk | Safety case document |
| Simulation validation | 10M+ miles, >99.9% pass rate | <95% on critical scenarios | Simulation report |
| Closed-course testing | All edge cases covered | Any safety-critical failure | Test report |
| Regulatory pre-review | Alignment confirmed | Compliance gaps | Regulatory memo |

#### PHASE 2: CONTROLLED DEPLOYMENT (Weeks 4-12)

| Task | ✓ Done When | ✗ FAIL If | Output |
|------|-------------|-----------|--------|
| Geo-fenced pilot | 10K+ miles without incident | Any at-fault incident | Pilot metrics |
| Gradual expansion | Service area increased 10× | Disengagement rate increase | Expansion report |
| Driver feedback integration | 95%+ positive sentiment | <80% satisfaction | Feedback analysis |
| Performance monitoring | All KPIs within bounds | Any safety metric regression | Monitoring dashboard |

#### PHASE 3: FULL DEPLOYMENT (Weeks 12+)

| Task | ✓ Done When | ✗ FAIL If | Output |
|------|-------------|-----------|--------|
| City-wide availability | Full service area coverage | Availability <99.5% | Launch report |
| Continuous monitoring | Real-time safety dashboard | Alert fatigue, missed incidents | Operations center |
| Iterative improvement | Weekly model updates | Regression in any metric | Improvement log |
| Public reporting | Monthly safety data release | Transparency gaps | Safety Impact Hub update |

### 4.2 Safety Investigation Template

```markdown
## Safety Incident Report: [ID]

**Date/Time:** [YYYY-MM-DD HH:MM]  
**Location:** [City, Intersection]  
**Vehicle ID:** [Fleet ID]  
**Miles at Incident:** [Odometer]

### Incident Summary
[2-3 sentence objective description]

### Sensor Data Analysis
| Modality | Data Quality | Key Observations |
|----------|--------------|------------------|
| LiDAR | ✅ Complete | [Object detection details] |
| Camera | ✅ Complete | [Visual classification] |
| Radar | ✅ Complete | [Velocity measurements] |

### Root Cause Analysis
1. **Immediate Cause:** [What happened]
2. **Contributing Factors:** [Why it happened]
3. **System Factor:** [Underlying design/process issue]

### Corrective Actions
- [ ] Immediate: [Action + Owner + Due Date]
- [ ] Short-term: [Action + Owner + Due Date]
- [ ] Long-term: [Action + Owner + Due Date]

### Simulation Replay
- Scenario recreated: ✅/❌
- Fix validated: ✅/❌
- Regression test added: ✅/❌
```

---
