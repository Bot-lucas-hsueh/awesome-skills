# json Example

```
{
  "aggs": {
    "sales_over_time": {
      "date_histogram": {
        "field": "date",
        "calendar_interval": "month"
      },
      "aggs": {
        "revenue": { "sum": { "field": "amount" } },
        "avg_price": { "avg": { "field": "price" } }
      }
    },
    "top_categories": {
      "terms": {
        "field": "category",
        "size": 5,
        "order": { "revenue": "desc" }
      },
      "aggs": {
        "revenue": { "sum": { "field": "amount" } }
      }
    },
    "price_ranges": {
      "range": {
        "field": "price",
        "ranges": [
          { "key": "budget", "to": 50 },
          { "key": "mid", "from": 50, "to": 200 },
          { "key": "premium", "from": 200 }
        ]
      }
    }
  }
}
```
