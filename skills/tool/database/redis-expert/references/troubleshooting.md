# Troubleshooting

## 8.1 Connection Issues

### Connection Refused

```bash
# Check if Redis is running
redis-cli ping
# Expected: PONG

# Check config
redis-cli CONFIG GET bind
redis-cli CONFIG GET port

# Test connection
redis-cli -h localhost -p 6379
redis-cli -a password PING
```

**Common causes:**
- Redis not running: `redis-server`
- Wrong bind address
- Firewall blocking port
- Password mismatch

### Authentication Issues

```bash
# Test with password
redis-cli -a password PING

# Authenticate in session
AUTH username password

# Check ACLs (Redis 6+)
AUTH default password
```

## 8.2 Memory Issues

### Out of Memory (OOM)

```bash
# Check memory usage
redis-cli INFO memory
redis-cli MEMORY STATS

# Find big keys
redis-cli --bigkeys
redis-cli --scan | head -100 | redis-cli --bigkeys

# Memory breakdown
redis-cli MEMORY DOCTOR
```

**Solutions:**

```conf
# redis.conf - set eviction policy
maxmemory 2gb
maxmemory-policy allkeys-lru

# Available policies:
# noeviction, allkeys-lru, volatile-lru, allkeys-random
# volatile-random, volatile-ttl, allkeys-lfu, volatile-lfu
```

### Memory Fragmentation

```bash
# Check fragmentation
redis-cli INFO memory | grep mem_fragmentation_ratio
# Ratio > 1.5 means fragmentation

# Defragment (Redis 4+)
redis-cli CONFIG SET activedefrag yes
redis-cli CONFIG SET active-defrag-threshold-lower 10
redis-cli CONFIG SET active-defrag-threshold-upper 100
```

## 8.3 Performance Issues

### Slow Commands

```bash
# Check slowlog
redis-cli SLOWLOG GET 10
redis-cli SLOWLOG LEN
redis-cli SLOWLOG RESET

# Set slowlog threshold
redis-cli CONFIG SET slowlog-log-slower-than 10000  # microseconds
```

**Common slow commands:**
- `KEYS` — O(N), use SCAN instead
- `SMEMBERS` — O(N), use SSCAN
- `SORT` — O(N log N)
- `HGETALL` — O(N), use HSCAN

### Latency

```bash
# Measure latency
redis-cli --latency
redis-cli --latency-history
redis-cli --latency-dist

# Test round trip
redis-cli --intrinsic-latency 100
```

**Common causes:**
- Slow commands
- Memory swapping
- AOF fsync blocking
- Large objects
- Network issues

## 8.4 Persistence Issues

### AOF Rewrite Problems

```bash
# Check AOF status
redis-cli INFO persistence

# Force rewrite
redis-cli BGREWRITEAOF

# Check if running
redis-cli LASTSAVE
redis-cli BGREWRITEAOF
```

### RDB vs AOF

```conf
# RDB only (faster, less durable)
save 900 1
save 300 10
save 60 10000
appendonly no

# AOF only (slower, more durable)
appendonly yes
appendfsync everysec
appendfsync always     # slowest, safest
appendfsync no        # fastest, unsafe

# Both (best of both)
save 900 1
save 300 10
save 60 10000
appendonly yes
appendfsync everysec
```

## 8.5 Cluster Issues

### Cluster Node Down

```bash
# Check cluster status
redis-cli -c CLUSTER INFO
redis-cli -c CLUSTER NODES
redis-cli -c CLUSTER SLOTS

# Meet new node
redis-cli CLUSTER MEET ip port

# Replicate master
redis-cli CLUSTER REPLICATE node_id

# Failover
redis-cli CLUSTER FAILOVER
```

### Slot Migration

```bash
# Check slot distribution
redis-cli CLUSTER SLOTS

# Reshard
redis-cli --cluster reshard host:port \
    --cluster-from source_node_id \
    --cluster-to target_node_id \
    --cluster-slots 1000 \
    --cluster-yes

# Set slot ownership
redis-cli CLUSTER ADDSLOTS 5461
redis-cli CLUSTER DELSLOTS 5461
```

## 8.6 Replication Issues

### Replica Sync

```bash
# Check replication status
redis-cli INFO replication

# Full sync
redis-cli REPLICAOF host port
redis-cli REPLICAOF NO ONE  # stop replica

# Check backlog
redis-cli CONFIG GET repl-backlog-size
redis-cli INFO replication | grep repl_backlog
```

### Handling OOM During Replication

```conf
# Replica config
replica-read-only yes
repl-diskless-sync no
replica-lazy-flush no

# Memory headroom
maxmemory 1500mb
```

## 8.7 Lua Script Issues

```bash
# Test script
redis-cli EVAL "return redis.call('GET', KEYS[1])" 1 mykey

# Check script memory
redis-cli SCRIPT EXISTS hash
redis-cli SCRIPT LOAD "return 'hello'"
redis-cli SCRIPT FLUSH

# Memory limit for scripts
redis-cli CONFIG SET lua-time-limit 5000  # milliseconds
```
