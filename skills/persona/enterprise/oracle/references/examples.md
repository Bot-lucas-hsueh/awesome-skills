## §5 · Examples

### §5.1 · AI Vector Search for RAG

**Context:** Build a RAG-based customer support system using Oracle Database 23ai.

**Solution:**

```sql
-- Step 1: Create vector table for knowledge base
CREATE TABLE knowledge_vectors (
    doc_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    content CLOB NOT NULL,
    embedding VECTOR(1536, FLOAT32),
    category VARCHAR2(50),
    created_at TIMESTAMP DEFAULT SYSTIMESTAMP
);

-- Step 2: Create vector index
CREATE VECTOR INDEX idx_knowledge_embedding
ON knowledge_vectors(embedding)
ORGANIZATION NEIGHBOR PARTITIONS
DISTANCE COSINE
WITH TARGET ACCURACY 95;

-- Step 3: Insert with embeddings (generated via OCI Generative AI)
INSERT INTO knowledge_vectors (content, embedding)
VALUES (
    'How to reset your Oracle Cloud password: Navigate to Identity → Users → ...',
    VECTOR('[0.023, -0.156, 0.892, ...]')  -- 1536 dimensions from embedding model
);

-- Step 4: Similarity search for RAG
WITH relevant_docs AS (
    SELECT content,
           VECTOR_DISTANCE(embedding, :query_embedding, COSINE) as similarity
    FROM knowledge_vectors
    WHERE VECTOR_DISTANCE(embedding, :query_embedding, COSINE) < 0.3
    ORDER BY similarity
    FETCH FIRST 5 ROWS ONLY
)
SELECT * FROM relevant_docs;

-- Step 5: Combined with LLM via OCI Generative AI
SELECT AI.GENERATE(
    prompt => 'Answer this customer question: ' || :user_question ||
              ' using this context: ' ||
              (SELECT content FROM knowledge_vectors
               WHERE doc_id = :matched_doc_id),
    provider => 'OCI',
    model => 'cohere.command-r-plus'
) AS ai_response
FROM DUAL;
```

**Expected Output:**
```json
{
  "query": "How do I reset my cloud password?",
  "retrieved_documents": [
    {
      "content": "How to reset your Oracle Cloud password: Navigate to Identity...",
      "similarity": 0.92
    }
  ],
  "ai_response": "To reset your Oracle Cloud password, navigate to Identity → Users..."
}
```

---

### §5.2 · Database Performance Optimization

**Context:** E-commerce platform experiencing slow queries during peak traffic.

**Oracle-Engineer Approach:**

**Phase 1: Diagnostic Assessment**
```sql
-- Identify top SQL by elapsed time
SELECT sql_id,
       SUBSTR(sql_text, 1, 100) as sql_preview,
       ROUND(elapsed_time/executions/1000000, 3) as avg_seconds,
       executions
FROM v$sql
WHERE executions > 100
  AND elapsed_time > 1000000
ORDER BY elapsed_time DESC
FETCH FIRST 10 ROWS ONLY;

-- Check execution plan for problem query
EXPLAIN PLAN FOR
SELECT o.order_id, c.customer_name, p.product_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE o.order_date > SYSDATE - 30;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);
```

**Phase 2: Autonomous Database Optimization**
```sql
-- Enable Automatic Indexing (Autonomous)
BEGIN
    DBMS_AUTO_INDEX.CONFIGURE('AUTO_INDEX_MODE', 'IMPLEMENT');
END;
/

-- Review recommended indexes after 24 hours
SELECT index_name, table_name, index_type, auto_index_config
FROM dba_auto_indexes
WHERE status = 'VALID'
ORDER BY last_analyzed DESC;
```

**Phase 3: Manual Optimization**
```sql
-- Create composite index based on query pattern
CREATE INDEX idx_orders_cust_date ON orders(customer_id, order_date)
COMPUTE STATISTICS;

-- Gather optimizer statistics
EXEC DBMS_STATS.GATHER_TABLE_STATS('SCHEMA_NAME', 'ORDERS',
    estimate_percent => DBMS_STATS.AUTO_SAMPLE_SIZE,
    method_opt => 'FOR ALL COLUMNS SIZE AUTO',
    cascade => TRUE);

-- Create SQL Profile for complex queries
DECLARE
    sql_tune_task VARCHAR2(100);
BEGIN
    sql_tune_task := DBMS_SQLTUNE.CREATE_TUNING_TASK(
        sql_id => 'a1b2c3d4e5f6',
        scope => DBMS_SQLTUNE.SCOPE_COMPREHENSIVE,
        time_limit => 3600,
        task_name => 'tune_slow_query'
    );
    DBMS_SQLTUNE.EXECUTE_TUNING_TASK(sql_tune_task);
END;
/
```

**Phase 4: Application Connection Pooling**
```python
# Oracle Universal Connection Pool (UCP)
from ucpsql import create_pool

pool = create_pool(
    user='app_user',
    password='secure_password',
    dsn='mydb_medium',
    min_pool_size=10,
    max_pool_size=50,
    connection_wait_timeout=30000,
    validate_connection_on_borrow=True
)

# Batch processing for bulk operations
with pool.acquire() as conn:
    cursor = conn.cursor()
    cursor.executemany(
        """INSERT INTO order_items (order_id, product_id, qty)
           VALUES (:1, :2, :3)""",
        batch_data  # List of tuples
    )
    conn.commit()
```

**Outcome:** Query time reduced from 2.5s to 45ms; CPU utilization down 40%.

---

### §5.3 · Zero Downtime Migration to OCI

**Context:** Migrate 50TB on-premises Oracle Database to OCI with <1 hour downtime.

**Oracle-Engineer Approach:**

**Phase 1: Strategy Selection**
```yaml
Decision Matrix:
    Downtime Tolerance: <1 hour
    Database Size: 50TB
    Version: 19c on-premises
    Target: Autonomous Dedicated
    
Selected Approach: ZDM (Zero Downtime Migration)
    - Logical migration using Data Pump + GoldenGate
    - Rollback capability maintained
    - Near-zero production impact
```

**Phase 2: Infrastructure Preparation**
```hcl
# Terraform for OCI target infrastructure
resource "oci_database_autonomous_database" "target_db" {
    compartment_id       = var.compartment_id
    db_name              = "PRODDBMIG"
    display_name         = "Production DB Migration"
    db_workload          = "OLTP"
    db_version           = "19c"
    license_model        = "BRING_YOUR_OWN_LICENSE"
    
    # Exadata infrastructure for performance parity
    autonomous_database_infrastructure_type = "DEDICATED"
    
    # Auto-scaling configuration
    cpu_core_count           = 16
    data_storage_size_in_tbs = 100
    is_auto_scaling_enabled  = true
    
    # Backup configuration
    backup_retention_period_in_days = 60
}
```

**Phase 3: Migration Execution**
```bash
# ZDM migration workflow - Evaluation
zdmcli migrate database \
    -sourcedb onprem-db.company.com:1521/PRODDB \
    -sourcenode onprem-db.company.com \
    -targetnode adb-target.oraclecloud.com \
    -backupuser MIGRATION_USER \
    -rspfile ./migration.rsp \
    -eval

# Execute actual migration (after eval success)
zdmcli migrate database \
    -jobid previous_eval_job_id \
    -execute
```

**Phase 4: Cutover and Validation**
```sql
-- Post-migration validation
SELECT 'Row Count Check' as validation,
       table_name,
       COUNT(*) as row_count
FROM user_tables
WHERE table_name IN ('ORDERS', 'CUSTOMERS', 'PRODUCTS')
GROUP BY table_name;

-- Performance baseline comparison
SELECT sql_id,
       plan_hash_value,
       executions,
       ROUND(elapsed_time/executions/1000, 2) as avg_ms
FROM v$sql
WHERE sql_text LIKE '%orders%'
ORDER BY elapsed_time DESC
FETCH FIRST 10 ROWS ONLY;
```

**Outcome:** Migration completed with 15 minutes downtime; query performance improved 35%.

---

### §5.4 · Multi-Cloud Database Deployment

**Context:** Deploy Oracle Database across AWS and OCI for disaster recovery.

**Oracle-Engineer Architecture:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    AWS us-east-1                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Oracle Database@AWS                        │   │
│  │           (Exadata infrastructure)                      │   │
│  │                    PRIMARY                              │   │
│  └─────────────────────────────────────────────────────────┘   │
└───────────────────────────┬─────────────────────────────────────┘
                            │ FastConnect + Direct Connect
                            │ (Encrypted, <5ms latency)
┌───────────────────────────┼─────────────────────────────────────┐
│                    OCI us-ashburn-1                             │
│  ┌────────────────────────┴────────────────────────────────┐   │
│  │              Oracle Cloud Infrastructure                 │   │
│  │          Autonomous Database Dedicated                   │   │
│  │                   STANDBY / DR                           │   │
│  │                                                          │   │
│  │  • Real-time replication via GoldenGate                 │   │
│  │  • Automatic failover (planned/unplanned)               │   │
│  │  • Read-only reporting during normal operation          │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

**Implementation:**

```sql
-- GoldenGate Extract (on AWS source)
EXTRACT ext1
USERIDALIAS ggs_admin DOMAIN OracleGoldenGate
EXTTRAIL ./dirdat/et
TABLE schema.*;

-- GoldenGate Replicat (on OCI target)
REPLICAT rep1
USERIDALIAS ggs_admin DOMAIN OracleGoldenGate
MAP schema.*, TARGET schema.*;

-- Monitor replication lag
SELECT name, value, unit, time_computed
FROM v$dataguard_stats
WHERE name IN ('transport lag', 'apply lag', 'apply finish time');
```

```python
# OCI Function for automated failover
import oci
import json

def failover_handler(event, context):
    """Handle database failover from AWS to OCI"""
    
    database_client = oci.database.DatabaseClient({})
    
    # Check primary database health
    health_check = check_primary_health()
    
    if not health_check['healthy']:
        # Promote OCI standby to primary
        response = database_client.switchover_autonomous_database(
            autonomous_database_id="ocid1.autonomousdatabase.oc1..xxx",
            switchover_autonomous_database_details={
                "databaseAdminPassword": get_secret("db_admin_password")
            }
        )
        
        # Update DNS records
        update_dns_records(new_primary="oci")
        
        # Notify operations team
        send_alert("Database failover completed", severity="CRITICAL")
    
    return {"status": "success"}
```

**Outcome:** RTO <5 minutes, RPO <30 seconds, seamless cross-cloud operation.

---

### §5.5 · JSON Relational Duality Views

**Context:** Modern application needs JSON document access with relational consistency.

**Oracle 23ai Solution:**

```sql
-- Relational schema (normalized storage)
CREATE TABLE departments (
    deptno NUMBER PRIMARY KEY,
    dname VARCHAR2(50),
    location VARCHAR2(50)
);

CREATE TABLE employees (
    empno NUMBER PRIMARY KEY,
    ename VARCHAR2(50),
    job VARCHAR2(50),
    salary NUMBER,
    deptno NUMBER REFERENCES departments(deptno)
);

-- JSON Relational Duality View
CREATE JSON RELATIONAL DUALITY VIEW dept_emp_view AS
SELECT JSON {
    'department_id' : d.deptno,
    'department_name' : d.dname,
    'location' : d.location,
    'employees' : [
        SELECT JSON {
            'employee_id' : e.empno,
            'name' : e.ename,
            'job_title' : e.job,
            'salary' : e.salary
        }
        FROM employees e
        WHERE e.deptno = d.deptno
    ]
}
FROM departments d
WITH INSERT UPDATE DELETE;

-- Application GET (JSON document)
SELECT JSON_SERIALIZE(data FORMAT JSON)
FROM dept_emp_view
WHERE JSON_VALUE(data, '$.department_id') = 10;

-- Application PUT (updates underlying tables)
UPDATE dept_emp_view
SET data = JSON {
    'department_id' : 10,
    'department_name' : 'ACCOUNTING',
    'employees' : [
        {'employee_id' : 7782, 'name' : 'CLARK', 'job_title' : 'MANAGER', 'salary' : 2450}
    ]
}
WHERE JSON_VALUE(data, '$.department_id') = 10;

-- Value-based concurrency control (optimistic locking)
-- Uses ETAGs to prevent lost updates
SELECT JSON_SERIALIZE(data RETURNING CLOB) as doc,
       ORA_ROWSCN as etag
FROM dept_emp_view
WHERE JSON_VALUE(data, '$.department_id') = 10;
```

**Benefits:**
- Single data store, dual access patterns
- No ETL, no duplication, no consistency issues
- ACID transactions across both access patterns
- Lock-free concurrency control

---
