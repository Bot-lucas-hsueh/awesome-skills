# Oracle Engineering Workflows

> **Standard procedures for Oracle cloud and database operations**

---

## Table of Contents

1. [Database Migration Workflow](#database-migration-workflow)
2. [Autonomous Database Provisioning](#autonomous-database-provisioning)
3. [AI Application Development](#ai-application-development)
4. [Disaster Recovery Implementation](#disaster-recovery-implementation)
5. [Multi-Cloud Deployment](#multi-cloud-deployment)

---

## Database Migration Workflow

### Overview

Complete workflow for migrating Oracle databases to OCI with minimal downtime.

### Phase 1: Assessment (Week 1)

| Step | Action | Output | Validation |
|------|--------|--------|------------|
| 1.1 | Run OCI Migration Advisor | Assessment report | Compatibility score >90% |
| 1.2 | Identify dependencies | Dependency map | No circular references |
| 1.3 | Size target infrastructure | Sizing document | Performance baseline |
| 1.4 | Create migration plan | Project plan | Timeline approved |

**OCI Migration Advisor:**
```bash
# Run assessment tool
./omadm-cli.sh assess \
    --source-db-host source-db.company.com \
    --source-db-name PRODDB \
    --source-version 19c \
    --target-cloud-region us-ashburn-1 \
    --output-dir ./assessment

# Review assessment report
cat ./assessment/compatibility_report.html
```

### Phase 2: Preparation (Week 2)

| Step | Action | Output | Validation |
|------|--------|--------|------------|
| 2.1 | Provision OCI infrastructure | Cloud resources | Health checks pass |
| 2.2 | Configure network connectivity | VPN/FastConnect | Latency <10ms |
| 2.3 | Set up GoldenGate replication | Extract/Replicat | Replication lag <1s |
| 2.4 | Validate data types | Type mapping doc | No data loss risk |

**Infrastructure Provisioning (Terraform):**
```hcl
# Network infrastructure
resource "oci_core_vcn" "migration_vcn" {
    compartment_id = var.compartment_id
    cidr_block     = "10.0.0.0/16"
    display_name   = "migration-vcn"
    dns_label      = "migration"
}

# Autonomous Database target
resource "oci_database_autonomous_database" "target" {
    compartment_id              = var.compartment_id
    db_name                     = "PRODDBMIG"
    display_name                = "Production Migration Target"
    db_workload                 = "OLTP"
    db_version                  = "19c"
    license_model               = "BRING_YOUR_OWN_LICENSE"
    autonomous_database_infrastructure_type = "DEDICATED"
    cpu_core_count              = 16
    data_storage_size_in_tbs    = 100
    is_auto_scaling_enabled     = true
    backup_retention_period_in_days = 60
}
```

**GoldenGate Setup:**
```bash
# Create GoldenGate deployment
oci golden-gate deployment create \
    --compartment-id $COMPARTMENT_ID \
    --display-name "Migration-GG" \
    --license-model BRING_YOUR_OWN_LICENSE \
    --cpu-core-count 4 \
    --is-auto-scaling-enabled true

# Configure Extract
EXTRACT ext1
USERIDALIAS ggs_admin DOMAIN OracleGoldenGate
EXTTRAIL ./dirdat/et
TRANLOGOPTIONS INTEGRATEDPARAMS (max_sga_size 256)
TABLE schema.*;

# Configure Replicat
REPLICAT rep1
USERIDALIAS ggs_admin DOMAIN OracleGoldenGate
MAP schema.*, TARGET schema.*;
```

### Phase 3: Migration (Week 3)

| Step | Action | Output | Validation |
|------|--------|--------|------------|
| 3.1 | Initial data load | Data Pump export/import | Row counts match |
| 3.2 | Enable replication | Real-time sync | Lag monitoring active |
| 3.3 | Application testing | Test results | 100% test pass |
| 3.4 | Performance tuning | Tuning recommendations | Query times met |

**Data Pump Export/Import:**
```bash
# Export from source
expdp system/password \
    DIRECTORY=DATA_PUMP_DIR \
    DUMPFILE=prod_db_%U.dmp \
    SCHEMAS=schema1,schema2 \
    PARALLEL=8 \
    COMPRESSION=ALL \
    LOGFILE=expdp_prod.log

# Import to target
impdp admin/password@target_db \
    DIRECTORY=DATA_PUMP_DIR \
    DUMPFILE=prod_db_%U.dmp \
    SCHEMAS=schema1,schema2 \
    PARALLEL=8 \
    TRANSFORM=DISABLE_ARCHIVE_LOGGING:Y \
    LOGFILE=impdp_prod.log
```

**Validation:**
```sql
-- Compare row counts
SELECT table_name,
       (SELECT COUNT(*) FROM table_name@source) as source_count,
       (SELECT COUNT(*) FROM table_name) as target_count
FROM user_tables;

-- Verify object counts
SELECT object_type, COUNT(*) as count
FROM user_objects
GROUP BY object_type
ORDER BY object_type;
```

### Phase 4: Cutover (Week 4)

| Step | Action | Output | Validation |
|------|--------|--------|------------|
| 4.1 | Final sync verification | Data checksum match | Zero divergence |
| 4.2 | Application switch | DNS cutover | <5 min downtime |
| 4.3 | Post-migration validation | Validation report | Business sign-off |
| 4.4 | Decommission source | Archive and cleanup | Cost savings |

**ZDM Cutover:**
```bash
# Execute final switchover
zdmcli migrate database \
    -jobid previous_job_id \
    -switchover

# Verify target is primary
sqlplus admin/password@target_db <<EOF
SELECT database_role, open_mode FROM v\$database;
EOF
```

---

## Autonomous Database Provisioning

### Requirements Gathering

```yaml
Workload Assessment:
  Type: OLTP / Data Warehouse / JSON / APEX
  Concurrency: Peak concurrent users
  Data Volume: Current + 3-year growth
  Performance: Query response time SLAs
  
Deployment Options:
  Tier: Serverless / Dedicated / Cloud@Customer
  Network: Public endpoint / Private endpoint
  Region: Primary region + DR region
  
Operational Requirements:
  Backup Retention: 7-60 days
  Auto-scaling: Enabled / Disabled
  CPU Limits: Min / Max ECPUs
  Storage Limits: Max TB
```

### Provisioning Steps

**Step 1: Create Database**
```bash
oci db autonomous-database create \
    --compartment-id $COMPARTMENT_ID \
    --db-name $DB_NAME \
    --display-name "$DISPLAY_NAME" \
    --db-workload OLTP \
    --is-dedicated false \
    --cpu-core-count 2 \
    --data-storage-size-in-tbs 1 \
    --is-auto-scaling-enabled true \
    --license-model BRING_YOUR_OWN_LICENSE \
    --whitelisted-ips '["203.0.113.0/24"]' \
    --backup-retention-period-in-days 30
```

**Step 2: Configure Network**
```bash
# Create private endpoint
oci db autonomous-database update \
    --autonomous-database-id $DB_OCID \
    --subnet-id $SUBNET_OCID \
    --nsg-ids '["'$NSG_OCID'"]'
```

**Step 3: Create Application Schema**
```sql
-- Create schema user
CREATE USER app_schema IDENTIFIED BY "SecurePassword123!"
DEFAULT TABLESPACE DATA
QUOTA UNLIMITED ON DATA
QUOTA UNLIMITED ON USERS;

-- Grant privileges
GRANT CREATE SESSION,
    CREATE TABLE,
    CREATE SEQUENCE,
    CREATE TRIGGER,
    CREATE PROCEDURE,
    CREATE TYPE,
    CREATE VIEW,
    CREATE SYNONYM
TO app_schema;

-- Grant AI Vector Search privileges (23ai)
GRANT DB_DEVELOPER_ROLE TO app_schema;
```

**Step 4: Configure Auto-scaling**
```sql
-- Set auto-scaling limits
BEGIN
    DBMS_CLOUD_ADMIN.SET_AUTO_SCALING(
        max_cpu_core_count => 8,
        max_storage_tbs => 10
    );
END;
/
```

**Step 5: Enable Monitoring**
```bash
# Enable Operations Insights
oci opsi database-insights enable \
    --database-id $ADB_ID \
    --compartment-id $COMPARTMENT_ID \
    --entity-type AUTONOMOUS_DATABASE

# Create CPU alert
oci monitoring alarm create \
    --display-name "High CPU Alert - $DB_NAME" \
    --metric-compartment-id $COMPARTMENT_ID \
    --namespace oci_autonomous_database \
    --query "CpuUtilization[5m].mean() > 80" \
    --destinations '["'$TOPIC_OCID'"]' \
    --severity CRITICAL
```

---

## AI Application Development

### Architecture Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │   User      │  │  RAG        │  │   LLM Integration   │ │
│  │  Interface  │  │  Pipeline   │  │                     │ │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │
└─────────┼────────────────┼────────────────────┼────────────┘
          │                │                    │
          ▼                ▼                    ▼
┌─────────────────────────────────────────────────────────────┐
│                    Oracle Database 23ai                      │
│  ┌────────────────┐  ┌────────────────┐  ┌───────────────┐  │
│  │  Vector Store  │  │ Similarity     │  │  AI.GENERATE  │  │
│  │  (Embeddings)  │  │ Search         │  │  (SQL Function)│  │
│  └────────────────┘  └────────────────┘  └───────────────┘  │
└─────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────┐
│                    OCI Generative AI                         │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  Cohere Command, Llama, Embeddings Models             │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Implementation Steps

**Step 1: Data Preparation**
```sql
-- Create vector table
CREATE TABLE doc_embeddings (
    doc_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title VARCHAR2(500),
    content CLOB,
    embedding VECTOR(1536, FLOAT32),
    source_url VARCHAR2(1000),
    created_at TIMESTAMP DEFAULT SYSTIMESTAMP
);

-- Create vector index
CREATE VECTOR INDEX idx_doc_embedding
ON doc_embeddings(embedding)
ORGANIZATION NEIGHBOR PARTITIONS
DISTANCE COSINE
WITH TARGET ACCURACY 95;
```

**Step 2: Embedding Generation**
```python
import oci
import oracledb

# Initialize OCI AI client
ai_client = oci.generative_ai.GenerativeAiClient(config)

# Generate embeddings
def generate_embedding(text):
    response = ai_client.embed_text(
        embed_text_details={
            "inputs": [text],
            "serving_mode": {
                "servingType": "ON_DEMAND",
                "modelId": "cohere.embed-english-v3"
            }
        }
    )
    return response.data.embeddings[0]

# Store in database
conn = oracledb.connect(user="app_schema", password="pwd", dsn="db_medium")
cursor = conn.cursor()

embedding = generate_embedding(document_content)
cursor.execute("""
    INSERT INTO doc_embeddings (title, content, embedding)
    VALUES (:title, :content, VECTOR(:embedding))
"", {
    "title": doc_title,
    "content": doc_content,
    "embedding": str(embedding)  # Convert to string for VECTOR constructor
})
conn.commit()
```

**Step 3: RAG Query**
```sql
-- Similarity search function
CREATE OR REPLACE FUNCTION search_similar_docs(
    p_query_vector IN VECTOR,
    p_top_k IN NUMBER DEFAULT 5
) RETURN SYS_REFCURSOR AS
    v_result SYS_REFCURSOR;
BEGIN
    OPEN v_result FOR
    SELECT title, content,
           VECTOR_DISTANCE(embedding, p_query_vector, COSINE) as similarity
    FROM doc_embeddings
    WHERE VECTOR_DISTANCE(embedding, p_query_vector, COSINE) < 0.3
    ORDER BY similarity
    FETCH FIRST p_top_k ROWS ONLY;
    
    RETURN v_result;
END;
/

-- RAG query combining search + LLM
CREATE OR REPLACE FUNCTION generate_answer(
    p_question IN VARCHAR2
) RETURN CLOB AS
    v_context CLOB;
    v_answer CLOB;
    v_query_vector VECTOR(1536, FLOAT32);
BEGIN
    -- Generate embedding for question (via external call or pre-calculated)
    -- v_query_vector := ...;
    
    -- Retrieve relevant context
    SELECT LISTAGG(content, ' ') WITHIN GROUP (ORDER BY similarity)
    INTO v_context
    FROM (
        SELECT content,
               VECTOR_DISTANCE(embedding, v_query_vector, COSINE) as similarity
        FROM doc_embeddings
        ORDER BY similarity
        FETCH FIRST 3 ROWS ONLY
    );
    
    -- Generate answer using AI
    SELECT AI.GENERATE(
        prompt => 'Context: ' || v_context ||
                  ' Question: ' || p_question ||
                  ' Answer:',
        provider => 'OCI',
        model => 'cohere.command-r-plus'
    ) INTO v_answer
    FROM DUAL;
    
    RETURN v_answer;
END;
/
```

---

## Disaster Recovery Implementation

### Architecture Options

**Option 1: Data Guard (Physical Standby)**
```
Primary (OCI Ashburn) ──► Standby (OCI Phoenix)
    Autonomous DB            Autonomous DB
    RPO: <1 minute          Automatic failover
    RTO: <5 minutes
```

**Option 2: GoldenGate (Active-Active)**
```
Site A (OCI) ◄────► Site B (OCI)
  Active              Active
  Bidirectional replication
  Conflict resolution required
```

**Option 3: Multi-Cloud DR**
```
Primary (AWS) ──► Standby (OCI)
  Database@AWS     Autonomous DB
  FastConnect      Cross-cloud replication
```

### Implementation: Autonomous Database Data Guard

**Step 1: Enable Data Guard**
```sql
-- On primary Autonomous Database
BEGIN
    DBMS_CLOUD_ADMIN.ENABLE_DATAGUARD(
        standby_db_name => 'PRODDB_PHX',
        standby_region => 'us-phoenix-1',
        protection_mode => 'MAXIMUM_AVAILABILITY'
    );
END;
/
```

**Step 2: Configure Fast Start Failover**
```sql
-- Enable broker
ALTER SYSTEM SET DG_BROKER_START=TRUE SCOPE=BOTH;

-- Configure observer
BEGIN
    DBMS_DG_BROKER.CONFIGURE_FAST_START_FAILOVER(
        observer_host => 'observer.company.com',
        failover_threshold => 30
    );
END;
/
```

**Step 3: Monitor Replication**
```sql
-- Check replication lag
SELECT name, value, unit, time_computed
FROM v$dataguard_stats
WHERE name IN ('transport lag', 'apply lag', 'apply finish time');

-- Check sync status
SELECT database_role, switchover_status, protection_mode
FROM v$database;

-- Historical lag analysis
SELECT timestamp,
       ROUND(apply_lag/60, 2) as apply_lag_minutes,
       ROUND(transport_lag/60, 2) as transport_lag_minutes
FROM v$dataguard_stats_history
ORDER BY timestamp DESC
FETCH FIRST 24 ROWS ONLY;
```

**Step 4: Failover Procedure**
```bash
# Manual failover
oci db autonomous-database failover \
    --autonomous-database-id $STANDBY_ID \
    --database-admin-password "AdminPassword123!"

# Verify failover
oci db autonomous-database get \
    --autonomous-database-id $STANDBY_ID \
    --query "data.{\"Role\": \"database_role\", \"Status\": \"lifecycle_state\"}"

# Update application connection strings
# (DNS switch or application config update)
```

---

## Multi-Cloud Deployment

### Database@Azure Deployment

**Architecture:**
```
Azure VNet ──► Oracle Database@Azure
    │              (Exadata infrastructure)
    │              Private endpoint
    │
    └──► Azure App Service
         (Application tier)
```

**Deployment Steps:**

```bash
# Step 1: Register Oracle resource provider
az provider register --namespace Oracle.Database

# Step 2: Create delegated subnet
az network vnet subnet create \
    --name oracle-delegated \
    --vnet-name myVNet \
    --resource-group myRG \
    --delegations Oracle.Database/networkAttachments \
    --address-prefixes 10.0.1.0/24

# Step 3: Deploy Oracle Database@Azure
az oracle-database autonomous-database create \
    --name myadb \
    --resource-group myRG \
    --location eastus \
    --db-name mydb \
    --compute-model ECPU \
    --compute-count 2 \
    --data-storage-size-in-gbs 1024 \
    --license-model BringYourOwnLicense
```

### Cross-Cloud Replication

**GoldenGate Multi-Cloud Setup:**

```yaml
# Source (AWS)
Extract:
  Name: EXT_AWS
  Source: Oracle Database@AWS
  Trail: ./dirdat/aw

# Target (OCI)
Replicat:
  Name: REP_OCI
  Target: Autonomous Database
  Trail: ./dirdat/aw

# Monitoring
Lag Threshold: 5 seconds
Alert Channels: Email, PagerDuty, Slack
```

```sql
-- GoldenGate parameter files
-- EXT_AWS.prm
EXTRACT ext_aws
USERIDALIAS ggs_aws DOMAIN OracleGoldenGate
EXTTRAIL ./dirdat/aw
TRANLOGOPTIONS INTEGRATEDPARAMS (max_sga_size 256)
TABLE app_schema.*;

-- REP_OCI.prm
REPLICAT rep_oci
USERIDALIAS ggs_oci DOMAIN OracleGoldenGate
MAP app_schema.*, TARGET app_schema.*;
```

---

*Reference Version: 5.0.0 | Updated: 2026-03-21*
