---
name: debug-diagnose
kind: workflow
version: 1.0.0
tags:
  - domain: engineering
  - subtype: debug-diagnose
  - methodology: structured-debugging
description: "Structured six-phase debugging workflow centered on building a reliable feedback loop before theorizing. Use when: debugging hard-to-reproduce issues, performance regression, mysterious failures, agent-assisted root cause analysis, systematic bug fixing."
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
  inspired_by: mattpocock/skills
---

# Debug & Diagnose

## One-Liner

Build a fast, deterministic, agent-runnable pass/fail signal first — the bug is 90% fixed once you have that.

---

## § 1 · Core Philosophy

**The critical insight:** If you have a fast, deterministic, agent-runnable pass/fail signal for the bug, you will find the cause. Without it, you are guessing.

Most debugging fails not because the engineer lacks knowledge, but because they skip directly to hypotheses without first establishing a reproducible signal. Build the loop, then let the loop drive everything else.

---

## § 2 · The Six Phases

### Phase 1 — Build a Feedback Loop

Create the fastest reproducible test signal you can. Options in order of preference:

1. **Unit test** — isolates the exact failing condition
2. **Integration test** — exercises the real subsystem path
3. **CLI script** — passes known-bad input, asserts known-bad output
4. **REPL session** — interactive exploration to narrow the search space
5. **Fuzz input** — for non-deterministic or data-dependent failures

**Key constraints:**
- Must be runnable by the agent without human interaction
- Must produce pass/fail, not just "looks wrong"
- Must be deterministic (same input → same result)

Be aggressive and creative. Refuse to give up. A slow loop is better than no loop; a noisy loop can be narrowed.

**Gate:** You have a script/test that reproducibly demonstrates the failure.

### Phase 2 — Reproduce

Run the loop and confirm it demonstrates **exactly** the reported failure — not a nearby issue, not a similar symptom.

If the loop shows a different failure than reported:
- You have found a second bug (note it, don't pursue it now)
- Continue narrowing until the loop matches the report precisely

**Gate:** Loop output matches the failure description word-for-word.

### Phase 3 — Hypothesize

Before touching any code, generate **3–5 ranked hypotheses**. Each must be:

- **Falsifiable** — a specific, testable prediction
- **Ranked** — order by likelihood given what you know
- **Independent** — don't let one hypothesis assume another is true

Write them down. Do not skip this step even if one hypothesis feels obvious — the obvious hypothesis is frequently wrong.

### Phase 4 — Instrument

Test hypotheses in ranked order. For each:

1. Add **targeted** instrumentation at the relevant boundary (not blanket logging)
2. Use a debugger or tagged log output, not `print`-everywhere
3. Run the feedback loop
4. Does the output confirm or falsify the hypothesis?

Stop when one hypothesis is confirmed. Remove instrumentation from all falsified hypotheses immediately to keep signal clean.

**Anti-pattern:** Adding instrumentation for all hypotheses at once. You lose the ability to read the signal.

### Phase 5 — Fix + Regression Test

1. Write a test **at the appropriate architectural seam** that fails because of the bug — before writing the fix
2. Implement the minimal fix
3. Confirm: feedback loop is now green, new regression test is green, existing tests still green
4. If the fix required touching more than one module, consider whether the modules should be decoupled

### Phase 6 — Cleanup + Post-Mortem

1. Remove all debug instrumentation
2. Verify the feedback loop test is committed (it is now a permanent regression guard)
3. Document findings:
   - Root cause in one sentence
   - Why the bug was not caught earlier
   - What architectural change (if any) would prevent the class of bug

---

## § 3 · Quick Reference

```
Phase 1: BUILD THE LOOP (deterministic, agent-runnable, pass/fail)
Phase 2: REPRODUCE (confirm the loop shows exactly the reported failure)
Phase 3: HYPOTHESIZE (3-5 ranked, falsifiable hypotheses — written down)
Phase 4: INSTRUMENT (targeted, one hypothesis at a time)
Phase 5: FIX + REGRESSION TEST (test first, then fix)
Phase 6: CLEANUP + POST-MORTEM (remove debug code, document root cause)
```

---

## § 4 · When to Use This Skill

**Use when:**
- A bug is hard to reproduce or intermittent
- A performance regression appeared without obvious cause
- The same bug keeps recurring
- An agent is stuck in a "try random things" loop
- You need to present root cause analysis to stakeholders

**Do NOT use when:**
- The bug is a typo or trivially obvious from the error message
- You need to design a new feature (use `to-prd`)
- The codebase is unfamiliar — run `zoom-out` first

---

## § 5 · Relationship to Other Skills

| Skill | When to reach for it |
|-------|---------------------|
| `zoom-out` | Unfamiliar codebase — map it before Phase 1 |
| `tdd-workflow` | Once the bug is fixed — retrofit the regression test into the test suite |
| `architecture-review` | Post-mortem reveals a structural issue |
