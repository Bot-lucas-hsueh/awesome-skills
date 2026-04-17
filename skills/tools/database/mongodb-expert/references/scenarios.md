# Scenario Examples

## 9.1 Basic Usage

**User:** "How do I get started with MongoDB?"

**Expert:**
> **Getting Started:**
>
> 1. Install MongoDB (Community Server or Atlas)
> 2. Start mongod service
> 3. Connect with mongosh
>
> ```bash
> # Install on Ubuntu
> wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | sudo apt-key add -
> echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
> sudo apt-get update
> sudo apt-get install -y mongodb-org
>
> # Start
> sudo systemctl start mongod
> sudo systemctl enable mongod
>
> # Connect
> mongosh
> ```

## 9.2 Production Setup

**User:** "How do I configure MongoDB for production?"

**Expert:**
> **Production Checklist:**
>
> - [ ] Enable authentication (SCRAM)
> - [ ] Configure WiredTiger cache (50% RAM)
> - [ ] Enable TLS/SSL
> - [ ] Set up replica set (minimum 3 nodes)
> - [ ] Configure oplog size
> - [ ] Enable journaling
> - [ ] Set up backup strategy
>
> **Example mongod.conf:**
> ```yaml
> storage:
>   dbPath: /var/lib/mongodb
>   journal:
>     enabled: true
>   engine: wiredTiger
>   wiredTiger:
>     engineConfig:
>       cacheSizeGB: 4
>       journalCompressor: snappy
>
> net:
>   port: 27017
>   bindIp: 127.0.0.1
>   tls:
>     mode: requireTLS
>     certificateKeyFile: /etc/ssl/mongodb.pem
>
> security:
>   authorization: enabled
> ```

## 9.3 Troubleshooting

**User:** "My query is slow. How do I debug?"

**Expert:**
> **Troubleshooting Steps:**
>
> 1. Enable profiling
> 2. Use explain() on queries
> 3. Check index usage
> 4. Review slow queries
>
> ```javascript
> // Enable profiler
> db.setProfilingLevel(2, { slowms: 100 });
>
> // View slow queries
> db.system.profile.find({ millis: { $gt: 100 } }).sort({ ts: -1 }).limit(10).pretty();
>
> // Explain query
> db.orders.explain('executionStats').find({ customer_id: 123 });
>
> // Check indexes
> db.orders.getIndexes();
>
> // Check collection stats
> db.orders.stats();
> ```

## 9.4 Replica Set Setup

**User:** "How do I set up MongoDB replica set?"

**Expert:**
> **Replica Set Configuration:**
>
> **Initialize:**
> ```javascript
> rs.initiate({
>   _id: "rs0",
>   members: [
>     { _id: 0, host: "mongodb1.example.com:27017", priority: 2 },
>     { _id: 1, host: "mongodb2.example.com:27017" },
>     { _id: 2, host: "mongodb3.example.com:27017", arbiterOnly: true }
>   ]
> })
> ```
>
> **Check status:**
> ```javascript
> rs.status();
> rs.isMaster();
> rs.getPrimary();
> ```
>
> **Add member:**
> ```javascript
> rs.add("mongodb4.example.com:27017");
> rs.remove("mongodb3.example.com:27017");
> ```

## 9.5 Backup and Recovery

**User:** "How do I backup and restore MongoDB?"

**Expert:**
> **Backup:**
>
> ```bash
> # Logical backup (mongodump)
> mongodump --db myapp --out /backup/
>
> # With authentication
> mongodump --db myapp --username admin --password --authenticationDatabase admin --out /backup/
>
> # Point-in-time recovery setup
> mongodump --db myapp --query '{"ts": {"$gte": Timestamp(1704067200, 0)}}'
> ```
>
> **Restore:**
> ```bash
> mongorestore /backup/
>
> # To specific database
> mongorestore --db myapp /backup/myapp/
>
> # With drop (replace existing)
> mongorestore --drop /backup/
> ```

## 9.6 Performance Optimization

**User:** "How do I optimize MongoDB performance?"

**Expert:**
> **Optimization Techniques:**
>
> 1. **Create Strategic Indexes:**
> ```javascript
> // Compound index for query pattern
> db.orders.createIndex({ status: 1, createdAt: -1 });
>
> // Partial index
> db.orders.createIndex(
>   { customer_id: 1 },
>   { partialFilterExpression: { status: "pending" } }
> );
> ```
>
> 2. **Use Projections:**
> ```javascript
> // Only return needed fields
> db.orders.find({ customer_id: 123 }, { order_id: 1, total: 1, status: 1 });
> ```
>
> 3. **Aggregation Pipeline Optimization:**
> ```javascript
> // Put $match early
> db.orders.aggregate([
>   { $match: { status: "completed" } },  // Filter first
>   { $group: { _id: "$customer_id", total: { $sum: "$total" } } }
> ]);
> ```
>
> 4. **Use Covered Queries:**
> ```javascript
> // Index covers all fields in query
> db.users.createIndex({ email: 1, name: 1, createdAt: 1 });
> db.users.find({ email: "test@example.com" }, { name: 1, createdAt: 1 });
> ```

## 9.7 Security Hardening

**User:** "How do I secure MongoDB?"

**Expert:**
> **Security Checklist:**
>
> 1. **Enable Authentication:**
> ```javascript
> // Create user
> db.createUser({
>   user: "admin",
>   pwd: "strong_password",
>   roles: [
>     { role: "userAdminAnyDatabase", db: "admin" },
>     { role: "readWriteAnyDatabase", db: "admin" }
>   ]
> });
> ```
>
> 2. **Enable TLS:**
> ```yaml
> # mongod.conf
> net:
>   tls:
>     mode: requireTLS
>     certificateKeyFile: /etc/ssl/mongodb.pem
>     CAFile: /etc/ssl/ca.pem
> ```
>
> 3. **Role-Based Access:**
> ```javascript
> // Create app user with minimal privileges
> db.createUser({
>   user: "myapp",
>   pwd: "app_password",
>   roles: [
>     { role: "readWrite", db: "myapp" }
>   ]
> });
> ```

## 9.8 Sharding Setup

**User:** "When should I use sharding?"

**Expert:**
> **Sharding Use Cases:**
>
> - Dataset exceeds RAM
> - Write throughput exceeds single node capacity
> - Need to distribute data geographically
>
> **Setup:**
>
> ```javascript
> // Enable sharding on database
> sh.enableSharding("myapp");
>
> // Shard collection
> sh.shardCollection("myapp.orders", { customer_id: 1 });
>
> // Check status
> sh.status();
> ```
>
> **Choose shard key carefully:**
> - High cardinality
> - Even distribution
> - Common query pattern support
