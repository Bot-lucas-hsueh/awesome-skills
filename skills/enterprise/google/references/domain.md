## §2. Domain Knowledge

### §2.1 Google Products & Engineering Scale (2025-2026)

| Product | Users | Engineering Org | Key Metrics |
|---------|-------|-----------------|-------------|
| **Search** | 4.2B+ | Amber, Core Search | 99% relevance, <100ms latency |
| **YouTube** | 2.5B+ MAU | YouTube Engineering | 500hrs uploaded/min, 1B hours watched/day |
| **Android** | 3B+ devices | Android Platform | <0.5% malware rate, monthly patches |
| **Chrome** | 3.4B users | Chrome Team | 65%+ browser market share |
| **Cloud** | 2M+ customers | Google Cloud | $48B ARR, 30%+ YoY growth |
| **Gemini** | 100M+ subscribers | Google DeepMind | 2.5 Flash/Pro, 1M token context |
| **Maps** | 1B+ users | Geo/Maps | 220+ countries, real-time navigation |
| **Workspace** | 3B+ accounts | Workspace | Gmail, Docs, Drive, Meet at scale |

### §2.2 Technical Excellence at Google Scale

**Infrastructure Principles:**
- **Global Distribution**: Data centers on every continent, 10-50ms latency globally
- **Horizontal Scaling**: Everything stateless; state in Spanner, Bigtable, Colossus
- **99.99% Uptime**: SRE-engineered SLAs; error budgets drive release cadence
- **Toil Reduction**: SRE target <50% on-call toil; automation over manual intervention

**Data & Experimentation:**
- **A/B Testing**: All significant product changes tested; 100K-1M+ user samples typical
- **Metrics Infrastructure**: Internal A/B platform, leaderboard of metrics
- **Statistical Rigor**: p-value <0.05, minimum detectable effect defined upfront
- **Launch Gates**: Metrics (engagement, retention, revenue) must move positively

**Development Practices:**
- **Monorepo**: 2B+ lines of code in google3; Bazel for build
- **Code Review**: Every CL requires ≥1 reviewer; 24hr turnaround SLA
- **Testing**: Unit (>80% coverage), integration, canary (prod shadow)
- **Rollback < 30min**: Every change must be reversible within 30 minutes
- **On-call**: Rotations with blameless postmortem culture; SHARP program

### §2.3 Google-Specific Engineering Concepts

| Concept | Definition | Application |
|---------|-----------|-------------|
| **TTF (Time to Fry)** | How long before a system fails at scale | Design for 10× headroom |
| **Tooth-to-Tail Ratio** | % time creating value vs. overhead | Target >70% productive time |
| **Error Budget** | Allowed failure room for SLO | Spend budget on shipping; protect on reliability |
| **Blameless Postmortem** | Root cause analysis without blame | Learn from failures; no punishment |
| **Rollout Gates** | Staged release with metric checks | 1% → 10% → 50% → 100% |
| **Dogfooding** | Internal users test first | 100K+ internal users for early feedback |
| **Tech Debt Tuesday** | Dedicated time to address debt | 20% of sprint time |
| **Googler Mobility** | Internal transfer culture | Ping-pong team mobility encouraged |

---
