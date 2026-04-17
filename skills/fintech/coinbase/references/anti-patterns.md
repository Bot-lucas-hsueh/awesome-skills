## § 6 — Anti-Patterns

### 6.1 Critical Anti-Patterns

| # | Anti-Pattern | ❌ Wrong | ✅ Right | Severity |
|---|--------------|----------|----------|----------|
| 1 | **Single-sig custody** | CEO has full key access | Multi-sig with geographic distribution | 🔴 Critical |
| 2 | **Compliance as checkbox** | "We'll add KYC later" | Compliance-first from day one | 🔴 Critical |
| 3 | **Hot wallet overexposure** | 50% in hot wallets | 98% cold, 2% hot maximum | 🔴 Critical |
| 4 | **Opaque operations** | "Trust us, we're secure" | Public attestations, transparency reports | 🔴 High |
| 5 | **Feature before security** | Ship fast, fix later | Security review gates all deployments | 🔴 High |
| 6 | **No disaster recovery** | Single region deployment | Multi-region, tested failover | 🟡 Medium |
| 7 | **Ignoring regulatory changes** | Wait for enforcement | Proactive engagement, legal review | 🟡 Medium |
| 8 | **Mission drift** | Chasing short-term revenue | Focus on economic freedom | 🟡 Medium |

---
