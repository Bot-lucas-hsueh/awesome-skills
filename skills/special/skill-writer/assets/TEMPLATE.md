---
name: example-skill                             # Lowercase, hyphen-separated
display_name: Example Expert Skill / 示例专家技能  # Bilingual display name
author: your-id                                  # Author identifier
version: 1.0.0                                   # Semantic versioning (MAJOR.MINOR.PATCH)
difficulty: expert|intermediate|beginner         # Skill complexity level
category: category-name                          # Must match a /skills/ subdirectory
tags: [tag1, tag2, tag3]                         # 3-5 searchable tags
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  [Role description]. Use when [trigger conditions].
  Triggers: "keyword1", "keyword2", "keyword3"
  Works with: Claude Code, OpenAI Codex, Kimi Code, OpenCode, Cursor, Cline, OpenClaw.
---

# Example Expert Skill / 示例专家技能

> **Version 1.0.0** | **[Basic | Community Verified | Expert Verified]** | **Last Updated: YYYY-MM-DD**

---

## 1. System Prompt / 系统提示词

### 1.1 Role Definition / 角色定义

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

### 1.2 Decision Framework / 决策框架

Before responding in this domain, evaluate:
<!-- 在此领域回应前，通过以下关卡评估： -->

| Gate / 关卡 | Question / 问题 | Fail Action / 不通过时 |
|-------------|----------------|----------------------|
| **[Gate 1]** | [Decision question] | [Concrete action if failed] |
| **[Gate 2]** | [Decision question] | [Concrete action if failed] |
| **[Gate 3]** | [Decision question] | [Concrete action if failed] |

### 1.3 Thinking Patterns / 思维模式

| Dimension / 维度 | [Role] Perspective / 视角 |
|-----------------|---------------------------|
| **[Dimension 1]** | [How this expert thinks — concrete, not generic] |
| **[Dimension 2]** | [How this expert thinks — concrete, not generic] |
| **[Dimension 3]** | [How this expert thinks — concrete, not generic] |

### 1.4 Communication Style / 沟通风格

- **[Style trait 1]**: [Description with concrete example]
  <!-- [中文描述] -->
- **[Style trait 2]**: [Description with concrete example]
  <!-- [中文描述] -->
- **[Style trait 3]**: [Description with concrete example]
  <!-- [中文描述] -->

---

## 2. What This Skill Does / 此技能做什么

1. **[Capability 1]** — [Specific, measurable change in AI output — not generic]
   <!-- **[能力 1]** — [具体可衡量的描述] -->
2. **[Capability 2]** — [description]
3. **[Capability 3]** — [description]
4. **[Capability 4]** — [description]

---

## 3. Risk Disclaimer / 风险提示

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation / 缓解措施 |
|------------|-----------------|-------------------|---------------------|
| **[Risk 1]** | 🔴 High | [Domain-specific risk — NOT generic "AI may be wrong"] | [Concrete mitigation with specific action] |
| **[Risk 2]** | 🔴 High | [Domain-specific risk] | [Concrete mitigation] |
| **[Risk 3]** | 🟡 Medium | [Domain-specific risk] | [Concrete mitigation] |
| **[Risk 4]** | 🟢 Low | [Domain-specific risk] | [Concrete mitigation] |

**⚠️ IMPORTANT / 重要**:
- [Domain-specific warning — describes a real consequence, not a generic disclaimer]
  <!-- [领域特定警告] -->
- [Domain-specific warning]
  <!-- [领域特定警告] -->

---

## 4. Core Philosophy / 核心理念

### 4.1 [Core Framework Name] / [核心框架名称]

```
[ASCII diagram, decision tree, or scoring matrix showing the domain's core mental model.
 ≤ 5 levels / decision nodes. Example: pyramid, 2×2 matrix, phase-gate flow.]
```

[One sentence: how the components relate and when each applies.]

### 4.2 Guiding Principles / 指导原则

1. **[Principle 1]**: [Explanation with concrete, domain-specific application]
   <!-- **[原则 1]**：[解释及具体领域应用] -->
2. **[Principle 2]**: [Explanation with concrete application]
   <!-- **[原则 2]**：[解释及具体应用] -->
3. **[Principle 3]**: [Explanation with concrete application]
   <!-- **[原则 3]**：[解释及具体应用] -->

---

## 5. Platform Support / 平台支持

| Platform / 平台 | Session Install / 会话安装 | Persistent Config / 持久化配置 |
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

## 6. Professional Toolkit / 专业工具包

| Tool / 工具 | Purpose / 用途 |
|------------|---------------|
| **[Tool 1]** | [Specific purpose — when and why to use this tool] |
| **[Tool 2]** | [Specific purpose] |
| **[Tool 3]** | [Specific purpose] |
| **[Framework or Standard]** | [How it applies in this domain] |

---

## 7. Standards & Reference / 标准与参考

### 7.1 [Domain] Frameworks / 领域框架

| Framework / 框架 | When to Use / 使用场景 | Key Steps / 关键步骤 |
|-----------------|----------------------|-------------------|
| **[Framework 1]** | [Trigger: what problem it solves] | [1. Step → 2. Step → 3. Step → Output] |
| **[Framework 2]** | [Trigger] | [1. Step → 2. Step → Output] |
| **[Framework 3]** | [Trigger] | [1. Step → 2. Step → Output] |

### 7.2 [Domain] Metrics / 领域指标

| Metric / 指标 | Formula / 公式 | Target / 目标 |
|--------------|--------------|---------------|
| **[Metric 1]** | [Specific formula or calculation] | [Concrete target: e.g., ">95%", "<200ms", "3:1 ratio"] |
| **[Metric 2]** | [Formula] | [Target with unit] |
| **[Metric 3]** | [Formula] | [Target] |

---

## 8. Standard Workflow / 标准工作流程

### 8.1 [Primary Task Name] / [主要任务名称]

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

### 8.2 [Secondary Task Name] / [次要任务名称]

```
Step 1: [Description — specific action, not generic]
Step 2: [Description]
Step 3: [Description with expected output]
```

---

## 9. Scenario Examples / 场景示例

### 9.1 [Scenario: Primary Use Case] / [场景：主要用例]

**User:** "[Realistic trigger request]"

**[Role Name]:**
> **[Framework applied from §7]:** [Expert framing — not generic advice]
>
> | [Decision Column] | [Data/Score] | [Recommendation] |
> |-------------------|-------------|-----------------|
> | [Option A] | [metric] | [action] |
>
> **Next I need:** [Clarifying question showing expert judgment]

### 9.2 [Scenario: Edge Case or Anti-Pattern Correction] / [场景：边界情况]

**User:** "[Different request type — tests a second capability]"

**[Role Name]:**
> **[Different framework from §7]:** [Expert-level insight — domain-specific, not generic]
> 1. [Actionable step with domain rationale]
> 2. [Actionable step]

---

## 10. Common Pitfalls & Anti-Patterns / 常见陷阱与反模式

| # | Anti-Pattern / 反模式 | Severity / 严重度 | Quick Fix / 快速修复 |
|---|----------------------|-----------------|---------------------|
| 1 | **[Name]** | 🔴 High | [Domain-specific fix] |
| 2 | **[Name]** | 🟡 Medium | [Fix] |
| 3 | **[Name]** | 🟢 Low | [Fix] |

```
❌ [Specific wrong approach in this domain]
✅ [Correct approach — measurably different, domain-specific]
```

---

## 11. Integration with Other Skills / 与其他技能的集成

| Combination / 组合 | Workflow / 工作流 | Result / 结果 |
|-------------------|-----------------|--------------|
| [This Skill] + **[Complementary Skill]** | [Step 1: This skill does X → Step 2: Other skill does Y] | [Specific outcome] |
| [This Skill] + **[Complementary Skill]** | [Workflow description] | [Specific outcome] |
| [This Skill] + **[Complementary Skill]** | [Workflow description] | [Specific outcome] |

---

## 12. Scope & Limitations / 范围与限制

**✓ Use this skill when:**
<!-- 适用场景： -->
- [Specific use case 1 — concrete trigger condition]
- [Specific use case 2]
- [Specific use case 3]

**✗ Do NOT use this skill when:**
<!-- 不适用场景： -->
- [Excluded case 1] → use `[alternative-skill-name]` skill instead
- [Excluded case 2] → use `[alternative-skill-name]` skill instead
- [Excluded case 3] → [reason why this skill doesn't apply + alternative]

---

## 13. How to Use This Skill / 如何使用此技能

### Quick Install / 快速安装
```
Read https://awesome-skills.dev/skills/[category]/[skill-name].md and install as skill
```

### Persistent Install (Claude Code) / 持久化安装（Claude Code）
```bash
# Global — applies to all projects / 全局，适用于所有项目
echo "Read https://awesome-skills.dev/skills/[category]/[skill-name].md and apply [skill-name] skill." >> ~/.claude/CLAUDE.md

# Project-level / 项目级
echo "Read https://awesome-skills.dev/skills/[category]/[skill-name].md and apply [skill-name] skill." >> ./CLAUDE.md
```

### Trigger Words / 触发词 (Authoritative List / 权威列表)
- "[trigger word 1]" / "[中文触发词 1]"
- "[trigger word 2]" / "[中文触发词 2]"
- "[trigger word 3]" / "[中文触发词 3]"
- "[trigger word 4]" / "[中文触发词 4]"

---

## 14. Quality Verification / 质量验证

Full checklist: `references/standards.md §7.10` — Critical blocking checks:
<!-- 完整清单见 references/standards.md §7.10 -->

| Check / 检查项 | Blocks Merge? |
|--------------|---------------|
| ☐ All 9 metadata fields; no HTML in YAML description; description ≤ 263 chars | ✅ Yes |
| ☐ All 16 H2 sections in correct order; no TBD/placeholder content | ✅ Yes |
| ☐ §5: all 7 platforms; session + persistent options; `[URL]` defined below table | ✅ Yes |
| ☐ Weighted rubric score ≥ 7.0 (Expert) / ≥ 9.0 (Exemplary) | ✅ Yes |
| ☐ Zero self-inconsistencies; no filler; every line earns its token cost | ✅ Yes |

### Test Cases / 测试用例

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

**Self-Score / 自评分:** [X.X/10 — Tier] — Justification: [brief evidence]

---

## 15. Version History / 版本历史

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | YYYY-MM-DD | Initial release |

---

## 16. License & Author / 许可证与作者

MIT with Attribution — Full terms, community links: [COMMON.md](../../COMMON.md)

| Field / 字段 | Details / 详情 |
|-------------|---------------|
| **Author** | [Your name or handle] |
| **Contact** | [Email or GitHub] |
| **GitHub** | [GitHub profile URL] |

**Author / 作者**: [name] <[email]> | **License**: MIT with Attribution
