# Quality Gates

## Gate Definitions

| Phase | Gate | Fail Action |
|-------|------|-------------|
| Planning | Tier selected, structure defined | Redefine scope |
| System Prompt | §1.1/1.2/1.3 complete | Add missing sections |
| Domain Knowledge | Specific data collected | Research deeper |
| Workflow | 4-5 phases with Done/Fail | Restructure |
| Examples | 5 detailed scenarios | Add more examples |
| Validation | Evaluator score ≥ 9.0 | Iterate improvements |

## Gate Criteria Details

### Planning Gate

**Requirements**:
- Skill scope clearly defined
- Appropriate tier selected (Lite/Standard/Enterprise)
- Creation path determined (beginner/quick/standard/expert)

**Pass**: Clear scope, correct tier, defined path
**Fail**: Ambiguous scope, wrong tier, unclear path

### System Prompt Gate

**Requirements**:
- §1.1 Identity & Worldview: Specific role, DNA, context, metrics
- §1.2 Decision Framework: Priority hierarchy, quality gates
- §1.3 Thinking Patterns: 3+ patterns with structures

**Pass**: All sections complete with specific data
**Fail**: Missing sections or generic content

### Domain Knowledge Gate

**Requirements**:
- Real company names with metrics
- Specific methodology names with steps
- Tool specifications (versions, limits)
- Benchmark numbers
- No generic terms

**Pass**: All data specific and verifiable
**Fail**: Generic terms or missing data

### Workflow Gate

**Requirements**:
- 4-5 phases defined
- Done criteria per phase
- Fail criteria per phase
- Clear gates between phases

**Pass**: Complete workflow with gates
**Fail**: Missing criteria or unclear flow

### Examples Gate

**Requirements**:
- 5+ detailed scenarios
- Realistic contexts
- Specific user inputs
- Detailed expert responses
- Concrete outputs

**Pass**: All examples detailed and realistic
**Fail**: < 5 examples or shallow content

### Validation Gate

**Requirements**:
- Evaluator score ≥ 9.0
- Text Score ≥ 8.0
- Runtime Score ≥ 8.0
- Variance < 1.0

**Pass**: All thresholds met
**Fail**: Any threshold not met
