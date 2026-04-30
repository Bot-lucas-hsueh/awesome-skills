## § 3 · Risk Documentation

### Risk Matrix

| Risk | Severity | Likelihood | Impact | Mitigation | Verification |
|------|----------|------------|--------|------------|--------------|
| Overly permissive access | 🔴 Critical | Medium | High | Least privilege principle; regular audits | Quarterly permission review |
| Force-push on main branches | 🔴 Critical | Low | Critical | Block force-push on protected branches | Template enforcement check |
| Missing audit trail | 🔴 Critical | Medium | High | Maintain change history on refs/meta/config | Git log verification |
| Anonymous read on private repos | 🔴 Critical | High | Critical | Restrict to Registered Users group | Access test from unauthenticated session |
| Privilege escalation via group nesting | 🟠 High | Low | Critical | Review group inheritance chains | Monthly group audit |
| Unverified permission changes | 🟠 High | Medium | Medium | Test in non-production first | Staging environment validation |
| Group UUID mismatches | 🟡 Medium | Medium | Medium | Verify UUIDs match across environments | UUID consistency check |
| Manifest sync failures | 🟡 Medium | Low | Medium | Check permissions on manifest repo | Repo sync test |
| Stale group memberships | 🟡 Medium | High | Low | Automated offboarding workflow | Weekly membership review |
| Broken inheritance chains | 🟢 Low | Low | Medium | Document parent-child relationships | Inheritance verification script |

### Risk Acceptance Criteria

- 🔴 **Critical**: Must have mitigation in place; no exceptions
- 🟠 **High**: Mitigation required; temporary exceptions with approval only
- 🟡 **Medium**: Mitigation recommended; monitor and review
- 🟢 **Low**: Acceptable risk; document and proceed

---
