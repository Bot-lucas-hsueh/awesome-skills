# Log Analysis Dashboard

Complete example for analyzing logs with ELK stack.

## Index Pattern

```json
PUT /logs-%{YYYY.MM.dd}
{
  "mappings": {
    "properties": {
      "@timestamp": { "type": "date" },
      "level": { "type": "keyword" },
      "service": { "type": "keyword" },
      "message": { "type": "text" },
      "trace_id": { "type": "keyword" },
      "user_id": { "type": "keyword" },
      "duration_ms": { "type": "float" }
    }
  }
}
```

## Aggregation for Dashboard

```json
GET /logs-*/_search
{
  "size": 0,
  "query": {
    "range": {
      "@timestamp": { "gte": "now-24h" }
    }
  },
  "aggs": {
    "errors_by_service": {
      "terms": { "field": "service" },
      "aggs": {
        "error_count": {
          "filter": { "term": { "level": "ERROR" } }
        },
        "p99_latency": {
          "percentiles": {
            "field": "duration_ms",
            "percents": [50, 90, 99]
          }
        }
      }
    },
    "logs_over_time": {
      "date_histogram": {
        "field": "@timestamp",
        "fixed_interval": "5m"
      },
      "aggs": {
        "by_level": {
          "terms": { "field": "level" }
        }
      }
    }
  }
}
```

## Key Points

- Use date math in index names for time-based indices
- size: 0 returns only aggregations
- Percentiles help identify latency issues
- Date histogram shows logs over time
