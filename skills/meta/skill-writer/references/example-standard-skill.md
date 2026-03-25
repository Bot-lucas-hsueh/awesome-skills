# Example 2: Create Standard Skill

## Context

User wants a data analysis assistant that can help with cleaning, visualization, and insights.

## User Input

"Create a skill that helps me analyze data. I need help with cleaning data, creating charts, and getting insights."

## Assessment

- Scope: 3 capabilities (cleaning, visualization, insights)
- Complexity: Domain knowledge + workflows
- Tier: **Standard** (150-500 lines)

## Created Skill

### Key Sections

**§1 System Prompt**:
- §1.1: Data Analysis Assistant identity
- §1.2: Priority hierarchy (clean → visualize → analyze)
- §1.3: 3 thinking patterns

**§3 Domain Knowledge**:
- Pandas methods (head, describe, info, isnull)
- Matplotlib/seaborn chart types
- Statistical tests (t-test, correlation)

**§4 Workflow**:
4 phases: Load → Clean → Visualize → Analyze
Each with Done/Fail criteria

**§5 Examples**:
3 detailed scenarios (CSV cleaning, time series, correlation analysis)

## Key Design Decisions

1. **Standard Tier**: 3 capabilities, ~250 lines
2. **Full System Prompt**: §1.1/1.2/1.3 structure
3. **Specific Tools**: Pandas, Matplotlib, Seaborn with specific methods
4. **Workflow**: 4 phases with clear Done/Fail
5. **Multiple Examples**: 3 scenarios covering common use cases
6. **Progressive Disclosure**: Details in references/
