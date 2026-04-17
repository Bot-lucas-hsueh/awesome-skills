## §2. Domain Knowledge

### §2.1 ByteDance Products & Engineering Scale (2025-2026)

| Product | Users | Engineering Org | Key Metrics |
|---------|-------|-----------------|-------------|
| **TikTok** | 1.5B+ MAU | Global Tech | 10B+ videos/day, 1M+ creators, 52min avg session |
| **Douyin** | 700M+ DAU | China Tech | 120min avg daily time, $100B+ GMV in e-commerce |
| **Lark** | 20M+ paying | Enterprise Tech | 30M+ workspace, B2B SaaS focus |
| **CapCut** | 500M+ users | Creator Tech | #1 mobile video editor globally |
| **Resso** | 40M+ MAU | Music Tech | Social music streaming, emerging markets |
| **GOGO** | 10M+ DAU | Gaming Tech | Mobile gaming expansion |
| **AI Studio** | 100M+ users | AI Lab | AI content generation, Streamer Center |

### §2.2 Technical Excellence at ByteDance Scale

**Infrastructure Principles:**
- **Global Distribution**: China (Douyin) + Global (TikTok) with separate compliance stacks
- **Microservices**: 5000+ services, service mesh, 1000+ deployments/day
- **CICD Excellence**: Sub-30min rollback, feature flags for every change
- **Data Infrastructure**: Petabyte-scale data lake, million QPS feature store
- **Recommendation Engine**: Real-time feature pipeline, 30-min model refresh

**Data & Experimentation:**
- **AB Testing**: Platform handles 100M+ user experiments simultaneously
- **Granularity Obsession**: Drill into user segments, cohorts, behavioral clusters
- **Metric Hierarchy**: Day 1/7/30 retention → engagement → monetization
- **Algorithmic Loop**: Content → User → Signal → Model → Content (continuous)

**Development Practices:**
- **Rapid Iteration**: 2-week sprints, ship weekly, kill underperformers fast
- **OKR + Weekly Check-ins**: Quarterly OKRs, weekly 1:1 alignment
- **Context-Driven**: Clear context documents, autonomous execution
- **APP Factory**: Treat products as experiments; iterate or kill

### §2.3 ByteDance-Specific Engineering Concepts

| Concept | Definition | Application |
|---------|-----------|-------------|
| **字节范 (ByteStyle)** | ByteDance's cultural DNA: speed, data, context, consensus | Core operating principles |
| **Context Not Control** | Provide context, trust teams; avoid micro-management | Leadership philosophy |
| **APP Factory** | Factory-like product creation: ship fast, evaluate, scale or kill | Product development model |
| **Data Granularity** | Drill into segment-level metrics, not aggregates | Data analysis philosophy |
| **Recommendation Loop** | Continuous cycle: content → user signal → model → content | Algorithmic thinking |
| **CICD at Scale** | 1000+ deployments/day, sub-30min rollback | Engineering velocity |
| **Douyin vs TikTok** | Same core, different content, compliance, features | Multi-product strategy |
| **Kill Metric** | Specific metric that determines product viability | APP Factory decision gate |
| **Streamer Center** | Creator tools, analytics, monetization platform | Creator ecosystem |

---
