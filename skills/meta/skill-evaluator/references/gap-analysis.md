# Gap Analysis Guide

> Diagnose skill quality gaps and prioritize improvements

---

## The Gap Analysis Process

```
1. Measure → 2. Compare → 3. Prioritize → 4. Plan → 5. Execute
```

---

## Step 1: Measure Current State

### Text Quality Gaps

| Dimension | Current | Target | Gap |
|-----------|---------|--------|-----|
| System Prompt | ? | 7.0+ | ? |
| Domain Knowledge | ? | 7.0+ | ? |
| Workflow | ? | 7.0+ | ? |
| Error Handling | ? | 7.0+ | ? |
| Examples | ? | 7.0+ | ? |
| Metadata | ? | 7.0+ | ? |

### Runtime Quality Gaps

| Dimension | Current | Target | Gap |
|-----------|---------|--------|-----|
| Role Immersion | ? | 7.0+ | ? |
| Framework Execution | ? | 7.0+ | ? |
| Output Actionability | ? | 7.0+ | ? |
| Knowledge Accuracy | ? | 7.0+ | ? |
| Long-Conversation Stability | ? | 7.0+ | ? |
| Resilience | ? | 7.0+ | ? |

---

## Step 2: Identify Gap Patterns

### Pattern 1: Foundation Gap
**Symptoms:**
- System Prompt score < 6
- Role Immersion score < 6

**Root Causes:**
- Unclear role definition
- Missing boundaries
- Conflicting guidance

**Fix:** Redefine core identity

---

### Pattern 2: Knowledge Gap
**Symptoms:**
- Domain Knowledge score < 6
- Knowledge Accuracy score < 6

**Root Causes:**
- Insufficient research
- Outdated information
- Superficial coverage

**Fix:** Deepen expertise

---

### Pattern 3: Execution Gap
**Symptoms:**
- Workflow score < 6
- Framework Execution score < 6

**Root Causes:**
- Unclear process
- Missing steps
- Poor organization

**Fix:** Define clear workflow

---

### Pattern 4: Robustness Gap
**Symptoms:**
- Error Handling score < 6
- Resilience score < 6

**Root Causes:**
- No edge case consideration
- Missing error scenarios
- Fragile design

**Fix:** Add comprehensive error handling

---

### Pattern 5: Usability Gap
**Symptoms:**
- Examples score < 6
- Output Actionability score < 6

**Root Causes:**
- Few/no examples
- Vague outputs
- Hard to apply

**Fix:** Add concrete examples

---

### Pattern 6: Stability Gap
**Symptoms:**
- Long-Conversation Stability score < 6

**Root Causes:**
- Context loss
- Quality degradation
- Inconsistency

**Fix:** Strengthen context management

---

## Step 3: Prioritize Fixes

### Priority Matrix

| Impact | Effort | Priority | Action |
|--------|--------|----------|--------|
| High | Low | **P0** | Do first |
| High | High | **P1** | Plan carefully |
| Low | Low | **P2** | Quick wins |
| Low | High | **P3** | Defer |

### Example Prioritization

```
Dimension       Current  Target  Gap   Impact  Effort  Priority
System Prompt   5/10     7/10    2     High    Low     P0
Examples        4/10     7/10    3     High    Low     P0
Error Handling  5/10     7/10    2     Med     Med     P1
Workflow        6/10     8/10    2     Med     High    P1
```

---

## Step 4: Create Improvement Plan

### Plan Template

```markdown
## Improvement Plan: [Skill Name]

### Goal
Reach [target score] from [current score]

### P0 Actions (This Week)
- [ ] Fix 1: [Specific action]
- [ ] Fix 2: [Specific action]

### P1 Actions (Next 2 Weeks)
- [ ] Enhancement 1: [Specific action]
- [ ] Enhancement 2: [Specific action]

### P2 Actions (If Time Permits)
- [ ] Polish 1: [Specific action]

### Success Criteria
- [ ] All dimensions ≥ 7.0
- [ ] No dimension < 6.0
- [ ] Variance < 1.0
```

---

## Step 5: Execute and Validate

### Quick Validation (After Each Fix)
```
1. Make change
2. Self-assess affected dimension
3. Verify improvement
4. Move to next fix
```

### Full Validation (After All Fixes)
```
1. Complete re-evaluation
2. Compare before/after
3. Verify targets met
4. Document lessons
```

---

## Common Gap Fixes

### System Prompt Gaps
| Issue | Fix |
|-------|-----|
| Vague role | Add specific expertise + experience level |
| No boundaries | Add "What I don't do" section |
| Conflicting guidance | Review for consistency |

### Domain Knowledge Gaps
| Issue | Fix |
|-------|-----|
| Too shallow | Add technical depth |
| Outdated | Update to current practices |
| Inaccurate | Research and correct |

### Workflow Gaps
| Issue | Fix |
|-------|-----|
| Missing steps | Add numbered workflow |
| Unclear entry | Define trigger detection |
| No validation | Add checkpoints |

### Error Handling Gaps
| Issue | Fix |
|-------|-----|
| No errors covered | Brainstorm 5 common failures |
| Generic messages | Make specific and actionable |
| No recovery | Add "How to fix" for each error |

---

## Gap Analysis Example

```
Skill: PDF Rotator (Lite)

Current Scores:
  System Prompt: 8/10 ✅
  Domain Knowledge: 7/10 ✅
  Workflow: 6/10 ⚠️
  Error Handling: 4/10 ❌
  Examples: 7/10 ✅
  Metadata: 8/10 ✅

Overall: 6.7/10
Target: 7.0+

Gap Analysis:
1. Error Handling (Gap: 3 points) - P0
   - Missing: Password protection error
   - Missing: Corrupted file error
   - Fix: Add 2-3 error scenarios

2. Workflow (Gap: 1 point) - P1
   - Unclear: Step 2 details
   - Fix: Expand validation step

Improvement Plan:
P0: Add error handling section (30 min)
P1: Clarify workflow step 2 (15 min)

Expected Result: 7.5/10
```

---

## Quick Gap Checklist

**Text Quality:**
- [ ] System Prompt clear and specific?
- [ ] Domain knowledge accurate and deep?
- [ ] Workflow has clear steps?
- [ ] Error handling covers common cases?
- [ ] Examples demonstrate usage?
- [ ] Metadata complete?

**Runtime Quality:**
- [ ] Stays in character consistently?
- [ ] Uses frameworks correctly?
- [ ] Output is actionable?
- [ ] Knowledge is accurate?
- [ ] Stable over long conversations?
- [ ] Handles edge cases gracefully?

---

**Lines:** ~200 | Load when diagnosing skill issues
