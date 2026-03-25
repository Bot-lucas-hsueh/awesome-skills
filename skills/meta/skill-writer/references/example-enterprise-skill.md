# Example 3: Create Enterprise Skill

## Context

Enterprise needs a strategic planning consultant skill for C-level strategy development.

## User Input

"Create an enterprise skill for strategic planning. Our executives need help with market analysis, competitive positioning, and roadmap development."

## Assessment

- Scope: 5+ capabilities (analysis, positioning, roadmap, risk, execution)
- Complexity: Complete methodology
- Tier: **Enterprise** (500-1500 lines)

## Created Skill

### Architecture

**Three-Layer Design**:
1. Assessment Layer: Strategy maturity evaluation
2. Analysis Layer: Market, competitive, internal analysis
3. Planning Layer: Roadmap, risk, execution planning

**§1 System Prompt**:
- §1.1: Strategic Planning Consultant identity
  - DNA: Pattern Matcher, Data Synthesizer, Decision Architect
  - Context: Works with Fortune 500, uses McKinsey/BCG frameworks
  - Metrics: 80%+ strategy acceptance, 70%+ implementation success
- §1.2: Decision framework with 5 priorities
- §1.3: 5 thinking patterns with concrete structures

**§3 Domain Knowledge**:
- McKinsey 7-S Framework steps
- BCG Matrix quadrants and actions
- Porter's 5 Forces analysis process
- Real company data (market shares, growth rates)

**§4 Workflow**:
5 phases: Discovery → Analysis → Strategy → Planning → Execution
Each with detailed Done/Fail criteria

**§5 Examples**:
5 scenarios (market entry, digital transformation, M&A, cost reduction, growth strategy)

**§6 Anti-Patterns**:
8 common strategic planning mistakes with solutions

## Key Design Decisions

1. **Enterprise Tier**: Complete methodology, ~800 lines in references/
2. **Specific Frameworks**: McKinsey 7-S, BCG Matrix, Porter's 5 Forces
3. **Real Data**: Company metrics, market data
4. **5 Examples**: Covering major strategy types
5. **Extensive Error Handling**: Risk matrix, crisis playbooks
6. **Progressive Disclosure**: SKILL.md ~280 lines, 20+ references
