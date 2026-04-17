## § 6 — Anti-Patterns

### 6.1 The 10 Critical Anti-Patterns

| # | Anti-Pattern | ❌ Wrong | ✅ Right | Severity |
|---|--------------|----------|----------|----------|
| 1 | **Camera-Only Shortcuts** | "LiDAR is too expensive, cameras are enough" | "LiDAR is essential for safety — optimize cost elsewhere" | 🔴 Critical |
| 2 | **Skip Simulation** | "We tested on roads, we don't need simulation" | "10M simulated miles before any road deployment" | 🔴 Critical |
| 3 | **Single Point of Failure** | "One sensor suite per area" | "Triple redundancy for all critical functions" | 🔴 Critical |
| 4 | **Hide Safety Data** | "Don't publish incident details" | "Transparency builds trust — publish all NHTSA data" | 🔴 High |
| 5 | **Fast-Track Deployment** | "Launch in 30 days to beat competition" | "Safety validation takes time — no shortcuts" | 🔴 High |
| 6 | **Ignore Edge Cases** | "99% coverage is good enough" | "The 1% edge case kills — simulate everything" | 🟡 Medium |
| 7 | **Regulatory Avoidance** | "Better to ask forgiveness than permission" | "Partner with regulators from day one" | 🟡 Medium |
| 8 | **Underestimate Weather** | "It works in California, ship it" | "Validate in snow, rain, dust before expansion" | 🟡 Medium |
| 9 | **Cost Before Safety** | "Cut LiDAR to hit cost target" | "Maintain safety, achieve cost through scale" | 🟡 Medium |
| 10 | **Ignore Public Perception** | "The data speaks for itself" | "Community engagement is essential" | 🟢 Low |

---
