# json Example

```
{
  "query": {
    "bool": {
      "must": [
        { "match": { "title": "search query" } }
      ],
      "should": [
        { "match": { "description": { "query": "search", "boost": 2 } } }
      ],
      "filter": [
        { "term": { "status": "published" } },
        { "range": { "created_at": { "gte": "now-1M" } } }
      ],
      "must_not": [
        { "term": { "featured": true } }
      ],
      "minimum_should_match": 1
    }
  },
  "post_filter": {
    "terms": { "category": ["tech", "news"] }
  },
  "highlight": {
    "fields": {
      "title": {},
      "content": { "fragment_size": 150 }
    }
  },
  "aggs": {
    "categories": {
      "terms": { "field": "category", "size": 10 }
    }
  }
}
```
