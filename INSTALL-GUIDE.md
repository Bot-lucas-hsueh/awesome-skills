# Awesome Skills — 平台安装指南 / Platform Installation Guide

> 按平台查找安装命令 | Find installation commands by platform

---

## 平台功能对比 / Platform Capability Matrix

| 功能 | OpenCode | OpenClaw | Claude Code | Cursor | Codex | Cline | Kimi Code |
|------|----------|----------|-------------|--------|-------|-------|-----------|
| **一键安装** | ✅ 原生命令 | ✅ 原生命令 | ⚠️ 手动 | ⚠️ 手动 | ⚠️ 手动 | ⚠️ 手动 | ⚠️ 手动 |
| **持久化配置** | ✅ 全局 | ✅ 全局 | ⚠️ 项目级 | ✅ 全局 | ⚠️ 项目级 | ⚠️ 项目级 | ⚠️ 项目级 |
| **技能自动更新** | ✅ 支持 | ✅ 支持 | ❌ 手动 | ❌ 手动 | ❌ 手动 | ❌ 手动 | ❌ 手动 |
| **技能包安装** | ✅ 支持 | ✅ 支持 | ✅ 支持 | ⚠️ 脚本 | ❌ 不支持 | ❌ 不支持 | ❌ 不支持 |
| **推荐优先级** | ⭐⭐⭐ P0 | ⭐⭐⭐ P0 | ⭐⭐ P1 | ⭐⭐ P1 | ⭐ P2 | ⭐ P2 | ⭐ P2 |

---

## 目录 / Contents

- [OpenCode（推荐）](#opencode推荐)
- [OpenClaw（推荐）](#openclaw推荐)
- [Claude Code](#claude-code)
- [Cursor](#cursor)
- [OpenAI Codex](#openai-codex)
- [Cline](#cline)
- [Kimi Code](#kimi-code)
- [热门技能速查](#热门技能速查)
- [技能分类目录](#技能分类目录)
- [安装验证](#安装验证)
- [常见问题](#常见问题)

---

## OpenCode（推荐）

OpenCode 原生支持技能安装，提供最完整的功能支持。

### 安装单个技能（原生命令）
```
/skill install ceo
```

### 安装技能包（原生命令）
```
/skill install --package executive
/skill install --package tech
/skill install --package ai-ml
```

### 通过 Read 命令安装
```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo/SKILL.md and install ceo skill
```

### 安装全部技能
```
Read https://theneoai.github.io/awesome-skills/INSTALL.md and install all skills
```

**技能存储位置：** `~/.opencode/skills/[skill-name]/SKILL.md`

**特性：**
- ✅ 原生命令支持，最简便
- ✅ 技能持久化到全局配置
- ✅ 支持自动更新

---

## OpenClaw（推荐）

OpenClaw 原生支持通过 `Read ... and install` 命令安装技能。

### 安装单个技能
```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo/SKILL.md and install ceo skill
```

### 安装技能包
```
Read https://github.com/theneoai/awesome-skills/blob/main/packages/executive.md and install executive package
```

### 安装全部技能
```
Read https://theneoai.github.io/awesome-skills/INSTALL.md and install all skills
```

**技能存储位置：** `~/.openclaw/workspace/skills/[skill-name]/SKILL.md`

**特性：**
- ✅ Read 命令原生支持
- ✅ 技能持久化到全局配置
- ✅ 支持技能包批量安装

---

## Claude Code

Claude Code 通过 `CLAUDE.md` 文件或单次会话读取加载技能。

### 方法 1：项目级持久化（推荐）

将技能读取指令追加到项目 `CLAUDE.md`，每次进入项目时自动生效：

```bash
cat >> CLAUDE.md << 'EOF'
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo/SKILL.md and apply the CEO skill guidelines to this project.
EOF
```

### 方法 2：全局持久化

追加到用户级全局配置（适用于所有项目）：

```bash
cat >> ~/.claude/CLAUDE.md << 'EOF'
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo/SKILL.md and apply the CEO skill guidelines.
EOF
```

### 方法 3：单次会话加载

在对话中直接读取技能文件（仅当前会话有效）：

```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo/SKILL.md and install ceo skill
```

### 方法 4：手动复制 System Prompt

1. 打开技能文件（如 `skills/executive/ceo/SKILL.md`）
2. 复制 `§1.1 Role Definition` 代码块中的内容
3. 粘贴到 Claude Project 的"Project Instructions"（全局持久化）

**技能存储位置：**
- 项目级：`./CLAUDE.md`
- 全局：`~/.claude/CLAUDE.md`

**特性：**
- ⚠️ 默认项目级，不跨项目共享
- ⚠️ 技能更新需手动重新加载

---

## Cursor

Cursor 通过 `.cursorrules` 文件应用技能配置。

### 安装单个技能

```bash
# 方法 1：命令行追加（使用 raw URL）
curl -s https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/executive/ceo/SKILL.md >> .cursorrules

# 方法 2：在 Cursor 内提示加载
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo/SKILL.md and append the skill content to .cursorrules
```

### 批量安装多个技能

```bash
BASE_URL="https://raw.githubusercontent.com/theneoai/awesome-skills/main"

for skill in "executive/ceo" "executive/cto" "software/software-architect"; do
  curl -s "${BASE_URL}/skills/${skill}.md" >> .cursorrules
  echo -e "\n---\n" >> .cursorrules
done
```

### 安装技能包

```bash
# 安装 Executive 技能包（CEO、CTO、CFO、COO、CMO）
curl -s https://raw.githubusercontent.com/theneoai/awesome-skills/main/packages/executive.md >> .cursorrules
```

**技能存储位置：** `.cursorrules`（项目根目录）或 `~/.cursor/rules/`（全局）

**特性：**
- ✅ 全局配置，跨项目共享（使用 `~/.cursor/rules/`）
- ⚠️ 技能更新需手动重新下载
- ⚠️ `.cursorrules` 有文件大小限制，建议按需安装

---

## OpenAI Codex

Codex 通过系统提示词（System Prompt）加载技能配置。

### 单次会话安装

```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo/SKILL.md, extract the system prompt and guidelines, and apply as system context for this session.
```

### 持久化配置

1. 打开 Codex 配置文件 `~/.codex/config.yaml`（需 Codex CLI）
2. 在 `system_prompt` 字段中粘贴技能的 `§1.1 Role Definition` 内容：

```yaml
# ~/.codex/config.yaml
system_prompt: |
  You are a seasoned CEO with the following characteristics:
  [粘贴 ceo.md 中 §1.1 Role Definition 代码块内容]
```

> ⚠️ **注意**：Codex 平台的持久化配置方式因版本而异，建议参考 [Codex 官方文档](https://github.com/openai/codex)。

**特性：**
- ⚠️ 默认单次会话有效
- ⚠️ 持久化需手动编辑配置文件

---

## Cline

Cline 作为 VS Code 插件，通过系统提示词或 MCP 服务加载技能。

### 方法 1：单次会话（对话框输入）

```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo/SKILL.md and apply the CEO skill to this session.
```

### 方法 2：通过 `.clinerules` 持久化

在项目根目录创建 `.clinerules` 文件并追加技能内容：

```bash
curl -s https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/executive/ceo/SKILL.md >> .clinerules
```

### 方法 3：自定义指令（Custom Instructions）

在 VS Code Cline 插件设置中，找到"Custom Instructions"字段，粘贴技能文件的 `§1.1 Role Definition` 内容。

**技能存储位置：** `.clinerules`（项目根目录）或 Cline Custom Instructions

**特性：**
- ⚠️ 默认单次会话有效
- ⚠️ 持久化需手动配置

---

## Kimi Code

Kimi Code 支持通过提示词或配置文件加载技能。

### 单次会话安装

```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo/SKILL.md and install ceo skill for this session.
```

### 通过 `.kimiignore` 或项目配置持久化

```bash
# 追加到项目配置
curl -s https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/executive/ceo/SKILL.md >> .kimi-rules
```

> ⚠️ **注意**：Kimi Code 平台适配仍在测试中，安装效果可能因版本而异。建议参考 [Kimi 官方文档](https://kimi.moonshot.cn)获取最新配置方式。

**特性：**
- ⚠️ 功能与其他平台基本一致
- ⚠️ 持久化支持程度因版本而定

---

## 热门技能速查

| 技能 | URL 路径 | 安装命令 |
|------|---------|---------|
| **CEO** | `skills/executive/ceo/SKILL.md` | `Read .../ceo.md and install ceo skill` |
| **CTO** | `skills/executive/cto/SKILL.md` | `Read .../cto.md and install cto skill` |
| **CFO** | `skills/executive/cfo/SKILL.md` | `Read .../cfo.md and install cfo skill` |
| **Software Architect** | `skills/software/software-architect/SKILL.md` | `Read .../software-architect.md and install software-architect skill` |
| **Prompt Engineer** | `skills/ai-ml/prompt-engineer/SKILL.md` | `Read .../prompt-engineer.md and install prompt-engineer skill` |
| **LLM Research Scientist** | `skills/ai-ml/llm-research-scientist/SKILL.md` | `Read .../llm-research-scientist.md and install llm-research-scientist skill` |
| **Clinical Physician** | `skills/healthcare/general-practitioner/SKILL.md` | `Read .../general-practitioner.md and install general-practitioner skill` |
| **Legal Counsel** | `skills/legal/legal-counsel/SKILL.md` | `Read .../legal-counsel.md and install legal-counsel skill` |

**GitHub URL 前缀（blob）：** `https://github.com/theneoai/awesome-skills/blob/main/`

**Raw URL 前缀（curl 下载）：** `https://raw.githubusercontent.com/theneoai/awesome-skills/main/`

---

## 技能分类目录

| 分类 | 路径 | 代表技能 |
|------|------|---------|
| 高管 Executive | `skills/executive/` | CEO, CTO, CFO, COO, CMO |
| AI & ML | `skills/ai-ml/` | Prompt Engineer, LLM Scientist, AI PM |
| 软件开发 Software | `skills/software/` | Software Architect, DevOps, Security |
| 金融 Finance | `skills/finance/` | Financial Analyst, Investment Analyst, CPA |
| 医疗 Healthcare | `skills/healthcare/` | Clinical Physician, Psychologist |
| 法律 Legal | `skills/legal/` | Legal Counsel, Patent Attorney |
| 市场营销 Marketing | `skills/marketing/` | Digital Marketing, Sales Manager |
| 产品 Product | `skills/product/` | Product Manager, UX Designer |
| 数据 Data | `skills/data/` | Data Analyst, Data Engineer |
| 研究 Research | `skills/research/` | Principal Investigator, Statistician |

**查看全部 460+ 技能 → [CATALOG.md](./CATALOG.md)**

---

## 安装验证

安装技能后，使用以下方式验证效果：

1. 提问该领域专业问题
2. 检查 AI 是否使用框架式回答（而非泛泛而谈）
3. 对比安装前后的回答风格

**示例验证问题（CEO 技能）：**
> "我们公司现金流紧张，应该裁员还是融资？"

**期望行为：**
- 提供分析框架（财务指标、利益相关者、方案对比）
- 要求量化数据而非直接给出答案
- 考虑非财务因素（团队士气、市场信号）
- 推荐具体工具（13-week cash flow forecast）

---

## 常见问题

### Q: 技能安装后没有明显效果？

检查以下几点：
1. 确认技能文件 URL 可以正常访问
2. 在新对话中测试（避免旧上下文影响）
3. 主动提及你安装的技能身份（如"以 CEO 视角分析..."）

### Q: 如何同时安装多个技能？

推荐使用技能包：
```
Read https://github.com/theneoai/awesome-skills/blob/main/packages/executive.md and install executive package
```

### Q: Claude Code 安装的技能如何卸载？

删除 `CLAUDE.md` 或 `~/.claude/CLAUDE.md` 中对应的技能读取指令。

### Q: Cursor 的 `.cursorrules` 文件太大怎么办？

建议仅保留当前项目最相关的 1-3 个技能，或将完整内容移至 `~/.cursor/rules/` 全局配置中。

### Q: 技能文件更新后如何同步？

重新运行安装命令即可覆盖旧版本。OpenCode 和 OpenClaw 支持自动更新。

---

**← [快速安装](./INSTALL.md)** | **[技能目录](./CATALOG.md)** | **[贡献指南](./CONTRIBUTING.md)**
