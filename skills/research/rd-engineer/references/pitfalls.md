# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns in R&D

| # | Anti-Pattern| Severity| Quick Fix|
|---|----------------------|-----------------|---------------------|
| 1 | **Specifying tolerances tighter than needed** | 🔴 High | Apply functional tolerance analysis; don't guess |
| 2 | **Designing without manufacturing input** | 🔴 High | Include manufacturing engineer in design reviews from concept |
| 3 | **Skipping DFMEA for safety-critical products** | 🔴 High | Mandatory per IEC 60601, ISO 26262 — no exceptions |
| 4 | **Testing only that it works, not that it can fail** | 🟡 Medium | Add failure mode testing — what happens when it breaks? |
| 5 | **Over-engineering early prototypes** | 🟡 Medium | Prototype to learn, not to perfect — speed beats polish |

## 10.2 Problematic Statements

| ❌ Avoid | ✅ Use Instead |
|----------|----------------|
| "Let's make the tolerance ±0.01mm to be safe." | "Functional analysis shows ±0.05mm meets the assembly requirement. Reducing to ±0.1mm cuts tooling cost 30%." |
| "We'll figure out manufacturing later." | "Manufacturing engineer assigned to project from Day 1" |
| "It works in the lab, let's move to production." | "Design verification complete; production validation needed" |
| "The prototype looks good enough." | "First pass yield was X%; we need Y% to proceed" |

## 10.3 Common R&D Mistakes

### Design Phase
- **Over-specification:** Requirements that exceed customer needs
- **Under-specification:** Missing critical requirements
- **Premature optimization:** Focusing on performance before basics work

### Prototype Phase
- **Analysis paralysis:** Too many variants, not enough learning
- **Perfectionism:** Delaying release for minor improvements
- **Single-prototype dependency:** No backup if prototype fails

### Production Phase
- **Late DFMEA:** Finding failure modes after tooling is built
- **Noisy handoff:** Insufficient documentation for production
- **Untoleranced designs:** Assuming manufacturing will "figure it out"

## 10.4 Quality Checklist

Before design review, verify:
- [ ] All requirements mapped to design inputs
- [ ] DFMEA complete with RPN priorities addressed
- [ ] DFM review completed with manufacturing
- [ ] Tolerance analysis performed
- [ ] Test plan defined for verification and validation
- [ ] Regulatory requirements identified and addressed
- [ ] IP assessment completed
- [ ] Cost target validated with suppliers

## 10.5 Best Practices Summary

1. **Stage-Gate Discipline:** Don't skip gates, even when under pressure
2. **Manufacturing Early:** Engage manufacturing in design, not after
3. **Test to Fail:** Verify failure modes, not just success
4. **Document Everything:** Design intent, decisions, trade-offs
5. **Think Systems:** Consider integration, not just components