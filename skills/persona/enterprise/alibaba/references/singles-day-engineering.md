# Singles' Day (双11) Engineering

> How Alibaba engineers for the world's largest shopping event: 540B+ RMB GMV, 1B+ users, and systems handling millions of transactions per second.

---

## The Scale of 11.11

### 2024 Singles' Day Metrics

| Metric | Value |
|--------|-------|
| **GMV** | ¥540+ billion (~$75B USD) |
| **Participating Brands** | 290,000+ |
| **New Products Launched** | 10M+ |
| **Livestream Views** | 300M+ |
| **88VIP Members Active** | 42M+ |
| **Orders Processed** | 1B+ |
| **Peak Transactions/Second** | 583,000 |
| **Logistics Packages** | 2B+ shipped |

### Historical Growth

```
2009:  ¥50M    █
2010:  ¥900M   ██
2011:  ¥5.2B   ████
2012:  ¥19B    ████████
2013:  ¥35B    ██████████████
2014:  ¥57B    ██████████████████████
2015:  ¥91B    ███████████████████████████████
2016:  ¥120B   ████████████████████████████████████████
2017:  ¥168B   ██████████████████████████████████████████████████
2018:  ¥213B   ████████████████████████████████████████████████████████████
2019:  ¥268B   ████████████████████████████████████████████████████████████████████████
2020:  ¥498B   ██████████████████████████████████████████████████████████████████████████████████████████████████████
2021:  ¥540B+  ████████████████████████████████████████████████████████████████████████████████████████████████████████████████
```

---

## Engineering for Peak Scale

### The Challenge

Normal day traffic: ████████ (100%)
Singles' Day peak: ████████████████████████████████████████████████████████████████████████████ (1000%+)

```
Problem: Building for 10x normal capacity is wasteful 364 days/year
Solution: Elastic architecture + aggressive pre-warming + graceful degradation
```

---

## Architecture Strategies

### 1. Elastic Infrastructure

```
Pre-Event (30 days):        Event Day (Peak):
┌──────────────┐           ┌──────────────────────────────┐
│  1,000 VMs   │   ───►    │      100,000+ VMs            │
│  Standard    │           │  Auto-scaled across regions  │
└──────────────┘           └──────────────────────────────┘

Scale-out triggers:
- CPU > 60% for 2 minutes → Add 50 instances
- Queue depth > 1000 → Add 100 consumers
- Latency P99 > 100ms → Add read replicas
```

### 2. Multi-Level Caching Strategy

```
User Request
     │
     ▼
┌─────────────┐  Hit: 80%   ┌─────────────┐
│  CDN Edge   │────────────►│ Static Page │
└──────┬──────┘             └─────────────┘
       │ Miss
       ▼
┌─────────────┐  Hit: 15%   ┌─────────────┐
│   Nginx     │────────────►│ Cached HTML │
│   Cache     │             │ (5min TTL)  │
└──────┬──────┘             └─────────────┘
       │ Miss
       ▼
┌─────────────┐  Hit: 4%    ┌─────────────┐
│  Redis      │────────────►│ API Response│
│  Cluster    │             │ (1min TTL)  │
└──────┬──────┘             └─────────────┘
       │ Miss
       ▼
┌─────────────┐             ┌─────────────┐
│ Application │────────────►│ Dynamic     │
│   Logic     │             │ Generate    │
└─────────────┘             └─────────────┘
```

### 3. Database Sharding Strategy

```
Before 11.11:
┌─────────────────┐
│   Single DB     │
│   (Read Replicas)│
└─────────────────┘

During 11.11:
┌─────────┬─────────┬─────────┐
│ Shard 1 │ Shard 2 │ Shard 3 │ ... 1024 shards
│ Users   │ Users   │ Users   │
│ 0-1M    │ 1M-2M   │ 2M-3M   │
└────┬────┴────┬────┴────┬────┘
     │         │         │
     └─────────┼─────────┘
               ▼
        ┌─────────────┐
        │  DB Proxy   │
        │ (Auto-route)│
        └─────────────┘
```

### 4. Async Processing Pipeline

```
Order Creation Flow:

User Click ──► API Gateway ──► Order Service ──► Kafka
                                                    │
                    ┌───────────────────────────────┼───────────────┐
                    │                               │               │
                    ▼                               ▼               ▼
            ┌──────────────┐              ┌──────────────┐ ┌──────────────┐
            │ Inventory    │              │ Payment      │ │ Notification │
            │ Consumer     │              │ Consumer     │ │ Consumer     │
            │ (Immediate)  │              │ (Async)      │ │ (Async)      │
            └──────────────┘              └──────────────┘ └──────────────┘
```

---

## The Preparation Timeline

### T-90 Days: Planning

```
┌─────────────────────────────────────────────────────────────┐
│ CAPACITY PLANNING                                           │
│ • Forecast traffic based on marketing spend                 │
│ • Identify system bottlenecks from previous year            │
│ • Plan infrastructure budget (temporary capacity)           │
└─────────────────────────────────────────────────────────────┘
```

### T-60 Days: Architecture Review

| System | Action | Owner |
|--------|--------|-------|
| Core Transaction | Stress test at 3x expected peak | Platform Team |
| Payment | Bank integration capacity check | Ant Group |
| Search | Index optimization, query plan review | AI Team |
| Recommendations | Model pre-computation | ML Team |
| Logistics | Carrier capacity reservation | Cainiao |

### T-30 Days: Pre-Warming

```
Cache Pre-Warming Strategy:

1. Hot Item Cache
   - Identify top 100K SKUs from historical data
   - Pre-load product details, inventory, pricing
   - 99.9% cache hit rate target

2. User Profile Cache
   - Pre-compute recommendations for active users
   - Cache user preferences, addresses, payment methods

3. Search Index Optimization
   - Freeze index updates 24h before event
   - Pre-compute popular query results
```

### T-7 Days: War Room Setup

```
┌─────────────────────────────────────────────────────────────┐
│                    COMMAND CENTER                           │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐              │
│  │ System     │ │ Business   │ │ Logistics  │              │
│  │ Health     │ │ Metrics    │ │ Tracking   │              │
│  │ Dashboard  │ │ Dashboard  │ │ Dashboard  │              │
│  └────────────┘ └────────────┘ └────────────┘              │
│                                                             │
│  Teams On-Site:                                             │
│  • Platform Engineering (24/7 rotation)                     │
│  • Database Administration                                  │
│  • Network Operations                                       │
│  • Security Operations                                      │
│  • Business Operations                                      │
└─────────────────────────────────────────────────────────────┘
```

### T-0: Event Day

```
Countdown to Midnight (GMT+8):

23:30:00 - All hands on deck
23:45:00 - Final system health check
23:50:00 - Disable non-critical jobs
23:55:00 - Activate all circuit breakers
00:00:00 - 🚀 GO LIVE!

First 5 minutes: Most critical
- 50M+ users simultaneously accessing deals
- Flash sale items sell out in seconds
- Payment systems face 10x normal load
```

---

## Degradation Strategy

### Graceful Degradation Levels

| Level | Trigger | Action |
|-------|---------|--------|
| **Green** | Normal load | Full functionality |
| **Yellow** | 80% capacity | Disable non-critical features |
| **Orange** | 90% capacity | Static fallbacks, simplified UI |
| **Red** | 95% capacity | Essential functions only (browse, buy, pay) |
| **Black** | System failure | Static "we'll be back" page |

### Feature Degradation Priority

```
P0 (Never Degrade):
├── Product browsing
├── Search (basic)
├── Add to cart
├── Checkout
└── Payment processing

P1 (Degrade if necessary):
├── Real-time inventory
├── Personalized recommendations
├── Reviews (show cached)
└── Live chat

P2 (First to degrade):
├── Analytics
├── Admin dashboards
├── Reporting
└── Non-essential APIs
```

---

## Chaos Engineering

### Pre-Event Failure Testing

```
Weekly Chaos Drills (8 weeks before):

Week 1: Single server failure
Week 2: Database replica failure
Week 3: Cache cluster failure
Week 4: Network partition
Week 5: Region failure simulation
Week 6: Dependency service failure
Week 7: Cascading failure scenario
Week 8: Full disaster recovery test
```

### Failure Injection Points

| Component | Failure Mode | Expected Response |
|-----------|--------------|-------------------|
| Redis | Node failure | Automatic failover, <5s impact |
| MySQL | Master failure | Promote replica, <30s impact |
| Service | Pod crash | Kubernetes restart, <10s impact |
| Network | Latency spike | Circuit breaker opens |
| External API | Timeout | Fallback to cached data |

---

## Key Lessons

### Technical Lessons

1. **Scale Horizontally**: No single point of failure
2. **Cache Aggressively**: Every cache hit is a database save
3. **Decouple Everything**: Async processing buys you resilience
4. **Test Failure**: Chaos engineering builds confidence
5. **Measure Everything**: If you can't measure it, you can't optimize it

### Organizational Lessons

1. **War Room Culture**: Bring teams together physically for crisis
2. **Clear Escalation**: Pre-defined decision makers for every scenario
3. **Celebrate Wins**: Acknowledge the heroic effort
4. **Post-Mortem**: Document learnings for next year

---

## The Human Element

### The Cost of 11.11

- Engineers sleep in office for days
- Family time sacrificed
- Health impacts from stress and sleep deprivation

### Modern Evolution

Alibaba has evolved to reduce human toll:
- Better automation reduces manual intervention
- Improved architecture reduces firefighting
- Cultural shift toward sustainable engineering

---

## Reference: System Architecture During 11.11

```
┌─────────────────────────────────────────────────────────────────┐
│                        GLOBAL TRAFFIC                          │
│                     (DDoS Protection)                          │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────┴─────────────────────────────────────┐
│                        CDN LAYER                                 │
│           (Static content, edge caching)                        │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────┴─────────────────────────────────────┐
│                     LOAD BALANCERS                               │
│              (Global Server Load Balancing)                     │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────┴─────────────────────────────────────┐
│                   APPLICATION LAYER                              │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐  │
│  │ Search  │ │ Product │ │  Cart   │ │  Order  │ │ Payment │  │
│  │ Service │ │ Service │ │ Service │ │ Service │ │ Service │  │
│  │ (1000+) │ │ (500+)  │ │ (200+)  │ │ (300+)  │ │ (200+)  │  │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘  │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────┴─────────────────────────────────────┐
│                     DATA LAYER                                   │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐               │
│  │  Redis  │ │OceanBase│ │  HBase  │ │  OSS    │               │
│  │ (Cache) │ │  (OLTP) │ │(BigData)│ │(Storage)│               │
│  │ 1000+   │ │ 100+    │ │ 50+     │ │ Global  │               │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘               │
└─────────────────────────────────────────────────────────────────┘
```

---

**Reference Version**: 1.0.0 | **Last Updated**: 2026-03-21
