## § 8 · Standard Workflow

### 8.1 New Skill Creation

```
Phase 1: Discovery [✓ Done: issue created with scope]
├── Verify skill doesn't exist
├── Confirm scope is single domain
└── Assign priority (P0/P1/P2)

Phase 2: Branch [✓ Done: branch created]
├── git checkout -b feature/[skill-name]
├── Copy TEMPLATE.md to skills/[category]/
└── Fill metadata (9 fields)

Phase 3: Development [✓ Done: all 16 sections complete]
├── Write §1 System Prompt (30-50 lines)
├── Build domain frameworks (§7)
├── Add 3+ scenarios (§9)
├── Document risks (§3)
└── Self-score against rubric

Phase 4: Validation [✓ Done: CI passes]
├── yamllint SKILL.md
├── markdownlint SKILL.md
├── Calculate rubric score
├── Run test cases
└── git push && gh pr create
```

### 8.2 Skill Upgrade

```
Phase 1: Assess [✓ Done: current score known]
├── Read existing skill
├── Score each dimension
└── Identify gap (lowest scoring section)

Phase 2: Plan [✓ Done: upgrade strategy defined]
├── Prioritize sections by ROI
├── Set target score
└── Estimate effort

Phase 3: Execute [✓ Done: changes complete]
├── Upgrade in priority order
├── Add missing sections
└── Improve low-scoring sections

Phase 4: Verify [✓ Done: score ≥ target]
├── Recalculate rubric
├── Run all test cases
└── Ensure no regression
```

### 8.3 Review Process

```
Step 1: Validate Structure
├── 16 sections in order?
├── YAML frontmatter valid?
└── All required fields present?

Step 2: Score Dimensions
├── System Prompt: _/10
├── Domain Knowledge: _/10
├── Workflow: _/10
├── Risk: _/10
├── Examples: _/10
└── Metadata: _/10

Step 3: Calculate Weighted Score
├── Formula: SP×0.20 + DK×0.25 + WA×0.15 + RD×0.10 + EQ×0.20 + MC×0.10
└── Result: __/10

Step 4: Decision
├── ≥9.0 → Approve as Exemplary
├── ≥7.0 → Approve as Expert
├── <7.0 → Request changes
└── Any dimension <4 → BLOCK
```

---
