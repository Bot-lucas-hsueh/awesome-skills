# App Development Reference

## Overview

Shopify apps extend the platform's functionality. Apps can be:
- **Custom**: Built for a single merchant
- **Public**: Listed on the Shopify App Store
- **Private**: Unlisted, for specific partners

## App Architecture

### App Structure
```
my-shopify-app/
├── web/
│   ├── backend/           # Express/Fastify server
│   ├── frontend/          # React/Vue admin UI
│   └── extensions/        # Checkout/UI extensions
├── shopify.app.toml       # App configuration
└── package.json
```

### shopify.app.toml
```toml
name = "My Shopify App"
client_id = "your-client-id"
application_url = "https://your-app.com"
embedded = true

[auth]
redirect_urls = [
  "https://your-app.com/auth/callback",
  "https://your-app.com/auth/shopify/callback",
  "https://your-app.com/api/auth/callback"
]

[webhooks]
api_version = "2025-01"

[access_scopes]
# Learn more at https://shopify.dev/docs/apps/tools/cli/configuration#access_scopes
scopes = "read_products,write_orders,read_customers"

[access.admin]
direct_api_mode = "online"
embedded_app_incompatible_with_future_scopes = false
```

## OAuth Implementation

### Express.js OAuth Route
```typescript
import {shopifyApi, LATEST_API_VERSION} from '@shopify/shopify-api';
import express from 'express';

const shopify = shopifyApi({
  apiKey: process.env.SHOPIFY_API_KEY,
  apiSecretKey: process.env.SHOPIFY_API_SECRET,
  scopes: ['read_products', 'write_orders'],
  hostName: process.env.HOST.replace(/https:\/\//, ''),
  hostScheme: 'https',
  apiVersion: LATEST_API_VERSION,
  isEmbeddedApp: true,
  sessionStorage: new Shopify.Session.MongoDBSessionStorage(
    process.env.MONGODB_URI,
    'sessions'
  ),
});

// Start OAuth
app.get('/api/auth', async (req, res) => {
  const shop = shopify.utils.sanitizeShop(req.query.shop);
  
  await shopify.auth.begin({
    shop,
    callbackPath: '/api/auth/callback',
    isOnline: true,  // Online = user-specific, Offline = shop-wide
    rawRequest: req,
    rawResponse: res,
  });
});

// OAuth Callback
app.get('/api/auth/callback', async (req, res) => {
  const callback = await shopify.auth.callback({
    rawRequest: req,
    rawResponse: res,
  });

  const {session} = callback;
  
  // Register webhooks
  await shopify.webhooks.register({
    session,
    webhookHandlers: {
      ORDERS_CREATE: {
        deliveryMethod: DeliveryMethod.Http,
        callbackUrl: '/api/webhooks/orders',
        callback: orderHandler,
      },
      APP_UNINSTALLED: {
        deliveryMethod: DeliveryMethod.Http,
        callbackUrl: '/api/webhooks/app-uninstalled',
        callback: uninstallHandler,
      },
    },
  });

  // Redirect to embedded app
  res.redirect(`/?shop=${session.shop}&host=${req.query.host}`);
});
```

## Webhooks

### Webhook Handler
```typescript
import {Shopify} from '@shopify/shopify-api';

const orderHandler = async (
  topic: string,
  shop: string,
  body: string,
  webhookId: string,
): Promise<void> => {
  // Verify webhook is not duplicate
  const processed = await WebhookLog.findOne({webhookId});
  if (processed) {
    console.log(`Webhook ${webhookId} already processed`);
    return;
  }

  const payload = JSON.parse(body);
  
  // Process order
  await processOrder(shop, payload);
  
  // Log processed webhook
  await WebhookLog.create({
    webhookId,
    topic,
    shop,
    processedAt: new Date(),
  });
};

// Express webhook endpoint
app.post('/api/webhooks/:topic', express.text({type: '*/*'}), async (req, res) => {
  const {topic} = req.params;
  const shop = req.headers['x-shopify-shop-domain'];
  const hmac = req.headers['x-shopify-hmac-sha256'];
  
  // Verify HMAC
  const generatedHmac = crypto
    .createHmac('sha256', process.env.SHOPIFY_API_SECRET)
    .update(req.body, 'utf8')
    .digest('base64');
  
  if (generatedHmac !== hmac) {
    return res.status(401).send('Unauthorized');
  }

  // Process webhook asynchronously
  res.status(200).send('OK');
  
  // Queue for processing
  await webhookQueue.add({
    topic,
    shop,
    body: req.body,
    webhookId: req.headers['x-shopify-webhook-id'],
  });
});
```

## Admin API Operations

### GraphQL Admin API
```typescript
const client = new shopify.clients.Graphql({session});

// Create a product
const response = await client.request(`
  mutation productCreate($input: ProductInput!) {
    productCreate(input: $input) {
      product {
        id
        title
        handle
      }
      userErrors {
        field
        message
      }
    }
  }
`, {
  variables: {
    input: {
      title: 'New Product',
      descriptionHtml: '<p>Product description</p>',
      vendor: 'My Brand',
      productType: 'Widget',
      variants: [
        {
          price: '29.99',
          sku: 'WIDGET-001',
          inventoryQuantities: [
            {
              locationId: 'gid://shopify/Location/123456',
              availableQuantity: 100,
            },
          ],
        },
      ],
    },
  },
});

if (response.data.productCreate.userErrors.length > 0) {
  console.error('Errors:', response.data.productCreate.userErrors);
}
```

## App Bridge

### Embedded App Setup
```tsx
// App.tsx
import {AppProvider} from '@shopify/app-bridge-react';
import {NavigationMenu} from '@shopify/app-bridge-react/components/NavigationMenu';

const config = {
  apiKey: process.env.SHOPIFY_API_KEY,
  host: new URLSearchParams(window.location.search).get('host'),
  forceRedirect: true,
};

function App() {
  return (
    <AppProvider config={config}>
      <NavigationMenu
        navigationLinks={[
          {
            label: 'Dashboard',
            destination: '/',
          },
          {
            label: 'Settings',
            destination: '/settings',
          },
        ]}
      />
      <Page>
        <Layout>
          <Layout.Section>
            <Card>
              <Text variant="headingMd">Welcome to My App</Text>
            </Card>
          </Layout.Section>
        </Layout>
      </Page>
    </AppProvider>
  );
}
```

## Billing API

### Subscription Creation
```graphql
mutation appSubscriptionCreate($name: String!, $lineItems: [AppSubscriptionLineItemInput!]!, $returnUrl: URL!) {
  appSubscriptionCreate(name: $name, lineItems: $lineItems, returnUrl: $returnUrl) {
    appSubscription {
      id
      name
      status
    }
    confirmationUrl
    userErrors {
      field
      message
    }
  }
}
```

### Usage Charges
```graphql
mutation appUsageRecordCreate($subscriptionLineItemId: ID!, $description: String!, $price: MoneyInput!) {
  appUsageRecordCreate(subscriptionLineItemId: $subscriptionLineItemId, description: $description, price: $price) {
    appUsageRecord {
      id
      description
      price {
        amount
        currencyCode
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

## Best Practices

1. **Security**
   - Always verify webhook HMAC signatures
   - Store sensitive data encrypted
   - Use online access tokens for user-specific actions
   - Validate all user inputs

2. **Performance**
   - Process webhooks asynchronously
   - Implement request caching
   - Use bulk operations for large data imports
   - Monitor API rate limits

3. **Reliability**
   - Handle API failures gracefully
   - Implement retry logic with exponential backoff
   - Log all webhook deliveries
   - Monitor app health

4. **User Experience**
   - Follow Polaris design system
   - Provide clear error messages
   - Implement onboarding flows
   - Support mobile devices
