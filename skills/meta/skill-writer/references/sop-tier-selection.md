# SOP 1: Tier Selection

## Purpose

Determine appropriate tier (Lite/Standard/Enterprise) for a new skill.

## Decision Matrix

### Lite Tier (50-150 lines)

**Choose When**:
- Single API/tool wrapper
- One primary function
- Simple input/output transformation
- No complex decision logic

**Examples**:
- Weather API caller
- Currency converter
- Password generator
- QR code creator

### Standard Tier (150-500 lines)

**Choose When**:
- Domain knowledge base
- 2-5 related capabilities
- Multi-step workflows
- Some complexity

**Examples**:
- Data analyst assistant
- Marketing copywriter
- Code reviewer
- Research assistant

### Enterprise Tier (500-1500 lines)

**Choose When**:
- Complete methodology
- 5+ integrated capabilities
- Complex decision frameworks
- Extensive error handling

**Examples**:
- Strategic consultant
- Product manager
- Security auditor
- Enterprise architect

## Selection Workflow

1. **List Capabilities**: What will this skill do?
2. **Count Functions**: How many distinct capabilities?
3. **Assess Complexity**: Simple workflow or complex methodology?
4. **Select Tier**: Match to Lite/Standard/Enterprise
5. **Verify**: Does complexity match tier expectations?

## Common Mistakes

- **Over-tiering**: Making a simple tool Enterprise (bloat)
- **Under-tiering**: Making a complex methodology Lite (incomplete)
- **Scope Creep**: Starting Lite, adding features, becoming messy
