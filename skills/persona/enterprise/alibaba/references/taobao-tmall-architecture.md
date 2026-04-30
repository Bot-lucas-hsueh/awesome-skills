# Taobao & Tmall Architecture

> Architecture patterns from China's largest e-commerce platform handling $1.1 trillion GMV and 960M+ monthly active users.

---

## System Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           TAOBAO/TMALL PLATFORM                             │
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │    Users     │  │   Merchants  │  │  Operations  │  │  Ecosystem   │    │
│  │   ( buyers)  │  │  ( sellers)  │  │   (平台运营)  │  │  (partners)  │    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘    │
│         │                 │                 │                 │            │
│         └─────────────────┴─────────────────┴─────────────────┘            │
│                                   │                                        │
│                    ┌──────────────┴──────────────┐                        │
│                    │      Unified Gateway        │                        │
│                    │   (Traffic management,      │                        │
│                    │    authentication, routing) │                        │
│                    └──────────────┬──────────────┘                        │
│                                   │                                        │
│  ┌────────────────────────────────┼────────────────────────────────┐      │
│  │                    CORE SERVICES LAYER                          │      │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │      │
│  │  │  Product │ │   Order  │ │ Payment  │ │  Search  │          │      │
│  │  │  Service │ │  Service │ │  Service │ │  Service │          │      │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │      │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │      │
│  │  │  User    │ │Inventory │ │  Promo   │ │Recommend │          │      │
│  │  │  Service │ │  Service │ │  Service │ │  Service │          │      │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │      │
│  └────────────────────────────────┼────────────────────────────────┘      │
│                                   │                                        │
│  ┌────────────────────────────────┼────────────────────────────────┐      │
│  │                    DATA LAYER                                     │      │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │      │
│  │  │  MySQL   │ │   Redis  │ │  MongoDB │ │  HBase   │          │      │
│  │  │ (OLTP)   │ │  (Cache) │ │(Document)│ │ (Big Data)│         │      │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │      │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐                        │      │
│  │  │   Kafka  │ │  Flink   │ │ MaxCompute│ (Data processing)     │      │
│  │  │ (Events) │ │(Stream)  │ │ (Analytics)│                      │      │
│  │  └──────────┘ └──────────┘ └──────────┘                        │      │
│  └─────────────────────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Scale Metrics

| Metric | Value |
|--------|-------|
| **Peak QPS** | 500M+ queries/second (Singles' Day) |
| **Daily Orders** | 100M+ (normal), 1B+ (11.11) |
| **Product SKUs** | 1+ billion |
| **Concurrent Users** | 100M+ (peak) |
| **Data Volume** | 100+ PB daily |
| **Search Queries/Day** | 1+ billion |

---

## Architecture Patterns

### 1. Horizontal Sharding

Database sharding by user ID hash:

```
User ID: 123456789
Hash: 123456789 % 1024 = 789
Shard: db-789.cluster.taobao.com
```

**Sharding Strategy:**

| Entity | Shard Key | Shard Count |
|--------|-----------|-------------|
| Users | user_id | 1024 |
| Orders | order_id | 4096 |
| Products | product_id | 512 |
| Shops | shop_id | 256 |

### 2. Multi-Level Caching

```
Browser Cache → CDN → Nginx Cache → Local Cache (Caffeine) → Redis → Database
     ↓             ↓        ↓              ↓                  ↓          ↓
   <1ms          <5ms     <10ms         <1ms               <5ms      >50ms
```

**Cache Hierarchy:**

| Level | Technology | Hit Rate | Data Size |
|-------|------------|----------|-----------|
| L1 (Local) | Caffeine/Guava | 60% | ~10MB per instance |
| L2 (Distributed) | Redis Cluster | 30% | ~10TB total |
| L3 (CDN) | Alibaba CDN | 80% static | Global edge |

### 3. Async Processing

Decoupling through message queues:

```
Order Creation ──► Order Service ──► Kafka ──► Inventory Service
                              │
                              └─► Kafka ──► Payment Service
                              │
                              └─► Kafka ──► Notification Service
                              │
                              └─► Kafka ──► Analytics Pipeline
```

### 4. Database Architecture

**Read/Write Splitting:**

```
                    ┌──► Read Replica 1
Write ──► Master ──┼──► Read Replica 2
                    └──► Read Replica 3
```

**Sharding Implementation:**

```sql
-- Auto-routing based on user_id
SELECT * FROM order_${user_id % 1024} 
WHERE user_id = #{user_id} AND order_id = #{order_id}
```

---

## Microservices Design

### Service Decomposition

| Domain | Services | Key Responsibility |
|--------|----------|-------------------|
| **Product** | Product Service, Category Service, Price Service | Catalog management |
| **Order** | Order Service, Cart Service, Checkout Service | Purchase flow |
| **Payment** | Payment Service, Refund Service | Financial transactions |
| **User** | User Service, Auth Service, Profile Service | Identity management |
| **Merchant** | Shop Service, Seller Service | Merchant operations |
| **Marketing** | Coupon Service, Promotion Service, Point Service | Campaigns & incentives |
| **Logistics** | Shipping Service, Tracking Service | Delivery coordination |

### Service Communication

| Pattern | Use Case | Implementation |
|---------|----------|----------------|
| **Sync (REST/gRPC)** | User-facing, low latency | 100ms timeout, circuit breaker |
| **Async (Message Queue)** | Background processing | Kafka, at-least-once delivery |
| **Event Sourcing** | Audit trails, replay | Domain events stored forever |

---

## Search & Recommendation

### Search Architecture

```
Query ──► Query Understanding ──► Retrieval ──► Ranking ──► Presentation
            │                        │             │            │
            ▼                        ▼             ▼            ▼
       Intent Classification    Inverted Index   ML Model    Result Formatting
       Spell Correction         BM25 + Vector    Feature     Personalization
       Entity Recognition       Recall: 10K      Score       A/B Testing
```

**Ranking Layers:**

| Layer | Model | Latency | Items |
|-------|-------|---------|-------|
| Recall | Vector similarity + Text | <10ms | 10,000 |
| Pre-rank | LightGBM | <5ms | 1,000 |
| Rank | Deep Learning (DIN) | <50ms | 100 |
| Re-rank | Business rules | <1ms | 50 |

### Recommendation System

**Multi-Interest Network:**

```
User Behavior ──► Interest Extraction ──► Candidate Generation ──► Ranking
     │                   │                        │                  │
     ▼                   ▼                        ▼                  ▼
 Clicks, Views      Multi-head Attention    Collaborative       Deep Interest
 Purchases,         learns diverse          Filtering           Network (DIN)
 Dwell time         interests               Content-based       + RL for exploration
```

---

## High Availability Design

### Multi-Region Deployment

```
         ┌─────────────┐
         │   Global    │
         │    DNS      │
         └──────┬──────┘
                │
        ┌───────┴───────┐
        ▼               ▼
   ┌─────────┐     ┌─────────┐
   │  East   │◄───►│  West   │
   │ Region  │     │ Region  │
   │(Active) │     │(Active) │
   └─────────┘     └─────────┘
        │               │
        └───────┬───────┘
                ▼
           ┌─────────┐
           │  Data   │
           │  Sync   │
           └─────────┘
```

### Failure Handling

| Failure Type | Strategy | Implementation |
|--------------|----------|----------------|
| **Service Failure** | Circuit Breaker | Hystrix, 50% error threshold |
| **DB Failure** | Read-only mode | Degrade to cached data |
| **Cache Failure** | Fallback to DB | Rate limiting protection |
| **Full System** | Static pages | Pre-generated HTML |

---

## Singles' Day Engineering

### Capacity Planning

```
Normal Day:     ████ (100K QPS)
6.18 Festival:  ████████ (500K QPS)
Singles' Day:   ████████████████████ (1M+ QPS)

Capacity = Peak Expected × 1.5 (Safety Buffer)
```

### Pre-Warming Strategy

1. **Cache Pre-warming**: Load hot items into cache 24h before event
2. **DB Connection Pool**: Scale connections 2 weeks in advance
3. **CDN Cache**: Push static assets to edge nodes globally
4. **Traffic Prediction**: ML models predict per-minute traffic

### Degradation Plan

| Priority | Feature | Degradation Trigger |
|----------|---------|---------------------|
| P0 | Browse, Search, Buy | Never degrade |
| P1 | Recommendations | Degrade if latency > 200ms |
| P2 | Reviews | Static cache, 5min delay |
| P3 | Real-time inventory | Cached view, eventual consistency |
| P4 | Analytics | Sample 10% traffic |

---

## Key Lessons

1. **Design for Failure**: Assume everything fails; plan for graceful degradation
2. **Cache Aggressively**: Every millisecond matters at scale
3. **Decouple Everything**: Async communication enables independent scaling
4. **Measure Everything**: If you can't measure it, you can't optimize it
5. **Start Simple**: Complex architectures emerge from proven simple ones

---

**Reference Version**: 1.0.0 | **Last Updated**: 2026-03-21
