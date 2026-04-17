# Glossary

## Core Concepts

**Document** — Basic unit of data, stored as BSON (Binary JSON).

**Collection** — Group of documents (like a table in SQL).

**Database** — Container for collections.

**BSON** — Binary-encoded JSON, supports additional data types.

## Schema Design

**Embedding** — Storing related data in a single document.

**Referencing** — Storing relationships via ObjectId references.

**Denormalization** — Duplicating data for read performance.

**Normalization** — Eliminating redundancy via references.

## Index Types

**Single Field Index** — Index on one field.

**Compound Index** — Index on multiple fields, supports prefix matching.

**Multikey Index** — Index on array fields.

**Text Index** — Full-text search on string content.

**2dsphere Index** — Geospatial queries on a sphere.

**TTL Index** — Auto-delete documents after expiration.

**Partial Index** — Index only matching documents.

## Aggregation Stages

**$match** — Filter documents (use early to reduce pipeline).

**$group** — Group documents and aggregate.

**$project** — Reshape documents, add computed fields.

**$sort** — Sort documents in pipeline.

**$limit/$skip** — Pagination.

**$lookup** — Left outer join with another collection.

**$unwind** — Deconstruct array field.

**$facet** — Multiple pipelines in single stage.

## Replication

**Primary** — Handles all writes, single in replica set.

**Secondary** — Replicates primary's oplog, serves reads.

**Arbiter** — No data, only participates in elections.

**Oplog** — Operations log for replication.

**Read Preference** — Where reads go: primary, secondary, nearest.

## Sharding

**Shard Key** — Field that determines data distribution.

**Chunk** — Contiguous range of shard key values.

**Balancer** — Background process distributing chunks.

**Zone** — Tag shards for data locality.

## Query Operators

**Comparison** — `$eq`, `$gt`, `$gte`, `$lt`, `$lte`, `$ne`, `$in`, `$nin`

**Logical** — `$and`, `$or`, `$not`, `$nor`

**Element** — `$exists`, `$type`

**Array** — `$all`, `$elemMatch`, `$size`

**Evaluation** — `$expr`, `$regex`, `$text`, `$where`

**Array Operators** — `$push`, `$addToSet`, `$pop`, `$pull`, `$filter`

## Aggregation Operators

**Accumulator** — `$sum`, `$avg`, `$min`, `$max`, `$stdDevPop`

**Array Operators** — `$arrayElemAt`, `$concatArrays`, `$map`, `$filter`

**String Operators** — `$concat`, `$substr`, `$toLower`, `$trim`

**Date Operators** — `$year`, `$month`, `$dayOfWeek`, `$dateDiff`

**Conditional** — `$cond`, `$ifNull`, `$switch`

## Transaction Terms

**Read Concern** — Isolation level for reads: local, available, majority, linearizable, snapshot.

**Write Concern** — Acknowledgment level for writes: w: 0/1/majority.

**Read Preference** — Target for reads: primary, primaryPreferred, secondary, secondaryPreferred, nearest.
