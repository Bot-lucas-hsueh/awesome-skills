# Design Patterns for Skills

> Proven structural patterns for different skill types

---

## Pattern 1: Tool Wrapper

**Use when:** Wrapping a specific tool, library, or API

**Structure:**
```
Setup → Usage → Examples
```

**SKILL.md Structure:**
```markdown
## System Prompt
You are a [tool] assistant...

## Setup
Prerequisites, installation, configuration

## Capabilities
✅ What the tool can do

## Usage
### [Operation 1]
Steps to perform operation

### [Operation 2]
...

## Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| param1 | string | Description |

## Error Handling
Common errors and solutions

## Examples
Demonstrations of usage
```

**Best for:**
- API clients
- CLI tool wrappers
- Library interfaces
- File processors

**Example Skills:**
- PDF processor (PyPDF2 wrapper)
- Git assistant (git command wrapper)
- AWS CLI helper

---

## Pattern 2: Generator

**Use when:** Creating specific types of outputs

**Structure:**
```
Template → Variables → Output → Validation
```

**SKILL.md Structure:**
```markdown
## System Prompt
You are a [output type] generator...

## Output Format
[Template structure]

## Variables
| Variable | Required | Description |
|----------|----------|-------------|
| var1 | Yes | Description |
| var2 | No | Default: X |

## Generation Process
1. Collect variables
2. Apply template
3. Generate output
4. Validate result

## Examples
Input → Output pairs
```

**Best for:**
- Document generators
- Code generators
- Report creators
- Content templates

**Example Skills:**
- Meeting notes generator
- PR description writer
- Documentation generator
- Marketing copy creator

---

## Pattern 3: Reviewer

**Use when:** Evaluating existing content

**Structure:**
```
Criteria → Assessment → Feedback → Recommendations
```

**SKILL.md Structure:**
```markdown
## System Prompt
You are a [domain] reviewer...

## Review Criteria
1. [Criterion 1] - weight: high/medium/low
2. [Criterion 2] - weight: high/medium/low

## Assessment Process
1. Analyze against each criterion
2. Score each dimension
3. Identify issues
4. Prioritize fixes

## Feedback Format
```
## Review: [Item]

**Overall:** [Score/Assessment]

### Strengths
- [Strength 1]

### Issues
| Priority | Issue | Recommendation |
|----------|-------|----------------|
| High | [Issue] | [Fix] |

### Action Items
1. [Action 1]
```

## Examples
[Sample reviews]
```

**Best for:**
- Code reviewers
- Document reviewers
- Design critics
- Quality assessors

**Example Skills:**
- Code review assistant
- Resume reviewer
- Design critique
- Security auditor

---

## Pattern 4: Pipeline

**Use when:** Multi-step process with clear stages

**Structure:**
```
Input → Step 1 → Step 2 → Step 3 → Output
```

**SKILL.md Structure:**
```markdown
## System Prompt
You are a [process] orchestrator...

## Pipeline Overview
[Diagram or list of stages]

## Stages

### Stage 1: [Name]
**Input:** [What it receives]
**Process:** [What happens]
**Output:** [What it produces]
**Validation:** [Check before proceeding]

### Stage 2: [Name]
...

## Stage Transitions
- If [condition] → proceed to next
- If [condition] → retry current
- If [condition] → error handler

## Error Handling
Per-stage error handling

## Examples
End-to-end pipeline examples
```

**Best for:**
- Data processing workflows
- Content pipelines
- Approval processes
- ETL processes

**Example Skills:**
- Data cleaning pipeline
- Content approval workflow
- Onboarding process
- Incident response

---

## Pattern 5: Inversion

**Use when:** Need to gather info before acting

**Structure:**
```
Collection → Analysis → Execution
```

**SKILL.md Structure:**
```markdown
## System Prompt
You are a [role] that gathers requirements first...

## Information Needed
| Info | Why | How to Ask |
|------|-----|------------|
| [Info 1] | [Purpose] | [Question] |
| [Info 2] | [Purpose] | [Question] |

## Collection Phase
Questions to ask user

## Analysis Phase
How to process gathered info

## Execution Phase
What to do with analysis

## Examples
[Collection → Execution examples]
```

**Best for:**
- Requirements gathering
- Consultative roles
- Configuration assistants
- Diagnostic tools

**Example Skills:**
- Architecture consultant
- Troubleshooting assistant
- Requirements analyst
- Configuration wizard

---

## Pattern Selection Guide

| If your skill... | Use Pattern |
|------------------|-------------|
| Wraps a tool/library | Tool Wrapper |
| Creates outputs from templates | Generator |
| Evaluates existing work | Reviewer |
| Has multiple sequential steps | Pipeline |
| Needs info before helping | Inversion |

---

## Combining Patterns

Complex skills can combine patterns:

**Example: Data Analysis Skill**
- **Inversion** to gather requirements
- **Pipeline** for data processing steps
- **Generator** for report output

---

**Related:**
- Pattern Selector → ./pattern-selector.md
- Lite Workflow → ../workflow/lite-workflow.md
- Standard Workflow → ../workflow/standard-workflow.md
