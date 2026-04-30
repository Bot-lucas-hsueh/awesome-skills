# Ant Group & Alipay Payment Systems

> Architecture of the world's largest digital payment platform processing $17+ trillion annually with 1+ billion users.

---

## System Overview

| Metric | Value |
|--------|-------|
| **Annual Payment Volume** | $17+ trillion |
| **Active Users** | 1+ billion |
| **Daily Transactions** | 500+ million |
| **Peak TPS** | 1,000,000+ (Nov 11) |
| **Countries (Alipay+)** | 100+ |
| **Supported Currencies** | 30+ |

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         ANT GROUP PLATFORM                              │
│                                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌─────────────┐ │
│  │   Consumers  │  │   Merchants  │  │   Financial  │  │   Global    │ │
│  │   (Users)    │  │  (Sellers)   │  │ Institutions │  │  Partners   │ │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬──────┘ │
│         │                 │                 │                 │        │
│         └─────────────────┴─────────────────┴─────────────────┘        │
│                                   │                                    │
│                    ┌──────────────┴──────────────┐                    │
│                    │       Unified Gateway        │                    │
│                    │   (API Gateway, Rate Limit)  │                    │
│                    └──────────────┬──────────────┘                    │
│                                   │                                    │
│  ┌────────────────────────────────┼────────────────────────────────┐  │
│  │                    CORE SERVICES LAYER                          │  │
│  │                                                                 │  │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐   │  │
│  │  │  Payment   │ │   Risk     │ │  Wallet    │ │  Transfer  │   │  │
│  │  │  Core      │ │  Engine    │ │  Service   │ │  Service   │   │  │
│  │  └────────────┘ └────────────┘ └────────────┘ └────────────┘   │  │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐   │  │
│  │  │  Credit    │ │  Wealth    │ │ Insurance  │ │   KYC/     │   │  │
│  │  │ (Huabei)   │ │ (Yu'ebao)  │ │  Service   │ │ Identity   │   │  │
│  │  └────────────┘ └────────────┘ └────────────┘ └────────────┘   │  │
│  │                                                                 │  │
│  └────────────────────────────────┼────────────────────────────────┘  │
│                                   │                                    │
│  ┌────────────────────────────────┼────────────────────────────────┐  │
│  │                    INFRASTRUCTURE LAYER                         │  │
│  │                                                                 │  │
│  │  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐   │  │
│  │  │  OceanBase │ │   SOFA     │ │  Message   │ │  Compute   │   │  │
│  │  │ (Database) │ │Middleware) │ │   Queue    │ │   Engine   │   │  │
│  │  └────────────┘ └────────────┘ └────────────┘ └────────────┘   │  │
│  │                                                                 │  │
│  └─────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Core Payment Flow

### Standard Payment Process

```
┌──────┐     ┌─────────┐     ┌──────────┐     ┌─────────┐     ┌──────────┐
│ User │────►│ Merchant│────►│  Alipay  │────►│  Bank   │────►│ Clearing │
│ App  │     │ Server  │     │  Gateway │     │ Network │     │  System  │
└──────┘     └─────────┘     └────┬─────┘     └─────────┘     └──────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │      Alipay Platform        │
                    │  ┌───────────────────────┐  │
                    │  │    Risk Check         │  │
                    │  │  - Fraud detection    │  │
                    │  │  - Limit checks       │  │
                    │  │  - KYC verification   │  │
                    │  └───────────────────────┘  │
                    │  ┌───────────────────────┐  │
                    │  │   Balance/Card Auth   │  │
                    │  │  - Wallet balance     │  │
                    │  │  - Bank card charge   │  │
                    │  │  - Credit (Huabei)    │  │
                    │  └───────────────────────┘  │
                    │  ┌───────────────────────┐  │
                    │  │   Transaction Record  │  │
                    │  │  - OceanBase write    │  │
                    │  │  - Async notification │  │
                    │  └───────────────────────┘  │
                    └─────────────────────────────┘
```

### Escrow Model (担保交易)

The trust innovation that made e-commerce possible in China:

```
Step 1: Order Creation
Buyer ──► Alipay (holds funds) ──► Merchant notified

Step 2: Shipping
Merchant ships ──► Tracking recorded

Step 3: Confirmation
Buyer confirms receipt ──► Alipay releases funds ──► Merchant receives payment

Step 4: Settlement (T+1)
Alipay ──► Merchant's bank account
```

---

## OceanBase: Financial-Grade Database

### Architecture

```
         ┌─────────────────────────────────────┐
         │           OBProxy (SQL Router)       │
         │   - Parse SQL, route to correct node │
         │   - Load balance, failover           │
         └───────────────┬─────────────────────┘
                         │
         ┌───────────────┴───────────────┐
         ▼                               ▼
    ┌─────────┐                    ┌─────────┐
    │ Root    │                    │ Root    │
    │ Service │◄─────Heartbeat────►│ Service │
    │ (Zone A)│    (Leader Election)│ (Zone B)│
    └────┬────┘                    └────┬────┘
         │                              │
    ┌────┴────┐                    ┌────┴────┐
    ▼         ▼                    ▼         ▼
┌───────┐ ┌───────┐            ┌───────┐ ┌───────┐
│ Data  │ │ Data  │            │ Data  │ │ Data  │
│ Node  │ │ Node  │            │ Node  │ │ Node  │
│ (Paxos)│ │(Paxos)│            │(Paxos)│ │(Paxos)│
└───────┘ └───────┘            └───────┘ └───────┘
   Zone A                        Zone B
   (Leader)                      (Follower)
```

### Performance Benchmarks

| Metric | Performance |
|--------|-------------|
| **TPC-C** | 7.07 million tpmC (world record) |
| **Peak TPS** | 61 million transactions/second (2019 Singles' Day) |
| **Latency (P99)** | < 10ms |
| **Data Capacity** | PB scale |
| **Availability** | 99.999% |

---

## Risk Management Engine

### Multi-Layer Risk Control

```
Layer 1: Rule Engine (Real-time)
├── Device fingerprinting
├── Location analysis
├── Velocity checks
└── Blacklist matching
        ↓
Layer 2: ML Models (50ms)
├── Behavioral biometrics
├── Transaction patterns
├── Network analysis
└── Device risk score
        ↓
Layer 3: Graph Analysis (Async)
├── Relationship networks
├── Fraud ring detection
└── Anomaly detection
```

### Risk Decision Matrix

| Risk Score | Action | Latency |
|------------|--------|---------|
| 0-30 (Low) | Approve | < 10ms |
| 30-70 (Medium) | Step-up auth | < 100ms |
| 70-90 (High) | Manual review | Async |
| 90-100 (Critical) | Block | < 10ms |

---

## Alipay+ Cross-Border Payments

### Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                           Alipay+ Network                            │
│                                                                      │
│   ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐     │
│   │ Alipay  │     │  TrueMoney   │ │ GCash   │     │  PayPay   │     │
│   │ (China) │     │ (Thailand)   │ │(Philippines)│ │ (Japan)   │     │
│   └────┬────┘     └────┬────┘     └────┬────┘     └────┬────┘     │
│        │               │               │               │           │
│        └───────────────┴───────┬───────┴───────────────┘           │
│                                │                                    │
│                    ┌───────────┴───────────┐                       │
│                    │   Alipay+ Hub          │                       │
│                    │  • FX conversion       │                       │
│                    │  • Compliance check    │                       │
│                    │  • Settlement          │                       │
│                    │  • Dispute handling    │                       │
│                    └───────────┬───────────┘                       │
│                                │                                    │
│        ┌───────────────────────┼───────────────────────┐           │
│        ▼                       ▼                       ▼           │
│   ┌─────────┐            ┌─────────┐            ┌─────────┐        │
│   │Merchant │            │Merchant │            │Merchant │        │
│   │  (SG)   │            │  (JP)   │            │  (EU)   │        │
│   └─────────┘            └─────────┘            └─────────┘        │
└─────────────────────────────────────────────────────────────────────┘
```

### Value Propositions

| Stakeholder | Benefit |
|-------------|---------|
| **Consumer** | Use home app abroad, competitive FX rates |
| **Merchant** | Access 1B+ Asian consumers, unified integration |
| **Wallet Partner** | International expansion, shared merchants |
| **Alipay+** | Network effects, transaction fees, data insights |

---

## Key Products

### Consumer Products

| Product | Description | Users |
|---------|-------------|-------|
| **Alipay** | Digital wallet & payments | 1B+ |
| **Yu'ebao** | Money market fund | 600M+ |
| **Huabei** | Consumer credit | 300M+ |
| **Jiebei** | Small business loans | 50M+ |
| **Zhima Credit** | Credit scoring | 800M+ |

### Merchant Products

| Product | Function |
|---------|----------|
| **当面付** | In-store QR payments |
| **APP支付** | In-app payments |
| **网站支付** | Online checkout |
| **商家服务** | Business management tools |
| **经营贷** | Merchant financing |

---

## Regulatory Compliance

### Key Regulations

| Regulation | Requirement | Implementation |
|------------|-------------|----------------|
| **Payment License** | Central bank approval | 3rd party payment牌照 |
| **Customer Funds** | Segregated custody | 100% reserve in licensed banks |
| **KYC/AML** | Identity verification | Multi-factor verification |
| **Data Localization** | China data in China | Dedicated data centers |
| **Anti-Monopoly** | Fair competition | Open ecosystem policies |

---

## Key Lessons

1. **Trust is the Product**: Escrow model solved the chicken-and-egg problem of e-commerce trust
2. **Scale Requires Custom Infrastructure**: OceanBase built when MySQL couldn't handle the scale
3. **Risk as Competitive Advantage**: Real-time risk control enables frictionless user experience
4. **Platform Economics**: Network effects create winner-take-most dynamics
5. **Regulatory Navigation**: Compliance as product feature, not afterthought

---

**Reference Version**: 1.0.0 | **Last Updated**: 2026-03-21
