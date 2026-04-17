---
name: machine-learning-engineer
kind: persona
version: 1.0.0
tags:
  - domain: ai-ml
  - subtype: machine-learning-engineer
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
name: evaluation-report--machine-learning-engineer
description: Expert skill for Evaluation Report — machine-learning-engineer
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
---

## Skill Summary
| Field | Value |
|-------|-------|
| **Name** | machine-learning-engineer |
| **Version** | 5.0.0 |
| **Quality Tier** | Exemplary ⭐⭐ |
| **Rubric Score** | 9.2/10 |
| **Line Count** | 494 |

---

## 6-Dimension Rubric Scores

| Dimension | Score | Weight | Weighted | Tier |
|-----------|-------|--------|----------|------|
| System Prompt Depth | 9.0 | 20% | 1.80 | Exemplary |
| Domain Knowledge Density | 9.5 | 25% | 2.375 | Exemplary |
| Workflow Actionability | 9.0 | 15% | 1.35 | Exemplary |
| Risk Documentation | 8.5 | 10% | 0.85 | Expert |
| Example Quality | 9.0 | 20% | 1.80 | Exemplary |
| Metadata Completeness | 9.5 | 10% | 0.95 | Exemplary |

---

## Strengths

### §1 System Prompt — Exemplary
- Principal engineer identity at Google/Meta/Netflix scale (billions of predictions daily)
- Professional DNA table (4 attributes: Feature Engineer, Model Architect, Scale Optimizer, Production Focused)
- Core Competencies table (5 domains: Frameworks, Training, Features, Deployment, Optimization) with scale evidence
- **Decision Framework**: 5-gate hierarchy matching the rubric dimensions
- **5 Thinking Patterns**: Baseline-First, Feature-Centric, Training-Serving Skew Prevention, Reproducible Experiments, Production-First Design
- Each pattern includes specific practices
- **Verdict**: Exemplary

### §2 What This Skill Does
- 5 capabilities: Feature Engineering, Model Development, Distributed Training, Model Optimization, Production ML Systems
- Measurable outcomes

### §3 Risk Documentation — Strong
- 6 risks (3 🔴 Critical, 2 🟠 High, 1 🟡 Medium)
- Critical risks: overfitting, training-serving skew, data leakage
- Specific mitigations

### §4 Core Philosophy
- ML System Architecture (6-layer ASCII diagram)
- 5 guiding principles

### §5 Professional Toolkit
- 7 categories with specific tools (PyTorch, TensorFlow, JAX, XGBoost, Horovod, MLflow, TorchServe, TensorRT, Feast)
- Clear use case for each

### §6 Domain Knowledge
- Model Selection Guide (5 problem types)
- Distributed Training Methods (4 methods with scaling)
- Inference Optimization (5 techniques with speedup ratios)
- **Verdict**: High density, specific metrics

### §7 Standard Workflow
- 4 phases (Problem Definition, Feature Engineering, Model Development, Production Deployment) over 25 days
- [✓ Done]/[✗ FAIL] criteria

### §8 Scenario Examples
- **5 full scenarios**: Recommendation System, Fraud Detection, CV Model, NLP Sentiment, Time Series Forecasting
- Each with Features → Model → Optimization → Results structure
- Specific metrics (20% watch time increase, 10ms p99 latency, 87% top-1 accuracy, 92% F1)
- Diverse coverage across ML domains

### §9 Common Pitfalls
- 6 anti-patterns (over-engineering, data leakage, class imbalance, no validation, feature overfitting, neglecting inference cost)
- Specific to ML engineering

### §10 Scope & Limitations
- Clear ✓/✗ with specific skill references

---

## Weaknesses

### ❌ Missing §5 Platform Support (Severity: High)
- No platform installation section

### ❌ Missing Quality Verification Section
- §11 References exist pointing to 4 `references/` files
- These files likely don't exist

### ❌ References Point to Non-Existent Files
- Same issue as ai-product-manager

### ❌ Risk Documentation Slightly Below Exemplary
- Could quantify more risks with specific dollar/metric impacts

---

## Anti-Patterns Detected

| # | Anti-Pattern | Severity | Location |
|---|-------------|----------|----------|
| #9 | Platform Coverage Miss — §5 Platform Support absent | 🔴 High | Missing section |
| — | References to non-existent files | 🟡 Medium | §11 |

---

## Token Budget Analysis

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| SKILL.md lines | 494 | ≤500 | ✅ Within budget |
| Room for platform section | ~6-10 lines | — | Need to trim elsewhere |

---

## Recommendation

**Tier: Exemplary ⭐⭐** (9.2/10)

Identical quality tier as ai-product-manager. The 11-section structure is the right choice for this domain. 5 diverse, quantified scenario examples with specific ML metrics. Same single blocking issue: missing platform support section.

**Immediate actions required:**
1. Add §5 Platform Support table (~10 lines)
2. Trim ~10 lines from existing content to stay under 500
3. Verify/create the 4 `references/` files

After fixes: Estimated score → 9.3/10 Exemplary ⭐⭐

**One of the two best AI-ML skills in this batch. Platform support addition is the only blocker.**


## Workflow

### Phase 1: Requirements
- Gather functional and non-functional requirements
- Clarify acceptance criteria
- Document technical constraints

**Done:** Requirements doc approved, team alignment achieved
**Fail:** Ambiguous requirements, scope creep, missing constraints

### Phase 2: Design
- Create system architecture and design docs
- Review with stakeholders
- Finalize technical approach

**Done:** Design approved, technical decisions documented
**Fail:** Design flaws, stakeholder objections, technical blockers

### Phase 3: Implementation
- Write code following standards
- Perform code review
- Write unit tests

**Done:** Code complete, reviewed, tests passing
**Fail:** Code review failures, test failures, standard violations

### Phase 4: Testing & Deploy
- Execute integration and system testing
- Deploy to staging environment
- Deploy to production with monitoring

**Done:** All tests passing, successful deployment, monitoring active
**Fail:** Test failures, deployment issues, production incidents

## Examples

### Example 1: Standard Scenario

| **Done** | All steps complete |
| **Fail** | Steps incomplete |
Input: Design and implement a machine learning engineer solution for a production system
Output: Requirements Analysis → Architecture Design → Implementation → Testing → Deployment → Monitoring

Key considerations for machine-learning-engineer:
- Scalability requirements
- Performance benchmarks
- Error handling and recovery
- Security considerations

### Example 2: Edge Case

| **Done** | All steps complete |
| **Fail** | Steps incomplete |
Input: Optimize existing machine learning engineer implementation to improve performance by 40%
Output: Current State Analysis:
- Profiling results identifying bottlenecks
- Baseline metrics documented

Optimization Plan:
1. Algorithm improvement
2. Caching strategy
3. Parallelization

Expected improvement: 40-60% performance gain



## Error Handling & Recovery

| Scenario | Response |
|----------|----------|
| Failure | Analyze root cause and retry |
| Timeout | Log and report status |
| Edge case | Document and handle gracefully |
