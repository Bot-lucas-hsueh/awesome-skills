# Standards & Reference

## 7.1 Official Documentation

- [Elasticsearch Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)
- [Logstash Reference](https://www.elastic.co/guide/en/logstash/current/index.html)
- [Kibana Guide](https://www.elastic.co/guide/en/kibana/current/index.html)
- [Elastic Cloud Documentation](https://www.elastic.co/guide/en/cloud/current/index.html)
- [Beats Reference](https://www.elastic.co/guide/en/beats/libbeat/current/index.html)
- [Elastic Common Schema (ECS)](https://www.elastic.co/guide/en/ecs/current/index.html)

## 7.2 Configuration Reference

### Elasticsearch (elasticsearch.yml)

```yaml
cluster.name: my-cluster
node.name: node-1
path.data: /var/lib/elasticsearch
path.logs: /var/log/elasticsearch
network.host: 0.0.0.0
http.port: 9200
discovery.type: single-node
xpack.security.enabled: true
```

### Logstash (pipelines.yml)

```yaml
- pipeline.id: main
  path.config: "/etc/logstash/pipelines/main/*.conf"
  pipeline.workers: 4
  pipeline.batch.size: 125
  queue.type: persisted
  queue.max_bytes: 1gb
```

### Logstash Pipeline Example

```ruby
input {
  beats {
    port => 5044
  }
  tcp {
    port => 5000
    codec => json_lines
  }
}

filter {
  if [log_level] == "ERROR" {
    mutate {
      add_tag => ["alert"]
    }
  }
  date {
    match => ["timestamp", "ISO8601"]
    target => "@timestamp"
  }
  geoip {
    source => "client.ip"
  }
  useragent {
    source => "user_agent"
    target => "ua"
  }
}

output {
  elasticsearch {
    hosts => ["https://localhost:9200"]
    index => "app-logs-%{+YYYY.MM.dd}"
    user => "elastic"
    password => "${ES_PASSWORD}"
    ssl_certificate_verification => true
    cacert => "/etc/logstash/certs/ca.crt"
  }
  if "alert" in [tags] {
    email {
      to => "ops@example.com"
      from => "alerts@example.com"
      subject => "ERROR Alert: %{host}"
      body => "An error occurred: %{message}"
      via => "smtp"
      options => {
        address => "smtp.example.com"
        port => 587
        enable_starttls_auto => true
      }
    }
  }
}
```

### Kibana (kibana.yml)

```yaml
server.name: kibana
server.host: "0.0.0.0"
elasticsearch.hosts: ["https://localhost:9200"]
elasticsearch.username: "kibana_system"
elasticsearch.password: "${KIBANA_PASSWORD}"
elasticsearch.ssl.certificateAuthorities: ["/etc/kibana/certs/ca.crt"]
monitoring.ui.container.elasticsearch.enabled: true
```

## 7.3 Common Commands

### Elasticsearch

| Command | Description |
|---------|-------------|
| `GET /_cluster/health?wait_for_status=yellow&timeout=30s` | Check cluster health |
| `GET /_cat/nodes?v` | List nodes with stats |
| `GET /_cat/indices?v` | List all indices |
| `POST /_reindex` | Reindex documents |
| `POST /_ilm/explain_lifecycle/` | Check ILM status |
| `GET /_cluster/settings?include_defaults=true` | Get cluster settings |
| `PUT /_cluster/settings` | Update cluster settings |
| `POST /_security/user/admin/_disable` | Disable built-in user |
| `GET /_security/role` | List security roles |

### Logstash

| Command | Description |
|---------|-------------|
| `bin/logstash -f pipeline.conf --config.test_and_exit` | Test pipeline config |
| `bin/logstash -f pipeline.conf --log.level=debug` | Run with debug logging |
| `bin/logstash-plugin install` | Install plugins |
| `bin/logstash-plugin update` | Update plugins |
| `bin/logstash-keystore --create` | Create keystore for secrets |

### Kibana

| Command | Description |
|---------|-------------|
| `GET /_api/console/proxy?path=_cluster/health&method=GET` | API console proxy |
| `POST /_api/saved_objects/_import` | Import saved objects |
| `POST /_api/features` | Enable/disable features |

## 7.4 Version Compatibility

| Stack Version | Elasticsearch | Logstash | Kibana | Beats | Status |
|---------------|---------------|---------|--------|-------|--------|
| 8.x | 8.x | 8.x | 8.x | 8.x | Current |
| 7.17.x | 7.17.x | 7.17.x | 7.17.x | 7.17.x | LTS |
| 7.x | 7.x | 7.x | 7.x | 7.x | Maintenance |

### Breaking Changes in 8.x

- Java client required (REST client deprecated)
- API keys replaced role-based API keys
- Spaces are now Tenants in Elastic Cloud
- Transport layer security enabled by default
- Painless scripting sandboxed by default
- Searchable snapshots require specific tier

## 7.5 Index Lifecycle Management (ILM)

```json
{
  "policy": "hot-warm-delete",
  "phases": {
    "hot": {
      "min_age": "0ms",
      "actions": {
        "rollover": {
          "max_age": "7d",
          "max_primary_shard_size": "50gb"
        },
        "set_priority": 100
      }
    },
    "warm": {
      "min_age": "7d",
      "actions": {
        "set_priority": 50,
        "shrink": { "number_of_shards": 1 },
        "forcemerge": { "max_num_segments": 1 }
      }
    },
    "delete": {
      "min_age": "30d",
      "actions": {
        "delete": {}
      }
    }
  }
}
```

## 7.6 Security (XPack)

```yaml
xpack.security:
  enabled: true
  enrollment:
    enabled: false
  audit:
    outputs:
      - file
    events:
      exclude:
        - authentication_failed
  tls:
    verification_mode: certificate
```

### Role Mapping

```json
{
  "roles": ["superuser"],
  "rules": {
    "any": [
      { "field": { "groups": "cn=admins,ou=groups,dc=example,dc=com" } },
      { "field": { "username": "admin" } }
    ]
  },
  "enabled": true
}
```
