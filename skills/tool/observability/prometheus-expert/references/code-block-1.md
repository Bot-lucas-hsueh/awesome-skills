# yaml Example

```
# Recommended scrape config with proper relabeling
scrape_configs:
  - job_name: 'application'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      # Only scrape pods with prometheus.io/scrape=true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: 'true'
      
      # Override metrics path
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: '(.+)'
      
      # Override port
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        target_label: __param_target
        regex: '(\d+)'
      
      # Normalize instance label
      - source_labels: [__meta_kubernetes_pod_ip]
        action: replace
        target_label: instance
      
      # Add labels from pod metadata
      - action: labelmap
        regex: __meta_kubernetes_pod_label_(.+)
      
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: namespace
```
