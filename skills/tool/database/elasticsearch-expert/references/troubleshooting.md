# Troubleshooting

## 8.1 Connection Issues

### Cluster Unavailable

```bash
# Check cluster health
curl -X GET "localhost:9200/_cluster/health?pretty"

# Check node stats
curl -X GET "localhost:9200/_nodes/stats"

# Verify network
curl -X GET "localhost:9200/"
```

**Common causes:**
- Out of disk space (ES requires disk space for shard allocation)
- Network connectivity issues
- Java heap exhaustion
- Incorrect bind address in `elasticsearch.yml`

### Connection Timeout

```yaml
# elasticsearch.yml
network.host: 0.0.0.0
http.port: 9200
gateway.recover_after_nodes: 2
```

## 8.2 Performance Issues

### Slow Queries

```json
POST /my-index/_search
{
  "timeout": "5s",
  "query": { ... },
  "profile": true
}
```

**Solutions:**
- Increase `search.default_search_timeout`
- Use filter context instead of query context for exact matches
- Add docvalue_fields for sorting
- Reduce `max_result_window`

### High CPU/Load

```bash
# Check hot threads
curl -X GET "localhost:9200/_nodes/hot_threads"

# Check pending tasks
curl -X GET "localhost:9200/_cluster/pending_tasks"
```

**Common causes:**
- Too many segments (trigger merge: `POST /_forcemerge`)
- Unbounded pagination (`search.after` instead of `from/size`)
- Regex queries on keyword fields
- Missing filter cache

## 8.3 Shard Issues

### Unassigned Shards

```bash
# Diagnose unassigned shards
curl -X GET "localhost:9200/_cat/shards?v&h=index,shard,prirep,state,unassigned.reason"

# Force shard allocation
curl -X POST "localhost:9200/_cluster/reroute?retry_failed=true"
```

**Common reasons:**
- `INDEX_CREATED` — waiting for replicas
- `NODE_LEFT` — node left cluster
- `ALLOCATION_FAILED` — disk watermark exceeded

### Cluster Red Balance

```json
PUT /_cluster/settings
{
  "transient": {
    "cluster.routing.allocation.enable": "none"
  }
}
```

## 8.4 Memory Issues

### JVM Heap

```bash
# Check JVM memory
curl -X GET "localhost:9200/_nodes/stats/jvm?pretty"
```

**Recommendations:**
- Set heap to 50% of RAM, max 32GB (to use compressed oops)
- Leave other 50% for OS cache
- Set `-XX:+UseG1GC` for heap > 8GB

### Circuit Breaker

```json
PUT /_cluster/settings
{
  "persistent": {
    "indices.breaker.total.use_real_memory": false
  }
}
```

## 8.5 Mapping Issues

### Field Type Conflicts

```bash
# Check current mapping
curl -X GET "localhost:9200/my-index/_mapping?pretty"

# Reindex to change mapping
POST /_reindex
{
  "source": { "index": "old-index" },
  "dest": { "index": "new-index" }
}
```

### Dynamic Mapping Issues

```json
PUT /my-index
{
  "mappings": {
    "dynamic": "strict",
    "properties": { ... }
  }
}
```

## 8.6 Index Issues

### Index Alias

```bash
# Create alias
curl -X POST "localhost:9200/_aliases" -H 'Content-Type: application/json' -d'
{
  "actions": [
    { "add": { "index": "my-index-v1", "alias": "my-index" } }
  ]
}
'

# Switch alias
curl -X POST "localhost:9200/_aliases" -H 'Content-Type: application/json' -d'
{
  "actions": [
    { "remove": { "index": "my-index-v1", "alias": "my-index" } },
    { "add": { "index": "my-index-v2", "alias": "my-index" } }
  ]
}
'
```

### Rollover Index

```json
PUT /logs
{
  "aliases": {
    "logs-write": { "is_write_index": true }
  }
}

POST /logs-write/_rollover
{
  "conditions": {
    "max_age": "7d",
    "max_docs": 100000
  }
}
```
