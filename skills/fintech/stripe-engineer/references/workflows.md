## § 7 · Workflows

### 7.1 Payment Integration Workflow

```
Phase 1: Architecture Design
├── Define payment methods (card, local, wallet)
├── Determine Connect requirements (platform?)
├── Plan for SCA/3DS compliance
├── Design webhook handling strategy
└── Document idempotency approach

Phase 2: Implementation
├── Set up Stripe.js for PCI scope reduction
├── Implement PaymentIntents API
├── Build webhook endpoint with idempotency
├── Add Radar for fraud protection
└── Create reconciliation process

Phase 3: Testing
├── Use Stripe test mode and test cards
├── Test 3D Secure flows (success/failure)
├── Simulate webhook events
├── Test idempotency with duplicate requests
└── Verify error handling paths

Phase 4: Go-Live
├── Production API keys
├── Real webhook endpoint (HTTPS required)
├── Dashboard monitoring setup
├── Dispute process documentation
└── Customer support playbooks
```

### 7.2 Connect Platform Workflow

```
Step 1: Choose account type
├── Standard — Stripe handles onboarding, full Dashboard
├── Express — Stripe onboarding, embedded Dashboard
└── Custom — You control everything, highest integration burden

Step 2: Account creation
├── OAuth (Standard/Express) or API (Custom)
├── Collect required verification info
└── Handle account.updated webhooks

Step 3: Payment flows
├── Direct charges (on connected account)
├── Destination charges (on platform, split to connected)
└── Separate charges and transfers (flexible timing)

Step 4: Compliance
├── Platform terms acceptance
├── Identity verification handling
└── Tax form (1099-K) reporting
```

### 7.3 Fraud Prevention Workflow

```
Step 1: Enable Radar
├── Automatic ML risk scoring (0-100)
├── Review queue for elevated risk
└── Block lists for known bad actors

Step 2: Configure rules
├── Custom rules based on business patterns
├── 3D Secure triggering rules
└── Request 3DS for high-risk transactions

Step 3: Monitor and refine
├── Review false positives/negatives
├── Adjust risk thresholds
└── A/B test rule changes

Step 4: Advanced (Enterprise)
├── Radar for Fraud Teams (manual review)
├── Chargeback protection
└── Custom ML models
```

---
