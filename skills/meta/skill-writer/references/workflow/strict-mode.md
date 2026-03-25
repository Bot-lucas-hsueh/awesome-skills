# Strict Mode Workflow

> Maximum rigor for safety-critical and public-release skills

**Time:** 1+ days  
**Target Score:** 9.0+  
**Use for:** Safety-critical, public release, organizational standards

---

## When to Use Strict Mode

- Safety-critical (medical, financial, legal, automotive)
- Public/open source release
- Organizational standards
- High consequence of failure
- Regulatory compliance required

---

## Strict vs Standard

| Aspect | Standard | Strict |
|--------|----------|--------|
| Time | 1-2 hours | 1+ days |
| Testing | Self + basic | Comprehensive suite |
| Review | Self | Peer + expert |
| Documentation | Complete | Exemplary |
| Safety review | Optional | Required |
| Compliance | If applicable | Verified |
| Target score | 8.0+ | 9.0+ |

---

## Phase 1: Requirements (2 hours)

### Stakeholder Interviews

Interview key stakeholders:
- Primary users
- Subject matter experts
- Legal/compliance (if applicable)
- Safety reviewers (if applicable)

### Risk Assessment

Document:
- All failure modes
- Impact of each failure
- Mitigation strategies
- Residual risks

### Compliance Mapping

Identify and document:
- Applicable regulations
- Industry standards
- Organizational policies
- Certification requirements

---

## Phase 2: Design Review (2 hours)

### Architecture Review

Present design to peers:
- Structure justification
- Pattern selection
- Reference organization
- Safety considerations

### Feedback Integration

Document and address all feedback.

---

## Phase 3: Development (4 hours)

Same as Standard/Enterprise, with additional:

### Safety Features

```markdown
## Safety Considerations

### Critical Warnings
⚠️ [Warning 1 with consequence]
⚠️ [Warning 2 with consequence]

### Safety Checks
Before proceeding, verify:
- [ ] [Check 1]
- [ ] [Check 2]

### Emergency Procedures
If [critical failure]:
1. [Immediate action]
2. [Notification process]
3. [Documentation requirement]
```

### Compliance Documentation

```markdown
## Compliance

### Regulation X Compliance
- Requirement: [text]
- Implementation: [how skill addresses it]
- Verification: [how to confirm compliance]

### Standard Y Adherence
...
```

---

## Phase 4: Testing (4 hours)

### Test Suite

**1. Functionality Tests**
- All capabilities tested
- Happy path verified
- Edge cases covered

**2. Error Handling Tests**
- Each error scenario triggered
- Recovery paths verified
- Error messages clear

**3. Safety Tests**
- Safety features tested
- Fail-safe behavior verified
- Warnings trigger correctly

**4. Adversarial Tests**
- Malformed inputs
- Attempted misuse
- Boundary conditions

**5. User Simulation**
- New user can use without guidance
- Common mistakes handled gracefully
- Clear next steps always provided

---

## Phase 5: Review (2 hours)

### Peer Review

Minimum 2 reviewers check:
- Technical accuracy
- Completeness
- Safety
- Usability

### Expert Review

Subject matter expert validates:
- Domain knowledge accuracy
- Best practices alignment
- Safety considerations

### Documentation Review

Verify:
- All sections complete
- Examples work
- Cross-references valid
- No ambiguity

---

## Phase 6: Certification (2 hours)

### Final Checklist

- [ ] All tests passing
- [ ] Peer reviews complete
- [ ] Expert sign-off obtained
- [ ] Safety review passed
- [ ] Compliance verified
- [ ] Documentation complete
- [ ] Version tagged

### Release

- Tag version 1.0.0
- Create release notes
- Announce availability

---

## Summary

```
Strict Mode = Standard Mode + Safety + Compliance + Review + Certification
```

**Result:** Production-ready, safety-verified, expert-reviewed skill.

---

**Related:**
- Flexibility Framework → ./flexibility-framework.md
- Standard Workflow → ./standard-workflow.md
- Enterprise Workflow → ./enterprise-workflow.md
