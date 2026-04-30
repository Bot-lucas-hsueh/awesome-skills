# Standard Workflow

## 8.1 Installation & Setup

### Install MongoDB

```bash
# Ubuntu (Community Server)
wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org

# Start service
sudo systemctl start mongod
sudo systemctl enable mongod
```

### Connect

```bash
# Using mongosh
mongosh

# With authentication
mongosh -u username -p --authenticationDatabase admin
```

### Basic Operations

```javascript
// Switch database
use myapp

// Show databases
show dbs

// Show collections
show collections

// Create collection
db.createCollection("users")

// Insert document
db.users.insertOne({ name: "John", email: "john@example.com" })

// Find documents
db.users.find({ name: "John" })

// Update
db.users.updateOne({ name: "John" }, { $set: { email: "new@example.com" } })

// Delete
db.users.deleteOne({ name: "John" })
```

## 8.2 Data Operations

### CRUD Operations

```javascript
// Insert
db.collection.insertOne({ field: "value" })
db.collection.insertMany([{ a: 1 }, { a: 2 }])

// Query
db.collection.find({ field: "value" })
db.collection.findOne({ _id: ObjectId("...") })
db.collection.find({ status: "active" }).limit(10)

// Update
db.collection.updateOne({ _id: 1 }, { $set: { status: "completed" } })
db.collection.updateMany({}, { $inc: { count: 1 } })

// Delete
db.collection.deleteOne({ _id: 1 })
db.collection.deleteMany({ status: "inactive" })
```

### Aggregation Pipeline

```javascript
// Basic aggregation
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { _id: "$customer_id", total: { $sum: "$total" } } },
  { $sort: { total: -1 } }
])

// Complex pipeline
db.sales.aggregate([
  { $match: { date: { $gte: ISODate("2024-01-01") } } },
  { $group: { _id: { month: { $month: "$date" } }, revenue: { $sum: "$amount" } } },
  { $sort: { _id: 1 } },
  { $limit: 10 }
])
```

## 8.3 Indexing

### Create Indexes

```javascript
// Single field
db.users.createIndex({ email: 1 })

// Compound index
db.orders.createIndex({ status: 1, createdAt: -1 })

// Unique index
db.users.createIndex({ email: 1 }, { unique: true })

// TTL index
db.sessions.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 })

// Partial index
db.orders.createIndex(
  { customer_id: 1 },
  { partialFilterExpression: { status: "pending" } }
)

// Text index
db.articles.createIndex({ title: "text", content: "text" })
```

### Manage Indexes

```javascript
// List indexes
db.collection.getIndexes()

// Drop index
db.collection.dropIndex("email_1")

// Drop all indexes
db.collection.dropIndexes()
```

## 8.4 Replication

### Replica Set Operations

```javascript
// Initialize replica set
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongodb1:27017", priority: 2 },
    { _id: 1, host: "mongodb2:27017" },
    { _id: 2, host: "mongodb3:27017", arbiterOnly: true }
  ]
})

// Check status
rs.status()
rs.isMaster()
rs.getPrimary()

// Add/remove member
rs.add("mongodb4:27017")
rs.remove("mongodb3:27017")
```

## 8.5 Sharding

### Enable Sharding

```javascript
// Enable sharding on database
sh.enableSharding("myapp")

// Shard collection
sh.shardCollection("myapp.orders", { customer_id: 1 })

// Check shard status
sh.status()
sh.getBalancerState()
```
