---
name: aliyun-cdn-expert
kind: tool-skill
version: 1.0.0
tags:
  - domain: tools
  - subtype: aliyun-cdn-expert
  - level: expert
description: 阿里云CDN专家：加速配置、缓存策略、HTTPS、回源优化。Use when configuring CDN acceleration, cache rules, or optimizing delivery. Triggers: 'CDN', '阿里云CDN', '缓存', '加速'. Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
---

# Aliyun CDN Expert

## Decision Framework

| Scenario | Recommendation |
|----------|----------------|
| Static website | Cache everything, long TTL |
| API responses | No-cache, bypass CDN |
| User-generated content | Short TTL, versioned URLs |
| Live streaming | Use dedicated live CDN |

---


### Thinking Patterns

| Pattern | When to Use | Approach |
|---------|-------------|----------|
| First-Principles | Novel problems | Break down to fundamentals |
| Pattern Matching | Known scenarios | Apply proven templates |
| Constraint Optimization | Resource limits | Maximize within bounds |
| Systems Thinking | Complex interactions | Consider holistic impact |


## § 2 · What This Skill Does

1. **域名配置** — 添加加速域名
2. **缓存规则** — 缓存策略设置
3. **性能优化** — 压缩、回源

---

## § 3 · Platform Support

**[URL]:** `https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/tools/cn-cloud/aliyun/aliyun-cdn-expert.md`

---

## § 4 · Pricing

| 计费方式 | 价格 |
|----------|------|
| 流量 | ¥0.24/GB |
| 带宽峰值 | ¥377/Mbps/月 |

---

## § 5 · Core Configuration

### 5.1 添加加速域名

1. 进入CDN控制台 → 添加域名
2. 选择业务类型（图片小文件/大文件下载/视频点播）
3. 配置源站（IP/域名/OSS）
4. 等待全球节点生效（5-30分钟）

### 5.2 缓存配置

| 类型 | 推荐TTL | 场景 |
|------|---------|------|
| 静态资源 | 1-7天 | JS/CSS/图片 |
| HTML | 1小时 | 频繁更新 |
| API | 0 | 实时数据 |

---

## § 6 · Standards & Reference

### 6.1 Nginx配置示例

```nginx
location ~* \.(jpg|png|gif|js|css)$ {
    expires 7d;
    add_header Cache-Control "public";
}
```

### 6.2 性能优化参数

| 参数 | 推荐值 | 作用 |
|------|--------|------|
| 压缩 | gzip/brotli | 减少传输量 |
| HTTP/2 | 开启 | 多路复用 |
| QUIC | 开启 | 低延迟 |

---

## § 7 · Risk Disclaimer

| 风险 | 级别 | 建议 |
|------|------|------|
| 流量突增 | 🟡 | 配置带宽封顶 |
| 源站压力大 | 🟡 | 开启二级缓存 |
| HTTPS配置错误 | 🟡 | 使用阿里云证书 |

---

## 9.1 WordPress站点加速

**User:** "想加速WordPress网站"

**Expert:**
> 1. 添加域名到CDN
> 2. 配置缓存规则：
>    - `/wp-content/*` 缓存7天
>    - `/wp-admin/*` 不缓存
> 3. 开启Gzip压缩
> 4. 配置HTTPS（免费SSL）
> 5. 绑定回源host避免404

### 9.2 图片存储加速

**User:** "使用OSS存储图片，如何加速？"

**Expert:**
> 1. OSS作为源站
> 2. 开启图片处理（缩略/水印）
> 3. 配置referer防盗链
> 4. 设置CDN域名解析

### 9.3 刷新缓存

**User:** "需要更新CDN缓存的内容"

**Expert:**
> 1. CDN控制台 → 刷新缓存
> 2. 支持URL刷新/目录刷新
> 3. 刷新后全球生效需5-10分钟

---


### § 10 · Edge Cases

| 问题 | 解决方案 |
|------|----------|
| 缓存不生效 | 检查Cache-Control头 |
| 回源失败 | 检查源站443端口 |
| 502错误 | 源站响应超时 |
| 带宽账单高 | 配置带宽封顶/阶梯计费 |

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
A new client or stakeholder needs expert guidance on a aliyun cdn expert matter.

**User Input:**
"I'm new to this area and need help understanding [specific problem]. Where should I start?"

**Expert Response:**
Welcome! I'm here to help you navigate this aliyun cdn expert challenge effectively. Let me start by understanding your situation better.

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
An urgent, complex aliyun cdn expert issue requires immediate expert intervention.

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
Long-term aliyun cdn expert strategy development for sustained excellence.

**User Input:**
"We want to build world-class capability in aliyun cdn expert. What's our roadmap?"

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

## § 11 · Monitoring

| 指标 | 告警阈值 |
|------|----------|
| 命中率 | <80%需优化 |
| 带宽峰值 | >80%带宽上限 |
| 4xx错误率 | >1%需检查 |

---

## § 12 · Scope & Limitations

**In Scope:**
- CDN acceleration configuration
- Cache strategy design
- HTTPS/SSL configuration
- Origin pull optimization
- Performance monitoring

**Out of Scope:**
- DDoS protection (use security products)
- Application-level optimization
- Origin server configuration
- Complex geo-blocking rules

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
