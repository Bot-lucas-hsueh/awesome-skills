# json Example

```
{
  "title": "Checkout Service Overview",
  "widgets": [
    {
      "id": 1,
      "type": "timeseries",
      "title": "Request Rate (per second)",
      "definition": {
        "requests": {
          "q": "sum:trace.checkout.request{service:checkout-api}.as_rate()",
          "style": { "palette": "dog_classic" }
        }
      }
    },
    {
      "id": 2,
      "type": "timeseries",
      "title": "Error Rate (%)",
      "definition": {
        "requests": {
          "q": "sum:trace.checkout.error{service:checkout-api}.as_rate() / sum:trace.checkout.request{service:checkout-api}.as_rate() * 100"
        }
      }
    },
    {
      "id": 3,
      "type": "service_map",
      "title": "Checkout Service Dependencies",
      "definition": {
        "service": "checkout-api",
        "filters": []
      }
    }
  ]
}
```
