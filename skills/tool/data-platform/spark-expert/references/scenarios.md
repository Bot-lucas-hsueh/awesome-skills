# Glossary

## Core Spark Concepts

### SparkSession
The unified entry point for Spark functionality. Created once per application. Provides access to SparkContext, SQLContext, and StreamingContext functionality. All DataFrame operations go through SparkSession.

### DataFrame
A distributed collection of data organized into named columns, similar to a relational table or Pandas DataFrame. Immutable once created. Lazy — transformations build a DAG, actions trigger execution.

### RDD (Resilient Distributed Dataset)
The low-level Spark abstraction. Resilient (recomputable on failure), distributed (partitioned across nodes), dataset (collection of elements). DataFrames compile to RDDs internally.

### Dataset
A strongly-typed API on top of DataFrames. Provides compile-time type safety while maintaining Catalyst optimization. Use `Dataset[T]` for JVM languages (Scala/Java).

### Catalyst Optimizer
Spark SQL's query optimizer. Transforms SQL/DataFrame plans through multiple phases: analysis, logical optimization, physical planning, and code generation.

### Tungsten / Project Tungsten
Spark's memory management and CPU optimization project. Key features: off-heap memory management, cache-aware computation, code generation.

### Lazy Evaluation
Transformations (map, filter, select) build a DAG but don't execute. Actions (collect, count, write) trigger execution. Enables Spark to optimize the entire pipeline.

### Narrow Transformation
A transformation where each input partition contributes to only one output partition (e.g., filter, select, map). No shuffle required.

### Wide Transformation
A transformation where data from multiple partitions is combined (e.g., groupBy, join, repartition). Requires shuffle (exchange).

### Shuffle
The redistribution of data across partitions. Spark writes shuffle files to disk and transfers them across the network. The most expensive operation in Spark. Also called `Exchange` in Spark UI.

### Partition
A chunk of data processed by a single task. Controlled by `spark.sql.shuffle.partitions` (default 200) or explicit `repartition()`. Optimal size: 128-256MB.

### Task
A unit of work sent to an executor. One task per partition per stage. Number of tasks = number of partitions × number of stages.

### Stage
A set of tasks that can be executed together without a shuffle. Stages are connected by shuffle boundaries.

### Job
A complete Spark action (e.g., `collect()`, `write()`). Each job consists of one or more stages.

### DAG (Directed Acyclic Graph)
The execution plan built from transformations. The DAGScheduler splits it into stages and schedules tasks.

### Broadcast Variable
A read-only variable cached on each executor (instead of shipped with each task). Used for lookup tables and small reference data. Created via `spark.sparkContext.broadcast()`.

### Accumulator
A write-only variable that can be summed across tasks. Used for counters and sums. Spark guarantees only driver-side reads.

### DataFrame API
The declarative API for Spark SQL. Operations like `select`, `filter`, `join`, `groupBy`. Optimized by Catalyst and executed as RDD operations.

### Spark SQL
The Spark module for structured data processing. Supports SQL queries, DataFrames, Datasets, and embedded Hive metastore.

### Spark Structured Streaming
The stream processing API built on DataFrames. Treats streams as unbounded tables. Supports event-time processing, watermarks, stateful aggregations.

### Watermark
A moving boundary that defines when late data is dropped. Configured with `withWatermark()`. Used in streaming aggregations to clean up old state.

### Checkpoint (Streaming)
Saves the streaming query state to reliable storage. Enables recovery from driver failure. Two types: metadata checkpoint (recovery config) and data checkpoint (state).

### Delta Lake
An open-source storage layer that brings ACID transactions to Spark DataFrames. Supports time travel, schema enforcement, and UPSERT operations.

### Apache Iceberg
A high-performance open-table format for analytic workloads. Supports hidden partitioning, time travel, schema evolution, and partition spec evolution.

### Apache Hudi
An open-source lakehouse platform providing upsert/insert support, time travel, and incremental pull.

### Spark Connect
A client-server interface (Spark 3.4+) that separates the Spark client from the driver. Enables connecting to Spark from remote applications via DataFrame API.

### AQE (Adaptive Query Execution)
A feature (Spark 3.2+) that re-optimizes query plans at runtime based on shuffle statistics. Adapts partition counts, join strategies, and handles skew.

### Spark on Kubernetes
Native Kubernetes support for Spark. Executors run as pods. Spark manages resource negotiation via the Kubernetes scheduler.

### Spark History Server
A UI for viewing completed Spark applications. Reads event logs from `spark.eventLog.dir`.

### Spark UI
The web UI for monitoring Spark applications. Shows jobs, stages, tasks, storage, environment, and SQL execution.

### Kryo Serialization
The default serialization for shuffling data between Spark nodes (faster than Java serialization). Register classes for best performance.

## CLI Reference

| Command | Purpose |
|---------|---------|
| `spark-submit` | Submit a Spark application |
| `pyspark` | Launch PySpark shell |
| `spark-shell` | Launch Scala Spark shell |
| `spark-sql` | Launch Spark SQL CLI |
| `spark-class` | Run Spark class main method |
| `start-history-server.sh` | Start Spark History Server |
| `stop-history-server.sh` | Stop History Server |
| `find-spark-home` | Find Spark installation directory |

## Key Configuration

| Config | Default | Purpose |
|--------|---------|---------|
| `spark.sql.shuffle.partitions` | 200 | Default shuffle partition count |
| `spark.executor.instances` | 1 | Number of executors |
| `spark.executor.cores` | 1 | Cores per executor |
| `spark.executor.memory` | 1g | Memory per executor |
| `spark.executor.memoryOverhead` | executorMemory × 0.1 | Off-heap memory |
| `spark.sql.adaptive.enabled` | true | Enable AQE |
| `spark.sql.autoBroadcastJoinThreshold` | 10MB | Max size for broadcast join |
| `spark.sql.files.maxPartitionBytes` | 128MB | Max bytes per partition |
| `spark.serializer` | JavaSerializer | Shuffle serialization |
