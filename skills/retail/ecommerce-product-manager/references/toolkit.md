## § 6 · Professional Toolkit

### Analytics & Experimentation
- **Google Analytics 4** — Full-funnel analysis, user journeys, custom events
- **Optimizely / VWO** — A/B testing, multivariate testing, personalization
- **Hotjar
- **Amplitude

### E-commerce Platforms
- **Shopify Plus** — Enterprise e-commerce, checkout extensibility
- **Salesforce Commerce Cloud** — Enterprise omnichannel, B2C/B2B
- **Magento (Adobe Commerce)** — Open-source enterprise, customization
- **BigCommerce** — Headless commerce, API-first

### Personalization & Recommendations
- **Nosto** — AI-powered personalization, dynamic content
- **Dynamic Yield** — Decisioning engine, A/B testing, recommendations
- **Algolia** — Site search, merchandising, autocomplete
- **Klevu** — AI search, product recommendations

### Product Information Management
- **Pimcore** — Open-source PIM, MDM, digital asset management
- **Akeneo** — Open-source PIM, product data syndication
- **Informatica MDM** — Enterprise master data management

## Phase 1: Conversion Audit & Baseline

```
Week 1: Data Collection
  ├── GA4 funnel analysis: landing → product → cart → checkout → purchase
  ├── Device breakdown: mobile vs. desktop vs. tablet conversion rates
  ├── Traffic source analysis: organic, paid, email, social conversion
  ├── Exit page analysis: where are users dropping off?
  └── Benchmark: Compare to industry averages (e-commerce avg: 2.5-3%)

Week 2: Heuristic Evaluation
  ├── UX audit: navigation, search, filters, product page layout
  ├── Performance: PageSpeed score, Core Web Vitals
  ├── Mobile audit: thumb zone, tap targets, form complexity
  ├── Checkout audit: steps, form fields, payment options
  └── Competitive benchmark: test top 3 competitors' checkout flows

Week 3: User Research (if needed)
  ├── 5 user interviews (current customers) on purchase barriers
  ├── 10 session recordings review (focus on cart/checkout abandonment)
  └── Survey: "What stopped you from completing purchase?" (exit intent)
```

### Phase 2: A/B Test Design & Execution

```
Test Hypothesis Template:
  "We believe [change] will improve [metric] from [baseline] to [target]
  because [user insight/research finding]."

Example:
  "We believe moving the 'Add to Cart' button above the fold on mobile
  will increase mobile cart rate from 3.2% to 4.0% because heatmaps show
  60% of users scroll past the current button position."

Statistical Significance Calculator:
  • Baseline conversion: 3.0%
  • Minimum detectable effect (MDE): 20% relative lift
  • Statistical power: 80%
  • Significance level: 95%
  • Required sample size: ~12,000 visitors per variant
  • Estimated test duration: 14 days

Test Priority Matrix:
  ┌─────────────────┬──────────┬──────────────┐
  │ Impact
  ├─────────────────┼──────────┼──────────────┤
  │ High           │ Priority │  Quick Wins  │
  │ Low            │ Fill-ins │  Deprioritize│
  └─────────────────┴──────────┴──────────────┘
```

### Phase 3: Checkout Optimization

```
Checkout Redesign Checklist:
  □ Guest checkout default (no account required)
  □ Progress indicator (Shipping → Payment → Review)
  □ Address auto-complete (Google Places API)
  □ Form field reduction: <8 fields for standard checkout
  □ Express checkout: Apple Pay, Google Pay, PayPal prominent
  □ Order summary sidebar: always visible on desktop
  □ Trust signals: security badges, SSL, payment method icons
  □ Error handling: inline validation, clear error messages
  □ Mobile: large tap targets (44px+), numeric keyboard for phone/CC

Cart Abandonment Recovery:
  • Email sequence: 1 hr (cart reminder) → 24 hr (urgency) → 72 hr (incentive)
  • SMS: 1 hr + 24 hr (with consent)
  • Retargeting ads: dynamic product display
  • Exit intent popup: last resort (avoid annoyance)

Cart Abandonment Metrics:
  • Target: <65% abandonment (>35% cart-to-checkout)
  • Current benchmark by industry:
    - Fashion: 68%
    - Electronics: 73%
    - Grocery: 55%
    - Luxury: 65%
```

### Phase 4: Personalization Implementation

```
Personalization Framework:
  1. First-time visitor:
     • Homepage: bestsellers + hero promotional content
     • No personalized recommendations (no data yet)

  2. Returning visitor (known):
     • Homepage: "Welcome back, [name]" + recently viewed
     • Product pages: "Customers also bought"

  3. Browse Abandonment:
     • Email: "You left these behind" (browse history)
     • Retargeting: dynamic ads of viewed products

  4. Cart Abandonment:
     • Email sequence (see above)
     • Exit intent: discount popup (last 10% of sessions)

  5. Post-purchase:
     • Thank you page: complementary product suggestions
     • Email: order confirmation + "what's next" + review request
     • 7 days: upsell email with 10% off next item

Personalization Privacy:
  • Cookie consent banner (GDPR/CCPA compliant)
  • No tracking without consent
  • Anonymize recommendation data where possible
  • Clear opt-out in account settings
```

## 🔬 Scenario Examples

### 🚫 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Testing Without Hypothesis
**Wrong:** "Let's change the button color from blue to green and see what happens."
**Why it fails:** No hypothesis means no insight. Even if green wins by 2%, you don't know WHY. Next test is random.
**Correct:** "We believe changing the CTA from 'Submit' to 'Get My Free Quote' will increase form submissions because 'Get My Free Quote' communicates specific value, matching user intent on pricing page. We expect 15% lift."

### Anti-Pattern 2: Ignoring Mobile Experience
**Wrong:** Design for desktop, then make it responsive. "Mobile users can pinch-zoom."
**Why it fails:** Mobile conversion is typically 50-70% of desktop. Broken mobile experience = losing 40%+ of potential revenue.
**Correct:** Mobile-first design. Separate mobile KPIs (tap targets 44px+, simplified forms, thumb zone navigation). Test on real devices, not just responsive emulators.

### Anti-Pattern 3: Measuring Vanity Metrics
**Wrong:** "Pageviews are up 30%!" — declare victory.
**Why it fails:** Pageviews don't pay bills. If traffic up but conversion flat, revenue is flat. Vanity metrics mask real performance.
**Correct:** Focus on metrics that directly impact revenue: conversion rate, revenue per session, cart abandonment rate, customer acquisition cost (CAC), customer lifetime value (LTV).

### Anti-Pattern 4: Personalization That Feels Creepy
**Wrong:** "Hey, you were looking at this treadmill! Don't miss out!" in exit popup with exact product.
**Why it fails:** Aggressive retargeting feels invasive. Users close the tab. Privacy concerns. GDPR/CCPA violations.
**Correct:** Personalization should feel helpful, not stalkerish. Use soft signals ("Popular in your area"), delay retargeting (browsed yesterday, not "you were looking at 5 minutes ago"), always provide opt-out.

### Anti-Pattern 5: One-Size-Fits-All Product Pages
**Wrong:** Same product page for fashion and electronics.
**Why it fails:** Fashion = visual, emotional, sizing, fit. Electronics = specs, comparison, technical details. Same page serves neither well.
**Correct:** Category-specific product page templates. Fashion: large images, model shots, size guide. Electronics: specs table, comparison chart, video demo.

