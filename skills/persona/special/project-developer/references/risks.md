## § 3 · Risk Disclaimer

| Risk| Severity| Description| Mitigation|
|------------|-----------------|-------------------|---------------------|
| **Quality Drift** | 🔴 High | Skills merged with score <9.0 dilute repository quality | Auto-block merge if score <9.0; require explicit exemption |
| **Scope Creep** | 🔴 High | New skill expands to 2+ domains | Reject; require single-domain scope |
| **Broken Links** | 🟡 Medium | References to non-existent files/sections | CI check with link validator |
| **Metadata Errors** | 🟡 Medium | Invalid YAML or missing required fields | Pre-commit yamllint hook |
| **Token Overflow** | 🟢 Low | SKILL.md >500 lines causes slow loads | Lint for line count; offload to references/ |

---
