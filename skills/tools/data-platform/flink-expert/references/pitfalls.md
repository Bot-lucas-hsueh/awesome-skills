# Examples

## 10.1 DataStream API Examples

### Event-Time Windowed Aggregation

```java
import org.apache.flink.api.common.eventtime.*;
import org.apache.flink.streaming.api.functions.windowing.*;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.apache.flink.streaming.api.windowing.windows.TimeWindow;

public class RevenueAggregation {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        env.setStateBackend(new EmbeddedRocksDBStateBackend());
        env.enableCheckpointing(60000L);
        env.getCheckpointConfig().setCheckpointStorage("s3://flink-checkpoints/");

        DataStream<Order> orders = env
            .addSource(new KafkaSource<Order>("orders", properties))
            .assignTimestampsAndWatermarks(
                WatermarkStrategy
                    .<Order>forBoundedOutOfOrderness(Duration.ofSeconds(30))
                    .withTimestampAssigner((order, ts) -> order.getTimestamp())
                    .withIdleness(Duration.ofMinutes(1))
            )
            .keyBy(Order::getCustomerId)
            .window(SlidingEventTimeWindows.of(Time.minutes(10), Time.minutes(1)))
            .allowedLateness(Time.minutes(2))
            .sideOutputLateData(lateOutputTag)
            .aggregate(new RevenueAggregator(), new RevenueWindowFunction());

        lateOutputTag = OutputTag<Order>("late-orders");
    }
}

public class RevenueAggregator implements AggregateFunction<Order, RevenueAccumulator, Double> {
    @Override
    public RevenueAccumulator createAccumulator() {
        return new RevenueAccumulator(0.0, 0, 0L);
    }

    @Override
    public RevenueAccumulator add(Order value, RevenueAccumulator acc) {
        return new RevenueAccumulator(
            acc.totalRevenue + value.getAmount(),
            acc.orderCount + 1,
            Math.max(acc.lastTimestamp, value.getTimestamp())
        );
    }

    @Override
    public Double getResult(RevenueAccumulator acc) {
        return acc.totalRevenue;
    }

    @Override
    public RevenueAccumulator merge(RevenueAccumulator a, RevenueAccumulator b) {
        return new RevenueAccumulator(
            a.totalRevenue + b.totalRevenue,
            a.orderCount + b.orderCount,
            Math.max(a.lastTimestamp, b.lastTimestamp)
        );
    }
}
```

### Async I/O with Enrichment

```java
import org.apache.flink.connector.async.base.*;

DataStream<UserEvent> enriched = AsyncDataStream
    .unorderedWait(
        env,
        new AsyncDatabaseEnricher(),
        3000, TimeUnit.MILLISECONDS,
        100  // capacity
    )
    .setTimeout(60000, TimeUnit.MILLISECONDS)
    .setOutputMode(AsyncOutputMode.UNORDERED);

public class AsyncDatabaseEnricher 
    extends AsyncFunction<UserEvent, EnrichedEvent> {

    private transient DBConnection db;

    @Override
    public void open(Configuration parameters) {
        String url = parameters.getString("db.url");
        db = DBConnection.create(url);
    }

    @Override
    public void timeout(UserEvent input, ResultFuture<EnrichedEvent> resultFuture) {
        resultFuture.complete(Collections.singletonList(
            EnrichedEvent.from(input).markTimedOut()
        ));
    }

    @Override
    public void asyncInvoke(UserEvent input, ResultFuture<EnrichedEvent> resultFuture) {
        CompletableFuture<UserProfile> profileFuture = 
            CompletableFuture.supplyAsync(() -> db.getProfile(input.getUserId()));

        profileFuture.thenAccept(profile -> {
            if (profile != null) {
                resultFuture.complete(Collections.singletonList(
                    EnrichedEvent.from(input).withProfile(profile)
                ));
            } else {
                resultFuture.complete(Collections.singletonList(
                    EnrichedEvent.from(input).markNoProfile()
                ));
            }
        });
    }

    @Override
    public void close() {
        db.close();
    }
}
```

## 10.2 Table API / SQL Examples

### Streaming Aggregation with Tumbling Windows

```sql
-- Windowed revenue by customer
SELECT
    customer_id,
    TUMBLE_START(event_time, INTERVAL '5' MINUTE) AS window_start,
    TUMBLE_END(event_time, INTERVAL '5' MINUTE) AS window_end,
    SUM(amount) AS total_revenue,
    COUNT(*) AS order_count,
    AVG(amount) AS avg_order_value
FROM orders
WHERE currency = 'USD'
GROUP BY
    customer_id,
    TUMBLE(event_time, INTERVAL '5' MINUTE)
HAVING SUM(amount) > 100
```

### CDC → Deduplication → Upsert

```sql
-- Step 1: Define CDC source (Debezium)
CREATE TABLE cdc_orders (
    id STRING,
    order_id STRING,
    customer_id STRING,
    total_amount DECIMAL(10, 2),
    status STRING,
    updated_at TIMESTAMP(3),
    WATERMARK FOR updated_at AS updated_at - INTERVAL '10' SECOND
) WITH (
    'connector' = 'kafka',
    'topic' = 'orders_cdc',
    'properties.bootstrap.servers' = 'kafka:9092',
    'format' = 'debezium-json'
);

-- Step 2: Deduplicate by taking latest per order_id
CREATE VIEW deduped_orders AS
SELECT *
FROM (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY order_id
            ORDER BY updated_at DESC
        ) AS _rn
    FROM cdc_orders
)
WHERE _rn = 1;

-- Step 3: Upsert into dimension table
CREATE TABLE dim_orders (
    order_id STRING PRIMARY KEY NOT ENFORCED,
    customer_id STRING,
    total_amount DECIMAL(10, 2),
    status STRING,
    updated_at TIMESTAMP,
    processed_at TIMESTAMP
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:postgresql://pg:5432/warehouse',
    'table-name' = 'dim_orders',
    'username' = 'flink',
    'password' = '${env:PG_PASSWORD}'
);

INSERT INTO dim_orders
SELECT
    order_id,
    customer_id,
    total_amount,
    status,
    updated_at,
    CURRENT_TIMESTAMP
FROM deduped_orders;
```

### Pattern Matching (CEP) for Fraud Detection

```sql
-- Detect rapid consecutive high-value orders from same customer
SELECT
    customer_id,
    first_order_id,
    second_order_id,
    first_ts,
    second_ts,
    second_ts - first_ts AS gap_ms
FROM (
    SELECT
        customer_id,
        LAG(order_id, 1) OVER win AS first_order_id,
        order_id AS second_order_id,
        LAG(ts, 1) OVER win AS first_ts,
        ts AS second_ts
    FROM orders
    WINDOW win AS (
        PARTITION BY customer_id
        ORDER BY ts
        ROWS BETWEEN 1 PRECEDING AND 1 PRECEDING
    )
)
WHERE total_amount > 5000
    AND first_total_amount > 5000
    AND (second_ts - first_ts) < INTERVAL '5' MINUTE';
```

## 10.3 Production Job Configs

### flink-conf.yaml (High-Throughput Streaming)

```yaml
# flink-conf.yaml

# JobManager
jobmanager.memory.process.size: 1600m
jobmanager.memory.flink.size: 1280m

# TaskManager
taskmanager.memory.process.size: 4g
taskmanager.memory.flink.size: 3g
taskmanager.numberOfTaskSlots: 8

# State
state.backend: rocksdb
state.backend.incremental: true
state.backend.rocksdb.memory.managed: true
state.backend.rocksdb.memory.managed.fraction: 0.4
state.backend.checkpoints.dir: s3://flink-checkpoints/
state.savepoints.dir: s3://flink-savepoints/

# Checkpointing
execution.checkpointing.interval: 60s
execution.checkpointing.mode: EXACTLY_ONCE
execution.checkpointing.timeout: 10min
execution.checkpointing.min-pause: 30s
execution.checkpointing.max-concurrent-checkpoints: 1
execution.checkpointing.externalized-checkpoint-retention: RETAIN_ON_CANCELLATION

# Network
taskmanager.network.memory.fraction: 0.15
taskmanager.network.memory.min: 256mb
taskmanager.network.memory.max: 1gb

# Table/SQL
table.exec.state-backend: rocksdb
table.exec.resource.default-parallelism: 4
table.exec.async.enabled: true
table.optimizer.agg-phase-strategy: TWO_PHASE

# High Availability
high-availability: kubernetes
high-availability.storageDir: s3://flink-ha/
```

### Kubernetes Deployment (Flink Operator)

```yaml
apiVersion: flink.apache.org/v1beta1
kind: FlinkDeployment
metadata:
  name: orders-streaming
  namespace: flink
spec:
  image: flink:1.19
  flinkVersion: v1_19
  flinkConfiguration:
    state.backend: rocksdb
    state.backend.incremental: "true"
    execution.checkpointing.interval: "60s"
    state.checkpoints.dir: s3://flink-checkpoints/
    high-availability: org.apache.flink.kubernetes.highavailability
    high-availability.storageDir: s3://flink-ha/
  serviceAccount: flink-service-account
  jobManager:
    resource:
      memory: "2048m"
      cpu: 2
    replicas: 2
    podTemplate:
      spec:
        containers:
          - name: flink-main-container
            env:
              - name: AWS_DEFAULT_REGION
                value: us-east-1
            volumeMounts:
              - name: flink-secrets
                mountPath: /opt/flink/secrets
        volumes:
          - name: flink-secrets
            secret:
              secretName: flink-secrets
  taskManager:
    resource:
      memory: "4096m"
      cpu: 4
    replicas: 4
    podTemplate:
      spec:
        containers:
          - name: flink-main-container
            resources:
              requests:
                memory: "4Gi"
                cpu: "2"
              limits:
                memory: "8Gi"
                cpu: "4"
  job:
    jarURI: s3://flink-jars/orders-job.jar
    entryClass: com.example.OrdersJob
    args:
      - "--kafka.bootstrap.servers"
      - "kafka:9092"
      - "--pg.url"
      - "jdbc:postgresql://pg:5432/warehouse"
    parallelism: 16
    upgradeMode: savepoint
    state: running
```

## 10.4 Integration Examples

### Flink → Iceberg (Lakehouse)

```sql
-- Create Iceberg table
CREATE TABLE iceberg_orders (
    order_id STRING,
    customer_id STRING,
    total_amount DECIMAL(10, 2),
    status STRING,
    event_time TIMESTAMP
) PARTITIONED BY (days(event_time))
TBLPROPERTIES (
    'format-version' = '2',
    'write.distribution-mode' = 'hash',
    'write.metadata.delete-after-commit.enabled' = 'true',
    'write.metadata.previous-versions-max' = '100'
);

-- MERGE (upsert) pattern
MERGE INTO iceberg_orders AS target
USING source_stream AS source
ON target.order_id = source.order_id
WHEN MATCHED AND source.op = 'UPDATE' THEN
    UPDATE SET *
WHEN MATCHED AND source.op = 'DELETE' THEN
    DELETE
WHEN NOT MATCHED THEN
    INSERT *;
```

### Flink → Kafka with Exactly-Once

```java
KafkaSink<OutputEvent> sink = KafkaSink.<OutputEvent>builder()
    .setBootstrapServers("kafka:9092")
    .setRecordSerializer(KafkaRecordSerializationSchema.builder()
        .setTopic("output-events")
        .setValueSerializationSchema(new EventSerializer())
        .setKeySerializationSchema(new EventKeySerializer())
        .build())
    .setDeliveryGuarantee(DeliveryGuarantee.EXACTLY_ONCE)
    .setTransactionalIdPrefix("flink-orders")
    .setKafkaProducerConfig(properties)
    .setBuild()
    .build();

DataStream<OrderEvent> stream = env.fromSource(
    KafkaSource...,
    WatermarkStrategy...,
    "Kafka Source"
);

stream
    .keyBy(OrderEvent::getCustomerId)
    .process(new OrderAggregator())
    .sinkTo(sink);
```
