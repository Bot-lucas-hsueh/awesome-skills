# Glossary

## Core Concepts

**InnoDB** — Default storage engine, ACID compliant, row-level locking.

**MyISAM** — Legacy storage engine, table-level locking, no transactions.

**Row Format** — How rows are stored: DYNAMIC, COMPRESSED, REDUNDANT, COMPACT.

**Tablespace** — Logical container for table data.

## Index Types

**B-Tree Index** — Default index type, optimized for range queries.

**Hash Index** — Memory tables only, fast exact lookups.

**Full-Text Index** — Text search with MATCH AGAINST.

**Spatial Index** — R-tree for GIS data (POINT, POLYGON).

**Primary Key** — Unique index, clustered by default.

**Unique Index** — Enforces uniqueness constraint.

**Composite/Compound Index** — Multiple columns, leftmost prefix rule applies.

## SQL Concepts

**ACID** — Atomicity, Consistency, Isolation, Durability.

**Transaction** — Unit of work with all-or-nothing semantics.

**Isolation Level** — READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE.

**Lock Granularity** — Table-level vs row-level locks.

**Deadlock** — Two transactions waiting for each other's locks.

## Replication

**Binlog** — Binary log of all changes.

**GTID** — Global Transaction Identifier for automatic positioning.

**Source/Master** — Primary server sending changes.

**Replica/Slave** — Secondary receiving changes.

**Relay Log** — Replica's local copy of binlog events.

**IO Thread** — Fetches binlog events from source.

**SQL Thread** — Executes binlog events on replica.

## Query Optimization

**EXPLAIN** — Shows query execution plan.

**Handler** — Low-level storage engine interface.

**Optimizer Hints** — Direct query execution approach.

**Index Condition Pushdown** — Filter using indexes.

**MRR** — Multi-Range Read optimization.

**Batched Key Access** — Join optimization using index.

## Data Types

**VARCHAR** — Variable-length, 1-65535 bytes.

**CHAR** — Fixed-length, padded.

**TEXT** — Non-binary large text (4GB max).

**BLOB** — Binary large object.

**ENUM** — Single value from list.

**SET** — Multiple values from list.

**JSON** — Native JSON storage (MySQL 5.7+).

**GEOMETRY** — Spatial data types.

## InnoDB Concepts

**Buffer Pool** — Memory cache for table data/indexes.

**Change Buffer** — Buffered secondary index updates.

**Log Buffer** — In-memory buffer for redo log.

**Doublewrite Buffer** — Safety net for page writes.

**Adaptive Hash Index** — In-memory hash optimization.

**Page** — InnoDB unit of I/O (16KB default).

**Row Lock** — Lock at row level.

**Gap Lock** — Lock on gap between records.

## Performance Terms

**Query Cache** — (Removed in 8.0) Cached query results.

**Prepared Statements** — Pre-compiled SQL.

**Connection Pool** — Reuse of connections.

**Slow Query Log** — Queries exceeding long_query_time.

**Performance Schema** — Monitoring infrastructure.
