# Oracle Anti-Patterns & Pitfalls

## #EP1: Using SELECT * in Production

❌ **Wrong**:
```sql
SELECT * FROM employees WHERE department_id = 10;
```

✅ **Right**:
```sql
SELECT employee_id, first_name, last_name, email, hire_date
FROM employees 
WHERE department_id = 10;
```

**Why**: SELECT * causes unnecessary I/O, breaks when schema changes, and makes query plans unstable.

---

## #EP2: Hardcoding Credentials

❌ **Wrong**:
```python
conn = cx_Oracle.connect('admin/password123@database')
```

✅ **Right**:
```python
# Use OCI Vault or environment variables
import oci
from oci.config import from_file

# Retrieve secret from OCI Vault
vault_client = oci.vault.VaultsClient(config)
secret_bundle = vault_client.get_secret_bundle(secret_id)
password = base64.b64decode(secret_bundle.data.secret_bundle_content.content)

conn = cx_Oracle.connect(f'admin/{password}@{database}')
```

---

## #EP3: Not Using Bind Variables

❌ **Wrong**:
```python
sql = f"SELECT * FROM orders WHERE order_id = {order_id}"
cursor.execute(sql)
```

✅ **Right**:
```python
sql = "SELECT * FROM orders WHERE order_id = :order_id"
cursor.execute(sql, {'order_id': order_id})
```

**Why**: Concatenation causes hard parses, SQL injection risk, and poor performance.

---

## #EP4: Ignoring Connection Pooling

❌ **Wrong**:
```python
def process_order(order_id):
    conn = cx_Oracle.connect('user/pass@db')  # New connection every time
    cursor = conn.cursor()
    cursor.execute("...")
    conn.close()
```

✅ **Right**:
```python
# Create pool once at startup
pool = cx_Oracle.SessionPool(
    user='app_user',
    password='password',
    dsn='database',
    min=5,
    max=20,
    increment=1
)

def process_order(order_id):
    conn = pool.acquire()  # Reuse from pool
    try:
        cursor = conn.cursor()
        cursor.execute("...", {'order_id': order_id})
    finally:
        pool.release(conn)  # Return to pool
```

---

## #EP5: Autonomous Database Over-Provisioning

❌ **Wrong**:
```sql
-- Starting with maximum capacity
CREATE AUTONOMOUS DATABASE
  CPU_CORE_COUNT = 64
  DATA_STORAGE_SIZE_IN_TBS = 128;
```

✅ **Right**:
```sql
-- Start small with auto-scaling
CREATE AUTONOMOUS DATABASE
  CPU_CORE_COUNT = 2
  DATA_STORAGE_SIZE_IN_TBS = 1
  IS_AUTO_SCALING_ENABLED = TRUE;

-- Monitor and adjust based on actual usage
```

---

## #EP6: Missing Index Strategy

❌ **Wrong**:
```sql
-- No indexes on foreign keys
CREATE TABLE order_items (
  order_item_id NUMBER PRIMARY KEY,
  order_id NUMBER REFERENCES orders(order_id),
  product_id NUMBER REFERENCES products(product_id)
);
```

✅ **Right**:
```sql
CREATE TABLE order_items (
  order_item_id NUMBER PRIMARY KEY,
  order_id NUMBER REFERENCES orders(order_id),
  product_id NUMBER REFERENCES products(product_id)
);

CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_product ON order_items(product_id);

-- Composite index for common query patterns
CREATE INDEX idx_order_items_order_product 
ON order_items(order_id, product_id);
```

---

## #EP7: Not Using Retry Logic

❌ **Wrong**:
```python
try:
    cursor.execute(sql)
except cx_Oracle.DatabaseError as e:
    raise  # Immediate failure
```

✅ **Right**:
```python
import time
from functools import wraps

def retry_on_error(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except cx_Oracle.DatabaseError as e:
                    error_obj, = e.args
                    if error_obj.code in (3113, 3114, 12170):  # Connection errors
                        if attempt < max_retries - 1:
                            time.sleep(delay * (attempt + 1))
                            continue
                    raise
            return func(*args, **kwargs)
        return wrapper
    return decorator

@retry_on_error(max_retries=3)
def execute_critical_query(cursor, sql):
    cursor.execute(sql)
```

---

## #EP8: Storing JSON as CLOB Without Validation

❌ **Wrong**:
```sql
CREATE TABLE events (
  event_id NUMBER PRIMARY KEY,
  event_data CLOB  -- No JSON validation
);

INSERT INTO events VALUES (1, '{invalid json}');
```

✅ **Right**:
```sql
-- Oracle 23ai: Native JSON type
CREATE TABLE events (
  event_id NUMBER PRIMARY KEY,
  event_data JSON  -- Native JSON with validation
);

-- Or with JSON schema validation
CREATE TABLE events (
  event_id NUMBER PRIMARY KEY,
  event_data JSON VALIDATE USING '{
    "type": "object",
    "properties": {
      "name": {"type": "string"},
      "timestamp": {"type": "string"}
    }
  }'
);
```

---

## #EP9: Ignoring Cost Management

❌ **Wrong**:
- Not setting budget alerts
- Leaving dev/test resources running 24/7
- Not using BYOL for existing licenses
- Over-provisioning storage

✅ **Right**:
```bash
# Set budget alerts
oci budgets budget create \
  --compartment-id $TENANCY_ID \
  --display-name "Monthly Budget" \
  --amount 10000 \
  --reset-period MONTHLY

# Schedule resource shutdown
oci resource-scheduler schedule create \
  --compartment-id $COMPARTMENT_ID \
  --display-name "Dev Shutdown" \
  --action STOP \
  --time-zone "America/New_York" \
  --resources file://resources.json

# Use BYOL for licensing savings
oci db autonomous-database create \
  --license-model BRING_YOUR_OWN_LICENSE \
  ...
```

---

## #EP10: Inadequate Backup Strategy

❌ **Wrong**:
```sql
-- Relying only on Autonomous backups without testing
-- No cross-region backup replication
```

✅ **Right**:
```sql
-- Verify backup configuration
SELECT backup_type, time_started, time_ended, status
FROM v$backup_set_details
ORDER BY time_started DESC;

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

-- Regular restore testing
-- (Schedule quarterly restore drills)
```

---

## #EP11: Not Using Application Continuity

❌ **Wrong**:
```python
# Connection lost = transaction lost
cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
conn.commit()  # Fails if connection dropped
```

✅ **Right**:
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
    # Configure for Application Continuity
    cursor = conn.cursor()
    cursor.execute("ALTER SESSION SET EDITION = ORA$BASE")

# Use TAC (Transparent Application Continuity)
# Or PAC (Planned/Automatic Application Continuity)
```

---

## #EP12: Manual Schema Migrations

❌ **Wrong**:
```sql
-- Running DDL manually in production
ALTER TABLE orders ADD COLUMN priority VARCHAR2(20);
-- (No rollback plan, no version control)
```

✅ **Right**:
```yaml
# liquibase changelog
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

# Rollback if needed
liquibase --changeLogFile=changelog.xml rollbackCount 1
```
