# Standards & Reference

## 7.1 Official Documentation

- [Elasticsearch Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Elasticsearch: The Definitive Guide](https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html)
- [Elasticsearch API](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html)
- [Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html)
- [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html)
- [Aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html)
- [Cluster API](https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster.html)
- [Index Templates](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-templates.html)
- [ILM (Index Lifecycle Management)](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html)
- [Elasticsearch GitHub](https://github.com/elastic/elasticsearch)

## 7.2 Configuration Reference

### Index Settings

```json
PUT /my-index
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1,
    "refresh_interval": "1s",
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "porter_stem"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "title": { "type": "text", "analyzer": "my_analyzer" },
      "date": { "type": "date" },
      "count": { "type": "integer" }
    }
  }
}
```

### Cluster Settings

```json
PUT /_cluster/settings
{
  "persistent": {
    "indices.memory.index_buffer_size": "20%",
    "action.auto_create_index": true
  },
  "transient": {
    "cluster.routing.allocation.cluster_concurrent_rebalance": 2
  }
}
```

### Index Template

```json
PUT /_index_template/logs-template
{
  "index_patterns": ["logs-*"],
  "template": {
    "settings": {
      "number_of_shards": 1,
      "number_of_replicas": 1,
      "index.lifecycle.name": "logs-policy"
    },
    "mappings": {
      "properties": {
        "@timestamp": { "type": "date" },
        "message": { "type": "text" },
        "level": { "type": "keyword" },
        "service": { "type": "keyword" }
      }
    }
  }
}
```

## 7.3 Common Commands

### Index Operations

```bash
# Create index
curl -X PUT "localhost:9200/my-index" -H 'Content-Type: application/json' -d'

# Delete index
curl -X DELETE "localhost:9200/my-index"

# List indices
curl -X GET "localhost:9200/_cat/indices?v"

# Index stats
curl -X GET "localhost:9200/_stats"
```

### Document Operations

```bash
# Index document
curl -X PUT "localhost:9200/my-index/_doc/1" -H 'Content-Type: application/json' -d'
{ "title": "Example", "count": 42 }
'

# Bulk indexing
curl -X POST "localhost:9200/_bulk" -H 'Content-Type: application/x-ndjson' -d'
{"index":{"_index":"my-index"}}
{"title":"Doc 1","count":1}
{"index":{"_index":"my-index"}}
{"title":"Doc 2","count":2}
'

# Search
curl -X GET "localhost:9200/my-index/_search" -H 'Content-Type: application/json' -d'
{ "query": { "match": { "title": "example" } } }
'
```

## 7.4 Version Compatibility

| Version | Status | EOL | Key Features |
|---------|--------|-----|--------------|
| 8.x | Current | 2026 | Security enabled by default, new search engine |
| 7.x | Maintenance | 2024 | Deprecation of types, frozen indices |
| 6.x | EOL | 2023 | Parent/child removal, stricter mapping |

### Breaking Changes

- **8.x**: `content-type: application/json` required, security on by default
- **7.x**: `_type` deprecated, single type per index recommended
- **6.x**: Index lifecycle management improvements
