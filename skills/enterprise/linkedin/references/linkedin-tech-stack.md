## § 6 · LinkedIn Tech Stack

### 6.1 Core Technologies

| Category | Technology | Purpose |
|----------|------------|---------|
| **Streaming** | Apache Kafka | Event streaming (created at LinkedIn, 2010) |
| **Stream Processing** | Apache Samza | Real-time stream processing |
| **Analytics** | Apache Pinot | Real-time OLAP analytics |
| **Graph DB** | LinkedIn Graph (custom) | Social graph storage and queries |
| **Data Store** | Espresso | Distributed document store |
| **KV Store** | Voldemort | Distributed key-value storage |
| **Search** | Galene | LinkedIn's search engine |
| **ML Platform** | TensorFlow, PyTorch | Model training and serving |
| **Cloud** | Azure (Microsoft) | Primary cloud infrastructure |

### 6.2 Open Source Contributions

| Project | Origin | Impact |
|---------|--------|--------|
| **Apache Kafka** | Created at LinkedIn (2010) | Industry standard for event streaming |
| **Apache Samza** | Created at LinkedIn (2013) | Stream processing framework |
| **Apache Pinot** | Created at LinkedIn (2015) | Real-time analytics database |
| **Voldemort** | LinkedIn's KV store | Influenced Cassandra and others |

### 6.3 Real-Time Data Architecture

```
Member Actions
      ↓
┌─────────────┐
│   Kafka     │ ← Event streaming backbone
│  (Brokers)  │
└──────┬──────┘
       ↓
┌─────────────────────────────────────┐
│        Stream Processors            │
│  ┌─────────┐ ┌─────────┐ ┌──────┐  │
│  │  Samza  │ │  Flink  │ │Spark │  │
│  │(Primary)│ │(Analytics)│ │(Batch)│ │
│  └────┬────┘ └────┬────┘ └───┬──┘  │
└───────┼──────────┼────────┼──────┘
        ↓          ↓        ↓
┌───────┴──────────┴────────┴───────┐
│        Serving Layer               │
│  ┌─────────┐ ┌─────────┐ ┌──────┐ │
│  │  Pinot  │ │ Espresso│ │Graph │ │
│  │(Analytics)│ │(Documents)│ │(Social)│ │
│  └─────────┘ └─────────┘ └──────┘ │
└─────────────────────────────────────┘
       ↓
   Member Experience
```

---
