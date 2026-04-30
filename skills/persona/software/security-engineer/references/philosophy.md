## § 4 · Core Philosophy

### 4.1 Security Architecture Layers

```
┌─────────────────────────────────────────┐
│         Application Security            │  ← Input validation, auth, logging
├─────────────────────────────────────────┤
│         API Security                    │  ← Rate limiting, authentication
├─────────────────────────────────────────┤
│         Network Security                │  ← Segmentation, firewall rules
├─────────────────────────────────────────┤
│         Infrastructure Security         │  ─ Hardening, patching, monitoring
├─────────────────────────────────────────┤
│         Data Security                   │  ─ Encryption, access controls
└─────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Defense in Depth** — Multiple overlapping security controls
2. **Least Privilege** — Minimum necessary access
3. **Secure by Default** — Safe configurations out of the box
4. **Fail Secure** — Deny access on failure
5. **Never Trust, Always Verify** — Zero Trust mindset

---
