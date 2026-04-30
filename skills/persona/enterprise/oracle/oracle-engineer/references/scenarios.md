# Oracle Scenario Examples

## Scenario 1: Disaster Recovery Implementation

**Context**: Financial services company requires RPO <1 minute, RTO <15 minutes.

**Solution Architecture**:
```
Primary: OCI Ashburn (Autonomous Dedicated)
  ↓ GoldenGate Real-time Replication
Standby: OCI Phoenix (Autonomous Dedicated)
  ↓ Automated Failover
DR: OCI London (Read-only replica)
```

**Implementation**:
```sql
-- Enable Data Guard on Autonomous
BEGIN
  DBMS_CLOUD_ADMIN.ENABLE_DATAGUARD(
    standby_db_name => 'PRODDB_PHX',
    standby_region => 'us-phoenix-1'
  );
END;
/

-- Configure fast start failover
ALTER SYSTEM SET DG_BROKER_START=TRUE SCOPE=BOTH;

-- Monitor replication lag
SELECT name, value, unit, time_computed 
FROM v$dataguard_stats 
WHERE name IN ('transport lag', 'apply lag', 'apply finish time');
```

**Failover Procedure**:
```bash
# 1. Check primary status
oci db autonomous-database get --autonomous-database-id $PRIMARY_ID

# 2. Initiate failover
oci db autonomous-database failover \
  --autonomous-database-id $STANDBY_ID \
  --database-admin-password "AdminPassword123!"

# 3. Update application connections
# (DNS switch or application config update)

# 4. Verify standby is now primary
oci db autonomous-database get --autonomous-database-id $STANDBY_ID
```

## Scenario 2: Multi-Tenant SaaS Database Design

**Context**: SaaS provider serving 1,000+ customers with data isolation requirements.

**Architecture Options**:

### Option A: Pluggable Database (PDB) per Tenant
```sql
-- Container Database (CDB) setup
CREATE PLUGGABLE DATABASE tenant_001
  ADMIN USER tenant_admin IDENTIFIED BY password
  FILE_NAME_CONVERT = ('pdbseed', 'tenant_001');

ALTER PLUGGABLE DATABASE tenant_001 OPEN;

-- PDB-level resource management
ALTER SYSTEM SET cpu_count = 2 CONTAINER = tenant_001;
ALTER SYSTEM SET sga_target = 4G CONTAINER = tenant_001;
```

### Option B: Schema per Tenant
```sql
-- Single database with isolated schemas
CREATE USER tenant_001_schema IDENTIFIED BY password
DEFAULT TABLESPACE tenant_001_ts
QUOTA UNLIMITED ON tenant_001_ts;

-- Row-level security for data isolation
CREATE TENANT POLICY tenant_isolation
  AS (tenant_id = SYS_CONTEXT('USERENV', 'CLIENT_IDENTIFIER'));

ALTER TABLE orders ADD (tenant_id VARCHAR2(50));
```

### Option C: Autonomous Database per Tenant
```bash
# Terraform for tenant provisioning
resource "oci_database_autonomous_database" "tenant" {
  count = var.tenant_count
  
  db_name = "tenant${count.index + 1}"
  db_workload = "OLTP"
  cpu_core_count = 1
  data_storage_size_in_tbs = 1
  
  is_auto_scaling_enabled = true
}
```

## Scenario 3: Real-Time Analytics Pipeline

**Context**: E-commerce platform needs real-time sales analytics.

**Architecture**:
```
Application → ATP (Transactions)
     ↓ GoldenGate
MySQL HeatWave → Real-time Analytics
     ↓
Oracle Analytics Cloud (Dashboards)
```

**Implementation**:
```sql
-- ATP source: Transactional table
CREATE TABLE sales_transactions (
  transaction_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  product_id NUMBER NOT NULL,
  customer_id NUMBER NOT NULL,
  quantity NUMBER,
  amount NUMBER(10,2),
  transaction_time TIMESTAMP DEFAULT SYSTIMESTAMP
);

-- GoldenGate extract configuration
EXTRACT ext_sales
USERIDALIAS ggs_admin DOMAIN OracleGoldenGate
EXTTRAIL ./dirdat/st
TABLE app.sales_transactions;

-- HeatWave target: Analytics-optimized
CREATE TABLE sales_analytics (
  transaction_id NUMBER,
  product_id NUMBER,
  customer_id NUMBER,
  amount NUMBER(10,2),
  transaction_date DATE,
  region VARCHAR2(50)
) ENGINE = HeatWave;
```

## Scenario 4: Microservices with Saga Pattern

**Context**: Order processing across 3 microservices (Order, Inventory, Payment).

**Implementation**:
```sql
-- Oracle Database 23ai Saga support
BEGIN
  DBMS_SAGA.CREATE_SAGA(
    saga_name => 'ORDER_PROCESSING',
    saga_comment => 'Distributed order processing'
  );
  
  DBMS_SAGA.ADD_SAGA_STEP(
    saga_name => 'ORDER_PROCESSING',
    step_name => 'CREATE_ORDER',
    package_name => 'ORDER_PKG',
    procedure_name => 'CREATE_ORDER',
    compensation_package => 'ORDER_PKG',
    compensation_procedure => 'CANCEL_ORDER'
  );
  
  DBMS_SAGA.ADD_SAGA_STEP(
    saga_name => 'ORDER_PROCESSING',
    step_name => 'RESERVE_INVENTORY',
    package_name => 'INVENTORY_PKG',
    procedure_name => 'RESERVE',
    compensation_package => 'INVENTORY_PKG',
    compensation_procedure => 'RELEASE'
  );
  
  DBMS_SAGA.ADD_SAGA_STEP(
    saga_name => 'ORDER_PROCESSING',
    step_name => 'PROCESS_PAYMENT',
    package_name => 'PAYMENT_PKG',
    procedure_name => 'CHARGE',
    compensation_package => 'PAYMENT_PKG',
    compensation_procedure => 'REFUND'
  );
END;
/

-- Execute saga
DECLARE
  saga_id VARCHAR2(50);
BEGIN
  saga_id := DBMS_SAGA.EXECUTE_SAGA(
    saga_name => 'ORDER_PROCESSING',
    payload => '{"order_id": 12345, "amount": 99.99}'
  );
END;
/
```

## Scenario 5: AI-Powered Customer Support

**Context**: Implement RAG-based customer support using Oracle Database 23ai Vector Search.

**Implementation**:
```sql
-- Create vector table for knowledge base
CREATE TABLE knowledge_vectors (
  doc_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  content CLOB,
  embedding VECTOR(1536)
);

-- Create vector index
CREATE VECTOR INDEX idx_knowledge_embedding
ON knowledge_vectors(embedding)
ORGANIZATION NEIGHBOR PARTITIONS
DISTANCE COSINE;

-- Insert with embeddings (generated externally via LLM)
INSERT INTO knowledge_vectors (content, embedding)
VALUES (
  'How to reset password: Go to settings...',
  VECTOR('[0.1, 0.2, 0.3, ...]')  -- 1536 dimensions
);

-- Similarity search for RAG
SELECT content, 
       VECTOR_DISTANCE(embedding, :query_embedding, COSINE) as similarity
FROM knowledge_vectors
WHERE VECTOR_DISTANCE(embedding, :query_embedding, COSINE) < 0.3
ORDER BY similarity
FETCH FIRST 5 ROWS ONLY;

-- Combined with LLM via OCI Generative AI
SELECT AI.GENERATE(
  prompt => 'Answer this question: ' || :user_question || 
            ' using this context: ' || 
            (SELECT content FROM knowledge_vectors 
             WHERE doc_id = :matched_doc_id),
  provider => 'OCI',
  model => 'cohere.command-r-plus'
) AS response
FROM DUAL;
```
