# Awesome Skills — 全面重构优化方案
<!-- Awesome Skills — Comprehensive Refactoring & Optimization Plan -->

> **版本**: v1.0.0 | **日期**: 2026-02-19 | **状态**: 待审批

---

## 一、现状诊断 / Current State Diagnosis

### 1.1 全局指标

| 维度 | 当前值 | 目标值 | 差距 |
|------|--------|--------|------|
| 技能总数 | 464 | 464 | — |
| ⭐ Expert Verified | ~20 (4.3%) | 50 (10.8%) | +30 |
| ✅ Community Verified | ~50 (10.8%) | 150 (32.3%) | +100 |
| 📝 Basic（低效占比） | ~394 (84.9%) | <264 (56.9%) | -130 |
| 元数据完整率 | ~25% | 100% | +75% |
| 模板合规率（16节） | ~1% | 80%（Top 50） | +79% |
| 自动化测试覆盖 | 0% | 核心流水线 100% | +100% |
| CI/CD | 无 | GitHub Actions 全覆盖 | — |

### 1.2 核心问题诊断

#### P0 — 阻塞性问题（立即修复）

| # | 问题 | 影响范围 | 严重程度 |
|---|------|----------|----------|
| P0-1 | **82% 技能是无效占位符**：安装后 AI 行为无任何变化 | 394 个文件 | 致命 |
| P0-2 | **零自动化验证**：YAML 格式错误、模板违规长期积累无人发现 | 全部 464 文件 | 严重 |
| P0-3 | **YAML frontmatter HTML 注释注入**：`description` 字段含 `<!--` 导致部分平台解析失败 | 数十个文件 | 严重 |

#### P1 — 高优先级问题（本季度修复）

| # | 问题 | 影响范围 | 严重程度 |
|---|------|----------|----------|
| P1-1 | **元数据字段缺失率 75%**：`difficulty`、`category`、`tags`、`platforms` 普遍缺失 | ~350 个文件 | 高 |
| P1-2 | **平台支持声明虚假**：7 个平台均声明支持但仅 1-2 个有实际安装说明 | 全部文件 | 高 |
| P1-3 | **双语格式不统一**：Expert 技能严格执行；Basic 技能完全忽略 | ~400 个文件 | 中高 |
| P1-4 | **版本号停滞**：95% 文件停在 v1.0.0，无法追踪改进历史 | ~440 个文件 | 中 |

#### P2 — 中优先级问题（下季度修复）

| # | 问题 | 影响范围 |
|---|------|----------|
| P2-1 | 包（packages）纯链接列表，无聚合逻辑 | 14 个包文件 |
| P2-2 | 触发词过于宽泛（"create"、"write"）导致误触发 | 若干技能 |
| P2-3 | index.html 硬编码技能列表，文件结构变化即失效 | 网站首页 |
| P2-4 | 文档交叉引用形成环形依赖（4 个治理文档互相引用） | 治理文档 |

---

## 二、重构策略总体设计 / Refactoring Strategy

### 2.1 核心原则

```
精 > 广       质量优先于数量
可验证 > 声明  每项改进必须可自动测量
渐进式 > 大爆炸 不破坏现有可用技能
```

### 2.2 技能质量金字塔（目标态）

```
        ⭐ Expert Verified
        50 skills (11%)
       ─────────────────────
      ✅ Community Verified
      150 skills (32%)
     ─────────────────────────
    📝 Basic（有内容，待升级）
    264 skills (57%)
   ───────────────────────────
  🗑️ 已归档 / 合并（不再展示）
  若干重复或空洞技能
```

### 2.3 三条并行改进轨道

| 轨道 | 目标 | 主要交付物 |
|------|------|------------|
| **Track A - 内容质量** | Top 50 技能达到 Expert 标准 | 50 个高质量技能文件 |
| **Track B - 工程基础** | 自动化验证 + CI/CD | GitHub Actions 流水线 |
| **Track C - 用户体验** | 安装体验统一 + 文档精简 | 重构后的 README、INSTALL 系列 |

---

## 三、分阶段实施计划 / Phased Implementation Plan

---

### Phase 0: 工程基础设施（优先级 P0，前置条件）

**目标**：建立自动化护栏，所有后续改进在验证框架下进行。

#### 0.1 YAML / Markdown 验证脚本

新建 `.github/scripts/validate_skills.py`：

```python
# 验证逻辑（伪代码）
for each skill in skills/**/*.md:
    frontmatter = parse_yaml(skill)

    # 必填字段检查
    assert frontmatter.name        # 存在且格式合法
    assert frontmatter.version     # 语义版本格式
    assert frontmatter.category    # 与目录匹配
    assert frontmatter.difficulty  # expert|intermediate|beginner
    assert frontmatter.tags        # 3-5 个标签
    assert frontmatter.platforms   # 非空列表

    # HTML 注释注入检查（P0-3）
    assert "<!--" not in frontmatter.description

    # 内容结构检查（Top 50 技能强制要求）
    if skill is in top_50_list:
        assert has_section("## 1. System Prompt")
        assert has_code_block_in_section("1.1 Role Definition")
        assert has_section("## 2. What This Skill Does")
```

#### 0.2 GitHub Actions CI 流水线

新建 `.github/workflows/validate.yml`：

```yaml
name: Skill Validation
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate frontmatter & structure
        run: python .github/scripts/validate_skills.py
      - name: Check broken links
        run: npx markdown-link-check skills/**/*.md --config .mlc-config.json
      - name: Lint YAML
        run: yamllint skills/**/*.md
```

#### 0.3 交付物清单

- [ ] `.github/scripts/validate_skills.py`
- [ ] `.github/workflows/validate.yml`
- [ ] `.yamllint` 配置文件
- [ ] `.mlc-config.json` 断链检测配置
- [ ] `.editorconfig`（编辑器一致性）

**验收标准**：PR 触发 CI，所有现有 Expert Verified 技能通过验证。

---

### Phase 1: 精品技能深度化（优先级 P0）

**目标**：将 Top 20 → Top 50 技能全部提升至 Expert Verified 标准。

#### 1.1 Expert Verified 技能标准（量化定义）

技能必须满足以下全部条件才能标注 ⭐：

| 维度 | 最低要求 |
|------|----------|
| **系统提示词** | `§1.1` 含 Identity / Writing Style / Core Expertise 三段结构代码块 |
| **决策框架** | `§1.2` 含 3 行以上决策关卡表格 |
| **思维模式** | `§1.3` 含 3 维度以上思维模式表格 |
| **知识框架** | `§6` 含 3+ 个专业框架（含使用场景和关键步骤） |
| **场景示例** | `§8` 含 3+ 个真实场景，每个场景含输入/输出示例 |
| **风险声明** | `§3` 含 4+ 条领域特定风险警告 |
| **元数据完整** | 全部 9 个 frontmatter 字段填写完整 |
| **字数下限** | 正文 ≥ 500 行 |

#### 1.2 优先升级列表（按优先级排序）

**P0 — 立即开始（高频 + 已有基础）**

| 技能 | 当前版本 | 文件路径 | 升级工作量 |
|------|----------|----------|------------|
| CEO | v2.0+ | `skills/executive/ceo.md` | 已完成，保持 |
| CTO | — | `skills/executive/cto.md` | 中 |
| Software Architect | — | `skills/software/software-architect.md` | 中 |
| Prompt Engineer | — | `skills/ai-ml/prompt-engineer.md` | 低（主题契合） |
| Product Manager | — | `skills/business/product-manager.md` | 中 |
| skill-writer | v11.0 | `skills/admin/skill-writer.md` | 已完成，保持 |

**P1 — 第二批**

| 技能 | 类别 | 理由 |
|------|------|------|
| Data Scientist | Tech | 高需求，框架丰富 |
| Legal Counsel | Legal | 专业壁垒高 |
| Clinical Physician | Healthcare | 风险声明尤为重要 |
| Investment Analyst | Finance | 量化框架丰富 |
| DevOps Engineer | Tech | 工程实践标准化 |
| CFO | Executive | 财务专业深度 |
| Cybersecurity Engineer | Security | 专业性强 |
| UI/UX Designer | Creative | 设计思维可量化 |
| Marketing Manager | Marketing | GTM 框架丰富 |
| Project Manager | Management | 方法论成熟 |

**P2 — 第三批**

| 技能 | 类别 |
|------|------|
| Research Scientist | Research |
| Supply Chain Expert | Logistics |
| HR Expert | HR |
| Financial Analyst | Finance |
| Copywriter | Creative |
| Data Engineer | Tech |
| ML Engineer | AI/ML |
| Backend Engineer | Software |
| Frontend Engineer | Software |
| QA Engineer | Software |

#### 1.3 技能升级标准工作流

```
1. 阅读现有文件（了解已有内容）
2. 对照 TEMPLATE.md 识别缺失章节
3. 按 §1 → §6 → §8 → §3 顺序补充
4. 运行验证脚本确认合规
5. 更新版本号（遵循语义版本）
6. 更新 CATALOG.md 质量标签
7. PR + 代码审查
```

---

### Phase 2: 元数据标准化（优先级 P1）

**目标**：全部 464 个技能文件的 YAML frontmatter 100% 合规。

#### 2.1 自动修复策略

编写 `.github/scripts/fix_frontmatter.py`：

```python
# 自动推断并填充缺失字段
for each skill_file:
    # 从文件路径推断 category
    category = skill_file.parent.name  # skills/finance/ → finance

    # 从文件名推断 name
    name = skill_file.stem  # investment-analyst.md → investment-analyst

    # 从标题推断 display_name（需要人工确认）
    display_name = extract_h1_title(skill_file)

    # 默认值填充
    if not frontmatter.difficulty:
        frontmatter.difficulty = "intermediate"  # 安全默认值

    if not frontmatter.platforms:
        frontmatter.platforms = ["opencode", "openclaw", "claude", "cursor", "codex", "cline", "kimi"]

    # 修复 HTML 注释注入（P0-3）
    frontmatter.description = remove_html_comments(frontmatter.description)
```

#### 2.2 需要人工确认的字段

| 字段 | 自动化可行性 | 需要人工处理 |
|------|-------------|-------------|
| `name` | ✅ 从文件名推断 | 仅命名冲突时 |
| `category` | ✅ 从目录推断 | 无 |
| `difficulty` | ⚠️ 基于字数估算 | 建议人工复核 |
| `tags` | ❌ 无法自动生成 | 每个技能需提供 3-5 个 |
| `description` | ⚠️ 从正文提取第一段 | 建议人工润色 |
| `display_name` | ⚠️ 从 H1 提取 | 中文部分需人工翻译 |

#### 2.3 tags 标准词汇表（部分）

为确保 tags 一致性，建立标准词汇：

```yaml
# 职能标签
management, strategy, finance, legal, healthcare, technology,
engineering, design, marketing, research, education, operations

# 技能标签
decision-making, frameworks, analysis, planning, communication,
risk-assessment, data-driven, cross-functional

# 难度标签（与 difficulty 字段对应）
expert, intermediate, beginner
```

---

### Phase 3: 内容治理与去冗余（优先级 P1）

**目标**：识别并处理 394 个 Basic 技能，停止"广而浅"的扩张。

#### 3.1 技能分类决策树

```
对每个 Basic 技能：

是否与其他技能高度重复（>70% 内容相同）？
├── 是 → 合并到主技能，添加重定向注释，原文件删除
└── 否 → 继续评估

是否有真实用户使用需求（GitHub Issues/Stars/Forks 相关）？
├── 否 → 移入 /skills/_archived/ 目录，CATALOG.md 中隐藏
└── 是 → 继续评估

是否有人愿意贡献内容？
├── 否 → 保留模板骨架，标注 "Contributions Welcome"
└── 是 → 分配给贡献者，进入 Phase 1 升级流程
```

#### 3.2 公共内容提取

当前 464 个文件中存在大量重复的安装说明和许可证声明。重构策略：

**新建 `skills/_common/installation.md`**：
```markdown
# 安装指南（公共引用）
所有技能文件中的平台安装说明统一引用此文件，
避免在 464 个文件中重复维护相同内容。
```

**技能文件安装章节精简方案**：

```markdown
## Installation / 安装

→ 详见 [通用安装指南](../_common/installation.md)

**快速安装（OpenCode/OpenClaw）：**
\`\`\`
Read [URL] and install [skill-name] skill
\`\`\`
```

#### 3.3 预计处理结果

| 处理方式 | 预计数量 | 说明 |
|----------|----------|------|
| 升级为 Community Verified | ~100 | 补充内容后达到基本标准 |
| 保留 Basic（有内容骨架） | ~200 | 等待社区贡献 |
| 归档（重复/空洞） | ~94 | 移入 `_archived/` |
| 合并（近似技能） | ~20 | 如 "Actor" + "Voice Actor" |

---

### Phase 4: 平台适配完善（优先级 P1）

**目标**：将平台支持从"声明"变为"已验证"。

#### 4.1 平台验证矩阵

| 功能 | OpenCode | OpenClaw | Claude Code | Cursor | Codex | Cline | Kimi |
|------|----------|----------|-------------|--------|-------|-------|------|
| 安装命令 | ✅ 已测 | ✅ 已测 | ⚠️ 待测 | ⚠️ 待测 | ❌ 待定 | ⚠️ 待测 | ❌ 待定 |
| 持久化 | ✅ | ✅ | ⚠️ 项目级 | ✅ `.cursorrules` | ⚠️ | ⚠️ | ❓ |
| 技能更新 | ✅ 自动 | ✅ 自动 | ❌ 手动 | ❌ 手动 | ❌ | ❌ | ❓ |
| 多技能并行 | ✅ | ✅ | ⚠️ | ⚠️ | ❓ | ⚠️ | ❓ |

**每个平台的验收测试**：
1. 安装 CEO 技能
2. 提问："帮我制定公司战略"
3. 验证 AI 是否使用了框架式回答（而非泛泛而谈）
4. 记录测试结果到平台对应的 `INSTALL-GUIDE.md`

#### 4.2 安装文档重构

当前问题：`INSTALL.md`、`INSTALL-COMMANDS.md`、`INSTALL-GUIDE.md` 三个文件内容重叠、互相矛盾。

**重构方案**：

```
INSTALL.md          → 保留：用户快速上手入口（<50 行）
INSTALL-GUIDE.md    → 重构：每平台详细图文步骤
INSTALL-COMMANDS.md → 删除：内容合并入 INSTALL-GUIDE.md
```

新 `INSTALL-GUIDE.md` 结构：
```markdown
# 平台安装指南

## OpenCode（推荐）
## OpenClaw
## Claude Code
## Cursor
## OpenAI Codex（待测试，不保证有效）
## Cline
## Kimi Code（待测试，不保证有效）
```

---

### Phase 5: 社区生态建设（优先级 P2）

**目标**：建立可持续的社区贡献机制。

#### 5.1 贡献流程优化

**当前贡献流程痛点**：
- CONTRIBUTING.md 400 行，信息过载
- 新贡献者不清楚从哪里开始
- 没有 "Good First Issue" 标签或指引

**优化后流程**：

```
新贡献者入口
     ↓
选择贡献类型：
A. 改进现有技能  → 查看 CATALOG.md 中的 📝 Basic 列表
B. 新增技能      → 先开 Issue 确认需求，再提 PR
C. 测试平台适配  → 查看 Phase 4 平台验证矩阵

每种类型都有对应的 PR 模板（.github/PULL_REQUEST_TEMPLATE/）
```

#### 5.2 GitHub 工作流优化

新建以下 GitHub 配置：

```
.github/
├── ISSUE_TEMPLATE/
│   ├── new-skill.yml          # 新技能提案
│   ├── improve-skill.yml      # 现有技能改进
│   └── platform-test.yml      # 平台适配测试报告
├── PULL_REQUEST_TEMPLATE/
│   ├── new-skill.md
│   └── improve-skill.md
└── workflows/
    ├── validate.yml           # Phase 0 实现
    ├── auto-label.yml         # 自动标签
    └── catalog-update.yml     # PR 合并后自动更新 CATALOG.md
```

#### 5.3 质量分级自动化

当前 CATALOG.md 手动维护，随时滞后。

**自动化方案**：

```python
# .github/scripts/update_catalog.py
# 每次 PR 合并后运行，重新生成 CATALOG.md

for each skill:
    score = calculate_quality_score(skill)
    # score 基于：字数、章节数、frontmatter 完整度、有无代码块示例

    if score >= 90:
        tier = "⭐ Expert Verified"
    elif score >= 60:
        tier = "✅ Community Verified"
    else:
        tier = "📝 Basic"

    update_catalog_entry(skill, tier)
```

---

## 四、工具链建议 / Recommended Toolchain

| 工具 | 用途 | 配置文件 |
|------|------|----------|
| `yamllint` | YAML frontmatter 语法验证 | `.yamllint` |
| `markdownlint` | Markdown 格式检查 | `.markdownlint.json` |
| `markdown-link-check` | 断链检测 | `.mlc-config.json` |
| `prettier` | 统一代码格式 | `.prettierrc` |
| `pre-commit` | 本地提交前钩子 | `.pre-commit-config.yaml` |
| GitHub Actions | CI/CD 流水线 | `.github/workflows/` |

### 最小可行配置（立即可部署）

**.yamllint**:
```yaml
extends: default
rules:
  line-length: disable
  truthy:
    allowed-values: ['true', 'false']
```

**.markdownlint.json**:
```json
{
  "MD013": false,
  "MD033": false,
  "MD041": false
}
```

**.pre-commit-config.yaml**:
```yaml
repos:
  - repo: https://github.com/adrienverge/yamllint
    rev: v1.35.1
    hooks:
      - id: yamllint
        files: \.md$
  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.43.0
    hooks:
      - id: markdownlint
```

---

## 五、成功指标 / Success Metrics

### 内容质量指标

| 指标 | 当前值 | Phase 1 目标 | 最终目标 |
|------|--------|-------------|---------|
| Expert Verified 技能数 | ~20 | 30 | 50 |
| Community Verified 技能数 | ~50 | 80 | 150 |
| 平均技能字数（Top 50） | ~200 行 | 400 行 | 600+ 行 |
| 元数据完整率 | ~25% | 80% | 100% |

### 工程质量指标

| 指标 | 当前值 | 目标 |
|------|--------|------|
| CI 通过率 | N/A（无 CI） | 100% |
| 断链数量 | 未知 | 0 |
| YAML 语法错误 | 未知 | 0 |
| PR 平均合并时间 | 无数据 | <72h |

### 用户体验指标

| 指标 | 衡量方式 | 目标 |
|------|----------|------|
| 安装成功率（CEO 技能） | 用户测试 | >95% |
| 安装后 AI 行为变化可感知 | A/B 测试 | >90% 用户感知到差异 |
| 新贡献者首次 PR 成功率 | GitHub 数据 | >70% |

---

## 六、风险矩阵 / Risk Matrix

| 风险 | 概率 | 影响 | 缓解策略 |
|------|------|------|----------|
| 大规模修改破坏现有可用技能 | 中 | 高 | Phase 0 先建验证基线，渐进式修改 |
| 元数据自动填充不准确 | 高 | 中 | 所有自动填充经人工审核后合并 |
| 社区贡献质量参差不齐 | 高 | 中 | CI 强制验证 + PR 模板约束 |
| 平台接口变化导致安装失效 | 低 | 高 | 定期（每月）平台适配验证 |
| 维护者单点瓶颈 | 高 | 高 | 培育 2-3 名核心 Reviewer |

---

## 七、执行优先级总结 / Execution Priority Summary

```
立即执行（本周）:
  ✦ Phase 0.1: 编写 validate_skills.py
  ✦ Phase 0.2: 配置 GitHub Actions
  ✦ Phase 2.1: 批量修复 HTML 注释注入（P0-3 Bug）

本月执行:
  ✦ Phase 1: CTO、Software Architect、Prompt Engineer 升级为 Expert Verified
  ✦ Phase 2.2: 批量修复元数据缺失（自动化脚本）
  ✦ Phase 4.2: INSTALL 文档合并重构

本季度执行:
  ✦ Phase 1: 完成全部 Top 20 升级
  ✦ Phase 3: Basic 技能分类与归档
  ✦ Phase 5: GitHub Issue/PR 模板部署

长期持续:
  ✦ Phase 1 扩展：Top 20 → Top 50
  ✦ Phase 5: 社区生态建设
  ✦ 平台适配持续验证
```

---

## 八、附录：技能质量评分模型 / Appendix: Quality Scoring Model

基于 skill-writer 分析框架，定义可量化的 6 维质量评分：

| 维度 | 权重 | 评分标准 |
|------|------|----------|
| **System Prompt 深度** | 25% | 1-10：仅有角色声明(1) → 完整 4 子节结构(10) |
| **知识框架完整性** | 20% | 1-10：无框架(1) → 5+ 个带步骤的专业框架(10) |
| **场景覆盖度** | 20% | 1-10：无场景(1) → 5+ 个带输入输出的场景(10) |
| **元数据规范性** | 15% | 1-10：完全缺失(1) → 9 字段 100% 合规(10) |
| **双语质量** | 10% | 1-10：英文only(1) → 全文高质量双语(10) |
| **平台适配** | 10% | 1-10：无安装说明(1) → 7 平台均有验证步骤(10) |

**等级映射**：
- 85-100 分 → ⭐ Expert Verified
- 60-84 分 → ✅ Community Verified
- 0-59 分 → 📝 Basic

---

*本方案由 Claude (claude-sonnet-4-6) 基于代码库全面分析自动生成 | 2026-02-19*
*This plan was auto-generated by Claude based on comprehensive codebase analysis | 2026-02-19*
