# Domain Knowledge Reference

## skill-writer v5 Specification

### 6-Dimension Quality Rubric

| Dimension | Weight | Key Requirements | Scoring Criteria |
|-----------|--------|------------------|------------------|
| **System Prompt** | 20% | §1.1 Identity, §1.2 Framework, §1.3 Thinking | Each subsection: 3-4 points |
| **Domain Knowledge** | 20% | Specific data, methodologies, benchmarks | Real numbers required |
| **Workflow** | 20% | 4-5 phases, Done/Fail criteria | Gates between phases |
| **Error Handling** | 15% | Anti-patterns, risk matrix, crisis playbooks | Actionable solutions |
| **Examples** | 15% | 5+ detailed scenarios | Realistic contexts |
| **Metadata** | 10% | Complete YAML frontmatter | Accurate information |

### Quality Tiers

| Tier | Lines | Capabilities | Examples |
|------|-------|--------------|----------|
| **Lite** | 50-150 | 1 function | API wrapper, utility tool |
| **Standard** | 150-500 | 2-5 capabilities | Domain assistant |
| **Enterprise** | 500-1500 | 5+ capabilities | Complete methodology |

## skill-evaluator v2.1 Certification

### Dual-Track Assessment

**Text Quality (50%)**:
- System Prompt completeness
- Domain Knowledge specificity
- Workflow clarity
- Error Handling coverage
- Examples richness
- Metadata accuracy

**Runtime Quality (50%)**:
- Role immersion
- Framework execution
- Output actionability
- Knowledge accuracy
- Long-conversation stability
- Resilience

### Certification Thresholds

```
EXEMPLARY (9.0-10.0):
├── Text Score ≥ 8.0
├── Runtime Score ≥ 8.0
├── Variance < 1.0
└── All dimensions ≥ 6.0

PRODUCTION (7.0-8.9):
├── Text Score ≥ 7.0
├── Runtime Score ≥ 7.0
├── Variance < 1.5
└── All dimensions ≥ 5.0

DEVELOPMENT (5.0-6.9):
├── Text Score ≥ 5.0
├── Runtime Score ≥ 5.0
└── Basic structure present
```

## Progressive Disclosure Standard

### Token Efficiency Target

```
SKILL.md: 250-300 lines (navigation)
references/: 2500-3000 lines (details)
Total: 2750-3300 lines professional content

Navigation Ratio: 1:10 (overview:detail)
```

### File Structure

```
skill-name/
├── SKILL.md (navigation, <300 lines)
└── references/
    ├── concepts/ (domain fundamentals)
    ├── workflow/ (detailed procedures)
    ├── examples/ (full scenarios)
    └── sop/ (standard operating procedures)
```
