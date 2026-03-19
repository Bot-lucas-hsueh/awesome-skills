# 软件工程职业路径 Software Engineering Roadmap

> 覆盖方向：后端 · 前端 · 全栈 · 架构师 · DevOps · QA · 安全工程师

---

## 职业全景

```
软件工程
├── 后端工程师 → 高级后端 → 技术负责人 → 架构师 → 首席架构师
├── 前端工程师 → 高级前端 → 前端架构师 → 全栈架构师
├── 全栈工程师 → 独立开发者 / 技术创始人
├── DevOps工程师 → SRE → 平台工程师 → 基础设施架构师
├── QA工程师 → 测试架构师 → 质量总监
└── 安全工程师 → 安全架构师 → CISO
```

---

## 通用基础（所有方向必备）

在进入具体方向前，所有软件工程师需要掌握：

- **编程基础**: 至少一门主流语言（Python/Java/Go/TypeScript）
- **数据结构与算法**: 数组、链表、树、图、排序、搜索
- **计算机网络**: HTTP/HTTPS、TCP/IP、DNS、REST API
- **操作系统**: 进程/线程、内存管理、文件系统
- **数据库**: SQL基础、事务、索引
- **Git版本控制**: 分支管理、代码审查流程
- **命令行**: Linux基础操作

---

## 🌱 第1级 · 入门 (0-12个月)

### 目标
完成第一个能实际运行的项目，理解软件开发基本流程。

### 必备技能

**后端方向**
- [ ] 掌握一门后端语言（推荐Python/Go/Java）
- [ ] 能写简单的REST API（CRUD操作）
- [ ] 理解HTTP状态码和请求方法
- [ ] 会用MySQL/PostgreSQL做基础增删改查
- [ ] 能用Docker运行本地开发环境

**前端方向**
- [ ] HTML/CSS布局（Flexbox、Grid）
- [ ] JavaScript基础（ES6+、DOM操作、事件）
- [ ] React或Vue基础组件开发
- [ ] 会用浏览器DevTools调试
- [ ] 响应式设计基础

**DevOps方向**
- [ ] Linux命令行熟练操作
- [ ] Git工作流（分支、合并、冲突解决）
- [ ] Docker容器基础概念和使用
- [ ] 一个CI工具（GitHub Actions / Jenkins）
- [ ] 基础Shell脚本

### 关键里程碑
- ✅ 独立完成并部署一个Web应用（哪怕功能简单）
- ✅ 第一次参与开源项目（提PR被合并）
- ✅ 通过代码审查并根据反馈修改代码

### 学习资源
- freeCodeCamp / The Odin Project（前端）
- CS50（编程基础）
- LeetCode 简单题 × 50道
- 官方文档：React/Django/Spring Boot

### 常见陷阱 ⚠️
- 教程地狱：只看不做，必须动手写代码
- 跳跃过快：基础不牢就学框架，后期会还债
- 孤立学习：多加技术社群，多问问题

---

## 🌿 第2级 · 初级工程师 (1-3年)

### 目标
能够独立完成分配的任务，代码质量达到团队标准，开始理解系统设计。

### 必备技能

**后端**
- [ ] 熟悉主流框架（Spring Boot / FastAPI / Express / Gin）
- [ ] 数据库优化：索引设计、查询优化、连接池
- [ ] Redis缓存基础应用
- [ ] 单元测试 + 集成测试编写
- [ ] API设计规范（RESTful最佳实践）
- [ ] 消息队列基础（RabbitMQ / Kafka入门）

**前端**
- [ ] React高级用法（Hooks、Context、自定义Hook）
- [ ] 状态管理（Redux / Zustand / Pinia）
- [ ] 前端工程化（Webpack/Vite配置）
- [ ] TypeScript基础到进阶
- [ ] 性能优化基础（懒加载、代码分割）
- [ ] 前端测试（Jest + Testing Library）

**DevOps**
- [ ] Kubernetes基础（Pod、Service、Deployment）
- [ ] Terraform入门（基础设施即代码）
- [ ] 监控告警（Prometheus + Grafana）
- [ ] 日志管理（ELK Stack）

### 关键里程碑
- ✅ 独立负责一个模块从设计到上线
- ✅ Code Review时提出有价值的意见
- ✅ 发现并修复一个生产Bug
- ✅ 参与一次系统设计讨论

### 薪资参考（中国市场）
- 一线城市：15K-25K/月
- 二线城市：10K-18K/月

---

## 🌳 第3级 · 中级工程师 (3-6年)

### 目标
主导功能模块开发，具备初步的系统设计能力，能指导初级工程师。

### 必备技能

**系统设计**
- [ ] 熟悉常见设计模式（工厂、策略、观察者、装饰器等）
- [ ] 分布式系统基础（CAP理论、一致性模型）
- [ ] 微服务架构设计与权衡
- [ ] 高可用设计（负载均衡、故障转移、熔断器）
- [ ] 数据库分库分表基础

**后端深度**
- [ ] 深入理解JVM/Python GIL/Go runtime
- [ ] 高并发处理（限流、降级、熔断）
- [ ] 分布式事务（Saga、2PC）
- [ ] API安全（OAuth2、JWT、RBAC）
- [ ] 性能调优方法论（Profiling、火焰图）

**前端深度**
- [ ] 性能优化进阶（Web Vitals、LCP/FID/CLS）
- [ ] 微前端架构
- [ ] 前端监控（错误追踪、性能监控）
- [ ] SSR/SSG（Next.js / Nuxt.js）
- [ ] 低代码/可视化平台开发

**软技能**
- [ ] 技术方案文档写作（RFC/ADR格式）
- [ ] 需求拆解与估时
- [ ] 跨团队沟通协调

### 关键里程碑
- ✅ 主导完成一个复杂系统设计
- ✅ 面试并辅导初级工程师
- ✅ 发现并推动一个技术债务改造项目
- ✅ 在团队内做技术分享

### 薪资参考（中国市场）
- 一线城市：25K-45K/月
- 大厂P6/P7级别

---

## 🦅 第4级 · 高级工程师 / Tech Lead (6-10年)

### 目标
技术决策能力，跨团队影响力，定义团队技术标准和最佳实践。

### 必备技能

**技术领导力**
- [ ] 技术路线规划（季度/年度）
- [ ] 建立团队编码规范与CI/CD标准
- [ ] 技术风险评估与应对
- [ ] 主导架构评审（Architecture Review Board）
- [ ] 研究新技术并评估引入价值

**系统设计专家**
- [ ] 百万级/千万级用户系统设计
- [ ] 多数据中心/多活架构
- [ ] 复杂数据模型设计
- [ ] 平台化、中台化架构

**团队建设**
- [ ] 构建技术面试体系
- [ ] 技术培训计划制定
- [ ] 工程师职业发展辅导
- [ ] OKR制定与拆解

**跨职能合作**
- [ ] 与产品/设计深度协作
- [ ] 向管理层做技术汇报
- [ ] 技术选型影响商业决策

### 关键里程碑
- ✅ 负责一个核心系统的完整生命周期
- ✅ 带领团队（3-8人）完成关键项目
- ✅ 在公司内推行一项技术标准
- ✅ 培养出至少1名晋升到中级的工程师

### 薪资参考（中国市场）
- 一线城市：45K-80K/月
- 大厂P8级别或以上

---

## 👑 第5级 · 精英 / 首席架构师 (10年+)

### 特征
- 在技术社区有广泛影响力（技术博客/开源/演讲）
- 能从零设计整个技术体系
- 参与公司技术战略和产品战略
- 培养出多名高级工程师

### 核心能力

**战略级技术能力**
- 预判技术趋势（3-5年视野）
- 设计公司级技术平台和中台
- 平衡技术理想与商业现实
- 跨行业技术借鉴与创新

**组织影响力**
- 建立技术文化和工程师文化
- 招募和保留顶尖人才
- 对外技术品牌建设
- 开源项目或行业标准制定参与

### 精英标志
- 🏆 主导过百万DAU以上系统的设计与稳定运营
- 🏆 在顶级技术会议（QCon/ArchSummit）发表演讲
- 🏆 开源项目获得1000+ Star
- 🏆 培养出多名技术负责人

---

## 各方向专项路径

### 🔒 安全工程师路径
```
入门 → OWASP Top10基础 → CTF竞赛 →
初级 → 渗透测试（Burp Suite/Metasploit）→ CEH认证 →
中级 → 安全开发(DevSecOps) + 代码审计 →
高级 → 安全架构设计 + 红队演练 + CISSP认证 →
精英 → CISO / 安全顾问
```

### 🚀 DevOps / SRE路径
```
入门 → Linux+Git+Docker →
初级 → Kubernetes + CI/CD (GitHub Actions) →
中级 → Terraform + 监控告警 + SLO制定 →
高级 → 平台工程 + FinOps + 多云架构 →
精英 → 平台工程VP / 基础设施架构师
```

### 🧪 QA工程师路径
```
入门 → 手工测试 + Bug报告 →
初级 → 自动化测试(Selenium/Playwright) + API测试 →
中级 → 测试框架设计 + 性能测试 + 质量度量 →
高级 → 质量体系建设 + 测试策略制定 →
精英 → 质量总监 / 测试架构师
```

---

## 认证路线图

| 级别 | 推荐认证 |
|------|---------|
| 初级 | AWS Cloud Practitioner / Google Associate |
| 中级 | AWS Solutions Architect Associate / CKA(Kubernetes) |
| 高级 | AWS Solutions Architect Professional / CISSP(安全) |
| 精英 | Google Fellow / Distinguished Engineer |

---

## 🤖 AI时代的软件工程师规划

### AI对软件工程的冲击与机会

```
当前趋势（2025-2030）：
  - GitHub Copilot / Cursor 等AI编码工具覆盖率达70%+
  - AI可自动完成约40-60%的常规编码任务（CRUD/测试/文档）
  - 初级重复性编码岗位需求收缩，高阶设计岗位需求激增
  - AI原生应用架构（LLM集成、Agent系统）成为新标准
```

### 各阶段AI融合建议

**初级工程师 — AI是加速器**
- 用 Cursor / GitHub Copilot 提升编码效率（目标：3x速度）
- 学会用 AI 审查代码：让 Claude 解释每行你不理解的代码
- 用 AI 生成测试用例：理解测试意图，不要盲目复制
- ⚠️ 警惕：不能依赖AI写代码但不理解原理，AI会产生微妙Bug

**中级工程师 — AI是协作者**
- 掌握 AI 辅助系统设计：让 AI 生成方案草图，你来评估和决策
- 学习 RAG / LLM集成：几乎所有产品都需要 AI 功能
- 研究 AI Agent 架构：Tool Use、Memory、多Agent协作
- 建立 AI 评估能力：判断什么场景适合用AI、什么场景不适合

**高级工程师/架构师 — AI是放大器**
- 设计 AI 原生架构：将 LLM 作为一等公民纳入系统设计
- 制定团队 AI 工具规范：AI编码的代码审查标准、测试覆盖要求
- 评估 AI 成本：Token费用、延迟、可靠性的权衡
- 探索 Vibe Coding 范式：用自然语言驱动复杂系统构建

### 必须掌握的 AI 技术栈（2026）

```
LLM集成: OpenAI API · Anthropic Claude API · 本地模型(Ollama)
AI应用框架: LangChain · LlamaIndex · Vercel AI SDK
向量数据库: Pgvector · Pinecone · Weaviate
AI编码工具: Cursor · GitHub Copilot · Windsurf
AI测试: 基于LLM的测试生成 · 模糊测试
AI运维: LLM Observability（LangSmith/Langfuse）
```

### 不会被AI取代的核心竞争力

| 能力 | 原因 |
|------|------|
| 系统设计与架构决策 | 需要业务理解 + 工程判断 + 权衡取舍 |
| 复杂Bug的根因分析 | 需要系统全局视角，AI难以定位 |
| 技术方向判断 | 判断新技术何时成熟，是否值得引入 |
| 跨团队技术协调 | 人际关系与组织政治是AI的盲区 |
| AI系统的设计与评估 | 评估AI系统的人，本身不会被AI替代 |

### 行动建议：未来3年重点投资方向

1. **立即**: 把 Cursor 或 Copilot 集成进日常工作流，每天使用
2. **3个月内**: 完成一个使用 Claude/GPT API 的端到端项目
3. **6个月内**: 学会构建 RAG 应用或 AI Agent
4. **1年内**: 主导团队的 AI 工具选型和使用规范制定

---

## 关联技能文件

- [`skills/software/backend-developer/`](../skills/software/backend-developer/) — 后端开发完整技能体系
- [`skills/software/frontend-developer/`](../skills/software/frontend-developer/) — 前端开发完整技能体系
- [`skills/software/software-architect/`](../skills/software/software-architect/) — 软件架构师
- [`skills/software/devops-engineer/`](../skills/software/devops-engineer/) — DevOps工程师
- [`skills/software/qa-engineer/`](../skills/software/qa-engineer/) — QA工程师
- [`skills/cybersecurity/security-engineer/`](../skills/cybersecurity/security-engineer/) — 安全工程师
- [`skills/software/system-architect/`](../skills/software/system-architect/) — 系统架构师
