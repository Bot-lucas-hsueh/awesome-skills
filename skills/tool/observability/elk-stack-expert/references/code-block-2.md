# Filebeat Configuration

```yaml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/*.log
      - /var/log/**/*.log
    json.keys_under_root: true
    json.add_error_key: true
    fields:
      log_type: application
      environment: production
    fields_under_root: true

  - type: docker
    enabled: true
    containers.ids:
      - '*'
    processors:
      - add_docker_metadata:
          host: "unix:///var/run/docker.sock"

processors:
  - add_host_metadata:
      when.not.contains.tags: forwarded
  - add_cloud_metadata: ~
  - add_docker_metadata: ~
  - add_kubernetes_metadata: ~

output.logstash:
  hosts: ["logstash:5044"]
  ssl.enabled: false

logging.level: info
logging.to_files: true
logging.files:
  path: /var/log/filebeat
  name: filebeat
  keepfiles: 7
  permissions: 0644
```
