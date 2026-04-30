## § 7 · Standards & Reference

### 7.1 Test Naming Conventions

```typescript
// Pattern: "given [context], when [action], then [expected outcome]"
// Or: "[subject] should [expected behavior] when [condition]"

// ✅ GOOD — Describes behavior, not implementation
it('returns 404 when user does not exist', () => {});
it('applies 25% discount for enterprise tier customers', () => {});
it('rejects login after 5 consecutive failed attempts', () => {});
it('sends welcome email upon successful registration', () => {});
it('rolls back transaction when payment processing fails', () => {});

// ❌ BAD — Describes implementation, useless on failure
it('calls getUserById', () => {});
it('works', () => {});
it('test 1', () => {});
it('handles edge case', () => {});
it('processes correctly', () => {});

// ✅ GOOD — BDD-style with describe/it hierarchy
describe('PaymentProcessor', () => {
  describe('when processing valid payment', () => {
    it('should charge the provided amount', () => {});
    it('should create transaction record', () => {});
    it('should send receipt email', () => {});
  });
  
  describe('when payment is declined', () => {
    it('should not create transaction record', () => {});
    it('should log the declined reason', () => {});
    it('should notify user with specific error', () => {});
  });
});
```

### 7.2 Coverage Standards

```
Minimum Standards (enforced in CI):
  ├─ New code line coverage: ≥ 80% (enforced via diff-cover)
  ├─ New code branch coverage: ≥ 70%
  ├─ Global line coverage: ≥ 80% threshold (CI fails if lower)
  ├─ Critical paths (auth, payments, data processing): ≥ 95%
  ├─ Mutation score (test quality proxy): ≥ 60% (Stryker)
  └─ API contract coverage: 100% for public endpoints

Coverage Exclusions (justified only):
  ├─ Generated code (proto, swagger)
  ├─ Simple DTOs with no logic
  ├─ Framework boilerplate
  └─ External integration adapters

What Coverage Does NOT Tell You:
  ├─ Whether assertions are meaningful
  ├─ Whether edge cases are truly covered
  ├─ Whether tests will catch real bugs
  └─ Whether non-functional requirements are met
```

### 7.3 Flaky Test SLA

```
Flakiness Detection → Immediate Action Required:
  
  Individual Test Flakiness:
    > 10% per test → Fix within 8 hours (quarantine immediately)
    > 5%  per test → Fix within 24 hours
    > 1%  per test → Fix within 1 week
    
  Suite-Wide Flakiness:
    > 2%  global → Team investigation sprint
    > 5%  global → Halt new feature work; stabilize suite
    
  Prevention Measures:
    ├─ Auto-quarantine after 3 consecutive flaky runs
    ├─ Require flaky test investigation in standup
    ├─ Track flakiness rate in team metrics dashboard
    └─ Celebrate flakiness reduction achievements
```

### 7.4 Test Data Management Standards

```
Factory Pattern Requirements:
  ├─ Each test creates its own data (no shared state)
  ├─ Automatic cleanup in afterEach/afterAll
  ├─ Unique identifiers to prevent collisions
  ├─ Minimal valid data by default
  └─ Override options for specific test needs

Data Isolation Levels:
  Level 1: In-memory (fastest, for unit tests)
  Level 2: Test database per test (TestContainers)
  Level 3: Shared test DB with transaction rollback
  Level 4: Staging environment (E2E only)
```

---
