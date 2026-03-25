# Create Reference

> Full creation workflow, system prompt design, tier templates, and SOPs.

---

## Tier Selection

Choose tier first — it determines every downstream decision.

| Tier | Lines | References | Scope | Example |
|------|-------|-----------|-------|---------|
| **Lite** | 50–150 | 0–2 files | 1 function | dice roller, file converter |
| **Standard** | 150–500 | 3–8 files | 2–5 capabilities | data analyst, code reviewer |
| **Enterprise** | 500–1500 | 9–21 files | 5+ capabilities | strategic consultant, CTO |

**Selection rules**:
- Start with Lite. Upgrade only if the domain genuinely requires more depth.
- If you're unsure between tiers, pick the lower one and let scope drive expansion.
- A 600-line Lite skill is always a mistake — restructure with progressive disclosure.

---

## 6-Phase Creation Workflow

| Phase | Objective | Duration | Done | Fail |
|-------|-----------|----------|------|------|
| 1. Assess | Select tier, understand scope | 5 min | Tier confirmed, entry point set | Scope ambiguous |
| 2. Architecture | Design §1.1/1.2/1.3, plan structure | 15 min | Blueprint complete, disclosure split planned | Missing sections |
| 3. Content | Write system prompt + domain knowledge | 60–120 min | All sections filled, no generic content | Generic terms remain |
| 4. Examples | Create 5 detailed scenarios | 30 min | 5 scenarios with realistic data | < 5, or shallow |
| 5. Validation | Self-evaluate against 6-dimension rubric | 15–30 min | Score ≥ 9.0, variance < 1.0 | Score < 8.5 |
| 6. Delivery | Package files, write report | 10 min | All files ready, EVALUATION_REPORT.md saved | Missing files |

---

## System Prompt Design (§1.1 / §1.2 / §1.3)

The System Prompt accounts for **20% of the total score**. Missing any section caps the score at ≤ 7.0.

### §1.1 — Identity & Worldview

Define who the skill *is*, not what it does.

```markdown
### § 1.1 · Identity & Worldview

You are a **[Role Title]**, specialized in [specific domain].

**Professional DNA**:
- [Specific expertise 1]: [What makes it unique — real methodology, company, framework]
- [Specific expertise 2]: [Quantified capability — "20K token context", "99.9% uptime SLA"]
- [Specific expertise 3]: [Domain-specific lens — not "professional", but "ex-Goldman Sachs credit analyst"]

**Your Context**:
- [Key constraint or operating environment]
- [Specific tools, frameworks, or methods used]
- [Success metric that defines good output]
```

**Avoid**: "You are an expert with 20+ years of experience." → Generic, adds nothing.
**Use**: "You are a McKinsey engagement manager with 12 years of Fortune 500 restructuring." → Specific.

### §1.2 — Decision Framework

Define how the skill makes choices, especially under ambiguity.

```markdown
### § 1.2 · Decision Framework

**Priority Hierarchy**:
1. [Highest priority — e.g., data accuracy over speed]
2. [Second — e.g., user's stated goal over inferred goal]
3. [Third — e.g., completeness over brevity]
4. [Fourth — e.g., standard approach over creative]

**When inputs conflict**: [Explicit tie-breaking rule]
**When scope is unclear**: [Ask vs. assume — state which]
**When quality vs. speed trade-off**: [Explicit default]
```

### §1.3 — Thinking Patterns

3–5 named patterns that describe how the skill reasons. Use code blocks for tree/flow formats.

```markdown
### § 1.3 · Thinking Patterns

**Pattern 1: [Name]**
```
[Pseudocode or decision tree showing the pattern]
```

**Pattern 2: [Name]**
[Prose explanation of the reasoning approach]
```

---

## Progressive Disclosure Rules

| What belongs in SKILL.md | What belongs in references/ |
|--------------------------|------------------------------|
| Navigation tables | Full scoring rubrics |
| Phase summaries (1–2 lines) | Step-by-step SOPs |
| Key framework names | Detailed framework explanations |
| 1-sentence examples | Full example transcripts |
| Anti-pattern names | Anti-pattern explanations |

**Test**: If removing a section from SKILL.md would break the skill's navigation, it stays. Otherwise, move it.

---

## Pre-Delivery Checklist

```
[ ] §1.1 Identity — specific, not generic
[ ] §1.2 Decision Framework — priority hierarchy defined
[ ] §1.3 Thinking Patterns — 3+ named patterns
[ ] Domain Knowledge — real numbers, no "best practices"
[ ] Workflow — 4–6 phases with explicit Done/Fail criteria
[ ] 5+ Examples — realistic data, edge cases included
[ ] Anti-Patterns — named failures with solutions
[ ] Progressive Disclosure — SKILL.md ≤ 300 lines
[ ] Metadata — agentskills-spec compliant, description ≤ 1024 chars
[ ] Validation — dual-track score ≥ 9.0, variance < 1.0
[ ] EVALUATION_REPORT.md — saved alongside SKILL.md
```

---

## Entry Points by Level

| Level | Command | What Happens |
|-------|---------|--------------|
| Beginner | `start beginner` | Guided walkthrough, one section at a time, 30 min |
| Quick | `start quick` | Lite tier only, minimal structure, 15 min |
| Standard | `start standard` | Full 6-phase flow, Standard tier, 1–2 hrs |
| Expert | `start expert` | Enterprise tier, full progressive disclosure, 2+ hrs |

---

## Data-Driven Content Rules

Generic → Specific replacements:

| Generic (avoid) | Specific (use) |
|-----------------|----------------|
| "industry-leading solution" | "top-3 market position per Gartner 2024" |
| "proven methodology" | "McKinsey 7-S framework" |
| "significant improvement" | "16.7% error reduction over 3 sprints" |
| "20+ years experience" | "ex-Principal Engineer, Stripe payments infra" |
| "best practices" | "Google SRE error budget policy" |

Every claim needs a source, number, or named methodology. Vague claims are scored at ≤ 4/10.
