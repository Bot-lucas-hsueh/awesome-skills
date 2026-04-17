## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| PCI-DSS non-compliance | 🔴 Critical | Storing raw card data illegally | Use Stripe.js, Tokens; never touch PAN |
| Fraud losses | 🔴 Critical | Unauthorized transactions | Implement Radar, 3DS, velocity checks |
| Chargebacks | 🔴 High | Customer disputes, liability | Clear descriptors, evidence submission |
| Regulatory violations | 🔴 Critical | Violating PSD2, KYC, AML laws | Compliance review, legal consultation |
| Webhook handling failures | 🟡 High | Missed payment events | Idempotency, retries, monitoring |
| Integration errors | 🟡 Medium | Failed payments, poor UX | Sandboxing, comprehensive testing |

```
❌ "Let's store the card number in our database for convenience"
✅ Always use Stripe.js to tokenize; never store raw card data

❌ "Webhooks are optional, we'll poll for status"
✅ Webhooks are required for reliable event delivery; implement idempotency

❌ "We'll handle PCI compliance ourselves"
✅ Use Stripe Elements to minimize PCI scope to SAQ A
```

---
