# Oracle Domain Knowledge Reference

> **Deep technical details for OCI, Database, and Enterprise Applications**

---

## Table of Contents

1. [OCI Architecture](#oci-architecture)
2. [Oracle Database 23ai](#oracle-database-23ai)
3. [AI Vector Search](#ai-vector-search)
4. [Multi-Cloud Strategy](#multi-cloud-strategy)
5. [Enterprise Applications](#enterprise-applications)

---

## OCI Architecture

### Gen2 Cloud Design Philosophy

Oracle Cloud Infrastructure (OCI) was built from the ground up as a Generation 2 cloud,
designed specifically for enterprise workloads with these differentiators:

| Aspect | OCI Approach | Traditional Cloud |
|--------|--------------|-------------------|
| **Network** | Non-blocking flat topology | Tiered, oversubscribed |
| **Virtualization** | Bare metal standard | Virtualization-heavy |
| **Storage** | NVMe local + block | Shared pools |
| **Pricing** | Simple, predictable | Complex, variable |
| **Performance** | Consistent, HPC-optimized | Burstable |

### OCI Global Footprint

**Public Cloud Regions (75+ live, 14+ planned):**

```yaml
Americas:
  - us-ashburn-1, us-phoenix-1 (US)
  - us-sanjose-1, us-chicago-1 (US)
  - ca-toronto-1, ca-montreal-1 (Canada)
  - sa-saopaulo-1, sa-vinhedo-1 (Brazil)
  - sa-bogota-1 (Colombia)
  - sa-santiago-1 (Chile)

Europe:
  - uk-london-1, uk-cardiff-1 (UK)
  - eu-frankfurt-1, eu-munich-1 (Germany)
  - eu-amsterdam-1 (Netherlands)
  - eu-paris-1, eu-marseille-1 (France)
  - eu-milan-1, eu-turin-1 (Italy)
  - eu-madrid-1, eu-barcelona-1 (Spain)
  - eu-stockholm-1 (Sweden)
  - eu-zurich-1 (Switzerland)
  - eu-jovanovac-1 (Serbia)

Asia Pacific:
  - ap-tokyo-1, ap-osaka-1 (Japan)
  - ap-seoul-1, ap-chuncheon-1 (Korea)
  - ap-singapore-1 (Singapore)
  - ap-sydney-1, ap-melbourne-1 (Australia)
  - ap-mumbai-1, ap-hyderabad-1 (India)
  - ap-mumbai-2 (India - Disaster Recovery)
  - ap-ibaraki-1, ap-tokyo-2 (Japan)

Middle East & Africa:
  - me-jeddah-1, me-riyadh-1 (Saudi Arabia)
  - me-dubai-1, me-abudhabi-1 (UAE)
  - af-johannesburg-1 (South Africa)
  - il-jerusalem-1 (Israel)
```

**OCI Dedicated Region:**
- Full OCI cloud in customer data center
- Minimum 3 racks (OCI Dedicated Region25)
- 200+ AI and cloud services
- Oracle-managed infrastructure

### Core OCI Services

**Compute:**

| Service | Description | Use Case |
|---------|-------------|----------|
| **Bare Metal** | Physical servers, no hypervisor | HPC, databases, performance-critical |
| **VM** | Virtual machines | General purpose workloads |
| **Dedicated VM Host** | Socket-level visibility | Licensing compliance |
| **Container Engine (OKE)** | Managed Kubernetes | Container orchestration |
| **Functions** | Serverless compute | Event-driven, short tasks |

**Storage:**

| Service | Durability | Latency | Use Case |
|---------|------------|---------|----------|
| **Object Storage** | 99.999999999% (11 9s) | ms | Backups, archives, media |
| **Block Volume** | 99.9999% | sub-ms | Database, boot volumes |
| **File Storage** | 99.9999% | ms | Shared filesystems (NFS) |
| **Archive Storage** | 99.999999999% | hours | Cold data, compliance |

**Database Services:**

| Service | Target | Key Feature |
|---------|--------|-------------|
| **Autonomous Database** | All workloads | Self-driving, auto-tuning |
| **Exadata Database Service** | Extreme performance | Exadata Cloud, sub-ms latency |
| **Base Database** | Control & flexibility | Full DBA access |
| **NoSQL Database** | Document, key-value | Serverless, elastic |
| **MySQL HeatWave** | Analytics + OLTP | In-memory analytics |

**AI/ML Services:**

| Service | Description | Use Case |
|---------|-------------|----------|
| **OCI Generative AI** | LLM inference | Text generation, summarization |
| **OCI AI Agent Platform** | Agent development | AI agents, automation |
| **OCI Vision** | Computer vision | Image analysis, OCR |
| **OCI Speech** | Speech-to-text | Audio transcription |
| **OCI Language** | NLP services | Sentiment, entity extraction |

**Security Services:**

| Service | Function | Capability |
|---------|----------|------------|
| **Identity and Access Management (IAM)** | Authentication, authorization | Policies, federation, MFA |
| **Cloud Guard** | Threat detection | AI-driven security monitoring |
| **Data Safe** | Data security | Masking, auditing, discovery |
| **Vault** | Secrets management | HSM-backed encryption |
| **Bastion** | Secure access | Zero-trust session access |
| **Web Application Firewall (WAF)** | Application security | DDoS protection, bot management |
| **Zero Trust Packet Routing (ZPR)** | Network security | Default-deny network policies |

---

## Oracle Database 23ai

### Converged Database Architecture

Oracle Database 23ai is the latest long-term support release, featuring over 300
major enhancements and thousands of improvements.

```
┌─────────────────────────────────────────────────────────────────┐
│                    Oracle Database 23ai                         │
├─────────────────────────────────────────────────────────────────┤
│                     Data Access Layer                            │
├───────────┬───────────┬───────────┬───────────┬─────────────────┤
│Relational │   JSON    │   Graph   │  Spatial  │  Vector / ML    │
│   SQL     │ Document  │ Property  │   Maps    │  AI Search      │
├───────────┼───────────┼───────────┼───────────┼─────────────────┤
│ SQL:2016  │ JSON/     │ SQL/PGQ   │ OGC       │ VECTOR          │
│ Analytic  │ REST      │ Standard  │ Standards │ Datatype        │
│ Functions │ APIs      │           │           │ Similarity      │
├───────────┴───────────┴───────────┴───────────┴─────────────────┤
│              Unified Storage & Processing Layer                  │
│         (Single engine, ACID transactions, parallel)            │
├─────────────────────────────────────────────────────────────────┤
│                    Infrastructure Layer                          │
├───────────────┬───────────────┬─────────────────────────────────┤
│   Exadata     │   Cloud       │      Cloud@Customer             │
├───────────────┼───────────────┼─────────────────────────────────┤
│  Engineered   │  Autonomous   │      On-premises                │
│  Systems      │  Database     │      Cloud                      │
└───────────────┴───────────────┴─────────────────────────────────┘
```

### Key 23ai Features

#### AI Vector Search

Native vector capabilities for AI/ML workloads:

```sql
-- Vector datatype
CREATE TABLE documents (
    id NUMBER PRIMARY KEY,
    content CLOB,
    embedding VECTOR(1536, FLOAT32)
);

-- Vector index for similarity search
CREATE VECTOR INDEX idx_doc_embedding
ON documents(embedding)
ORGANIZATION NEIGHBOR PARTITIONS
DISTANCE COSINE
WITH TARGET ACCURACY 95;

-- Similarity search
SELECT content,
       VECTOR_DISTANCE(embedding, :query_vector, COSINE) as similarity
FROM documents
ORDER BY similarity
FETCH FIRST 10 ROWS ONLY;
```

**Supported Distance Metrics:**
- COSINE (default)
- EUCLIDEAN
- EUCLIDEAN_SQUARED
- HAMMING
- MANHATTAN
- DOT

#### JSON Relational Duality

Dual access patterns for modern applications:

```sql
-- Create duality view over relational tables
CREATE JSON RELATIONAL DUALITY VIEW customer_orders AS
SELECT JSON {
    'customer_id' : c.customer_id,
    'name' : c.customer_name,
    'email' : c.email,
    'orders' : [
        SELECT JSON {
            'order_id' : o.order_id,
            'order_date' : o.order_date,
            'total' : o.total_amount
        }
        FROM orders o
        WHERE o.customer_id = c.customer_id
    ]
}
FROM customers c
WITH INSERT UPDATE DELETE;

-- GET as JSON document
SELECT JSON_SERIALIZE(data)
FROM customer_orders
WHERE JSON_VALUE(data, '$.customer_id') = 101;

-- PUT updates underlying tables
UPDATE customer_orders
SET data = JSON {...}
WHERE JSON_VALUE(data, '$.customer_id') = 101;
```

**Benefits:**
- Single data store, no duplication
- ACID transactions across both access patterns
- Lock-free optimistic concurrency control
- Automatic ETAG generation

#### Property Graph Views

SQL/PGQ standard graph queries:

```sql
-- Create property graph
CREATE PROPERTY GRAPH bank_graph
    VERTEX TABLES (
        accounts KEY (account_id)
        PROPERTIES (account_id, name, balance)
    )
    EDGE TABLES (
        transactions KEY (transaction_id)
        SOURCE KEY (from_account) REFERENCES accounts
        DESTINATION KEY (to_account) REFERENCES accounts
        PROPERTIES (transaction_id, amount, transaction_date)
    );

-- Graph query (find money laundering patterns)
SELECT a1.account_id, a2.account_id, a3.account_id
FROM GRAPH_TABLE (bank_graph,
    MATCH (a1)-[t1]->(a2)-[t2]->(a3)
    WHERE t1.amount > 10000 AND t2.amount > 10000
    COLUMNS (a1.account_id, a2.account_id, a3.account_id)
);
```

#### In-Database ML

Machine learning without moving data:

```sql
-- Create ML model
BEGIN
    DBMS_DATA_MINING.CREATE_MODEL(
        model_name => 'CHURN_PREDICTION',
        mining_function => DBMS_DATA_MINING.CLASSIFICATION,
        data_table_name => 'CUSTOMERS',
        case_id_column_name => 'CUSTOMER_ID',
        target_column_name => 'CHURNED',
        settings_table_name => 'CHURN_SETTINGS'
    );
END;
/

-- Real-time prediction
SELECT customer_id,
       PREDICTION(CHURN_PREDICTION USING *) as prediction,
       PREDICTION_PROBABILITY(CHURN_PREDICTION, 1 USING *) as probability
FROM customers
WHERE customer_id = :id;
```

#### Security Enhancements

**SQL Firewall:**
```sql
-- Create SQL Firewall policy
BEGIN
    DBMS_SQL_FIREWALL.CREATE_POLICY(
        policy_name => 'PROD_FIREWALL',
        allow_sql_injection => FALSE,
        allow_unauthorized_sql => FALSE
    );
END;
/

-- Enable for user
BEGIN
    DBMS_SQL_FIREWALL.ENABLE_USER(
        policy_name => 'PROD_FIREWALL',
        username => 'APP_USER'
    );
END;
/
```

**Read-Only Users:**
```sql
-- Create read-only user
CREATE USER reporting_user IDENTIFIED BY password READ ONLY;

-- Alter existing user
ALTER USER existing_user READ ONLY;
```

**DB_DEVELOPER_ROLE:**
```sql
-- Grant all developer privileges in one command
GRANT DB_DEVELOPER_ROLE TO developer_user;
```

### Autonomous Database

**Self-Driving Capabilities:**

| Capability | Implementation | Benefit |
|------------|----------------|---------|
| **Self-Driving** | AI-based query optimization, auto-indexing | Zero tuning effort |
| **Self-Securing** | Auto-patching (no downtime), threat detection | Always secure |
| **Self-Repairing** | Automatic backup, failover, recovery | 99.995% uptime |
| **Auto-Scaling** | Compute/storage independent scaling | Cost optimization |

**Workload Types:**
- **ATP (Autonomous Transaction Processing)**: OLTP, mixed workloads
- **ADW (Autonomous Data Warehouse)**: Analytics, BI, reporting
- **AJD (Autonomous JSON Database)**: Document-centric apps

**Deployment Options:**
- **Serverless**: Fully managed, pay-per-use
- **Dedicated**: Isolated Exadata infrastructure
- **Cloud@Customer**: On-premises OCI deployment

---

## AI Vector Search

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    RAG Application                               │
└───────────────────────────┬─────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
   ┌─────────┐       ┌─────────────┐      ┌─────────────┐
   │  User   │       │   Oracle    │      │   OCI Gen   │
   │  Query  │──────▶│  Database   │◀─────│     AI      │
   └─────────┘       │   23ai      │      │  Service    │
                     └──────┬──────┘      └─────────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
        ┌──────────┐ ┌────────────┐ ┌────────────┐
        │  Vector  │ │ Similarity │ │  Generate  │
        │  Store   │ │   Search   │ │  Response  │
        └──────────┘ └────────────┘ └────────────┘
```

### Implementation Pattern

**Step 1: Create Vector Table**
```sql
CREATE TABLE knowledge_base (
    doc_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR2(200),
    content CLOB,
    embedding VECTOR(1536, FLOAT32),
    metadata JSON,
    created_at TIMESTAMP DEFAULT SYSTIMESTAMP
);
```

**Step 2: Generate Embeddings**
```python
# Using OCI Generative AI
import oci

ai_client = oci.generative_ai.GenerativeAiClient(config)

# Generate embedding for content
response = ai_client.embed_text(
    embed_text_details={
        "inputs": ["Your text here"],
        "serving_mode": {
            "servingType": "ON_DEMAND",
            "modelId": "cohere.embed-english-v3"
        }
    }
)
embedding = response.data.embeddings[0]
```

**Step 3: Store with Vector**
```sql
INSERT INTO knowledge_base (title, content, embedding)
VALUES (
    'Oracle Database 23ai',
    'Oracle Database 23ai introduces AI Vector Search...',
    VECTOR(:embedding_array)
);
```

**Step 4: Similarity Search**
```sql
WITH relevant_docs AS (
    SELECT title, content,
           VECTOR_DISTANCE(embedding, :query_embedding, COSINE) as distance
    FROM knowledge_base
    WHERE VECTOR_DISTANCE(embedding, :query_embedding, COSINE) < 0.3
    ORDER BY distance
    FETCH FIRST 5 ROWS ONLY
)
SELECT * FROM relevant_docs;
```

**Step 5: RAG with LLM**
```sql
SELECT AI.GENERATE(
    prompt => 'Answer based on context: ' ||
              (SELECT content FROM knowledge_base WHERE doc_id = :doc_id) ||
              ' Question: ' || :user_question,
    provider => 'OCI',
    model => 'cohere.command-r-plus'
) AS response
FROM DUAL;
```

---

## Multi-Cloud Strategy

### Database@Azure

**Availability:** 28 regions live, 5 planned

```yaml
Regions:
  Live: Australia East, Australia Southeast, Brazil South, Canada Central,
        Canada East, Central India, Central US, East US, East US 2, France Central,
        Germany North, Germany West Central, Italy North, Japan East, Japan West,
        North Europe, Southeast Asia, South Central US, Spain Central, Sweden Central,
        Switzerland North, UAE Central, UAE North, UK South, UK West, West US,
        West US 2, West US 3
  Planned: Brazil Southeast, France South, North Central US, South India, West Europe

Services:
  - Oracle Autonomous Database
  - Oracle Base Database Service
  - Oracle Exadata Database Service
  - Oracle Autonomous AI Lakehouse
  - OCI GoldenGate
```

### Database@AWS

**Availability:** 2 regions live, 20 planned

```yaml
Regions:
  Live: US East (N. Virginia), US West (Oregon)
  Planned: Canada (Central), Frankfurt, Hyderabad, Ireland, London, Melbourne,
           Milan, Mumbai, Osaka, Paris, São Paulo, Seoul, Singapore, Spain,
           Stockholm, Sydney, Tokyo, US East (Ohio), US West (N. California), Zurich

Services:
  - Oracle Autonomous Database
  - Oracle Exadata Database Service
  - Oracle Base Database Service
  - Oracle Autonomous AI Lakehouse
  - Oracle Database Zero Data Loss Autonomous Recovery Service
```

### Database@Google Cloud

**Availability:** 8+ regions live, 17 planned

```yaml
Regions:
  Live: Tokyo (asia-northeast1), London (europe-west2), Ashburn (us-east4),
        Salt Lake City (us-west3), Melbourne (australia-southeast2),
        Montreal (northamerica-northeast1), Iowa (us-central1), Frankfurt (europe-west3)
  Planned: Mexico, Sydney, Osaka, Mumbai, Delhi, Milan, Turin, Toronto, São Paulo

Services:
  - Oracle Exadata Database Service on Exascale Infrastructure
  - Oracle Base Database Service
  - Oracle Autonomous AI Lakehouse
```

### Interconnect

**Oracle Interconnect for Azure:**
- 18+ global regions
- <2ms latency
- Native Azure portal integration

**Oracle Interconnect for Google Cloud:**
- 8+ global regions
- Cross-cloud data sharing
- Unified billing options

---

## Enterprise Applications

### Oracle Fusion Cloud Applications

**Fusion ERP:**
- Financial management
- Revenue management
- Project management
- Procurement
- Risk management
- FY2025 Revenue: $0.9B (up 16%)

**Fusion HCM:**
- Core HR
- Payroll
- Talent management
- Workforce rewards
- Workforce management

**Fusion SCM:**
- Supply chain planning
- Manufacturing
- Order management
- Logistics
- Product lifecycle management

**Fusion CX:**
- Sales
- Service
- Marketing
- Customer data platform

### NetSuite

**Overview:**
- Cloud ERP for mid-market
- 36,000+ customers
- 220+ countries supported
- FY2025 Revenue: $0.9B (up 16%)

**Modules:**
- Financials
- CRM
- E-commerce
- PSA (Professional Services Automation)
- Inventory management

### Oracle Health (Cerner)

**Acquisition:** $28.3B (2022) — Oracle's largest ever

**Products:**
- **Millennium EHR**: Electronic health record platform
- **HealtheIntent**: Population health management
- **Cerner RevWorks**: Revenue cycle management

**Integration:**
- Oracle Cloud infrastructure
- AI-powered healthcare analytics
- Unified patient records
- Clinical decision support

---

*Reference Version: 5.0.0 | Updated: 2026-03-21*
