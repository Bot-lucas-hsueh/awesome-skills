# ILM, Logstash Pipeline & Index Template

## Index Lifecycle Management (ILM)

```json
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_age": "1d",
            "max_primary_shard_size": "50gb"
          }
        }
      },
      "warm": {
        "min_age": "30d",
        "actions": {
          "shrink": { "number_of_shards": 1 },
          "forcemerge": { "max_num_segments": 1 }
        }
      },
      "cold": {
        "min_age": "60d",
        "actions": {
          "freeze": {}
        }
      },
      "delete": {
        "min_age": "365d",
        "actions": {
          "delete": {}
        }
      }
    }
  }
}
```

## Logstash Pipeline Pattern

```ruby
input {
  beats {
    port => 5044
    host => "0.0.0.0"
  }
  tcp {
    port => 5000
    codec => json_lines
  }
}

filter {
  if [log_type] == "json" {
    json {
      source => "message"
      target => "parsed"
    }
  } else {
    grok {
      match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{DATA:service} - %{GREEDYDATA:msg}" }
    }
    date {
      match => [ "timestamp", "ISO8601" ]
      target => "@timestamp"
    }
  }
  
  mutate {
    add_field => { "[@metadata][index_prefix]" => "app-logs" }
  }
  
  if [level] == "ERROR" or [level] == "WARN" {
    mutate {
      add_tag => [ "alert" ]
    }
  }
}

output {
  if "alert" in [tags] {
    elasticsearch {
      hosts => ["http://elasticsearch:9200"]
      index => "%{[@metadata][index_prefix]}-alert-%{+YYYY.MM.dd}"
    }
  } else {
    elasticsearch {
      hosts => ["http://elasticsearch:9200"]
      index => "%{[@metadata][index_prefix]}-%{+YYYY.MM.dd}"
      ilm_enabled => true
      ilm_rollover_alias => "app-logs"
      ilm_pattern => "000001"
      ilm_policy => "app-logs-policy"
    }
  }
}
```

## Elasticsearch Index Template

```json
{
  "index_patterns": ["app-logs-*"],
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1,
    "index.lifecycle.name": "app-logs-policy",
    "index.lifecycle.rollover_alias": "app-logs"
  },
  "mappings": {
    "properties": {
      "@timestamp": { "type": "date" },
      "level": { "type": "keyword" },
      "service": { "type": "keyword" },
      "message": { "type": "text", "fields": { "keyword": { "type": "keyword" } } },
      "trace.id": { "type": "keyword" },
      "span.id": { "type": "keyword" },
      "user.id": { "type": "keyword" },
      "host": { "type": "ip" },
      "url.path": { "type": "keyword" },
      "http.status_code": { "type": "short" }
    }
  }
}
```
