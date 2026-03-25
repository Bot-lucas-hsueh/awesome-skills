# Competitive Analysis: Skill Management Tools

**Scope**: AI skill lifecycle management — creation, evaluation, quality assurance
**Date**: 2026-03-25
**Analyst**: neo.ai
**Sources**: agentskills spec (fetched), anthropics/skills SKILL.md (~900 lines, fetched), Anthropic engineering blog, agentskills.io

---

## 1. Competitors Surveyed

| Tool | Owner | Stars | License | Source |
|------|-------|-------|---------|--------|
| **skill-creator** | Anthropic | 102k+ | Apache 2.0 | [anthropics/skills](https://github.com/anthropics/skills) |
| **agentskills-ref** | agentskills.io | — | — | [agentskills/agentskills](https://github.com/agentskills/agentskills) |
| **skill-manager** | neo.ai | — | MIT | theneoai/awesome-skills |

---

## 2. Product Overview

### skill-creator (Anthropic)

A ~900-line skill that automates the full skill lifecycle with emphasis on **measurable quality**:

**Core workflow** (Decide → Draft → Test → Evaluate → Improve → Repeat):
- **Create**: Interview-based intent capture; research-driven SKILL.md writing
- **Test**: Spawns parallel subagents — one with skill, one without (baseline) — captures token count and duration per run
- **Evaluate**: LLM-grades assertions from `evals/evals.json`; computes pass rate, mean/stddev, delta vs baseline
- **Improve**: Synthesizes failed assertions + execution transcripts → proposes SKILL.md changes
- **Description optimization**: 20-query eval set, train/validation split, automated trigger rate loop
- **Output**: Live HTML benchmark report + `benchmark.json`

**Platform support**: Claude.ai, Claude Code, Cowork, API
**Philosophy**: Real-world tasks first; evaluate before optimizing; generalize from feedback, not specific examples

### agentskills-ref (agentskills.io)

Reference implementation of the agentskills open format spec:
- `skills-ref validate ./skill-name` — checks frontmatter validity
- Defines progressive disclosure (3-level: metadata → body → resources)
- Platform-agnostic specification (works with VS Code Copilot, Claude Code, OpenAI Codex)
- No creation, evaluation, or improvement tooling

### skill-manager (this skill)

Unified lifecycle tool built on the neo.ai 6-dimension quality rubric:
- **Create**: Tier-based (Lite/Standard/Enterprise), §1.1/1.2/1.3 system prompt methodology
- **Evaluate**: Interactive dual-track scoring (6 text + 6 runtime dimensions), `EVALUATION_REPORT.md`
- **Restore**: 7-step methodology to bring 5-7/10 skills to 9.5/10
- **Tools**: `validate.sh` / `score.sh` / `eval.sh` / `certify.sh`

---

## 3. Feature Matrix

| Capability | skill-creator | agentskills-ref | skill-manager |
|------------|:---:|:---:|:---:|
| **CREATION** | | | |
| Intent capture / interviewing | ✅ Structured | ❌ | ❌ |
| Tier-based creation guide | ❌ | ❌ | ✅ Lite/Standard/Enterprise |
| System prompt methodology (§1.1/1.2/1.3) | ❌ | ❌ | ✅ |
| Template library | ✅ | ❌ | ✅ (references/create.md) |
| Progressive disclosure guide | ✅ 3-level spec | ✅ Spec definition | ✅ Enforced by scripts |
| **EVALUATION** | | | |
| Text quality rubric (dimensional) | ❌ | ❌ | ✅ 6 dimensions |
| Runtime quality rubric (dimensional) | ❌ | ❌ | ✅ 6 dimensions |
| Automated parallel eval runs | ✅ Subagents | ❌ | ❌ |
| Assertion-based grading (LLM) | ✅ | ❌ | ❌ |
| Token + timing benchmarks | ✅ | ❌ | ❌ |
| Interactive human evaluation | ❌ | ❌ | ✅ eval.sh |
| Heuristic pre-check | ❌ | ❌ | ✅ score.sh |
| **OPTIMIZATION** | | | |
| Description trigger rate testing | ✅ Train/validation split | ❌ | ❌ |
| Blind comparison | ✅ | ❌ | ❌ |
| Execution transcript analysis | ✅ | ❌ | ❌ |
| Skill restoration methodology | ❌ | ❌ | ✅ 7-step |
| **TOOLING** | | | |
| Spec validation | ❌ | ✅ skills-ref | ✅ validate.sh |
| HTML benchmark report | ✅ Live | ❌ | ❌ |
| Markdown evaluation report | ❌ | ❌ | ✅ EVALUATION_REPORT.md |
| Certification suite | ❌ | ❌ | ✅ certify.sh |
| evals.json support | ✅ | ❌ | ❌ |
| **PLATFORM** | | | |
| Claude.ai | ✅ | ✅ | ✅ |
| Claude Code | ✅ | ✅ | ✅ |
| VS Code Copilot | ❌ | ✅ | ✅ |
| OpenAI Codex | ❌ | ✅ | ✅ |

---

## 4. Quality & Performance Benchmarks

### 4.1 Evaluation Depth

| Metric | skill-creator | agentskills-ref | skill-manager |
|--------|:---:|:---:|:---:|
| Quality dimensions assessed | ~2 (trigger + assertions) | 0 | **12** (6 text + 6 runtime) |
| Automation level | High (subagents) | Medium (CLI) | Low (interactive) |
| Human judgment required | Low | Low | High |
| Reproducibility | High (deterministic script) | High | Medium (scorer variance ±0.5) |
| Token cost per eval | High (parallel runs) | None | Low |
| Time per eval | 5–20 min (automated) | Seconds | 5–60 min (manual) |

### 4.2 Scope Coverage

| Phase | skill-creator | agentskills-ref | skill-manager |
|-------|:---:|:---:|:---:|
| Pre-creation planning | ✅ Interview | ❌ | ✅ Tier selection |
| Writing guidance | ✅ Research-first | ❌ | ✅ §1.1/1.2/1.3 |
| Spec compliance | ❌ | ✅ | ✅ |
| Content quality scoring | ❌ | ❌ | ✅ 12 dimensions |
| Performance benchmarking | ✅ pass rate, tokens, time | ❌ | ❌ |
| Description optimization | ✅ Train/val split | ❌ | ❌ |
| Restoration / repair | ❌ | ❌ | ✅ 7-step |
| Production certification | ❌ | ❌ | ✅ |

### 4.3 Methodology Comparison

| Design Choice | skill-creator | skill-manager |
|--------------|---------------|--------------|
| Quality signal | Pass rate on human-written assertions | Dimensional score across 12 axes |
| Evaluation approach | Automated (LLM grades outputs) | Human-in-loop (interactive scoring) |
| Improvement loop | Synthesizes transcripts → proposes changes | Gap analysis → guided restoration |
| Description tuning | Systematic train/val split, 20 eval queries | Manual — no tooling |
| "Good skill" definition | Passes assertions + triggers reliably | Text ≥ 8.0, Runtime ≥ 8.0, Variance < 1.0 |
| Creation philosophy | Interview real users, do real tasks first | Tier selection → structured template |

---

## 5. Unique Differentiators

### skill-creator has, skill-manager lacks:
- **Automated parallel eval runs** — no human time required per iteration
- **Token + timing benchmarks** — quantify skill cost vs quality delta
- **Description trigger rate optimization** — systematic, not guesswork
- **LLM-graded assertions** — scales to many skills
- **Live HTML report** — stakeholder-friendly output
- **Execution transcript analysis** — understands *why* skills fail at runtime

### skill-manager has, skill-creator lacks:
- **12-dimension dual-track rubric** — fine-grained diagnosis of exactly which axis is weak
- **7-step restoration methodology** — how to fix a bad skill, not just detect it
- **Tier system** — Lite/Standard/Enterprise gives clear scope expectations
- **§1.1/1.2/1.3 system prompt design** — structural guide for the highest-weight dimension
- **Certification suite** — adversarial + stress testing, production sign-off
- **Platform-agnostic shell scripts** — work without LLM invocation
- **Self-contained** — no external API calls needed to run an evaluation

---

## 6. Gap Analysis — Priority Fixes

### Gap 1: Trigger Rate Testing (P0)

**Why critical**: skill-creator's #1 unique value. A skill with perfect rubric scores but a weak description will never activate. This is a silent failure mode skill-manager cannot currently detect.

**Solution**:
```
evals/eval-queries.json    ← 20 queries, labeled should_trigger true/false
scripts/trigger-test.sh    ← runs each query, checks if skill activated, computes trigger rate
references/descriptions.md ← description optimization guide (train/val split methodology)
```

**Estimated effort**: Medium (requires agent invocation per query, ~4 hrs)

### Gap 2: evals.json Workflow (P0)

**Why critical**: agentskills spec defines this as the standard eval format. Without it, skill-manager is incompatible with the broader tooling ecosystem.

**Solution**: Add `evals/evals.json` template + documentation in `references/evaluate.md`

**Estimated effort**: Low (~1 hr)

### Gap 3: Token + Time Benchmarking (P1)

**Why matters**: skill-creator tracks `total_tokens` and `duration_ms` per eval run, enabling ROI analysis (does this skill's quality improvement justify the token cost?). skill-manager has no equivalent.

**Solution**: `scripts/benchmark.sh` — compares two EVALUATION_REPORT.md files, outputs delta table

**Estimated effort**: Low (~2 hrs)

### Gap 4: Automated Assertion Grading (P1)

**Why matters**: Human scoring via `eval.sh` is high-quality but doesn't scale beyond ~10 skills. Teams maintaining 50+ skills need automated grading.

**Solution**: `scripts/grade.sh` — takes `evals/evals.json` assertions, invokes LLM, records PASS/FAIL with evidence

**Estimated effort**: High (~8 hrs, requires Claude API integration)

### Gap 5: HTML Report (P2)

**Solution**: `scripts/report.sh` — converts EVALUATION_REPORT.md to styled HTML with score gauges

**Estimated effort**: Low (~2 hrs)

---

## 7. Recommended Integration Strategy

For maximum coverage, run skill-creator and skill-manager **together, at different stages**:

```
Stage 1 — WRITE
  skill-manager: create.md + validate.sh + score.sh
  → Ensures spec compliance, content structure, domain specificity

Stage 2 — CONTENT QUALITY
  skill-manager: eval.sh standard
  → Dual-track 12-dimension rubric, catches weak dimensions

Stage 3 — DESCRIPTION EFFECTIVENESS
  skill-creator: description optimization
  → Trigger rate on 20 eval queries, train/val split

Stage 4 — PRODUCTION
  skill-manager: certify.sh
  → Adversarial + stress tests, formal certification

Stage 5 — RESTORATION (if needed)
  skill-manager: restore.md
  → 7-step methodology to fix failing skills
```

**Positioning**: skill-manager owns *content quality*; skill-creator owns *description effectiveness* and *performance benchmarking*. They are complementary, not competing. The ideal workflow runs both.

---

## 8. Roadmap (Updated)

| Priority | Feature | Closes Gap | Effort |
|----------|---------|------------|--------|
| P0 | `evals/evals.json` template | Ecosystem compatibility | 1 hr |
| P0 | `scripts/trigger-test.sh` + `references/descriptions.md` | Silent activation failures | 4 hrs |
| P1 | `scripts/benchmark.sh` — before/after delta | Token/time ROI | 2 hrs |
| P1 | `scripts/grade.sh` — LLM assertion grading | Scale to 50+ skills | 8 hrs |
| P2 | `scripts/report.sh` — HTML output | Stakeholder reporting | 2 hrs |

---

*Based on: agentskills spec v1.0 (2026-03), skill-creator SKILL.md ~900 lines (fetched 2026-03-25), Anthropic engineering blog "Equipping agents for the real world with Agent Skills", agentskills.io documentation*
