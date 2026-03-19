# Skill Writer — Standard Workflow

Load this file when starting any create / review

---

## 8.0 Skill Category Taxonomy

Classify the skill before writing. Best skills belong to exactly one category; confused skills span two or more.

| # | Category | Signal | Key Contents |
|---|----------|--------|--------------|
| 1 | **Library / API Reference** | "Claude uses X wrong" | Gotchas list + reference code snippets |
| 2 | **Product Validation** | "Verify output is correct" | Test driver scripts + state assertions |
| 3 | **Data Fetching & Analysis** | "Query our data" | Credentials, table names, common query patterns |
| 4 | **Business Process / Automation** | "Automate recurring workflow" | Delta-only output + execution log file |
| 5 | **Code Scaffolding / Templates** | "Generate boilerplate" | Template files in `assets/` + scripts |
| 6 | **Code Quality / Review** | "Enforce standards" | Adversarial subagent + deterministic scripts |
| 7 | **CI/CD / Deploy** | "Ship code safely" | Progressive rollout + auto-rollback hooks |
| 8 | **Operations Runbook** | "Debug an incident" | Tool→query map, structured report template |
| 9 | **Infrastructure Ops** | "Routine maintenance" | Safety guards + confirmation gates |

---

## 8.1 Creating a New Skill

```
Phase 1: Discovery  [✓ Done: one-sentence scope + named tier target agreed]
├── What category does this skill fall into? → §8.0 table; reject if spans ≥2 categories
├── What domain? Who is the target user? → shapes §1 Role + §2 Capabilities
├── What specific problems does this skill solve? → shapes §3 Risks + §12 Scope
├── What existing skills overlap? (check /skills/) → shapes §11 Integration
├── Does this skill need hooks? → on-demand PreToolUse/PostToolUse guards (see §8.4)
└── What quality tier is the goal? → sets §7.1 threshold
✗ FAIL: Cannot answer all 5 in ≤2 sentences → scope too broad; apply Anti-Pattern #1

Phase 2: Architecture  [✓ Done: skeleton with all 16 H2 headers + 1-line purpose per section]
├── Define the system prompt (role + thinking patterns + style) → §1
├── Identify 3-5 core capabilities → §2
├── Map domain frameworks and decision tools → §7
├── Design multi-phase workflow → §8
├── Plan 2+ scenario examples → §9
├── Identify gotchas (Claude's common failure points) → §10
└── Plan folder structure: scripts/, references/, assets/, config.json if setup needed
✗ FAIL: Cannot identify ≥2 domain-specific decision frameworks → consult domain expert before writing

Phase 3: Writing  [✓ Done: all 16 sections complete; no placeholder or TBD content]
├── Fill complete metadata (all 9 fields; no HTML comments in YAML description) → §7.2
├── Write system prompt in code block → use §1 of SKILL.md as exemplar
├── Build each of the 16 sections in correct order → standards.md §7.3
├── No bilingual labels in headings/tables; no HTML comments → standards.md §7.4
└── Include concrete examples showing AI applying frameworks → scenarios.md
✗ FAIL: Any section contains "TBD" or placeholder text → complete or narrow scope before submitting

Phase 4: Quality Assurance  [✓ Done: rubric score ≥ tier target + litmus test passes]
├── Score against Quality Rubric → standards.md §7.1; target ≥7.0 (Expert), ≥9.0 (Exemplary)
├── Validate YAML metadata → yamllint; check all 9 fields
├── Confirm all 16 sections present → standards.md §7.3
├── Run anti-pattern scan → anti-patterns.md; check all 9 patterns
└── Litmus test: Prompt AI with vs. without skill on 3 tasks
    PASS = AI cites ≥1 framework AND uses different structure in ≥2/3 tasks
    FAIL = identical structure in ≥2/3 tasks OR 0 frameworks cited
✗ FAIL: Litmus test shows no behavioral difference → skill is Basic regardless of rubric score
```

---

## 8.2 Reviewing & Scoring a Skill

```
Step 1: Read the complete skill file
Step 2: Score each of the 6 Quality Rubric dimensions (1-10) → standards.md §7.1
Step 3: Calculate weighted average → determine tier
Step 4: Identify top 3 weaknesses by impact
Step 5: Provide rewrite suggestions with before/after examples
Step 6: Give classification and upgrade path
```

---

## 8.3 Upgrading Basic → Expert

```
From Basic to Expert, add in priority order (ROI table → standards.md §7.6):

☐ Structured System Prompt (role + thinking patterns + communication style)
☐ Deep Domain Frameworks (decision matrices with thresholds, not just lists)
☐ Scenario-Based Guidance (2-3 full conversation examples → scenarios.md)
☐ Complete Metadata (all 9 fields; no HTML in YAML description)
☐ Domain-Specific Risks (4+ with severity classification)
☐ Gotchas section populated from real Claude failure points (not generic pitfalls)
☐ Quality Score Verification (weighted avg ≥ 7.0 via standards.md §7.1)
```

---

## 8.4 Hook-Aware Skills

Skills can register on-demand hooks that activate for the session. Use hooks when:
- The check is opinionated and users shouldn't always run it
- You need to intercept tool calls before execution (PreToolUse)
- You need to post-process output (PostToolUse)

```
Hook Design Pattern:
├── Declare in SKILL.md description: "Registers a PreToolUse hook when invoked"
├── Include hook script in scripts/hooks/ folder
├── Trigger condition: specific to this skill (avoid broad matchers)
└── Provide /disable-<skill-name> or session-scoped — never permanent by default

Examples:
  /careful  → PreToolUse: intercepts rm -rf, DROP TABLE, force-push
  /freeze   → Blocks Edit/Write outside a specified directory
  /review   → PostToolUse: runs adversarial subagent after each file write
```

**Hook best practices:**
- Narrow matchers only — broad hooks cause friction and get disabled
- State what the hook does in the skill description (users need to know what they're activating)
- Store hook config in `config.json` if users need to customize match patterns

---

## 8.6 Design Pattern Selection

Before writing §8 of any new skill, run the pattern selection gate:

```
Gate: What structural pattern does this skill follow?
→ Reference: references/design-patterns.md §DP.0 (decision matrix)

Tool Wrapper  → "Claude uses X wrong" signal; build references/gotchas.md; no output template
Generator     → output consistency problem; build assets/template.md + references/style-guide.md
Reviewer      → auditing against criteria; build references/review-checklist.md (swappable)
Inversion     → need user info before acting; build phase-gated question bank; hard stop gates
Pipeline      → order is safety-critical; every step needs PREREQ / DONE / BLOCK

✗ FAIL: No pattern selected → apply Anti-Pattern #10
✗ FAIL: Pattern selected but §8 uses flat prose list → restructure §8 to match pattern template
```

**Pattern composition (when multiple patterns apply):**
```
Generator + Inversion  → Phase 1-2: collect vars (Inversion) → Phase 3: fill template (Generator)
Pipeline + Reviewer    → each Pipeline gate includes Reviewer checklist evaluation
Inversion + Pipeline   → Phase 1-2: discovery (Inversion) → Phase 3+: execution (Pipeline)
```

---

## 8.7 Skill Lifecycle & Audit

```
Skill Audit Cadence (from Anthropic engineering practice):
├── Add "last invoked" date to §15 Version History after each meaningful run
├── Audit every 2 weeks: skills not invoked → candidate for retirement or merge
├── Signal: if nobody uses a skill after 30 days post-publish → scope or trigger problem
└── Retire to `archive/` rather than delete; mark with "⚠️ Archived: [reason]" in CATALOG.md

Skill Inflation Prevention:
├── Each skill must have a unique trigger that no other skill covers
├── Two skills with 80%+ overlapping triggers → merge or specialize one
└── Prefer one Expert skill over three Basic skills covering the same domain

Skill Distribution:
├── Repo-bundled (./.claude/skills/) → small team, few repos, low management overhead
├── Plugin marketplace → large team, self-service install, let useful skills surface naturally
└── Sandbox folder first → test traction before promoting to marketplace
```

---

## 8.5 Config & Memory Patterns

**Initial Setup (config.json):**
```
If skill needs user context (channel, project, credentials):
├── Check if config.json exists in skill directory
├── If missing: ask user for required fields → write config.json
├── On subsequent runs: read config.json silently
└── Example fields: {"slack_channel": "#eng", "team": "platform"}
```

**Persistent Memory:**
```
Use ${CLAUDE_PLUGIN_DATA}/<skill-name>/ for data that must survive skill upgrades.
Use skill directory only for ephemeral/session data.

Patterns by complexity:
  Simple  → append-only .log file (standup history, execution trace)
  Medium  → JSON file with keyed entries
  Complex → SQLite database (queryable history, multi-table)
```
