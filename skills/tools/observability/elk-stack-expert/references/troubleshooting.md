# Troubleshooting Guide

## 8.1 Logstash Pipeline Issues

### Pipeline Not Starting
- Check pipeline syntax: `logstash -f pipeline.conf --config.test_and_exit`
- Verify input/output plugins available
- Check pipeline.yml configuration

### Data Not Flowing
- Check Logstash logs
- Verify input source accessible
- Check filter processing

## 8.2 Elasticsearch Issues

### Index Not Created
- Verify cluster health: `GET /_cluster/health`
- Check shard allocation
- Review index settings

### Query Timeout
- Add proper mappings
- Use routing for large queries
- Optimize query DSL

## 8.3 Kibana Issues

### Dashboard Not Loading
- Check index pattern exists
- Verify time field configured
- Clear browser cache

## 8.4 Beats Issues

### Filebeat Not Sending
- Check filebeat.yml config
- Verify file permissions
- Use: `filebeat test config`

## 8.5 Performance Issues

### High Memory Usage
- Adjust JVM heap in jvm.options
- Use pipelines for isolation
- Optimize filters