# Competitive Analysis: Skill Management Tools

**Scope**: AI skill lifecycle management — creation, evaluation, quality assurance
**Date**: 2026-03-25
**Analyst**: neo.ai

---

## 1. Competitors Surveyed

| Tool | Owner | Source |
|------|-------|--------|
| **skill-creator** | Anthropic | [anthropics/skills](https://github.com/anthropics/skills) |
| **agentskills-ref** | agentskills | [agentskills/agentskills](https://github.com/agentskills/agentskills) |
| **skill-manager** (this skill) | neo.ai | theneoai/awesome-skills |

---

## 2. Feature Matrix

| Capability | skill-creator | agentskills-ref | skill-manager |
|------------|:---:|:---:|:---:|
| **Skill creation workflow** | ❌ | ❌ | ✅ Tier-based (Lite/Standard/Enterprise) |
| **System prompt design guide** | ❌ | ❌ | ✅ §1.1/1.2/1.3 methodology |
| **Text quality evaluation** | ❌ | ❌ | ✅ 6-dimension rubric |
| **Runtime quality evaluation** | ❌ | ❌ | ✅ 6-dimension runtime rubric |
| **Skill restoration methodology** | ❌ | ❌ | ✅ 7-step methodology |
| **agentskills spec validation** | ❌ | ✅ `skills-ref validate` | ✅ `scripts/validate.sh` |
| **Automated scoring** | ❌ | ❌ | ✅ `scripts/score.sh` (heuristic) |
| **Evaluation runner** | ✅ Automated | ❌ | ✅ Interactive (`scripts/eval.sh`) |
| **Certification suite** | ❌ | ❌ | ✅ `scripts/certify.sh` |
| **Eval query testing** | ✅ Parallel | ❌ | ❌ Manual only |
| **Assertion grading (LLM)** | ✅ Automated | ❌ | ❌ Human-graded |
| **Trigger rate optimization** | ✅ Train/validation split | ❌ | ❌ Not implemented |
| **HTML benchmark report** | ✅ Live | ❌ | ❌ Markdown only |
| **evals.json support** | ✅ | ❌ | ❌ |
| **Progressive disclosure** | ❌ | ✅ Spec definition | ✅ Enforced by tools |
| **Dual-track (Text+Runtime)** | ❌ | ❌ | ✅ |

---

## 3. Detailed Comparison

### 3.1 skill-creator (Anthropic)

**Source**: Described in agentskills spec → [evaluating-skills.mdx](https://github.com/agentskills/agentskills/blob/main/docs/skill-creation/evaluating-skills.mdx)

**What it does**:
- Automates the full eval loop: runs evals, grades assertions, aggregates benchmarks, generates live HTML report
- Supports parallel eval execution across multiple test cases
- Implements train/validation split for trigger optimization (prevents description overfitting)
- Reads `evals/evals.json` as the standard eval format

**Strengths**:
- Fully automated — minimal human intervention
- Statistically rigorous: pass rate mean/stddev, delta vs baseline
- Description optimization loop with validation split
- HTML report with live updates

**Weaknesses**:
- Only covers the **evaluation/optimization** phase — no creation or restoration
- No quality rubric for skill content (only trigger rate and assertion pass rate)
- Treats skill quality as a binary pass/fail problem (assertion-based), not a dimensional score
- No guidance on *what to write* — only whether what's written works

**Best fit**: Teams that have already written skills and need to systematically test and tune their `description` field trigger rates.

---

### 3.2 agentskills-ref (agentskills.io)

**Source**: [agentskills/agentskills](https://github.com/agentskills/agentskills)

**What it does**:
- Defines the open format specification for SKILL.md files
- Provides `skills-ref validate` CLI to check frontmatter validity
- Documents the progressive disclosure model
- Platform-agnostic (works with Claude Code, VS Code Copilot, OpenAI Codex, etc.)

**Strengths**:
- Authoritative spec — what every other tool must conform to
- Minimal and precise: only validates what the spec defines
- Cross-platform compatibility

**Weaknesses**:
- Zero guidance on *content quality* — only structure
- No evaluation, scoring, or improvement tools
- No creation workflow or methodology
- `skills-ref validate` only checks syntax, not semantics

**Best fit**: Developers who want to publish skills and need spec compliance.

---

### 3.3 skill-manager (this skill)

**Strengths**:
- Only tool covering the **full lifecycle**: Create → Evaluate → Restore → Certify
- Unique **dual-track rubric**: Text Quality (6 dims) + Runtime Quality (6 dims)
- **Restoration methodology** (7-step) has no equivalent in any competitor
- **Tier system** (Lite/Standard/Enterprise) provides structured creation paths
- **Shell scripts** give repeatable, auditable workflows
- agentskills spec compliant via `validate.sh`

**Weaknesses vs skill-creator**:
- Evaluation is **interactive/human-driven** — not automated
- No `evals.json` support — cannot run assertion-based evals programmatically
- No **trigger rate testing** — description optimization is manual
- No **HTML report** — outputs Markdown only
- No **parallel test execution** — each eval run is sequential

**Best fit**: skill authors who need end-to-end guidance — from writing a new skill to restoring a low-quality one. Teams where human judgment in the loop is preferred.

---

## 4. Quality & Performance Benchmarks

### 4.1 Evaluation Depth

| Metric | skill-creator | agentskills-ref | skill-manager |
|--------|:---:|:---:|:---:|
| Dimensions assessed | ~2 (trigger + assertions) | 0 | 12 (6 text + 6 runtime) |
| Automation level | High | Medium | Low (interactive) |
| Human judgment required | Low | Low | High |
| Reproducibility | High (scripted) | High | Medium (human scorer variance) |

### 4.2 Scope Coverage

| Phase | skill-creator | agentskills-ref | skill-manager |
|-------|:---:|:---:|:---:|
| Pre-creation (planning) | ❌ | ❌ | ✅ |
| Creation (writing) | ❌ | ❌ | ✅ |
| Spec validation | ❌ | ✅ | ✅ |
| Content quality scoring | ❌ | ❌ | ✅ |
| Runtime testing | Partial (assertions) | ❌ | ✅ |
| Description optimization | ✅ | ❌ | ❌ |
| Restoration/repair | ❌ | ❌ | ✅ |
| Certification | ❌ | ❌ | ✅ |

### 4.3 Time-to-Quality Estimate

Starting from a zero-quality skill (5/10 text):

| Approach | Time to 8.0/10 | Manual effort |
|----------|---------------|---------------|
| skill-creator only | N/A (doesn't improve content) | — |
| agentskills-ref only | N/A (doesn't improve content) | — |
| skill-manager (restore + eval) | 2–4 hrs | High |
| skill-manager + skill-creator | 3–5 hrs | Medium |

---

## 5. Gap Analysis — What skill-manager Is Missing

### Gap 1: Automated Eval Queries (P0)

**Problem**: Description trigger rate is critical (skill-creator addresses this). A skill with a perfect rubric score but a weak description will never activate.

**Needed**: `evals/evals.json` support + `scripts/trigger-test.sh` that runs the skill against a query set and computes trigger rate.

**Effort**: Medium — requires agent invocation, not just file inspection.

### Gap 2: Assertion-Based Grading (P1)

**Problem**: skill-manager's eval.sh relies on human scoring. For teams running many skills, this doesn't scale.

**Needed**: `scripts/grade.sh` that takes `evals/evals.json` assertions and uses an LLM to grade outputs.

**Effort**: High — requires LLM API integration.

### Gap 3: HTML Report (P2)

**Problem**: EVALUATION_REPORT.md is Markdown. skill-creator produces live HTML with pass-rate charts.

**Needed**: `scripts/report.sh` that converts EVALUATION_REPORT.md to HTML with visualizations.

**Effort**: Low — straightforward templating.

### Gap 4: Benchmark Comparison (P2)

**Problem**: No way to compare skill versions (before/after restoration) with statistical rigor.

**Needed**: `scripts/benchmark.sh` that computes delta between two EVALUATION_REPORT.md files.

**Effort**: Low — file parsing + diff output.

---

## 6. Recommended Integration

For highest coverage, use **skill-manager + skill-creator** together:

```
WRITE  →  skill-manager (create.md + validate.sh + score.sh)
SCORE  →  skill-manager (eval.sh — dual-track rubric)
TUNE   →  skill-creator (trigger rate optimization, evals.json)
SHIP   →  skill-manager (certify.sh)
```

skill-manager handles *content quality*; skill-creator handles *description effectiveness*. They are complementary, not competing.

---

## 7. Roadmap Recommendations

| Priority | Feature | Effort | Value |
|----------|---------|--------|-------|
| P0 | `scripts/trigger-test.sh` — eval query trigger rate | Medium | High — closes biggest gap vs skill-creator |
| P0 | `evals/evals.json` template in references/ | Low | High — enables structured eval workflow |
| P1 | `scripts/grade.sh` — LLM assertion grading | High | Medium — replaces human grading for text dimensions |
| P2 | `scripts/benchmark.sh` — before/after comparison | Low | Medium — quantifies restoration impact |
| P2 | `scripts/report.sh` — HTML report generation | Low | Low — cosmetic improvement |

---

*Analysis based on: agentskills specification v1.0 (2026-03), Anthropic skill-creator documentation, skill-manager v1.0.0*
