# Checkout Extensions Reference

## Overview

Checkout Extensibility allows developers to customize Shopify checkout using:
- **Checkout UI Extensions**: Add custom UI components
- **Shopify Functions**: Implement custom business logic
- **Web Pixel Extensions**: Track customer behavior

## Checkout UI Extensions

### Extension Configuration
```toml
# extensions/checkout-ui/shopify.extension.toml
name = "Checkout Customization"
type = "checkout_ui_extension"
api_version = "2025-01"

[capabilities]
api_access = true
block_progress = true
network_access = true

[settings]
[[settings.fields]]
key = "banner_title"
name = "Banner Title"
type = "single_line_text_field"
[[settings.fields]]
key = "banner_message"
name = "Banner Message"
type = "multi_line_text_field"
```

### React Extension Component
```tsx
// extensions/checkout-ui/src/Checkout.tsx
import {
  useApi,
  useExtensionEditor,
  useTranslate,
  reactExtension,
  Banner,
  BlockStack,
  Text,
  Button,
} from '@shopify/ui-extensions-react/checkout';

export default reactExtension('purchase.checkout.block.render', () => <Extension />);

function Extension() {
  const {shop, sessionToken, settings} = useApi('purchase.checkout.block.render');
  const t = useTranslate();
  const isEditor = useExtensionEditor();

  const handleClick = async () => {
    const token = await sessionToken.get();
    
    // Call your backend
    const response = await fetch('https://your-api.com/validate', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        shop: shop.name,
      }),
    });

    const data = await response.json();
    console.log('Validation result:', data);
  };

  return (
    <BlockStack spacing="loose">
      <Banner title={settings.banner_title || 'Special Offer'} status="info">
        <Text>
          {settings.banner_message || 'Add $25 more for free shipping!'}
        </Text>
      </Banner>
      
      <Button onPress={handleClick}>
        Apply Discount
      </Button>
    </BlockStack>
  );
}
```

### Extension Targets

| Target | Location |
|--------|----------|
| `purchase.checkout.block.render` | Main checkout body |
| `purchase.checkout.contact.render-after` | After contact form |
| `purchase.checkout.delivery-address.render-before` | Before shipping address |
| `purchase.checkout.payment-method-list.render-before` | Before payment options |
| `purchase.checkout.cart-line-list.render-after` | After cart items |
| `purchase.thank-you.block.render` | Thank you page |
| `customer-account.order-details.block.render` | Order details page |

### Reading Checkout Data
```tsx
import {
  useApi,
  useCartLines,
  useShippingAddress,
  useTotalAmount,
  useApplyDiscountCode,
} from '@shopify/ui-extensions-react/checkout';

function Extension() {
  const cartLines = useCartLines();
  const shippingAddress = useShippingAddress();
  const totalAmount = useTotalAmount();
  const applyDiscountCode = useApplyDiscountCode();

  const subtotal = cartLines.reduce((sum, line) => {
    return sum + (line.cost.totalAmount.amount * line.quantity);
  }, 0);

  const handleApplyDiscount = () => {
    applyDiscountCode.change('FREESHIP2024');
  };

  return (
    <BlockStack>
      <Text>Subtotal: ${subtotal.toFixed(2)}</Text>
      <Text>Total: {totalAmount.amount} {totalAmount.currencyCode}</Text>
      
      {shippingAddress && (
        <Text>
          Shipping to: {shippingAddress.city}, {shippingAddress.countryCode}
        </Text>
      )}
    </BlockStack>
  );
}
```

## Shopify Functions

### Product Discount Function (Rust)
```rust
// extensions/product-discount/src/main.rs
use shopify_function::prelude::*;
use shopify_function::Result;

#[derive(Serialize, Deserialize, Default, PartialEq)]
struct Configuration {
    discount_percentage: f64,
    minimum_quantity: i64,
}

#[shopify_function_target]
fn generate_cart_run(input: input::ResponseData) -> Result<output::FunctionRunResult> {
    let config: Configuration = input
        .discount_node
        .and_then(|node| node.metafield)
        .and_then(|metafield| metafield.value)
        .map(|value| serde_json::from_str(&value).unwrap_or_default())
        .unwrap_or(Configuration {
            discount_percentage: 10.0,
            minimum_quantity: 2,
        });

    let mut targets = vec![];

    for line in &input.cart.lines {
        if line.quantity >= config.minimum_quantity {
            targets.push(output::Target {
                product_variant: Some(output::ProductVariantTarget {
                    id: line.id.clone(),
                    quantity: None, // Discount entire line
                }),
                order_subtotal: None,
            });
        }
    }

    if targets.is_empty() {
        return Ok(output::FunctionRunResult {
            discounts: vec![],
            discount_application_strategy: output::DiscountApplicationStrategy::FIRST,
        });
    }

    Ok(output::FunctionRunResult {
        discounts: vec![output::Discount {
            message: Some(format!("{}% Bulk Discount", config.discount_percentage)),
            targets,
            value: output::Value {
                percentage: Some(output::Percentage {
                    value: config.discount_percentage,
                }),
                fixed_amount: None,
                percentage_bundles: None,
                fixed_amount_bundles: None,
            },
        }],
        discount_application_strategy: output::DiscountApplicationStrategy::FIRST,
    })
}
```

### Input Query
```graphql
query Input($discountNodeId: ID!) {
  cart {
    lines {
      id
      quantity
      cost {
        amountPerQuantity {
          amount
        }
      }
    }
  }
  discountNode(id: $discountNodeId) {
    metafield(namespace: "custom", key: "function_configuration") {
      value
    }
  }
}
```

### Function Types

| Function Type | Use Case |
|--------------|----------|
| `product_discounts` | Discount specific products/variants |
| `order_discounts` | Discount entire order |
| `shipping_discounts` | Discount shipping rates |
| `payment_customization` | Hide/reorder payment methods |
| `delivery_customization` | Hide/reorder delivery options |
| `cart_transform` | Modify cart line items |
| `cart_checkout_validation` | Block checkout progress |

## Web Pixel Extensions

### Customer Events Tracking
```javascript
// extensions/web-pixel/src/index.js
import {register} from '@shopify/web-pixels-extension';

register(({configuration, analytics, browser}) => {
  // Initialize third-party tracking
  const trackingId = configuration.tracking_id;
  
  // Load external script
  const script = document.createElement('script');
  script.src = `https://tracking.example.com/script.js?id=${trackingId}`;
  document.head.appendChild(script);

  // Subscribe to events
  analytics.subscribe('page_viewed', (event) => {
    console.log('Page viewed:', event.context.document.location.pathname);
    
    // Send to your analytics
    window.tracker.pageView({
      path: event.context.document.location.pathname,
      title: event.context.document.title,
      timestamp: event.timestamp,
    });
  });

  analytics.subscribe('product_viewed', (event) => {
    const {product} = event.data;
    
    window.tracker.track('ViewContent', {
      content_ids: [product.id],
      content_name: product.title,
      content_type: 'product',
      currency: product.price.currency,
      value: product.price.amount,
    });
  });

  analytics.subscribe('product_added_to_cart', (event) => {
    const {cartLine} = event.data;
    
    window.tracker.track('AddToCart', {
      content_ids: [cartLine.merchandise.product.id],
      content_name: cartLine.merchandise.product.title,
      currency: cartLine.cost.totalAmount.currency,
      value: cartLine.cost.totalAmount.amount,
      quantity: cartLine.quantity,
    });
  });

  analytics.subscribe('checkout_started', (event) => {
    const {checkout} = event.data;
    
    window.tracker.track('InitiateCheckout', {
      currency: checkout.currencyCode,
      value: checkout.totalPrice.amount,
      num_items: checkout.lineItems.length,
    });
  });

  analytics.subscribe('checkout_completed', (event) => {
    const {checkout} = event.data;
    
    window.tracker.track('Purchase', {
      transaction_id: checkout.order.id,
      currency: checkout.currencyCode,
      value: checkout.totalPrice.amount,
      items: checkout.lineItems.map(item => ({
        id: item.variant.product.id,
        name: item.variant.product.title,
        quantity: item.quantity,
        price: item.variant.price.amount,
      })),
    });
  });
});
```

### Web Pixel Events

| Event | Trigger |
|-------|---------|
| `page_viewed` | Page load |
| `product_viewed` | Product page viewed |
| `collection_viewed` | Collection page viewed |
| `product_added_to_cart` | Add to cart button clicked |
| `cart_viewed` | Cart page viewed |
| `checkout_started` | Checkout initiated |
| `checkout_address_info_submitted` | Shipping address entered |
| `checkout_contact_info_submitted` | Contact info entered |
| `checkout_shipping_info_submitted` | Shipping method selected |
| `payment_info_submitted` | Payment info entered |
| `checkout_completed` | Order placed |

## Best Practices

1. **Performance**
   - Keep UI extensions lightweight
   - Minimize external API calls
   - Cache data where possible
   - Use server-side rendering for complex logic

2. **Security**
   - Never expose API keys in client code
   - Use session tokens for API authentication
   - Validate all user inputs
   - Follow principle of least privilege

3. **User Experience**
   - Match Shopify's design patterns
   - Provide clear loading states
   - Handle errors gracefully
   - Support all checkout steps

4. **Testing**
   - Test in development store
   - Verify behavior with different cart states
   - Test checkout completion flow
   - Validate discount calculations
