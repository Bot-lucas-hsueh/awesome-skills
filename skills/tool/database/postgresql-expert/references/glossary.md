# Glossary

## Core Concepts

**MVCC** — Multi-Version Concurrency Control, allows concurrent reads without locks.

**VACUUM** — Process that reclaims dead tuples and freezes transaction IDs.

**Autovacuum** — Automated vacuum daemon.

**TOAST** — The Oversized-Attribute Storage Technique for large values.

**FSM** — Free Space Map tracking available space in tables.

## Index Types

**B-Tree** — Default, handles equality and range queries.

**Hash** — Fast equality lookups, not persistent across crashes.

**GiST** — Generalized Search Tree, for geometric types, full-text search.

**SP-GiST** — Space-partitioned GiST, for quadtrees, k-d trees.

**GIN** — Generalized Inverted Index, for array values, JSONB, full-text.

**BRIN** — Block Range Index, for naturally ordered data (logs, time series).

**pgvector** — Vector embeddings for ML similarity search.

## Query Planning

**Seq Scan** — Sequential scan of entire table.

**Index Scan** — Use index to find rows, then fetch table.

**Index Only Scan** — Read only from index, no heap access.

**Bitmap Heap/Index Scan** — Build bitmap from index, then fetch rows.

**Nested Loop** — For each row of outer, scan inner.

**Hash Join** — Build hash table, probe with inner rows.

**Merge Join** — Sort both, then merge.

## Data Types

**SERIAL** — Auto-incrementing integer (creates sequence).

**BIGSERIAL** — 64-bit auto-incrementing integer.

**UUID** — Universally Unique Identifier.

**JSONB** — Binary JSON, indexed, preserves key order.

**JSON** — JSON stored as text, preserved formatting.

**ARRAY** — Variable-length arrays of any type.

**RANGE** — Range types (int4range, daterange, tsrange).

**HSTORE** — Key-value store (extension).

**VECTOR** — Dense vector for ML embeddings (pgvector extension).

## SQL Commands

**VACUUM** — Reclaim space, mark tuples as reusable.

**ANALYZE** — Update statistics for query planner.

**EXPLAIN** — Show query plan without executing.

**EXPLAIN ANALYZE** — Execute and show plan with timing.

**CLUSTER** — Reorder table by index.

**REINDEX** — Rebuild corrupted indexes.

**TRUNCATE** — Fast delete all rows.

## Replication Terms

**Physical Replication** — Binary replication via WAL.

**Logical Replication** — Row-based replication via publications.

**Streaming Replication** — Real-time WAL streaming to replicas.

**Synchronous Commit** — Wait for replica to confirm write.

**Asynchronous Commit** — Confirm immediately, replicate later.

**Slot** — Mechanism to retain WAL on primary for replicas.

**WAL** — Write-Ahead Log for durability and replication.

**pg_hba.conf** — Client authentication configuration file.

**pg_ident.conf** — User name mapping configuration.

## Configuration Parameters

**shared_buffers** — Memory for caching data pages (25% RAM).

**work_mem** — Memory per sort/hash operation.

**maintenance_work_mem** — Memory for VACUUM, CREATE INDEX.

**effective_cache_size** — Planner's assumption for available cache.

**random_page_cost** — Cost estimate for non-sequential disk reads.

**effective_io_concurrency** — Parallel disk I/O capability.

**max_connections** — Maximum client connections.

**wal_level** — WAL content (minimal, replica, logical).

## Transaction Isolation

**READ COMMITTED** — Default, sees committed rows only.

**REPEATABLE READ** — Consistent snapshot for entire transaction.

**SERIALIZABLE** — Full isolation, may cause serialization failures.

## Constraint Types

**PRIMARY KEY** — Unique, not null, creates index.

**UNIQUE** — Unique values (null allowed).

**CHECK** — Boolean expression constraint.

**NOT NULL** — Cannot be null.

**EXCLUDE** — Advanced constraint (e.g., no overlapping ranges).

**FOREIGN KEY** — Reference integrity.

## Performance Terms

**pg_stat_statements** — Query performance statistics extension.

**autovacuum** — Background vacuum processes.

**checkpoint** — Periodic flush of WAL to data files.

**FPI** — Full Page Write in WAL for crash recovery.

## Extensions

**pgvector** — Vector similarity search.

**PostGIS** — Geospatial data support.

**pg_trgm** — Trigram similarity for text search.

**uuid-ossp** — UUID generation functions.

**pgcrypto** — Cryptographic functions.

**hstore** — Key-value store data type.
