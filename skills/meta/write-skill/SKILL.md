---
name: write-skill
kind: workflow
version: 1.0.0
tags:
  - domain: meta
  - subtype: write-skill
  - methodology: skill-authoring
description: "Meta-skill for creating high-quality SKILL.md files. Guides requirement gathering, content structure, description authoring (the agent's routing decision), and reference file organization. Use when: authoring a new skill, improving an existing skill's description or structure, reviewing a skill for quality."
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
  inspired_by: mattpocock/skills
---

# Write a Skill

## One-Liner

The description field is your agent's only routing signal — get it right first, then write the content.

---

## § 1 · Core Insight

When an agent decides which skill to load, it reads the **description field** and nothing else. If the description is vague, the wrong skill gets loaded. If it is missing trigger language, the skill never loads at all.

**Everything else matters less.** A brilliant skill body attached to a weak description is effectively invisible to agents.

---

## § 2 · Workflow

### Phase 1 — Requirements Gathering

Before writing anything, answer:

1. **What capability does this skill provide?** (one sentence)
2. **When should it trigger?** (list 3–5 concrete user intents)
3. **What does it produce?** (artifact, behavior change, decision)
4. **Does it need executable scripts or just text instructions?**
   - Scripts: deterministic, repeatable operations where errors need explicit handling
   - Text: guidance, methodology, persona
5. **What skills is it composable with?** (list existing skills it pairs with)
6. **What skills overlap with it?** (how is this different from those?)

### Phase 2 — Write the Description First

The description must:

| Requirement | Detail |
|-------------|--------|
| State capability | What the skill provides in plain English |
| Include "Use when:" | Explicit trigger list (comma-separated intents) |
| Stay under 400 chars | Long descriptions get truncated by agent runtimes |
| Use third-person voice | "Guides the agent to..." not "Guide the agent to..." |
| Avoid vague verbs | Not "helps with X" — instead "executes X, produces Y" |

**Template:**
```
<What it does in one clause>. <What it produces>. Use when: <intent 1>, <intent 2>, <intent 3>.
```

**Example (weak):**
> "Helps with debugging and fixing bugs in code."

**Example (strong):**
> "Structured six-phase debugging workflow centered on building a reliable feedback loop before theorizing. Use when: debugging hard-to-reproduce issues, performance regression, mysterious failures, agent-assisted root cause analysis."

### Phase 3 — Draft the Skill Body

Structure the `SKILL.md` as follows:

```markdown
---
[frontmatter]
---

# Skill Name

## One-Liner
[Single sentence — the elevator pitch]

---

## § 1 · Core Philosophy / Purpose
[Why this skill exists. What mental model it instills.]

## § 2 · Workflow
[Step-by-step. Each phase has a clear gate/done condition.]

## § 3 · [Domain-specific section]
[Checklists, reference tables, heuristics]

## § 4 · When to Use This Skill
[Explicit "Use when" and "Do NOT use when" lists]

## § 5 · Relationship to Other Skills
[Skill pairing table]
```

**Line budget:** Keep the main `SKILL.md` under 200 lines. If it exceeds this, move sections to `references/` files and link them.

### Phase 4 — Organize Reference Files

Split content into `references/` when:
- The section is long but only needed occasionally (scenario examples, deep how-to)
- The section contains multiple distinct domains
- The main file exceeds 200 lines

Reference files are loaded **on demand** — they do not increase the token cost of every skill activation.

### Phase 5 — User Review

Present the draft description first. Ask: "Does this capture when an agent should load this skill?"

Only proceed to the full body review after the description is approved.

---

## § 3 · Description Quality Checklist

| Check | Pass | Fail |
|-------|------|------|
| Capability clear | "Structured debugging workflow" | "Helps with bugs" |
| Trigger language | Contains "Use when:" | No trigger language |
| Under 400 chars | ✓ | Exceeds limit |
| Third-person | "Guides the agent" | "Guide the agent" |
| Specific verb | "executes", "produces", "converts" | "helps", "assists" |
| No overlapping skills | Differentiated from similar skills | Identical description to another |

---

## § 4 · Frontmatter Reference

```yaml
name: kebab-case-id          # required; matches folder name
kind: persona|workflow|tool|template|composite   # required
version: 1.0.0               # required
description: "..."           # required; the routing signal
tags:
  - domain: <category>
  - subtype: <role-or-workflow>
  - methodology: <approach>  # for workflow skills
license: MIT
```

For `kind: workflow` skills — use present-tense imperative verbs in phase titles ("Build the loop", "Map the modules").  
For `kind: persona` skills — use declarative identity statements ("You are a...").

---

## § 5 · When to Use This Skill

**Use when:**
- Authoring a new skill from scratch
- Improving a skill that agents are failing to load correctly
- Reviewing a skill contribution for quality
- Teaching someone the SKILL.md format

**Do NOT use when:**
- Installing an existing skill (use the install guide)
- Searching for a skill to use (browse the catalog)
