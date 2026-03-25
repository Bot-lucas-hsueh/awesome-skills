# Example 4: Review & Score Existing Skill

## Context

User has a skill and wants to know its quality score and improvement areas.

## User Input

"Please review this skill and give me a score. [pastes skill content]"

## Review Process

### Step 1: Initial Assessment

**Quick Scan**:
- Lines: 450 (Standard tier range ✓)
- System Prompt: Has §1.1, missing §1.2/1.3 ✗
- Generic terms: "expert", "professional" detected ✗

### Step 2: Dimension Scoring

| Dimension | Score | Issues |
|-----------|-------|--------|
| System Prompt | 5/10 | Missing §1.2/1.3 |
| Domain Knowledge | 6/10 | Generic content, no specific data |
| Workflow | 7/10 | Good phases, weak Done/Fail |
| Error Handling | 6/10 | Basic, no risk matrix |
| Examples | 7/10 | 3 examples, need 5 |
| Metadata | 8/10 | Complete YAML |
| **Total** | **6.5/10** | |

### Step 3: Gap Analysis

**Critical Issues**:
1. Missing §1.2/1.3 (structural)
2. Generic content throughout
3. No specific company/methodology data
4. Only 3 examples (need 5)

**Improvement Path**:
- Add §1.2 Decision Framework
- Add §1.3 Thinking Patterns
- Replace generic terms with specific data
- Add 2 more examples

### Step 4: Upgrade Plan

**Estimated Time**: 2-3 hours
**Target Score**: 9.5/10

**Tasks**:
1. Research domain data (30 min)
2. Write §1.2/1.3 (20 min)
3. Replace generic content (40 min)
4. Add 2 examples (30 min)
5. Strengthen Done/Fail criteria (20 min)
6. Validation (15 min)

## Delivered Report

```
Current Score: 6.5/10
Target Score: 9.5/10
Gap: +3.0 points

Priority Fixes:
1. [HIGH] Add missing System Prompt sections
2. [HIGH] Replace generic content with specific data
3. [MEDIUM] Add 2 more examples
4. [MEDIUM] Strengthen Done/Fail criteria

Estimated Time: 2-3 hours
```
