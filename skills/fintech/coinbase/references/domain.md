## § 2 — Domain Knowledge

### 2.1 Coinbase Exchange Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CLIENT LAYER                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐    │
│  │   Mobile    │  │    Web      │  │   API/Pro   │  │  Institutional  │    │
│  │  (iOS/Droid)│  │  (React)    │  │  (REST/WebS)│  │    (Prime)      │    │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └────────┬────────┘    │
└─────────┼────────────────┼────────────────┼──────────────────┼─────────────┘
          │                │                │                  │
          └────────────────┴────────────────┴──────────────────┘
                                     │
┌────────────────────────────────────┴───────────────────────────────────────┐
│                           API GATEWAY (Kong/AWS)                          │
│  • Rate Limiting: 10 req/s public, 100 req/s auth'd                       │
│  • WAF / DDoS Protection                                                  │
│  • Auth: OAuth 2.0 + API Key + IP Whitelist                               │
└────────────────────────────────────┬───────────────────────────────────────┘
                                     │
┌────────────────────────────────────┴───────────────────────────────────────┐
│                         TRADING ENGINE (Aeron Cluster)                    │
│  ┌────────────────────────────────────────────────────────────────────┐   │
│  │  • Matching Engine: Sub-100μs latency                              │   │
│  │  • Order Types: Market, Limit, Stop, TWAP, Iceberg                 │   │
│  │  • Throughput: 1M+ orders/second                                   │   │
│  │  • Replication: 3-region active-active                             │   │
│  └────────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────┬───────────────────────────────────────┘
                                     │
┌────────────────────────────────────┴───────────────────────────────────────┐
│                           CUSTODY LAYER                                   │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐    │
│  │  Hot Wallet     │  │   Warm Wallet   │  │   Cold Storage (98%)    │    │
│  │  (Instant)      │  │  (Timed delay)  │  │  (HSM + Multi-sig)      │    │
│  │  2% assets      │  │   <1% assets    │  │   Air-gapped, global    │    │
│  └─────────────────┘  └─────────────────┘  └─────────────────────────┘    │
└────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Custody Security Model

| Layer | Technology | Security Controls | Recovery Time |
|-------|------------|-------------------|---------------|
| **Cold Storage** | HSM (Hardware Security Module) | 3-of-5 multi-sig, geographic distribution, air-gapped | 24-48 hours |
| **Warm Wallet** | HSM with time delays | 2-of-3 multi-sig, 24h timelock | 1-4 hours |
| **Hot Wallet** | Online HSM | 2-of-3 multi-sig, automated rebalancing | Instant |
| **Operational** | MPC (Multi-Party Computation) | Policy engine, approval workflows | Minutes |

**Institutional Custody (Coinbase Prime):**
- Custodies 80%+ of US BTC and ETH ETF assets
- $515.9B assets under management (Q3 2025)
- 270+ Crypto-as-a-Service clients
- 150+ government agencies as clients
- 9th straight quarter of native unit growth

### 2.3 Base L2 Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                            BASE L2 (OP Stack)                           │
├─────────────────────────────────────────────────────────────────────────┤
│  Sequencer (Coinbase-operated, decentralization roadmap 2025)           │
│  ├── Receives transactions from RPC                                     │
│  ├── Orders transactions                                                │
│  ├── Publishes blocks to L1 (Ethereum)                                  │
│  └── Revenue: Transaction fees - L1 data costs                          │
│                                                                          │
│  Key Metrics (2025):                                                     │
│  ├── 62% of total L2 revenue ($75.4M of $120.7M)                        │
│  ├── 46% of L2 DeFi TVL ($4.63B)                                        │
│  ├── 30.7M monthly active addresses                                     │
│  └── 9.24M 24-hour transactions                                         │
│                                                                          │
│  Fraud Proof System                                                      │
│  ├── 7-day challenge window                                             │
│  ├── Permissioned challengers (initial)                                 │
│  └── Progressive decentralization roadmap                               │
│                                                                          │
│  Data Availability                                                      │
│  ├── Transaction data posted to Ethereum L1                             │
│  ├── Blobs (EIP-4844) for cost efficiency                               │
│  └── ~10x cost reduction vs calldata                                    │
└─────────────────────────────────────────────────────────────────────────┘
```

### 2.4 Revenue Diversification Strategy

| Revenue Stream | FY2025 | % of Total | Growth Driver |
|----------------|--------|------------|---------------|
| Transaction Revenue | $4.1B | ~57% | Trading volume, derivatives (Deribit) |
| Subscription & Services | $2.9B+ | ~40% | USDC, staking, custody, Coinbase One |
| Stablecoin Revenue (USDC) | $364M/Q4 | ~15% | Interest on reserves, revenue share with Circle |
| Base L2 Revenue | $75M+ | ~1% | Sequencer fees, growing ecosystem |

**Key Insight:** Subscription & services revenue is 5.5x higher than 2021 cycle peak, providing volatility buffer.

---
