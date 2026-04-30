# yaml Example

```
global:
  resolve_timeout: 5m
  smtp_smarthost: 'smtp.example.com:587'
  smtp_from: 'alerts@example.com'
  smtp_auth_username: 'alerts'
  smtp_auth_identity: 'alerts'
  smtp_auth_password: '${SMTP_PASSWORD}'
  slack_api_url: 'https://hooks.slack.com/services/XXX/YYY/ZZZ'

templates:
  - /etc/alertmanager/template/*.tmpl

route:
  group_by: ['alertname', 'service', 'namespace']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: default
  routes:
    # Critical alerts go to PagerDuty
    - match:
        severity: critical
      receiver: pagerduty-critical
      continue: true
    
    # Team routing
    - match:
        team: platform
      receiver: slack-platform
      routes:
        - match:
            severity: critical
          receiver: pagerduty-platform
    
    - match:
        team: backend
      receiver: slack-backend
    
    # Kubernetes alerts
    - match:
        kind: Kubernetes
      receiver: slack-platform

receivers:
  - name: 'default'
    slack_configs:
      - channel: '#alerts-default'
        send_resolved: true
        title: '{{ range .Alerts }}{{ .Annotations.summary }}\n{{ end }}'
        text: |
          {{ range .Alerts }}
          *Alert:* {{ .Annotations.summary }}
          *Description:* {{ .Annotations.description }}
          *Labels:* {{ range .Labels.SortedPairs }}`{{ .Name }}="{{ .Value }}"` {{ end }}
          {{ if .Annotations.runbook_url }}*Runbook:* {{ .Annotations.runbook_url }}{{ end }}
          {{ end }}

  - name: 'pagerduty-critical'
    pagerduty_configs:
      - service_key: '${PAGERDUTY_SERVICE_KEY}'
        severity: critical
        component: prometheus
        group: '{{ .GroupLabels.alertname }}'
        class: '{{ .Labels.alertname }}'
        details:
          summary: '{{ .GroupLabels.alertname }}'
          description: '{{ range .Alerts }}{{ .Annotations.description }}{{ end }}'

  - name: 'pagerduty-platform'
    pagerduty_configs:
      - service_key: '${PAGERDUTY_PLATFORM_KEY}'
        severity: critical
        component: prometheus
        group: platform

  - name: 'slack-platform'
    slack_configs:
      - channel: '#alerts-platform'
        send_resolved: true
        title: 'Prometheus Alert: {{ .GroupLabels.alertname }}'
        text: |
          {{ range .Alerts }}
          *{{ .Labels.severity | toUpper }}*: {{ .Annotations.summary }}
          {{ .Annotations.description }}
          {{ if .Annotations.runbook_url }}*Runbook:* {{ .Annotations.runbook_url }}{{ end }}
          {{ end }}

  - name: 'slack-backend'
    slack_configs:
      - channel: '#alerts-backend'
        send_resolved: true

inhibit_rules:
  # Inhibit warning if critical alert is active
  - source_match:
      severity: 'critical'
    target_match:
      severity: 'warning'
    equal: ['alertname', 'service', 'namespace']
```
