# Skill Writer — Standard Workflow

Load this file when starting any create / review / upgrade task.

---

## 8.1 Creating a New Skill

```
Phase 1: Discovery  [✓ Done: one-sentence scope + named tier target agreed]
├── What domain? Who is the target user? → shapes §1 Role + §2 Capabilities
├── What specific problems does this skill solve? → shapes §3 Risks + §12 Scope
├── What existing skills overlap? (check /skills/) → shapes §11 Integration
└── What quality tier is the goal? → sets §7.1 threshold
✗ FAIL: Cannot answer all 4 in ≤2 sentences → scope too broad; apply Anti-Pattern #1

Phase 2: Architecture  [✓ Done: skeleton with all 16 H2 headers + 1-line purpose per section]
├── Define the system prompt (role + thinking patterns + style) → §1
├── Identify 3-5 core capabilities → §2
├── Map domain frameworks and decision tools → §7
├── Design multi-phase workflow → §8
└── Plan 2+ scenario examples → §9
✗ FAIL: Cannot identify ≥2 domain-specific decision frameworks → consult domain expert before writing

Phase 3: Writing  [✓ Done: all 16 sections complete; no placeholder or TBD content]
├── Fill complete metadata (all 9 fields; no HTML comments in YAML description) → §7.2
├── Write system prompt in code block → use §1 of SKILL.md as exemplar
├── Build each of the 16 sections in correct order → standards.md §7.3
├── No bilingual labels in headings/tables; no HTML comments → standards.md §7.4
└── Include concrete examples showing AI applying frameworks → scenarios.md
✗ FAIL: Any section contains "TBD" or placeholder text → complete or narrow scope before submitting

Phase 4: Quality Assurance  [✓ Done: rubric score ≥ tier target + litmus test passes]
├── Score against Quality Rubric → standards.md §7.1; target ≥7.0 (Expert), ≥9.0 (Exemplary)
├── Validate YAML metadata → yamllint; check all 9 fields
├── Confirm all 16 sections present → standards.md §7.3
├── Run anti-pattern scan → anti-patterns.md; check all 9 patterns
└── Litmus test: Prompt AI with vs. without skill on 3 tasks
    PASS = AI cites ≥1 framework AND uses different structure in ≥2/3 tasks
    FAIL = identical structure in ≥2/3 tasks OR 0 frameworks cited
✗ FAIL: Litmus test shows no behavioral difference → skill is Basic regardless of rubric score
```

---

## 8.2 Reviewing & Scoring a Skill

```
Step 1: Read the complete skill file
Step 2: Score each of the 6 Quality Rubric dimensions (1-10) → standards.md §7.1
Step 3: Calculate weighted average → determine tier
Step 4: Identify top 3 weaknesses by impact
Step 5: Provide rewrite suggestions with before/after examples
Step 6: Give classification and upgrade path
```

---

## 8.3 Upgrading Basic → Expert

```
From Basic to Expert, add in priority order (ROI table → standards.md §7.6):

☐ Structured System Prompt (role + thinking patterns + communication style)
☐ Deep Domain Frameworks (decision matrices with thresholds, not just lists)
☐ Scenario-Based Guidance (2-3 full conversation examples → scenarios.md)
☐ Complete Metadata (all 9 fields; no HTML in YAML description)
☐ Domain-Specific Risks (4+ with severity classification)
☐ Quality Score Verification (weighted avg ≥ 7.0 via standards.md §7.1)
```
