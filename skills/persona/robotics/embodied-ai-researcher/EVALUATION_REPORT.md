# Skill Evaluation Report: embodied-ai-researcher

**Evaluation Date:** 2026-03-24  
**Evaluator:** skill-writer methodology  
**Quality Tier:** Expert ⭐ (7.8/10)

---

## 1. System Prompt Depth (Score: 9/10)

| Criterion | Assessment |
|-----------|------------|
| Role Definition | Senior Embodied AI Research Scientist with 10+ years, specific labs/companies, 30+ papers |
| Decision Framework | 5 gates: Safety, Reproducibility, Sim2Real, Data Efficiency, Benchmark |
| Thinking Patterns | 5 patterns: Task hierarchy, Observation-action space, Data pipeline, Failure mode taxonomy, Ablation logic |
| Communication Style | Cite papers with year, provide hyperparameters, quantify claims |

**Strengths:** Excellent safety-first framework; specific benchmarks (LIBERO, RLBench, BridgeData).

---

## 2. Domain Knowledge Density (Score: 9/10)

| Dimension | Evidence |
|-----------|----------|
| Frameworks | Policy architecture selection, IL pipeline, sim2real transfer, RL fine-tuning |
| Quantified Metrics | ACT 85% success with 50 demos, 0.95^10 compounding |
| Real Scenarios | RT-2, ACT, Diffusion Policy, OpenVLA implementations |

---

## 3. Workflow Actionability (Score: 6/10)

| Phase | Assessment |
|-------|------------|
| Discovery & Assessment | Generic |
| Analysis & Strategy | Generic |
| Implementation & Execution | Generic |
| Review & Optimization | Generic |

**Issue:** Generic template not adapted to embodied AI research workflow.

---

## 4. Risk Documentation (Score: 9/10)

| Risk | Severity | Quality |
|------|----------|---------|
| Real-robot policy deployment | CRITICAL | Excellent - collision checking |
| Overfit from small demos | HIGH | Good - 50+ demos guidance |
| Uncalibrated camera extrinsics | HIGH | Good - calibration protocol |
| Sim2real gap | HIGH | Good - contact randomization |
| Reward hacking | MEDIUM | Good - sparse rewards |
| Compounding errors | HIGH | Excellent - hierarchical policies |

---

## 5. Example Quality (Score: 7/10)

| Scenario | Assessment |
|----------|------------|
| Scenarios 1-4 | Generic patterns |
| Test Cases (§14) | Excellent - Architecture selection, sim2real triage, ablation study |

**Assessment:** Test cases provide strong domain-specific content.

---

## 6. Metadata Completeness (Score: 9/10)

| Field | Status |
|-------|--------|
| name | ✓ present |
| description | ✓ present |
| author | ✓ present |
| version | ✓ present (3.0.0) |
| difficulty | ✓ expert |
| category | ✓ robotics |
| tags | ✓ 10 tags |
| platforms | ✓ section present |
| license | ✓ MIT |

---

## Weighted Score Calculation

```
Score = (9×0.20) + (9×0.25) + (6×0.15) + (9×0.10) + (7×0.20) + (9×0.10)
      = 1.8 + 2.25 + 0.9 + 0.9 + 1.4 + 0.9 = 8.15 → 8.2 Expert
```

---

## Summary

| Dimension | Score | Tier |
|-----------|-------|------|
| System Prompt | 9/10 | Exemplary |
| Domain Knowledge | 9/10 | Exemplary |
| Workflow | 6/10 | Community |
| Risk Docs | 9/10 | Exemplary |
| Examples | 7/10 | Expert |
| Metadata | 9/10 | Exemplary |
| **Weighted** | **8.2/10** | **Expert ⭐** |

**Self-Score from SKILL.md:** 7.7/10 (underestimates by 0.5)
