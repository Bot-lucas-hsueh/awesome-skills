---
name: tencentcloud-hunyuan-api
kind: tool
version: 1.0.0
tags:
  - domain: tools
  - subtype: tencentcloud-hunyuan-api
  - level: expert
description: 腾讯混元大模型API：模型调用、多模态理解、费用说明。Use when calling Tencent Hunyuan LLM API. Triggers: '混元', 'Hunyuan', 'API调用', '腾讯LLM'. Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
---

# Tencent Hunyuan API Expert

## Decision Framework

| Use Case | Model | Notes |
|----------|-------|-------|
| Complex tasks | Hunyuan-pro | Best quality |
| Standard tasks | Hunyuan-standard | Balanced |
| Simple tasks | Hunyuan-lite | Fast, cheap |
| Image understanding | Hunyuan-vision | Multimodal |

---


### Thinking Patterns

| Pattern | When to Use | Approach |
|---------|-------------|----------|
| First-Principles | Novel problems | Break down to fundamentals |
| Pattern Matching | Known scenarios | Apply proven templates |
| Constraint Optimization | Resource limits | Maximize within bounds |
| Systems Thinking | Complex interactions | Consider holistic impact |


## § 2 · What This Skill Does

1. **API调用** — SDK使用
2. **多模态** — 图文理解
3. **成本** — 计费说明

---

## § 3 · Platform Support

**[URL]:** `https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/tools/cn-cloud/tencent/tencentcloud-hunyuan-api.md`

---

## § 4 · Pricing

| 模型 | 输入 | 输出 |
|------|------|------|
| Hunyuan-pro | ¥0.0015/千token | ¥0.005/千token |
| Hunyuan-standard | ¥0.0006/千token | ¥0.001/千token |
| Hunyuan-lite | ¥0.0001/千token | ¥0.0003/千token |

---

## § 5 · Model Comparison

| 模型 | 上下文 | 适用场景 |
|------|--------|----------|
| Hunyuan-pro | 32K | 复杂推理 |
| Hunyuan-standard | 32K | 日常对话 |
| Hunyuan-lite | 32K | 简单问答 |
| Hunyuan-vision | 4K图片 | 图文理解 |

---

## § 6 · Standards & Reference

### 6.1 Python SDK

```python
import os
from tencentcloud.common import credential
from tencentcloud.common.profile import client_profile
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models

cred = credential.Credential("secret_id", "secret_key")
client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou")

req = models.ChatCompletionsRequest()
req.Model = "hunyuan-pro"
req.Messages = [
    {"Role": "system", "Content": "你是专业助手"},
    {"Role": "user", "Content": "什么是云计算?"}
]

resp = client.ChatCompletions(req)
print(resp.Choices[0].Message.Content)
```

### 6.2 流式输出

```python
req = models.ChatCompletionsRequest()
req.Model = "hunyuan-pro"
req.Messages = [{"Role": "user", "Content": "写一首诗"}]
req.Stream = True

for event in client.ChatCompletions(req):
    if event.Choices[0].Delta.Content:
        print(event.Choices[0].Delta.Content, end='')
```

---

## § 7 · Risk Disclaimer

| 风险 | 级别 | 建议 |
|------|------|------|
| API费用超支 | 🟡 | 设置配额 |
| 内容安全 | 🟡 | 开启审核 |
| 响应超时 | 🟡 | 增加超时设置 |

---

## 9.1 客服对话

**User:** "接入客服API"

**Expert:**
> ```python
> def chat(user_input, history=[]):
>     messages = [{"Role": "system", "Content": "你是智能客服"}]
>     messages.extend(history)
>     messages.append({"Role": "user", "Content": user_input})
>
>     req = models.ChatCompletionsRequest()
>     req.Model = "hunyuan-pro"
>     req.Messages = messages
>
>     resp = client.ChatCompletions(req)
>     return resp.Choices[0].Message.Content
> ```

### 9.2 图文理解

**User:** "分析图片内容"

**Expert:**
> ```python
> import base64
>
> with open("image.jpg", "rb") as f:
>     img_base64 = base64.b64encode(f.read()).decode()
>
> req = models.ChatCompletionsRequest()
> req.Model = "hunyuan-vision"
> req.Messages = [{
>     "Role": "user",
>     "Content": [
>         {"Type": "text", "Text": "描述这张图片"},
>         {"Type": "image_url", "ImageUrl": {"Url": f"data:image/jpeg;base64,{img_base64}"}}
>     ]
> }]
> ```

### 9.3 RAG集成

**User:** "结合知识库使用"

**Expert:**
> 1. 检索相关文档
> 2. 组装prompt
> 3. 调用API
> ```python
> prompt = f"""基于以下信息回答问题：
>
> {retrieved_context}
>
> 问题：{question}
>
> 回答："""
> ```

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
A new client or stakeholder needs expert guidance on a tencentcloud hunyuan api matter.

**User Input:**
"I'm new to this area and need help understanding [specific problem]. Where should I start?"

**Expert Response:**
Welcome! I'm here to help you navigate this tencentcloud hunyuan api challenge effectively. Let me start by understanding your situation better.

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
An urgent, complex tencentcloud hunyuan api issue requires immediate expert intervention.

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
Long-term tencentcloud hunyuan api strategy development for sustained excellence.

**User Input:**
"We want to build world-class capability in tencentcloud hunyuan api. What's our roadmap?"

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

## § 10 · Edge Cases

| 问题 | 解决方案 |
|------|----------|
| 输出截断 | 增大max_tokens |
| 响应慢 | 使用lite模型 |
| 上下文过长 | 压缩/摘要 |
| 幻觉严重 | 优化prompt |

---

## § 11 · Content Moderation

| 配置 | 说明 |
|------|------|
| 输入审核 | 自动审核用户输入 |
| 输出审核 | 自动审核模型输出 |
| 自定义词库 | 敏感词过滤 |

---

## § 12 · Scope & Limitations

**In Scope:**
- Hunyuan API calling
- Model selection
- Token optimization

**Out of Scope:**
- Custom fine-tuning
- Prompt engineering services

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
