# Skill Evaluation Report: 6g-communication-researcher

**Evaluation Date:** 2026-03-24  
**Evaluator:** skill-writer methodology  
**Quality Tier:** Expert ⭐ (7.7/10)

---

## 1. System Prompt Depth (Score: 9/10)

| Criterion | Assessment |
|-----------|------------|
| Role Definition | Principal Research Scientist with 12+ years, specific publications, hands-on USRP/Sionna experience |
| Decision Framework | 5 gates with specific technical criteria (frequency regime, near-field, hardware impairment, channel model, IMT-2030 KPI) |
| Thinking Patterns | 5 patterns with actionable thresholds (near-field first, channel capacity hierarchy, AI-native vs AI-assisted, RIS trade-off, semantic fidelity) |
| Communication Style | Led with physical layer fundamentals, includes MATLAB/Python pseudocode guidance, cites ITU/3GPP standards |

**Strengths:** Domain-specific gate framework with measurable thresholds; clear technical depth in 6G specific areas (sub-THz, OTFS, holographic MIMO)

---

## 2. Domain Knowledge Density (Score: 9/10)

| Dimension | Evidence |
|-----------|----------|
| Frameworks | ITU IMT-2030 KPIs with numeric targets, frequency regime ladder, 6G technology stack mental model |
| Quantified Metrics | Peak data rate >1 Tbps, spectral efficiency >100 bit/s/Hz, latency <0.1ms, positioning <1cm |
| Real Scenarios | Sub-THz channel modeling with ITU-R P.676, DeepMIMO dataset, CRB derivation for localization |

**Assessment:** Deep technical content with specific formulas and thresholds. Content would benefit from more example calculations.

---

## 3. Workflow Actionability (Score: 6/10)

| Phase | Assessment |
|-------|------------|
| Discovery & Assessment | Generic activities - not specific to 6G research |
| Analysis & Strategy | Generic root cause analysis, option generation |
| Implementation & Execution | Generic planning/tracking |
| Review & Optimization | Generic outcome evaluation |

**Issue:** Workflow is a generic template applied without adaptation to the 6G domain. Should include specific 6G research phases (channel measurement, simulation validation, prototype testing).

---

## 4. Risk Documentation (Score: 7/10)

| Risk | Severity | Quality |
|------|----------|---------|
| THz hardware immaturity | 🔴 Critical | Good mitigation (hardware impairment models) |
| Near-field model invalidation | 🔴 Critical | Good mitigation (spherical wavefront) |
| Molecular absorption blind spot | 🟡 High | Good with ITU-R P.676 reference |
| AI channel estimator generalization | 🟡 High | Domain-specific mitigation |
| Semantic comms security vulnerability | 🟡 High | Specific mitigation |
| IMT-2030 timeline overconfidence | 🟢 Medium | Good framing guidance |

**Strengths:** Domain-specific risks with severity ratings. Missing escalation triggers for each risk.

---

## 5. Example Quality (Score: 6/10)

| Scenario | Assessment |
|----------|------------|
| Scenario 1-4 | Generic consulting patterns with no 6G-specific content |

**Issue:** All scenarios are generic "consulting" templates with no actual 6G technical content. Should include specific examples like "design OTFS for V2X at 300 GHz" or "validate holographic MIMO channel model".

---

## 6. Metadata Completeness (Score: 8/10)

| Field | Status |
|-------|--------|
| name | ✓ present |
| description | ✓ present (263 chars - at limit) |
| author | ✓ present |
| version | ✓ present (3.0.0) |
| difficulty | ✓ expert |
| category | ✓ telecom |
| tags | ✓ 8 tags |
| platforms | ✗ missing |
| license | ✓ MIT |

**Missing:** Platform installation guide (§5).

---

## Weighted Score Calculation

```
Score = (System Prompt × 0.20) + (Domain Knowledge × 0.25) + (Workflow × 0.15)
      + (Risk Docs × 0.10) + (Examples × 0.20) + (Metadata × 0.10)

Score = (9×0.20) + (9×0.25) + (6×0.15) + (7×0.10) + (6×0.20) + (8×0.10)
      = 1.8 + 2.25 + 0.9 + 0.7 + 1.2 + 0.8 = 7.65 → 7.7 Expert
```

---

## Critical Issues

1. **🔴 Generic Workflow** - The §8 workflow uses a generic consulting template not adapted for 6G research. This reduces actionability.
2. **🔴 Generic Examples** - §9 scenarios are filler content without actual 6G technical content.
3. **🟡 Missing Platform Support** - §5 Platform Support section absent (only header present).

---

## Recommendations

| Priority | Action | Impact |
|----------|--------|--------|
| **HIGH** | Replace generic §8 workflow with 6G-specific phases: (1) Requirements/KPI Analysis, (2) Channel Modeling, (3) Algorithm Design, (4) Simulation, (5) Prototype | +1.5 pts |
| **HIGH** | Add 2+ domain-specific examples in §9: OTFS waveform design, RIS phase optimization, CRB derivation | +1.0 pt |
| **MEDIUM** | Add platform installation for all 7 platforms | +0.5 pt |

---

## Summary

| Dimension | Score | Tier |
|-----------|-------|------|
| System Prompt Depth | 9/10 | Exemplary |
| Domain Knowledge | 9/10 | Exemplary |
| Workflow Actionability | 6/10 | Community |
| Risk Documentation | 7/10 | Expert |
| Example Quality | 6/10 | Community |
| Metadata | 8/10 | Expert |
| **Weighted** | **7.7/10** | **Expert ⭐** |

**Self-Score from SKILL.md:** 7.8/10 (accurate)  
**Variance:** -0.1 (consistent)
