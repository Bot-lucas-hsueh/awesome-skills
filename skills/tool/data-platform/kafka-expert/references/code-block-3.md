# Schema Registry (Avro)

Schema-aware producer with Avro serialization and Schema Registry.

```python
from confluent.kafka import Producer
from confluent.kafka.schema_registry import SchemaRegistryClient
from confluent.kafka.schema_registry.avro import AvroSerializer
import json

# Order schema (Avro format)
order_schema = """
{
  "type": "record",
  "name": "Order",
  "namespace": "com.example",
  "fields": [
    {"name": "order_id", "type": "long"},
    {"name": "customer_id", "type": "long"},
    {"name": "total", "type": "double"},
    {"name": "items", "type": {"type": "array", "items": {
      "type": "record",
      "name": "Item",
      "fields": [
        {"name": "sku", "type": "string"},
        {"name": "qty", "type": "int"},
        {"name": "price", "type": "double"}
      ]
    }}},
    {"name": "created_at", "type": {"type": "long", "logicalType": "timestamp-millis"}}
  ]
}
"""

# Setup Schema Registry client
schema_registry_client = SchemaRegistryClient({'url': 'http://schema-registry:8081'})
avro_serializer = AvroSerializer(
    schema_str=order_schema, 
    schema_registry_client=schema_registry_client
)

# Create producer with Avro serializer
producer = Producer({
    'bootstrap.servers': 'kafka:9092',
    'value.serializer': avro_serializer,
    'key.serializer': 'org.apache.kafka.common.serialization.StringSerializer',
})

# Produce Avro message
producer.produce(
    topic='orders.avro',
    key='user-123',
    value={
        'order_id': 1, 
        'customer_id': 456,
        'total': 99.99, 
        'items': [{'sku': 'A1', 'qty': 2, 'price': 49.99}],
        'created_at': 1700000000000
    },
)

producer.flush()

# Key points:
# - Schema Registry manages schema evolution
# - Avro provides compact binary format
# - Schema compatibility: BACKWARD, FORWARD, FULL
# - Register schemas before producing
```
