---
name: example-skill                             # Lowercase, hyphen-separated
display_name: Example Expert Skill
author: your-id                                  # Author identifier
version: 1.0.0                                   # Semantic versioning (MAJOR.MINOR.PATCH)
difficulty: expert|intermediate|beginner         # Skill complexity level
category: category-name                          # Must match a /skills/ subdirectory
tags: [tag1, tag2, tag3]                         # 3-5 searchable tags
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  [Invoke when: exact trigger condition]. [What the skill does — measurable output].
  Triggers: "keyword1", "keyword2", "keyword3"
  Works with: Claude Code, OpenAI Codex, Kimi Code, OpenCode, Cursor, Cline, OpenClaw.
---

<!-- description tip: The model scans `description` to decide IF to activate this skill.
     Write as "invoke when [exact condition]", not as a summary of what the skill does.
     Front-load the primary trigger verb in the first 50 chars. Keep ≤263 chars. -->

# Example Expert Skill

---

## 1. System Prompt

### 1.1 Role Definition

```
You are a senior [role] with [X]+ years of experience in [domain].

**Identity:**
- [Credential or background that establishes authority]
- [Key specialization or focus area]
- [Distinctive methodology or approach]

**Writing Style:**
- [Communication trait 1]: [brief description]
- [Communication trait 2]: [brief description]
- [Communication trait 3]: [brief description]

**Core Expertise:**
- [Expertise area 1]: [what it means in practice]
- [Expertise area 2]: [what it means in practice]
- [Expertise area 3]: [what it means in practice]
```

### 1.2 Decision Framework

Before responding in this domain, evaluate:
| Gate| Question| Fail Action|
|-------------|----------------|----------------------|
| **[Gate 1]** | [Decision question] | [Concrete action if failed] |
| **[Gate 2]** | [Decision question] | [Concrete action if failed] |
| **[Gate 3]** | [Decision question] | [Concrete action if failed] |

### 1.3 Thinking Patterns

| Dimension| [Role] Perspective|
|-----------------|---------------------------|
| **[Dimension 1]** | [How this expert thinks — concrete, not generic] |
| **[Dimension 2]** | [How this expert thinks — concrete, not generic] |
| **[Dimension 3]** | [How this expert thinks — concrete, not generic] |

### 1.4 Communication Style

- **[Style trait 1]**: [Description with concrete example]
- **[Style trait 2]**: [Description with concrete example]
- **[Style trait 3]**: [Description with concrete example]

---

## 2. What This Skill Does

1. **[Capability 1]** — [Specific, measurable change in AI output — not generic]
2. **[Capability 2]** — [description]
3. **[Capability 3]** — [description]
4. **[Capability 4]** — [description]

---

## 3. Risk Disclaimer

| Risk| Severity| Description| Mitigation|
|------------|-----------------|-------------------|---------------------|
| **[Risk 1]** | 🔴 High | [Domain-specific risk — NOT generic "AI may be wrong"] | [Concrete mitigation with specific action] |
| **[Risk 2]** | 🔴 High | [Domain-specific risk] | [Concrete mitigation] |
| **[Risk 3]** | 🟡 Medium | [Domain-specific risk] | [Concrete mitigation] |
| **[Risk 4]** | 🟢 Low | [Domain-specific risk] | [Concrete mitigation] |

**⚠️ IMPORTANT:**
- [Domain-specific warning — describes a real consequence, not a generic disclaimer]
- [Domain-specific warning]

---

## 4. Core Philosophy

### 4.1 [Core Framework Name]

```
[ASCII diagram, decision tree, or scoring matrix showing the domain's core mental model.
 ≤ 5 levels / decision nodes. Example: pyramid, 2×2 matrix, phase-gate flow.]
```

[One sentence: how the components relate and when each applies.]

### 4.2 Guiding Principles

1. **[Principle 1]**: [Explanation with concrete, domain-specific application]
2. **[Principle 2]**: [Explanation with concrete application]
3. **[Principle 3]**: [Explanation with concrete application]

---

## 5. Platform Support

| Platform| Session Install| Persistent Config|
|----------------|--------------------------|-------------------------------|
| **OpenCode** | `/skill install [skill-name]` | Auto-saved to `~/.opencode/skills/` |
| **OpenClaw** | `Read [URL] and install as skill` | Auto-saved to `~/.openclaw/workspace/skills/` |
| **Claude Code** | `Read [URL] and install as skill` | Append to `~/.claude/CLAUDE.md` (global) |
| **Cursor** | Paste §1 into `.cursorrules` | Save to `~/.cursor/rules/[skill-name].mdc` (global) |
| **OpenAI Codex** | Paste §1 into system prompt | `~/.codex/config.yaml` → `system_prompt:` |
| **Cline** | Paste §1 into Custom Instructions | Append §1 to `.clinerules` (project) |
| **Kimi Code** | `Read [URL] and install as skill` | Append to `.kimi-rules` |

**[URL]:** `https://awesome-skills.dev/skills/[category]/[skill-name].md`

---

## 6. Professional Toolkit

| Tool| Purpose|
|------------|---------------|
| **[Tool 1]** | [Specific purpose — when and why to use this tool] |
| **[Tool 2]** | [Specific purpose] |
| **[Tool 3]** | [Specific purpose] |
| **[Framework or Standard]** | [How it applies in this domain] |

---

## 7. Standards & Reference

### 7.1 [Domain] Frameworks

| Framework| When to Use| Key Steps|
|-----------------|----------------------|-------------------|
| **[Framework 1]** | [Trigger: what problem it solves] | [1. Step → 2. Step → 3. Step → Output] |
| **[Framework 2]** | [Trigger] | [1. Step → 2. Step → Output] |
| **[Framework 3]** | [Trigger] | [1. Step → 2. Step → Output] |

### 7.2 [Domain] Metrics

| Metric| Formula| Target|
|--------------|--------------|---------------|
| **[Metric 1]** | [Specific formula or calculation] | [Concrete target: e.g., ">95%", "<200ms", "3:1 ratio"] |
| **[Metric 2]** | [Formula] | [Target with unit] |
| **[Metric 3]** | [Formula] | [Target] |

---

## 8. Standard Workflow

### 8.1 [Primary Task Name]

```
Phase 1: [Discovery / Research / Assessment]
├── [Step with what information to gather]
├── [Step with specific question to answer]
└── [Step with deliverable or checkpoint]

Phase 2: [Design / Planning / Analysis]
├── [Step with template or tool to use]
├── [Step with decision to make]
└── [Step with output to produce]

Phase 3: [Execution / Delivery / Implementation]
├── [Step]
├── [Step]
└── [Final checkpoint: what "done" looks like]
```

### 8.2 [Secondary Task Name]

```
Step 1: [Description — specific action, not generic]
Step 2: [Description]
Step 3: [Description with expected output]
```

### 8.3 Initial Setup (if needed)

```
If config.json not found in skill directory:
├── Ask user for: [required field 1], [required field 2]
├── Write to skill-dir/config.json: {"field1": value, "field2": value}
└── Confirm setup complete; proceed with main workflow

On subsequent runs: read config.json silently, no prompts.
```

### 8.4 On-Demand Hooks (if applicable)

```
Hooks registered when this skill is invoked (session-scoped, not permanent):
├── Hook type: PreToolUse / PostToolUse / [other]
├── Trigger pattern: [specific matcher — narrow scope]
├── Action: [what the hook does]
└── Script: scripts/hooks/[hook-name].sh

To disable: [disable command or restart session]
```

> Skip §8.3–§8.4 if skill needs no setup or hooks.

---

## 9. Scenario Examples

### 9.1 [Scenario: Primary Use Case]

**User:** "[Realistic trigger request]"

**[Role Name]:**
> **[Framework applied from §7]:** [Expert framing — not generic advice]
>
> | [Decision Column] | [Data/Score] | [Recommendation] |
> |-------------------|-------------|-----------------|
> | [Option A] | [metric] | [action] |
>
> **Next I need:** [Clarifying question showing expert judgment]

### 9.2 [Scenario: Edge Case or Anti-Pattern Correction]

**User:** "[Different request type — tests a second capability]"

**[Role Name]:**
> **[Different framework from §7]:** [Expert-level insight — domain-specific, not generic]
> 1. [Actionable step with domain rationale]
> 2. [Actionable step]

---

## 10. Gotchas & Anti-Patterns

> **Gotchas** = Claude's observed failure points when using this skill. Update this section as new failures are discovered — this is the most information-dense part of any skill.

| # | Gotcha / Anti-Pattern | Severity | Fix |
|---|----------------------|----------|-----|
| 1 | **[Real failure Claude made]** | 🔴 High | [Specific corrective instruction] |
| 2 | **[Real failure Claude made]** | 🟡 Medium | [Fix] |
| 3 | **[Edge case or wrong default]** | 🟢 Low | [Fix] |

```
❌ [Claude's actual wrong behavior in this domain]
✅ [Correct behavior — domain-specific, observed from real runs]
```

---

## 11. Integration with Other Skills

| Combination| Workflow| Result|
|-------------------|-----------------|--------------|
| [This Skill] + **[Complementary Skill]** | [Step 1: This skill does X → Step 2: Other skill does Y] | [Specific outcome] |
| [This Skill] + **[Complementary Skill]** | [Workflow description] | [Specific outcome] |
| [This Skill] + **[Complementary Skill]** | [Workflow description] | [Specific outcome] |

---

## 12. Scope & Limitations

**✓ Use this skill when:**
- [Specific use case 1 — concrete trigger condition]
- [Specific use case 2]
- [Specific use case 3]

**✗ Do NOT use this skill when:**
- [Excluded case 1] → use `[alternative-skill-name]` skill instead
- [Excluded case 2] → use `[alternative-skill-name]` skill instead
- [Excluded case 3] → [reason why this skill doesn't apply + alternative]

---

## 13. How to Use This Skill

### Quick Install
```
Read https://awesome-skills.dev/skills/[category]/[skill-name].md and install as skill
```

### Persistent Install (Claude Code)
```bash
# Global — applies to all projects
echo "Read https://awesome-skills.dev/skills/[category]/[skill-name].md and apply [skill-name] skill." >> ~/.claude/CLAUDE.md

# Project-level
echo "Read https://awesome-skills.dev/skills/[category]/[skill-name].md and apply [skill-name] skill." >> ./CLAUDE.md
```

### Trigger Words
- "[trigger word 1]"
- "[trigger word 2]"
- "[trigger word 3]"
- "[trigger word 4]"

---

## 14. Quality Verification

Full checklist: `references/standards.md §7.10` — Critical blocking checks:
| Check| Blocks Merge? |
|--------------|---------------|
| ☐ All 9 metadata fields; no HTML in YAML description; description ≤ 263 chars | ✅ Yes |
| ☐ All 16 H2 sections in correct order; no TBD/placeholder content | ✅ Yes |
| ☐ §5: all 7 platforms; session + persistent options; `[URL]` defined below table | ✅ Yes |
| ☐ Weighted rubric score ≥ 7.0 (Expert) / ≥ 9.0 (Exemplary) | ✅ Yes |
| ☐ Zero self-inconsistencies; no filler; every line earns its token cost | ✅ Yes |

### Test Cases

**Test 1: [Primary Capability]**
```
Input: "[Representative user request]"
Expected: [Expert-level response — frameworks applied, domain-specific recommendations]
```

**Test 2: [Secondary Capability]**
```
Input: "[Different type of request]"
Expected: [Expert-level response characteristics]
```

**Self-Score:** [X.X/10 — Tier] — Justification: [brief evidence]

---

## 15. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | YYYY-MM-DD | Initial release |

---

## 16. License & Author

MIT with Attribution — Full terms, community links: [COMMON.md](../../COMMON.md)

| Field| Details|
|-------------|---------------|
| **Author** | [Your name or handle] |
| **Contact** | [Email or GitHub] |
| **GitHub** | [GitHub profile URL] |

**Author**: [name] <[email]> | **License**: MIT with Attribution
