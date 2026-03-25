# Layer 3: Validation Engine

## Purpose

Verify skill quality against 6-dimension rubric.

## Components

### Dimension Scorer

**System Prompt (20%)**:
- §1.1 Identity complete: 5 points
- §1.2 Framework clear: 5 points
- §1.3 Thinking patterns (3+): 5 points
- Professional DNA specific: 5 points

**Domain Knowledge (20%)**:
- Specific company data: 5 points
- Specific methodologies: 5 points
- Real numbers/benchmarks: 5 points
- No generic terms: 5 points

**Workflow (20%)**:
- 4-5 phases: 5 points
- Done criteria per phase: 5 points
- Fail criteria per phase: 5 points
- Clear gates: 5 points

**Error Handling (15%)**:
- Anti-patterns documented: 5 points
- Risk matrix: 5 points
- Crisis playbooks: 5 points

**Examples (15%)**:
- 5+ scenarios: 5 points
- Detailed contexts: 5 points
- Realistic data: 5 points

**Metadata (10%)**:
- Complete YAML: 5 points
- Accurate information: 5 points

### Evaluator Simulation

Pre-check before formal evaluation:

```
Text Quality Check:
├── System Prompt: §1.1/1.2/1.3 present?
├── Domain Knowledge: Specific data?
├── Workflow: Done/Fail criteria?
├── Error Handling: Anti-patterns?
├── Examples: 5+ detailed?
└── Metadata: Complete YAML?

Runtime Quality Check:
├── Role immersion: Clear identity?
├── Framework execution: Decision hierarchy?
├── Output actionability: Concrete steps?
├── Knowledge accuracy: Verified data?
├── Long-conversation stability: Consistent?
└── Resilience: Error handling?
```

## Validation Workflow

1. **Dimension Scoring**: Score each of 6 dimensions
2. **Gap Analysis**: Identify improvement areas
3. **Upgrade Planning**: Design improvement path
4. **Iterate**: Fix and re-score until ≥ 9.0
