# E-commerce Product Search

Complete example for building product search with Elasticsearch.

## Index Design

```json
PUT /products
{
  "settings": {
    "number_of_shards": 2,
    "number_of_replicas": 1,
    "analysis": {
      "analyzer": {
        "autocomplete": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "autocomplete_filter"]
        }
      },
      "filter": {
        "autocomplete_filter": {
          "type": "edge_ngram",
          "min_gram": 2,
          "max_gram": 20
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "name": {
        "type": "text",
        "analyzer": "standard",
        "fields": {
          "keyword": { "type": "keyword" },
          "autocomplete": { "type": "text", "analyzer": "autocomplete" }
        }
      },
      "brand": { "type": "keyword" },
      "price": { "type": "float" },
      "categories": { "type": "keyword" },
      "in_stock": { "type": "boolean" }
    }
  }
}
```

## Search Query

```json
GET /products/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "multi_match": {
            "query": "wireless headphones",
            "fields": ["name^3", "brand^2", "categories"],
            "type": "best_fields"
          }
        }
      ],
      "filter": [
        { "term": { "in_stock": true } },
        { "range": { "price": { "gte": 50, "lte": 200 } } }
      ]
    }
  },
  "aggs": {
    "brands": { "terms": { "field": "brand", "size": 10 } },
    "price_ranges": {
      "range": {
        "field": "price",
        "ranges": [
          { "key": "Under $50", "to": 50 },
          { "key": "$50-$100", "from": 50, "to": 100 },
          { "key": "$100+", "from": 100 }
        ]
      }
    }
  }
}
```

## Key Points

- Use edge_ngram for autocomplete functionality
- Boost name field (^3) for higher relevance
- Use filter context for non-scoring queries (price range, in_stock)
- Aggregations provide faceted navigation
