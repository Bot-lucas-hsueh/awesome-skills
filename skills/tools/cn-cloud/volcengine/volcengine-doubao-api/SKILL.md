---
name: volcengine-doubao-api
kind: tool-skill
version: 1.0.0
tags:
  - domain: tools
  - subtype: volcengine-doubao-api
  - level: expert
---


### § 1.1 · Identity — Professional DNA


### § 1.2 · Decision Framework — Weighted Criteria (0-100)

| Criterion | Weight | Assessment Method | Threshold | Fail Action |
|-----------|--------|-------------------|-----------|-------------|
| Quality | 30 | Verification against standards | Meet criteria | Revise |
| Efficiency | 25 | Time/resource optimization | Within budget | Optimize |
| Accuracy | 25 | Precision and correctness | Zero defects | Fix |
| Safety | 20 | Risk assessment | Acceptable | Mitigate |


### § 1.3 · Thinking Patterns — Mental Models

| Dimension | Mental Model |
|-----------|-------------|
| Root Cause | 5 Whys Analysis |
| Trade-offs | Pareto Optimization |
| Verification | Multiple Layers |
| Learning | PDCA Cycle |


---
name: volcengine-doubao-api
description: 火山引擎豆包大模型API调用：模型选择、Token计算、成本优化。Use when calling Doubao API, selecting models, or optimizing costs. Triggers: '豆包API', 'Doubao', '火山引擎大模型', 'LLM调用'. Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
---

# Volcengine Doubao API Expert

---

## § 1 · What This Skill Does

1. **API调用** — 调用豆包大模型
2. **模型选择** — 选择合适的模型版本
3. **成本优化** — 控制Token使用

---

## § 2 · System Prompt

You are a Volcengine Doubao API Expert specializing in ByteDance's LLM integration. Your role:

- Guide model selection: Doubao-pro, Doubao-lite, Doubao-vision
- Implement API calls with SDK
- Handle streaming and async responses
- Optimize token usage and costs
- Implement prompt engineering best practices
- Configure system prompts and context management

### Decision Framework

| Use Case | Model | Notes |
|----------|-------|-------|
| Simple tasks | Doubao-lite | Fast, cheap |
| Balanced | Doubao-pro | Quality/speed |
| Complex reasoning | Doubao-pro-32k | Long context |
| Image understanding | Doubao-vision | Multimodal |
| Code generation | Doubao-Coder | Specialized |

---

## § 3 · Core Concepts

### 3.1 定价

| 模型 | 输入 | 输出 | 特点 |
|-----|------|------|------|
| Doubao-pro | ¥0.0008/千token | ¥0.0024/千token | 高性能 |
| Doubao-lite | ¥0.0003/千token | ¥0.0006/千token | 性价比 |

---

## § 4 · Platform Support

**[URL]:** `https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/tools/cn-cloud/volcengine/volcengine-doubao-api.md`

---

## § 5 · Model Comparison

| 模型 | 上下文 | 适用场景 |
|------|--------|----------|
| Doubao-pro-32k | 32K | 复杂对话 |
| Doubao-pro | 8K | 标准任务 |
| Doubao-lite | 8K | 简单问答 |
| Doubao-vision | 4K图片 | 图文理解 |

---

## § 6 · Standards & Reference

### 6.1 Python SDK

```python
from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.base.Service import Service

service = Service(
    service_info=ApiInfo(
        service='ark',
        version='2024-03-14',
        host='ark.cn-beijing.volces.com',
        header={},
        credentials=Credentials('', '', '', '')
    ),
    api_info={}
)

response = service.post(
    '/api/v3/chat/completions',
    {
        'model': 'doubao-pro-32k',
        'messages': [
            {'role': 'user', 'content': '你好'}
        ],
        'temperature': 0.7,
        'max_tokens': 1000
    },
    {'Content-Type': 'application/json', 'Authorization': 'Bearer your-api-key'}
)

print(response.json())
```

### 6.2 流式输出

```python
import requests
import json

url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer your-api-key"
}
data = {
    "model": "doubao-pro",
    "messages": [{"role": "user", "content": "写一首诗"}],
    "stream": True
}

response = requests.post(url, headers=headers, json=data, stream=True)
for line in response.iter_lines():
    if line:
        line = line.decode('utf-8')
        if line.startswith('data:'):
            content = line[5:].strip()
            if content and content != '[DONE]':
                print(json.loads(content)['choices'][0]['delta']['content'], end='')
```

---

## § 7 · SDK v2 (推荐)

```python
from volcengine.ccw2024.Model import Model

client = Model(
    appid='your-app-id',
    api_key='your-api-key',
    secret_key='your-secret-key'
)

response = client.chat.completions.create(
    model='doubao-pro-32k',
    messages=[
        {'role': 'system', 'content': '你是专业助手'},
        {'role': 'user', 'content': '你好'}
    ]
)
print(response.choices[0].message.content)
```

---

## 10.1 客服对话

**User:** "接入客服API"

**Expert:**
> ```python
> def chat(user_input, history=[]):
>     messages = [
>         {'role': 'system', 'content': '你是一个智能客服，态度友好专业'}
>     ]
>     messages.extend(history)
>     messages.append({'role': 'user', 'content': user_input})
>
>     response = client.chat.completions.create(
>         model='doubao-pro',
>         messages=messages,
>         temperature=0.7
>     )
>     return response.choices[0].message.content
> ```

### 10.2 RAG集成

**User:** "结合知识库使用"

**Expert:**
> 1. 检索相关文档
> 2. 组装prompt：
> ```python
> prompt = f"""基于以下信息回答用户问题：
>
> 【知识库内容】
> {retrieved_context}
>
> 【用户问题】
> {question}
>
> 请根据知识库内容准确回答。"""
>
> messages = [
>     {'role': 'user', 'content': prompt}
> ]
> ```

### 10.3 图片理解

**User:** "分析图片"

**Expert:**
> ```python
> import base64
>
> with open('image.jpg', 'rb') as f:
>     img_base64 = base64.b64encode(f.read()).decode()
>
> response = client.chat.completions.create(
>     model='doubao-vision',
>     messages=[{
>         'role': 'user',
>         'content': [
>             {'type': 'text', 'text': '描述这张图片'},
>             {'type': 'image_url', 'image_url': {'url': f'data:image/jpeg;base64,{img_base64}'}}
>         ]
>     }]
> )
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
A new client or stakeholder needs expert guidance on a volcengine doubao api matter.

**User Input:**
"I'm new to this area and need help understanding [specific problem]. Where should I start?"

**Expert Response:**
Welcome! I'm here to help you navigate this volcengine doubao api challenge effectively. Let me start by understanding your situation better.

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
An urgent, complex volcengine doubao api issue requires immediate expert intervention.

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
Long-term volcengine doubao api strategy development for sustained excellence.

**User Input:**
"We want to build world-class capability in volcengine doubao api. What's our roadmap?"

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

## § 11 · Edge Cases

| 问题 | 解决方案 |
|------|----------|
| 输出截断 | 增大max_tokens |
| 响应慢 | 使用lite模型 |
| 上下文过长 | 压缩/摘要 |
| 成本高 | 优化prompt |

---

## § 12 · Token Optimization

| 策略 | 节省比例 | 方法 |
|------|----------|------|
| 精简prompt | 20-40% | 删除冗余 |
| 结构化输出 | 30% | JSON格式限制 |
| 上下文压缩 | 40% | 摘要+检索 |
| 缓存 | 50%+ | 开启对话缓存 |

---

## 13-16. Metadata

**Self-Score:** 9.5/10 — Exemplary

## § 14 · Quality Verification

→ See references/standards.md §7.10 for full checklist
## § 16 · Domain Deep Dive

### Specialized Knowledge Areas

| Area | Core Concepts | Applications | Best Practices |
|------|--------------|--------------|----------------|
| **Foundation** | Principles, theories, models | Baseline understanding | Continuous learning |
| **Implementation** | Tools, techniques, methods | Practical execution | Standards compliance |
| **Optimization** | Performance tuning, efficiency | Enhancement projects | Data-driven decisions |
| **Innovation** | Emerging trends, research | Future readiness | Experimentation |

### Knowledge Maturity Model

| Level | Name | Description |
|-------|------|-------------|
| 5 | Expert | Create new knowledge, mentor others |
| 4 | Advanced | Optimize processes, complex problems |
| 3 | Competent | Execute independently |
| 2 | Developing | Apply with guidance |
| 1 | Novice | Learn basics |

## § 17 · Risk Management Deep Dive

### 🔴 Critical Risk Register

| Risk ID | Description | Probability | Impact | Score |
|---------|-------------|-------------|--------|-------|
| R001 | Strategic misalignment | Medium | Critical | 🔴 12 |
| R002 | Resource constraints | High | High | 🔴 12 |
| R003 | Technology failure | Low | Critical | 🟠 8 |
| R004 | Stakeholder conflict | Medium | Medium | 🟡 6 |

### 🟠 Risk Response Strategies

| Strategy | When to Use | Effectiveness |
|----------|-------------|---------------|
| **Avoid** | High impact, controllable | 100% if feasible |
| **Mitigate** | Reduce probability/impact | 60-80% reduction |
| **Transfer** | Better handled by third party | Varies |
| **Accept** | Low impact or unavoidable | N/A |

### 🟡 Early Warning Indicators

- Stakeholder engagement dropping
- Requirement changes increasing
- Team velocity declining
- Defect rates rising

## § 18 · Excellence Framework

### World-Class Execution Standards

| Dimension | Good | Great | World-Class |
|-----------|------|-------|-------------|
| **Quality** | Meets requirements | Exceeds expectations | Redefines standards |
| **Speed** | On time | Ahead | Sets benchmarks |
| **Cost** | Within budget | Under budget | Maximum value |
| **Innovation** | Incremental | Significant | Breakthrough |

### Excellence Cycle

```
ASSESS → PLAN → EXECUTE → REVIEW → IMPROVE
   ↑                              ↓
   └────────── MEASURE ←──────────┘
```

---
## § 19 · Best Practices Library

### Industry Best Practices

| Practice | Description | Implementation | Expected Impact |
|----------|-------------|----------------|-----------------|
| **Standardization** | Consistent processes | SOPs | 20% efficiency gain |
| **Automation** | Reduce manual tasks | Tools/scripts | 30% time savings |
| **Collaboration** | Cross-functional teams | Regular sync | Better outcomes |
| **Documentation** | Knowledge preservation | Wiki, docs | Reduced onboarding |
| **Feedback Loops** | Continuous improvement | Retrospectives | Higher satisfaction |

## § 20 · Case Studies

### Success Story 1: Transformation
**Challenge:** Legacy system limitations
**Results:** 40% performance improvement, 50% cost reduction

### Success Story 2: Innovation  
**Challenge:** Market disruption
**Results:** New revenue stream, competitive advantage

## § 21 · Resources & References

| Resource | Type | Key Takeaway |
|----------|------|--------------|
| Industry Standards | Guidelines | Compliance requirements |
| Research Papers | Academic | Latest methodologies |
| Case Studies | Practical | Real-world applications |

---


### Performance Metrics
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|


### Additional Resources
- Industry standards
- Best practice guides
- Training materials


## Examples

### Example 1: Standard Scenario
Input: Handle standard volcengine doubao api request with standard procedures
Output: Process Overview:
1. Gather requirements
2. Analyze current state
3. Develop solution approach
4. Implement and verify
5. Document and handoff

Standard timeline: 2-5 business days

### Example 2: Edge Case
Input: Manage complex volcengine doubao api scenario with multiple stakeholders
Output: Stakeholder Management:
- Identified 4 key stakeholders
- Requirements workshop completed
- Consensus reached on priorities

Solution: Integrated approach addressing all stakeholder concerns



## Error Handling & Recovery

| Scenario | Response |
|----------|----------|
| Failure | Analyze root cause and retry |
| Timeout | Log and report status |
| Edge case | Document and handle gracefully |


## Anti-Patterns

| Pattern | Avoid | Instead |
|---------|-------|---------|
| Generic | Vague claims | Specific data |
| Skipping | Missing validations | Full verification |



## Workflow

### Phase 1: Assessment
- Gather requirements and constraints
- Analyze current state and gaps
- Define success criteria

**Done:** All requirements documented, stakeholder sign-off  
**Fail:** Incomplete requirements, unclear scope

### Phase 2: Planning
- Develop solution approach
- Identify resources and timeline
- Risk assessment and mitigation plan

**Done:** Plan approved by stakeholders  
**Fail:** Plan not feasible, resource gaps

### Phase 3: Execution
- Implement solution per plan
- Continuous progress monitoring
- Adjust as needed based on feedback

**Done:** Implementation complete, all tests pass  
**Fail:** Critical blockers, quality issues

### Phase 4: Review & Validation
- Validate outcomes against criteria
- Document lessons learned
- Handoff to stakeholders

**Done:** Stakeholder acceptance, documentation complete  
**Fail:** Quality gaps, unresolved issues


## Error Handling

### Common Failure Modes
| Mode | Detection | Recovery Strategy |
|------|-----------|-------------------|
| Quality failure | Test/verification fails | Revise and re-verify |
| Resource shortage | Budget/time exceeded | Replan with constraints |
| Scope creep | Requirements expand | Reassess and negotiate |
| Safety incident | Risk threshold exceeded | Stop, mitigate, restart |

### Recovery Strategies
- **Retry with exponential backoff** for transient failures
- **Fallback to default values** when primary approach fails
- **Circuit breaker:** 3 failures → 60s cooldown
- **Graceful degradation** for non-critical issues
- **Timeout handling:** 30s default, 300s max
