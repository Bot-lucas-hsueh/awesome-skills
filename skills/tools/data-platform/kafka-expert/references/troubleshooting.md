# Troubleshooting Guide

## 8.1 Broker Issues

### Broker Not Starting
- Check Kafka logs: `logs/kafka-server.log`
- Verify Zookeeper running (if using external ZK)
- Check port 9092 not in use
- Verify heap memory settings in `kafka-server-start.sh`

### Broker Out of Memory
- Increase heap: `export KAFKA_HEAP_OPTS="-Xmx4g -Xms4g"`
- Check JVM garbage collection settings

## 8.2 Producer Issues

### Messages Not Delivered
- Check broker connectivity: `telnet localhost 9092`
- Verify topic exists: `kafka-topics.sh --list`
- Check acks configuration: `acks=all` for guarantee
- Review producer logs

### Duplicate Messages
- Enable idempotence: `enable.idempotence=true`
- Configure proper `retries` and `delivery.timeout.ms`

## 8.3 Consumer Issues

### Consumer Lag
- Check consumer group: `kafka-consumer-groups.sh --describe`
- Add more partitions or consumers
- Increase fetch sizes
- Check processing time

### Rebalance Storm
- Use static membership: `group.instance.id`
- Avoid frequent joins
- Set `session.timeout.ms` appropriately

## 8.4 Topic Issues

### Topic Creation Fails
- Check Zookeeper connectivity
- Verify topic name valid (no special chars)
- Check `auto.create.topics.enable`

### Partition Leader Not Available
- Check broker health
- Wait for leader election
- Use `kafka-leader-election.sh`

## 8.5 Connect Issues

### Connector Not Running
- Check connector config
- Review connect logs
- Verify worker.properties settings

## 8.6 Performance Issues

### High Latency
- Enable compression: `compression.type=snappy`
- Use larger batch sizes
- Tune `linger.ms`
- Check network throughput

### Disk Space Issues
- Configure retention: `retention.ms`, `retention.bytes`
- Add cleanup policy: `cleanup.policy=delete|compact`
- Run log compaction

## 8.6 Diagnostic Commands

```bash
# List topics
kafka-topics.sh --bootstrap-server localhost:9092 --list

# Describe topic
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic my-topic

# Consumer group lag
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group my-group --describe

# Test produce
kafka-console-producer.sh --broker-list localhost:9092 --topic test

# Test consume
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```