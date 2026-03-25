## § 9 · Scenario Examples

### Scenario 1: Initial Consultation

**Context:** A new client needs guidance on skill evaluator.

**User:** "I'm new to this and need help with [problem]. Where do I start?"

**Expert:** Welcome! Let me help you navigate this challenge.

**Assessment:**
- Current experience level?
- Immediate goals and constraints?
- Key stakeholders involved?

**Roadmap:**
1. **Phase 1:** Discovery & Assessment
2. **Phase 2:** Strategy Development
3. **Phase 3:** Implementation
4. **Phase 4:** Review & Optimization

---

### Scenario 2: Problem Resolution

**Context:** Urgent skill evaluator issue needs attention.

**User:** "Critical situation: [problem]. Need solution fast!"

**Expert:** Let's address this systematically.

**Triage:**
- Impact: [Critical/High/Medium]
- Timeline: [Immediate/24h/Week]
- Reversibility: [Yes/No]

**Options:**
| Option | Approach | Risk | Timeline |
|--------|----------|------|----------|
| Quick | Immediate fix | High | 1 day |
| Standard | Balanced | Medium | 1 week |
| Complete | Thorough | Low | 1 month |

---

### Scenario 3: Strategic Planning

**Context:** Build long-term skill evaluator capability.

**User:** "How do we become world-class in this area?"

**Expert:** Here's an 18-month roadmap.

**Phase 1 (M1-3): Foundation**
- Baseline assessment
- Quick wins identification
- Infrastructure setup

**Phase 2 (M4-9): Acceleration**
- Core system implementation
- Team upskilling
- Process standardization

**Phase 3 (M10-18): Excellence**
- Advanced methodologies
- Innovation pipeline
- Knowledge leadership

**Metrics:**
| Dimension | 6 Mo | 12 Mo | 18 Mo |
|-----------|------|-------|-------|
| Efficiency | +20% | +40% | +60% |
| Quality | -30% | -50% | -70% |

---

### Scenario 4: Quality Assurance

**Context:** Deliverable requires quality verification.

**User:** "Can you review [deliverable] before delivery?"

**Expert:** Conducting comprehensive quality review.

**Checklist:**
- [ ] Requirements aligned
- [ ] Standards compliant
- [ ] Best practices applied
- [ ] Documentation complete

**Gap Analysis:**
| Aspect | Current | Target | Action |
|--------|---------|--------|--------|
| Completeness | 80% | 100% | Add X |
| Accuracy | 90% | 100% | Fix Y |

**Result:** ✓ Ready for delivery

---

## Anti-Patterns

❌ **Rating by Feel** - Use rubric, not intuition  
❌ **Text Only** - Always test runtime  
❌ **Ignoring Variance** - Investigate >2.0 point gaps  
❌ **Missing Critical Dimensions** - Any <6 = fail  
❌ **Quick Fix Syndrome** - Find root cause first  

## Content Validation Checklist

When evaluating skills, check for these structural issues:

| Issue | Severity | How to Check |
|-------|----------|--------------|
| Platform Support section | 🔴 High | Search for "Platform Support" or installation tables - should not exist |
| Installation instructions | 🔴 High | Search for "Install", "Quick Install" - should be in frontmatter only |
| Version history | 🟡 Medium | Search for "Version History", "Changelog" - should not exist |
| License & Author section | 🟡 Medium | Search for "§ 16" or "License & Author" - should only be in frontmatter |
| Triggers/Works with lines | 🟡 Medium | Should not appear after frontmatter |
| Duplicate description | 🟡 Medium | Description should not repeat in body |

**Note:** Skills should be platform-agnostic following AgentSkills spec. Installation is standardized across Claude, Codex, Cursor, Kimi, OpenCode, and OpenClaw.

---

**Version:** 2.1.0  
**Quality:** Exemplary  
**Lines:** < 300 (Enterprise standard)  
**Last Updated:** 2026-03-21

