# Scenario Examples

## 9.1 Basic Usage

**User:** "How do I get started with Redis?"

**Expert:**
> **Getting Started:**
>
> 1. Install Redis
> 2. Start redis-server
> 3. Connect with redis-cli
>
> ```bash
> # Install on Ubuntu
> sudo apt install redis-server
> sudo systemctl start redis
> sudo systemctl enable redis
>
> # Connect
> redis-cli
> PING
>
> # Basic operations
> SET key value
> GET key
> ```

## 9.2 Production Setup

**User:** "How do I configure Redis for production?"

**Expert:**
> **Production Checklist:**
>
> - [ ] Set maxmemory and eviction policy
> - [ ] Configure persistence (RDB + AOF)
> - [ ] Enable password authentication
> - [ ] Configure TLS/SSL
> - [ ] Set up replication
> - [ ] Configure slowlog
> - [ ] Set up monitoring
>
> **Example redis.conf:**
> ```conf
> maxmemory 2gb
> maxmemory-policy allkeys-lru
> appendonly yes
> appendfsync everysec
> requirepass your_password
> tls-port 6380
> ```

## 9.3 Caching Patterns

**User:** "How do I implement caching with Redis?"

**Expert:**
> **Cache-Aside Pattern:**
>
> ```python
> import redis
> import json
>
> r = redis.Redis(host='localhost', port=6379, decode_responses=True)
>
> def get_user(user_id):
>     # Check cache
>     cached = r.get(f"user:{user_id}")
>     if cached:
>         return json.loads(cached)
>
>     # Fetch from database
>     user = db.fetch("SELECT * FROM users WHERE id = ?", user_id)
>
>     # Store in cache with 1-hour TTL
>     r.setex(f"user:{user_id}", 3600, json.dumps(user))
>     return user
>
> def update_user(user_id, data):
>     # Update database
>     db.execute("UPDATE users SET ... WHERE id = ?", user_id)
>     # Invalidate cache
>     r.delete(f"user:{user_id}")
> ```

## 9.4 Session Store

**User:** "How do I use Redis for session storage?"

**Expert:**
> **Session Management:**
>
> ```python
> import redis
>
> r = redis.Redis(decode_responses=True)
>
> # Store session
> session_id = "session_abc123"
> session_data = {
>     'user_id': 123,
>     'email': 'user@example.com',
>     'roles': ['admin', 'user']
> }
>
> r.hset(f"session:{session_id}", mapping=session_data)
> r.expire(f"session:{session_id}", 86400)  # 24 hours
>
> # Get session
> session = r.hgetall(f"session:{session_id}")
>
> # Check if exists
> if not session:
>     return None  # Session expired
>
> # Extend session on activity
> r.expire(f"session:{session_id}", 86400)
> ```

## 9.5 Rate Limiting

**User:** "How do I implement rate limiting with Redis?"

**Expert:**
> **Rate Limiting:**
>
> ```python
> import time
>
> def is_rate_limited(r, client_id, limit=100, window=60):
>     key = f"ratelimit:{client_id}"
>
>     now = time.time()
>     window_start = now - window
>
>     pipe = r.pipeline()
>     pipe.zremrangebyscore(key, 0, window_start)
>     pipe.zcard(key)
>     pipe.zadd(key, {str(now): now})
>     pipe.expire(key, window)
>     results = pipe.execute()
>
>     return results[1] >= limit
>
> # Sliding window with fixed window
> def fixed_window_limit(r, key, limit=100, window=60):
>     current = r.get(key)
>     if current and int(current) >= limit:
>         return False
>
>     pipe = r.pipeline()
>     pipe.incr(key)
>     if not current:
>         pipe.expire(key, window)
>     pipe.execute()
>     return True
> ```

## 9.6 Distributed Lock

**User:** "How do I implement a distributed lock?"

**Expert:**
> **Redlock Pattern:**
>
> ```python
> import time
> import uuid
>
> def acquire_lock(r, lock_name, timeout=10):
>     lock_key = f"lock:{lock_name}"
>     token = str(uuid.uuid4())
>
>     if r.set(lock_key, token, nx=True, ex=timeout):
>         return token
>     return None
>
> def release_lock(r, lock_name, token):
>     lock_key = f"lock:{lock_name}"
>
>     script = """
>     if redis.call("GET", KEYS[1]) == ARGV[1] then
>         return redis.call("DEL", KEYS[1])
>     else
>         return 0
>     end
>     """
>     r.eval(script, 1, lock_key, token)
>
> def with_lock(r, lock_name, func, timeout=10):
>     token = acquire_lock(r, lock_name, timeout)
>     if not token:
>         raise Exception("Could not acquire lock")
>     try:
>         return func()
>     finally:
>         release_lock(r, lock_name, token)
> ```

## 9.7 Pub/Sub

**User:** "How do I use Redis pub/sub?"

**Expert:**
> **Pub/Sub Pattern:**
>
> ```python
> # Publisher
> def publish_event(r, channel, event_data):
>     r.publish(channel, json.dumps(event_data))
>
> # Subscriber
> def subscribe_to_channel(r, channel):
>     pubsub = r.pubsub()
>     pubsub.subscribe(channel)
>
>     for message in pubsub.listen():
>         if message['type'] == 'message':
>             data = json.loads(message['data'])
>             handle_event(data)
>
> # Pattern subscription
> pubsub = r.pubsub()
> pubsub.psubscribe('events:*', 'logs:*')
> ```

## 9.8 Redis Cluster

**User:** "How do I set up Redis Cluster?"

**Expert:**
> **Cluster Setup:**
>
> ```bash
> # Create cluster
> redis-cli --cluster create 192.168.1.1:6379 192.168.1.2:6379 192.168.1.3:6379 \
>     192.168.1.4:6379 192.168.1.5:6379 192.168.1.6:6379 \
>     --cluster-replicas 1
>
> # Check cluster status
> redis-cli -c cluster info
> redis-cli -c cluster nodes
>
> # Key distribution
> redis-cli -c cluster keyslot mykey
> ```
>
> **Client:**
> ```python
> import redis
>
> r = redis.RedisCluster(
>     host='localhost',
>     port=6379,
>     decode_responses=True
> )
>
> # Commands automatically route to correct node
> r.set('key', 'value')
> r.get('key')
> ```

## 9.9 Data Types

**User:** "Which Redis data type should I use?"

**Expert:**
> **Data Type Selection:**
>
> | Use Case | Data Type |
> |----------|-----------|
> | Simple value (JSON, text) | STRING |
> | Counter | STRING (INCR) |
> | Queue/Stack | LIST |
> | Unique items (tags) | SET |
> | Ranked list (leaderboard) | ZSET |
> | Object (user profile) | HASH |
> | Time series | TS (Redis Stack) |
> | Vector search | SEARCH (Redis Stack) |
