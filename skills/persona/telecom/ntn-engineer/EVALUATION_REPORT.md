# Skill Evaluation Report: ntn-engineer

**Evaluation Date:** 2026-03-24  
**Evaluator:** skill-writer methodology  
**Quality Tier:** Expert ⭐ (7.9/10)

---

## 1. System Prompt Depth (Score: 9/10)

| Criterion | Assessment |
|-----------|------------|
| Role Definition | Principal NTN engineer with 15+ years, 3GPP Rel-17/18 expertise, specific satellite platforms |
| Decision Framework | 5-gate decision tree: Latency, Coverage, Data rate, Terminal type, Regulatory |
| Thinking Patterns | 5 patterns: Doppler pre-compensation, Timing advance, HARQ extension, Rain fade, Link budget |
| Communication Style | Quantitative with specific formulas, cites 3GPP TR 38.811, TS 38.821 |

**Strengths:** Excellent NTN-specific decision framework with numeric thresholds for each platform.

---

## 2. Domain Knowledge Density (Score: 9/10)

| Dimension | Evidence |
|-----------|----------|
| Frameworks | 5-gate NTN platform selection, HARQ RTT extension logic, TCP BDP calculation |
| Quantified Metrics | FSPL formulas, Doppler shift calculation, TA = 2×h/c, HARQ process count formula |
| Real Scenarios | LEO 600 km Ka-band link budget, GEO TCP throughput analysis |

**Assessment:** Deep NTN-specific knowledge with concrete calculations.

---

## 3. Workflow Actionability (Score: 6/10)

| Phase | Assessment |
|-------|------------|
| Discovery & Assessment | Generic |
| Analysis & Strategy | Generic |
| Implementation & Execution | Generic |
| Review & Optimization | Generic |

**Issue:** Generic template not adapted to NTN engineering workflow. Note: Contains code snippets (Phase 1-3) but these reference external files.

---

## 4. Risk Documentation (Score: 8/10)

| Risk | Severity | Quality |
|------|----------|---------|
| Doppler-Induced Demodulation Failure | 🔴 Critical | Excellent - specific kHz values |
| Timing Advance Overflow | 🔴 Critical | Good - 3GPP extended TA |
| HARQ Retransmission Timeout | 🔴 Critical | Excellent - Rel-17 solution |
| Rain Fade Outage | 🟡 High | Good - ACM fallback |
| Spectrum Interference | 🟡 High | Good - ITU Epfd compliance |

---

## 5. Example Quality (Score: 7/10)

| Scenario | Assessment |
|----------|------------|
| Scenarios 1-4 | Generic consulting patterns |
| Anti-Patterns (§) | Excellent - 5 specific NTN anti-patterns with code |

**Assessment:** Anti-pattern section is excellent domain-specific content. Main scenarios generic.

---

## 6. Metadata Completeness (Score: 8/10)

| Field | Status |
|-------|--------|
| name | ✓ present |
| description | ✓ present |
| author | ✓ present |
| version | ✓ present |
| difficulty | ✓ expert |
| category | ✓ telecom |
| tags | ✓ 12 tags |
| platforms | ✗ missing |
| license | ✓ MIT |

---

## Weighted Score Calculation

```
Score = (9×0.20) + (9×0.25) + (6×0.15) + (8×0.10) + (7×0.20) + (8×0.10)
      = 1.8 + 2.25 + 0.9 + 0.8 + 1.4 + 0.8 = 7.95 → 7.9 Expert
```

---

## Summary

| Dimension | Score | Tier |
|-----------|-------|------|
| System Prompt | 9/10 | Exemplary |
| Domain Knowledge | 9/10 | Exemplary |
| Workflow | 6/10 | Community |
| Risk Docs | 8/10 | Expert |
| Examples | 7/10 | Expert |
| Metadata | 8/10 | Expert |
| **Weighted** | **7.9/10** | **Expert ⭐** |
