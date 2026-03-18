# Skill 共享平台设计：优先级排序 & 认证鉴权安全方案

> 结合 AI 对软件行业的冲击，系统规划哪些 Skill 最值得优先共享，以及如何安全管理 Skill 运行所需的凭证。

---

## 一、AI 发展趋势对软件行业的影响框架

在排优先级前，先明确三个维度的判断依据：

| 维度 | 说明 |
|------|------|
| **岗位冲击烈度** | AI 在多大程度上正在替代/重塑这个角色的核心工作 |
| **杠杆倍率** | 用 Skill 增强后，单人产出提升倍数 |
| **技能稀缺性** | 原始培养周期长、人才缺口大的领域，Skill 的补位价值越高 |

核心趋势判断（2024-2026）：
- **AI 编码助手**正在让初级开发者产能×3-5，但架构判断力仍是瓶颈
- **Vibe Coding** 兴起，非专业人员也在写软件，需要专业 Skill 兜底质量
- **AI Agent/工作流**爆发，Prompt/Agent 工程师成稀缺岗位
- **AI 安全**成监管重点，需求急速上升但人才极少
- **数据工程/MLOps**成 AI 落地的最大卡点

---

## 二、可共享 Skill 全景 & 优先级排序

### Tier 1：战略必做（AI 冲击最直接，缺口最大）

这些领域 AI 正在根本性重塑工作方式，Skill 价值最高。

| 优先级 | Skill | 核心理由 |
|--------|-------|---------|
| P0-1 | **AI Application Engineer** | 每家公司都在做 AI 应用，但懂工程化落地的人极少 |
| P0-2 | **Prompt Engineer** | Vibe Coding 时代，Prompt 质量决定 AI 产出上限 |
| P0-3 | **LLM Integration Specialist** | 连接 LLM 与现有系统，是 AI 落地最高频动作 |
| P0-4 | **AI Product Manager** | 需要同时懂 AI 能力边界 + 产品思维，复合稀缺 |
| P0-5 | **MLOps / AI Platform Engineer** | AI 模型上线最大卡点，DevOps ≠ MLOps |
| P0-6 | **AI Safety & Red Teaming** | 监管压力（EU AI Act 等）使需求爆发，供给接近零 |

### Tier 2：高价值（AI 大幅增强，但角色不会消失）

| 优先级 | Skill | 核心理由 |
|--------|-------|---------|
| P1-1 | **Software Architect** | AI 生成大量代码，但整体架构判断仍靠人；Skill 帮助架构审查 |
| P1-2 | **Security Engineer** | AI 加速漏洞发现 + 攻击工具化，防御侧需求成倍增长 |
| P1-3 | **Data Engineer** | 所有 AI 项目都需要数据管道，数据工程是 AI 落地卡点 |
| P1-4 | **DevOps / Platform Engineer** | AI 推动频繁部署，DevOps 自动化需求更强 |
| P1-5 | **Code Reviewer / Tech Lead** | AI 写代码量激增，代码评审成新瓶颈 |
| P1-6 | **API Designer** | AI agent 互联互通依赖标准 API，设计能力稀缺 |
| P1-7 | **Backend Developer（高阶）** | 初级被 AI 替代，高阶系统设计需求上升 |

### Tier 3：重要补充（AI 改变工作方式，效率倍增）

| 优先级 | Skill | 核心理由 |
|--------|-------|---------|
| P2-1 | **QA / Test Engineer（AI-native）** | AI 生成代码缺陷率高，测试工程更关键 |
| P2-2 | **Database Administrator** | AI 应用数据密集，DB 优化需求长期存在 |
| P2-3 | **Cloud Infrastructure Engineer** | AI 推理成本高，云架构优化成核心竞争力 |
| P2-4 | **Technical Writer（AI-assisted）** | AI 生成文档质量参差，专业校核仍需人工 |
| P2-5 | **Performance Engineer** | AI 推理延迟优化是新需求 |
| P2-6 | **Frontend Developer（AI-native）** | Cursor/v0 等 AI 工具让前端开发被大量非专业人员涉及 |

### Tier 4：跨域高价值（非纯软件，但 AI 影响深远）

| 优先级 | Skill | 核心理由 |
|--------|-------|---------|
| P3-1 | **Algorithm Engineer（LLM-specific）** | 推理优化、量化、蒸馏等新赛道 |
| P3-2 | **LLM Research Scientist** | 推动技术前沿，学术/工业均需求 |
| P3-3 | **AI Chip Architect** | 算力争夺成国家战略，供需极度紧张 |
| P3-4 | **Strategy Consultant（AI-era）** | 企业 AI 转型咨询爆发 |
| P3-5 | **CTO（AI-native）** | 技术决策者需要 AI 战略判断力 |

### 总优先级矩阵

```
              高稀缺性
                 ↑
  AI Safety    AI App Eng    Prompt Eng
  MLOps        LLM Integ.    AI PM
      ←─────────────────────────→
  低冲击烈度              高冲击烈度
      ─────────────────────────→
  DB Admin     QA Engineer   Code Review
  Tech Writer  DevOps        Security Eng
                 ↓
              低稀缺性
```

---

## 三、Skill 中认证鉴权信息安全方案

### 3.1 核心安全原则

```
黄金法则：
  Skill 文件 = 逻辑（公开可分发）
  凭证信息   = 数据（永不进入 Skill 文件）
```

凭证与 Skill 解耦，通过**引用名**绑定，而非直接嵌入值。

---

### 3.2 凭证分类

| 类型 | 示例 | 敏感级别 |
|------|------|---------|
| API Key | `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` | 🔴 高 |
| OAuth Token | `GITHUB_TOKEN`, `GOOGLE_ACCESS_TOKEN` | 🔴 高 |
| 数据库连接串 | `DATABASE_URL`, `REDIS_URL` | 🔴 高 |
| 服务账号 | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | 🔴 高 |
| Webhook Secret | `SLACK_WEBHOOK_URL` | 🟡 中 |
| 非敏感配置 | `API_BASE_URL`, `MODEL_NAME` | 🟢 低 |

---

### 3.3 凭证引用语法规范

在 Skill 文件的 `credentials` frontmatter 中声明所需凭证，使用占位符引用：

```yaml
# skill frontmatter 示例
name: ai-application-engineer
credentials:
  required:
    - name: ANTHROPIC_API_KEY
      description: "Anthropic Claude API 密钥"
      source: env          # 从环境变量读取
      sensitive: true
    - name: GITHUB_TOKEN
      description: "GitHub Personal Access Token（需 repo 权限）"
      source: env
      sensitive: true
  optional:
    - name: OPENAI_API_KEY
      description: "OpenAI API 密钥（可选，用于多模型对比）"
      source: env
      sensitive: true
    - name: API_BASE_URL
      description: "自定义 API 网关地址"
      source: env
      sensitive: false
      default: "https://api.anthropic.com"
```

在 Skill 系统提示中引用方式：

```markdown
## Tool Access
You have access to the following tools via credentials:
- GitHub API: use token from `${GITHUB_TOKEN}`
- Claude API: use key from `${ANTHROPIC_API_KEY}`

Never output credential values. Always reference by variable name.
```

---

### 3.4 分层存储架构

```
┌─────────────────────────────────────────────────────┐
│                   Skill 分发层                        │
│   skill.md（仅含引用名，无实际凭证值）                  │
│   credentials: [ANTHROPIC_API_KEY, GITHUB_TOKEN]     │
└─────────────────┬───────────────────────────────────┘
                  │ 凭证名 → 凭证值 在运行时绑定
┌─────────────────▼───────────────────────────────────┐
│                   平台凭证层                           │
│                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐  │
│  │ 用户本地环境  │  │  平台密钥库   │  │ 团队密钥库 │  │
│  │  ~/.env      │  │ Claude Code  │  │  Vault    │  │
│  │  .env.local  │  │ Settings     │  │  1Password│  │
│  └──────────────┘  └──────────────┘  └───────────┘  │
└─────────────────────────────────────────────────────┘
```

**三种存储方式适用场景：**

| 存储方式 | 适用场景 | 安全级别 |
|---------|---------|---------|
| 本地 `.env` 文件 | 个人开发，单机使用 | 🟡 中（需加入 .gitignore）|
| 平台原生密钥库 | 单平台工作流（如 Claude Code settings）| 🟢 高 |
| 企业级密钥管理 | 团队共享、生产环境（Vault/1Password/AWS Secrets Manager）| 🟢 高 |

---

### 3.5 各平台凭证注入方案

#### Claude Code

```bash
# 方式 1：项目级 .env（已在 .gitignore 中）
echo "ANTHROPIC_API_KEY=sk-ant-xxx" >> .env

# 方式 2：CLAUDE.md 中声明所需凭证（仅名称，不含值）
# CLAUDE.md:
# ## Required Credentials
# - ANTHROPIC_API_KEY: Set via environment or .env
# - GITHUB_TOKEN: Set via `gh auth login` then export
```

#### OpenCode / OpenClaw

```bash
# OpenCode 原生支持 secret 管理
/secret set ANTHROPIC_API_KEY sk-ant-xxx
/secret set GITHUB_TOKEN ghp_xxx

# Skill 安装时自动检查所需凭证，缺失时提示用户
```

#### Cursor / 通用平台

```bash
# 通过系统环境变量注入（在 shell 配置文件中）
# ~/.zshrc 或 ~/.bashrc
export ANTHROPIC_API_KEY="$(security find-generic-password -a anthropic -w)"
# macOS Keychain 集成，避免明文存储
```

---

### 3.6 凭证生命周期管理

```
创建  →  存储  →  分发  →  使用  →  轮换  →  吊销
  ↓        ↓        ↓        ↓        ↓        ↓
最小       加密     零明文   审计     定期     立即
权限       存储     传输     日志     更新     生效
```

**关键安全控制：**

1. **最小权限原则**
   ```yaml
   # Skill 凭证应声明最小所需权限范围
   credentials:
     - name: GITHUB_TOKEN
       required_scopes: ["repo:read", "issues:write"]  # 不要 repo:admin
   ```

2. **凭证有效期控制**
   ```yaml
   credentials:
     - name: OPENAI_API_KEY
       rotation_reminder: "90d"   # 90 天提示轮换
       expiry_check: true         # 运行时检查是否过期
   ```

3. **审计日志**
   - 记录哪个 Skill 在什么时间访问了哪个凭证
   - 不记录凭证值，只记录凭证名 + 访问元信息

4. **凭证泄露检测**
   - pre-commit hook 扫描 Skill 文件，阻止任何形如 `sk-`, `ghp_`, `eyJ` 的字符串提交
   - CI 中集成 `truffleHog` 或 `gitleaks` 扫描

---

### 3.7 团队共享 Skill 的凭证分发方案

当团队共享同一套 Skill 时，凭证分发挑战最大。推荐分级方案：

```
┌─────────────────────────────────────────────────────┐
│                 团队 Skill 共享模型                    │
├─────────────────────────────────────────────────────┤
│  Skill Registry（公开）                               │
│    └── skill.md（无凭证）+ credentials.schema.yaml   │
│                                                      │
│  Team Vault（私有，加密）                             │
│    └── 团队共享凭证（如内部服务账号）                   │
│    └── 访问控制：RBAC，最小权限                        │
│                                                      │
│  个人凭证（用户自管）                                  │
│    └── 个人 API Key（如 OpenAI 个人账号）              │
│    └── 平台不代管，用户自行注入                        │
└─────────────────────────────────────────────────────┘
```

**推荐工具链：**

| 场景 | 工具 | 说明 |
|------|------|------|
| 个人开发 | `direnv` + `.env` | 目录级自动加载，不污染全局环境 |
| 小团队 | `1Password Secrets Automation` | CLI 集成，团队共享 vault |
| 企业 | `HashiCorp Vault` | 动态凭证、细粒度 RBAC、完整审计 |
| CI/CD | GitHub Secrets / GitLab Variables | 流水线中安全注入 |
| macOS | Keychain + `security` CLI | 系统级加密存储 |

---

### 3.8 Skill 文件安全校验 Checklist

在 Skill 文件提交前，需通过以下校验：

```python
# .github/scripts/validate_credentials.py （伪代码示意）

FORBIDDEN_PATTERNS = [
    r"sk-[a-zA-Z0-9]{48}",           # OpenAI API Key
    r"sk-ant-[a-zA-Z0-9\-]{95}",     # Anthropic API Key
    r"ghp_[a-zA-Z0-9]{36}",          # GitHub Personal Access Token
    r"gho_[a-zA-Z0-9]{36}",          # GitHub OAuth Token
    r"AKIA[0-9A-Z]{16}",             # AWS Access Key
    r"eyJ[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+",  # JWT Token
    r"postgres://.*:.*@",             # DB connection with credentials
]

def validate_skill_file(path):
    content = open(path).read()
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, content):
            raise SecurityError(f"凭证泄露风险: {path}")

    # 检查 credentials 字段是否符合规范
    frontmatter = extract_frontmatter(content)
    if "credentials" in frontmatter:
        validate_credentials_schema(frontmatter["credentials"])
```

---

## 四、总结：执行路线图

### 第一阶段（0-3个月）：核心 AI 技能 Skill 上线

**目标：** 上线 Tier 1 全部 6 个 Skill，确保质量达到 9.5/10

```
Week 1-2: AI Application Engineer + Prompt Engineer（已有基础，升级完善）
Week 3-4: LLM Integration Specialist（新建）
Week 5-6: AI Product Manager + MLOps Engineer（已有基础，升级）
Week 7-8: AI Safety & Red Teaming（新建，填补市场空白）
```

### 第二阶段（3-6个月）：基础设施 + 凭证管理

**目标：** 建立凭证安全框架，上线 Tier 2 Skill

```
Month 4: 在所有新 Skill 中实施 credentials frontmatter 规范
Month 5: 集成 pre-commit 凭证泄露检测
Month 6: 发布团队凭证管理最佳实践文档
```

### 第三阶段（6-12个月）：平台化 + 生态建设

**目标：** 构建 Skill 市场，支持团队级共享

```
Q3: Skill Registry API（按名查询、版本管理）
Q4: 凭证模板市场（标准化凭证 schema）
Q4: 团队 Vault 集成（1Password / Vault 官方集成）
```

---

*文档版本: v2.0 | 作者: neo.ai | 日期: 2026-03-18 | 状态: 已完成核心功能设计*
