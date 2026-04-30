# Glossary

## Core Data Types

**STRING** — Simple string, number, or JSON (up to 512MB).

**LIST** — Ordered list, LPUSH/RPOP = queue, LPUSH/LPOP = stack.

**SET** — Unordered collection of unique strings.

**HASH** — Field-value pairs, like a hash table or document.

**ZSET (Sorted Set)** — Set with scores, ordered by score.

**STREAM** — Append-only log, consumer groups (event sourcing).

**BITMAP** — String with bit operations (users online, attendance).

**BITFIELD** — Arbitrary bit field operations.

**HYPERLOGLOG** — Probabilistic cardinality estimation.

**GEOSPATIAL** — GEOADD/GEODIST for lat/lng (based on sorted set).

## Keyspace

**Key** — Unique identifier, max 512MB, binary safe.

**TTL** — Time to live, key auto-deleted after expiration.

**Keyspace Notifications** — Pub/sub for key events.

## Persistence

**RDB** — Point-in-time snapshot, binary file.

**AOF** — Append-only file, logs all commands.

**Fork** — Background save uses copy-on-write.

**BGREWRITEAOF** — Compact AOF file.

## Replication

**Primary (Master)** — Read/write, receives writes.

**Replica (Slave)** — Copies primary, read-only by default.

**SYNC** — Full sync from primary.

**PSYNC** — Partial sync, continues from offset.

**Replication ID** — Unique identifier for replica's history.

**Replication Backlog** — Buffer for partial sync.

## Clustering

**Cluster** — Multiple Redis nodes, data sharded across.

**Slot** — 16384 slots, data distributed by key hash.

**MIGRATE** — Move keys between nodes.

**ASK/REDIRECT** — Client routing in cluster.

**MOVED** — Slot permanently moved.

**ASK** — Slot temporarily moved.

## Pub/Sub

**Channel** — Named message channel.

**Pattern** — Wildcard subscription (*, []).

**PSUBSCRIBE** — Pattern-based subscription.

**PUBLISH** — Send to channel.

**Sharded Pub/Sub** — Redis 7+ cluster-aware pub/sub.

## Streams

**Entry ID** — Timestamp + sequence (e.g., 1234-0).

**Consumer Group** — Multiple consumers processing messages.

**PEL** — Pending entries list.

**ACK** — Acknowledge message processed.

**XREADGROUP** — Read new messages for consumer.

**XCLAIM** — Claim pending messages from dead consumer.

## Lua Scripts

**EVAL** — Execute Lua script.

**EVALSHA** — Execute cached script by SHA.

**MULTI/EXEC** — Transaction (no rollback).

**WATCH** — Optimistic locking for transactions.

## Memory

**maxmemory** — Max memory for dataset.

**Eviction Policy** — What to remove when full.

**LRU** — Least Recently Used.

**LFU** — Least Frequently Used.

**Memory Fragmentation** — Ratio > 1.5 needs defrag.

**Lazy Free** — Free objects asynchronously.

## Sentinel

**Sentinel** — Redis HA with automatic failover.

**Monitor** — Watch master/replica.

**Quorum** — Number of sentinels for failover.

**SDOWN** — Subjectively down (local view).

**ODOWN** — Objectively down (quorum agreement).

## Blocking Operations

**BLPOP** — Blocking pop from list.

**BRPOPLPUSH** — Blocking move between lists.

**SUBSCRIBE** — Blocking channel subscription.

## Commands by Time Complexity

**O(1)** — GET, SET, INCR, SADD, HSET

**O(log N)** — ZADD, ZRANK

**O(N)** — LRANGE, SMEMBERS, KEYS

**O(N+M)** — HGETALL, SMEMBERS with count

**O(N log N)** — SORT, ZRANGEBYSCORE

## Protocol

**RESP2** — Redis Serialization Protocol, v2.

**RESP3** — Redis Serialization Protocol, v3 (Redis 6+).

**PIPELINE** — Batch multiple commands.

**TX** — Transaction with MULTI/EXEC.
