# LinkedIn Engineering Stack

## Streaming & Messaging

### Apache Kafka (Created at LinkedIn, 2010)
- **Purpose**: Event streaming backbone
- **Scale**: Trillions of messages per day
- **Usage**: Activity tracking, metric collection, log aggregation
- **Key Features**: High throughput, low latency, fault tolerance

### Apache Samza (Created at LinkedIn, 2013)
- **Purpose**: Stream processing framework
- **Integration**: Works natively with Kafka
- **Use Cases**: Real-time analytics, complex event processing
- **Processing Model**: Stateful stream processing

## Analytics

### Apache Pinot (Created at LinkedIn, 2015)
- **Purpose**: Real-time OLAP analytics
- **Capabilities**: Sub-second queries on billions of rows
- **Features**: Real-time ingestion, time-series analysis
- **Use Cases**: Dashboards, anomaly detection, trend analysis

## Data Storage

### Espresso
- **Type**: Distributed document store
- **Purpose**: Primary data store for member profiles
- **Features**: Horizontal scaling, multi-region replication
- **Consistency**: Tunable consistency levels

### Voldemort
- **Type**: Distributed key-value store
- **Purpose**: High-throughput read-heavy workloads
- **Inspiration**: Influenced Cassandra design

### LinkedIn Graph (Custom)
- **Type**: Graph database
- **Purpose**: Social graph storage and queries
- **Scale**: Billions of nodes, trillions of edges
- **Query Language**: Custom graph traversal APIs

### OpenHouse
- **Type**: Control plane for Iceberg tables
- **Purpose**: Data lake management
- **Features**: RESTful catalog, data services

## Search

### Galene
- **Type**: LinkedIn's search engine
- **Purpose**: Member, company, job search
- **Features**: Real-time indexing, relevance ranking

## Machine Learning

### Training Frameworks
- TensorFlow
- PyTorch

### Feature Store
- Centralized feature management
- Real-time and batch features
- Feature versioning and lineage

### Model Serving
- Real-time inference APIs
- A/B testing infrastructure
- Model versioning and rollback

## Cloud Infrastructure

### Microsoft Azure
- Primary cloud provider
- Integration with Microsoft 365
- AI/ML services (Azure ML)

### Data Centers
- Maintained own data centers pre-2022
- Hybrid Azure migration
- Global presence with regional replication

## Programming Languages

| Language | Usage |
|----------|-------|
| Java | Backend services, Kafka |
| Scala | Big data processing, Spark |
| Python | ML/AI, data science |
| JavaScript/TypeScript | Frontend applications |
| C++ | Performance-critical systems |

## Data Infrastructure

### Hadoop Ecosystem
- HDFS for distributed storage
- Spark for batch processing
- Hive for data warehousing

### Real-Time Processing
- Kafka → Samza → Pinot pipeline
- Event sourcing architecture
- Lambda architecture (batch + real-time)

### Data Governance
- OpenHouse for table management
- Apache Iceberg for table format
- Data lineage tracking
