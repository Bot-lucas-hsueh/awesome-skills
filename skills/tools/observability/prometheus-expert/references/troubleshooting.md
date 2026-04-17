# Troubleshooting Guide

## 8.1 Prometheus Server

### Target Not Scraped
- Check target endpoint: `http://prometheus:9090/targets`
- Verify metrics path
- Check firewall rules
- Review scrape configs

### High Memory Usage
- Reduce retention period
- Reduce number of metrics
- Use recording rules

## 8.2 Exporters

### Exporter Not Working
- Check exporter logs
- Verify port accessible
- Test metrics: `curl localhost:9100/metrics`

## 8.3 Query Issues

### Query Not Returning Data
- Check time range
- Verify metric name
- Use EXPLAIN in query
- Check PromQL syntax

## 8.4 Alert Manager

### Alert Not Sent
- Check alert manager config
- Verify receiver config
- Review amtool check-config

## 8.5 Storage

### TSDB Issues
- Check disk space
- Review WAL size
- Run head compaction