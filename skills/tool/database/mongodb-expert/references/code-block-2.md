# javascript Example

```
// Compound index (order matters!)
// Query: db.orders.find({ status: "pending" }).sort({ created_at: -1 })
// Correct: status comes first (equality), then sort field
db.orders.createIndex({ status: 1, created_at: -1 })

// Covered query index
db.users.createIndex(
  { email: 1 },
  { unique: true, projection: { email: 1, name: 1, _id: 0 } }
)

// Partial index (only index documents matching filter)
db.orders.createIndex(
  { customer_id: 1, created_at: -1 },
  { partialFilterExpression: { status: "pending" } }
)

// TTL index - auto-delete documents after expiration
db.sessions.createIndex(
  { created_at: 1 },
  { expireAfterSeconds: 86400 } // 24 hours
)

// Wildcard index - for dynamic fields
db.products.createIndex(
  { "specs.$**": 1 }
)

// Text index with weights
db.articles.createIndex(
  { title: "text", body: "text", tags: "text" },
  { weights: { title: 10, tags: 5, body: 1 } }
)
```
