# Common Pitfalls & Anti-Patterns

## 10.1 High-Severity Anti-Patterns

### 🔴 Anti-Pattern 1: Copying Existing Skills Without Improvement
```
❌ BAD: Submitting skill that's 90% identical to existing skill with just name changed
✅ GOOD: Add genuine new capability; find gaps the repository doesn't fill
```
**Why it matters**: Duplicate skills confuse users; maintainers will reject near-duplicates.

### 🔴 Anti-Pattern 2: Overclaiming Quality Score
```
❌ BAD: Basic skill with generic content claiming "Exemplary 9.5/10"
✅ GOOD: Self-assess honestly using rubric; quality score helps users find good skills
```
**Why it matters**: Users rely on quality scores; misleading scores erode trust.

### 🔴 Anti-Pattern 3: Including Placeholder URLs
```
❌ BAD: Adding "https://example.com/docs" as a real resource
✅ GOOD: Replace all placeholders with actual, verifiable resources
```
**Why it matters**: Broken links fail CI and frustrate users; fake URLs are obvious.

### 🔴 Anti-Pattern 4: Incomplete Section Templates
```
❌ BAD: SKILL.md missing H2 sections (e.g., no Risk Disclaimer or Workflow)
✅ GOOD: Include all 16 required sections; fill each meaningfully
```
**Why it matters**: Missing sections indicate incomplete skills; reviewers will request additions.

## 10.2 Medium-Severity Anti-Patterns

### 🟡 Anti-Pattern 5: Generic System Prompts
```
❌ BAD: "You are a helpful AI assistant" as entire system prompt
✅ GOOD: Detailed role definition with specific expertise, methodology, and constraints
```

### 🟡 Anti-Pattern 6: Ignoring Reviewer Feedback
```
❌ BAD: Responding to review with "I disagree, merging anyway"
✅ GOOD: Address feedback seriously; discuss if you disagree with reasoning
```

### 🟡 Anti-Pattern 7: Version Not Updated on Changes
```
❌ BAD: Making significant changes without bumping version number
✅ GOOD: Update version in frontmatter per semantic versioning guidelines
```

### 🟡 Anti-Pattern 8: Using HTML in YAML Frontmatter
```
❌ BAD: <img src="..."> inside YAML frontmatter block
✅ GOOD: Use markdown images or external hosting; YAML must be valid
```

## 10.3 Best Practices Checklist

### Before Submission
- [ ] All 16 H2 sections present and complete
- [ ] YAML frontmatter valid (no HTML, proper formatting)
- [ ] Quality score self-assessed honestly
- [ ] All placeholder URLs replaced with real resources
- [ ] Reference files added (minimum 4)
- [ ] Run local linting tools

### During Review
- [ ] Respond to comments promptly
- [ ] Make requested changes
- [ ] Ask clarifying questions if feedback is unclear
- [ ] Don't take feedback personally

### After Merge
- [ ] Delete feature branch
- [ ] Verify skill appears in repository
- [ ] Test skill functionality
- [ ] Monitor for any reported issues

## 10.4 Red Flags to Watch For

| Red Flag | Risk Level | Action |
|----------|------------|--------|
| Quality score >8.5 with generic content | High | Request re-assessment using rubric |
| All resources pointing to one site | Medium | Verify resources are actually helpful |
| System prompt <200 characters | High | Require detailed role definition |
| No trigger words defined | Medium | Add specific triggering phrases |
| Category doesn't match content | High | Re-assign to appropriate category |