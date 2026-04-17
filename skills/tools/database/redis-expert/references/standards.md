# Standards & Reference

## 7.1 Official Documentation

- [Redis Documentation](https://redis.io/docs/)
- [Redis Commands](https://redis.io/commands)
- [Redis Cluster](https://redis.io/docs/management/scaling/)
- [Redis Persistence](https://redis.io/docs/management/persistence/)
- [Redis Security](https://redis.io/docs/management/security/)
- [Redis Streams](https://redis.io/docs/data-types/streams/)
- [Redis Pub/Sub](https://redis.io/docs/interact/pubsub/)
- [Redis Memory Optimization](https://redis.io/docs/management/optimization/memory-optimization/)
- [Redis Configuration](https://redis.io/docs/management/config/)
- [Redis Sentinel](https://redis.io/docs/management/sentinel/)

## 7.2 Configuration Reference

### redis.conf

```conf
# Network
bind 127.0.0.1
port 6379
timeout 300
tcp-keepalive 60

# General
daemonize no
supervised no
pidfile /var/run/redis_6379.pid
loglevel notice
logfile ""

# Snapshotting (RDB)
save 900 1      # 15 min if 1 key changed
save 300 10     # 5 min if 10 keys changed
save 60 10000   # 1 min if 10000 keys changed
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
dbfilename dump.rdb

# AOF Persistence
appendonly yes
appendfilename "appendonly.aof"
appendfsync everysec
no-appendfsync-on-rewrite no
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

# Memory
maxmemory 2gb
maxmemory-policy allkeys-lru
maxmemory-samples 5

# Lazy Free
lazyfree-lazy-eviction no
lazyfree-lazy-expire no
lazyfree-lazy-server-del no
replica-lazy-flush no

# Replication
replica-serve-stale-data yes
replica-read-only yes
repl-diskless-sync no
repl-diskless-sync-delay 5

# Security
requirepass ""
rename-command CONFIG "b840fc02d524045377241f1f846d7b16"
```

### TLS Configuration

```conf
tls-port 6380
tls-cert-file /path/to/redis.crt
tls-key-file /path/to/redis.key
tls-ca-cert-file /path/to/ca.crt
```

## 7.3 Common Commands

### String Commands

```bash
SET key value [EX seconds] [PX milliseconds] [NX|XX]
GET key
MGET key1 key2 key3
SETEX key seconds value
SETNX key value
INCR key
INCRBY key increment
DECRBY key decrement
APPEND key value
STRLEN key
```

### Hash Commands

```bash
HSET key field value
HGET key field
HMGET key field1 field2
HGETALL key
HINCRBY key field increment
HEXISTS key field
HDEL key field
HSCAN key cursor [MATCH pattern] [COUNT count]
```

### List Commands

```bash
LPUSH key value [value ...]
RPUSH key value [value ...]
LPOP key
RPOP key
LRANGE key start stop
LTRIM key start stop
BLPOP key [key ...] timeout
BRPOP key [key ...] timeout
```

### Set Commands

```bash
SADD key member [member ...]
SREM key member [member ...]
SMEMBERS key
SISMEMBER key member
SCARD key
SRANDMEMBER key [count]
SPOP key [count]
SINTER key1 key2
SUNION key1 key2
SDIFF key1 key2
```

### Sorted Set Commands

```bash
ZADD key [NX|XX] [GT|LT] [CH] [INCR] score member [score member ...]
ZRANGE key start stop [BYSCORE|BYLEX] [REV] [LIMIT offset count]
ZREVRANGE key start stop [WITHSCORES]
ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]
ZINCRBY key increment member
ZRANK key member
ZSCORE key member
ZREM key member
```

## 7.4 Version Compatibility

| Version | Status | Key Features |
|---------|--------|--------------|
| 7.4 | Current | Sharded pub/sub, improved memory |
| 7.2 | Current | Function ACLs, ACL categories |
| 7.0 | Current | Sharded pub/sub, client-output-buffer-limit |
| 6.2 | Maintenance | COPY, CLUSTER SHARDS, HRANDFIELD |
| 6.0 | Maintenance | TLS, ACL, RESP3 |

### Redis vs Redis Stack

| Feature | Redis | Redis Stack |
|---------|-------|-------------|
| Core data structures | Yes | Yes |
| Persistence | RDB/AOF | RDB/AOF |
| JSON | No | Yes (RedisJSON) |
| Search | No | Yes (RediSearch) |
| Time series | No | Yes |
| Graph | No | Yes (RedisGraph) |
| Probabilistic | No | Yes (Bloom, CMS) |
| Vector search | No | Yes |
