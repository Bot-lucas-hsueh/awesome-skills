# Lyft Technology Stack

## Core Platform Architecture

### Infrastructure

| Layer | Technology |
|-------|------------|
| **Cloud Provider** | AWS (Primary), Multi-region |
| **Container Orchestration** | Kubernetes (K8s) |
| **Service Mesh** | Envoy Proxy |
| **API Gateway** | Custom/Envoy |
| **Message Queue** | Apache Kafka, Kinesis |
| **Caching** | Redis, Memcached |
| **CDN** | CloudFront |

### Databases

| Type | Technology | Use Case |
|------|------------|----------|
| **Primary Database** | MySQL, PostgreSQL | Transactional data |
| **NoSQL** | MongoDB, DynamoDB | Document storage |
| **Data Warehouse** | Snowflake, BigQuery | Analytics |
| **Time Series** | TimescaleDB, InfluxDB | Metrics, GPS |
| **Graph** | Neo4j | Network analysis |

## Machine Learning Stack

### Recommendation & Ranking

| Component | Technology |
|-----------|------------|
| **Framework** | LightGBM (Microsoft) |
| **Ranking** | LambdaRank, LambdaMART |
| **Classification** | XGBoost, LightGBM |
| **Deep Learning** | PyTorch, TensorFlow |
| **Feature Store** | Feast, Tecton |
| **Model Serving** | Triton, custom gRPC |

### ML Infrastructure

| Component | Technology |
|-----------|------------|
| **Training Platform** | Kubeflow, SageMaker |
| **Experiment Tracking** | MLflow, Weights & Biases |
| **Model Registry** | MLflow Model Registry |
| **Monitoring** | Evidently, custom dashboards |

## Matching Algorithm

### Batch Matching System

```
Input: Driver positions, Rider requests, Constraints
↓
Batch Window: 5-10 seconds
↓
Optimization: Weighted bipartite matching
↓
Output: Driver-Rider pairs
```

### Key Algorithms

| Algorithm | Purpose |
|-----------|---------|
| **Hungarian Algorithm** | Optimal assignment |
| **Stable Marriage** | Preference matching |
| **Geospatial Indexing** | S2 Geometry, H3 |
| **ETA Prediction** | Gradient Boosted Trees |
| **Surge Pricing** | Dynamic optimization |

## Mobile Applications

### Rider App

| Platform | Technology |
|----------|------------|
| **iOS** | Swift, SwiftUI |
| **Android** | Kotlin, Jetpack Compose |
| **Maps** | Mapbox, Google Maps |
| **Payments** | Stripe, Braintree |

### Driver App

| Feature | Technology |
|---------|------------|
| **Navigation** | In-app navigation, Waze SDK |
| **Earnings** | Real-time calculation |
| **Heat Maps** | Real-time demand visualization |
| **Incentives** | Gamification engine |

## Real-Time Systems

### Streaming Architecture

| Component | Technology |
|-----------|------------|
| **Event Streaming** | Apache Kafka |
| **Stream Processing** | Flink, Kafka Streams |
| **Pub/Sub** | Redis Pub/Sub |
| **WebSockets** | Custom implementation |

### GPS & Geolocation

| Component | Technology |
|-----------|------------|
| **Location Tracking** | GPS, WiFi, Cell towers |
| **Geofencing** | Custom polygon matching |
| **Route Optimization** | OSRM, Valhalla |
| **Map Matching** | Hidden Markov Model |

## Pricing Systems

### Dynamic Pricing Engine

```
Demand Signals → ML Model → Price Multiplier
                    ↑
Supply Signals → Driver Availability
```

### Components

| Component | Description |
|-----------|-------------|
| **Prime Time** | Percentage-based surge |
| **Personal Power Zones** | Guaranteed earnings areas |
| **Predictive Pricing** | 15-min ahead demand prediction |
| **Elasticity Models** | City-level price sensitivity |

## Data Platform

### Data Pipeline

| Layer | Technology |
|-------|------------|
| **Ingestion** | Kafka Connect, Kinesis |
| **Processing** | Spark, Flink |
| **Storage** | S3, Delta Lake |
| **Query** | Presto/Trino, BigQuery |
| **Visualization** | Tableau, Looker, Superset |

### Data Types

| Category | Examples |
|----------|----------|
| **Operational** | Rides, payments, user profiles |
| **Telemetry** | GPS traces, app events |
| **ML Features** | User behavior, demand patterns |
| **Analytics** | Aggregated metrics, forecasts |

## DevOps & SRE

| Practice | Tools |
|----------|-------|
| **CI/CD** | Jenkins, CircleCI, Spinnaker |
| **Monitoring** | Datadog, Prometheus, Grafana |
| **Logging** | ELK Stack, Splunk |
| **Tracing** | Jaeger, Zipkin |
| **Feature Flags** | LaunchDarkly |
| **Incident Response** | PagerDuty |

## Security

| Layer | Implementation |
|-------|----------------|
| **Authentication** | OAuth 2.0, SSO |
| **API Security** | Rate limiting, JWT |
| **Data Encryption** | AES-256, TLS 1.3 |
| **Fraud Detection** | ML-based real-time scoring |

---
*Based on Lyft Engineering Blog, Conference Talks, and Industry Analysis*
