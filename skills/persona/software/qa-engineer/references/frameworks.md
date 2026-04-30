## 7. Standards & Reference

### 7.1 Test Naming Convention

```typescript
// Pattern: "given [context], when [action], then [expected outcome]"
// Or: "[subject] [predicate] [expected behavior]"

// ✅ GOOD — describes behavior, not implementation
it('returns 404 when user does not exist', ...)
it('applies 25% discount for enterprise tier', ...)
it('rejects login after 5 consecutive failed attempts', ...)

// ❌ BAD — describes implementation, useless on failure
it('calls getUserById', ...)
it('works', ...)
it('test 1', ...)
```

### 7.2 Test Coverage Standards

```
Minimum Standards (enforced in CI):
  - New code coverage: ≥ 80% (enforced via diff-cover)
  - Global line coverage: ≥ 80% threshold (fail CI if lower)
  - Critical paths (auth, payments, data processing): ≥ 95%
  - Test quality proxy: mutation score ≥ 65% (Stryker)

What coverage does NOT tell you:
  - Whether assertions are meaningful
  - Whether edge cases are covered
  - Whether tests will catch real bugs
```

### 7.3 Flaky Test SLA

```
Flakiness Rate → Action Required:
  > 5%  per test    → Fix within 24 hours (quarantine immediately)
  > 1%  per test    → Fix within 1 week
  > 0.1% global     → Team investigation sprint
  > 5%  global      → Halt new feature work; stabilize suite first
```
