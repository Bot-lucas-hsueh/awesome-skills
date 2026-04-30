## § 4 · Core Philosophy

### 4.1 The Test Pyramid Architecture

```
                    ╱─────────────╲
                   ╱   E2E Tests   ╲        ← 5-10%
                  ╱  [Playwright/     ╲          Critical user journeys
                 ╱   Cypress/WebDriver]  ╲         Slow, expensive, valuable
                ╱─────────────────────────╲
               ╱    Integration Tests      ╲     ← 20-25%
              ╱   [TestContainers/Pact/       ╲      Service boundaries,
             ╱    Supertest/REST-assured]      ╲     DB interactions, contracts
            ╱───────────────────────────────────╲
           ╱          Unit Tests                 ╲  ← 65-75%
          ╱      [Jest/pytest/JUnit/Vitest]       ╲   Fast, focused,
         ╱─────────────────────────────────────────╲   edge cases, logic
        ╱        Static Analysis & Linting           ╲ ← Foundation
       ╱     [ESLint/TypeCheck/Security Scans]        ╲   Fastest feedback
      ╱─────────────────────────────────────────────────╲
```

**Pyramid Principles:**
- **Foundation First**: Maximum unit tests for immediate feedback and precise failure isolation
- **Integration Layer**: Verify component interactions, API contracts, and data flows
- **E2E Sparingly**: Only for critical paths that justify maintenance cost
- **Anti-Patterns**: The "ice cream cone" (many E2E, few unit) = slow, brittle, untrusted

### 4.2 The 7 Immutable QA Principles

1. **Quality is Built In, Not Inspected In** — Testing is a team sport, not a phase handoff
2. **Test Behavior, Never Implementation** — Tests must survive refactoring; public API over private methods
3. **Flaky Tests Are Worse Than No Tests** — A 90% passing test lies 10% of the time; quarantine immediately
4. **Shift Left Relentlessly** — Find defects in requirements, not production — cost increases 10x per stage
5. **Non-Functional Is Functional** — Performance, security, accessibility are first-class requirements
6. **Fast Feedback Wins** — Tests that run frequently catch issues early; slow tests are skipped tests
7. **Measurement Enables Improvement** — Baseline everything: coverage, flakiness, escape rate, MTTR

---
