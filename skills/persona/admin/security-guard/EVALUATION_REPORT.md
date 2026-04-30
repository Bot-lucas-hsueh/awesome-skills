# Evaluation Report — security-guard

## Skill Summary
| Field | Value |
|-------|-------|
| **Name** | security-guard |
| **Version** | 1.0.0 |
| **Quality Tier** | Expert ⭐ |
| **Rubric Score** | 7.7/10 |
| **Line Count** | 653 |

---

## 6-Dimension Rubric Scores

| Dimension | Score | Weight | Weighted | Tier |
|-----------|-------|--------|----------|------|
| System Prompt Depth | 7.5 | 20% | 1.50 | Expert |
| Domain Knowledge Density | 7.5 | 25% | 1.875 | Expert |
| Workflow Actionability | 7.5 | 15% | 1.125 | Expert |
| Risk Documentation | 8.5 | 10% | 0.85 | Expert |
| Example Quality | 7.5 | 20% | 1.50 | Expert |
| Metadata Completeness | 7.5 | 10% | 0.75 | Expert |

---

## Strengths

### §1 System Prompt — Specific & Actionable
- Quantified identity ($100M+ facilities, 500+ incidents)
- Layered defense philosophy
- Core Expertise covering 6 domains (access control, patrol, surveillance, emergency, loss prevention, physical security)
- Threat modeling thinking pattern ("assume hostile intent")
- Chain of custody and de-escalation mindset
- **Verdict**: Expert-level

### §3 Risk Documentation — Strong
- 7 risks (5 🔴 High, 2 🟡 Medium)
- Dollar impacts: "$100K+ settlements"
- Specific mitigations with quantified outcomes (e.g., mantrap cost $15-25K per door)
- Reference to ASIS International and SIA guidelines
- Physical intervention disclaimer

### §7 Standards & Reference
- 4 security frameworks (TVA, Physical Security Survey, Incident Response, Visitor Management)
- Metrics with targets (response time <5 min, video retrieval <10 min)

### §8 Workflow
- Access Control Incident (3 phases with Done/Fail criteria)
- Active Threat Emergency Response (4 steps)
- Detailed with specific actions

### §9 Examples
- §9.1: Tailgating prevention with anti-tailgating solutions (mantrap/turnstile/vestibule) with costs
- §9.2: Video evidence collection with chain of custody protocol
- Both have specific system recommendations and "Next, I need from you" items

### §10 Integration
- Security-specific cross-skill combinations (Warehouse, Admin, HR)
- Meaningful, not generic

---

## Weaknesses

### ❌ Line Count Over Budget (Severity: High)
- **653 lines** — exceeds 500-line limit by 153 lines

### ❌ Missing §5 Platform Support
- No platform installation section

### ❌ Duplicate Boilerplate Sections (Severity: High)
- §16-21 boilerplate (estimated ~150 lines)

### ❌ Duplicate Generic Scenarios (§9 lines 372-469)
- Same 4 generic templates

### ❌ Duplicate §5 Professional Toolkit
- §5 and §6 both present (lines 195-206 and 208 onward)

### ❌ Anti-Pattern: Chinese Character in English Text
- §3 line 155: `Inadequate lighting` row contains `夜间巡逻audit` — mixed Chinese character in English table
- Violates format rule (English primary)

### ❌ Non-Standard Metadata
- 10-field block instead of standard 9-field

---

## Anti-Patterns Detected

| # | Anti-Pattern | Severity | Location |
|---|-------------|----------|----------|
| #4 | Token Waste — 653 lines (limit 500) | 🔴 High | Entire file |
| #4 | Token Waste — boilerplate + generic scenarios | 🔴 High | §16-21, §9 |
| #7 | Literal Translation — `夜间巡逻audit` in English table | 🟢 Low | §3 line 155 |
| #9 | Platform Coverage Miss | 🔴 High | Missing section |
| — | Non-standard metadata | 🟡 Medium | Lines 8-17 |

---

## Token Budget Analysis

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| SKILL.md lines | 653 | ≤500 | ❌ Over by 153 lines |
| Post-cleanup estimate | ~500 lines | ≤500 | ✅ At target |

---

## Recommendation

**Tier: Expert ⭐** (7.7/10)

Good domain-specific content with quantified security scenarios. Risk documentation is strong with dollar impacts. Primary issue is token bloat from boilerplate and generic scenarios. Fix the Chinese character in English text as well.

**Immediate actions required:**
1. Strip boilerplate (§16-21), generic scenarios, duplicate §6
2. Add §5 Platform Support
3. Fix `夜间巡逻audit` → `night patrol audit`
4. Fix metadata

After cleanup: Estimated score → 8.2/10 Expert ⭐
