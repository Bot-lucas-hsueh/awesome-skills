# Stripe Integration Patterns

## Pattern 1: Stripe-hosted Checkout

### When to Use
- Quick time-to-market
- Limited customization needs
- Want optimized conversion
- Global payment methods needed

### Architecture
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Customer   │────>│   Your App   │────>│    Stripe    │
│   Browser    │<────│   (Server)   │<────│   Checkout   │
└──────────────┘     └──────────────┘     └──────────────┘
       │                                          │
       │<────────────────────────────────────────>│
              Redirect to Stripe-hosted page
```

### Implementation

**1. Create Checkout Session:**
```javascript
// Server
const session = await stripe.checkout.sessions.create({
  payment_method_types: ['card'],
  line_items: [{
    price_data: {
      currency: 'usd',
      product_data: { name: 'T-shirt' },
      unit_amount: 2000,
    },
    quantity: 1,
  }],
  mode: 'payment',
  success_url: 'https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
  cancel_url: 'https://example.com/cancel',
});

// Return session.url to client
```

**2. Redirect Customer:**
```javascript
// Client
window.location.href = session.url;
```

**3. Handle Webhooks:**
```javascript
// Listen for checkout.session.completed
app.post('/webhook', express.raw({type: 'application/json'}), (req, res) => {
  const sig = req.headers['stripe-signature'];
  const event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
  
  if (event.type === 'checkout.session.completed') {
    const session = event.data.object;
    // Fulfill order
  }
  
  res.json({received: true});
});
```

**Pros:**
- Fastest integration
- Optimized for conversion
- PCI compliance handled
- Mobile-responsive

**Cons:**
- Limited customization
- Customer leaves your site
- Less control over UX

---

## Pattern 2: Embedded Elements

### When to Use
- Custom UI required
- Stay on your site
- PCI scope reduction (SAQ A)
- Flexible design

### Architecture
```
┌─────────────────────────────────────────────────────────┐
│                    Your Application                      │
│  ┌─────────────────────────────────────────────────┐   │
│  │              Your Custom UI                      │   │
│  │  ┌─────────────────────────────────────────┐   │   │
│  │  │     Stripe Elements (iframe)            │   │   │
│  │  │  ┌─────────────────────────────────┐   │   │   │
│  │  │  │   Card Element / Express Checkout │   │   │   │
│  │  │  └─────────────────────────────────┘   │   │   │
│  │  └─────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────┘   │
│                         │                              │
│                    Server API                         │
│                         │                              │
│                    Stripe API                         │
└─────────────────────────────────────────────────────────┘
```

### Implementation

**1. Include Stripe.js:**
```html
<script src="https://js.stripe.com/v3/"></script>
```

**2. Create Elements:**
```javascript
const stripe = Stripe('pk_test_...');
const elements = stripe.elements();

const cardElement = elements.create('card', {
  style: {
    base: {
      fontSize: '16px',
      color: '#32325d',
    }
  }
});

cardElement.mount('#card-element');
```

**3. Create PaymentIntent (Server):**
```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: 'usd',
  automatic_payment_methods: { enabled: true }
});

// Return client_secret to client
```

**4. Confirm Payment (Client):**
```javascript
const {error, paymentIntent} = await stripe.confirmCardPayment(
  clientSecret,
  {
    payment_method: {
      card: cardElement,
      billing_details: { name: 'Jenny Rosen' }
    }
  }
);

if (error) {
  // Show error to customer
} else if (paymentIntent.status === 'succeeded') {
  // Show success message
}
```

**Element Types:**
- `card` — Single card element
- `cardNumber`, `cardExpiry`, `cardCvc` — Split fields
- `idealBank` — iDEAL bank selector
- `fpxBank` — FPX bank selector
- `auBankAccount` — BECS Direct Debit
- `payment` — Payment Element (all methods)

**Pros:**
- Full UI customization
- Customer stays on site
- PCI SAQ A compliance
- Flexible payment methods

**Cons:**
- More complex integration
- Need to handle 3D Secure
- More testing required

---

## Pattern 3: Connect - Standard Accounts

### When to Use
- Marketplace with quick onboarding
- Sellers want full Stripe Dashboard
- Platform wants simplicity
- OAuth-based flow acceptable

### Architecture
```
┌─────────────────┐
│   Customer      │
└────────┬────────┘
         │
    ┌────▼──────────────────────────────┐
    │       Your Platform               │
    │  ┌──────────────────────────┐     │
    │  │   Platform Stripe Account │     │
    │  └──────────────────────────┘     │
    └────┬──────────────────────────────┘
         │
    ┌────▼──────────────────────────────┐
    │     Connected Account (Standard)  │
    │       Seller's Stripe Dashboard   │
    └───────────────────────────────────┘
```

### Implementation

**1. OAuth Onboarding:**
```javascript
// Redirect seller to Stripe
const url = `https://connect.stripe.com/oauth/authorize?` + 
  `response_type=code&` +
  `client_id=${CLIENT_ID}&` +
  `scope=read_write`;

res.redirect(url);
```

**2. Handle Callback:**
```javascript
// Exchange authorization code for account ID
const response = await stripe.oauth.token({
  grant_type: 'authorization_code',
  code: req.query.code
});

const accountId = response.stripe_user_id;
// Store accountId for future charges
```

**3. Direct Charges:**
```javascript
// Charge on connected account
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'usd',
  application_fee_amount: 123,  // Platform fee
}, {
  stripeAccount: '{{CONNECTED_ACCOUNT_ID}}'
});
```

**Pros:**
- Easiest Connect option
- Stripe handles onboarding
- Sellers get full Dashboard
- Platform just collects fee

**Cons:**
- Sellers see Stripe branding
- Less control over UX
- OAuth flow required

---

## Pattern 4: Connect - Express Accounts

### When to Use
- Balance of control and ease
- Embedded Dashboard acceptable
- Platform wants more control
- Faster onboarding than Custom

### Architecture
```
┌─────────────────────────────────────────────────────────┐
│                    Customer Payment                      │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────┐
│                  Your Platform                          │
│                    (Controls UX)                        │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────┐
│              Connected Account (Express)                │
│          Stripe handles KYC, embedded Dashboard         │
└─────────────────────────────────────────────────────────┘
```

### Implementation

**1. Create Express Account:**
```javascript
const account = await stripe.accounts.create({
  type: 'express',
  country: 'US',
  capabilities: {
    card_payments: { requested: true },
    transfers: { requested: true }
  }
});
```

**2. Create Onboarding Link:**
```javascript
const accountLink = await stripe.accountLinks.create({
  account: account.id,
  refresh_url: 'https://example.com/reauth',
  return_url: 'https://example.com/return',
  type: 'account_onboarding'
});

res.redirect(accountLink.url);
```

**3. Destination Charges:**
```javascript
// Charge on platform, transfer to connected
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'usd',
  transfer_data: {
    destination: '{{CONNECTED_ACCOUNT_ID}}',
    amount: 877  // Amount after platform fee
  },
  application_fee_amount: 123  // Platform keeps this
});
```

**Pros:**
- Balance of control and ease
- Stripe handles KYC
- Embedded Dashboard available
- Platform controls payment UX

**Cons:**
- Less control than Custom
- Some Stripe branding present

---

## Pattern 5: Connect - Custom Accounts

### When to Use
- Full control over UX required
- White-label experience
- Complex platform requirements
- Willing to handle compliance

### Architecture
```
┌─────────────────────────────────────────────────────────┐
│                    Your Application                      │
│                                                          │
│  ┌─────────────────┐      ┌──────────────────┐         │
│  │  Custom Onboarding │    │  Custom Dashboard  │       │
│  │  (You build UI)    │    │  (You build UI)    │       │
│  └────────┬─────────┘      └────────┬───────────┘       │
│           │                         │                   │
│  ┌────────▼─────────────────────────▼───────────┐       │
│  │         Stripe API (Custom Account)           │       │
│  └───────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────┘
```

### Implementation

**1. Create Custom Account:**
```javascript
const account = await stripe.accounts.create({
  type: 'custom',
  country: 'US',
  capabilities: {
    card_payments: { requested: true },
    transfers: { requested: true }
  },
  business_type: 'individual',
  individual: {
    first_name: 'Jane',
    last_name: 'Diaz',
    // ... more info required
  },
  tos_acceptance: {
    date: Math.floor(Date.now() / 1000),
    ip: req.connection.remoteAddress
  }
});
```

**2. Handle Verification:**
```javascript
// Listen for account.updated
if (event.type === 'account.updated') {
  const account = event.data.object;
  
  if (account.requirements.currently_due.length > 0) {
    // Request more info from user
  }
  
  if (account.charges_enabled) {
    // Account ready to charge
  }
}
```

**3. Separate Charges and Transfers:**
```javascript
// Charge on platform
const charge = await stripe.charges.create({
  amount: 1000,
  currency: 'usd',
  source: token
});

// Transfer to connected account later
const transfer = await stripe.transfers.create({
  amount: 877,
  currency: 'usd',
  destination: '{{CONNECTED_ACCOUNT_ID}}'
});
```

**Pros:**
- Full control over UX
- White-label experience
- Most flexible

**Cons:**
- Highest integration burden
- You handle compliance
- You build onboarding
- More regulatory responsibility

---

## Pattern 6: Subscription Billing

### When to Use
- Recurring revenue business
- Multiple pricing tiers
- Usage-based billing
- Need proration handling

### Architecture
```
┌─────────────────────────────────────────────────────────┐
│                    Subscription Lifecycle                │
│                                                          │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐         │
│  │  Customer │───>│ Subscribe │───>│  Invoice  │         │
│  └──────────┘    └──────────┘    └──────────┘         │
│       │                │                │               │
│       │                │                ▼               │
│       │                │          ┌──────────┐         │
│       │                │          │ Payment  │         │
│       │                │          └──────────┘         │
│       │                │                │               │
│       │                ▼                ▼               │
│       │         ┌─────────────────────────┐            │
│       └────────>│   Billing Engine        │            │
│                 │   (Stripe Billing)      │            │
│                 └─────────────────────────┘            │
└─────────────────────────────────────────────────────────┘
```

### Implementation

**1. Create Product and Price:**
```javascript
const product = await stripe.products.create({
  name: 'Pro Plan'
});

const price = await stripe.prices.create({
  product: product.id,
  unit_amount: 2900,
  currency: 'usd',
  recurring: { interval: 'month' }
});
```

**2. Subscribe Customer:**
```javascript
const subscription = await stripe.subscriptions.create({
  customer: 'cus_...',
  items: [{ price: price.id }],
  trial_period_days: 14,
  automatic_tax: { enabled: true },
  collection_method: 'charge_automatically'
});
```

**3. Handle Proration:**
```javascript
// Customer upgrades
const updatedSubscription = await stripe.subscriptions.update(
  'sub_...',
  {
    items: [{
      id: existingItemId,
      price: 'price_enterprise_...'  // New tier
    }],
    proration_behavior: 'always_invoice'  // Charge immediately
  }
);
```

**4. Usage-Based Billing:**
```javascript
// Report usage
await stripe.billing.meters.createEvent({
  event_name: 'api_requests',
  payload: {
    stripe_customer_id: 'cus_...',
    value: 150,
    timestamp: Math.floor(Date.now() / 1000)
  }
});
```

---

## Pattern 7: Webhook Handling

### Critical Requirements

**1. Verify Signatures:**
```javascript
const sig = req.headers['stripe-signature'];
let event;

try {
  event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
} catch (err) {
  return res.status(400).send(`Webhook Error: ${err.message}`);
}
```

**2. Idempotency:**
```javascript
// Track processed events to avoid duplicates
const processed = await db.query(
  'SELECT * FROM processed_events WHERE event_id = ?',
  [event.id]
);

if (processed.length > 0) {
  return res.json({received: true});  // Already processed
}

// Process event...
await db.query(
  'INSERT INTO processed_events (event_id) VALUES (?)',
  [event.id]
);
```

**3. Handle Failures:**
```javascript
// Return 200 for processed events
// Return error codes for retries (Stripe retries automatically)

app.post('/webhook', async (req, res) => {
  try {
    const event = constructEvent(...);
    await processEvent(event);
    res.json({received: true});  // 200 OK
  } catch (err) {
    console.error(err);
    res.status(500).send('Error');  // Triggers retry
  }
});
```

### Essential Events

| Event | When | Action |
|-------|------|--------|
| `payment_intent.succeeded` | Payment complete | Fulfill order |
| `payment_intent.payment_failed` | Payment failed | Notify customer |
| `invoice.paid` | Subscription paid | Grant access |
| `invoice.payment_failed` | Subscription payment failed | Retry/dunning |
| `customer.subscription.deleted` | Subscription canceled | Revoke access |
| `account.updated` | Connect account status change | Update verification |
| `charge.dispute.created` | Chargeback filed | Submit evidence |

---

## Pattern 8: Idempotency

### Why Idempotency Matters

- Network failures cause retries
- Without idempotency = double charges
- Required for reliable distributed systems

### Implementation

**1. Generate Idempotency Key:**
```javascript
// Use unique key per operation
const idempotencyKey = `payment-${userId}-${timestamp}`;
// Or: crypto.randomUUID()
```

**2. Include in API Call:**
```javascript
const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,
  currency: 'usd',
  customer: 'cus_...'
}, {
  idempotencyKey: idempotencyKey
});
```

**3. Key Strategies:**
```javascript
// Per-action unique key
const key = `create-payment-${userId}-${Date.now()}`;

// Deterministic key for retries
const key = `create-payment-${userId}-${orderId}`;

// Store key before API call for retries
await db.query(
  'INSERT INTO idempotency_keys (key, status) VALUES (?, ?)',
  [key, 'pending']
);

try {
  const result = await stripe.paymentIntents.create(..., { idempotencyKey: key });
  await db.query('UPDATE idempotency_keys SET status = ? WHERE key = ?', ['success', key]);
} catch (err) {
  await db.query('UPDATE idempotency_keys SET status = ? WHERE key = ?', ['failed', key]);
}
```

**Idempotency Key Expiration:**
- Keys expire after 24 hours
- Same key + same params = cached response
- Same key + different params = error

---

*Last Updated: March 2026*
