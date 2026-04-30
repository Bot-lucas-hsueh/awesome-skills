## § 9 · Scenario Examples

### Scenario 1: Writing API Reference Documentation

**Context:**
User provides an OpenAPI specification and needs complete, scannable API reference documentation.

**User Input:**
```
I have an OpenAPI spec for our payment API. Can you generate reference documentation for these endpoints:
- POST /payments (create payment)
- GET /payments/{id} (get payment status)
- POST /payments/{id}/refund (process refund)

Authentication is via Bearer token. Include Python and JavaScript examples.
```

**Expert Response:**
I'll create comprehensive API reference documentation for your payment endpoints. Here's the structure and content:

**1. POST /payments — Create Payment**

**Description:** Creates a new payment transaction. Returns a payment ID and status.

**Request:**
- **Method:** POST
- **URL:** `https://api.example.com/v1/payments`
- **Authentication:** Bearer token (required)
- **Content-Type:** application/json

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| amount | integer | Yes | Amount in smallest currency unit (cents) |
| currency | string | Yes | ISO 4217 currency code (e.g., "USD", "EUR") |
| payment_method | string | Yes | "card", "bank_transfer", "wallet" |
| customer_email | string | No | Customer email for receipts |
| metadata | object | No | Custom key-value data |

**Response (201 Created):**
| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique payment identifier |
| status | string | "pending", "processing", "succeeded", "failed" |
| amount | integer | Original amount |
| currency | string | Currency code |
| created_at | string | ISO 8601 timestamp |

**Error Responses:**
| Code | Description | Resolution |
|------|-------------|------------|
| 400 | Invalid request body | Check required fields and format |
| 401 | Invalid or missing token | Provide valid Bearer token |
| 422 | Business rule violation | Check amount limits, currency support |
| 429 | Rate limit exceeded | Wait and retry with exponential backoff |

**Example — cURL:**
```bash
curl -X POST "https://api.example.com/v1/payments" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 1999,
    "currency": "USD",
    "payment_method": "card",
    "customer_email": "customer@example.com"
  }'
```

**Example — Python:**
```python
import requests

response = requests.post(
    "https://api.example.com/v1/payments",
    headers={
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    },
    json={
        "amount": 1999,
        "currency": "USD",
        "payment_method": "card",
        "customer_email": "customer@example.com"
    }
)

if response.status_code == 201:
    payment = response.json()
    print(f"Payment {payment['id']}: {payment['status']}")
```

**Example — JavaScript:**
```javascript
const response = await fetch('https://api.example.com/v1/payments', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    amount: 1999,
    currency: 'USD',
    payment_method: 'card',
    customer_email: 'customer@example.com'
  })
});

const payment = await response.json();
console.log(`Payment ${payment.id}: ${payment.status}`);
```

---

### Scenario 2: Designing a Diátaxis Tutorial

**Context:**
User needs a tutorial to get developers started with their SDK.

**User Input:**
```
We have a Python SDK for our ML API. Need a quickstart tutorial that takes developers from zero to making their first prediction. Assume they have Python 3.8+ and an API key.
```

**Expert Response:**
I'll design a Diátaxis-compliant tutorial with clear prerequisites, step-by-step instructions, and a working outcome.

**Tutorial: Getting Started with the ML SDK**

**Audience:** Python developers with basic API familiarity
**Estimated Time:** 10 minutes
**Prerequisites:**
- Python 3.8+ installed
- pip package manager
- API key (sign up at https://example.com/api)

**What You'll Build:**
By the end of this tutorial, you'll have a working script that sends data to our ML API and receives predictions.

---

**Step 1: Install the SDK**

```bash
pip install ml-sdk
```

Verify the installation:
```bash
python -c "import ml_sdk; print(ml_sdk.__version__)"
```

You should see the version number printed.

---

**Step 2: Configure Your API Key**

Set the API key as an environment variable:

```bash
export ML_API_KEY="your_api_key_here"
```

Or set it programmatically in your script:
```python
import os
os.environ["ML_API_KEY"] = "your_api_key_here"
```

---

**Step 3: Make Your First Prediction**

Create a file named `predict.py`:

```python
from ml_sdk import MLClient

# Initialize the client
client = MLClient()

# Prepare your input data
input_data = {
    "features": [1.2, 3.4, 5.6, 7.8],
    "model": "classification-v1"
}

# Get prediction
result = client.predict(input_data)

# Print results
print(f"Prediction: {result['label']}")
print(f"Confidence: {result['confidence']:.2%}")
```

Run the script:

```bash
python predict.py
```

**Expected Output:**
```
Prediction: positive
Confidence: 94.32%
```

---

**Step 4: Handle Errors Gracefully**

Update your script to handle potential errors:

```python
from ml_sdk import MLClient, APIError, RateLimitError

client = MLClient()

try:
    result = client.predict(input_data)
    print(f"Prediction: {result['label']}")
except RateLimitError:
    print("Rate limit exceeded. Please wait and retry.")
except APIError as e:
    print(f"API error: {e.message}")
```

---

**Next Steps:**
- Explore the [API Reference](/docs/api-reference) for advanced features
- Check out [How-To Guides](/docs/how-to) for specific use cases
- Join our [Discord community](https://discord.gg/example) for support

---

### Scenario 3: Docs-as-Code Pipeline Setup

**Context:**
User wants to set up a docs-as-code workflow with MkDocs Material and CI/CD.

**User Input:**
```
We want to set up a docs-as-code pipeline for our API documentation. 
We have OpenAPI specs that need to be rendered, and we want CI to fail if 
documentation coverage drops. Also want Vale for style checking.
```

**Expert Response:**
I'll set up a complete docs-as-code pipeline including MkDocs Material, OpenAPI rendering, Vale linting, and CI/CD gates.

**1. Project Structure:**

```
docs/
├── docs-as-code/
│   ├── mkdocs.yml
│   ├── requirements.txt
│   └── .vale.ini
├── docs/
│   ├── index.md
│   ├── api/
│   │   └── openapi.md
│   └── guides/
│       └── getting-started.md
├── .github/
│   └── workflows/
│       └── docs.yml
└── Makefile
```

**2. mkdocs.yml Configuration:**

```yaml
site_name: API Documentation
dev_addr: "8000"

plugins:
  - search:
      separator: '[\s\-\.]+'
  - mermaid2
  - openapi:
      openapi_path: ../api-specs/openapi.yaml

theme:
  name: material
  palette:
    primary: indigo
    accent: indigo
  features:
    - navigation.instant
    - navigation.tracking
    - search.suggest

markdown_extensions:
  - admonition
  - pymdownx.highlight
  - pymdownx.inlinemath
```

**3. Vale Configuration (.vale.ini):**

```ini
StylesPath = .vale/styles

[*.md]
BasedOnStyles = Google, Microsoft
Google.First_Person = NO
Microsoft.First_Person = NO
Microsoft.Passive = NO
```

**4. CI/CD Workflow (.github/workflows/docs.yml):**

```yaml
name: Documentation CI

on:
  pull_request:
    branches: [main]
    paths:
      - 'docs/**'
      - 'api-specs/**'

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Vale
        uses: errata-ai/vale-action@v1
        with:
          files: ['docs']

  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build documentation
        run: |
          cd docs-as-code
          pip install -r requirements.txt
          mkdocs build --strict

  coverage:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - uses: actions/checkout@v4
      - name: Check API coverage
        run: |
          # Compare OpenAPI endpoints to documented endpoints
          # Fail if coverage < 95%
          python scripts/check_docs_coverage.py
```

**5. Build & Preview Locally:**

```bash
cd docs-as-code
pip install -r requirements.txt
mkdocs serve
```

**Verification:**
1. Open http://localhost:8000 to preview
2. Run `make lint` to test Vale
3. Check CI pipeline passes on PR

---

### Scenario 4: Documentation Audit

**Context:**
User wants an audit of their existing developer documentation to identify gaps and improvements.

**User Input:**
```
Can you audit our developer documentation at https://docs.example.com? 
We've noticed increasing support tickets and poor search analytics. 
Need a comprehensive review with prioritized recommendations.
```

**Expert Response:**
I'll conduct a comprehensive documentation audit covering structure, content quality, searchability, and maintenance.

**## Documentation Audit Report**

### Executive Summary
| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Documentation Coverage | 72% | 95% | -23% |
| Time to First Call | 18 min | <10 min | +8 min |
| Search Success Rate | 58% | 80% | -22% |
| Average Grade Level | 12.4 | <10 | +2.4 |

---

### Findings by Category

#### 1. Structure & Navigation (Score: 6/10)

**Issues Found:**
- ❌ Inconsistent heading hierarchy (H1 → H3 without H2)
- ❌ No breadcrumbs navigation
- ❌ Missing table of contents on long pages
- ❌ No cross-linking between related content

**Recommendations:**
- Restructure all pages with proper H1 → H2 → H3 hierarchy
- Add breadcrumbs to all nested pages
- Enable TOC on pages > 100 lines

#### 2. API Reference (Score: 5/10)

**Issues Found:**
- ❌ 28% of API endpoints missing code examples
- ❌ Authentication section outdated (still references API key, not OAuth)
- ❌ Error codes not linked to resolution steps
- ❌ Response schemas missing field descriptions

**Recommendations:**
- Prioritize adding code examples for top 20 endpoints
- Update authentication to OAuth 2.0
- Create error code lookup with remediation
- Add field descriptions to all response schemas

#### 3. Tutorials (Score: 4/10)

**Issues Found:**
- ❌ Mixed Diátaxis types (tutorials contain explanation content)
- ❌ No visible progress indicators
- ❌ Prerequisites buried in prose
- ❌ No "clean up" or "next steps" section

**Recommendations:**
- Separate tutorial and explanation content
- Add progress bar to multi-step tutorials
- Create Prerequisites sidebar on all tutorials
- Add "Clean Up" section for resources created

#### 4. Search & Discoverability (Score: 6/10)

**Issues Found:**
- ❌ Search doesn't support partial matches
- ❌ No popular searches displayed
- ❌ Content not tagged by topic
- ❌ Some pages missing meta descriptions

**Recommendations:**
- Enable fuzzy search in Algolia/MkDocs
- Add "Popular Searches" section
- Implement topic tagging
- Add meta descriptions to all pages

#### 5. Readability (Score: 7/10)

**Issues Found:**
- ⚠️ Average sentence length 24 words (target: <20)
- ⚠️ Some passive voice usage
- ⚠️ 3 idioms that will not translate ("hit the ground running", "out of the box", "boilerplate")

**Recommendations:**
- Run Hemingway Editor on all pages
- Convert passive to active voice
- Replace idioms with plain language

---

### Prioritized Action Plan

| Priority | Item | Effort | Impact |
|----------|------|--------|--------|
| P0 | Fix authentication docs | 2 days | High |
| P0 | Add code examples to top 20 endpoints | 1 week | High |
| P1 | Restructure heading hierarchy | 3 days | Medium |
| P1 | Add prerequisites to tutorials | 2 days | High |
| P2 | Fix idioms for i18n | 1 day | Low |
| P2 | Enable fuzzy search | 2 days | Medium |

---

### Next Steps

1. **Week 1:** Fix P0 items (authentication, code examples)
2. **Week 2-3:** Address P1 items (structure, tutorials)
3. **Week 4:** P2 items and validation
4. **Week 5:** Re-audit and measure improvement

---

### Scenario 5: Writing a How-To Guide

**Context:**
User needs a how-to guide for a specific developer task.

**User Input:**
```
We need a how-to guide for implementing webhooks in our system. 
Our users need to know how to register endpoints, verify signatures, 
and handle retry logic. Assume they already know basic API concepts.
```

**Expert Response:**
I'll create a focused how-to guide that assumes baseline knowledge and jumps straight to accomplishing the task.

**How-To Guide: Implementing Webhooks**

**Use When:** You need to receive real-time notifications when events occur in our system.
**Prerequisites:** API key, working server endpoint, basic HTTP knowledge

---

### Register a Webhook Endpoint

**1. Determine your endpoint URL**

Your endpoint must:
- Be publicly accessible (not localhost)
- Accept POST requests
- Respond within 30 seconds
- Use HTTPS in production

**2. Register via API:**

```bash
curl -X POST "https://api.example.com/v1/webhooks" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://yourserver.com/webhook",
    "events": ["payment.succeeded", "payment.failed"],
    "secret": "whsec_your_secret_key"
  }'
```

**Response:**
```json
{
  "id": "wh_abc123",
  "url": "https://yourserver.com/webhook",
  "active": true,
  "events": ["payment.succeeded", "payment.failed"]
}
```

---

### Verify Webhook Signatures

Always verify the signature to ensure the request came from us.

**Python:**
```python
import hmac
import hashlib
import base64

def verify_signature(payload, signature, secret):
    expected_signature = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).digest()
    
    return hmac.compare_digest(
        base64.b64encode(expected_signature).decode(),
        signature
    )
```

**JavaScript:**
```javascript
const crypto = require('crypto');

function verifySignature(payload, signature, secret) {
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('base64');
  
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}
```

**Usage:**
```python
# In your webhook handler
@app.route("/webhook", methods=["POST"])
def handle_webhook():
    payload = request.get_data(as_text=True)
    signature = request.headers.get("X-Signature")
    
    if verify_signature(payload, signature, "whsec_your_secret_key"):
        event = json.loads(payload)
        process_event(event)
        return "OK", 200
    else:
        return "Invalid signature", 401
```

---

### Handle Retry Logic

We automatically retry failed webhooks with exponential backoff:

| Attempt | Delay |
|---------|-------|
| 1 | Immediate |
| 2 | 1 minute |
| 3 | 5 minutes |
| 4 | 30 minutes |
| 5 | 2 hours |

**Best Practices:**
1. **Respond quickly** — Return 200 immediately, process asynchronously
2. **Idempotency** — Check for duplicate events using event ID
3. **Logging** — Log all received events for debugging
4. **Testing** — Use our webhook testing tool to simulate failures

---

### Troubleshooting

**"Signature invalid" error:**
- Ensure you're using raw request body, not parsed JSON
- Verify secret matches dashboard setting

**"Endpoint not reachable" error:**
- Check URL is HTTPS and publicly accessible
- Verify firewall allows incoming traffic on port 443

**Missing events:**
- Confirm event type is in your subscriptions
- Check the event delivery logs in dashboard

---
