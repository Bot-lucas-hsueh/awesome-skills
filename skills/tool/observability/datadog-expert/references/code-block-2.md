# json Example

```
{
  "name": "Checkout Flow",
  "type": "browser",
  "subtype": "multi",
  "locations": ["aws:us-east-1", "aws:eu-west-1"],
  "tags": ["checkout", "critical"],
  "steps": [
    {
      "name": "Navigate to product",
      "type": "goToUrl",
      "url": "https://shop.example.com/product/123"
    },
    {
      "name": "Add to cart",
      "type": "click",
      "target": "button[data-testid='add-to-cart']"
    },
    {
      "name": "Proceed to checkout",
      "type": "click",
      "target": "a[data-testid='checkout-btn']"
    },
    {
      "name": "Verify checkout page",
      "type": "assertElementPresent",
      "target": "h1[data-testid='checkout-title']"
    }
  ],
  "options": {
    "retry": { "count": 3, "interval": 300 },
    "ci": { "executionRule": "blocked" }
  }
}
```
