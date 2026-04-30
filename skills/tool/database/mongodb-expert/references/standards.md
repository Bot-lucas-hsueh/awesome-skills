# Standards & Reference

## 7.1 Official Documentation

- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [MongoDB CRUD Operations](https://www.mongodb.com/docs/manual/crud/)
- [Aggregation Pipeline](https://www.mongodb.com/docs/manual/reference/operator/aggregation-pipeline/)
- [Indexes](https://www.mongodb.com/docs/manual/indexes/)
- [Data Models](https://www.mongodb.com/docs/manual/data-modeling/)
- [Replication](https://www.mongodb.com/docs/manual/replication/)
- [Sharding](https://www.mongodb.com/docs/manual/sharding/)
- [MongoDB Atlas](https://www.mongodb.com/atlas)
- [MongoDB Driver Docs](https://www.mongodb.com/docs/drivers/)

## 7.2 Configuration Reference

### mongod.conf

```yaml
storage:
  dbPath: /var/lib/mongodb
  journal:
    enabled: true
  engine: wiredTiger
  wiredTiger:
    engineConfig:
      cacheSizeGB: 4
      journalCompressor: snappy
    collectionConfig:
      blockCompressor: snappy
    indexConfig:
      prefixCompression: true

systemLog:
  destination: file
  path: /var/log/mongodb/mongod.log
  logAppend: true

net:
  port: 27017
  bindIp: 127.0.0.1
  maxIncomingConnections: 65536

replication:
  replSetName: "rs0"

sharding:
  clusterRole: shardsvr
```

### Replica Set Configuration

```javascript
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongodb1.example.com:27017", priority: 2 },
    { _id: 1, host: "mongodb2.example.com:27017" },
    { _id: 2, host: "mongodb3.example.com:27017", arbiterOnly: true }
  ]
})

rs.add("mongodb4.example.com:27017")
rs.remove("mongodb3.example.com:27017")
```

## 7.3 Common Commands

### Shell Commands

```javascript
// Database operations
use mydb
db.getSiblingDB('admin')
db.getMongo().getDBNames()

// Collection operations
db.createCollection("mycollection")
db.mycollection.drop()
db.getCollectionNames()

// User management
db.createUser({
  user: "appuser",
  pwd: "password",
  roles: [
    { role: "readWrite", db: "mydb" },
    { role: "dbAdmin", db: "mydb" }
  ]
})
```

### Index Creation

```javascript
// Single field
db.mycollection.createIndex({ email: 1 })

// Compound index
db.mycollection.createIndex({ status: 1, createdAt: -1 })

// Unique index
db.mycollection.createIndex({ userId: 1 }, { unique: true })

// TTL index (auto-delete after 30 days)
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 2592000 })

// Partial index
db.orders.createIndex(
  { customerId: 1 },
  { partialFilterExpression: { status: "pending" } }
)

// Text index
db.articles.createIndex({ title: "text", content: "text" })
```

## 7.4 Version Compatibility

| Version | Status | Key Features |
|---------|--------|--------------|
| 7.0 | Current | $count, $density, improved aggregation |
| 6.0 | Current | Flattening transformations, improvements |
| 5.0 | Maintenance | Time-series collections, live resharding |
| 4.4 | Security fixes only | Change Streams GA |
| 4.2 | EOL | Multi-document ACID transactions |

### MongoDB Server Versions

```javascript
db.version()           // Server version
db.adminCommand('buildInfo').versionArray  // Detailed version
```
