## § 6 · Standards & Reference

### 6.1 Integration Patterns

| Pattern | When to Use | Key Implementation |
|---------|-------------|-------------------|
| **Stripe-hosted Checkout** | Quick launch, low customization | Redirect to Stripe, handle webhooks |
| **Embedded Elements** | Custom UI, PCI scope reduction | Stripe.js Elements, client-server flow |
| **API-only** | Full control, more PCI scope | Raw card collection (SAQ D required) |
| **Connect Express** | Platforms, quick onboarding | OAuth, account tokens |
| **Connect Custom** | Full control over UX | API account creation, TOS acceptance |

### 6.2 Compliance Requirements

| Standard | Applies When | Stripe's Role | Your Responsibility |
|----------|--------------|---------------|---------------------|
| **PCI-DSS** | Card data handling | Level 1 certified; Elements reduce scope | SAQ A with Elements; SAQ D without |
| **PSD2/SCA** | EU card payments | 3DS2 support, exemption routing | Trigger 3DS when required |
| **KYC/AML** | Connected accounts | Identity verification platform | Collect required info, monitor |
| **SOC 2** | Enterprise customers | Type II certified | Your own compliance |

### 6.3 Local Payment Methods (2025)

| Region | Method | Use Case | Integration |
|--------|--------|----------|-------------|
| Europe | SEPA Direct Debit | Recurring euro payments | Mandate setup, notification webhooks |
| Netherlands | iDEAL | Dutch e-commerce | Bank redirect flow (60%+ usage) |
| Germany | Klarna/Sofort | BNPL, bank transfer | Customer authentication |
| APAC | Alipay, WeChat Pay | China cross-border | QR code, redirect flows |
| Brazil | Pix | Instant payments | QR code, key-based (now dominant) |
| India | UPI | Real-time payments | Collect VPA, intent flow |
| Global | USDC Stablecoin | Crypto payments | Reintroduced 2024, Circle integration |

---
