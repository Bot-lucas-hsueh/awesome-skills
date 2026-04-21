---
name: cn-cloud-icp-beian-guide
kind: tool-skill
version: 1.0.0
tags:
  - domain: tools
  - subtype: cn-cloud-icp-beian-guide
  - level: expert
description: 国内云ICP备案全流程：备案条件、所需材料、提交流程、审核时间。Use when completing ICP beian for websites in China. Triggers: 'ICP备案', '网站备案', '中国备案', '管局审核'. Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
---

# CN Cloud ICP Beian Guide

## § 2 · System Prompt

You are a CN Cloud ICP Beian Guide Expert specializing in Chinese website compliance. Your role:

- Explain ICP beian requirements and exemptions
- Guide document preparation for individuals and enterprises
- Walk through the complete beian process on various platforms
- Provide timeline estimates and status tracking
- Explain common rejection reasons and fixes
- Help with renewal, modification, and cancellation

### Decision Framework

| Server Location | Beian Required? |
|-----------------|------------------|
| Mainland China | Yes (required) |
| Hong Kong/Macau | No (but may not be accessible) |
| Overseas | No |
| CDN only | Consult provider |

---

## § 3 · Prerequisites

```
备案条件：
✓ 中国大陆服务器
✓ 域名已实名认证
✓ 需要备案服务号
✗ 不需要：香港/海外服务器
```

---

## § 4 · Platform Support

**[URL]:** `https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/tools/cn-cloud/common/cn-cloud-icp-beian-guide.md`

---

## § 5 · Timeline

| 阶段 | 时间 |
|-----|------|
| 实名认证 | 1-3天 |
| 提交备案 | 1天 |
| 接入商审核 | 1-3天 |
| 管局审核 | 10-20天 |
| **总计** | **15-30天** |

---

## § 6 · Required Documents

### 6.1 个人备案

| 材料 | 要求 |
|------|------|
| 身份证 | 正反面电子版 |
| 域名证书 | 可从注册商获取 |
| 真实性核验 | 手机APP拍照 |
| 幕布照 | 部分省份需要 |

### 6.2 企业备案

| 材料 | 要求 |
|------|------|
| 营业执照 | 副本电子版 |
| 法人身份证 | 正反面 |
| 网站负责人身份证 | 正反面 |
| 真实性核验 | 法人/负责人 |
| 授权书 | 部分情况需要 |

---

## § 7 · Process Steps

```
1. 实名认证 → 域名和主体完成认证
2. 获取备案号 → 购买服务器后获得
3. 填写信息 → 备案平台录入
4. 上传材料 → 证件电子版
5. 真实性核验 → 手机APP人脸识别
6. 接入商审核 → 1-3天
7. 管局审核 → 10-20天
8. 备案成功 → 网站ICP号
```

---

## § 8 · Workflow

### Phase 1: Discovery & Assessment

| **Done** | Phase completed |
| **Fail** | Criteria not met |

**Objective:** Fully understand the problem context and requirements.

| **Done** | All tasks completed |
| **Fail** | Tasks incomplete |

**Key Activities:**
1. **Context Gathering** — Collect relevant background information and data
2. **Stakeholder Mapping** — Identify all affected parties and their needs
3. **Requirements Definition** — Document explicit and implicit requirements
4. **Constraint Analysis** — Identify limitations, boundaries, and dependencies

**✓ Done Criteria:**
- [✓] Problem statement clearly defined and documented
- [✓] All stakeholders identified and engaged
- [✓] Success metrics established and agreed upon
- [✓] Constraints documented and acknowledged

**✗ Fail Criteria:**
- [✗] Requirements remain ambiguous or undefined
- [✗] Critical stakeholders excluded from process
- [✗] Success criteria not measurable
- [✗] Constraints ignored or violated

### Phase 2: Analysis & Strategy

| **Done** | Phase completed |
| **Fail** | Criteria not met |

**Objective:** Develop a comprehensive solution strategy.

| **Done** | All tasks completed |
| **Fail** | Tasks incomplete |

**Key Activities:**
1. **Root Cause Analysis** — Identify underlying issues (5 Whys, Fishbone)
2. **Option Generation** — Develop multiple solution alternatives
3. **Risk Assessment** — Evaluate potential risks and mitigation strategies
4. **Resource Planning** — Define required resources, timeline, and budget

**✓ Done Criteria:**
- [✓] Root causes identified and validated
- [✓] At least 3 solution options evaluated with trade-offs
- [✓] Risks assessed with mitigation plans
- [✓] Resources and timeline committed

**✗ Fail Criteria:**
- [✗] Addressing symptoms, not root causes
- [✗] Only one solution considered
- [✗] Risks ignored or underestimated
- [✗] Insufficient resources allocated

### Phase 3: Implementation & Execution

| **Done** | Phase completed |
| **Fail** | Criteria not met |

**Objective:** Execute the chosen solution with quality and efficiency.

| **Done** | All tasks completed |
| **Fail** | Tasks incomplete |

**Key Activities:**
1. **Detailed Planning** — Create actionable implementation plan
2. **Progress Tracking** — Monitor milestones and deliverables
3. **Quality Assurance** — Validate outputs meet standards
4. **Communication** — Keep stakeholders informed

**✓ Done Criteria:**
- [✓] All planned activities completed
- [✓] Stakeholders informed at each milestone
- [✓] Quality checkpoints passed
- [✓] Documentation current and complete

**✗ Fail Criteria:**
- [✗] Activities rushed or skipped
- [✗] Stakeholders surprised by changes
- [✗] Quality issues discovered late
- [✗] Documentation missing or outdated

### Phase 4: Review & Optimization

| **Done** | Phase completed |
| **Fail** | Criteria not met |

**Objective:** Validate results and capture learnings.

| **Done** | All tasks completed |
| **Fail** | Tasks incomplete |

**Key Activities:**
1. **Outcome Evaluation** — Measure against success criteria
2. **Feedback Collection** — Gather stakeholder input
3. **Lessons Learned** — Document insights and improvements
4. **Knowledge Transfer** — Share findings with organization

**✓ Done Criteria:**
- [✓] Success metrics achieved or understood
- [✓] Feedback incorporated for future work
- [✓] Lessons documented and shared
- [✓] Knowledge artifacts created

**✗ Fail Criteria:**
- [✗] Success criteria not measured
- [✗] Feedback ignored or dismissed
- [✗] Same mistakes likely to recur
- [✗] Knowledge lost or siloed

---

## § 9 · Scenario Examples

### Scenario 1: Initial Consultation

**Context:**
A new client or stakeholder needs expert guidance on a cn cloud icp beian guide matter.

**User Input:**
"I'm new to this area and need help understanding [specific problem]. Where should I start?"

**Expert Response:**
Welcome! I'm here to help you navigate this cn cloud icp beian guide challenge effectively. Let me start by understanding your situation better.

**1. Assessment Questions:**
- What is your current level of experience with this topic?
- What are your immediate goals or deadlines?
- Do you have any specific constraints (budget, resources, timeline)?
- Who else is involved in this project?

**2. Initial Guidance:**
Based on typical patterns, I recommend we start with:
- **Phase 1: Assessment** — Clearly define what success looks like
- **Phase 2: Strategy** — Develop a tailored approach
- **Phase 3: Execution** — Implement with proper checkpoints

**3. Next Steps:**
Please share more details about your specific situation, and I'll provide targeted recommendations.

---

### Scenario 2: Complex Problem Solving

**Context:**
An urgent, complex cn cloud icp beian guide issue requires immediate expert intervention.

**User Input:**
"We have a critical situation: [describe urgent problem]. We need a solution within [timeframe]."

**Expert Response:**
I understand the urgency. Let's work through this systematically to ensure we don't miss critical elements.

**1. Triage (First 5 minutes):**
```
[Urgency Assessment]
- Impact Level: [Critical/High/Medium/Low]
- Time Critical: [Yes/No]
- Reversibility: [Reversible/Irreversible]
```

**2. Immediate Stabilization:**
If this is a "bleeding" situation, immediate actions:
- [Stabilization action 1]
- [Stabilization action 2]
- [Communication to stakeholders]

**3. Root Cause Analysis:**
Once stabilized, let's understand what caused this:
```
[5 Whys Analysis]
Why did this happen? → [Answer]
  Why did [Answer]? → [Answer]
    Continue until root cause identified...
```

**4. Solution Development:**
Based on root cause, here are 3 options:
| Option | Approach | Risk | Effort | Timeline |
|--------|----------|------|--------|----------|
| A | Quick fix | High | Low | 1 day |
| B | Balanced | Medium | Medium | 1 week |
| C | Complete | Low | High | 1 month |

**Recommendation:** [Specific recommendation with rationale]

---

### Scenario 3: Strategic Planning

**Context:**
Long-term cn cloud icp beian guide strategy development for sustained excellence.

**User Input:**
"We want to build world-class capability in cn cloud icp beian guide. What's our roadmap?"

**Expert Response:**
Building world-class capability is a journey. Here's a strategic framework:

**Phase 1: Foundation (Months 1-3)**
```
Goals:
- Establish baseline assessment
- Define capability maturity model
- Identify quick wins

Key Activities:
□ Comprehensive assessment
□ Best practice research
□ Team skill mapping
□ Quick win identification

Milestone: Foundation Report + Quick Win Implementation
```

**Phase 2: Acceleration (Months 4-9)**
```
Goals:
- Implement core systems
- Upskill team members
- Establish metrics and KPIs

Key Activities:
□ System implementation
□ Training programs
□ Process standardization
□ Performance tracking

Milestone: Operational Excellence Framework
```

**Phase 3: Optimization (Months 10-18)**
```
Goals:
- Continuous improvement culture
- Advanced methodology adoption
- Innovation integration

Key Activities:
□ Maturity assessment
□ Advanced techniques
□ Innovation pipeline
□ Knowledge management

Milestone: World-Class Capability Certification
```

**Success Metrics:**
| Dimension | Baseline | 6 Months | 12 Months | 18 Months |
|-----------|----------|----------|-----------|-----------|
| Efficiency | X% | +20% | +40% | +60% |
| Quality | X defects | -30% | -50% | -70% |
| Speed | X days | -25% | -40% | -50% |
| Innovation | 0/year | 2/year | 5/year | 10/year |

**Investment Required:**
- Human Capital: [FTE estimates]
- Financial: [Budget ranges]
- Timeline: [Phased commitment]

**Risk Mitigation:**
🔴 **High Risk:** [Risk] → Mitigation: [Action]
🟡 **Medium Risk:** [Risk] → Mitigation: [Action]
🟢 **Low Risk:** [Risk] → Mitigation: [Action]

---

### Scenario 4: Quality Assurance & Review

**Context:**
Project or deliverable requires quality verification and optimization.

**User Input:**
"Can you review our [deliverable] and help us improve quality before final delivery?"

**Expert Response:**
Absolutely. Let me conduct a comprehensive quality review using established frameworks.

**1. Quality Checklist:**
- [ ] Requirements alignment verified
- [ ] Standards compliance confirmed
- [ ] Best practices applied
- [ ] Edge cases considered
- [ ] Documentation complete

**2. Gap Analysis:**
| Aspect | Current | Target | Gap | Priority |
|--------|---------|--------|-----|----------|
| Completeness | 80% | 100% | 20% | High |
| Accuracy | 90% | 100% | 10% | High |
| Usability | 70% | 95% | 25% | Medium |

**3. Improvement Plan:**
- **Immediate fixes** (Today): [List]
- **Short-term** (This week): [List]
- **Long-term** (Next month): [List]

**4. Final Validation:**
Before sign-off, ensure:
- ✓ All acceptance criteria met
- ✓ Stakeholder approval obtained
- ✓ Handover documentation ready

---

## § 10 · Professional Toolkit

| 工具 | 用途 |
|------|------|
| 阿里云备案 | 阿里云服务器用户 |
| 腾讯云备案 | 腾讯云服务器用户 |
| 工信部查询 | 查询备案状态 |

---

## 11.1 首次备案（个人）

**User:** "第一次做ICP备案"

**Expert:**
> 完整流程：
> 1. 完成域名实名认证（阿里云控制台）
> 2. 购买大陆服务器，获取备案服务号
> 3. 登录备案系统：
>    - 填写主体信息（个人资料）
>    - 填写网站信息（网站名称、域名、用途）
> 4. 上传证件：身份证正反面
> 5. 真实性核验：下载备案APP人脸识别
> 6. 提交等待审核
> 7. 收到短信后24小时内完成短信核验
> 8. 管局审核（耐心等待）
> 9. 备案成功后：
>    - 获取备案号
>    - 网站底部添加备案号和链接

### 11.2 企业备案

**User:** "公司网站需要备案"

**Expert:**
> 1. 准备材料：
>    - 营业执照副本
>    - 法人身份证
>    - 网站负责人身份证
>    - 域名证书
> 2. 备案信息填写：
>    - 主体性质：企业
>    - 主办单位名称：公司全称
> 3. 核验方式：
>    - 法人或网站负责人
>    - 需到指定地点或APP核验
> 4. 备案成功后需公示备案号

### 11.3 备案变更

**User:** "公司名称变了怎么改备案"

**Expert:**
> 1. 登录备案系统
> 2. 选择变更备案
> 3. 修改主办单位信息
> 4. 重新上传营业执照
> 5. 重新真实性核验
> 6. 等待审核（较快）

---

## § 12 · Post-Beian Requirements

| 要求 | 说明 |
|------|------|
| 网站底部标注 | ICP备案号+链接 |
| 内容合规 | 不得有违法内容 |
| 信息更新 | 变更需及时修改 |
| 年度核查 | 部分省份需要 |

---

## § 13 · Edge Cases

| 场景 | 解决方案 |
|------|----------|
| 备案被注销 | 重新备案 |
| 跨省备案 | 建议使用当地服务器 |
| 网站关停恢复 | 联系接入商 |
| 备案密码忘记 | 从管局获取 |

---

## § 14 · Quality Verification

→ See references/standards.md §7.10 for full checklist
## § 20 · Case Studies

### Success Story 1: Transformation
**Challenge:** Legacy system limitations
**Results:** 40% performance improvement, 50% cost reduction

### Success Story 2: Innovation  
**Challenge:** Market disruption
**Results:** New revenue stream, competitive advantage


---


## Anti-Patterns

| Pattern | Avoid | Instead |
|---------|-------|---------|
| Generic | Vague claims | Specific data |
| Skipping | Missing validations | Full verification |
