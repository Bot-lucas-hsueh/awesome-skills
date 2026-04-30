# Skill Evaluation Report: motion-control-engineer

**Evaluation Date:** 2026-03-24  
**Evaluator:** skill-writer methodology  
**Quality Tier:** Expert ⭐ (7.9/10)

---

## 1. System Prompt Depth (Score: 9/10)

| Criterion | Assessment |
|-----------|------------|
| Role Definition | Senior Robot Motion Control Engineer with 12+ years, real-time systems expertise |
| Decision Framework | 5-gate: Stability, Safety, Real-time, Performance, Tuning Path |
| Thinking Patterns | 5 patterns: Cascade separation, Model plant first, Gravity comp mandatory, MPC horizon, Safety hardcoded |
| Communication Style | Transfer functions, Bode plots, C++ code, SI units |

**Strengths:** Excellent cascade control architecture; specific PREEMPT_RT, EtherCAT references.

---

## 2. Domain Knowledge Density (Score: 9/10)

| Dimension | Evidence |
|-----------|----------|
| Frameworks | Cascade control architecture, damped least squares IK, MPC with CasADi/Acados |
| Quantified Metrics | < 1ms control loops, > 6dB/45° gain/phase margin |
| Real Scenarios | FOC for PMSM/BLDC, ros2_control interfaces |

---

## 3. Workflow Actionability (Score: 6/10)

| Phase | Assessment |
|-------|------------|
| All phases | Generic template |

**Issue:** Generic workflow not adapted to motion control engineering.

---

## 4. Risk Documentation (Score: 8/10)

| Risk | Severity | Quality |
|------|----------|---------|
| Controller Instability | 🔴 Critical | Excellent - gain/phase margin |
| Real-Time Deadline Miss | 🔴 Critical | Excellent - PREEMPT_RT, cyclictest |
| Singularity Approach | 🔴 Critical | Excellent - DLS with damping |
| Integrator Windup | 🟡 Warning | Good |
| Torque Sensor Offset | 🟡 Warning | Good |

---

## 5. Example Quality (Score: 6/10)

| Scenario | Assessment |
|----------|------------|
| All scenarios | Generic patterns |

**Missing:** No motion control-specific examples (PID tuning, MPC setup, IK solving).

---

## 6. Metadata Completeness (Score: 8/10)

| Field | Status |
|-------|--------|
| name | ✓ present |
| description | ✓ present |
| author | ✓ present |
| version | ✓ present |
| difficulty | ✓ expert |
| category | ✓ robotics |
| tags | ✓ 7 tags |
| platforms | ✗ missing |
| license | ✓ MIT |

---

## Weighted Score Calculation

```
Score = (9×0.20) + (9×0.25) + (6×0.15) + (8×0.10) + (6×0.20) + (8×0.10)
      = 1.8 + 2.25 + 0.9 + 0.8 + 1.2 + 0.8 = 7.75 → 7.8 Expert
```

---

## Summary

| Dimension | Score | Tier |
|-----------|-------|------|
| System Prompt | 9/10 | Exemplary |
| Domain Knowledge | 9/10 | Exemplary |
| Workflow | 6/10 | Community |
| Risk Docs | 8/10 | Expert |
| Examples | 6/10 | Community |
| Metadata | 8/10 | Expert |
| **Weighted** | **7.8/10** | **Expert ⭐** |

**Self-Score:** 8.0/10 (accurate)
