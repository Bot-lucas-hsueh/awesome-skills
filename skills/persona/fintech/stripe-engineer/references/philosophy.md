## § 4 · Core Philosophy

### 4.1 Stripe's Product Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   STRIPE PLATFORM ARCHITECTURE                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    PRESENTATION LAYER                     │  │
│  │   Stripe.js | Elements | Checkout | Dashboard | Mobile SDK│  │
│  └─────────────────────────┬────────────────────────────────┘  │
│                            │                                     │
│  ┌─────────────────────────▼────────────────────────────────┐  │
│  │                    PAYMENT APIS                           │  │
│  │   PaymentIntents | Charges | SetupIntents | Refunds       │  │
│  └─────────────────────────┬────────────────────────────────┘  │
│                            │                                     │
│  ┌─────────────────────────▼────────────────────────────────┐  │
│  │                    PLATFORM LAYER                         │  │
│  │   Connect | Billing | Radar | Treasury | Issuing          │  │
│  └─────────────────────────┬────────────────────────────────┘  │
│                            │                                     │
│  ┌─────────────────────────▼────────────────────────────────┐  │
│  │                    INFRASTRUCTURE LAYER                    │  │
│  │   Global Payments Network | Treasury Network | ML Platform │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              CROSS-CUTTING: Compliance | Security | ML   │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Product Suite Overview (2025-2026)

| Product | Purpose | Key Metrics |
|---------|---------|-------------|
| **Payments** | Core payment processing | $1.9T annual volume, 500M+ API requests/day |
| **Checkout** | Pre-built payment page | 10.5% avg revenue uplift for merchants |
| **Connect** | Platform/marketplace | 75% of top global marketplaces use Connect |
| **Billing** | Subscription management | 300K+ companies, 200M active subscriptions |
| **Radar** | Fraud prevention | ML-powered, $6.5B+ revenue recovered (2024) |
| **Atlas** | Business incorporation | 50K+ companies, 25% of Delaware corps |
| **Tax** | Sales tax automation | 57 countries (expanding to 102 for physical goods) |
| **Sigma** | SQL-based analytics | Query payment data with SQL |
| **Issuing** | Card program management | Virtual/physical card creation |
| **Terminal** | In-person payments | Available in 23+ countries |
| **Climate** | Carbon removal | $925M Frontier AMC for permanent carbon removal |
| **Identity** | ID verification | Enhanced UX for KYC flows |
| **Treasury** | Banking-as-a-service | Embedded financial accounts |

---
