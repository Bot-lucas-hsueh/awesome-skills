# Skill Writer — Design Patterns

Load this file when selecting a structural pattern for a new skill, reviewing whether the right pattern is applied, or composing multiple patterns.

---

## DP.0 Pattern Selection Decision Matrix

Before writing §1, answer these questions to determine the correct pattern:

| Question | YES → Consider | NO → Eliminate |
|----------|---------------|----------------|
| Does the skill wrap a library/framework to teach domain-specific rules? | Tool Wrapper | — |
| Does the skill enforce consistent output format from variable inputs? | Generator | — |
| Does the skill evaluate existing work against a checklist? | Reviewer | — |
| Does the skill need user input before it can act meaningfully? | Inversion | — |
| Does the skill execute a multi-step workflow where order is safety-critical? | Pipeline | — |
| Does the skill need both consistent output AND pre-flight questions? | Generator + Inversion | — |
| Does the skill run a workflow AND audit each step? | Pipeline + Reviewer | — |

**Tiebreaker rule:** If two patterns seem equally valid, pick the one whose "failure mode" is less costly for your use case.

---

## DP.1 Tool Wrapper

**Core idea:** Teach the agent domain knowledge on demand. The skill is a knowledge delivery vehicle, not a workflow engine.

**Trigger signal:** "Claude uses X wrong" / "team keeps making the same mistake with Y library"

**Mechanism:**
- Package library/framework gotchas, idioms, and non-obvious rules into the skill
- Agent loads domain docs only when the relevant tool/library is detected in context
- Keyword monitoring drives dynamic loading — avoids polluting context with unrelated rules

**Structure:**
```
§1 System Prompt     → Role as {library} expert; monitoring keywords that trigger activation
§7 Standards         → Gotchas list + correct usage patterns (dense tables, not prose)
§8 Workflow          → Phase 1: Detect usage → Phase 2: Surface relevant rules → Phase 3: Verify output
§9 Examples          → Side-by-side: wrong usage ↔ correct usage with explanation
§10 Gotchas          → Accumulated real failure cases; Claude's default wrong-guesses for this library
```

**Anthropic Iron Law applied:** Write only what Claude doesn't already know — skip basics, focus on non-obvious footguns.

**Folder structure:**
```
skills/{category}/{skill-name}/
├── SKILL.md
└── references/
    ├── gotchas.md        ← non-obvious traps; keyword-indexed
    ├── patterns.md       ← correct usage idioms
    └── quick-ref.md      ← API cheat sheet / decision table
```

**Quality test:** Remove the skill. Does Claude make ≥1 mistake in the domain? Re-add it. Does Claude avoid that mistake? If YES to both → skill works.

---

## DP.2 Generator

**Core idea:** Guarantee consistent output format by separating template from content. The skill acts as a project manager filling a form.

**Trigger signal:** "Output is inconsistent" / "different agents produce different formats for the same thing"

**Mechanism:**
- Template stored in `assets/` (fill-in-the-blank structure)
- Style guide stored in `references/` (rules for tone, terminology, formatting)
- SKILL.md §8 defines the fill-order and variable collection steps
- Agent must ask for missing variables before generating — never guess

**Structure:**
```
§1 System Prompt     → Role as format enforcer; never generate without all variables
§7 Standards         → Variable definitions, required vs optional fields, validation rules
§8 Workflow          → Step 1: Load template → Step 2: Read style guide → Step 3: Collect missing vars → Step 4: Fill and output
§9 Examples          → Full before/after: raw input + filled template output
```

**Inversion gate (mandatory):** List all required variables in §8. Before generating, confirm each variable is collected or declared optional.

**Folder structure:**
```
skills/{category}/{skill-name}/
├── SKILL.md
├── assets/
│   ├── template.md       ← output skeleton with {{variable}} placeholders
│   └── style-guide.md    ← tone, terminology, formatting rules
└── references/
    └── variables.md      ← field definitions, validation constraints
```

**Anti-pattern to avoid:** Guessing missing variables silently → output looks correct but contains wrong assumptions. Force explicit collection.

---

## DP.3 Reviewer

**Core idea:** Separate the review logic (SKILL.md) from the review criteria (checklist file). Swapping the checklist changes what is audited — same infrastructure.

**Trigger signal:** "Review this" / "check for compliance with X" / "audit against Y standard"

**Mechanism:**
- SKILL.md defines HOW to review (severity classification, output format, escalation triggers)
- Checklist lives in `references/review-checklist.md` (WHAT to check)
- Swapping checklists enables Python style → OWASP security → GDPR compliance → same skill

**Structure:**
```
§1 System Prompt     → Role as auditor; always read checklist before evaluating; always classify by severity
§7 Standards         → Severity levels (Critical / High / Medium / Low / Info) with definitions
§8 Workflow          → Step 1: Load checklist → Step 2: Evaluate each item → Step 3: Group by severity → Step 4: Output structured report
§9 Examples          → Sample checklist item + evaluation output showing severity classification
```

**Output format requirement (mandatory):**
```
## Critical
- [item]: [finding] → [fix]

## High
- [item]: [finding] → [fix]

## (lower severities follow same pattern)
```

**Folder structure:**
```
skills/{category}/{skill-name}/
├── SKILL.md
└── references/
    ├── review-checklist.md      ← swappable; defines WHAT to check
    ├── severity-guide.md        ← defines Critical/High/Medium/Low criteria
    └── report-template.md       ← output structure
```

**Power move:** Create multiple checklist files (e.g., `checklist-security.md`, `checklist-style.md`, `checklist-perf.md`) and switch by user command. One Reviewer skill → N audit types.

---

## DP.4 Inversion

**Core idea:** Reverse the default agent behavior (act on assumptions) to interview-first, act-after. The agent becomes an interviewer.

**Trigger signal:** "Plan this project" / "help me architect X" / "I need to build Y" (complex enough that acting on assumptions wastes effort)

**Mechanism:**
- Agent must complete ALL discovery questions before any generation begins
- Questions grouped into phases; each phase has a gate condition
- Explicit gating instruction: "Do NOT proceed to [next phase] until [condition] is confirmed"
- No skipping, no guessing, no partial completion

**Structure:**
```
§1 System Prompt     → Role as interviewer; explicit prohibition: never generate until all phases complete
§8 Workflow          → Phase 1: Context questions (gate: all answered) → Phase 2: Constraint questions (gate: all answered) → Phase 3: Generation
§9 Examples          → Full interview flow showing agent asking, user answering, then generation
```

**Gate instruction template:**
```
Phase 1: Discovery
- Ask: [list of required questions]
✗ STOP: Do not proceed to Phase 2 until all Phase 1 questions are answered with specific, non-vague responses.
```

**Anti-pattern to avoid:** Asking all questions in one message block → user skips some → agent proceeds anyway. Use sequential phase gates, not a question dump.

**Folder structure:**
```
skills/{category}/{skill-name}/
├── SKILL.md
└── references/
    ├── question-bank.md      ← all discovery questions, organized by phase
    └── template.md           ← output template loaded AFTER phases complete
```

---

## DP.5 Pipeline

**Core idea:** Enforce strict execution order with hard checkpoints. No step starts until the previous step is confirmed complete. Safety through mandatory sequencing.

**Trigger signal:** "Complex task that cannot safely skip steps" / "multi-stage workflow" / "needs verification between stages"

**Mechanism:**
- Each step has a defined prerequisite (precondition)
- Each step has a defined exit condition (what "done" means)
- Hard gate between steps: agent must confirm completion before advancing
- Failure at any gate stops the pipeline; no silent fallthrough

**Structure:**
```
§1 System Prompt     → Role as pipeline executor; never advance without gate confirmation; never skip steps
§8 Workflow          → Step 1 [PREREQ: X] → [✓ DONE: Y confirmed] → Step 2 [PREREQ: Y confirmed] → ...
§9 Examples          → Full pipeline run showing gate confirmations and a blocked gate scenario
```

**Step definition template:**
```
Step N: [Action]
  PREREQ: [what must exist/be confirmed before this step runs]
  ACTIONS: [what this step does]
  ✓ DONE: [measurable completion criterion]
  ✗ BLOCK: [what causes this step to halt; escalation path]
```

**Folder structure:**
```
skills/{category}/{skill-name}/
├── SKILL.md
└── references/
    ├── pipeline-steps.md     ← full step definitions with PREREQ/DONE/BLOCK
    ├── gate-criteria.md      ← what counts as passing each gate
    └── rollback-guide.md     ← how to undo each step if needed
```

**Hook opportunity:** Pipeline skills are prime candidates for PreToolUse hooks that enforce gate conditions at the tool-call level — not just at the conversational level.

---

## DP.6 Pattern Composition

Patterns are not mutually exclusive. Common high-value combinations:

| Combination | When to Use | How to Combine |
|-------------|-------------|----------------|
| **Generator + Inversion** | Output must be consistent AND requires user-specific variables | Add Inversion phases (DP.4) before Generator's template fill step |
| **Pipeline + Reviewer** | Multi-stage workflow where each stage output must pass quality gates | Add Reviewer step as the final (or per-stage) Pipeline gate |
| **Tool Wrapper + Generator** | Library-specific output that must follow a consistent format | Tool Wrapper surfaces the rules; Generator enforces the format |
| **Inversion + Pipeline** | Complex workflow requiring both discovery and strict execution | Phase 1-2 Inversion (discovery), Phase 3+ Pipeline (execution) |

**Composition rule:** When combining, the primary pattern defines §8 Workflow structure. The secondary pattern adds a phase or gate within the primary workflow.

**Token warning:** Combining 3+ patterns → skill body likely exceeds 500 lines. Apply References-First aggressively; keep SKILL.md as index only.

---

## DP.7 Anthropic's 3 Iron Laws

From Anthropic engineering practice — the foundation beneath all pattern choices:

### Law 1: Write Only What Claude Doesn't Know

```
❌ Include: "Always write clean, readable code"
✅ Include: "This library's `connect()` call is synchronous on init but async on reconnect —
            Claude defaults to treating both as async, causing silent data loss"
```

Test: Read each sentence. Would Claude behave correctly without it? If YES → delete it.

### Law 2: Prioritize the Pitfall List

```
❌ "Best practices for working with X"
✅ "Top 7 mistakes teams make with X (collected from production incidents)"
```

Gotchas (§10) are the highest-ROI section. Real failure cases, not generic advice. Each gotcha should name the specific wrong assumption Claude makes, not just the correct behavior.

### Law 3: Give Tools, Not Instructions

```
❌ "When reviewing code, check for security issues, performance issues,
    and maintainability issues, then provide feedback."

✅ references/review-checklist.md  ← 40 specific items with severity classifications
   references/severity-guide.md    ← criteria for Critical vs High vs Medium
   assets/report-template.md       ← exact output structure
```

The best skill is a toolbox, not a prompt. Instructions tell; tools constrain. Tools are verifiable; instructions are interpretable.

---

## DP.8 Pattern Anti-Patterns

| Anti-Pattern | Pattern Violated | Consequence | Fix |
|--------------|-----------------|-------------|-----|
| **No pattern** — all logic in system prompt | All | System prompt bloats; behavior unpredictable | Apply DP.0 decision matrix; select one primary pattern |
| **Wrong pattern** — Generator for sequential safety workflow | Pipeline | Steps can be skipped when output "looks right" | Switch to Pipeline; use Generator only for format enforcement |
| **Inversion without gates** — all questions in one dump | Inversion | User skips questions; agent proceeds on incomplete info | Add explicit ✗ STOP gate after each phase |
| **Pipeline without BLOCK** — no failure criteria | Pipeline | Silent failure; pipeline continues on bad output | Define ✗ BLOCK condition for every step |
| **Reviewer without swappable checklist** — hardcoded rules | Reviewer | Cannot reuse infrastructure for different audit types | Externalize checklist to `references/review-checklist.md` |
| **Tool Wrapper with basics** — includes obvious content | Tool Wrapper | Dilutes signal; wastes tokens on what Claude already knows | Apply Iron Law 1: delete anything Claude knows without the skill |
