# EVALUATION_REPORT.md — Patent Attorney Skill

**Skill:** Patent Attorney  
**File:** skills/legal/patent-attorney/SKILL.md  
**Current Score:** 8.3/10  
**Evaluator:** skill-writer  
**Date:** 2026-03-24

---

## 6-Dimension Quality Rubric

### Dimension 1: Prompt Quality (System Prompt)

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| Clarity of role definition | 9 | 15+ years, technical degree + JD, thousands of patents |
| Decision framework present | 7 | Generic 4-gate framework, not patent-specific |
| Thinking patterns actionable | 8 | First-principles, pattern matching, but generic |
| Communication style specified | 8 | Clear disclaimers, professional tone |

**Dimension 1 Total:** 8.0/10 (weighted 20%)

---

### Dimension 2: Domain Expertise

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| Depth of patent law knowledge | 10 | §101, §102, §103, Alice/Mayo, IPR detailed |
| Jurisdiction awareness | 9 | USPTO, EPO, PCT covered |
| Industry tools referenced | 9 | USPTO, Espacenet, WIPO, Anaqua, PTAB |
| Practical workflows | 8 | Patentability + office action, but high-level |

**Dimension 2 Total:** 9.0/10 (weighted 25%)

---

### Dimension 3: Workflow Clarity

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| Task breakdowns clear | 8 | Phase 1 (5 steps), Phase 2 (5 steps) |
| Deliverables specified | 8 | Claim charts, responses, filing strategy |
| Examples show workflow | 7 | Generic scenarios not patent-specific |

**Dimension 3 Total:** 7.75/10 (weighted 15%)

---

### Dimension 4: Risk Documentation

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| Legal disclaimer present | 10 | Clear comprehensive disclaimer |
| Risk matrix detailed | 9 | 6 risks with severity |
| Mitigation strategies | 9 | Practical for each risk |

**Dimension 4 Total:** 9.33/10 (weighted 10%)

---

### Dimension 5: Scenario Examples

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| Examples are concrete | 7 | Generic template scenarios |
| Real-world application | 8 | Claim strength matrix, deadlines table |
| Trigger relevance | 7 | Scenarios use generic "problem" placeholders |

**Dimension 5 Total:** 7.33/10 (weighted 20%)

---

### Dimension 6: Metadata & Structure

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| YAML valid | 9 | Clean YAML |
| Description concise | 9 | 251 chars, good triggers |
| Tags appropriate | 10 | Comprehensive patent tags |
| Version tracking | 9 | Version 3.0.0 |

**Dimension 6 Total:** 9.25/10 (metadata weighted 10%)

---

## Overall Score Calculation

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| Prompt Quality | 20% | 8.00 | 1.60 |
| Domain Expertise | 25% | 9.00 | 2.25 |
| Workflow Clarity | 15% | 7.75 | 1.16 |
| Risk Documentation | 10% | 9.33 | 0.93 |
| Scenario Examples | 20% | 7.33 | 1.47 |
| Metadata & Structure | 10% | 9.25 | 0.93 |
| **TOTAL** | 100% | — | **8.34/10** |

---

## Tier Classification

**Current Tier:** Expert ⭐ (declared 8.3/10)  
**Evaluated Tier:** Expert ⭐ (8.34/10)

---

## Findings

### Strengths
1. Excellent patent-specific frameworks (Alice/Mayo, claim strength matrix)
2. Comprehensive patent law coverage (§101-103, IPR, prosecution)
3. Good tool references (USPTO, Espacenet, PTAB)
4. Detailed deadline table with statutory references

### Issues to Address
1. **Generic decision framework** — Gates 1-4 are generic, should be patent-specific
2. **Generic §9 scenarios** — Use placeholders like "[problem]" instead of concrete patent scenarios
3. **Sections 16-21** — Generic filler content, not patent-specific
4. **Missing concrete examples** — No actual claim chart, office action response example

### Recommendations for Upgrade
1. Replace generic decision framework with patent-specific gates:
   - Gate: Is this patentable subject matter under §101?
   - Gate: Does prior art create §102/§103 issues?
   - Gate: Is this within prosecution timeline?
2. Replace §9 scenarios with patent-specific examples:
   - Example: Alice rejection response strategy
   - Example: IPR vulnerability assessment
   - Example: PCT national phase deadline tracking
3. Remove sections 16-21 (generic content)
4. Add claim chart template to §7

---

## Decision

**Action:** MINOR UPDATE (add patent-specific frameworks, trim generic content)  
**Priority:** Medium  
**Estimated Token Savings:** ~200 tokens
