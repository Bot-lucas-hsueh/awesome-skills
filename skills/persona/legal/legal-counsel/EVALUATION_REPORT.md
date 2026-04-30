# EVALUATION_REPORT.md — Legal Counsel Skill

**Skill:** Legal Counsel  
**File:** skills/legal/legal-counsel/SKILL.md  
**Current Score:** 8.2/10  
**Evaluator:** skill-writer  
**Date:** 2026-03-24

---

## 6-Dimension Quality Rubric

### Dimension 1: Prompt Quality (System Prompt)

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| Clarity of role definition | 9 | GC for Fortune 500, startup to IPO, clear identity |
| Decision framework present | 8 | IRAC structure, but not domain-specific gates |
| Thinking patterns actionable | 8 | IRAC, but generic thinking patterns |
| Communication style specified | 9 | Professional, defines terms, cites cases |

**Dimension 1 Total:** 8.5/10 (weighted 20%)

---

### Dimension 2: Domain Expertise

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| Depth of legal knowledge | 9 | Contracts, compliance, employment, IP, M&A, litigation |
| Jurisdiction awareness | 9 | US federal, CA/NY/DE/TX, EU/UK |
| Industry tools referenced | 9 | Westlaw, Lexis, CLM platforms, eCFR |
| Practical workflows | 8 | IRAC workflow, but less detailed than specialized skills |

**Dimension 2 Total:** 8.75/10 (weighted 25%)

---

### Dimension 3: Workflow Clarity

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| Task breakdowns clear | 8 | 5-step analysis, 5-step review |
| Deliverables specified | 8 | Redlines, risk matrices, recommendations |
| Examples show workflow | 7 | Generic template scenarios |

**Dimension 3 Total:** 7.75/10 (weighted 15%)

---

### Dimension 4: Risk Documentation

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| Legal disclaimer present | 10 | Comprehensive disclaimer |
| Risk matrix detailed | 9 | 6 risks with severity |
| Mitigation strategies | 9 | Practical for each |

**Dimension 4 Total:** 9.33/10 (weighted 10%)

---

### Dimension 5: Scenario Examples

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| Examples are concrete | 7 | Generic template scenarios |
| Real-world application | 8 | Contract review checklist practical |
| Trigger relevance | 7 | Scenarios use "[problem]" placeholders |

**Dimension 5 Total:** 7.33/10 (weighted 20%)

---

### Dimension 6: Metadata & Structure

| Criterion | Score (1-10) | Notes |
|-----------|--------------|-------|
| YAML valid | 9 | Clean YAML |
| Description concise | 9 | 243 chars |
| Tags appropriate | 9 | Appropriate tags |
| Version tracking | 9 | Version 3.0.0 |

**Dimension 6 Total:** 9.0/10 (metadata weighted 10%)

---

## Overall Score Calculation

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| Prompt Quality | 20% | 8.50 | 1.70 |
| Domain Expertise | 25% | 8.75 | 2.19 |
| Workflow Clarity | 15% | 7.75 | 1.16 |
| Risk Documentation | 10% | 9.33 | 0.93 |
| Scenario Examples | 20% | 7.33 | 1.47 |
| Metadata & Structure | 10% | 9.00 | 0.90 |
| **TOTAL** | 100% | — | **8.35/10** |

---

## Tier Classification

**Current Tier:** Expert ⭐ (declared 8.2/10)  
**Evaluated Tier:** Expert ⭐ (8.35/10)

---

## Findings

### Strengths
1. IRAC methodology for legal analysis
2. Comprehensive legal domain coverage (contracts, compliance, employment, IP, M&A)
3. Contract review checklist practical
4. Good tool references

### Issues to Address
1. **Generic §9 scenarios** — Use placeholder "[problem]" instead of concrete legal scenarios
2. **Sections 16-21** — Generic filler content not specific to legal counsel
3. **Decision framework** — Not as domain-specific as specialized skills (contract-lawyer, litigation-lawyer)
4. **Lower version** — Version 3.0.0 vs. 5.0.0 for specialized skills

### Recommendations for Upgrade
1. Replace §9 scenarios with 3 concrete legal-counsel examples:
   - Example: Contract negotiation strategy
   - Example: Regulatory investigation response
   - Example: Board memorandum on acquisition
2. Remove sections 16-21 (generic filler, ~100 lines)
3. Update version to 4.0.0

---

## Decision

**Action:** MINOR UPDATE (replace scenarios, trim generic content)  
**Priority:** Medium  
**Estimated Token Savings:** ~150 tokens
