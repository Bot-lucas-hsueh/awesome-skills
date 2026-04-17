# Glossary

## Core Concepts

**Cluster** — A collection of one or more nodes that share data and load.

**Node** — A single Elasticsearch process running within a cluster.

**Index** — A collection of documents with similar characteristics (like a database table).

**Shard** — A subset of an index, can be primary or replica.

**Document** — The basic unit of information, stored as JSON.

**Mapping** — Schema definition defining fields and their data types.

## Index Types

**Primary Shard** — The main shard where documents are stored.

**Replica Shard** — Copy of a primary shard for redundancy and read scaling.

**Searchable Snapshot** — Read-only snapshot mounted for search (frozen tier).

**ILM (Index Lifecycle Management)** — Automated index rotation and deletion.

## Query Types

**Query Context** — "How well does this document match?" (relevance scoring).

**Filter Context** — "Does this document match?" (yes/no, cached).

**Full-Text Query** — `match`, `multi_match`, `query_string` for text search.

**Term Query** — `term`, `terms`, `range` for exact matching.

**Compound Query** — `bool` combining multiple queries with `must`, `should`, `must_not`, `filter`.

## Aggregation Types

**Metric Aggregation** — `sum`, `avg`, `min`, `max`, `stats` computing values.

**Bucket Aggregation** — `terms`, `histogram`, `date_histogram` grouping documents.

**Pipeline Aggregation** — `avg_bucket`, `cumulative_sum` operating on aggregation output.

**Cardinality** — Approximate distinct count using HyperLogLog.

## Cluster States

**Green** — All primary and replica shards allocated.

**Yellow** — All primary shards allocated, some replicas not.

**Red** — Some primary shards unallocated.

## Data Types

**text** — Analyzed full-text field.

**keyword** — Not analyzed, exact match, good for sorting/filtering.

**date** — Date/time field with format support.

**numeric** — `long`, `integer`, `short`, `byte`, `double`, `float`.

**nested** — Array of objects with independent queries.

**join** — Parent-child relationships within same index.

## Analysis

**Analyzer** — Tokenizer + filters for text processing.

**Tokenizer** — Splits text into terms (e.g., `standard`, `whitespace`).

**Token Filter** — Modifies tokens (e.g., `lowercase`, `stemmer`, `synonym`).

**Normalizer** — Like analyzer but for keyword fields.

## Performance Terms

**Segment** — Immutable Lucene index file.

**Refresh** — Make recent changes searchable (default 1s).

**Flush** — Persist translog to disk.

**Merge** — Combine small segments into larger ones.

**Circuit Breaker** — Prevents OOM from aggregation results.
