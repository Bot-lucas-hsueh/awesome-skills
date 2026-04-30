## 10. Common Pitfalls

### Anti-Pattern 1: Explaining Implementation Instead of User Task

❌ **BAD:**
"The `createPayment()` function instantiates a `PaymentRequest` object, serializes it to JSON using the internal `JsonSerializer` class, and passes it to the `HttpClient.post()` method which handles the TLS handshake."

✅ **GOOD:**
"Create a payment by calling `createPayment()` with the amount and currency. The function returns a `Payment` object with the transaction ID and status."

*Why it matters:* Developers need to know what to do, not how the library is implemented. Implementation details belong in code comments and architecture docs, not user-facing documentation.

---

### Anti-Pattern 2: Code Examples Without Context

❌ **BAD:**
```python
client.payments.create(amount=1099, currency="USD")
```

✅ **GOOD:**
```python
import payments_sdk

client = payments_sdk.Client(api_key="sk_live_your_key_here")

payment = client.payments.create(
    amount=1099,       # Amount in cents ($10.99)
    currency="USD",
    description="Order #1042"
)

print(payment.id)     # pay_abc123
print(payment.status) # succeeded
```

*Why it matters:* Code without imports, initialization, or expected output forces the developer to guess. Every guess is a potential support ticket.

---

### Anti-Pattern 3: Nested Documentation (Docs Inside Docs)

❌ **BAD:**
A "Getting Started" guide that links to an "Overview" which links to a "Concepts" page which links back to "Getting Started". No clear entry point; developers lose context and give up.

✅ **GOOD:**
Four distinct pages with single-direction links: Tutorial links to How-To Guides. How-To Guides link to Reference. Reference links to Explanation. Explanation stands alone. No cycles. No nesting.

*Why it matters:* Documentation navigation should be a directed graph, not a maze. Circular linking signals that document purposes have not been defined.

---

### Anti-Pattern 4: Passive Voice Obscuring Responsibility

❌ **BAD:**
"The request should be authenticated. An API key must be included. The response will be returned."

✅ **GOOD:**
"Include your API key in the `Authorization` header. The API returns the response object on success."

*Why it matters:* Passive voice hides who performs the action. In technical documentation, the reader needs to know: do I do this, or does the system do this?

---

### Anti-Pattern 5: Outdated Screenshots Showing the Wrong UI

❌ **BAD:**
A "How to create an API key" guide with screenshots from a UI that was redesigned 8 months ago. The "API Keys" tab is now under "Security" not "Settings". Developers follow the screenshots, cannot find the element, and file support tickets.

✅ **GOOD:**
Prefer text navigation over screenshots: "In the dashboard, select **Security** > **API Keys** > **Create new key**." Use screenshots only for complex visual states that cannot be described in text. When screenshots are required, add a banner to the Figma source file that displays the date and review deadline.

*Why it matters:* Screenshots have the highest drift rate of any documentation element. Every product UI change creates a documentation debt item if screenshots are used liberally.
