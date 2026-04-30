## § 8 · Examples

### Example 1: E-commerce Payment Processing

**Context:** Implementing a checkout flow for an online retailer processing $10M/year.

**User:** "We need to accept credit cards globally with 3D Secure support."

**Expert Response:**

**Architecture Recommendation:**
```
Frontend (Your Site)          Stripe                Backend
     │                          │                      │
     │  1. Load Stripe.js       │                      │
     │─────────────────────────>│                      │
     │                          │                      │
     │  2. Create PaymentIntent │                      │
     │                          │<─────────────────────│
     │                          │  (amount, currency)  │
     │                          │                      │
     │  3. client_secret        │                      │
     │                          │─────────────────────>│
     │                          │                      │
     │  4. Mount Card Element   │                      │
     │  5. Confirm payment      │                      │
     │─────────────────────────>│                      │
     │                          │                      │
     │  6. 3D Secure (if needed)│                      │
     │  7. Payment result       │                      │
     │                          │                      │
     │                     8. webhook: payment_intent.succeeded
     │                          │─────────────────────>│
```

**Key Implementation Details:**
```javascript
// Frontend: Stripe.js integration
const stripe = Stripe('pk_live_...');
const elements = stripe.elements();
const card = elements.create('card');
card.mount('#card-element');

// Server: Create PaymentIntent
const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,  // $20.00 in cents
  currency: 'usd',
  automatic_payment_methods: { enabled: true },
  // Enable 3D Secure when required
  payment_method_options: {
    card: { request_three_d_secure: 'automatic' }
  }
});

// Confirm on client
const result = await stripe.confirmCardPayment(clientSecret, {
  payment_method: { card: cardElement }
});
```

**Critical Considerations:**
- ✅ Use `automatic_payment_methods` for global method support
- ✅ Store `payment_intent.id` for idempotency and reconciliation
- ✅ Handle `requires_action` for 3D Secure authentication
- ✅ Listen for webhooks before confirming to customer

---

### Example 2: Marketplace with Connect

**Context:** Building a platform like Shopify where merchants sell and platform takes a fee.

**User:** "We need to onboard sellers and split payments between them and us."

**Expert Response:**

**Architecture:**
```
Customer pays $100 ──> Platform Stripe Account
                              │
                    ┌─────────┴──────────┐
                    ▼                    ▼
            Platform fee ($10)    Connected Account ($90)
            (Platform keeps)      (Seller receives)
```

**Implementation:**

1. **Onboard sellers with Express accounts:**
```javascript
// Create connected account
const account = await stripe.accounts.create({
  type: 'express',
  country: 'US',
  capabilities: {
    card_payments: { requested: true },
    transfers: { requested: true }
  }
});

// Generate onboarding link
const accountLink = await stripe.accountLinks.create({
  account: account.id,
  refresh_url: 'https://example.com/reauth',
  return_url: 'https://example.com/return',
  type: 'account_onboarding'
});
```

2. **Destination charges (platform controls, seller receives):**
```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 10000,
  currency: 'usd',
  // Funds go to platform first
  transfer_data: {
    destination: '{{CONNECTED_ACCOUNT_ID}}',
    amount: 9000  // Seller gets $90
  },
  application_fee_amount: 1000,  // Platform keeps $10
  // OR use on_behalf_of for seller's branding
  on_behalf_of: '{{CONNECTED_ACCOUNT_ID}}'
});
```

**Compliance Checklist:**
- [ ] Sellers complete Stripe onboarding (KYC verified)
- [ ] Platform agreement accepted
- [ ] Handle `account.updated` webhooks for verification status
- [ ] Tax reporting (1099-K) setup for US sellers

---

### Example 3: Fraud Detection with Radar

**Context:** Subscription SaaS experiencing card testing attacks and friendly fraud.

**User:** "We're seeing fraudulent signups and chargebacks. How should we use Radar?"

**Expert Response:**

**Radar Configuration:**

1. **Default ML Protection (always enabled):**
```
Risk Score: 0-100
├── 0-30: Low risk — Process normally
├── 31-65: Elevated — Allow, monitor
├── 66-75: High — Request 3D Secure
└── 76-100: Very High — Block or manual review
```

2. **Custom Rules for SaaS:**
```
# Block known bad patterns
Block if :issuer_country: = 'XX' and :amount_in_usd: < 1
  → Card testing from high-risk countries

# 3D Secure for elevated risk
Request 3D Secure if :risk_score: > 50 and :billing_address: != :ip_country:
  → Unusual location mismatch

# Velocity checks
Block if :email: has > 3 :declines: in 1 hour
  → Repeated failed attempts
```

3. **Review Queue Setup:**
```javascript
// Flag for manual review in Dashboard
const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: 'usd',
  radar_options: {
    // Force into review queue
    manual_review: 'require'
  }
});
```

**Best Practices:**
- Monitor chargeback rate (keep < 0.9% for Visa/MC compliance)
- Use Radar for Fraud Teams for high-volume manual review
- Implement velocity checks at application level too
- Review Radar weekly for false positive tuning

---

### Example 4: Global Expansion with Local Payment Methods

**Context:** US-based SaaS expanding to EU, APAC, and LATAM markets.

**User:** "We need to accept payments in Europe, Brazil, and India with local methods."

**Expert Response:**

**Payment Method Strategy:**

| Market | Primary Method | Secondary | Key Consideration |
|--------|---------------|-----------|-------------------|
| Germany | Cards (with Klarna) | SEPA DD | Strong BNPL preference |
| Netherlands | iDEAL | Cards | 60%+ iDEAL usage |
| India | UPI | Cards | RBI regulations, local entity |
| Brazil | Pix | Credit cards | Pix now dominant |
| Japan | Cards | Konbini | Cash culture persists |

**Implementation:**

```javascript
// Enable all relevant payment methods
const paymentIntent = await stripe.paymentIntents.create({
  amount: 5000,
  currency: 'eur',  // Local currency
  automatic_payment_methods: {
    enabled: true,
    // Allow only methods available in customer's country
    allow_redirects: 'always'
  },
  // Dynamic payment method availability
  payment_method_types: ['card', 'ideal', 'sepa_debit', 'klarna']
});

// For India (UPI)
const paymentIntentIN = await stripe.paymentIntents.create({
  amount: 500000,  // INR in paise
  currency: 'inr',
  payment_method_types: ['card', 'upi'],
  // UPI specific
  payment_method_options: {
    upi: {
      // Collect VPA from customer
      vpa: 'customer@upi'
    }
  }
});
```

**Regulatory Considerations:**

1. **EU - PSD2/SCA:**
   - Strong Customer Authentication required
   - Stripe handles exemptions (low-risk, subscription, merchant-initiated)
   - Enable 3D Secure for all card payments

2. **India - RBI:**
   - Additional factor authentication (AFA) required
   - Tokenization mandate for card storage
   - Local entity may be required for certain flows

3. **Brazil - Pix:**
   - Real-time, 24/7 instant payment
   - QR code or copy-paste keys
   - No chargebacks (irreversible)

---

### Example 5: AI-Powered Billing with Stripe (2025 New Feature)

**Context:** AI company needs to bill customers based on LLM token usage.

**User:** "We want to charge based on AI model usage like tokens and API calls."

**Expert Response:**

**Architecture:**
```
┌─────────────────────────────────────────────────────────────────┐
│                    AI USAGE BILLING FLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  AI Application          Stripe Proxy/Metering        Billing   │
│       │                         │                       │       │
│       │ 1. API Request            │                       │       │
│       │──────────────────────────>│                       │       │
│       │                         │                       │       │
│       │ 2. Record usage events    │                       │       │
│       │                         │──────────────────────>│       │
│       │                         │                       │       │
│       │ 3. Aggregate & bill       │                       │       │
│       │                         │<──────────────────────│       │
│       │                         │                       │       │
│       │ 4. Invoice customer       │                       │       │
│       │                         │──────────────────────>│       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Implementation:**

1. **Set up Meter for usage tracking:**
```javascript
// Create a meter for token usage
const meter = await stripe.billing.meters.create({
  display_name: 'LLM Tokens',
  event_name: 'llm_tokens_used',
  default_aggregation: {
    formula: 'sum'
  }
});

// Report usage events
await stripe.billing.meters.createEvent({
  event_name: 'llm_tokens_used',
  payload: {
    stripe_customer_id: 'cus_...',
    value: 1500,  // tokens used
    timestamp: Math.floor(Date.now() / 1000)
  }
});
```

2. **Configure dimensional pricing (new 2025 feature):**
```javascript
// Price based on multiple attributes
const price = await stripe.prices.create({
  product: '{{PRODUCT_ID}}',
  currency: 'usd',
  billing_scheme: 'tiered',
  tiers: [
    { up_to: 1000000, unit_amount: 0.002 },     // $0.002 per token
    { up_to: 10000000, unit_amount: 0.0015 },   // $0.0015 per token
    { up_to: 'inf', unit_amount: 0.001 }        // $0.001 per token
  ],
  recurring: {
    usage_type: 'metered',
    interval: 'month'
  },
  // Dimensional pricing for model types
  transform_quantity: {
    divide_by: 1000,
    round: 'up'
  }
});
```

3. **Real-time credit burning with alerts:**
```javascript
// Set up credit grants with real-time burning
const creditGrant = await stripe.billing.creditGrants.create({
  customer: 'cus_...',
  amount: {
    currency: 'usd',
    value: 10000  // $100 credit
  },
  priority: 1,
  category: 'prepaid',
  // Configure low balance alerts
  metadata: {
    alert_threshold: '1000'  // Alert when <$10 remaining
  }
});
```

**Key 2025 Billing Features:**
- **LLM Token Billing:** Native support for AI model usage tracking
- **Dimensional Pricing:** Bill by model type, request size, delivery speed
- **Real-time Credit Burning:** Live credit consumption with balance alerts
- **Usage Analytics API:** Real-time aggregated usage data per customer
- **Test Clock Support:** Test usage-based billing with time manipulation

---
