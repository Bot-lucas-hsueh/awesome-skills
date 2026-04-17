# Troubleshooting Guide

## 8.1 Connection Issues

### Connection Timeout

```javascript
// Connection string with timeout options
// mongodb://host:27017/db?connectTimeoutMS=10000&socketTimeoutMS=45000

// Driver options
const client = new MongoClient(uri, {
  connectTimeoutMS: 10000,
  socketTimeoutMS: 45000,
  serverSelectionTimeoutMS: 30000,
  maxPoolSize: 100
})
```

**Common causes:**
- Firewall blocking port 27017
- MongoDB not running (`systemctl status mongod`)
- Wrong bind IP in configuration
- DNS resolution issues

### Authentication Failures

```javascript
// Verify user exists
db.getSiblingDB('admin').getUsers()

// Check auth mechanism
db.adminCommand({ getParameter: 1, authenticationMechanisms: 1 })
```

## 8.2 Performance Issues

### Slow Queries

```javascript
// Enable profiler
db.setProfilingLevel(2, { slowms: 100 })

// Query profiler results
db.system.profile.find({ millis: { $gt: 100 } }).sort({ ts: -1 }).limit(10)

// Explain query
db.orders.explain('executionStats').find({ customerId: '123' })
```

**Common causes:**
- Missing indexes on filter/sort fields
- Collection scans instead of index use
- Unbounded result sets

### Index Not Used

```javascript
// Check index existence
db.mycollection.getIndexes()

// Force index hint
db.mycollection.find({ field: value }).hint({ field: 1 })

// Explain all plans
db.mycollection.explain('allPlansExecution').find({ field: value })
```

## 8.3 Replication Issues

### Replica Set Unreachable

```javascript
// Check replica set status
rs.status()

// Check primary
rs.isMaster()

// Reconfigure if member down
rs.reconfig({
  _id: "rs0",
  members: [
    { _id: 0, host: "host1:27017" },
    { _id: 1, host: "host2:27017" },
    { _id: 2, host: "host3:27017", arbiterOnly: true }
  ]
})
```

### Oplog Issues

```javascript
// Check oplog size
db.getSiblingDB('local').oplog.rs.stats()

// Calculate oplog window
db.getSiblingDB('local').oplog.rs.aggregate([
  { $collStats: { oplog: { size: true } } },
  { $project: { totalSize: 1 } }
])
```

## 8.4 Sharding Issues

### Chunk Migration Stuck

```javascript
// Check balancer status
sh.isBalancerRunning()
sh.getBalancerState()

// Check split points
db.getSiblingDB('config').chunks.find({ ns: 'mydb.collection' }).count()

// Manually move chunk
sh.moveChunk("mydb.collection", { _id: 5000 }, "shard0002")
```

### Shard Key Issues

```javascript
// Check shard key distribution
db.getSiblingDB('admin').runCommand({ distinct: "mydb.collection", key: "_id" })

// Refine shard key (cannot change base key)
db.adminCommand({ refineCollectionShardKey: "mydb.collection", key: { newField: 1 } })
```

## 8.5 Storage/Disk Issues

### Disk Space

```javascript
// Check disk usage
db.stats()

// Compact collection (reclaim space)
db.mycollection.compact()

// Repair database
db.repairDatabase()

// TTL index for auto-cleanup
db.logs.createIndex({ createdAt: 1 }, { expireAfterSeconds: 604800 })
```

## 8.6 Common Errors

### Write Concern Errors

```javascript
// W1 acknowledges write to primary
db.collection.insertOne({ doc: true }, { writeConcern: { w: 1 } })

// Majority acknowledges replica majority
db.collection.insertOne({ doc: true }, { writeConcern: { w: "majority", wtimeout: 5000 } })

// All nodes
db.collection.insertOne({ doc: true }, { writeConcern: { w: "all" } })
```

### Transaction Errors

```javascript
// Max transaction timeout is 5 minutes by default
const session = client.startSession()
session.startTransaction({ readConcern: { level: "snapshot" }, writeConcern: { w: "majority" } })

try {
  // operations
  await session.commitTransaction()
} catch (e) {
  await session.abortTransaction()
}
```
