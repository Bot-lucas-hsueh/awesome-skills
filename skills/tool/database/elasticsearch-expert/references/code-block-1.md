# json Example

```
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1,
    "analysis": {
      "analyzer": {
        "custom_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "stop", "snowball"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "standard",
        "fields": {
          "keyword": { "type": "keyword" },
          "autocomplete": {
            "type": "text",
            "analyzer": "autocomplete"
          }
        }
      },
      "content": {
        "type": "text",
        "analyzer": "standard"
      },
      "status": { "type": "keyword" },
      "created_at": { "type": "date" },
      "tags": { "type": "keyword" },
      "location": { "type": "geo_point" }
    }
  }
}
```
