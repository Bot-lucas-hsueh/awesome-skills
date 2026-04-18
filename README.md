<!-- Awesome Skills -->
<!-- Language: [English](#english) | [中文](#中文) -->

<div align="center">

# Awesome Skills

**A curated library of role-based AI skills, organised by professional domain.**

[![Skills](https://img.shields.io/badge/skills-943-blueviolet?style=flat-square)](./CATALOG.md)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![Pages](https://github.com/theneoai/awesome-skills/actions/workflows/pages-deploy.yml/badge.svg)](https://github.com/theneoai/awesome-skills/actions/workflows/pages-deploy.yml)

**[🌐 Website](https://theneoai.github.io/awesome-skills/)** · **[📚 Catalog](./CATALOG.md)** · **[📖 Install Guide](./INSTALL-GUIDE.md)** · **[🤝 Contributing](./CONTRIBUTING.md)**

**Language:** [English](#english) | [中文](#中文)

</div>

---

<a name="english"></a>
## English

### What this is

A library of **943 skill files** (`SKILL.md` + optional `references/`) covering 60 professional domains. Each skill is a role-based prompt pack — an instruction set plus reference material — designed to load into Claude Code, OpenCode, Cursor, or similar agent runtimes to give an LLM a consistent professional persona and working methodology.

### What this is NOT

- **Not an alternative to executable skill packs.** The official Anthropic/OpenAI `SKILL.md` convention can ship with `scripts/` and `assets/` that the agent runs. The vast majority of skills here are **persona + methodology**, not runnable tools. Treat them as opinionated system prompts, not as plugins.
- **Not a certification body.** Historical quality scores in this repo were produced by a self-authored scoring script grading against a self-authored rubric. The scoring is useful internally; it is not an independent benchmark.
- **Not feature-complete for every domain.** Coverage is broad but uneven — some categories have deep role hierarchies, others have a single stub.

### Layout

```
skills/                   841 first-party skill directories across ~60 categories
  <category>/<role>/
    SKILL.md              Frontmatter + system prompt (target ≤ 300 lines)
    references/           On-demand deep content (workflow / scenarios / …)
    EVALUATION_REPORT.md  Optional self-scored quality report

external/                 Registry of 10 curated third-party skill repos
                          (anthropics/skills, VoltAgent, awesome-claude-code, …).
                          Pulled on demand via scripts/sync_external.py — not vendored.
benchmarks/               Evaluation dataset + scoring script for comparison
packages/                 Curated skill bundles by domain
roadmap/                  Career-path documents (independent of skills/)
taxonomy.yml              Single source of truth mapping skills/packages/roadmap → 18 top-level categories
tools/                    Python package for skill analysis (scoring, tokens, anti-patterns)
scripts/                  Maintenance scripts (catalog regen, external sync, taxonomy check, …)
.github/                  CI workflows + scripts, CI/CD docs
```

### Quick start

The simplest way to install a skill is to have your agent read its `SKILL.md` URL:

```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo/SKILL.md and install as a skill
```

Platform-specific instructions (OpenCode native command, Claude Code, Cursor, Cline, Codex, Kimi) are in **[INSTALL-GUIDE.md](./INSTALL-GUIDE.md)**.

### Skill packages

Pre-bundled collections in `packages/`:

| Package | Focus |
|---------|-------|
| [tech](./packages/tech.md) | Software, AI/ML, data |
| [executive](./packages/executive.md) | CEO, CTO, CFO, COO, CMO |
| [finance](./packages/finance.md) | Banking, consulting, investment |
| [healthcare](./packages/healthcare.md) | Clinical and medical management |
| [software](./packages/software.md) | Backend, frontend, devops, QA |

### Featured enterprise skills

Role skills modelled after the methodology of specific companies (15 shown out of 100+ under `skills/enterprise/`):

| Skill | Company | Methodology |
|-------|---------|------------|
| [amazon-engineer](./skills/enterprise/amazon/amazon-engineer/SKILL.md) | Amazon | 14 LPs, Working Backwards, 6-page memos |
| [tesla-engineer](./skills/enterprise/tesla/tesla-engineer/SKILL.md) | Tesla | First principles, five-step algorithm |
| [spacex-engineer](./skills/enterprise/spacex/spacex-engineer/SKILL.md) | SpaceX | Rapid iteration, cost innovation |
| [nvidia-ml-engineer](./skills/enterprise/nvidia/nvidia-ml-engineer/SKILL.md) | NVIDIA | CUDA optimisation, GPU platforms |
| [mckinsey-consultant](./skills/enterprise/mckinsey/mckinsey-consultant/SKILL.md) | McKinsey | MECE, issue trees, pyramid principle |
| [toyota-engineer](./skills/enterprise/toyota/toyota-engineer/SKILL.md) | Toyota | TPS, JIT, Kaizen, Jidoka |
| [anthropic-researcher](./skills/enterprise/anthropic/anthropic-researcher/SKILL.md) | Anthropic | Constitutional AI, interpretability |

Full list in [CATALOG.md](./CATALOG.md).

### External ecosystem hub

`external/` is a **registry** of top third-party skill / subagent / plugin repositories —
not a mirror. Pull any subset on demand:

```bash
python3 scripts/sync_external.py --list                 # see what's registered
python3 scripts/sync_external.py --all                  # shallow-clone everything
python3 scripts/sync_external.py --slug anthropics-skills
```

Registered sources (see [`external/README.md`](./external/README.md) for the full table):

| Category | Repos |
|----------|-------|
| Official (Anthropic) | [`anthropics/skills`](https://github.com/anthropics/skills), [`claude-plugins-official`](https://github.com/anthropics/claude-plugins-official), [`knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins) |
| Curated lists | [`VoltAgent/awesome-agent-skills`](https://github.com/VoltAgent/awesome-agent-skills), [`hesreallyhim/awesome-claude-code`](https://github.com/hesreallyhim/awesome-claude-code), [`travisvn/awesome-claude-skills`](https://github.com/travisvn/awesome-claude-skills), [`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) |
| Subagents & orchestration | [`VoltAgent/awesome-claude-code-subagents`](https://github.com/VoltAgent/awesome-claude-code-subagents), [`wshobson/agents`](https://github.com/wshobson/agents), [`0xfurai/claude-code-subagents`](https://github.com/0xfurai/claude-code-subagents) |

To propose a new source, edit [`external/sources.yml`](./external/sources.yml) and open a PR.
External clones are gitignored and never linted by our CI — we are a pointer, not an enforcer.

### Tooling

The repo ships a Python package for static analysis of skills:

```bash
pip install -e ./tools/
python -m tools.skill_analyzer.cli score        # 8-dimension rubric scores
python -m tools.skill_analyzer.cli tokenizer    # Token budget + API cost
python -m tools.skill_analyzer.cli antipattern  # Common mistakes scanner
```

CI (`.github/workflows/quality.yml`) runs these on every PR and **blocks merges** whose changed `SKILL.md` files fall below score/token/description thresholds.

### Known limitations

- **Text-only skills.** Virtually no skill ships executable `scripts/` or `assets/` — they are persona prompts.
- **Description overlap.** The role taxonomy is fine-grained (60 categories, 842 roles) and many descriptions overlap, which hurts automatic skill-discovery in agent runtimes. A description-similarity linter is planned.
- **Self-scored quality.** `EVALUATION_REPORT.md` files reflect a self-graded rubric, not external review.
- **Three category systems.** `packages/` (14), `roadmap/` (22), and `skills/` (60) use different taxonomies — being consolidated.

### Documentation

| Doc | Purpose |
|-----|---------|
| [CATALOG.md](./CATALOG.md) | Full catalog of all skills |
| [INSTALL-GUIDE.md](./INSTALL-GUIDE.md) | Platform-specific install instructions |
| [CONTRIBUTING.md](./CONTRIBUTING.md) | How to add or improve skills |
| [.github/CI.md](./.github/CI.md) | CI/CD pipeline notes |

### License

MIT — see [LICENSE](./LICENSE).

---

<a name="中文"></a>
## 中文

### 项目定位

按专业领域组织的 **AI Skill 库**，共 **943 个技能**，覆盖 60 个领域。每个技能是一份 `SKILL.md`（+ 可选 `references/`），本质是**角色化的提示词包**——一套系统指令加参考资料，用于在 Claude Code / OpenCode / Cursor 等 agent 运行时里给 LLM 加载稳定的专业身份和工作方法。

### 不是什么

- **不是可执行 Skill 套件**。Anthropic/OpenAI 官方 `SKILL.md` 可以随包携带 `scripts/` 和 `assets/` 交给 agent 调用；本仓库绝大多数 skill 仅提供**角色 + 方法论**的文本，应视作有观点的系统提示词，而非可运行插件。
- **不是第三方认证**。仓库内历史质量分由本仓库自己编写的脚本按自家标准打出，对内有参考价值，但不是独立基准。
- **不是每个领域都覆盖完整**。分类很广但深浅不一：有些领域有完整角色树，有些只有一个占位文件。

### 目录结构

```
skills/                   841 个自产技能目录，分 ~60 个分类
  <category>/<role>/
    SKILL.md              Frontmatter + 系统提示词（目标 ≤ 300 行）
    references/           按需加载的深度内容（workflow / scenarios / …）
    EVALUATION_REPORT.md  可选：自评质量报告

external/                 10 个精选第三方 skill 仓库的注册表
                          （anthropics/skills、VoltAgent、awesome-claude-code 等）
                          通过 scripts/sync_external.py 按需拉取，不随仓库 vendored
benchmarks/               评估数据集 + 评分脚本
packages/                 按领域打包的 skill 合集
roadmap/                  职业路径文档（独立于 skills/）
taxonomy.yml              skills/packages/roadmap → 18 顶层分类 的唯一真源
tools/                    Skill 分析工具 Python 包（评分、token、反模式）
scripts/                  维护脚本（catalog 重生成、external 同步、taxonomy 检查等）
.github/                  CI 工作流与脚本、CI/CD 文档
```

### 快速开始

最通用的安装方式是让 agent 读 SKILL.md 的 URL：

```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo/SKILL.md 并安装为 skill
```

各平台（OpenCode 原生命令、Claude Code、Cursor、Cline、Codex、Kimi）详细步骤见 **[INSTALL-GUIDE.md](./INSTALL-GUIDE.md)**。

### Skill 合集

按领域打包，见 `packages/`：

| 合集 | 覆盖 |
|------|------|
| [tech](./packages/tech.md) | 软件、AI/ML、数据 |
| [executive](./packages/executive.md) | CEO、CTO、CFO、COO、CMO |
| [finance](./packages/finance.md) | 银行、咨询、投资 |
| [healthcare](./packages/healthcare.md) | 临床与医疗管理 |
| [software](./packages/software.md) | 后端、前端、devops、QA |

### 精选企业技能

仿照特定公司方法论建模的角色（从 `skills/enterprise/` 100+ 条中选 7 条）：

| Skill | 公司 | 方法论 |
|-------|------|--------|
| [amazon-engineer](./skills/enterprise/amazon/amazon-engineer/SKILL.md) | Amazon | 14 条领导力准则、Working Backwards、6 页备忘录 |
| [tesla-engineer](./skills/enterprise/tesla/tesla-engineer/SKILL.md) | Tesla | 第一性原理、五步算法 |
| [spacex-engineer](./skills/enterprise/spacex/spacex-engineer/SKILL.md) | SpaceX | 快速迭代、成本创新 |
| [nvidia-ml-engineer](./skills/enterprise/nvidia/nvidia-ml-engineer/SKILL.md) | NVIDIA | CUDA 优化、GPU 平台 |
| [mckinsey-consultant](./skills/enterprise/mckinsey/mckinsey-consultant/SKILL.md) | McKinsey | MECE、Issue Tree、金字塔原理 |
| [toyota-engineer](./skills/enterprise/toyota/toyota-engineer/SKILL.md) | Toyota | TPS、JIT、改善、自働化 |
| [anthropic-researcher](./skills/enterprise/anthropic/anthropic-researcher/SKILL.md) | Anthropic | Constitutional AI、可解释性 |

完整列表见 [CATALOG.md](./CATALOG.md)。

### 外部生态集散地

`external/` 是业界优秀 skill / subagent / plugin 仓库的**注册表**（非镜像），按需拉取任意子集：

```bash
python3 scripts/sync_external.py --list                 # 查看注册的仓库
python3 scripts/sync_external.py --all                  # 全量浅拉取
python3 scripts/sync_external.py --slug anthropics-skills
```

已注册仓库（完整表格见 [`external/README.md`](./external/README.md)）：

| 类别 | 仓库 |
|------|------|
| 官方（Anthropic） | [`anthropics/skills`](https://github.com/anthropics/skills)、[`claude-plugins-official`](https://github.com/anthropics/claude-plugins-official)、[`knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins) |
| 社区精选列表 | [`VoltAgent/awesome-agent-skills`](https://github.com/VoltAgent/awesome-agent-skills)、[`hesreallyhim/awesome-claude-code`](https://github.com/hesreallyhim/awesome-claude-code)、[`travisvn/awesome-claude-skills`](https://github.com/travisvn/awesome-claude-skills)、[`ComposioHQ/awesome-claude-skills`](https://github.com/ComposioHQ/awesome-claude-skills) |
| Subagent 与编排 | [`VoltAgent/awesome-claude-code-subagents`](https://github.com/VoltAgent/awesome-claude-code-subagents)、[`wshobson/agents`](https://github.com/wshobson/agents)、[`0xfurai/claude-code-subagents`](https://github.com/0xfurai/claude-code-subagents) |

提议新增来源：编辑 [`external/sources.yml`](./external/sources.yml) 并提交 PR。
`external/` 下的本地克隆已加入 `.gitignore`，也不被 CI 扫描——我们是**指针**，不是上游的审阅者。

### 工具

仓库附带 Python 分析包：

```bash
pip install -e ./tools/
python -m tools.skill_analyzer.cli score        # 8 维度评分
python -m tools.skill_analyzer.cli tokenizer    # Token 预算与 API 成本
python -m tools.skill_analyzer.cli antipattern  # 反模式扫描
```

CI（`.github/workflows/quality.yml`）会在每个 PR 上运行这些工具，若新改动的 `SKILL.md` 达不到阈值则**阻塞合并**。

### 已知局限

- **绝大多数 skill 是纯文本 persona**，并不随包携带可执行 `scripts/` 或 `assets/`。
- **描述重叠严重**：60 分类 × 842 角色，许多 description 字段相似度高，会降低 agent 运行时的 skill 自动发现准确度。计划引入描述相似度检查。
- **质量分是自评**：`EVALUATION_REPORT.md` 反映仓库自家规则的评分，不是独立评审。
- **三套分类互不一致**：`packages/`（14 类）、`roadmap/`（22 类）、`skills/`（60 类）仍在统一中。

### 文档

| 文档 | 用途 |
|------|------|
| [CATALOG.md](./CATALOG.md) | 完整技能目录 |
| [INSTALL-GUIDE.md](./INSTALL-GUIDE.md) | 各平台安装步骤 |
| [CONTRIBUTING.md](./CONTRIBUTING.md) | 如何贡献或改进技能 |
| [.github/CI.md](./.github/CI.md) | CI/CD 说明 |

### 许可证

MIT，见 [LICENSE](./LICENSE)。

---

<div align="center">

**[↑ Back to top](#awesome-skills)**

</div>
