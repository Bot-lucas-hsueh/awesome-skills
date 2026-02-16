# 智能安装命令

> 复制以下指令，AI 会自动检测平台、转换格式并安装

---

## 🔹 安装所有技能

### OpenClaw
```
Read https://theneoai.github.io/awesome-skills/INSTALL.md and install all skills from https://github.com/theneoai/awesome-skills/tree/main/skills. 

For each skill:
1. Read the skill's .md file (YAML frontmatter format)
2. Extract fields: name, display_name, description, author, version
3. Convert to OpenClaw SKILL.md format:
   - Keep 'name' as skill identifier
   - Use 'display_name' or 'name' as title
   - Extract English description (remove HTML comments and Chinese text)
   - Create SKILL.md with simple YAML frontmatter:
     ---
     name: [skill-name]
     description: "[English description]"
     ---
4. Save to ~/.openclaw/workspace/skills/[skill-name]/SKILL.md
5. Log installed skills

After installation, list all installed skills and confirm count.
```

### Claude Code
```
Install all skills from https://github.com/theneoai/awesome-skills/tree/main/skills for Claude Code.

For each skill:
1. Fetch the skill .md file from GitHub
2. Parse YAML frontmatter (name, display_name, description)
3. Convert to Claude Code format:
   - Create CLAUDE.md structure:
     # [display_name]
     
     [English description - remove HTML comments]
     
     ## Overview
     This skill provides expert-level guidance for [name].
     
     ## When to Use
     - [name] projects
     - Expert consultation
     - Best practices
     
     ## Guidelines
     [Extract key capabilities from skill content]
   
4. Save skills to ~/.claude/skills/[skill-name]/CLAUDE.md
5. Or save to current project: .claude/skills/[skill-name].md

Confirm: "X skills installed for Claude Code"
```

### Cursor
```
Install all skills from https://github.com/theneoai/awesome-skills/tree/main/skills for Cursor.

Process:
1. For each skill, fetch .md file
2. Parse YAML frontmatter and content
3. Convert to .cursorrules format:
   - Extract rules from skill capabilities
   - Format as:
     # [skill-name] Rules
     # [description]
     
     RULE: Always follow [skill-name] best practices
     RULE: [Capability 1]
     RULE: [Capability 2]
     ...
   
4. Concatenate ALL skills into single .cursorrules file
5. Save to: ./.cursorrules (project level)

The .cursorrules file should contain rules from all 450+ skills, organized by category.

Confirm installation with skill count.
```

### OpenAI Codex
```
Install all skills from https://github.com/theneoai/awesome-skills/tree/main/skills for OpenAI Codex.

For each skill:
1. Read skill .md from GitHub
2. Parse metadata and content
3. Convert to Codex format:
   - Create codex.md structure:
     # [skill-name] Guidelines
     
     ## Context
     You are an expert [skill-name] assistant.
     
     ## Instructions
     [Extract capabilities from skill content]
     
     ## Commands
     - help: Get help with [skill-name]
     - review: Review for best practices
     
4. Save to ~/.codex/skills/[skill-name]/codex.md

After installation, confirm: "All skills ready for Codex"
```

### Cline / Kimi Code
```
Install all skills from https://github.com/theneoai/awesome-skills/tree/main/skills for Cline.

Process:
1. Fetch each skill .md file
2. Extract: name, display_name, description, capabilities
3. Convert to Cline format (similar to Claude):
   - Create cline.md:
     ---
     name: [skill-name]
     description: "[English description]"
     ---
     
     # [display_name]
     
     ## Overview
     Expert guidance for [skill-name].
     
     ## When to Apply
     [Use cases from skill]
     
     ## Rules
     [Capability 1]
     [Capability 2]
     
4. Save to ~/.cline/skills/[skill-name]/cline.md
   (Kimi: ~/.kimi/skills/[skill-name]/cline.md)

Confirm installation.
```

### OpenCode
```
Install all skills from https://github.com/theneoai/awesome-skills/tree/main/skills for OpenCode.

OpenCode uses same format as OpenClaw (SKILL.md).

Process:
1. Read skill .md files
2. Convert to SKILL.md format:
   ---
   name: [skill-name]
   description: "[English description]"
   ---
   
   [Skill content]
   
3. Save to ~/.opencode/skills/[skill-name]/SKILL.md

Confirm: "Skills installed for OpenCode"
```

---

## 🔹 安装技能包

### 高管套件 (Executive Package)
```
Install executive skill package: ceo, cfo, cto, coo from https://github.com/theneoai/awesome-skills/tree/main/skills/business

For each skill in package:
1. Fetch skill/{skill-name}.md
2. Convert to current platform format (SKILL.md / CLAUDE.md / .cursorrules / codex.md / cline.md)
3. Install to appropriate directory
4. Report installed skills

Skills to install: ceo, cfo, cto, coo
```

### AI & ML 包
```
Install AI-ML skill package: llm-research-scientist, prompt-engineer, ai-product-manager, ai-ml-engineer from https://github.com/theneoai/awesome-skills/tree/main/skills/ai-ml

Auto-detect current platform and convert format accordingly.
Install to platform-specific directory.
```

### 技术开发包
```
Install tech skill package: software-architect, backend-developer, frontend-developer, devops-engineer, data-scientist, security-engineer from https://github.com/theneoai/awesome-skills/tree/main/skills/software

Platform: [auto-detect]
Format: [auto-convert]
Location: [platform-default]
```

### 金融会计包
```
Install finance skill package: accountant, cpa, financial-analyst, auditor, tax-specialist, investment-analyst from https://github.com/theneoai/awesome-skills/tree/main/skills/finance

Convert and install all finance skills.
```

### 医疗健康包
```
Install healthcare skill package: clinical-physician, icu-nurse, pharmacy-technician, radiologist, pathologist, anesthesiologist from https://github.com/theneoai/awesome-skills/tree/main/skills/healthcare

Auto-convert format for current platform.
```

### 法律合规包
```
Install legal skill package: legal-counsel, patent-attorney, compliance-specialist, judge, arbitrator, forensic-physician from https://github.com/theneoai/awesome-skills/tree/main/skills/legal
```

### 教育培训包
```
Install education skill package: university-professor, k12-teacher, corporate-trainer, curriculum-developer, teaching-assistant from https://github.com/theneoai/awesome-skills/tree/main/skills/education
```

---

## 🔹 安装单个技能

### CEO (首席执行官)
```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/business/ceo.md, convert to current platform format, and install.

Platform detection:
- If OpenClaw: Save to ~/.openclaw/workspace/skills/ceo/SKILL.md
- If Claude Code: Save to ~/.claude/skills/ceo/CLAUDE.md or ./CLAUDE.md
- If Cursor: Append to ./.cursorrules
- If Codex: Save to ~/.codex/skills/ceo/codex.md
- If Cline/Kimi: Save to ~/.cline/skills/ceo/cline.md
- If OpenCode: Save to ~/.opencode/skills/ceo/SKILL.md

Format conversion rules:
1. Extract: name, display_name, description, capabilities
2. Remove HTML comments (<!-- -->)
3. Keep English text only for description
4. Generate platform-specific file

Confirm: "CEO skill installed for [platform]"
```

### 软件架构师
```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/software/software-architect.md, auto-detect platform, convert format, and install.

Auto-detect → Convert → Install → Confirm
```

### Prompt 工程师
```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/ai-ml/prompt-engineer.md, convert to current platform format, and install.
```

### LLM 研究科学家
```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/ai-ml/llm-research-scientist.md, convert format, and install for current platform.
```

### 临床医师
```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/healthcare/clinical-physician.md, convert to platform format, and install.
```

---

## 🔹 自定义技能安装模板

### 安装任意技能
```
Install skill [skill-name] from https://github.com/theneoai/awesome-skills

Steps:
1. Fetch https://github.com/theneoai/awesome-skills/blob/main/skills/[category]/[skill-name].md
2. Detect current AI platform (OpenClaw/Claude/Cursor/Codex/Cline/Kimi/OpenCode)
3. Convert skill format:
   
   Input format (awesome-skills):
   ---
   name: [name]
   display_name: [display]
   description: >
     [English description]
     <!-- [Chinese comment] -->
   ---
   
   Output format (platform-specific):
   
   OpenClaw:
   ---
   name: [name]
   description: "[English-only description]"
   ---
   
   Claude Code:
   # [display_name]
   
   [English description]
   
   ## Overview
   Expert guidance for [name].
   
   Cursor:
   # [name] Rules
   RULE: [rule 1]
   RULE: [rule 2]
   
4. Save to platform-specific location
5. Confirm installation
```

---

## 🔧 格式转换规则详解

### 源格式 (awesome-skills)
```yaml
---
name: skill-name
display_name: Skill Name / 中文名
author: awesome-skills
version: 1.0.0
description: >
  English description here.
  <!-- Chinese comment here -->
  
  Triggers: "keyword1", "keyword2"
  Works with: Claude, Codex, Kimi, Cursor, Cline, OpenClaw
---

# Content with ## headers and bilingual text
```

### 目标格式转换

| 平台 | 关键字段 | 文件位置 |
|------|---------|---------|
| OpenClaw | `name`, `description` (English) | `~/.openclaw/workspace/skills/[name]/SKILL.md` |
| Claude Code | Title, Overview, When to Use | `~/.claude/skills/[name]/CLAUDE.md` |
| Cursor | RULE: prefixed rules | `./.cursorrules` |
| Codex | Guidelines, Commands | `~/.codex/skills/[name]/codex.md` |
| Cline/Kimi | Similar to Claude | `~/.cline/skills/[name]/cline.md` |
| OpenCode | Same as OpenClaw | `~/.opencode/skills/[name]/SKILL.md` |

### 转换步骤
1. **解析 YAML**: Extract name, display_name, description
2. **清理描述**: Remove HTML comments, keep English only
3. **提取能力**: Parse ## headers for capabilities
4. **生成文件**: Create platform-specific structure
5. **保存文件**: Write to appropriate directory

---

## 📋 可用技能查询

### 列出所有技能分类
```
List all available skill categories from https://github.com/theneoai/awesome-skills/tree/main/skills

Show:
1. All category directories
2. Skill count per category
3. Example skills from each category
```

### 搜索特定技能
```
Search for skills related to [topic] in https://github.com/theneoai/awesome-skills

Return matching skill names and their URLs.
```

---

## 🌐 快速链接

- **GitHub**: https://github.com/theneoai/awesome-skills
- **Skills**: https://github.com/theneoai/awesome-skills/tree/main/skills
- **Packages**: https://github.com/theneoai/awesome-skills/tree/main/packages
- **Website**: https://theneoai.github.io/awesome-skills/

---

## 💡 使用提示

1. **AI 会自动检测平台**: 不需要指定平台，AI 会识别当前环境
2. **自动格式转换**: AI 会按照上述规则转换技能格式
3. **批量安装**: 使用 "all" 或 "package" 命令安装多个技能
4. **确认安装**: 安装完成后 AI 会报告安装的技能数量
5. **更新技能**: 重新运行安装命令即可更新到最新版本
