# Skill Writer — Standards & Reference

Full reference for §7 of the Skill Writer skill. Load this file when you need to:
- Score a skill against the Quality Rubric (§7.1)
- Verify required metadata fields (§7.2)
- Check the 16-section compliance (§7.3)
- Apply bilingual, file organization, or promotion rules (§7.4–§7.6)
- Calibrate content density (§7.7)
- Follow Agent Skills standard (§7.8)
- Optimize token budgets (§7.9)

---

## 7.1 Skill Quality Rubric

| Dimension| Weight | Basic (1-3) | Community (4-6) | Expert (7-8) | Exemplary (9-10) |
|----------|--------|-------------|-----------------|--------------|------------------|
| **System Prompt Depth** | 20% | 1-2 sentence role description | Role + capabilities + style | Structured prompt with decision framework + thinking patterns | Adds domain-specific heuristics and communication nuances that are distinct from any other role |
| **Domain Knowledge Density** | 25% | Generic descriptions anyone could write | Domain-specific tools and processes | Deep frameworks + quantified metrics + real scenarios | Decision trees with specific thresholds; domain jargon used with precision; all metrics include target ranges |
| **Workflow Actionability** | 15% | 3-step abstract process | Phased with sub-steps | Each step has templates, examples, and checkpoints | Each phase references specific sections; measurable output test in final phase; failure criteria defined |
| **Risk Documentation** | 10% | 1-2 generic risks ("AI may be wrong") | 3-4 domain risks + mitigation | Risk matrix with severity + domain-specific mitigation | 5+ risks with escalation triggers + example consequences; edge cases and adjacent domain risks covered |
| **Example Quality** | 20% | None or trivial | 1-2 basic scenarios | Multi-scenario + full conversation flows + edge cases | 3+ full flows covering different use cases; at least one flow explicitly corrects an anti-pattern |
| **Metadata Completeness** | 10% | name + version only | + description + triggers | All 9 fields: name, display_name, author, version, difficulty, category, tags, platforms, description | All 9 fields + description has role, triggers, and works-with statement; version history has 3+ entries |

**Weighted Score Formula:**
```
Score = (System Prompt × 0.20) + (Domain Knowledge × 0.25) + (Workflow × 0.15)
      + (Risk Docs × 0.10) + (Examples × 0.20) + (Metadata × 0.10)

Example: 8×0.20 + 7×0.25 + 6×0.15 + 8×0.10 + 9×0.20 + 10×0.10 = 7.85 → Expert
```

**Scoring Rules:**
- **1-3 → Basic**: Template filled, structure present, content thin. Needs major work.
- **4-6 → Community**: Solid content, domain-specific, tested by users. Good foundation.
- **7-8 → Expert ⭐**: Deep frameworks, scenario guidance, measurably improves AI output.
- **9-10 → Exemplary ⭐⭐**: Gold standard; maximally specific on every dimension.
- **Weighted average determines tier.** A skill with 9/10 on metadata but 2/10 on examples is NOT Expert.

---

## 7.2 Required Metadata Fields

```yaml
---
name: skill-slug-name                    # Lowercase, hyphen-separated; max 64 chars
display_name: English Name
author: contributor-id                   # Author identifier
version: 1.0.0                           # Semantic versioning (MAJOR.MINOR.PATCH)
quality: basic                           # basic / community / expert / exemplary
difficulty: expert|intermediate|beginner
category: category-name                  # Must match a /skills/ subdirectory
tags: [tag1, tag2, tag3]                 # 3-5 searchable tags
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  [Role description]. Use when [trigger conditions].
  Triggers: "keyword1", "keyword2"
  Works with: Claude Code, OpenAI Codex, Kimi Code, OpenCode, Cursor, Cline, OpenClaw.
---
```

**Note**: Do not include `<!-- HTML comments -->` inside the YAML `description` field.

---

## 7.3 16-Section Checklist

| # | Section| Expert Hallmark|
|---|---------|-----------------|
| 1 | **System Prompt** | Role + decision framework + thinking patterns + communication style |
| 2 | **What This Skill Does** | 3-5 specific, measurable capabilities |
| 3 | **Risk Disclaimer** | 4+ risks with severity and domain-specific mitigation |
| 4 | **Core Philosophy** | Guiding principles, decision models, frameworks |
| 5 | **Platform Support** | Platform-specific installation for all 7 platforms |
| 6 | **Professional Toolkit** | Categorized tools with specific names and purposes |
| 7 | **Standards & Reference** | Quality rubric, metadata spec, compliance checklists |
| 8 | **Standard Workflow** | 3+ phases with templates and checkpoints per step |
| 9 | **Scenario Examples** | 2+ full conversation flows showing framework application |
| 10 | **Common Pitfalls** | Anti-patterns with ❌/✅ contrasts and severity ratings |
| 11 | **Integration** | Cross-skill combination patterns with workflows |
| 12 | **Scope & Limitations** | Explicit "when NOT to use" with alternatives |
| 13 | **How to Use** | Install command + authoritative trigger word list |
| 14 | **Quality Verification** | Self-checklist + test cases + self-score table |
| 15 | **Version History** | Dated entries with scope of change |
| 16 | **License & Author** | MIT + attribution requirements + author contact |

---

## 7.4 Format Rules

- Primary content in English (AI-optimized)
- No bilingual labels in headings or table headers
- No `<!-- Chinese comments -->` in body (token waste with zero AI value)
- Semantic Chinese translations belong in code block examples only when teaching Chinese-speaker use cases

---

## 7.5 File Organization

| Domain| Categories|
|--------|------------|
| **Tech** | software/, ai-ml/, data/, cybersecurity/, blockchain/, quantum/, semiconductor/ |
| **Business** | executive/, finance/, marketing/, sales/, hr/, product/, freelancer/ |
| **Healthcare** | healthcare/, medical/, biotech/ |
| **Legal & Gov** | legal/, public-service/, government/ |
| **Creative** | creative/, content/, entertainment/, media/ |
| **Engineering** | manufacturing/, construction/, materials/, robotics/, aerospace/, automotive/ |
| **Services** | service-worker/, hospitality/, logistics/, transportation/, realestate/, retail/ |
| **Other** | special/, education/, research/, agriculture/, energy/, environmental/ |

Folder skills: `skills/{category}/{skill-name}/SKILL.md` (name must match folder).

---

## 7.6 Skill Promotion Decision Tree

```
Weighted Average ≥ 7.0?
├── NO → Expert NOT eligible
│   ├── Any H2 section missing? → Fix structure first → §7.3
│   ├── Score all 6 dimensions → fix the lowest-scoring first → §7.1
│   └── Domain Knowledge < 4? → Consult domain expert; do not publish
├── YES + any single dimension < 4? → BLOCK promotion; fix that dimension first
├── YES + all dimensions ≥ 4 + avg 7.0–8.9 → Expert Verified ⭐
│   └── Weighted Average ≥ 9.0 + all dimensions ≥ 7?
│       ├── YES → Exemplary ⭐⭐
│       └── NO → Expert ⭐ (identify lowest dimension; upgrade it first)
└── Two or more dimensions < 4 simultaneously → Reject; restart from `../assets/TEMPLATE.md`
```

**Dimension Fix Priority by ROI:**

| Fix This First | When Score Is | Max Weighted Gain |
|----------------|--------------|-------------------|
| **Example Quality** | 0 examples (score 1) | +1.8 pts (9 × 20%) |
| **System Prompt** | 1-2 sentence hook (score 2) | +1.4 pts (9 × 20%) |
| **Domain Knowledge** | Generic descriptions (score 2) | +1.75 pts (9 × 25%) |
| **Workflow** | No phases (score 2) | +1.05 pts (9 × 15%) |
| **Risk Docs** | < 3 risks (score 2) | +0.7 pts (9 × 10%) |
| **Metadata** | Missing ≥3 fields (score 2) | +0.7 pts (9 × 10%) |

---

## 7.7 Content Density Calibration

| Metric| Basic | Community | Expert ⭐ | Exemplary ⭐⭐ |
|--------------|-------|-----------|----------|--------------|
| **Total line count** | <100 | 100–300 | 300–600 | 600–900* |
| **System prompt length** | 1–5 lines | 5–15 lines | 15–30 lines | 30–50 lines + ≥2 decision frameworks |
| **Decision frameworks in §7** | 0 | 1 (no thresholds) | 2–3 (with metrics) | 4+ (each with numeric thresholds) |
| **Scenario flows in §9** | 0 | 1 partial | 2 full multi-turn | 3+ full, covering ≥2 distinct use cases |
| **Risk entries in §3** | 1–2 | 3–4 | 5–6 (severity rated) | 6+ (all with escalation triggers) |
| **Trigger words in §13** | 1–3 | 4–6 | 6–8 specific phrases | 6–8 (hard cap; >8 = false activation >50%) |

*Meta-skills: up to 900 lines. Domain skills: under 600.

**Signal-to-Token Efficiency:**
```
Efficiency = (Frameworks × 3) + (Flows × 5) + (Risks × 2)
             ─────────────────────────────────────────────
                            Total Lines ÷ 100

Target: ≥ 2.0 → Expert | ≥ 3.5 → Exemplary | < 1.0 → move prose to references/
```

---

## 7.8 Agent Skills Standard Compatibility

Per [anthropics/skills](https://github.com/anthropics/skills), a valid skill requires **only two fields**:

```yaml
name: skill-name          # kebab-case, max 64 chars, MUST match parent folder name
description: >            # max 1024 chars; PRIMARY trigger signal — make it "pushy"
  What this skill does and when to invoke it.
```

**Optional standard fields:** `compatibility` (required tools/deps), `when_to_use` (supplements description).

**Three-Level Progressive Disclosure:**

| Level | Content | Load Condition |
|-------|---------|----------------|
| **1. Metadata** | `name` + `description` only | Always in context (~100 tokens/skill) |
| **2. SKILL.md body** | Full instructions | When skill is invoked (≤ 500 lines) |
| **3. Bundled resources** | scripts/, references/, assets/ | Only when Claude reads them |

**Folder structure:**
```
skills/my-skill/
├── SKILL.md          ← entrypoint; name must match folder
├── scripts/          ← executable helpers (output-only token cost)
├── agents/           ← sub-agent files
├── references/       ← on-demand reference docs
└── evals/evals.json  ← test cases
```

---

## 7.9 Token Budget Optimization

### Budget 1 — Description Character Budget

Claude Code allocates **~15,500 characters** across ALL installed skills for `name` + `description`.

```
Per-skill overhead: 109 chars (XML) + description length
Typical (263 chars) → max ~42 skills visible
Skills over budget: COMPLETELY INVISIBLE (no warning)
```

| Skills Installed | Max Description | Rule |
|-----------------|----------------|------|
| < 40 | ≤ 263 chars | Full detail allowed |
| 40–60 | ≤ 150 chars | Trigger verbs only |
| 60+ | ≤ 130 chars | Front-load trigger in first 50 chars |

**Description rules:** Front-load trigger verbs · Be "pushy" (use imperative) · No HTML comments · State measurable outcome · Include 3–5 trigger phrases · Max 1024 chars

### Budget 2 — SKILL.md Body

| Metric | Limit | Cost If Exceeded |
|--------|-------|-----------------|
| SKILL.md body | ≤ 500 lines | Full file loads every invocation |
| Referenced files | Unlimited | Zero cost until read |
| Script files | Unlimited | Output-only token cost |

**References-First Principle:**
> SKILL.md = system prompt (§1) + section index (§2–§16 as 1-line pointers). All detail goes to `references/`.
> Every 10 lines removed from SKILL.md saves ~100 tokens **on every invocation**, permanently.

| Rule | Threshold | Action |
|------|-----------|--------|
| Move to `references/` | Non-§1 section >3 lines | Create `references/{section}.md`; replace with 1-line pointer |
| Keep in SKILL.md | §1 System Prompt + §2 capabilities (≤5 lines) | These drive AI behavior directly; offloading loses the effect |
| Section headers required | All 16 H2 sections must remain | Pointer lines count; section structure must be preserved |

**Offload priority order:**
1. Long reference tables, API specs, field enumerations
2. Extended examples beyond the 2 required for Expert tier
3. Edge case docs and troubleshooting guides
4. Core decision frameworks (keep in body)

**Description Precision Rule:**
> A description must match the exact trigger intent — no vague verbs, no padding.
> Test: Would this description activate the skill for a request it shouldn't handle? If yes, rewrite.

| Signal | Action |
|--------|--------|
| Vague opening ("helps with", "assists in") | Replace with specific verb phrase ("write", "review", "score") |
| Padded to fill char limit | Cut until every word earns its place; prefer 150–200 chars over padded 263 |
| Missing measurable outcome | Add: "returns [output]", "produces [artifact]", "classifies into [tiers]" |
| Trigger verbs buried after line 1 | Front-load: first 50 chars must contain primary trigger verb |

**Diagnostics:**
```bash
/context                                  # Check for excluded skills warning
SLASH_COMMAND_TOOL_CHAR_BUDGET=32000 claude  # Override budget
echo -n "your description" | wc -c       # Measure description length
```

---

## 7.11 Platform Installation Standards

Guidelines for writing an effective §5 Platform Support section.
### Install Command Matrix

| Platform| Session Install| Persistent Config|
|----------------|--------------------------|-------------------------------|
| **OpenCode** | `/skill install [skill-name]` | Auto-saved to `~/.opencode/skills/` |
| **OpenClaw** | `Read [URL] and install as skill` | Auto-saved to `~/.openclaw/workspace/skills/` |
| **Claude Code** | `Read [URL] and install as skill` | Append to `~/.claude/CLAUDE.md` (global) |
| **Cursor** | Paste §1 into `.cursorrules` | Save to `~/.cursor/rules/[skill].mdc` (global) |
| **OpenAI Codex** | Paste §1 into system prompt | `~/.codex/config.yaml` → `system_prompt:` field |
| **Cline** | Paste §1 into Custom Instructions | Append to `.clinerules` (project-level) |
| **Kimi Code** | `Read [URL] and install as skill` | Append to `.kimi-rules` |

**[URL]:** `https://awesome-skills.dev/skills/[category]/[skill-name].md`
**Raw URL (for curl):** `https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/[category]/[skill-name].md`

### Rules for §5

| Rule| Threshold| Why|
|------------|-----------------|-----------|
| Cover all 7 platforms | 0 missing | Missing platform = 0% install rate for those users |
| Show session + persistent path | Both per platform | Session-only = skill lost on restart |
| Use `[URL]` shorthand in table | Full URL only in §13 | Repeating 80-char URLs 3× wastes ~160 tokens |
| Paste-target must be §1 | For Cursor/Codex/Cline | Users need exact copy target, not vague "prompt" |
| No redundant instructions | One action per cell | Multi-step cells → use §13 for extended guide |

### Claude Code Persistent Install Snippet

Every skill's §13 should include this for Claude Code users:
```bash
# Global (all projects)
echo "Read [URL] and apply [skill-name] skill." >> ~/.claude/CLAUDE.md

# Project-level
echo "Read [URL] and apply [skill-name] skill." >> ./CLAUDE.md
```

### Token Budget for §5

- Target: ≤ 10 lines (header + 7 platform rows + [URL] note)
- Persistent install details → §13 or `references/` file
- Do NOT repeat the full URL for every Read-based platform; use `[URL]` in the table and define it once below

---

## 7.10 Quality Verification Checklist

| Check | Rubric Dimension |
|-------|-----------------|
| ☐ All 9 metadata fields present; no HTML comments in YAML description | Metadata Completeness |
| ☐ System Prompt defines role, decision framework, thinking patterns, communication style | System Prompt Depth |
| ☐ All 16 standard H2 sections present in correct order | Metadata Completeness |
| ☐ Risk disclaimer has 4+ domain-specific risks with severity + escalation triggers | Risk Documentation |
| ☐ At least 2 full conversation scenario flows | Example Quality |
| ☐ Workflow has 3+ phases with [✓ Done] criteria and ✗ FAIL blocks | Workflow Actionability |
| ☐ Domain frameworks have numeric thresholds — not generic lists | Domain Knowledge Density |
| ☐ English primary; Chinese in ``; `/` separator in table cells | (Format Standard) |
| ☐ No filler — every line earns its token cost | Domain Knowledge Density |
| ☐ Weighted average ≥ 7.0 for Expert ⭐; ≥ 9.0 for Exemplary ⭐⭐ | All dimensions |
| ☐ SKILL.md body ≤ 500 lines (folder skills) / ≤ 900 lines (meta-skill flat files) | Token Budget |
| ☐ Description ≤ 263 chars; no HTML comments; trigger verbs front-loaded | Token Budget |
| ☐ References-First: every non-§1 section >3 lines has been moved to `references/` | Token Budget |
| ☐ Description uses precise trigger verbs; no vague openers; measurable outcome stated | Token Budget |
| ☐ Zero self-inconsistencies: skill follows every rule it defines | System Prompt Depth |
