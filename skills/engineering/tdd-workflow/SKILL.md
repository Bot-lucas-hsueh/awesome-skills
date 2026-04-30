---
name: tdd-workflow
kind: workflow
version: 1.0.0
tags:
  - domain: engineering
  - subtype: tdd-workflow
  - methodology: test-driven-development
description: "Test-driven development workflow using vertical slices (tracer bullets). Enforces behavior-first testing through public interfaces. Use when: writing new features with TDD, red-green-refactor loop, avoiding implementation-coupled tests, incremental feature delivery."
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
  inspired_by: mattpocock/skills
---

# TDD Workflow

## One-Liner

Drive feature development with tests that describe behavior — one tracer bullet at a time, never bulk-first.

---

## § 1 · Core Philosophy

Tests verify **behavior through public interfaces**, not implementation details. Code can be rewritten entirely; well-written tests should survive that rewrite.

**The critical anti-pattern: horizontal slicing.**
Writing all tests first, then all implementation, produces tests written against imagined behavior — they fail on contact with reality. Don't do it.

**The correct pattern: vertical slices (tracer bullets).**
Write one test → implement the minimum to pass it → repeat. Each cycle uses real learning from the previous one.

---

## § 2 · Workflow

### Phase 1 — Plan

Before writing any code:

1. Confirm the public interface (function signatures, HTTP endpoints, component props) with the user
2. List prioritized behaviors from most critical to least
3. Identify what "done" looks like for each behavior

**Gate:** Interface agreed. Behavior list approved. No code written yet.

### Phase 2 — Tracer Bullet

1. Write **one** test describing the first behavior
2. Test must:
   - Call a public interface (not internal functions)
   - Assert on observable output (not internal state)
   - Read like a specification ("given X, when Y, then Z")
3. Run the test — confirm it **fails** for the right reason
4. Write the minimal implementation to make it pass
5. Run again — confirm green

**Gate:** Test is green. Test would survive a complete rewrite of the implementation.

### Phase 3 — Incremental Loop

Repeat Phase 2 for each behavior in priority order:

```
for each behavior:
  → write test (public interface, behavior assertion)
  → confirm red (right reason)
  → implement minimum
  → confirm green
  → micro-refactor if obvious duplication
```

Never write more than one failing test at a time.

### Phase 4 — Refactor

After all behaviors are covered:

1. Extract duplication into well-named helpers
2. Deepen modules: if a function does two conceptually separate things, split it
3. Rerun all tests — must stay green
4. If a refactor breaks a test, the test was coupled to implementation; fix the test

---

## § 3 · Test Quality Checklist

Before marking any test done, verify:

| Check | Pass Condition |
|-------|---------------|
| Public interface | Test calls the outward-facing API, not internals |
| Behavior assertion | Asserts what the system does, not how |
| Survives refactor | A complete internal rewrite would leave this test green |
| Reads like spec | A reader unfamiliar with the code can understand the intent |
| One behavior | Each test asserts exactly one behavior |

---

## § 4 · When to Use This Skill

**Use when:**
- Adding a new feature to an existing codebase
- Building a module from scratch with known requirements
- Fixing a bug (write a failing test for the bug first)
- Pair-programming with an agent on incremental delivery

**Do NOT use when:**
- Exploring an unfamiliar codebase (use `zoom-out` first)
- The interface is entirely unknown (use `grill-with-docs` first to clarify)
- Writing tests for existing untested code (use `debug-diagnose` to stabilize first)

---

## § 5 · Relationship to Other Skills

| Skill | When to reach for it |
|-------|---------------------|
| `zoom-out` | Before starting — map the codebase context |
| `debug-diagnose` | When a test catches a bug mid-cycle |
| `architecture-review` | After a feature ships — assess if new code introduced shallow modules |
| `to-prd` | To convert the behavior list into a tracked issue |
