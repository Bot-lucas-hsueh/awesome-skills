
# Skill Improvement Plan

> **Created:** 2026-03-01 | **Updated:** 2026-03-18 | **Branch:** `claude/skill-evaluation-improvements-aXOj0`
> **Goal:** Raise all 587 skills to ≥9.5/10 (Exemplary v3.0) — standardized § format, full 16-section structure, correct install URLs

---

## 1. Current State Assessment

### 1.1 Portfolio Overview

| Metric | Value |
|--------|-------|
| **Total skills** | 587 |
| **Total categories** | 56 |
| **Largest category** | tools (115 skills) |
| **With references/ architecture** | 165 skills |

### 1.2 Version Distribution

| Version | Count | Quality | Status |
|---------|-------|---------|--------|
| v3.0.0 with § heading format | 87 | Exemplary — full 16 sections, rich toolkit tables | ✅ Done |
| v3.0.0 with old `N.` heading format | 280 | Exemplary — full content, old headings | ⚠️ Heading fix needed |
| v2.0.0 | 98 | Exemplary — full sections, broken install URLs | 🔴 URL fix + upgrade needed |
| v1.0.0 | 121 | Mixed — 5–6 stub sections only | 🔴 Full rewrite needed |
| Other/malformed | 1 | — | 🔴 Fix needed |
| **Total needing work** | **500** | — | — |

### 1.3 Quality Tier Distribution

| Tier | Count | Description |
|------|-------|-------------|
| ✅ Exemplary v3.0 (§ format, correct URLs) | 87 | Fully compliant — ready to ship |
| ⚠️ Exemplary v3.0 (old N. headings) | 280 | Content good, heading format inconsistent |
| 🔴 Exemplary v2.0 (broken install URLs) | 98 | Install commands broken — URL path mismatch |
| 🔴 Basic v1.0 (stub format) | 121 | Only 5–6 sections; missing system prompt, scenarios, pitfalls |
| **Total requiring changes** | **499** | |

---

## 2. Critical Bugs Found

### Bug #1 — URL Path Mismatch in v2.0 Skills (98 skills) 🔴 HIGH

**Problem:** All 98 v2.0 skills reference install URLs like:
```
https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/admin/driver.md
```
But the actual file path is a directory:
```
skills/admin/driver/SKILL.md   ← directory + SKILL.md
```
The flat `.md` URL does not exist. All install commands (OpenCode, OpenClaw, Claude Code, Kimi) fail silently.

**Impact:** 98 skills are uninstallable via copy-paste instructions.

**Fix required:** Update every Platform Support URL to:
```
https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/admin/driver/SKILL.md
```

**Affected categories:** admin (9), transport-worker (7), repair-worker (3), factory-worker (4), construction-worker (9), service-worker (13), farmer (3), hospitality (2), retail (2), international (1), and more.

---

### Bug #2 — Section Heading Format Inconsistency (461 skills) ⚠️ MEDIUM

**Problem:** Two heading formats coexist project-wide:
- **New standard** (v3.0+): `## § 1 · System Prompt` — 87 skills use this
- **Old format** (v2.0/v3.0): `## 1. System Prompt` — 461 skills use this

The § format is the established project standard (all reference skills, mobile-repair-technician exemplar). Old format should be phased out.

**Fix required:** Migrate all 461 old-format skills to § format during their next content upgrade round.

---

### Bug #3 — v1.0 Tools Skills Are Stubs (121 skills) 🔴 HIGH

**Problem:** All 121 v1.0 skills (115 in `tools/`, 6 in `special/`) have only 5–6 sections:
```
1. What This Skill Does  — 3 bullet points
2. Core Concepts         — basic pricing/config table
3. Platform Support      — URL only, no 7-platform install table
4. Standards & Reference — one code snippet
5-16. Metadata           — "MIT License" one-liner
```

Missing entirely: System Prompt, Risk Disclaimer, Core Philosophy, Decision Framework, Workflow, Scenario Examples, Common Pitfalls, Integration, Scope & Limitations, Quality Verification, Version History.

**Impact:** These skills provide no actionable AI persona — they are reference cards, not skill prompts.

---

### Bug #4 — YAML `quality` Field Missing on Some v1.0 Skills ⚠️ LOW

**Problem:** ~6 v1.0 skills in `special/` have no `quality:` YAML field (e.g., `gerrit-permission-manager`). Metadata tooling that reads this field will error or silently skip them.

**Fix:** Add `quality: basic` to all v1.0 skills that lack the field.

---

### Bug #5 — Score Badge Inflation on v2.0 Skills 🟡 MEDIUM

**Problem:** 98 v2.0 skills carry `Score-9.5/10-brightgreen` badges but are missing:
- Category column in Professional Toolkit table
- Detailed Thinking Patterns in System Prompt (§ 1.2)
- Full 3-flow scenario examples
- Correct install URLs (Bug #1 above)

These do not genuinely meet the 16-point quality gate. The self-reported score overstates actual quality.

**Fix:** Either upgrade content to genuinely meet 9.5/10 or temporarily downgrade badge to `Score-7.5/10-yellow` until upgraded.

---

## 3. Scoring Rubric

### 3.1 Scoring Formula

```
Score = SP×0.20 + DK×0.25 + WA×0.15 + RD×0.10 + EQ×0.20 + MC×0.10

SP = System Prompt Depth      (20%) — role identity, decision framework, thinking patterns, comms style
DK = Domain Knowledge Density (25%) — specific frameworks, metrics with formulas, tool selection guides
WA = Workflow Actionability   (15%) — 3+ phases, [✓/✗] gates, templates
RD = Risk Documentation       (10%) — 5+ domain-specific risks with severity + mitigation
EQ = Example Quality          (20%) — 3+ full conversation flows with domain artifacts
MC = Metadata Completeness    (10%) — 9 YAML fields, version history, license
```

### 3.2 Version → Score Mapping

| Version | Format | Typical Score | Gap to 9.5/10 |
|---------|--------|--------------|----------------|
| v3.0.0 § format | § N · headings, Category toolkit column, correct URLs | 9.5/10 ✅ | None |
| v3.0.0 N. format | Old headings, content otherwise complete | ~8.5/10 | Minor: heading + toolkit polish |
| v2.0.0 | Old headings, broken URLs, simpler toolkit | ~7.0/10 | Moderate: URL fix + content depth |
| v1.0.0 | Stub (5–6 sections) | ~2.0/10 | Major: full 16-section rewrite |

### 3.3 Required 16-Section Structure (v3.0 Standard)

Every 9.5/10 skill MUST include ALL 16 sections in § format:

| # | Section | Min Requirement |
|---|---------|----------------|
| § 1 | System Prompt | Role identity + Decision Framework (5+ gate questions) + Thinking Patterns (4+ dimensions) + Communication Style |
| § 2 | What This Skill Does | 4+ specific, measurable capabilities |
| § 3 | Risk Disclaimer | 5+ domain-specific risks with severity emoji + mitigation |
| § 4 | Core Philosophy | Mental model / ASCII diagram + 3+ guiding principles |
| § 5 | Platform Support | Full 7-platform install table + correct SKILL.md URL |
| § 6 | Professional Toolkit | 8+ tools with **Category** column + purpose + when-to-use |
| § 7 | Standards & Reference | Domain frameworks + decision trees + metrics with target ranges |
| § 8 | Standard Workflow | 3+ phases with [✓ Done] and [✗ FAIL] criteria + templates |
| § 9 | Scenario Examples | 3+ full conversation flows including edge cases + artifacts |
| § 10 | Common Pitfalls | 5+ named anti-patterns with ❌ BAD / ✅ GOOD + "why it matters" |
| § 11 | Integration with Other Skills | 3+ skill combinations with specific outcomes |
| § 12 | Scope & Limitations | 3+ "use when" + 3+ "do NOT use when" + alternatives |
| § 13 | How to Use This Skill | Quick install command + trigger word list |
| § 14 | Quality Verification | Self-checklist + 3 test cases with expected outputs |
| § 15 | Version History | 3+ entries with meaningful change descriptions |
| § 16 | License & Author | MIT License table + author attribution |

---

## 4. Per-Category Evaluation

### 4.1 Software & Tech Core — Score: 9.5/10 ✅

**Skills (10):** backend-developer, frontend-developer, devops-engineer, qa-engineer, security-engineer, software-architect, system-architect, algorithm-engineer, data-scientist, ai-ml-engineer

**Strengths:**
- Full 16 sections with § format and Category column in toolkits
- Rich code examples (actual SQL, Helm charts, CI configs)
- Decision frameworks with exact numeric thresholds
- Realistic [✓/✗] workflow gates
- 3+ full conversation scenarios with domain artifacts

**Weaknesses:** None significant — reference implementation quality.

**Improvement (minor):** Refresh 2026 toolchain references (React 19 patterns, k8s 1.32 APIs, Python 3.13 features). Bump to v3.1.0 for these updates.

---

### 4.2 AI/ML — Score: 9.5/10 ✅

**Skills (9):** ai-application-engineer, ai-product-manager, ai-safety-researcher, ai-chip-architect, ai-compute-platform-engineer, llm-research-scientist, llm-training-engineer, machine-learning-engineer, prompt-engineer

**Strengths:** Deep technical depth, cutting-edge frameworks (RLHF, Constitutional AI, MFU optimization, Roofline model), quantified metrics throughout.

**Weaknesses:** Some skills reference 2024-era models (GPT-4, LLaMA-2) that are now dated.

**Improvement:** Update benchmark references to 2026 models (GPT-4o, Claude 4, Llama 3.3, Gemini 2.0). Update MFU targets for NVIDIA Blackwell/GB200 era.

---

### 4.3 Executive & Business — Score: 9.2/10 ✅

**Skills (11):** ceo, cfo, cmo, coo, cto (all 9.5/10) + management-consultant, strategy-consultant, project-manager + community-verified: business-development-manager, hr-expert

**Strengths:** Board-level frameworks (OKR, BCG, Porter's Five Forces), M&A workflows, stakeholder communication.

**Weaknesses:** Community-verified skills (business-development-manager, hr-expert) still use old `N.` headings and lack Thinking Patterns subsection.

**Improvement:** Migrate to § format. Add AI-era strategic considerations: LLM cost as capex line item (CFO/CEO), AI talent acquisition (HR), AI product risk assessment (strategy-consultant).

---

### 4.4 Finance — Score: 9.0/10 ✅ (top 4) / 2.0/10 🔴 (15 stubs)

**Skills (19):** CPA, financial-analyst, fund-manager, investment-analyst (all 9.5/10) + 15 v1.0 stubs

**Strengths:** Top 4 have excellent quantitative depth — DCF templates, VaR formulas, ratio decision trees, GAAP/IFRS framework tables.

**Critical Gap:** 15 finance skills are v1.0 stubs with 5-section structure only. Finance is high-demand and high-stakes.

**Priority stubs to rewrite first:** quant-trader (AI application overlap), fintech-engineer (tech-adjacent), actuary (quantitative depth already has reference in statistician skill).

**Improvement:** Full 16-section rewrite for all 15 stubs. Use financial-analyst as reference implementation.

---

### 4.5 Legal — Score: 9.5/10 ✅ (top 2) / 2.0/10 🔴 (12 stubs)

**Skills (14):** legal-counsel, patent-attorney (both 9.5/10) + 12 v1.0 stubs

**Critical Gap:** 12 of 14 legal skills are stubs. Legal skills carry high-stakes risk if users misapply AI guidance.

**Specific issues:**
- `judge` and `prosecutor-assistant` require the strongest possible scope limitations in § 12 — AI must not simulate official legal decisions
- `arbitrator` needs ADR (Alternative Dispute Resolution) framework references
- All legal skills must include jurisdiction disclaimer (laws vary by country/state)

**Improvement:** Full rewrite with mandatory "not a substitute for licensed legal advice" in every § 9 scenario. Priority: paralegal, compliance-specialist (enterprise demand), corporate-legal.

---

### 4.6 Healthcare & Medical — Score: 9.5/10 ✅ (top 2) / 5.0/10 🔴 (43+ others)

**Skills (45+):** general-practitioner, psychologist (both 9.5/10) + 43 others across healthcare/ and medical/

**Strengths:** Top skills have excellent clinical reasoning (SOAP notes, Red Flag criteria, ABCDE assessment, CBT/DBT frameworks).

**Critical Gap:** 40+ healthcare skills at v1.0/v2.0 with insufficient risk documentation — this is the highest-risk domain in the entire portfolio.

**Domain-specific issues:**
- Anesthesiologist: needs airway management decision tree (RSI, difficult airway protocol)
- Radiologist: lacks ACR appropriateness criteria and Rad-Lex terminology
- Telemedicine-architect: needs HIPAA, GDPR, and data residency compliance section
- All medical skills: every § 9 scenario MUST end with "consult a licensed professional" recommendation

**Improvement:** Healthcare upgrades are highest priority after Phase 2 completion. Every skill needs mandatory clinical disclaimer hardcoded into system prompt, not just § 3.

---

### 4.7 Tools Category — Score: 2.0/10 🔴 CRITICAL

**Skills (115):** Spread across ai-ml, analytics, cad, cicd, cloud, cn-cloud, container, data-platform, database, design, engineering, engineering-simulation, enterprise, game-engine, iac, media, observability, productivity, scientific, security

**Current state:** All v1.0 (~80 lines each), stub format:
```
1. What This Skill Does  — 3 bullet points
2. Core Concepts         — pricing table or config snippet
3. Platform Support      — URL only (no 7-platform install table)
4. Standards & Reference — one code snippet
5-16. Metadata           — "MIT License" one-liner
```

**Root cause:** Tools skills were created as quick-reference cards. They need a different v3.0 upgrade approach than professional role skills.

**Recommended tools skill template (differs from professional skills):**

| Section | Tools-Specific Content |
|---------|----------------------|
| § 1 System Prompt | Tool expert identity + "when to use X vs Y" decision table |
| § 3 Risk Disclaimer | Cost overrun, vendor lock-in, security misconfig, version compatibility |
| § 6 Toolkit | Related/competing tools + integration patterns |
| § 7 Standards | Official docs URL + version compatibility matrix + config reference |
| § 8 Workflow | Install → configure → first use → production readiness |
| § 9 Scenarios | 3 common tasks with full command sequences and expected output |
| § 10 Pitfalls | 5+ wrong flags, version mismatches, common misconfigurations |
| § 12 Scope | When to use this tool vs. alternatives (e.g., "use k8s not ECS when...") |

**Priority sub-categories for Phase T1:** cicd (GitHub Actions, Jenkins, ArgoCD), database (PostgreSQL, Redis, MongoDB), container (Docker, Kubernetes, Helm), cloud (AWS, GCP, Azure core services), security (Vault, cert-manager, Snyk).

---

### 4.8 Education — Score: 7.5/10 ⚠️ (community-verified) / 2.0/10 🔴 (stubs)

**Skills (59):** university-professor, k12-teacher, private-tutor, corporate-trainer (community-verified, ~7.5/10) + 55 v1.0/v2.0 others

**Strengths:** Community-verified skills have solid pedagogical frameworks (Bloom's taxonomy, Socratic method, differentiated instruction).

**Gaps across all 59 skills:**
- Learning outcome measurement metrics (pre/post assessment, Kirkpatrick Level 1-4)
- Differentiated instruction for diverse learner needs (ELL, IEP, gifted)
- Assessment rubric templates
- Digital learning platform integration (LMS, LTI standards)

**Improvement:** Apply Bloom's taxonomy decision framework uniformly. Add UNESCO competency frameworks for international/cross-cultural education skills. Reference implementation: use corporate-trainer as base template for all adult learning skills.

---

### 4.9 Government & Public Service — Score: 4.0/10 🔴

**Skills (29):** All at v1.0 or v2.0 stub format

**Critical gaps:**
- No procedural depth for government decision workflows
- Skills reference jurisdiction-specific regulations without noting legal variation by country/region
- Missing civic ethics and public accountability frameworks
- No "AI cannot replace official government processes" scope guard

**Improvement:** All government skills need:
1. Jurisdiction disclaimer in § 1 system prompt
2. International frameworks cited (UN SDGs, OECD governance principles, ISO 37001 anti-bribery) rather than country-specific statutes
3. Strong § 12 "do NOT use when" — AI should not draft official government decisions

---

### 4.10 Cybersecurity — Score: 9.0/10 ✅

**Skills (3):** ai-security-engineer, data-security-officer, privacy-computing-engineer (all upgraded 2026-03-01)

**Strengths:** MITRE ATT&CK mapping, NIST CSF 2.0, threat modeling decision trees, Zero Trust architecture.

**Concern:** Cybersecurity content goes stale fastest of any domain. CVE references become outdated within months.

**Improvement:** Replace specific CVE lists with framework-based references (CWE categories, OWASP Top 10 methodology). Add reminder in all § 9 scenarios: "Check NVD and MITRE for current CVE/CVSSv3 scores before using in production."

---

### 4.11 Admin (Office Support) — Score: 7.0/10 ⚠️

**Skills (9):** executive-assistant (community-verified, ~7.5/10) + 8 v2.0 skills (administrative-manager, driver, security-guard, cleaning-staff, purchasing-specialist, receptionist, chef, warehouse-manager)

**Bugs present:**
- All v2.0 skills have broken install URLs (Bug #1) — uninstallable
- All use old `N.` heading format (Bug #2)
- `Score-9.5/10` badge is misleading

**Content gaps:**
- Professional Toolkit table missing Category column
- Scenario examples are 1-2 exchange stubs (vs. required 3 full flows)
- No Thinking Patterns subsection in System Prompt

**Improvement:** Fix URLs (Bug #1 critical). Expand scenarios. Add Category column to toolkits. Update score badges honestly.

---

### 4.12 Repair Workers — Score: 9.5/10 ✅ (mobile) / 8.5/10 ⚠️ (others)

**Skills (4):** mobile-repair-technician (9.5/10 ✅), auto-body-repairer (8.5/10), appliance-repairer (8.5/10), locksmith (7.5/10)

**mobile-repair-technician** is the category exemplar: § format headings, Category column, references/ architecture, full risk documentation.

**Other 3 skills** have full 16 sections with references/ but use old `N.` heading format and simpler toolkit tables.

**Improvement:**
- Migrate auto-body-repairer and appliance-repairer to § format (content is solid, just heading conversion)
- Locksmith needs stronger anti-misuse guardrails in § 12: "do NOT assist with bypassing locks on property you do not own"

---

### 4.13 Transportation & Transport Workers — Score: 8.5/10 ✅ (pilot, bus, truck) / 7.0/10 ⚠️ (v2.0 skills)

**Skills (10):** pilot, bus-driver, truck-driver (with references/, 8.5/10) + taxi-driver, flight-attendant, seaman (references/, 8.5/10) + delivery-rider (v2.0, broken URLs)

**Strengths:** Safety-critical skills have strong risk documentation. Pilot skill has excellent CRM (Crew Resource Management) framework. bus-driver, truck-driver have proper HOS (Hours of Service) regulation coverage.

**Weaknesses:**
- delivery-rider at v2.0 with broken install URL (Bug #1)
- No explicit note that traffic laws/regulations vary by country
- delivery-rider missing gig economy occupational health guidance (musculoskeletal risks, heat exposure)

**Improvement:** Fix delivery-rider URL. Add jurisdiction-agnostic regulatory note to all transport skills. Add occupational health section to gig economy skills.

---

### 4.14 Aerospace — Score: 6.5/10 ⚠️ (telecom) / 2.0/10 🔴 (most others)

**Skills (10 + 3 telecom):** Telecom skills (6g, isac, ntn) have full 16-section content with references/. All 10 core aerospace skills still Phase 2 pending.

**Priority:** HIGH — eVTOL and UAV are fastest-growing aerospace AI application areas in 2026. Urban Air Mobility regulatory frameworks (FAA AC 21-17, EASA SC VTOL) are stabilizing — good time to capture.

**Special consideration for airworthiness-certification-engineer and rocket-chief-designer:** These skills must carry ITAR/EAR export control disclaimers. Aerospace engineering data can be controlled technology.

---

### 4.15 Robotics — Score: 2.0/10 🔴

**Skills (5):** embodied-ai-researcher, robot-perception-engineer, motion-control-engineer, robot-mechanical-engineer, precision-reducer-engineer

**All Phase 2 pending.** Humanoid robotics is one of the fastest-growing AI application domains in 2026 (Figure AI, 1X, Tesla Optimus, Unitree G1).

**Key frameworks to include:** ROS2, Drake, MuJoCo for simulation; URDF/MJCF for robot description; ISO 10218 for industrial robot safety.

---

### 4.16 Automotive (Autonomous Driving) — Score: 7.5/10 ⚠️ (community-verified) / 2.0/10 🔴 (7 stubs)

**Skills (8):** autonomous-driving-engineer (community-verified, ~7.5/10) + 7 basic stubs

**Priority:** HIGH — Tesla FSD v13, Waymo 6th gen, BYD DiPilot — massive commercial developer demand.

**Key frameworks for stubs:** AUTOSAR Adaptive, Apollo 10, ROS2, OpenDRIVE/OpenSCENARIO for simulation, ISO 26262 ASIL for functional safety.

---

### 4.17 Biotech — Score: 2.0/10 🔴

**Skills (5):** ai-drug-design-scientist, brain-computer-interface-engineer, synthetic-biologist, cell-therapy-scientist, biomaterials-engineer

**All Phase 2 pending.** These skills carry the HIGHEST ethical risk in the portfolio alongside healthcare.

**Critical requirements:**
- BCI and cell-therapy skills: "Not a substitute for clinical trial protocol review" in every scenario
- Synthetic biologist: Must include biosafety level (BSL) guidance and dual-use research of concern (DURC) awareness
- All biotech skills: Reference GMP, GLP, GCP regulatory frameworks

---

### 4.18 Quantum Computing — Score: 2.0/10 🔴

**Skills (4):** quantum-algorithm-engineer, quantum-communication-engineer, quantum-physicist, quantum-sensor-researcher

**All Phase 2 pending.** Rapidly evolving field — 2026 context: IBM Heron, Google Willow, IonQ Forte achieving error-corrected logical qubits. Skills must reflect current NISQ-to-fault-tolerant transition era.

---

### 4.19 Semiconductor & Materials — Score: 2.0/10 🔴

**Skills (5 semiconductor + 4 materials):** chip-design-engineer, wide-bandgap-semiconductor-engineer, nanomaterials-engineer, composite-materials-engineer, superconducting-materials-researcher

**All Phase 2 pending.** High commercial demand post-CHIPS Act (US), EU Chips Act. chip-design-engineer should reference current EDA tools (Cadence, Synopsys, open-source: OpenROAD, Magic VLSI).

---

### 4.20 Creative & Media — Score: 7.5/10 ⚠️

**Skills (23):** graphic-designer, translator (community-verified, ~7.5/10) + 21 others at v2.0/v1.0

**Strengths:** Design skills have solid tool coverage (Figma, Adobe CC, Canva).

**Gaps:**
- Missing AI-era creative tools: Midjourney, Stable Diffusion 3.5, Runway Gen-3, Sora 2.0
- Translator skill lacks CAT tool workflows (memoQ, SDL Trados) and MT post-editing (MTPE) guidance
- No IP/copyright guidance for AI-generated content — critical legal gap for creative professionals

**Improvement:** Add AI tool integration section to all creative skills. Translator needs MTPE quality scoring (MQM framework). Add "AI-generated content IP" risk to § 3 for all creative skills.

---

### 4.21 Special Skills — Score: 8.5/10 ✅ (agent-persona) / 6.0/10 ⚠️ (others)

**Skills (19):** agent-persona-designer (exemplary) + skill-writer + ai-trainer + data-labeler + supply-chain-expert + 14 others

**agent-persona-designer** is the category exemplar with OCEAN matrix, 5-layer security policy, anti-jailbreak guardrails.

**skill-writer concern:** This is the meta-skill that templates all other skills. It has non-standard section structure (§ 7 "Workflow", § 8 "Templates" — different from project standard). Inconsistency here ripples into every new skill created.

**Improvement:** Upgrade `skill-writer` to v3.0 standard FIRST — before any other batch upgrades. It should demonstrate the exact format it teaches. Also update skill-writer's platform support with correct SKILL.md URL pattern.

---

## 5. Prioritized Upgrade Roadmap

### CRITICAL — Fix Immediately (bugs affecting usability)

| # | Action | Scope | Impact |
|---|--------|-------|--------|
| C1 | **Fix broken install URLs** in all v2.0 skills | 98 skills | Install commands now work |
| C2 | **Add `quality: basic`** YAML field to v1.0 skills lacking it | ~6 skills | Metadata tooling no longer errors |
| C3 | **Upgrade `skill-writer`** to v3.0 standard with correct URL pattern | 1 skill | Template accuracy for all future skills |

### HIGH PRIORITY — Phase 2 Completion (40 skills pending)

| Wave | Skills | Priority Rationale |
|------|--------|--------------------|
| Wave 2.2–2.3 | Autonomous Driving (7 skills) | Largest AV developer community |
| Wave 2.4 | Robotics (5 skills) | Humanoid robotics boom 2026 |
| Wave 2.5 | AI Biotech (5 skills) | High ethical risk — needs careful review |
| Wave 2.6 | Quantum (4 skills) | Fast-evolving — content window closing |
| Wave 2.7–2.8 | Aerospace (10 skills) | Include ITAR disclaimer |
| Wave 2.9 | Semiconductor + Materials (9 skills) | CHIPS Act demand |
| Wave 2.10 | Telecom (mark complete, update progress) | Content already done |

### MEDIUM PRIORITY — Phase 3: Professional Domains

| Wave | Focus | Skills |
|------|-------|--------|
| Wave 3.1 | Community Verified → § format + URL fix | 28 |
| Wave 3.2 | Finance stubs → full 16-section rewrite | 15 |
| Wave 3.3 | Legal stubs → full rewrite + scope guards | 12 |
| Wave 3.4 | Healthcare stubs → full rewrite + disclaimers | 40 |
| Wave 3.5 | Education (all) | 55 |
| Wave 3.6 | Government & Public Service + jurisdiction disclaimers | 29 |
| Wave 3.7 | Creative, Media, Entertainment + AI tool integration | 23 |
| Wave 3.8 | Construction, Workers | 26 |
| Wave 3.9 | Service, Retail, Agriculture | 23 |

### LOWER PRIORITY — Tools Category Overhaul (115 skills, specialized template)

| Phase | Sub-category Focus | Skills |
|-------|--------------------|--------|
| T1 | cicd, database, container, cloud, security | ~40 |
| T2 | cad, engineering-simulation, scientific, media, design | ~35 |
| T3 | cn-cloud (full subcategory), analytics, iac, productivity | ~40 |

---

## 6. Format Standardization Plan

### 6.1 Heading Migration (461 skills)

When any v2.0/v3.0 skill is content-upgraded, simultaneously migrate headings:

```
## 1. System Prompt          →  ## § 1 · System Prompt
## 2. What This Skill Does   →  ## § 2 · What This Skill Does
### 1.1 ...                  →  ### 1.1 ...   (subsections unchanged)
```

Do NOT migrate headings without content upgrade — avoid churn commits that only change heading style with no value.

### 6.2 Professional Toolkit Table Upgrade (98+ skills)

v2.0 format (missing Category column):
```markdown
| Tool | Purpose |
|------|---------|
| JCID | Diagnostics |
```

v3.0 standard format:
```markdown
| Category | Tools | Purpose |
|----------|-------|---------|
| Diagnostic | JCID, 3uTools | Software troubleshooting, firmware flashing |
```

### 6.3 Platform Support URL Fix (98 skills)

v2.0 broken URL pattern:
```
https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/{category}/{name}.md
```

Correct v3.0 URL pattern:
```
https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/{category}/{name}/SKILL.md
```

Update install echo commands in § 13 to match.

---

## 7. Quality Gate Checklist

Before marking any skill upgrade complete, verify ALL:

```
[ ] All 16 sections present in § N · format
[ ] System Prompt (§ 1) has: role identity + decision framework (5+ gates) + thinking patterns (4+) + comms style
[ ] Domain frameworks contain specific numeric thresholds (not just "consider X")
[ ] Metrics table has formula + target range for each metric
[ ] Workflow (§ 8) has [✓ Done] and [✗ FAIL] criteria for each phase
[ ] Risk table (§ 3) has 5+ rows, each domain-specific (no generic disclaimers)
[ ] 3+ scenario examples (§ 9) with full conversation flows and artifacts
[ ] Common Pitfalls (§ 10) has named anti-patterns with ❌/✅ and "why it matters"
[ ] All 9 YAML fields filled; description has role + triggers + "works with"
[ ] Platform Support URL uses /SKILL.md path (not flat .md)
[ ] Professional Toolkit (§ 6) has Category column
[ ] Version History (§ 15) has 3+ entries
[ ] License & Author (§ 16) complete
[ ] Score badge reflects actual quality (not self-inflated 9.5/10)
[ ] Healthcare/Legal/Biotech skills: professional disclaimer in § 1 system prompt
[ ] Aerospace/Materials skills: ITAR/export control awareness note where applicable
```

---

## 8. Reference Implementations

| Category | Reference Skill | Why Use It |
|----------|----------------|-----------|
| Software dev | `skills/software/backend-developer/SKILL.md` | Full 16-section exemplar with real code |
| AI/ML | `skills/ai-ml/ai-application-engineer/SKILL.md` | LLM+RAG pipeline examples |
| Security | `skills/software/security-engineer/SKILL.md` | Risk-heavy domain model |
| Architecture | `skills/software/software-architect/SKILL.md` | ADR + C4 diagram patterns |
| Research | `skills/research/principal-investigator/SKILL.md` | Grant/publication workflows |
| Finance | `skills/finance/financial-analyst/SKILL.md` | Quantitative metrics model |
| Healthcare | `skills/healthcare/general-practitioner/SKILL.md` | Clinical reasoning framework |
| Trade/Repair | `skills/repair-worker/mobile-repair-technician/SKILL.md` | § format, references/, trade depth |
| Safety-critical | `skills/transport-worker/pilot/SKILL.md` | CRM framework, emergency procedures |
| Tools (specialized) | `skills/it-support/macos-config-expert/SKILL.md` | Tool-expert persona model |

---

## 9. Progress Tracker

### Phase 1: Software Dev Adjacent — ✅ COMPLETE

| Skill | Status | Completed |
|-------|--------|-----------|
| AI Security Engineer | ✅ Done | 2026-03-01 |
| Data Security Officer | ✅ Done | 2026-03-01 |
| Privacy Computing Engineer | ✅ Done | 2026-03-01 |
| Blockchain Architect | ✅ Done | 2026-03-01 |
| Digital Twin Engineer | ✅ Done | 2026-03-01 |
| Spatial Computing Engineer | ✅ Done | 2026-03-04 |
| Tech Writer | ✅ Done | 2026-03-01 |
| ERP Administrator | ✅ Done | 2026-03-02 |
| Information Security Admin | ✅ Done | 2026-03-04 |
| IT Support Specialist | ✅ Done | 2026-03-02 |
| Data Asset Appraiser | ✅ Done | 2026-03-01 |
| Logistics Algorithm Engineer | ✅ Done | 2026-03-02 |

### Phase 2: AI Development Applications — 2/42 Done

| Skill | Status | Completed |
|-------|--------|-----------|
| AI Trainer | ✅ Done | 2026-03-04 |
| Data Labeler | ✅ Done | 2026-03-04 |
| Autonomous Driving Engineer | ⏳ Pending | — |
| End-to-End Autonomous Researcher | ⏳ Pending | — |
| Perception Algorithm Engineer | ⏳ Pending | — |
| Planning & Decision Engineer | ⏳ Pending | — |
| HD Map Engineer | ⏳ Pending | — |
| Simulation Platform Engineer | ⏳ Pending | — |
| V2X System Engineer | ⏳ Pending | — |
| Automotive Design Engineer | ⏳ Pending | — |
| Embodied AI Researcher | ⏳ Pending | — |
| Robot Perception Engineer | ⏳ Pending | — |
| Motion Control Engineer | ⏳ Pending | — |
| Robot Mechanical Engineer | ⏳ Pending | — |
| Precision Reducer Engineer | ⏳ Pending | — |
| AI Drug Design Scientist | ⏳ Pending | — |
| Brain-Computer Interface Engineer | ⏳ Pending | — |
| Synthetic Biologist | ⏳ Pending | — |
| Cell Therapy Scientist | ⏳ Pending | — |
| Biomaterials Engineer | ⏳ Pending | — |
| Quantum Algorithm Engineer | ⏳ Pending | — |
| Quantum Communication Engineer | ⏳ Pending | — |
| Quantum Physicist | ⏳ Pending | — |
| Quantum Sensor Researcher | ⏳ Pending | — |
| Remote Sensing Data Scientist | ⏳ Pending | — |
| UAV Flight Control Engineer | ⏳ Pending | — |
| Low-Altitude Traffic Engineer | ⏳ Pending | — |
| eVTOL Chief Designer | ⏳ Pending | — |
| Vertiport Planning Engineer | ⏳ Pending | — |
| Satellite Communication Engineer | ⏳ Pending | — |
| Airworthiness Certification Engineer | ⏳ Pending | — |
| Space Mission Planner | ⏳ Pending | — |
| Rocket Chief Designer | ⏳ Pending | — |
| Liquid Rocket Engine Engineer | ⏳ Pending | — |
| Chip Design Engineer | ⏳ Pending | — |
| Wide Bandgap Semiconductor Engineer | ⏳ Pending | — |
| Nanomaterials Engineer | ⏳ Pending | — |
| Composite Materials Engineer | ⏳ Pending | — |
| Superconducting Materials Researcher | ⏳ Pending | — |
| 6G Communication Researcher | ⏳ Pending | — |
| ISAC Engineer | ⏳ Pending | — |
| NTN Engineer | ⏳ Pending | — |

### Phase C: Critical Bug Fixes

| Fix | Scope | Status |
|-----|-------|--------|
| Fix broken install URLs (all v2.0 skills) | 98 skills | ⏳ Pending |
| Add missing `quality:` YAML field | ~6 skills | ⏳ Pending |
| Upgrade `skill-writer` to v3.0 standard | 1 skill | ⏳ Pending |

### Phase 3: Professional & Business Domains

| Batch | Focus | Count | Status |
|-------|-------|-------|--------|
| Wave 3.1 | Community Verified → § format + URL fix | 28 | ⏳ Pending |
| Wave 3.2 | Finance stubs → full 16-section | 15 | ⏳ Pending |
| Wave 3.3 | Legal stubs → full rewrite + scope guards | 12 | ⏳ Pending |
| Wave 3.4 | Healthcare stubs + mandatory disclaimers | 40 | ⏳ Pending |
| Wave 3.5 | Education (all) | 55 | ⏳ Pending |
| Wave 3.6 | Government & Public Service | 29 | ⏳ Pending |
| Wave 3.7 | Creative, Media, Entertainment | 23 | ⏳ Pending |
| Wave 3.8 | Construction, Workers | 26 | ⏳ Pending |
| Wave 3.9 | Service, Retail, Agriculture | 23 | ⏳ Pending |

### Phase T: Tools Category (v1.0 → v3.0)

| Phase | Focus | Count | Status |
|-------|-------|-------|--------|
| T1 | cicd, database, container, cloud, security | ~40 | ⏳ Pending |
| T2 | cad, engineering, scientific, media, design | ~35 | ⏳ Pending |
| T3 | cn-cloud, analytics, iac, productivity | ~40 | ⏳ Pending |

---

## 10. Effort Estimate

| Phase | Skills | AI-Assisted Hours | Notes |
|-------|--------|------------------|-------|
| ✅ Already exemplary v3.0 | 87 | — | — |
| C: Critical bug fixes | 105 | ~8h | URL fix is largely mechanical |
| P2: AI Dev Applications | 40 | ~80h | High technical depth required |
| P3: Professional Domains | 228 | ~420h | Batch processing with templates |
| T: Tools category overhaul | 115 | ~115h | Specialized tools template |
| **Total remaining** | **488** | **~623h** | |

**With 4 parallel agents × 2 skills/hour average:** ~78 hours wall-clock time to complete all remaining skills.

---

*Maintained by: neo.ai | Last Updated: 2026-03-18 | Branch: claude/skill-evaluation-improvements-aXOj0*
