## § 8 · Standard Workflow

### Phase 1: Test Strategy Design

| Step | Activity | Deliverable | Gate |
|------|----------|-------------|------|
| 1.1 | Requirements analysis — identify testable acceptance criteria | Testable requirements mapping | [✓] PASS / [✗] FAIL |
| 1.2 | Risk assessment — probability × impact analysis | Risk-prioritized test matrix | [✓] PASS / [✗] FAIL |
| 1.3 | Test pyramid design — Unit:Integration:E2E ratios | Test architecture diagram | [✓] PASS / [✗] FAIL |
| 1.4 | Coverage target definition — meaningful coverage goals | Coverage strategy document | [✓] PASS / [✗] FAIL |
| 1.5 | CI/CD integration plan — quality gates definition | Pipeline configuration spec | [✓] PASS / [✗] FAIL |

**Phase 1 Success Criteria:**
- All high-risk features have defined test strategies
- Coverage targets align with team capacity and sprint velocity
- Quality gates are enforceable in CI
- ⚠️ FAIL if any critical path lacks test coverage plan

### Phase 2: Framework Implementation

| Step | Activity | Deliverable | Gate |
|------|----------|-------------|------|
| 2.1 | Framework setup — tooling, configuration, base classes | Runnable test infrastructure | [✓] PASS / [✗] FAIL |
| 2.2 | Page Object/Component development | Reusable page/component library | [✓] PASS / [✗] FAIL |
| 2.3 | Test data factory implementation | Data generation utilities | [✓] PASS / [✗] FAIL |
| 2.4 | CI pipeline configuration | GitHub Actions/GitLab CI config | [✓] PASS / [✗] FAIL |
| 2.5 | Baseline coverage establishment | Initial coverage report | [✓] PASS / [✗] FAIL |

**Phase 2 Success Criteria:**
- Framework supports all required test types
- New tests can be written with minimal boilerplate
- CI pipeline runs in < 15 minutes
- ⚠️ FAIL if test execution time exceeds budget

### Phase 3: Test Implementation

| Step | Activity | Deliverable | Gate |
|------|----------|-------------|------|
| 3.1 | Unit test development — business logic coverage | Unit test suite | [✓] PASS / [✗] FAIL |
| 3.2 | Integration test development — service boundaries | Integration test suite | [✓] PASS / [✗] FAIL |
| 3.3 | Contract test implementation — API compatibility | Contract test suite | [✓] PASS / [✗] FAIL |
| 3.4 | E2E test development — critical user journeys | E2E test suite | [✓] PASS / [✗] FAIL |
| 3.5 | Coverage analysis and gap filling | Coverage report > 80% | [✓] PASS / [✗] FAIL |

**Phase 3 Success Criteria:**
- All high-risk code paths have automated tests
- Code coverage meets defined targets
- All tests pass consistently (flakiness < 1%)
- ⚠️ FAIL if coverage gaps exist in critical paths

### Phase 4: Quality Operations

| Step | Activity | Deliverable | Gate |
|------|----------|-------------|------|
| 4.1 | Metrics dashboard setup — coverage, flakiness, escape rate | Quality metrics dashboard | [✓] PASS / [✗] FAIL |
| 4.2 | Defect tracking integration — traceability | Bug-to-test mapping | [✓] PASS / [✗] FAIL |
| 4.3 | Flaky test monitoring and remediation | Flakiness report < 1% | [✓] PASS / [✗] FAIL |
| 4.4 | Performance baseline establishment | Performance benchmark | [✓] PASS / [✗] FAIL |
| 4.5 | Continuous improvement process | Quality retro cadence | [✓] PASS / [✗] FAIL |

**Phase 4 Success Criteria:**
- Quality metrics are visible to the team
- Flaky tests are tracked and addressed
- Performance regressions are caught in CI
- ⚠️ FAIL if quality issues are not measurable

---
