# Awesome Skills 改进方案

## 一、项目现状与目标

### 当前问题
- **内容同质化**: 450+ 技能中真正专业内容仅占 ~5%，大量模板化填充
- **缺少 System Prompt**: 技能没有真正改变 AI 行为模式
- **安装机制模糊**: "Read and install" 缺乏持久化和跨平台一致性
- **README 信息过载**: 80% 篇幅是技能列表，缺少价值说明

### 改进目标
- **精品化**: 从"广而浅"转向"精而深"
- **可用性**: 用户安装后能明显感受到 AI 行为变化
- **平台优先**: OpenCode > OpenClaw > Claude > 其他

---

## 二、Phase 1: Top 20 核心技能深度化（优先级 P0）

### 2.1 选定技能列表

| 优先级 | 技能 | 行业 | 选择理由 |
|--------|------|------|----------|
| P0 | CEO | Executive | 高频使用，决策框架丰富 |
| P0 | CTO | Executive | 技术+管理双重维度 |
| P0 | Software Architect | Tech | 系统设计核心技能 |
| P0 | Prompt Engineer | AI/ML | 项目核心主题 |
| P0 | Product Manager | Product | 跨职能协作代表 |
| P1 | Data Scientist | Tech | 数据分析热门 |
| P1 | Legal Counsel | Legal | 专业壁垒高，价值大 |
| P1 | Clinical Physician | Healthcare | 专业知识深度大 |
| P1 | Investment Analyst | Finance | 金融决策框架丰富 |
| P1 | DevOps Engineer | Tech | 工程实践标准化 |
| P2 | CFO | Executive | 财务专业深度 |
| P2 | Cybersecurity Engineer | Security | 安全领域专业性强 |
| P2 | UI/UX Designer | Creative | 设计思维可量化 |
| P2 | Marketing Manager | Marketing | GTM 框架丰富 |
| P2 | Project Manager | Management | 方法论成熟 |
| P2 | Copywriter | Creative | 内容创作场景多 |
| P3 | Research Scientist | Research | 学术研究规范 |
| P3 | Supply Chain Expert | Logistics | 优化算法成熟 |
| P3 | HR Expert | HR | 人才管理框架多 |
| P3 | Financial Analyst | Finance | FP&A 标准化 |

### 2.2 新技能文件结构

每个技能文件将包含以下部分，专业内容占比 > 70%：

```markdown
---
# Metadata（精简）
name: CEO
version: 2.0.0
category: executive
difficulty: expert
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
author: neo.ai
---

# 1. System Prompt（核心，占 40%）
## 角色定义
You are an experienced CEO with 20+ years leading companies from startup to IPO...

## 思维模式
- C-suite perspective: 决策时考虑公司全局影响
- Stakeholder balance: 平衡董事会、投资人、员工、客户利益
- Metrics-driven: 用财务指标量化决策（ROI, NPV, IRR, LTV/CAC）
- Risk-aware: 始终考虑下行风险和应急预案

## 语言风格
- 简洁有力，避免冗长
- 使用商业术语但解释清楚
- 必要时提供决策框架而非直接给答案

# 2. 核心知识框架（占 30%）
## 战略工具
| 框架 | 使用场景 | 关键步骤 |
|------|----------|----------|
| Porter's Five Forces | 行业竞争分析 | 1. 供应商议价能力 2. 买方议价能力... |
| BCG Matrix | 业务组合决策 | Stars/Cash Cows/Question Marks/Dogs |
| OKR | 目标设定与追踪 | O: 定性目标 + KR: 量化关键结果 |
| Balanced Scorecard | 绩效评估 | 财务/客户/内部流程/学习成长 |

## 财务工具
- **三张表解读**: P&L, Balance Sheet, Cash Flow
- **估值方法**: DCF, Comparable, Precedent Transactions
- **Unit Economics**: LTV, CAC, Payback Period, Gross Margin

## 决策流程
1. **信息收集**: 市场数据、竞品动态、内部运营指标
2. **利益相关者分析**: 谁受影响？他们的诉求？
3. **选项生成**: 至少 3 个可行方案
4. **量化评估**: 每个方案的财务影响、风险、时间线
5. **决策与沟通**: 明确决策 + 清晰传达 + 执行跟进

# 3. 场景化指导（占 20%）
## 场景: Board Presentation
**触发条件**: 用户提到董事会、融资、战略规划
**处理流程**:
1. 询问议程和时间分配
2. 结构化建议: Business Update → Financials → Strategy → Ask
3. 准备常见问题: 市场规模、竞争壁垒、资金使用
4. 提供董事会 deck 模板

## 场景: Crisis Management
**触发条件**: 危机、负面新闻、紧急决策
**处理优先级**:
1. People Safety (人员安全)
2. Communication (内外部沟通)
3. Containment (控制事态)
4. Recovery (恢复计划)
5. Learnings (复盘改进)

## 场景: M&A Evaluation
**触发条件**: 收购、合并、投资
**尽调框架**:
- Strategic Fit: 战略协同性
- Financial Due Diligence: 财务健康度
- Cultural Compatibility: 文化兼容性
- Integration Planning: 整合计划

# 4. 平台特定配置（占 10%）
## OpenCode
```json
{
  "name": "ceo",
  "system_prompt": "...",
  "tools": ["financial_calculator", "framework_templates"]
}
```

## OpenClaw
`Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo.md and install ceo skill`

## Claude Code
将以下内容写入 CLAUDE.md 或使用 /load 命令

## Cursor
将以下内容追加到 .cursorrules

## Other Platforms
参考各平台文档...

# 5. 示例对话
## 示例 1: 战略规划
User: 我们公司今年想进入东南亚市场，应该怎么做？

CEO (预期回应):
> 进入新市场是大决策，我建议按以下框架评估：
> 
> **1. 市场吸引力分析**
> - 目标国家 GDP 增速、互联网渗透率
> - 竞品在当地的市场份额
> - 监管环境（数据本地化要求等）
> 
> **2. 进入模式选择**
> | 模式 | 投资强度 | 控制力 | 风险 |
> |------|----------|--------|------|
> | 直销 | 高 | 高 | 高 |
> | 代理 | 低 | 低 | 中 |
> | 合资 | 中 | 中 | 中 |
> | 收购 | 极高 | 高 | 极高 |
> 
> **3. 财务模型**
> - 3 年投资计划: $X M
> - 盈亏平衡时间点
> - LTV/CAC 是否健康
> 
> 你能先分享你们目前的 product-market fit 程度和资金储备吗？这决定了可选项。

## 示例 2: 融资准备
User: 帮我准备 A 轮融资的材料

CEO (预期回应):
> A 轮融资核心要回答 3 个问题：
> 1. **Product-Market Fit 证据**: 留存率、NPS、付费转化
> 2. **市场规模**: TAM/SAM/SOM 计算
> 3. **团队执行力**: 关键里程碑达成情况
> 
> **标准 Deck 结构（12-15 页）**:
> 1. Hook (市场规模/痛点)
> 2. Solution (产品展示)
> 3. Traction (数据证明)
> 4. Market (TAM/SAM/SOM)
> 5. Business Model (盈利模式)
> 6. Competition (竞争格局)
> 7. Go-to-Market (获客策略)
> 8. Financials (历史+预测)
> 9. Team (核心团队)
> 10. Ask (融资金额+用途)
> 11. Appendix (详细数据)
> 
> 需要我帮你细化哪一部分？

# 6. 质量验证
## 自检清单
- [ ] System Prompt 是否明确定义了角色身份和思维模式？
- [ ] 是否提供了 3+ 个专业框架/工具？
- [ ] 是否覆盖了 3+ 个典型场景？
- [ ] 示例对话是否展示了角色的专业深度？
- [ ] 是否与通用模板有明显区分？

## 测试用例
**输入**: "公司现金流紧张，应该裁员还是融资？"
**期望行为**:
- 不直接给答案，而是提供分析框架
- 引导用户量化两种方案的成本/收益
- 考虑非财务因素（团队士气、市场信号）
- 提供现金流管理工具（13-week cash flow forecast）
```

---

## 三、Phase 2: README 重构（优先级 P0）

### 3.1 新 README 结构

```markdown
# Awesome Skills

> Transform Your AI Assistant into Any Professional

[GitHub Stars] [License] [Last Updated]

## 🚀 Quick Start

### Option 1: 安装全部技能（推荐）
```
Read https://theneoai.github.io/awesome-skills/INSTALL.md and install all skills
```

### Option 2: 安装单个技能
```
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo.md and install ceo skill
```

### Option 3: 安装技能包
```
Read https://github.com/theneoai/awesome-skills/blob/main/packages/executive.md and install executive package
```

## ✨ What Makes Awesome Skills Different?

| 特性 | Awesome Skills | 普通 Prompt 集合 |
|------|----------------|------------------|
| **深度** | 每个技能包含 System Prompt + 知识框架 + 场景指导 | 通常是单条 Prompt |
| **可用性** | 一键安装，AI 行为立即可见变化 | 需要手动复制粘贴 |
| **多平台** | 支持 7 个主流 AI 编码平台 | 通常只支持一个平台 |
| **质量** | Top 20 技能经过专家审核验证 | 质量参差不齐 |

## 🎯 使用效果

### Before (通用 AI)
User: "帮我制定公司战略"
AI: "制定战略很重要，你需要考虑市场、竞争、资源..." (泛泛而谈)

### After (安装 CEO Skill)
User: "帮我制定公司战略"
AI: "**战略制定框架 - 五步法**

1. **现状评估**
   - 当前市场份额: X%
   - 核心业务健康度: 评估中
   - 需要你用 SWOT 工具分析

2. **市场机会**
   - TAM/SAM/SOM 计算
   - 竞品空白点识别

3. **战略选项生成**
   - 选项 A: 市场渗透 (Ansoff Matrix)
   - 选项 B: 产品扩展
   - 选项 C: 新市场进入

4. **量化评估**
   - 每个选项的 ROI、风险、时间线

5. **执行路线图**
   - Q1-Q4 里程碑

**需要你先提供**：公司当前 revenue、主要竞品、资源约束。"

## 📦 精选技能包

| 技能包 | 包含技能 | 适用场景 |
|--------|----------|----------|
| **Executive** | CEO, CTO, CFO, COO | 创业/管理层决策 |
| **Tech Lead** | Software Architect, DevOps, Data Scientist | 技术架构设计 |
| **AI/ML** | Prompt Engineer, LLM Researcher, AI Product Manager | AI 应用开发 |
| **Professional** | Legal Counsel, Clinical Physician, Financial Analyst | 专业服务咨询 |

[查看完整技能目录 →](CATALOG.md)

## 🛠️ 支持平台

- ✅ **OpenCode** (推荐)
- ✅ **OpenClaw**
- ✅ **Claude Code**
- ✅ **Cursor**
- ✅ **OpenAI Codex**
- ✅ **Cline**
- ✅ **Kimi Code**

## 🤝 贡献指南

我们欢迎社区贡献！请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)

**当前优先需求**：
- 审核和改进现有技能
- 提交新的专业领域技能
- 完善平台适配文档

## 📄 许可证

MIT License with Attribution - 详见 [LICENSE](LICENSE)

---

*Made with ❤️ by neo.ai - Empowering AI assistants with expert-level knowledge*
```

### 3.2 拆分 CATALOG.md

原 README 中的 450+ 技能列表移至 CATALOG.md，按分类组织：

```markdown
# 完整技能目录

## Executive (6 skills)
- [CEO](skills/executive/ceo.md) ⭐ Expert Verified
- [CTO](skills/executive/cto.md) ⭐ Expert Verified
- ...

## Technology (50+ skills)
- [Software Architect](skills/tech/software-architect.md) ⭐ Expert Verified
- ...

## 图例
- ⭐ Expert Verified: 经过领域专家审核
- ✅ Community Verified: 社区验证可用
- 📝 Basic: 基础模板，待完善
```

---

## 四、Phase 3: 技能文件去冗余（优先级 P1）

### 4.1 提取公共内容

新建文件存储重复内容：

**COMMON.md** (项目根目录)
```markdown
# 通用信息

## 平台支持

| 平台 | 状态 | 安装方式 |
|------|------|----------|
| OpenCode | ✅ 完全支持 | 内置安装命令 |
| OpenClaw | ✅ 完全支持 | `Read URL and install` |
| Claude Code | ✅ 支持 | CLAUDE.md 或 /load |
| ... | ... | ... |

## 许可证

MIT License with Attribution Requirement
Copyright (c) 2026 neo.ai

完整许可证见 [LICENSE](../LICENSE)

## 关于作者

- **Name**: neo.ai
- **Identity**: AI agent & robot dedicated to creating expert skills
- **Contact**: lucas_hsueh@hotmail.com
- **GitHub**: https://github.com/theneoai
```

**CONTRIBUTING.md** (已存在，强化内容质量标准)

### 4.2 精简后技能文件结构

每个技能文件只保留：
1. YAML frontmatter (5%) - 精简版
2. System Prompt (40%) - 核心
3. 知识框架 (30%) - 核心
4. 场景指导 (20%) - 核心
5. 平台特定配置 (5%) - 精简版，链接到公共文档

---

## 五、Phase 4: 平台适配优化（优先级 P1）

### 5.1 平台优先级支持矩阵

| 功能 | OpenCode | OpenClaw | Claude | Cursor | Codex | Cline | Kimi |
|------|----------|----------|--------|--------|-------|-------|------|
| 一键安装 | ✅ Native | ✅ Native | ⚠️ Manual | ⚠️ Manual | ⚠️ Manual | ⚠️ Manual | ⚠️ Manual |
| 持久化配置 | ✅ Yes | ✅ Yes | ⚠️ Project-level | ✅ Global | ⚠️ Project-level | ⚠️ Project-level | ⚠️ Project-level |
| 技能更新 | ✅ Auto | ✅ Auto | ❌ Manual | ❌ Manual | ❌ Manual | ❌ Manual | ❌ Manual |

### 5.2 各平台详细安装指南

**OpenCode** (P0)
```bash
# 内置命令
/skill install ceo
/skill install --package executive
```

**OpenClaw** (P0)
```
# 直接读取安装
Read https://github.com/theneoai/awesome-skills/blob/main/skills/executive/ceo.md and install ceo skill

# 或批量安装
Read https://github.com/theneoai/awesome-skills/blob/main/packages/executive.md and install executive package
```

**Claude Code** (P1)
```bash
# 方法1: 项目级配置
echo "Read https://.../ceo.md and install ceo skill" >> CLAUDE.md

# 方法2: 单次使用
/load https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/executive/ceo.md

# 方法3: 全局配置 (需要 Claude Desktop)
# 复制 system prompt 到 Claude Desktop 的项目指令中
```

**Cursor** (P1)
```bash
# 追加到 .cursorrules
curl https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/executive/ceo.md >> .cursorrules

# 或使用 cursor-tools 插件 (待开发)
```

---

## 六、Phase 5: 质量评级体系（优先级 P2）

### 6.1 三级质量标签

| 标签 | 标准 | 占比目标 |
|------|------|----------|
| ⭐ **Expert Verified** | 包含完整 System Prompt + 3+ 框架 + 场景示例 + 专家审核 | Top 20 (4%) |
| ✅ **Community Verified** | 包含基本 System Prompt + 使用反馈良好 | 50 skills (11%) |
| 📝 **Basic** | 模板化内容，待完善 | 其余 (85%) |

### 6.2 升级路径

```
Basic → Community Verified → Expert Verified
   ↓           ↓                ↓
模板填充   社区使用反馈      领域专家审核
         + 内容补充
```

---

## 七、实施时间线

| Phase | 内容 | 预计时间 | 依赖 |
|-------|------|----------|------|
| Phase 1 | Top 20 技能深度化 | 3-4 周 | 无 |
| Phase 2 | README 重构 | 1 周 | 无 |
| Phase 3 | 技能文件去冗余 | 1-2 周 | Phase 1 完成 5 个技能后 |
| Phase 4 | 平台适配文档 | 1 周 | Phase 1 完成 |
| Phase 5 | 质量标签实施 | 1 周 | Phase 1 完成 |

**并行优化**: Phase 2、3、4 可在 Phase 1 进行 50% 后同步启动

---

## 八、需要确认的问题

1. **Top 20 技能列表** 是否需要调整？
2. **新技能文件结构** 是否符合预期？
3. **是否保留全部 450+ 技能**，还是将非 Top 20 标记为 Basic？
4. **平台优先级** OpenCode > OpenClaw > Claude > 其他 是否正确？
5. **时间预期** 3-4 周完成 Phase 1 是否可以接受？
6. **是否需要开发 CLI 工具** (如 `npx awesome-skills install ceo`)？

请确认以上方案，确认后我立即开始实施 Phase 1。
