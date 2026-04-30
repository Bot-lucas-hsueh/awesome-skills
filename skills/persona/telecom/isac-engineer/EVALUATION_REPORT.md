# Skill Evaluation Report: isac-engineer

**Evaluation Date:** 2026-03-24  
**Evaluator:** skill-writer methodology  
**Quality Tier:** Expert ⭐ (7.6/10)

---

## 1. System Prompt Depth (Score: 9/10)

| Criterion | Assessment |
|-----------|------------|
| Role Definition | Principal ISAC Systems Engineer with 10+ years, specific publications, USRP prototyping |
| Decision Framework | 5 gates: Function Priority, Waveform AF, Interference Isolation, CRB Verification, Regulatory Compliance |
| Thinking Patterns | 5 patterns: CRB-first, Ambiguity Function, Pareto Trade-off, Interference Budget, Prototype Realism |
| Communication Style | Lead with Pareto trade-off analysis, MATLAB/Python code, cites 3GPP TS 38.305, IEEE 802.11bf |

**Strengths:** Excellent CRB-focused reasoning; concrete SINR-SCNR trade-off framework; regulatory references specific.

---

## 2. Domain Knowledge Density (Score: 9/10)

| Dimension | Evidence |
|-----------|----------|
| Frameworks | SINR vs SCNR Pareto front, CRB for AoA/range/velocity, OFDM/OTFS ambiguity function |
| Quantified Metrics | Range resolution c/2B, velocity resolution λ/2T, SI cancellation 40+30+20 dB stages |
| Real Scenarios | Self-interference floor, OFDM radar false alarms, PAPR-induced distortion |

**Assessment:** Deep ISAC-specific frameworks with numeric thresholds. Excellent domain depth.

---

## 3. Workflow Actionability (Score: 6/10)

| Phase | Assessment |
|-------|------------|
| Discovery & Assessment | Generic activities |
| Analysis & Strategy | Generic root cause analysis |
| Implementation & Execution | Generic planning/tracking |
| Review & Optimization | Generic outcome evaluation |

**Issue:** Generic template not adapted to ISAC system design workflow. Should include: waveform selection, beamforming optimization, CRB validation phases.

---

## 4. Risk Documentation (Score: 8/10)

| Risk | Severity | Quality |
|------|----------|---------|
| Sensing-communication SINR degradation | 🔴 Critical | Good - Pareto optimization guidance |
| Self-interference floor in DFRC | 🔴 Critical | Excellent - 3-stage SI cancellation |
| False alarm in OFDM radar | 🟡 High | Good - windowing/CFAR solution |
| PAPR-induced PA distortion | 🟡 High | Good - PAPR reduction techniques |
| Regulatory spectrum emission mask | 🟡 High | Good - FCC/ITU compliance |
| Target RCS variability | 🟢 Medium | Good - CFAR adaptation |

**Strengths:** ISAC-specific risks with concrete mitigation thresholds.

---

## 5. Example Quality (Score: 6/10)

| Scenario | Assessment |
|----------|------------|
| Scenario 1-4 | Generic consulting patterns |

**Issue:** No actual ISAC technical examples (waveform design, beamforming optimization, CRB calculation).

---

## 6. Metadata Completeness (Score: 7/10)

| Field | Status |
|-------|--------|
| name | ✓ present |
| description | ✓ present (262 chars) |
| author | ✓ present |
| version | ✓ present |
| difficulty | ✓ expert |
| category | ✓ telecom |
| tags | ✓ 8 tags |
| platforms | ✗ missing |
| license | ✓ MIT |

---

## Weighted Score Calculation

```
Score = (9×0.20) + (9×0.25) + (6×0.15) + (8×0.10) + (6×0.20) + (7×0.10)
      = 1.8 + 2.25 + 0.9 + 0.8 + 1.2 + 0.7 = 7.65 → 7.6 Expert
```

---

## Critical Issues

1. 🔴 Generic Workflow - Not adapted to ISAC design process
2. 🔴 Generic Examples - No ISAC-specific technical content
3. 🟡 Missing Platform Support

---

## Recommendations

| Priority | Action |
|----------|--------|
| HIGH | Replace §8 with ISAC-specific phases: (1) Waveform Selection, (2) Beamforming Design, (3) CRB Validation, (4) Hardware Prototype |
| HIGH | Add ISAC-specific examples: OFDM-ISAC waveform design, Pareto front calculation |
| MEDIUM | Add §5 Platform Support |

---

## Summary

| Dimension | Score | Tier |
|-----------|-------|------|
| System Prompt | 9/10 | Exemplary |
| Domain Knowledge | 9/10 | Exemplary |
| Workflow | 6/10 | Community |
| Risk Docs | 8/10 | Expert |
| Examples | 6/10 | Community |
| Metadata | 7/10 | Expert |
| **Weighted** | **7.6/10** | **Expert ⭐** |
