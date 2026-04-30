## § 9 · Progressive Disclosure

### Level 1: Quick Start (First 5 Minutes)

**Just need to accept a payment?**

```javascript
// 1. Install: npm install stripe
// 2. Create PaymentIntent (server)
const stripe = require('stripe')('sk_test_...');
const intent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: 'usd'
});
// 3. Confirm with Stripe.js (client)
const result = await stripe.confirmCardPayment(intent.client_secret);
```

→ **Next:** Read Example 1 for complete integration

### Level 2: Common Patterns (First Hour)

- Payment form with Stripe Elements
- Webhook handling for post-payment actions
- Basic Connect onboarding
- Radar rule configuration

→ **Next:** Review §6 Integration Patterns

### Level 3: Production Readiness (First Day)

- Idempotency implementation
- Error handling and retry logic
- Reconciliation processes
- PCI compliance verification
- Monitoring and alerting

→ **Next:** Study §7 Workflows

### Level 4: Advanced Topics (First Week)

- Connect platform architecture
- Multi-currency and local payment methods
- Complex subscription billing
- Custom fraud rules and ML
- Treasury/Issuing embedded finance

→ **Next:** Work through all Examples

### Level 5: Expert Mastery (Ongoing)

- API design principles (internalize Stripe's approach)
- Global expansion strategy
- Regulatory compliance across jurisdictions
- Scale optimization (high TPV)
- AI-powered billing (new 2025 features)

→ **Next:** Study Stripe's engineering blog, API changelogs

---
