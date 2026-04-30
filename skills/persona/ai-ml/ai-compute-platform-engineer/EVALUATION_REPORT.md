# Evaluation Report — ai-compute-platform-engineer

## Skill Summary
| Field | Value |
|-------|-------|
| **Name** | ai-compute-platform-engineer |
| **Version** | 3.0.0 |
| **Quality Tier** | Expert ⭐ |
| **Rubric Score** | 7.6/10 |
| **Line Count** | 647 |

---

## 6-Dimension Rubric Scores

| Dimension | Score | Weight | Weighted | Tier |
|-----------|-------|--------|----------|------|
| System Prompt Depth | 8.0 | 20% | 1.60 | Expert |
| Domain Knowledge Density | 8.5 | 25% | 2.125 | Expert |
| Workflow Actionability | 7.0 | 15% | 1.05 | Expert |
| Risk Documentation | 8.0 | 10% | 0.80 | Expert |
| Example Quality | 8.0 | 20% | 1.60 | Expert |
| Metadata Completeness | 6.0 | 10% | 0.60 | Community |

---

## Strengths

### §1 System Prompt — Excellent
- Specific identity: 10,000 H100 GPU cluster, 3.2 Tb/s InfiniBand HDR, 55% MFU
- MFU-First gate with specific threshold (>45%)
- Decision Framework with 5 gates (MFU Baseline, Network Bottleneck, Failure Rate, Scheduling Efficiency, Storage I/O)
- **5 Thinking Patterns** with GPU-specific thinking
- MFU-decomposition model with specific formula
- Specific hardware specs (NVLink 900 GB/s, IB HDR 200 Gb/s = 25 GB/s)
- Bilingual Chinese headers (helpful for Chinese-speaking users but anti-pattern #7 violation)
- **Verdict**: Very deep domain knowledge

### §2 What This Skill Does
- 5 capabilities specific to GPU cluster engineering

### §3 Risk Disclaimer
- 4 risks with severity (Silent Data Corruption, Checkpoint Data Loss, NCCL Timeout Cascades, Storage I/O Amplification)
- Specific mitigations with XID error monitoring, atomic writes, watchdog process
- ⚠️ IMPORTANT block with MFU benchmarks

### §6 Professional Toolkit
- Specific tools (NVIDIA DCGM, NCCL, SLURM, Kubernetes + Volcano, Prometheus + Grafana, DeepSpeed, Megatron-LM, Lustre)
- GPU-specific monitoring tools

### §9.2 & §9.3 Scenario Examples
- **§9.2**: Training job stuck at 28% MFU — excellent diagnostic tree with command examples
- **§9.3**: Fault-tolerant pipeline design for 45-day runs with code
- Both are high-quality domain-specific examples with concrete commands

---

## Weaknesses

### ❌ Missing §7 Standard Workflow (Severity: High)
- Section §7 exists but only contains: `See [references/07-standards.md](references/07-standards.md)`
- No actual workflow content
- No [✓ Done]/[✗ FAIL] criteria

### ❌ Missing §8 Standard Workflow (Severity: High)
- Section §8 exists but only: `See [references/08-workflow.md](references/08-workflow.md)`
- No actual workflow

### ❌ Missing §10 Common Pitfalls (Severity: High)
- §10 exists but only: `See [references/10-pitfalls.md](references/10-pitfalls.md)`
- No actual anti-pattern content

### ❌ Missing §5 Platform Support (Severity: High)
- Professional Toolkit present but no platform installation guidance

### ❌ Duplicate Generic Scenarios (Severity: Medium)
- §9 Scenario Examples lines 367-463: identical generic templates

### ❌ Duplicate Boilerplate Sections (Severity: High)
- §16 Domain Deep Dive through §21 Resources identical to all admin skills (~130 lines)

### ❌ Metadata Below Standard (Severity: Medium)
- Has `tags` but uses non-standard format
- Missing `category`, `difficulty`, `platforms`
- Uses `tags` array instead of standard spec

### ❌ References Point to Non-Existent Files
- `references/07-standards.md`, `references/08-workflow.md`, `references/10-pitfalls.md`
- These files likely don't exist, making the workflow sections empty stubs

### ❌ Token Budget Exceeded (Severity: High)
- **647 lines** — exceeds 500-line limit by 147 lines
- Even worse: 647 lines but ~200 lines is boilerplate + generic scenarios + reference pointers

---

## Anti-Patterns Detected

| # | Anti-Pattern | Severity | Location |
|---|-------------|----------|----------|
| #4 | Token Waste — 647 lines + empty reference pointers | 🔴 High | Entire file |
| #4 | Token Waste — ~130 lines boilerplate | 🔴 High | §16-21 |
| #4 | Token Waste — generic scenarios | 🟡 Medium | §9 |
| #9 | Platform Coverage Miss | 🔴 High | Missing section |
| #7 | Literal Translation — bilingual headers throughout | 🟢 Low | §1.2, §1.3 table |
| — | Empty workflow sections (§7, §8, §10) pointing to missing files | 🔴 High | Lines 233, 241, 467 |
| — | Non-standard metadata (tags array format) | 🟡 Medium | Lines 8-15 |

---

## Token Budget Analysis

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| SKILL.md lines | 647 | ≤500 | ❌ Over by 147 lines |
| Post-cleanup estimate | ~500 lines | ≤500 | ✅ At target |

---

## Recommendation

**Tier: Expert ⭐** (7.6/10)

The §1 System Prompt is genuinely excellent — deep GPU cluster expertise with specific MFU thresholds, NCCL details, and fault-tolerance thinking. However, the skill is severely compromised by three empty sections that point to non-existent `references/` files. This is the same issue as ai-chip-architect. Either create the reference files or inline the workflow content.

**Immediate actions required:**
1. Create `references/07-standards.md`, `references/08-workflow.md`, `references/10-pitfalls.md` OR inline the content
2. Strip boilerplate (§16-21) and generic scenarios
3. Add §5 Platform Support
4. Fix metadata

After fixes: Estimated score → 8.5/10 Expert ⭐
