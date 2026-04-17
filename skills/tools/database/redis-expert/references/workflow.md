# Standard Workflow

## 8.1 Installation & Setup

### Install Redis

```bash
# Ubuntu/Debian
sudo apt install redis-server

# macOS
brew install redis

# Start service
sudo systemctl start redis
sudo systemctl enable redis
```

### Basic Commands

```bash
# Connect
redis-cli

# Test
PING

# String operations
SET mykey "Hello"
GET mykey

# Key operations
KEYS *
DEL mykey
EXISTS mykey

# TTL operations
SET mykey "value"
EXPIRE mykey 60
TTL mykey
```

### Configuration

```bash
# Runtime config
CONFIG SET maxmemory 2gb
CONFIG SET maxmemory-policy allkeys-lru

# Persistence
CONFIG SET save "900 1 300 10 60 10000"
CONFIG SET appendonly yes
CONFIG SET appendfsync everysec
```

## 8.2 Data Operations

### Strings

```bash
SET key value
GET key
INCR counter
INCRBY counter 10
APPEND key "suffix"
STRLEN key
```

### Hashes

```bash
HSET user:1 name "John"
HGET user:1 name
HGETALL user:1
HINCRBY user:1 age 1
HDEL user:1 field
```

### Lists

```bash
LPUSH mylist "first"
RPUSH mylist "last"
LPOP mylist
RPOP mylist
LRANGE mylist 0 -1
```

### Sets

```bash
SADD myset "member1"
SMEMBERS myset
SISMEMBER myset "member1"
SCARD myset
SINTER set1 set2
```

### Sorted Sets

```bash
ZADD leaderboard 100 "player1"
ZADD leaderboard 200 "player2"
ZRANGE leaderboard 0 -1 WITHSCORES
ZREVRANGE leaderboard 0 9 WITHSCORES
ZRANK leaderboard "player1"
```

## 8.3 Pipeline & Transactions

### Pipeline

```bash
# Send multiple commands at once
redis-cli PIPELINE
SET key1 value1
GET key1
SET key2 value2
GET key2
EOF
```

### Transactions

```bash
MULTI
SET key1 value1
GET key1
SET key2 value2
GET key2
EXEC
```

### Lua Scripts

```bash
EVAL "return redis.call('GET', KEYS[1])" 1 mykey
EVALSHA "sha1_hash" 1 mykey
```

## 8.4 Pub/Sub

### Subscribe

```bash
SUBSCRIBE mychannel
PSUBSCRIBE pattern*
UNSUBSCRIBE mychannel
```

### Publish

```bash
PUBLISH mychannel "message"
```

## 8.5 Server Management

### Monitoring

```bash
# Monitor live commands
MONITOR

# Slow log
SLOWLOG GET 10

# Info
INFO
INFO memory
INFO replication
```

### Maintenance

```bash
# Background save
BGSAVE

# Rewrite AOF
BGREWRITEAOF

# Shutdown
SHUTDOWN
SHUTDOWN SAVE
SHUTDOWN NOSAVE
```
