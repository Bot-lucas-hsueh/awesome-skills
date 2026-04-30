## 8. Standard Workflow

### Workflow 1: New Feature Test Strategy

```
PHASE 1: STORY KICK-OFF (Before any code is written)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 1.1: Risk assessment
  → Identify user-facing impact: payment flow? Auth? Data loss possible?
  → Classify risk: HIGH / MEDIUM
  ✓ Done: Risk matrix documented in ticket
  ✗ FAIL: Starting tests without understanding business risk

Step 1.2: Acceptance criteria review
  → Confirm ACs are testable: "user sees confirmation email" ✓
  → Flag untestable ACs: "system feels responsive" — needs SLO
  ✓ Done: Every AC has a corresponding test scenario
  ✗ FAIL: ACs are vague or untestable as written

Step 1.3: Test type selection
  → Unit tests: for business logic, calculations, transformations
  → Integration tests: for DB interactions, external service calls
  → E2E tests: for the critical user journey only (not every variation)
  → Performance gate: for any endpoint in a hot path
  ✓ Done: Test plan documented (what type, what tool, what coverage target)
  ✗ FAIL: "We'll figure it out when coding" — no plan = missing coverage

PHASE 2: TEST IMPLEMENTATION (During feature development)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 2.1: Unit tests first (TDD preferred)
  → Write failing tests for each acceptance criterion
  → Cover: happy path + error paths + boundary conditions
  ✓ Done: New code has ≥ 80% unit test coverage
  ✗ FAIL: Unit tests only cover happy path

Step 2.2: Integration tests for component interactions
  → Test DB queries with TestContainers (real DB, not mocks)
  → Test external service calls with WireMock stubs
  ✓ Done: Integration tests pass against containerized dependencies
  ✗ FAIL: Mocking DB/HTTP in integration tests (tests the mock, not the behavior)

Step 2.3: E2E test for the critical user journey
  → One happy-path E2E test per acceptance criterion (max 3 E2E per feature)
  → Use Page Object Model — no direct locators in test code
  ✓ Done: E2E passes on Playwright in CI with 0 retries needed
  ✗ FAIL: E2E passes only with retries=3 (quarantine immediately)

Step 2.4: Non-functional tests
  → Add k6 smoke test if endpoint is in the hot path
  → Add axe-core accessibility check if UI was changed
  ✓ Done: p95 < SLO, 0 critical accessibility violations
  ✗ FAIL: Skipping non-functional "because it's a small feature"

PHASE 3: CI/CD GATE & RELEASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 3.1: Coverage gate
  → CI reports coverage for new files; diff-cover enforces ≥ 80% on changed lines
  ✓ Done: PR passes coverage gate without exclusions
  ✗ FAIL: Coverage artificially inflated by excluding files

Step 3.2: Flakiness verification
  → Run E2E 3 times consecutively; all must pass without retries
  ✓ Done: 3/3 clean runs
  ✗ FAIL: Any failure → quarantine before merge

Step 3.3: Performance gate (merge to main only)
  → k6 smoke test against staging: p95 < 500ms, error rate < 1%
  ✓ Done: All thresholds pass
  ✗ FAIL: Block release; investigate DB queries, N+1, connection pool
```

### Workflow 2: Defect Investigation

```
PHASE 1: TRIAGE (< 30 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 1.1: Reproduce in isolation
  → Can you reproduce with a minimal test case?
  ✓ Done: Failing test written that proves the bug
  ✗ FAIL: Cannot reproduce → gather more data (logs, traces, test env)

Step 1.2: Severity classification
  → CRITICAL: Data loss, security breach, payment failure → hot-fix now
  → HIGH: Core feature broken → fix in current sprint
  → MEDIUM: Degraded experience → fix in next sprint
  → LOW: Cosmetic → backlog
  ✓ Done: Severity documented; stakeholders notified if CRITICAL/HIGH

PHASE 2: ROOT CAUSE ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Step 2.1: Write a failing regression test BEFORE fixing the code
  → The test must fail on the buggy code; pass after the fix
  ✓ Done: Regression test exists in the PR
  ✗ FAIL: Fixing without a test → same bug will recur

Step 2.2: Determine root cause (5 Whys or fishbone diagram)
  → Don't fix symptoms; find the root cause
  ✓ Done: Root cause documented in ticket
  ✗ FAIL: "We just added a null check" without understanding why null occurs

PHASE 3: FIX & VERIFY
━━━━━━━━━━━━━━━━━━━━
Step 3.1: Fix the code; verify regression test now passes
Step 3.2: Run full test suite; confirm no regressions introduced
Step 3.3: Update test for boundary cases exposed by the bug
  ✓ Done: PR merged; monitoring shows no recurrence within 48 hours
```
