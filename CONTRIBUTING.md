# Contributing to Awesome Skills <!-- 为 Awesome Skills 做贡献 -->

First off, thank you for considering contributing to Awesome Skills! 
<!-- 首先，感谢你考虑为 Awesome Skills 做贡献！-->

This document provides guidelines for contributing new skills, improving existing ones, and helping the community grow.
<!-- 本文档提供了贡献新技能、改进现有技能以及帮助社区发展的指南。-->

## 📋 Table of Contents <!-- 目录 -->

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Skill Development Guide](#skill-development-guide)
- [Bilingual Format Guide](#bilingual-format-guide)
- [Pull Request Process](#pull-request-process)
- [Validation & CI](#-validation--ci)
- [Style Guidelines](#style-guidelines)

## 🤝 Code of Conduct <!-- 行为准则 -->

This project adheres to a code of conduct that we expect all contributors to follow:
<!-- 本项目遵循行为准则，我们希望所有贡献者都能遵守：-->

- **Be respectful**: Treat everyone with respect. Healthy debate is encouraged, but harassment is not tolerated.
  <!-- **保持尊重**：尊重每个人。鼓励健康的辩论，但不容忍骚扰。-->
- **Be constructive**: Provide constructive feedback and be open to receiving it.
  <!-- **保持建设性**：提供建设性的反馈，并乐于接受反馈。-->
- **Focus on what's best for the community**: Prioritize the community's needs over individual preferences.
  <!-- **关注社区的最佳利益**：将社区需求置于个人偏好之上。-->

## 🚀 How Can I Contribute? <!-- 如何贡献？-->

### 1. Submit a New Skill <!-- 提交新技能 -->

Have expertise in a domain not yet covered? Create a new skill!
<!-- 拥有尚未涵盖的领域专业知识？创建一个新技能！-->

**Process:**
<!-- **流程：**-->
1. Check existing skills to avoid duplication
   <!-- 1. 检查现有技能以避免重复 -->
2. Use the [TEMPLATE.md](./skills/special/skill-writer/assets/TEMPLATE.md) as your starting point
   <!-- 2. 使用 [TEMPLATE.md](./skills/special/skill-writer/assets/TEMPLATE.md) 作为起点 -->
3. Follow the [Skill Development Guide](#skill-development-guide)
   <!-- 3. 遵循 [技能开发指南](#skill-development-guide) -->
4. Submit a Pull Request
   <!-- 4. 提交 Pull Request -->

### 2. Improve Existing Skills <!-- 改进现有技能 -->

Found a bug, typo, or outdated information? Help us fix it!
<!-- 发现错误、拼写错误或过时信息？帮助我们修复！-->

**Areas for improvement:**
<!-- **改进领域：**-->
- Correcting factual errors
  <!-- - 纠正事实错误 -->
- Updating outdated information
  <!-- - 更新过时信息 -->
- Adding missing best practices
  <!-- - 添加缺失的最佳实践 -->
- Improving clarity and readability
  <!-- - 提高清晰度和可读性 -->
- Adding Chinese translations
  <!-- - 添加中文翻译 -->

### 3. Report Issues <!-- 报告问题 -->

Found something wrong but can't fix it yourself? Open an issue!
<!-- 发现问题但无法自己修复？开 Issue！-->

**When opening an issue:**
<!-- **开 Issue 时：**-->
- Use a clear, descriptive title
  <!-- - 使用清晰、描述性的标题 -->
- Describe the problem in detail
  <!-- - 详细描述问题 -->
- Include steps to reproduce (if applicable)
  <!-- - 包含复现步骤（如适用） -->
- Suggest a solution (if you have one)
  <!-- - 建议解决方案（如果你有） -->

## 📚 Skill Development Guide <!-- 技能开发指南 -->

### Skill Structure <!-- 技能结构 -->

Each skill follows a standardized structure:
<!-- 每个技能遵循标准化结构：-->

```
skills/
└── [category]/
    └── [skill-name].md
```

**File naming convention:**
<!-- **文件命名约定：**-->
- Use lowercase letters
- Use hyphens for spaces
- Be descriptive but concise
- Example: `software-architect.md`, `finance-risk-expert.md`

### Required Sections <!-- 必需部分 -->

Every skill must include all **16 standard H2 sections** in the correct order. The canonical structure is defined in [TEMPLATE.md](./skills/special/skill-writer/assets/TEMPLATE.md) and the authoritative checklist is in [skill-writer.md §7.3](./skills/special/skill-writer/SKILL.md).
<!-- 每个技能必须按正确顺序包含所有 **16 个标准 H2 章节**。规范结构在 [TEMPLATE.md](./skills/special/skill-writer/assets/TEMPLATE.md) 中定义，权威清单在 [skill-writer.md §7.3](./skills/special/skill-writer/SKILL.md) 中。-->

The sections below describe the most critical ones:
<!-- 以下章节描述最关键的部分：-->

#### 1. Frontmatter (YAML) <!-- 1. 前言（YAML）-->

```yaml
---
name: skill-name                             # Unique identifier / 唯一标识符
display_name: Skill Display Name / 技能名称  # Bilingual display name
author: your-github-username                 # Contributor / 贡献者
version: 1.0.0                              # Semantic versioning / 语义化版本
difficulty: expert|intermediate|beginner     # Skill complexity level
category: category-name                      # Must match a /skills/ subdirectory
tags: [tag1, tag2, tag3]                    # 3-5 searchable tags
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  A world-class expert in [domain]. Use when [triggers].
  Triggers: "keyword1", "keyword2"
  Works with: Claude Code, OpenAI Codex, Kimi Code, OpenCode, Cursor, Cline, OpenClaw.
---
```

> **⚠️ Important**: Do NOT include `<!-- HTML comments -->` inside the YAML `description` field. YAML does not parse them — they become literal string content polluting machine-readable metadata. Keep bilingual content in the Markdown body only.

#### 2. What This Skill Does <!-- 2. 此技能做什么 -->

Clear description of capabilities.
<!-- 能力的清晰描述。-->

#### 3. Risk Disclaimer ⚠️ <!-- 3. 风险提示 ⚠️-->

**CRITICAL**: Every skill must include risk warnings specific to its domain.
<!-- **关键**：每个技能必须包含针对其领域的风险警告。-->

Examples:
<!-- 示例：-->
- Medical skills: "Not a substitute for professional medical advice"
  <!-- 医疗技能："不能替代专业医疗建议" -->
- Financial skills: "Not financial advice, consult qualified professionals"
  <!-- 金融技能："不是财务建议，请咨询合格专业人士" -->
- Legal skills: "Not legal advice, consult qualified attorneys"
  <!-- 法律技能："不是法律建议，请咨询合格律师" -->

#### 4. Core Philosophy <!-- 4. 核心理念 -->

Fundamental principles of the domain.
<!-- 领域的基本原则。-->

#### 5. Platform Support <!-- 5. 平台支持 -->

Installation instructions for all 7 supported platforms.
<!-- 所有 7 个支持平台的安装说明。-->

#### 6. Professional Toolkit <!-- 6. 专业工具包 -->

Tools, software, and resources used in the field.
<!-- 该领域使用的工具、软件和资源。-->

#### 7. Standard Workflow <!-- 7. 标准工作流程 -->

Step-by-step process for the domain.
<!-- 该领域的分步流程。-->

#### 8. Best Practices <!-- 8. 最佳实践 -->

Industry best practices with examples.
<!-- 带示例的行业最佳实践。-->

#### 9. Common Pitfalls <!-- 9. 常见陷阱 -->

Common mistakes and how to avoid them.
<!-- 常见错误以及如何避免。-->

#### 10. How to Use <!-- 10. 如何使用 -->

Clear installation and usage instructions.
<!-- 清晰的安装和使用说明。-->

### Skill Quality Criteria <!-- 技能质量标准 -->

Before submitting, ensure your skill meets these criteria:
<!-- 提交前，确保你的技能符合以下标准：-->

| Criterion / 标准 | Requirement / 要求 |
|-----------------|-------------------|
| **Accuracy / 准确性** | Content is factually correct / 内容事实正确 |
| **Completeness / 完整性** | All 9 metadata fields + all 16 H2 sections in correct order; see TEMPLATE.md / 所有 9 个元数据字段 + 按正确顺序排列的 16 个 H2 章节 |
| **Clarity / 清晰性** | Easy to understand; tables over prose / 易于理解；表格优于散文 |
| **Practicality / 实用性** | Actionable advice with frameworks and examples / 含框架和示例的可操作建议 |
| **Safety / 安全性** | 4+ domain-specific risk warnings with severity ratings / 4+ 条带严重度评级的领域特定风险警告 |
| **Bilingual / 双语** | English primary; Chinese in `<!-- -->` for prose; `/` separator in table headers / 英文为主；散文中文用 `<!-- -->`；表头用 `/` 分隔 |

## 🌏 Bilingual Format Guide <!-- 双语格式指南 -->

### Why This Format? <!-- 为什么用这种格式？-->

We use **comment-based bilingual format** to balance:
<!-- 我们使用**基于注释的双语格式**来平衡：-->

1. **AI Efficiency**: AI assistants primarily read English content
   <!-- **AI 效率**：AI 助手主要读取英文内容 -->
2. **Human Accessibility**: Chinese users can understand via comments
   <!-- **人类可访问性**：中文用户可以通过注释理解 -->
3. **Token Efficiency**: Comments don't significantly impact token count
   <!-- **Token 效率**：注释不会显著影响 token 数量 -->

### How to Write Bilingual Content <!-- 如何编写双语内容 -->

#### Basic Pattern <!-- 基本模式 -->

```markdown
English sentence here.
<!-- 中文翻译在这里。-->
```

#### Examples <!-- 示例 -->

**Headers:**
```markdown
## Core Philosophy / 核心理念
```

**Bullet points:**
```markdown
- **Principle 1**: Explanation here
  <!-- **原则 1**：这里的解释 -->
```

**Tables:**
```markdown
| English Header / 英文标题 | Description / 描述 |
```

**Risk warnings:**
```markdown
**⚠️ IMPORTANT / 重要**:
- Risk description here
  <!-- 这里的风险描述 -->
```

### What NOT to Do <!-- 不要做什么 -->

❌ **Don't duplicate entire sections**
<!-- ❌ **不要重复整个部分**-->
```markdown
## Section 1
English content...

## 第一部分  <!-- DON'T DO THIS -->
中文内容...
```

✅ **Do use comment format**
<!-- ✅ **使用注释格式**-->
```markdown
## Section 1 / 第一部分
English content...
<!-- 中文内容... -->
```

## 🔄 Pull Request Process <!-- Pull Request 流程 -->

### 1. Fork and Branch <!-- 1. Fork 和 Branch -->

```bash
# Fork the repository on GitHub first
# 先在 GitHub 上 Fork 仓库

# Clone your fork
# 克隆你的 Fork
git clone https://github.com/YOUR-USERNAME/awesome-skills.git
cd awesome-skills

# Create a new branch
# 创建新分支
git checkout -b add-skill-name
```

### 2. Add Your Skill <!-- 2. 添加你的技能 -->

```bash
# Create the skill file
# 创建技能文件
mkdir -p skills/[category]
touch skills/[category]/[skill-name].md

# Edit the file following TEMPLATE.md
# 按照 TEMPLATE.md 编辑文件
```

### 3. Test Your Skill <!-- 3. 测试你的技能 -->

Before submitting:
<!-- 提交前：-->
- [ ] Read through the entire skill
  <!-- [ ] 通读整个技能 -->
- [ ] Check for typos and formatting issues
  <!-- [ ] 检查拼写和格式问题 -->
- [ ] Verify all links work
  <!-- [ ] 验证所有链接有效 -->
- [ ] Test installation command
  <!-- [ ] 测试安装命令 -->

### 4. Submit PR <!-- 4. 提交 PR -->

```bash
# Commit your changes
# 提交更改
git add .
git commit -m "feat: add [skill-name] skill

- Brief description of what the skill covers
- Why it's valuable to the community"

# Push to your fork
# 推送到你的 Fork
git push origin add-skill-name

# Create Pull Request on GitHub
# 在 GitHub 上创建 Pull Request
```

### PR Title Format <!-- PR 标题格式 -->

```
feat: add [skill-name] skill
fix: correct [issue] in [skill-name]
docs: improve [section] in [skill-name]
```

### PR Description Template <!-- PR 描述模板 -->

```markdown
## Description
<!-- 描述 -->
Brief description of changes

## Type of Change
<!-- 变更类型 -->
- [ ] New skill
- [ ] Skill improvement
- [ ] Bug fix
- [ ] Documentation update

## Checklist
<!-- 检查清单 -->
- [ ] Validator passes locally: `python3 .github/scripts/validate_skills.py <file>`
- [ ] Followed TEMPLATE.md structure (all 16 H2 sections in correct order)
- [ ] All 9 YAML metadata fields present; no HTML comments in YAML `description`
- [ ] `quality` field set to `basic` / `community` / `expert` / `exemplary`
- [ ] `version` bumped using semver (MAJOR.MINOR.PATCH)
- [ ] Included 4+ domain-specific risk warnings with severity ratings
- [ ] Added bilingual comments (English primary, Chinese in `<!-- -->`)
- [ ] Tested installation command
- [ ] Updated CATALOG.md (if quality tier changed or new skill added)
- [ ] Updated index.html (if new category)

## Skill Details (if new skill)
<!-- 技能详情（如果是新技能）-->
- **Category**: [e.g., software, finance]
- **Target Users**: [who would use this]
- **Value Proposition**: [why it's useful]
```

## ✅ Validation & CI <!-- 验证与持续集成 -->

Every skill file is automatically validated by CI on push and pull request.
<!-- 每个技能文件都会在推送和 PR 时由 CI 自动验证。-->

### Running the Validator Locally <!-- 本地运行验证器 -->

```bash
# Validate all skill files
python3 .github/scripts/validate_skills.py skills/

# Validate a single file
python3 .github/scripts/validate_skills.py skills/software/software-architect/SKILL.md

# Strict mode: enforce 16-section structure (for Expert Verified skills)
python3 .github/scripts/validate_skills.py --strict skills/executive/
```

### What the Validator Checks <!-- 验证器检查内容 -->

| Check / 检查 | Applies To / 适用范围 | Failure Blocks Merge? |
|-------------|----------------------|----------------------|
| YAML frontmatter present | All skills | ✅ Yes |
| Required fields: `name`, `display_name`, `author`, `version`, `description` | All skills | ✅ Yes |
| No HTML comments inside YAML frontmatter | All skills | ✅ Yes |
| Semver format for `version` | All skills | ✅ Yes |
| Valid `difficulty` value (`expert`/`intermediate`/`beginner`) | If field present | ✅ Yes |
| Valid `quality` value (`basic`/`community`/`expert`/`exemplary`) | If field present | ✅ Yes |
| H1 title present in body | All skills | ✅ Yes |
| Recommended fields: `difficulty`, `category`, `tags`, `platforms`, `quality` | All skills | ⚠️ Warning only |
| ≥ 16 H2 sections present | Expert Verified skills | ✅ Yes (strict mode) |
| At least one fenced code block | Expert Verified skills | ✅ Yes (strict mode) |
| `## 1. System Prompt` section present | Expert Verified skills | ✅ Yes (strict mode) |

### CI Pipeline Overview <!-- CI 流水线概述 -->

The GitHub Actions workflow (`.github/workflows/validate.yml`) runs two passes:
<!-- GitHub Actions 工作流程运行两轮验证：-->

1. **Standard pass** — validates all `skills/**/*.md` files for basic compliance
   <!-- **标准检查** — 验证所有技能文件的基本合规性 -->
2. **Strict pass** — validates Expert Verified skill directories with `--strict` (enforces 16-section structure)
   <!-- **严格检查** — 对 Expert Verified 技能目录执行严格验证（强制要求 16 章节结构）-->
3. **PR diff pass** — re-validates only the changed files in the pull request
   <!-- **PR 差异检查** — 仅重新验证 PR 中更改的文件 -->

### Metadata Field Reference <!-- 元数据字段参考 -->

All metadata fields are expected for Expert Verified skills. The first five fields (`name`, `display_name`, `author`, `version`, `description`) are required by our validator. `when_to_use` and `compatibility` follow the [official Agent Skills standard](https://github.com/anthropics/skills). See [TEMPLATE.md](./skills/special/skill-writer/assets/TEMPLATE.md) for the full YAML example and [skill-writer.md §7.2](./skills/special/skill-writer/SKILL.md) for the authoritative field specification.
<!-- 所有元数据字段对于 Expert Verified 技能都是必需的。-->

| Field / 字段 | Required / 必需 | Valid Values / 有效值 | Standard / 来源 |
|-------------|----------------|----------------------|----------------|
| `name` | ✅ Required | kebab-case, max 64 chars; **must match parent folder name** if folder-based | Agent Skills |
| `display_name` | ✅ Required | `English Name / 中文名称` | Awesome Skills |
| `author` | ✅ Required | GitHub username or ID | Awesome Skills |
| `version` | ✅ Required | semver `MAJOR.MINOR.PATCH` | Awesome Skills |
| `description` | ✅ Required | Plain text only, max 1024 chars, no `<!-- HTML -->`. **Primary trigger signal — make it specific and "pushy"** | Agent Skills |
| `difficulty` | ⚠️ Recommended | `expert` / `intermediate` / `beginner` | Awesome Skills |
| `category` | ⚠️ Recommended | Must match a `/skills/` subdirectory | Awesome Skills |
| `tags` | ⚠️ Recommended | Array of 3–5 strings | Awesome Skills |
| `platforms` | ⚠️ Recommended | Array from: `opencode`, `openclaw`, `claude`, `cursor`, `codex`, `cline`, `kimi` | Awesome Skills |
| `quality` | ⚠️ Recommended | `basic` / `community` / `expert` / `exemplary` | Awesome Skills |
| `compatibility` | ⚠️ Optional | Required tools/deps e.g. `[python3, node]` | Agent Skills |
| `when_to_use` | ⚠️ Optional | Explicit invocation conditions (supplements `description`) | Agent Skills |

### Skill File vs. Folder Structure <!-- 文件 vs 文件夹结构 -->

Awesome Skills supports two layouts:
<!-- Awesome Skills 支持两种布局：-->

**Option A — Flat file (simple skills):**
```
skills/{category}/{skill-name}.md
```

**Option B — Folder (recommended for complex/bundled skills, full Agent Skills compatibility):**
```
skills/{category}/{skill-name}/
├── SKILL.md          ← required; name field must match folder name
├── scripts/          ← executable helpers
├── agents/           ← sub-agent instruction files
├── references/       ← reference docs (not validated by CI)
├── assets/           ← templates, icons, fonts
└── evals/
    └── evals.json    ← test cases
```

The folder format is **required** when bundling scripts, assets, or sub-agent files and enables full compatibility with Claude Code's `/plugin` system and GitHub Copilot.

---

## 🎨 Style Guidelines <!-- 风格指南 -->

### Writing Style <!-- 写作风格 -->

- **Be concise**: Clear and to the point
  <!-- **简洁**：清晰且切中要点 -->
- **Be specific**: Concrete examples over abstract concepts
  <!-- **具体**：具体示例优于抽象概念 -->
- **Be actionable**: Tell users exactly what to do
  <!-- **可操作**：准确告诉用户做什么 -->
- **Be consistent**: Follow the established patterns
  <!-- **一致**：遵循既定模式 -->

### Formatting <!-- 格式 -->

- Use Markdown for all content
  <!-- 对所有内容使用 Markdown -->
- Use emoji for visual hierarchy (🎯, ⚠️, ✅)
  <!-- 使用表情符号进行视觉层次划分 -->
- Use tables for comparisons
  <!-- 使用表格进行比较 -->
- Use code blocks for commands and examples
  <!-- 对命令和示例使用代码块 -->

## 💬 Questions? <!-- 有问题？-->

- **General questions**: Open a [Discussion](https://github.com/theneoai/awesome-skills/discussions)
  <!-- **一般问题**：开 [Discussion](https://github.com/theneoai/awesome-skills/discussions) -->
- **Bug reports**: Open an [Issue](https://github.com/theneoai/awesome-skills/issues)
  <!-- **Bug 报告**：开 [Issue](https://github.com/theneoai/awesome-skills/issues) -->
- **Skill ideas**: Open a [Discussion](https://github.com/theneoai/awesome-skills/discussions) with "Idea" label
  <!-- **技能想法**：开 [Discussion](https://github.com/theneoai/awesome-skills/discussions) 并标注 "Idea" -->

---

Thank you for contributing to Awesome Skills! 🌟
<!-- 感谢你为 Awesome Skills 做贡献！🌟-->
