## § 4 — Workflow

### § 4.1 Three-Phase Problem Solving

#### PHASE 1: DECONSTRUCTION (Hours 0-4)

| Task | ✓ Done When | ✗ FAIL If | Output |
|------|-------------|-----------|--------|
| List all requirements | Each has named owner | "Industry standard" unchallenged | Requirement register with owners |
| Categorize constraints | Physical / Economic / Tradition / Assumption | >50% "unknown/legacy" | Constraint classification |
| Strip tradition | ≥30% identified as assumptions | <10% challenged | Deletion candidate list |
| Build physics cost model | Bottom-up from material spot prices | Using market price as baseline | Cost floor analysis |
| Mission check | >70% alignment confirmed | <50% mission alignment | Go/No-go decision |

#### PHASE 2: RECONSTRUCTION (Hours 4-24)

| Task | ✓ Done When | ✗ FAIL If | Output |
|------|-------------|-----------|--------|
| Apply 5-Step Algorithm | All 5 steps executed in order | Steps skipped or reordered | Optimized solution |
| Generate alternatives | ≥3 radically different approaches | Minor variations only | Options with tradeoffs |
| Identify 80% drivers | Pareto analysis complete | No prioritization | Focus areas identified |
| Validate against physics | Checked vs thermodynamics, materials | Contradicts fundamental laws | Physics validation |
| Build decision matrix | Quantified comparison across options | Qualitative "pros/cons" only | Data-driven decision |

#### PHASE 3: VALIDATION (Hours 24-72)

| Task | ✓ Done When | ✗ FAIL If | Output |
|------|-------------|-----------|--------|
| Rapid prototype | Working demonstration in <2 weeks | >1 month to first test | Proof of concept |
| Real-world test | Physical test or shadow mode data | Simulation-only validation | Validated performance |
| Measure vs baseline | Quantified improvement documented | "Feels better" assessment | Metric confirmation |
| Assign ownership | Named end-to-end accountable owner | Handoffs, unclear accountability | Owner committed |
| Production readiness | Cpk >1.33, safety validated | Automating unstable process | Ready to scale |

### § 4.2 OTA Deployment Workflow

```
PHASE 1: DEVELOPMENT (Days 1-5)
├── Feature implementation with unit tests
├── Local simulation testing
├── Hardware-in-the-loop validation
└── Code review (no committees; direct peer review)

PHASE 2: VALIDATION (Days 5-8)
├── CI/CD automated test suite
├── Canary deployment to test fleet (100 vehicles)
├── Monitor metrics: crash rate, performance, battery impact
└── Dogfooding: Tesla employees get update first

PHASE 3: STAGED ROLLOUT (Days 8-15)
├── 1% of production fleet (50K vehicles)
├── Monitor for 24-48 hours
├── 10% of fleet (500K vehicles)
├── Monitor for 48-72 hours
├── 100% rollout
└── Automated rollback if error rate > 0.1%

PHASE 4: POST-DEPLOYMENT (Ongoing)
├── Fleet health monitoring
├── Customer feedback analysis
├── Performance regression detection
└── Next iteration planning
```

---
