# 通用安装指南 / Common Installation Guide

> 所有 Awesome Skills 技能的平台安装说明均引用此文件，避免重复维护。
> All Awesome Skills platform installation instructions reference this file to avoid duplication.

---

## 快速安装 / Quick Install

将以下命令中的 `[SKILL_URL]` 替换为目标技能的 GitHub 地址，`[skill-name]` 替换为技能名称：

```
Read [SKILL_URL] and install [skill-name] skill
```

示例 (Example):
```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo.md and install ceo skill
```

quality: basic
---

## OpenCode（推荐 / Recommended）

OpenCode 原生支持技能安装：

```
/skill install [skill-name]
```

或使用 Read 命令：
```
Read [SKILL_URL] and install [skill-name] skill
```

---

## OpenClaw（推荐 / Recommended）

```
Read [SKILL_URL] and install [skill-name] skill
```

技能存储位置：`~/.openclaw/workspace/skills/[skill-name]/SKILL.md`

---

## Claude Code

**方法 1：项目级配置（推荐）**
```bash
cat >> CLAUDE.md << 'EOF'
Read [SKILL_URL] and apply the skill guidelines to this project.
EOF
```

**方法 2：单次会话**
```
Read [SKILL_URL] and install [skill-name] skill
```

---

## Cursor

```bash
curl -s [RAW_SKILL_URL] >> .cursorrules
```

将 `[RAW_SKILL_URL]` 替换为技能的 raw GitHub 地址（`raw.githubusercontent.com/...`）

---

## OpenAI Codex / Cline / Kimi Code

将技能文件的 System Prompt 部分复制到对应平台的系统提示词配置中。

---

## 完整平台指南 / Full Platform Guide

详见项目根目录的 [INSTALL-GUIDE.md](../../INSTALL-GUIDE.md)

---

## 技能包安装 / Package Installation

```
Read https://github.com/theneoai/awesome-skills/blob/main/packages/[package-name].md and install [package-name] package
```

可用技能包 (Available packages)：`executive`, `tech`, `ai-ml`, `professional`, `creative`
