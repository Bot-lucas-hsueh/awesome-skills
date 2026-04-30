# Spotify Technology Stack

## Architecture Overview

Spotify operates one of the world's largest audio streaming platforms, serving 750M+ users with a microservices architecture designed for scalability, resilience, and rapid iteration.

## Backend Technologies

### Primary Languages

| Language | Usage | Frameworks |
|----------|-------|------------|
| **Java** | Primary backend language | Spring Framework, Spring Boot |
| **Scala** | Data processing, functional programming | Scio (Apache Beam), Akka |
| **Node.js** | API services, real-time features | Express, NestJS |
| **Python** | Machine learning, data science | TensorFlow, PyTorch, scikit-learn |
| **Go** | Infrastructure tools, microservices | Native |

### Data Streaming & Messaging

**Apache Kafka**
- Role: Central nervous system for event streaming
- Scale: Billions of events per day
- Use Cases:
  - User interaction events (plays, skips, searches)
  - Log aggregation
  - Real-time analytics pipelines
  - Cross-service communication
- Configuration: Multiple clusters across regions

**Google Pub/Sub**
- Supplementary messaging for GCP-native services

### Databases

**Apache Cassandra**
- Role: Primary user data storage
- Use Cases: Playlists, user libraries, listening history
- Scale: Petabytes of data across multiple regions
- Migration: Moved from PostgreSQL in 2015 (sharks ate the cable incident)

**PostgreSQL**
- Role: Relational data requiring ACID guarantees
- Use Cases: Financial transactions, user accounts, rights metadata

**Redis**
- Role: In-memory caching
- Use Cases: Session storage, metadata caching, rate limiting
- Configuration: Clustered deployment

**Bigtable**
- Role: NoSQL for large-scale analytics
- Use Cases: Wrapped data processing, feature storage

**Elasticsearch**
- Role: Search and analytics
- Use Cases: Full-text search, log analysis

### Data Processing

**Apache Beam + Scio**
- Role: Batch and stream processing
- Language: Scala (via Scio library)
- Use Cases:
  - Wrapped data aggregation
  - Recommendation feature generation
  - Analytics pipelines
- Optimization: Sort Merge Bucket (SMB) for efficient joins

**Apache Spark**
- Role: Large-scale data processing
- Use Cases: ML training, analytics, ETL

**BigQuery**
- Role: Data warehouse
- Use Cases: Business intelligence, ad-hoc analysis

## Infrastructure & DevOps

### Cloud Platform

**Google Cloud Platform (GCP)**
- Primary cloud provider (migrated from AWS ~2015)
- Services used:
  - Compute Engine (VMs)
  - Kubernetes Engine (GKE)
  - Cloud Storage
  - BigQuery
  - Cloud Pub/Sub
  - Cloud CDN

### Container Orchestration

**Kubernetes**
- Role: Container orchestration
- Scale: Thousands of microservices
- Features:
  - Auto-scaling
  - Self-healing
  - Rolling deployments
- Impact: Significantly improved downtime metrics and resource efficiency

**Docker**
- Role: Containerization standard
- Use: All services containerized

### Infrastructure as Code

**Terraform**
- Role: Infrastructure provisioning
- Use: AWS and GCP resource management

**Helm**
- Role: Kubernetes package management

## Frontend Technologies

### Web Application

**React**
- Role: Primary UI library
- Architecture: Component-based, reusable design system

**Redux**
- Role: State management
- Pattern: Predictable state container

**TypeScript**
- Role: Type-safe JavaScript
- Coverage: 100% of new code

**Sass/SCSS**
- Role: CSS preprocessing

**Webpack**
- Role: Module bundling

### Mobile Applications

**iOS:**
- Language: Swift (modern), Objective-C (legacy)
- Build System: Bazel (migrated from Xcode build system in 2023)
- Architecture: MVVM with Combine/RxSwift

**Android:**
- Language: Kotlin (primary), Java (legacy)
- Architecture: MVVM with Jetpack
- Build System: Gradle

**Shared Code:**
- Platform APIs: TypeScript abstractions
- C++ core: Audio playback engine

### Desktop Applications

**Technology Stack (2021 redesign):**
- Shared codebase with Web Player
- Platform APIs: TypeScript abstractions
- Container: Electron-like native wrapper
- Features: Offline playback, local files, system integration

**Migration:**
- 2021: Unified desktop and web codebases
- Result: Faster feature rollout, consistency across platforms

## Machine Learning & AI

### Recommendation Systems

**Core Technologies:**
- TensorFlow Extended (TFX) for production ML
- Custom ML models for ranking and recommendations
- Embeddings for users, tracks, artists, podcasts

**Model Types:**
- Collaborative filtering (matrix factorization)
- Content-based filtering (audio features, NLP)
- Deep learning (neural collaborative filtering)
- Reinforcement learning (contextual bandits for recommendations)

**Feature Engineering:**
- User taste profiles (dynamic, real-time updates)
- Audio feature extraction (tempo, energy, valence, danceability)
- Text analysis (NLP on lyrics, metadata, web content)
- Session context (time of day, device, location)

### AI Features

**AI DJ:**
- Technology: Generative AI, voice synthesis
- Provider: Sonantic (acquired 2022) + internal models
- Capability: Personalized radio host with commentary

**Prompted Playlist:**
- Technology: LLM integration
- Capability: Natural language playlist generation

## Audio Technology

### Streaming Protocols

**Protocols:**
- HTTP Live Streaming (HLS) for audio
- Custom protocols for low-latency scenarios

**Codecs:**
| Quality | Codec | Bitrate |
|---------|-------|---------|
| Low | HE-AACv2 | 24 kbps |
| Normal | AAC | 96 kbps |
| High | Ogg Vorbis | 160 kbps |
| Premium | Ogg Vorbis | 320 kbps |
| HiFi (announced) | FLAC | Lossless |

### Audio Pipeline

1. **Ingestion:** Master files from labels/distributors
2. **Transcoding:** Multiple quality levels generated
3. **Storage:** Distributed across CDN nodes
4. **Delivery:** Adaptive bitrate based on network conditions
5. **Playback:** Client-side decoding and audio rendering

### Audio Analysis

**Features Extracted:**
- Tempo (BPM)
- Energy level
- Danceability
- Valence (positiveness)
- Acousticness
- Instrumentalness
- Liveness
- Speechiness
- Key and mode
- Loudness (LUFS)

**Technology:**
- Custom audio analysis pipelines
- Machine learning models trained on labeled data
- Real-time analysis on upload

## Developer Tools

### Backstage (Open Source)

**Origin:** Built internally at Spotify, donated to CNCF
**Purpose:** Developer portal for managing microservices
**Features:**
- Service catalog
- Software templates
- TechDocs (documentation)
- Plugin ecosystem
**Adoption:** 1000+ companies, including Spotify internally

### Build & CI/CD

**Version Control:** Git (GitHub Enterprise)
**CI/CD:** Custom pipelines + GitHub Actions
**Build Tools:**
- Bazel (iOS, large-scale builds)
- Gradle (Android)
- Webpack (Web)

**Deployment:**
- Staged rollouts (1% → 5% → 20% → 100%)
- Feature flags for gradual enablement
- Automated rollback on error rate increase

### Monitoring & Observability

**Prometheus:** Metrics collection
**Grafana:** Visualization and dashboards
**Jaeger:** Distributed tracing
**ELK Stack:** Log aggregation (Elasticsearch, Logstash, Kibana)
**PagerDuty:** Incident management

### Testing

**Types:**
- Unit tests (Jest, JUnit, XCTest)
- Integration tests
- End-to-end tests
- A/B testing in production

**Quality Gates:**
- Code coverage requirements
- Performance benchmarks
- Accessibility checks

## Security

### Practices

- End-to-end encryption for sensitive data
- Regular security audits and penetration testing
- Bug bounty program
- SOC 2 Type II compliance
- GDPR/CCPA compliance

### DRM

- Widevine (Google)
- FairPlay (Apple)
- Protection against unauthorized ripping/stream-ripping

## Key Technical Achievements

### Wrapped Data Processing
- Billions of events processed
- 750M+ personalized experiences generated
- Sort Merge Bucket methodology: 60% cost reduction

### Migration to Cassandra (2015)
- Triggered by Atlantic cable failure
- Zero downtime migration
- Dark loading technique

### Desktop/Web Unification (2021)
- Shared TypeScript codebase
- Platform abstraction layer
- 2x feature velocity improvement

### iOS Build System Migration (2023)
- 120+ teams involved
- Migrated to Bazel
- Improved build performance and consistency

---

*Sources: Spotify Engineering Blog, Conference talks (QCon, Spotify R&D), Open source projects*
