# Standard Workflow

## 8.1 Getting Started

```
Phase 1: Local Development Setup
├── Download Elasticsearch, Logstash, Kibana (or use Docker)
├── Start Elasticsearch single-node cluster
├── Install Beats (Filebeat, Metricbeat, etc.)
├── Configure Filebeat to ship logs
└── Verify data in Kibana

Phase 2: Index and Search Configuration
├── Create index templates with ILM policies
├── Configure index mappings for custom fields
├── Set up Kibana index patterns
├── Create sample visualizations
└── Build initial dashboards

Phase 3: Production Deployment
├── Design cluster topology (hot-warm-cold)
├── Configure security (TLS, roles, API keys)
├── Set up monitoring for the stack itself
├── Configure Logstash pipelines with Dead Letter Queue
├── Set up alerting rules
└── Document runbooks
```

## 8.2 Common Workflows

### New Data Source Integration

1. **Identify the data source** (application logs, metrics, network flows)
2. **Choose the right Beats shipper** or direct input
3. **Configure the input** with appropriate fields and processors
4. **Test the pipeline** with `--config.test_and_exit`
5. **Create index template** with ILM policy
6. **Verify data ingestion** using Kibana Discover or `_cluster/stats`
7. **Create visualizations** for key metrics
8. **Add alerting rule** for anomalies or thresholds

### Search and Analysis Workflow

1. **Kibana Dev Tools** for quick queries and aggregations
2. **Discover** for log exploration with filters
3. **Visualize** builder for charts and graphs
4. **Dashboard** assembly with drill-down links
5. **Canvas** for presentation-ready data stories
6. **Maps** for geoIP enriched data

### Index Migration

1. **Create new index** with updated mappings
2. **Reindex with Painless script** for field transformations
3. **Update alias** atomically (atomic swap)
4. **Verify documents** count and data integrity
5. **Delete old index** after retention period

### Disaster Recovery

1. **Automated snapshots** to shared repository
2. **Cross-cluster replication** for zero RPO
3. **Document-level replication** with reindex
4. **Restore procedures** tested quarterly

## 8.3 Development Workflow with Docker

```bash
# Start full stack
docker network create elastic
docker run -d --name es01 --net elastic -p 9200:9200 -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=true" \
  -e "ELASTIC_PASSWORD=changeme" \
  docker.elastic.co/elasticsearch/elasticsearch:8.12.0

docker run -d --name logstash --net elastic -p 5044:5044 \
  docker.elastic.co/logstash/logstash:8.12.0

docker run -d --name kibana --net elastic -p 5601:5601 \
  -e "ELASTICSEARCH_HOSTS=http://es01:9200" \
  -e "ELASTICSEARCH_USERNAME=kibana_system" \
  -e "ELASTICSEARCH_PASSWORD=changeme" \
  docker.elastic.co/kibana/kibana:8.12.0
```

## 8.4 Deployment with Elasticsearch Operator (ECK)

```yaml
apiVersion: elasticsearch.k8s.elastic.co/v1
kind: Elasticsearch
metadata:
  name: production
spec:
  version: 8.12.0
  nodeSets:
    - name: hot-nodes
      count: 3
      config:
        node.roles: ["master", "data", "ingest"]
        node.attr.hot: "true"
      volumeClaimTemplates:
        - metadata:
            name: elasticsearch-data
          spec:
            accessModes: ["ReadWriteOnce"]
            resources:
              requests:
                storage: 100Gi
  secureSettings:
    - secretName: elastic-credentials
```

## 8.5 Testing Workflow

```bash
# Unit test Logstash filter
bin/logstash -f test-pipeline.conf --config.test_and_exit

# Integration test with Docker Compose
docker-compose up -d --build

# Check pipeline health
curl -X GET "localhost:9600/_node/stats/pipelines?pretty"

# Monitor ingestion rate
GET _cat/indices?v&h=index,health,docs.count,store.size,pri.store.size
```

## 8.6 Monitoring the Stack Itself

```yaml
# metricbeat.yml for Elastic Stack monitoring
metricbeat.modules:
  - module: elasticsearch
    metricsets: ["node", "node_stats"]
    period: 10s
    hosts: ["https://localhost:9200"]
    username: "beats_system"
    password: "${BEATS_PASSWORD}"
    ssl.enabled: true
    ssl.certificate_authorities: ["/etc/metricbeat/certs/ca.crt"]

  - module: logstash
    metricsets: ["node", "node_stats", "pipeline"]
    period: 10s
    hosts: ["localhost:9600"]
```
