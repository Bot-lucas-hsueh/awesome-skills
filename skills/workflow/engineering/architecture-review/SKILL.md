---
name: architecture-review
kind: workflow
version: 1.0.0
tags:
  - domain: engineering
  - subtype: architecture-review
  - methodology: module-depth-analysis
description: "Codebase architecture review using module depth analysis. Surfaces shallow modules, tight coupling, and locality violations. Proposes deepening opportunities. Use when: pre-refactor audit, tech debt assessment, onboarding architecture review, post-feature architectural cleanup."
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
  inspired_by: mattpocock/skills
---

# Architecture Review

## One-Liner

Surface architectural friction by finding shallow modules, poor locality, and tight coupling — then propose targeted deepening opportunities.

---

## § 1 · Vocabulary

| Term | Definition |
|------|-----------|
| **Module** | Any unit with an interface and an implementation (function, class, service, file) |
| **Depth** | How much behavior a module provides per unit of interface complexity. Deep = lots of behavior, simple interface. Shallow = little behavior, complex or leaky interface |
| **Seam** | The boundary where an interface lives; a place where behavior can shift without editing callers |
| **Locality** | The degree to which a change, bug, or piece of knowledge is concentrated in one place. High locality = one place to change. Low locality = scattered across files |
| **Deepening opportunity** | A refactor that increases module depth or locality without changing externally observable behavior |

---

## § 2 · Workflow

### Phase 1 — Establish Context

Before reviewing code, read:
1. `CONTEXT.md` (domain glossary) — understand canonical terms
2. ADRs in `docs/adr/` or `decisions/` — understand past trade-offs
3. `README.md` — understand stated architectural intent

You are looking for the gap between **stated** architecture and **actual** architecture.

### Phase 2 — Explore for Friction

Walk the codebase noting friction points. For each area, ask:

**Shallow module signals:**
- Does this function/class have a large, complex interface relative to the behavior it encapsulates?
- Would a caller need to know implementation details to use this correctly?
- The "deletion test": if you deleted this module and pushed its logic into callers, would callers become more complex? If yes, the module earns its keep. If no, it is shallow.

**Locality violations:**
- When one concept changes, how many files must change?
- Is business logic scattered across multiple layers (controller + service + model all contain business rules)?
- Are there parallel hierarchies that must be kept in sync?

**Coupling signals:**
- Can you test this module without standing up a large portion of the system?
- Does changing an internal data structure require changing callers?
- Are there untested paths because the module cannot be isolated?

### Phase 3 — Present Candidates

For each friction point found, produce a candidate entry:

```
### Candidate: <short name>

Files involved: <list>
Friction: <what makes this painful today>
Solution: <plain English — what changes>
Benefit: <how locality or depth improves>
Risk: <what could go wrong>
Effort: <S / M / L>
```

Present all candidates to the user before doing any work. Let the user prioritize.

### Phase 4 — Grill Loop

For the selected candidate(s), walk the design collaboratively:

1. Ask one question at a time about the proposed change
2. If a term is ambiguous, resolve it and update `CONTEXT.md`
3. Offer to create an ADR if and only if all three conditions hold:
   - **Hard to reverse**: meaningful cost to change later
   - **Surprising without context**: future reader will wonder "why?"
   - **Genuine trade-off**: real alternatives existed
4. Once design is agreed, implement the deepening

---

## § 3 · Module Depth Scoring (Quick Heuristic)

Rate each candidate module on a 1–5 scale for:

| Dimension | 1 (shallow) | 5 (deep) |
|-----------|------------|---------|
| Interface complexity | Many params, leaky internals | Single call, self-contained |
| Behavior per call | Does little | Does a lot |
| Testability | Requires entire system | Tested in isolation |
| Locality | Scattered knowledge | All knowledge in one place |
| Stability | Interface changes often | Interface rarely changes |

Modules scoring ≤ 2 on average are strong deepening candidates.

---

## § 4 · Common Deepening Patterns

| Pattern | When to apply |
|---------|--------------|
| **Extract value object** | Primitive obsession — raw strings/numbers carry domain meaning |
| **Introduce domain event** | Multiple callers react to state changes via polling or callbacks |
| **Consolidate business rule** | Same validation or decision logic exists in N places |
| **Invert dependency** | Module A knows too much about Module B's internals; introduce an interface |
| **Introduce façade** | Callers orchestrate complex subsystem sequences they shouldn't care about |

---

## § 5 · When to Use This Skill

**Use when:**
- Preparing for a significant refactor
- Onboarding to a new codebase to assess its health
- After shipping a feature — check if the code introduced new architectural debt
- Tech debt sprint planning

**Do NOT use when:**
- The codebase is being actively rewritten (wait for a stable snapshot)
- The task is a single-file change (overkill)

---

## § 6 · Relationship to Other Skills

| Skill | When to reach for it |
|-------|---------------------|
| `zoom-out` | Run first — map the terrain before reviewing it |
| `tdd-workflow` | After identifying a deepening candidate — write tests before refactoring |
| `debug-diagnose` | If a shallow module is masking bugs, diagnose first |
| `to-prd` | Convert the candidate list into tracked issues |
