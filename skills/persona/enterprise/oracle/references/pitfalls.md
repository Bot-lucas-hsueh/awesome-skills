# Oracle Anti-Patterns & Pitfalls

> **Common mistakes and how to fix them**

---

## #EP1: Using SELECT * in Production

**Problem:** Causes unnecessary I/O, breaks when schema changes, unstable query plans.

❌ **Wrong:**
```sql
SELECT * FROM employees WHERE department_id = 10;
```

✅ **Right:**
```sql
SELECT employee_id, first_name, last_name, email, hire_date, salary
FROM employees
WHERE department_id = 10;
```

**Why It Matters:**
- Unnecessary I/O for unused columns
- Application breaks when columns are added/removed
- Query plan instability

---

## #EP2: Hardcoding Credentials

**Problem:** Security risk, credential rotation difficulty.

❌ **Wrong:**
```python
conn = cx_Oracle.connect('admin/password123@database')
```

✅ **Right:**
```python
# Use OCI Vault
import oci
import cx_Oracle

# Retrieve secret from OCI Vault
vault_client = oci.vault.VaultsClient(config)
secret_bundle = vault_client.get_secret_bundle(secret_id)
password = base64.b64decode(secret_bundle.data.secret_bundle_content.content)

# Use instance principals for service accounts
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

# Connect with retrieved credentials
conn = cx_Oracle.connect(f'admin/{password}@{database}')
```

**Alternative with Environment Variables:**
```python
import os
import cx_Oracle

username = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
dsn = os.environ.get('DB_DSN')

conn = cx_Oracle.connect(user=username, password=password, dsn=dsn)
```

---

## #EP3: Not Using Bind Variables

**Problem:** Hard parses, SQL injection risk, poor performance.

❌ **Wrong:**
```python
order_id = request.get('order_id')
sql = f"SELECT * FROM orders WHERE order_id = {order_id}"
cursor.execute(sql)
```

✅ **Right:**
```python
order_id = request.get('order_id')
sql = "SELECT * FROM orders WHERE order_id = :order_id"
cursor.execute(sql, {'order_id': order_id})

# Or with positional binds
sql = "SELECT * FROM orders WHERE order_id = :1"
cursor.execute(sql, [order_id])
```

**Impact:**
- Reduces hard parses by 99%+
- Prevents SQL injection
- Enables cursor sharing

---

## #EP4: Ignoring Connection Pooling

**Problem:** Connection overhead, resource exhaustion.

❌ **Wrong:**
```python
def process_order(order_id):
    conn = cx_Oracle.connect('user/pass@db')  # New connection every time
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE order_id = :1", [order_id])
    result = cursor.fetchall()
    conn.close()
    return result
```

✅ **Right:**
```python
import cx_Oracle

# Create pool once at application startup
pool = cx_Oracle.SessionPool(
    user='app_user',
    password='password',
    dsn='database',
    min=5,
    max=20,
    increment=1,
    getmode=cx_Oracle.SPOOL_ATTRVAL_WAIT
)

def process_order(order_id):
    conn = pool.acquire()  # Reuse from pool
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id = :1", [order_id])
        return cursor.fetchall()
    finally:
        pool.release(conn)  # Return to pool
```

**UCP (Universal Connection Pool) Alternative:**
```python
from ucpsql import create_pool

pool = create_pool(
    user='app_user',
    password='password',
    dsn='mydb_medium',
    min_pool_size=10,
    max_pool_size=50,
    connection_wait_timeout=30000
)

with pool.acquire() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE order_id = :1", [order_id])
```

---

## #EP5: Autonomous Database Over-Provisioning

**Problem:** Unnecessary costs.

❌ **Wrong:**
```sql
-- Starting with maximum capacity
CREATE AUTONOMOUS DATABASE
    CPU_CORE_COUNT = 64
    DATA_STORAGE_SIZE_IN_TBS = 128;
```

✅ **Right:**
```bash
# Start small with auto-scaling
oci db autonomous-database create \
    --cpu-core-count 2 \
    --data-storage-size-in-tbs 1 \
    --is-auto-scaling-enabled true

# Monitor actual usage
oci monitoring metric-data summarize-metrics-data \
    --namespace oci_autonomous_database \
    --query "CpuUtilization[1h].mean()"

# Adjust based on actual usage patterns
```

**Auto-Scaling Configuration:**
```sql
-- Set maximum scaling limits
BEGIN
    DBMS_CLOUD_ADMIN.SET_AUTO_SCALING(
        max_cpu_core_count => 8,
        max_storage_tbs => 10
    );
END;
/
```

---

## #EP6: Missing Index Strategy

**Problem:** Poor query performance.

❌ **Wrong:**
```sql
-- No indexes on foreign keys
CREATE TABLE order_items (
    order_item_id NUMBER PRIMARY KEY,
    order_id NUMBER REFERENCES orders(order_id),
    product_id NUMBER REFERENCES products(product_id)
);
```

✅ **Right:**
```sql
CREATE TABLE order_items (
    order_item_id NUMBER PRIMARY KEY,
    order_id NUMBER REFERENCES orders(order_id),
    product_id NUMBER REFERENCES products(product_id)
);

-- Indexes on foreign keys
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_product ON order_items(product_id);

-- Composite index for common query patterns
CREATE INDEX idx_order_items_order_product 
ON order_items(order_id, product_id);

-- Function-based index for case-insensitive search
CREATE INDEX idx_products_name_upper ON products(UPPER(product_name));
```

---

## #EP7: Not Using Retry Logic

**Problem:** Transient failures cause application errors.

❌ **Wrong:**
```python
try:
    cursor.execute(sql)
except cx_Oracle.DatabaseError as e:
    raise  # Immediate failure
```

✅ **Right:**
```python
import time
import random
from functools import wraps

def retry_on_error(max_retries=3, delay=1, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except cx_Oracle.DatabaseError as e:
                    error_obj, = e.args
                    # Retry on connection errors
                    if error_obj.code in (3113, 3114, 12170, 1012):
                        if attempt < max_retries - 1:
                            sleep_time = delay * (backoff ** attempt) + random.uniform(0, 1)
                            time.sleep(sleep_time)
                            continue
                    raise
            return func(*args, **kwargs)
        return wrapper
    return decorator

@retry_on_error(max_retries=3, delay=1, backoff=2)
def execute_critical_query(cursor, sql, params=None):
    cursor.execute(sql, params or {})
```

---

## #EP8: Storing JSON as CLOB Without Validation

**Problem:** Invalid JSON, query difficulties.

❌ **Wrong:**
```sql
CREATE TABLE events (
    event_id NUMBER PRIMARY KEY,
    event_data CLOB  -- No JSON validation
);

INSERT INTO events VALUES (1, '{invalid json}');
```

✅ **Right:**
```sql
-- Oracle 23ai: Native JSON type
CREATE TABLE events (
    event_id NUMBER PRIMARY KEY,
    event_data JSON  -- Native JSON with validation
);

-- With JSON schema validation
CREATE TABLE events (
    event_id NUMBER PRIMARY KEY,
    event_data JSON VALIDATE USING '{
        "type": "object",
        "required": ["name", "timestamp"],
        "properties": {
            "name": {"type": "string"},
            "timestamp": {"type": "string", "format": "date-time"},
            "metadata": {"type": "object"}
        }
    }'
);

-- Query with dot notation
SELECT event_id, e.event_data.name, e.event_data.timestamp
FROM events e
WHERE e.event_data.name = 'user_login';
```

---

## #EP9: Ignoring Cost Management

**Problem:** Unexpected cloud bills.

❌ **Wrong:**
- Not setting budget alerts
- Leaving dev/test resources running 24/7
- Not using BYOL for existing licenses
- Over-provisioning storage

✅ **Right:**
```bash
# Set budget alerts
oci budgets budget create \
    --compartment-id $TENANCY_ID \
    --display-name "Monthly Budget" \
    --amount 10000 \
    --reset-period MONTHLY

# Create budget alert rule
oci budgets alert-rule create \
    --budget-id $BUDGET_ID \
    --display-name "80% Alert" \
    --threshold 80 \
    --threshold-type PERCENTAGE \
    --type ACTUAL

# Schedule resource shutdown
oci resource-scheduler schedule create \
    --compartment-id $COMPARTMENT_ID \
    --display-name "Dev Shutdown" \
    --action STOP \
    --time-zone "America/New_York" \
    --resources file://resources.json
```

**Terraform Cost Controls:**
```hcl
# Auto-shutdown tag
locals {
  shutdown_schedule = var.environment == "prod" ? "" : "0 19 * * *"
}

resource "oci_core_instance" "example" {
  # ...
  
  defined_tags = {
    "Oracle-Tags.Schedule" = local.shutdown_schedule
  }
}
```

---

## #EP10: Inadequate Backup Strategy

**Problem:** Data loss risk.

❌ **Wrong:**
```sql
-- Relying only on Autonomous backups without testing
-- No cross-region backup replication
```

✅ **Right:**
```sql
-- Verify backup configuration
SELECT backup_type, time_started, time_ended, status
FROM v$backup_set_details
ORDER BY time_started DESC
FETCH FIRST 10 ROWS ONLY;

-- Create manual backup before major changes
BEGIN
    DBMS_CLOUD_ADMIN.CREATE_BACKUP(
        backup_name => 'PRE_UPGRADE_BACKUP',
        backup_type => 'FULL'
    );
END;
/

-- Cross-region backup replication (OCI)
oci db autonomous-database create-backup-copy \
    --autonomous-database-id $DB_ID \
    --destination-region us-phoenix-1

-- Automated restore testing
-- (Schedule quarterly restore drills)
```

---

## #EP11: Not Using Application Continuity

**Problem:** Transaction loss on connection failures.

❌ **Wrong:**
```python
# Connection lost = transaction lost
cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
conn.commit()  # Fails if connection dropped
```

✅ **Right:**
```python
# Enable Application Continuity
pool = cx_Oracle.SessionPool(
    user='app_user',
    password='password',
    dsn='database',
    min=5,
    max=20,
    session_callback=init_session
)

def init_session(conn, requested_tag):
    cursor = conn.cursor()
    cursor.execute("ALTER SESSION SET EDITION = ORA$BASE")
    cursor.execute("ALTER SESSION ENABLE DML RETENTION")

# Use TAC (Transparent Application Continuity)
# Connection string with AC enabled
dsn = """
(DESCRIPTION=
    (ADDRESS=(PROTOCOL=TCP)(HOST=scan.example.com)(PORT=1521))
    (CONNECT_DATA=
        (SERVICE_NAME=oltp_svc)
        (FAILOVER_MODE=(TYPE=SELECT)(METHOD=BASIC))
    )
)
"""
```

---

## #EP12: Manual Schema Migrations

**Problem:** No version control, no rollback plan.

❌ **Wrong:**
```sql
-- Running DDL manually in production
ALTER TABLE orders ADD COLUMN priority VARCHAR2(20);
-- (No rollback plan, no version control)
```

✅ **Right:**
```yaml
# liquibase changelog (changelog.xml)
databaseChangeLog:
  - changeSet:
      id: 001-add-order-priority
      author: developer@company.com
      changes:
        - addColumn:
            tableName: orders
            columns:
              - column:
                  name: priority
                  type: VARCHAR2(20)
                  defaultValue: 'NORMAL'
                  constraints:
                    nullable: false
      rollback:
        - dropColumn:
            tableName: orders
            columnName: priority
```

```bash
# Execute with Liquibase
liquibase --changeLogFile=changelog.xml update

# Verify status
liquibase --changeLogFile=changelog.xml status

# Rollback if needed
liquibase --changeLogFile=changelog.xml rollbackCount 1
```

**Flyway Alternative:**
```sql
-- V1__initial_schema.sql
CREATE TABLE orders (
    order_id NUMBER PRIMARY KEY,
    customer_id NUMBER,
    order_date DATE
);

-- V2__add_priority.sql
ALTER TABLE orders ADD COLUMN priority VARCHAR2(20) DEFAULT 'NORMAL';
```

---

## #EP13: Not Monitoring Autonomous Database

**Problem:** Miss performance issues, runaway costs.

❌ **Wrong:**
- No performance monitoring
- No cost alerts
- No query analysis

✅ **Right:**
```sql
-- Monitor storage usage
SELECT storage_used_gb, storage_limit_gb,
       ROUND(storage_used_gb / storage_limit_gb * 100, 2) as pct_used
FROM v$autonomous_database_details;

-- Monitor top SQL
SELECT sql_id,
       ROUND(elapsed_time/executions/1000000, 3) as avg_seconds,
       executions,
       sql_text
FROM v$sql
WHERE executions > 100
ORDER BY elapsed_time DESC
FETCH FIRST 10 ROWS ONLY;

-- Monitor CPU utilization
SELECT timestamp, cpu_consumed_time_us,
       cpu_utilization_percent
FROM v$autonomous_database_time_series
WHERE timestamp > SYSTIMESTAMP - INTERVAL '1' HOUR
ORDER BY timestamp;
```

```bash
# OCI CLI monitoring
oci monitoring metric-data summarize-metrics-data \
    --namespace oci_autonomous_database \
    --query "StorageUtilization[1h].mean()"

# Set up alarms
oci monitoring alarm create \
    --display-name "High Storage Alert" \
    --metric-compartment-id $COMPARTMENT_ID \
    --namespace oci_autonomous_database \
    --query "StorageUtilization[5m].mean() > 80" \
    --destinations '["'$TOPIC_OCID'"]'
```

---

## #EP14: Using AI Vector Search Incorrectly

**Problem:** Poor search accuracy, performance issues.

❌ **Wrong:**
```sql
-- No vector index for similarity search
SELECT content
FROM documents
WHERE VECTOR_DISTANCE(embedding, :query, COSINE) < 0.5
ORDER BY VECTOR_DISTANCE(embedding, :query, COSINE)
FETCH FIRST 10 ROWS ONLY;
```

✅ **Right:**
```sql
-- Create vector index
CREATE VECTOR INDEX idx_doc_embedding
ON documents(embedding)
ORGANIZATION NEIGHBOR PARTITIONS
DISTANCE COSINE
WITH TARGET ACCURACY 95;

-- Use approximate search for large datasets
SELECT content,
       VECTOR_DISTANCE(embedding, :query, COSINE, {'epsilon': 0.1}) as distance
FROM documents
ORDER BY distance
FETCH FIRST 10 ROWS ONLY;

-- Combine with business filters for efficiency
SELECT content, category,
       VECTOR_DISTANCE(embedding, :query, COSINE) as distance
FROM documents
WHERE category = 'TECHNICAL'  -- Filter before vector search
ORDER BY distance
FETCH FIRST 10 ROWS ONLY;
```

---

## Summary Checklist

Before deploying Oracle solutions:

```markdown
□ Using explicit column lists (no SELECT *)
□ Credentials externalized (Vault or environment variables)
□ Bind variables used for all dynamic values
□ Connection pooling implemented
□ Auto-scaling enabled with limits
□ Foreign key indexes created
□ Retry logic for transient failures
□ Native JSON type for JSON data (23ai)
□ Budget alerts configured
□ Backup strategy tested
□ Application Continuity enabled
□ Schema migrations version controlled
□ Monitoring and alerting configured
□ Vector indexes created for similarity search
```

---

*Reference Version: 5.0.0 | Updated: 2026-03-21*
