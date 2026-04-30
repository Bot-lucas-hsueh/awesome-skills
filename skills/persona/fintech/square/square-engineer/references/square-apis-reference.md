# Square APIs Reference

## Core APIs

### Payments API
- **Purpose**: Process payments online, in-person, and card-not-present
- **Key Endpoints**:
  - `POST /v2/payments` - Create payment
  - `GET /v2/payments/{payment_id}` - Get payment details
  - `POST /v2/refunds` - Refund payment
- **SDKs**: Python, Node.js, Ruby, PHP, Java, .NET

### Terminal API
- **Purpose**: Integrate Square Terminal for in-person payments
- **Key Endpoints**:
  - `POST /v2/terminals/checkouts` - Create checkout
  - `GET /v2/terminals/checkouts/{checkout_id}` - Get checkout status
- **Devices**: Terminal, Reader, Register, Handheld

### Orders API
- **Purpose**: Create and manage orders across channels
- **Key Endpoints**:
  - `POST /v2/orders` - Create order
  - `POST /v2/orders/search` - Search orders
- **Features**: Line items, fulfillments, taxes, discounts

### Catalog API
- **Purpose**: Manage products, services, and pricing
- **Key Endpoints**:
  - `POST /v2/catalog/object` - Upsert catalog object
  - `POST /v2/catalog/batch-upsert` - Batch upsert
- **Object Types**: ITEM, ITEM_VARIATION, CATEGORY, DISCOUNT, TAX

### Inventory API
- **Purpose**: Track inventory levels and adjustments
- **Key Endpoints**:
  - `POST /v2/inventory/batch-change` - Adjust inventory
  - `POST /v2/inventory/batch-retrieve` - Get inventory counts

### Customers API
- **Purpose**: Manage customer profiles and groups
- **Key Endpoints**:
  - `POST /v2/customers` - Create customer
  - `POST /v2/customers/search` - Search customers

### Bookings API
- **Purpose**: Appointment scheduling
- **Key Endpoints**:
  - `POST /v2/bookings` - Create booking
  - `GET /v2/bookings` - List bookings

### Subscriptions API
- **Purpose**: Recurring billing
- **Key Endpoints**:
  - `POST /v2/subscriptions` - Create subscription
  - `POST /v2/subscriptions/search` - Search subscriptions

### Invoices API
- **Purpose**: Invoice creation and payment
- **Key Endpoints**:
  - `POST /v2/invoices` - Create invoice
  - `POST /v2/invoices/{invoice_id}/publish` - Send invoice

### Team API
- **Purpose**: Staff management and permissions
- **Key Endpoints**:
  - `POST /v2/team-members` - Create team member
  - `POST /v2/wages/search` - Get wage settings

## Webhooks

### Event Types
- `payment.created`
- `payment.updated`
- `order.created`
- `order.updated`
- `customer.created`
- `customer.updated`
- `inventory.count.updated`
- `booking.created`
- `invoice.payment_made`

### Implementation
```python
import hmac
import hashlib

# Verify webhook signature
def verify_webhook_signature(request_body, signature, signature_key):
    hash = hmac.new(
        signature_key.encode('utf-8'),
        request_body,
        hashlib.sha256
    ).digest()
    computed_signature = base64.b64encode(hash).decode('utf-8')
    return hmac.compare_digest(computed_signature, signature)
```

## OAuth (Square Connect)

### Scopes
- `PAYMENTS_READ`, `PAYMENTS_WRITE`
- `ORDERS_READ`, `ORDERS_WRITE`
- `CUSTOMERS_READ`, `CUSTOMERS_WRITE`
- `INVENTORY_READ`, `INVENTORY_WRITE`
- `MERCHANT_PROFILE_READ`

### Authorization Flow
1. Redirect to `https://connect.squareup.com/oauth2/authorize`
2. User authorizes application
3. Exchange code for token at `https://connect.squareup.com/oauth2/token`
4. Store access_token and refresh_token

## SDKs and Tools

| Language | Package | Installation |
|----------|---------|--------------|
| Python | squareup | `pip install squareup` |
| Node.js | square | `npm install square` |
| Ruby | squareup | `gem install squareup` |
| PHP | square/square | `composer require square/square` |
| Java | com.squareup | Maven/Gradle |
| .NET | Square | NuGet |

## API Versioning

- Current Version: 2025-01-23
- Base URL: `https://connect.squareup.com/v2`
- Sandbox URL: `https://connect.squareupsandbox.com/v2`

## Rate Limits

- Default: 10 requests per second per app per location
- Burst: 20 requests
- Headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`

## Documentation

- Main Docs: developer.squareup.com
- API Explorer: developer.squareup.com/explorer
- GraphQL: graphql explorer available
- Postman: Official collection available
