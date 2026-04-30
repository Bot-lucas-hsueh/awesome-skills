## § 2 · Domain Knowledge

### § 2.1 · AT&T Corporate Intelligence

| Metric | Value | Context |
|--------|-------|---------|
| **Annual Revenue** | $122.3B (2024) | Communications segment: $117.7B (97% of total) |
| **Market Cap** | $130B+ | NYSE: T |
| **Employees** | 150,000+ | Global workforce |
| **CEO** | John Stankey | Since July 2020; 40-year AT&T veteran |
| **HQ** | Dallas, Texas | Relocated from San Antonio in 2008 |
| **History** | 140+ years | Traces to Bell Telephone Company (1877), original "Ma Bell" |

**Key Corporate Events:**
- **2015**: DirecTV acquisition ($67B) — satellite TV expansion
- **2018**: Time Warner acquisition ($85B) — content/media vertical integration
- **2021**: DirecTV spinoff (70% stake to TPG) — focus on core connectivity
- **2022**: WarnerMedia-Discovery merger ($43B deal) — exit content business
- **2022**: Dividend reduction — prioritize debt reduction and 5G/fiber investment
- **2024**: 7th consecutive year of 1M+ fiber customer additions
- **2025-2029**: $250B infrastructure commitment — accelerate 5G and fiber build

### § 2.2 · AT&T Three-Layer Converged Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  LAYER 1: CUSTOMER EXPERIENCE LAYER                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   5G NSA/SA  │  │  AT&T Fiber  │  │  Fixed       │  │  Converged   │     │
│  │  C-band n77  │  │  GPON/XGS-PON│  │  Wireless    │  │  Bundles     │     │
│  │  mmWave n260 │  │  25M+ passes │  │  (Internet   │  │  Wireless+   │     │
│  │  270M POPs   │  │  9.3M subs   │  │   Air)       │  │  Fiber+Video │     │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘     │
│                    99.9%+ Availability Target                               │
├─────────────────────────────────────────────────────────────────────────────┤
│  LAYER 2: CONVERGED CORE & TRANSPORT                                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │   5G Core    │  │  IP/MPLS     │  │  Fiber       │  │  Edge        │     │
│  │   (5GC)      │  │  Backbone    │  │  Backhaul    │  │  Computing   │     │
│  │  SBA/Cloud   │  │  100G/400G   │  │  Metro/DWDM  │  │  (MEC)       │     │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘     │
│                    Unified IP Network + Automation                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  LAYER 3: SPECTRUM & INFRASTRUCTURE                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  Low-band    │  │  C-band      │  │  mmWave      │  │  FirstNet    │     │
│  │  (coverage)  │  │  (capacity)  │  │  (hotspots)  │  │  (public     │     │
│  │  850 MHz     │  │  3.7-3.98GHz │  │  28/39 GHz   │  │  safety)     │     │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘     │
│                    Licensed Spectrum + FirstNet Partnership                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

### § 2.3 · Six Core Methodologies

1. **连接质量第一 (Connectivity Quality First)**: Network reliability is job #1. Downtime is measured in revenue impact and customer trust lost.
2. **融合战略 (Convergence Strategy)**: Fiber + wireless together creates unbeatable customer value proposition. Bundle economics drive higher lifetime value.
3. **业主经济学 (Owner's Economics)**: Owning infrastructure beats leasing. AT&T's integrated fiber-wireless model delivers cost advantages.
4. **光纤优先 (Fiber-First)**: Fiber is the future. 25M+ locations passed, targeting 30M+ by 2025, 50M by 2029.
5. **铜缆退出 (Copper Exit)**: Aggressive retirement of legacy copper infrastructure. Migrate to fiber or fixed wireless by 2029.
6. **FirstNet优先 (FirstNet Priority)**: Public safety network commitment with dedicated Band 14 spectrum. Mission-critical reliability standard.

### § 2.4 · Platform Support

| Platform | Purpose | Key Metrics | Coverage |
|----------|---------|-------------|----------|
| **5G RAN** | Radio Access Network | Latency <20ms, 1+ Gbps peak | 270M+ POPs (C-band) |
| **AT&T Fiber** | FTTH broadband | Symmetric 1-5Gbps, <5ms latency | 28.9M locations passed |
| **Fixed Wireless** | 5G Home Internet | 100-300 Mbps typical | Expanding nationwide |
| **FirstNet** | Public safety network | 99.99% availability target | 2.8M+ subscribers |
| **IP/MPLS Core** | Converged backbone | <10ms coast-to-coast | 100G/400G DWDM |
| **Edge Compute** | Multi-access Edge | <20ms application latency | 30+ major markets |

### § 2.5 · Professional Toolkit

| Tool/Platform | Purpose |
|---------------|---------|
| **Ericsson ENM** | RAN management and configuration |
| **Cisco NSO** | Network Services Orchestrator for automation |
| **ONAP** | Open Network Automation Platform |
| **ServiceNow ITSM** | Incident, change, and problem management |
| **Splunk/SIEM** | Security monitoring and threat detection |
| **3-GIS/FiberGIS** | Fiber network design and documentation |
| **Airspan/CommScope** | Small cell and DAS management |

### § 2.6 · Standards & Frameworks

| Framework | When to Use | Key Steps |
|-----------|-------------|-----------|
| **5G Deployment** | New market or capacity expansion | 1. Spectrum clearing → 2. Site acquisition → 3. RF design → 4. Installation → 5. Optimization → 6. Launch |
| **Fiber Build Framework** | New market fiber deployment | 1. Market analysis → 2. Design/build → 3. Drop installation → 4. Service activation → 5. Customer acquisition |
| **Copper Migration** | Legacy customer transition | 1. Customer notification → 2. Migration offer → 3. Installation → 4. Service verification → 5. Copper retirement |
| **Incident Response** | Network/service outages | 1. Detect & alert → 2. Assess impact → 3. Engage teams → 4. Execute recovery → 5. Communicate → 6. Post-mortem |

### § 2.7 · Network Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **5G Coverage** | POPs with 5G / Total POPs | >90% (C-band) |
| **Fiber Passings** | Serviceable locations | 28.9M (2024) → 30M (2025) |
| **Postpaid Phone Churn** | Lost customers / Base | <0.9% monthly |
| **Fiber Net Adds** | Quarterly additions | 1M+/year (7 consecutive years) |
| **Network Availability** | Uptime % | 99.9% consumer, 99.999% enterprise |
| **FirstNet Reliability** | Public safety uptime | 99.99% target |

---
