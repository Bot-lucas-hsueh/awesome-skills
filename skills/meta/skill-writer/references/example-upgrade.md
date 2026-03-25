# Example 5: Upgrade Skill (6.0→9.5)

## Context

Existing skill scores 6.0/10. Need to upgrade to EXEMPLARY 9.5/10.

## Initial Assessment

**Current State**:
- Score: 6.0/10
- Lines: 680 (too long for content)
- System Prompt: Has generic "expert assistant" role
- Missing §1.2/1.3
- Generic content throughout
- Flat structure (no references/)
- 2 examples (need 5)

## Upgrade Process

### Phase 1: Diagnosis (15 min)

**Issues Identified**:
1. No §1.1/1.2/1.3 structure
2. Generic: "professional consultant", "best practices"
3. Flat structure - all content in one file
4. Insufficient examples
5. Weak Done/Fail criteria

### Phase 2: Research (45 min)

**Domain Research**:
- Company: McKinsey & Company (2024 revenue: $15B, 30,000 employees)
- Methodology: McKinsey 7-S Framework (7 elements, 32-step assessment)
- Tool: Tableau (2024.1, $75/user/month)
- Benchmark: Top consulting firms deliver 85%+ strategy success

### Phase 3: Architecture (20 min)

**New Structure**:
- SKILL.md: 280 lines, navigation-focused
- references/: 15 files, 2500+ lines
- §1.1/1.2/1.3: Complete System Prompt
- 5 Examples: Detailed scenarios

### Phase 4: Progressive Disclosure (15 min)

**Created Files**:
- references/domain-knowledge.md
- references/thinking-patterns.md
- references/examples-*.md (5 files)
- references/sop-*.md (4 files)

### Phase 5: Content Production (90 min)

**Changes Made**:
1. **System Prompt**: Added §1.1/1.2/1.3 with specific data
2. **Domain Knowledge**: Replaced generics with McKinsey data
3. **Workflow**: Strengthened Done/Fail criteria
4. **Examples**: Added 3 new detailed scenarios
5. **Anti-patterns**: Added 8 specific mistakes

### Phase 6: Validation (20 min)

**Self-Check Results**:
- System Prompt: 10/10 ✓
- Domain Knowledge: 9/10 ✓
- Workflow: 9/10 ✓
- Error Handling: 9/10 ✓
- Examples: 10/10 ✓
- Metadata: 10/10 ✓
- **Final Score: 9.5/10** ✓

## Final State

| Metric | Before | After |
|--------|--------|-------|
| Overall Score | 6.0 | 9.5 |
| Lines (SKILL.md) | 680 | 280 |
| Reference Files | 0 | 15 |
| Examples | 2 | 5 |
| System Prompt | Generic | §1.1/1.2/1.3 |
| Content | Generic | Specific data |

## Key Improvements

1. **Structure**: Flat → Progressive disclosure
2. **System Prompt**: Generic → §1.1/1.2/1.3
3. **Content**: Generic → McKinsey/BCG data
4. **Examples**: 2 → 5 detailed scenarios
5. **Quality**: 6.0 → 9.5 EXEMPLARY
