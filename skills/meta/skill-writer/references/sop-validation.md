# SOP 4: Quality Validation

## Purpose

Verify skill meets 9.5/10 EXEMPLARY standard before delivery.

## Pre-Delivery Checklist

### System Prompt (20%)

- [ ] §1.1 Identity: Specific role title (not "expert")
- [ ] §1.1 Identity: 3-4 professional DNA descriptors
- [ ] §1.1 Identity: Specific context and success metrics
- [ ] §1.2 Framework: Priority hierarchy defined
- [ ] §1.2 Framework: Quality gates table
- [ ] §1.3 Thinking: 3+ patterns with concrete structures

### Domain Knowledge (20%)

- [ ] Real company names with metrics
- [ ] Specific methodology names with steps
- [ ] Tool specifications (versions, limits)
- [ ] Benchmark numbers
- [ ] No generic terms ("professional", "expert", "best practices")

### Workflow (20%)

- [ ] 4-5 phases defined
- [ ] Done criteria per phase
- [ ] Fail criteria per phase
- [ ] Clear gates between phases

### Error Handling (15%)

- [ ] Anti-patterns documented
- [ ] Risk matrix included
- [ ] Crisis playbooks available

### Examples (15%)

- [ ] 5+ detailed scenarios
- [ ] Realistic contexts
- [ ] Specific user inputs
- [ ] Detailed expert responses
- [ ] Concrete outputs

### Metadata (10%)

- [ ] Complete YAML frontmatter
- [ ] Accurate version and date
- [ ] Correct tags
- [ ] Target scores documented

### Progressive Disclosure

- [ ] SKILL.md < 300 lines
- [ ] 15+ reference links
- [ ] references/ directory exists
- [ ] Key files created

## Validation Workflow

1. **Self-Check**: Run through checklist manually
2. **Content Scan**: grep for generic terms
3. **Line Count**: Verify SKILL.md < 300
4. **Link Count**: Verify 15+ reference links
5. **Evaluator**: Run skill-evaluator if available
6. **Iterate**: Fix issues until ≥ 9.0

## Generic Terms to Check

Search for and replace:
- "professional" → specific methodology/company
- "expert" → specific credentials/data
- "best practices" → specific frameworks
- "industry standard" → specific standard name
- "years of experience" → specific metrics
