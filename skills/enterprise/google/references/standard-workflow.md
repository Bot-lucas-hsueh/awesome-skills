## §4. Standard Workflow

### §4.1 Five-Phase Engineering Workflow

**Phase 1: UNDERSTAND (Days 1-3)**

| Task | ✓ Done When | ✗ FAIL If | Output |
|------|-----------|---------|--------|
| Define user problem | User persona + pain documented | "Users want more features" | Problem statement |
| Identify metrics | Primary + guardrail metrics defined | No way to measure success | Metrics spec |
| Research existing solutions | Internal + external landscape | Reinventing without reason | Research doc |
| Scope ambition | 10× improvement target set | <20% improvement goal | Scope doc |
| OKR check | Connects to team OKR | Orphan work without alignment | OKR link |

**Phase 2: DESIGN (Days 4-10)**

| Task | ✓ Done When | ✗ FAIL If | Output |
|------|-----------|---------|--------|
| System design doc | Covers API, data model, scaling | Single-person mental model | Design doc |
| Architecture review | Reviewed by senior+ engineers | Security/privacy not considered | Sign-off |
| Risk assessment | Failure modes identified | No rollback plan | Risk doc |
| Scaling plan | Load test to 10×, latency budget | Not tested for scale | Scale doc |
| Experiment design | A/B test plan with hypotheses | No control group | Exp. spec |

**Phase 3: IMPLEMENT (Weeks 2-5)**

| Task | ✓ Done When | ✗ FAIL If | Output |
|------|-----------|---------|--------|
| Code with tests | >80% unit test coverage | No tests committed | CLs merged |
| Code review | ≥1 approval, nits addressed | Blocking comments unresolved | Approved CL |
| Dogfood | Internal users testing in <1 week | No internal feedback | Dogfood report |
| Staging validation | Passes load + integration tests | P1 bugs in staging | Staging sign-off |

**Phase 4: LAUNCH (Weeks 5-6)**

| Task | ✓ Done When | ✗ FAIL If | Output |
|------|-----------|---------|--------|
| Staged rollout | 1% → 10% → 50% → 100% | Fast-forward without data | Rollout plan |
| Metrics monitoring | Dashboards live, alerts configured | No monitoring plan | Monitor setup |
| Rollback readiness | Tested rollback path | >30min to rollback | Rollback tested |
| Launch announcement | Comms drafted, stakeholders aligned | Surprised partners | Launch doc |

**Phase 5: LEARN (Continuous)**

| Task | ✓ Done When | ✗ FAIL If | Output |
|------|-----------|---------|--------|
| Post-launch analysis | 2-week data reviewed | Ignoring guardrail metrics | Analysis doc |
| 20% reflection | What worked? What didn't? | No learning captured | Retro doc |
| Next OKR cycle | Results inform next quarter | Disconnected from prior | OKR update |

### §4.2 OKR Cycle Workflow

| Phase | Timing | Activities |
|-------|--------|-----------|
| **Q-START** | Week 1 | Read org OKRs (Mon) → Draft team OKRs (Wed) → Manager calibration (Fri) |
| **MID-Q** | Week 6 | Review KR progress → Identify blockers → Rebaseline if scope changed |
| **Q-END** | Week 10 | Self-score KRs → Manager calibration → Retro → Draft next Q OKRs |

See references/okr-methodology.md for OKR templates and grading rubrics.

---
