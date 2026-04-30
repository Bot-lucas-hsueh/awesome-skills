# Stripe Product Reference

## Core Products

### Payments

**Overview:** The foundation of Stripe — accepting payments online and in-person.

**Key Features:**
- Credit/debit card processing ( Visa, Mastercard, Amex, Discover)
- 135+ currencies
- 62+ payment methods
- Automatic currency conversion
- Dynamic 3D Secure / SCA handling

**APIs:**
- `PaymentIntents` — Modern, SCA-ready payment flow
- `Charges` — Legacy API (still supported)
- `SetupIntents` — Save payment methods for future use
- `Refunds` — Return funds to customers

**Pricing:**
- Standard: 2.9% + $0.30 per transaction (US)
- Custom pricing for enterprise
- No monthly fees for basic processing

**Key Concepts:**
- `client_secret` — Token for client-side confirmation
- `payment_method` — Saved payment instrument
- `confirmation_method` — `automatic` vs `manual`
- `capture_method` — `automatic` vs `manual` (auth + capture)

---

### Checkout

**Overview:** Pre-built, Stripe-hosted payment page optimized for conversion.

**Use Cases:**
- Quick integration without custom UI
- High-conversion optimized design
- Global payment method support
- Mobile-responsive

**Features:**
- Accepts 40+ payment methods
- Automatic tax calculation (with Tax)
- Coupon/promo code support
- Customer portal integration
- Link (1-click checkout) support

**Integration:**
```javascript
const session = await stripe.checkout.sessions.create({
  line_items: [{ price: '{{PRICE_ID}}', quantity: 1 }],
  mode: 'payment',
  success_url: 'https://example.com/success',
  cancel_url: 'https://example.com/cancel'
});
```

---

### Connect

**Overview:** Platform solution for marketplaces, multi-party payments.

**Account Types:**

| Type | Onboarding | Dashboard | Best For |
|------|------------|-----------|----------|
| **Standard** | Stripe handles | Full Stripe Dashboard | Quick start, full control to seller |
| **Express** | Stripe handles | Embedded Dashboard | Balance of control and ease |
| **Custom** | You handle | None (you build UI) | Full control over UX |

**Charge Types:**
- **Direct** — Charge on connected account
- **Destination** — Charge on platform, split to connected
- **Separate** — Platform charges, transfers separately

**Capabilities:**
- Onboarding (OAuth or API)
- Identity verification
- Payout management
- Tax form (1099-K) reporting
- Platform fee collection

**Compliance:**
- KYC/AML verification required
- Account.updated webhooks for status changes
- Platform terms acceptance

---

### Billing

**Overview:** Subscription management, recurring revenue, invoicing.

**Key Features (2025):**
- 300,000+ companies using Billing
- 200M+ active subscriptions
- Usage-based billing with Meters API
- Dimensional pricing (new 2025)
- Credit grants with real-time burning
- Smart Retries for failed payments
- Revenue recognition support

**Core Concepts:**

```
Products → What you sell
   ↓
Prices → How you charge (amount, currency, interval)
   ↓
Subscriptions → Customer + Price(s) + recurring billing
   ↓
Invoices → Periodic bill generation
```

**Pricing Models:**
- Flat rate ($99/month)
- Per-seat ($10/user/month)
- Usage-based (API calls, tokens)
- Tiered (volume discounts)
- Hybrid (combinations)

**2025 New Features:**
- **LLM Token Billing** — Native AI usage tracking
- **Dimensional Pricing** — Bill by model type, request size
- **Real-time Credit Burning** — Live consumption tracking
- **Meter Usage Analytics API** — Real-time aggregated data
- **Test Clock Support** — Test time manipulation for billing

---

### Radar

**Overview:** ML-powered fraud detection and prevention.

**Features:**
- Automatic risk scoring (0-100)
- Real-time ML models
- Custom rule engine
- 3D Secure triggering
- Review queue
- Block/allow lists

**Risk Scores:**
```
0-30:   Low risk — Process normally
31-65:  Elevated — Allow, monitor
66-75:  High — Request 3D Secure
76-100: Very High — Block or manual review
```

**Custom Rules Example:**
```
Block if :risk_score: > 75
Request 3D Secure if :billing_address: != :ip_country:
Block if :email: has > 3 :declines: in 1 hour
```

**Radar for Fraud Teams (Enterprise):**
- Manual review queue
- Chargeback protection
- Custom ML models
- Advanced analytics

---

### Tax

**Overview:** Automatic sales tax, VAT, GST calculation.

**Coverage:**
- 57 countries (2025)
- Expanding to 102 countries for physical goods (2026)
- US state and local tax
- EU VAT
- Digital goods tax

**Features:**
- Automatic tax calculation at checkout
- Tax collection and remittance
- Tax reporting
- Tax overrides for custom rules
- Product tax codes

**Integration:**
```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: 'usd',
  automatic_tax: { enabled: true }
});
```

---

### Atlas

**Overview:** Business incorporation service (primarily Delaware C-Corps).

**Availability:** 140+ countries

**Services:**
- Delaware C-Corp or LLC formation
- Registered agent service
- EIN acquisition
- US business bank account
- Stripe Atlas Community access
- $100K+ in partner benefits

**Stats:**
- 50,000+ companies formed
- 25% of all new Delaware corporations
- Companies on pace for $5B collective annual revenue

**Pricing:**
- $500 one-time (includes government fees)
- $100/year ongoing

---

### Climate

**Overview:** Carbon removal commitment tool.

**How It Works:**
- Business commits % of revenue
- Funds directed to carbon removal
- Visible to customers at checkout
- Shown on receipts/invoices

**Frontier:**
- $925M, 9-year advance market commitment
- Fully owned by Stripe
- Funding from Stripe, Shopify, Alphabet, Meta, McKinsey
- Experts select carbon removal companies

---

### Sigma

**Overview:** SQL-based analytics on Stripe data.

**Features:**
- Write SQL against your Stripe data
- Pre-built templates
- Scheduled reports
- Export capabilities
- Custom dashboards

**Tables:**
- `charges`
- `subscriptions`
- `invoices`
- `customers`
- `refunds`
- `payouts`
- And many more...

**Pricing:**
- Usage-based based on query volume
- Subscription option available (2025)

---

### Issuing

**Overview:** Create and manage virtual/physical cards.

**Use Cases:**
- Corporate expense cards
- Platform card programs
- On-demand services
- Expense management

**Features:**
- Virtual cards (instant)
- Physical cards (mail delivery)
- Card controls (spending limits, categories)
- Real-time authorizations
- Fraud signals for Issuing (2025)

---

### Treasury

**Overview:** Banking-as-a-service infrastructure.

**Features:**
- Financial accounts for customers
- Money movement (ACH, wires)
- Balance management
- Interest-bearing accounts
- Embedded financial services

**Use Cases:**
- Platform financial accounts
- Seller/account holder funds
- Embedded banking products

---

### Terminal

**Overview:** In-person payments with card readers.

**Hardware:**
- Stripe Reader M2
- Stripe Reader S700
- BBPOS WisePOS E
- Tap to Pay on iPhone/Android

**Availability:** 23+ countries

**Features:**
- In-person card payments
- Contactless/NFC
- Chip (EMV)
- Magstripe
- Tipping
- Receipts

---

### Identity

**Overview:** Identity verification service.

**Features:**
- ID document verification
- Selfie matching
- Database verification
- Global coverage
- Enhanced UX (2025 update)

**Use Cases:**
- KYC/AML compliance
- Age verification
- Account verification
- High-value transaction verification

---

## Revenue and Finance Automation Suite

**Combined Products:**
- Billing
- Invoicing
- Tax
- Revenue Recognition
- Sigma
- Data Pipeline

**Metrics:**
- Approaching $1B annual run rate (2025)
- 300,000+ companies using Billing
- $6.5B+ revenue recovered via Smart Retries (2024)

---

## New & Experimental (2025-2026)

### AI Billing Features

**LLM Token Billing:**
- Track AI model usage
- Bill per token/API call
- Route through Stripe proxy

**Dimensional Pricing:**
- Price by multiple attributes
- Model type, request size, delivery speed

**Credit Grants 2.0:**
- Real-time credit burning
- Low balance alerts
- Automatic top-ups

### Crypto

**USDC Support:**
- Reintroduced 2024
- Circle integration
- Stablecoin payments
- Cross-border focus

**Bridge Acquisition:**
- $1.1B acquisition (Oct 2024)
- Stablecoin infrastructure
- Accelerating crypto payment adoption

---

*Last Updated: March 2026*
*Sources: stripe.com/docs, product changelogs*
