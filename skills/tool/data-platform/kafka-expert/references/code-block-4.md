# Kafka Streams for Real-time Aggregation

Java Kafka Streams application for real-time order counting.

```java
import org.apache.kafka.streams.*;
import org.apache.kafka.streams.kstream.*;
import org.apache.kafka.streams.state.StoreBuilder;
import org.apache.kafka.streams.state.Stores;

import java.time.Duration;
import java.util.Properties;

public class OrderCountStreams {
    public static void main(String[] args) {
        Properties config = new Properties();
        config.put(StreamsConfig.APPLICATION_ID_CONFIG, "order-count-app");
        config.put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "kafka:9092");
        config.put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        config.put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().getClass());
        
        StreamsBuilder builder = new StreamsBuilder();
        
        // Count orders per minute using tumbling windows
        KStream<String, String> orders = builder.stream("ecommerce.orders.created");
        
        orders
            .groupByKey()
            .windowedBy(TimeWindows.ofSizeWithNoGrace(Duration.ofMinutes(1)))
            .count(Materialized.as("order-count-per-minute"))
            .toStream()
            .foreach((key, count) -> {
                System.out.printf(
                    "Window %s-%s: %d orders%n",
                    key.window().startTime(),
                    key.window().endTime(),
                    count
                );
                // Publish to dashboard topic or expose via REST
            });

        KafkaStreams streams = new KafkaStreams(builder.build(), config);
        streams.start();
        
        // Graceful shutdown
        Runtime.getRuntime().addShutdownHook(new Thread(streams::close));
    }
}

# Maven dependencies:
# - kafka-streams
# - serde-api
# - json-simple (for JSON parsing)

# Key points:
# - Kafka Streams is stateful stream processing
# - Windows aggregate events within time boundaries
# - State stores maintain intermediate results
# - Exactly-once semantics by default
```
