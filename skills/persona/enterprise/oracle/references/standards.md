# Oracle Standards & Best Practices

> **OCI Well-Architected Framework and coding standards**

---

## OCI Well-Architected Framework

### Operational Excellence

| Best Practice | Implementation | Validation |
|---------------|----------------|------------|
| Infrastructure as Code | Resource Manager, Terraform | Version-controlled templates |
| CI/CD Integration | OCI DevOps service | Automated build/test/deploy |
| Monitoring | Cloud Guard, Logging, Alarms | 24/7 alerting configured |
| Runbooks | Confluence/Wiki | Documented procedures |
| Tagging Strategy | Mandatory tags | Cost allocation, ownership |

**Required Resource Tags:**

```yaml
mandatory_tags:
  - Project: Project identifier
  - Environment: dev|test|staging|prod
  - Owner: Team or individual email
  - CostCenter: Billing charge code
  - DataClassification: public|internal|confidential|restricted
```

### Security Pillar

| Control Layer | Service | Configuration |
|---------------|---------|---------------|
| **Identity** | IAM, Identity Domains | MFA enforced, least privilege |
| **Network** | Security Lists, NSGs, ZPR | Default deny, micro-segmentation |
| **Data** | TDE, Data Safe, Vault | Encryption at rest/transit |
| **Workload** | Cloud Guard, Vulnerability Scanning | Continuous monitoring |
| **Audit** | Audit Service, Data Safe | Immutable logs, 1-year retention |

**Security Checklist:**

```markdown
□ MFA enabled for all users
□ Service accounts use instance principals
□ Network security groups configured
□ ZPR policies applied
□ TDE enabled for all databases
□ Data Safe configured for sensitive data
□ Cloud Guard targets enabled
□ Vulnerability scanning scheduled
□ Bastion service for admin access
□ Secrets stored in OCI Vault
```

### Reliability Pillar

| Component | Target | Implementation |
|-----------|--------|----------------|
| **Compute** | 99.95% | Multi-AD deployment |
| **Database** | 99.995% | Autonomous HA, Data Guard |
| **Storage** | 11 9s durability | Cross-region replication |
| **Application** | 99.9% | Load balancer health checks |

**Backup Strategy:**

```yaml
Autonomous Database:
  Automatic Backups: Enabled
  Retention: 60 days
  Cross-region copy: Enabled

Block Volumes:
  Backup Policy: Daily
  Retention: 30 days
  Cross-region copy: Weekly

Object Storage:
  Replication: Cross-region
  Object Lock: Compliance mode
  Versioning: Enabled
```

### Performance Pillar

| Metric | Target | Tool |
|--------|--------|------|
| **Database Response** | <50ms | Performance Hub |
| **API Latency** | <100ms | APM |
| **Cache Hit Ratio** | >95% | Cloud Monitor |
| **Network Latency** | <10ms | Interconnect |

### Cost Optimization

| Strategy | Implementation | Savings |
|----------|----------------|---------|
| **BYOL** | Bring Your Own License | 30-50% |
| **Reserved Capacity** | 1-year or 3-year commit | 20-40% |
| **Auto-scaling** | Scale down during low usage | Variable |
| **Schedule-based Scaling** | Stop dev/test outside hours | 60-70% |

---

## Database Coding Standards

### SQL Best Practices

**1. Always Use Table Aliases:**
```sql
-- Good
SELECT e.employee_id, e.first_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.hire_date > SYSDATE - 365;

-- Bad
SELECT employee_id, first_name, department_name
FROM employees
JOIN departments ON employees.department_id = departments.department_id
WHERE hire_date > SYSDATE - 365;
```

**2. Explicit Column Lists:**
```sql
-- Good
INSERT INTO employees (employee_id, first_name, last_name, hire_date)
VALUES (1001, 'John', 'Doe', SYSDATE);

-- Bad
INSERT INTO employees
VALUES (1001, 'John', 'Doe', SYSDATE, NULL, NULL, NULL);
```

**3. Use Bind Variables:**
```sql
-- Good (performance + security)
SELECT * FROM orders WHERE order_id = :order_id;

-- Bad (hard parse for each execution, SQL injection risk)
SELECT * FROM orders WHERE order_id = 12345;
```

**4. Explicit Joins:**
```sql
-- Good
SELECT c.customer_name, o.order_date
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date > SYSDATE - 30;

-- Bad (old syntax, less readable)
SELECT c.customer_name, o.order_date
FROM customers c, orders o
WHERE c.customer_id = o.customer_id
  AND o.order_date > SYSDATE - 30;
```

**5. Index Strategy:**
```sql
-- Create indexes on foreign keys
CREATE INDEX idx_orders_customer ON orders(customer_id);

-- Composite indexes for query patterns
CREATE INDEX idx_orders_date_status ON orders(order_date, status);

-- Function-based index for case-insensitive search
CREATE INDEX idx_customers_email_upper ON customers(UPPER(email));

-- Index for JSON queries
CREATE INDEX idx_events_json ON events(json_column) INDEXTYPE IS CTXSYS.CONTEXT;
```

### PL/SQL Standards

**Package Structure:**
```sql
CREATE OR REPLACE PACKAGE order_mgmt IS
    -- Constants
    gc_status_pending   CONSTANT VARCHAR2(20) := 'PENDING';
    gc_status_complete  CONSTANT VARCHAR2(20) := 'COMPLETE';
    gc_status_cancelled CONSTANT VARCHAR2(20) := 'CANCELLED';
    
    -- Types
    TYPE t_order_rec IS RECORD (
        order_id   orders.order_id%TYPE,
        customer_id orders.customer_id%TYPE,
        total      NUMBER
    );
    
    TYPE t_order_table IS TABLE OF t_order_rec;
    
    -- Public procedures/functions
    PROCEDURE create_order(
        p_customer_id IN NUMBER,
        p_items       IN t_item_table,
        p_order_id    OUT NUMBER
    );
    
    FUNCTION get_order_total(
        p_order_id IN NUMBER
    ) RETURN NUMBER;
    
    PROCEDURE cancel_order(
        p_order_id IN NUMBER,
        p_reason   IN VARCHAR2
    );
    
END order_mgmt;
/

CREATE OR REPLACE PACKAGE BODY order_mgmt IS
    -- Private constants
    gc_max_items CONSTANT NUMBER := 100;
    
    -- Private helper functions
    FUNCTION calculate_tax(
        p_amount IN NUMBER
    ) RETURN NUMBER IS
    BEGIN
        RETURN p_amount * 0.08; -- 8% tax
    END;
    
    FUNCTION validate_items(
        p_items IN t_item_table
    ) RETURN BOOLEAN IS
    BEGIN
        RETURN p_items.COUNT > 0 AND p_items.COUNT <= gc_max_items;
    END;
    
    -- Public implementations
    PROCEDURE create_order(
        p_customer_id IN NUMBER,
        p_items       IN t_item_table,
        p_order_id    OUT NUMBER
    ) IS
    BEGIN
        -- Validate inputs
        IF NOT validate_items(p_items) THEN
            RAISE_APPLICATION_ERROR(-20001, 'Invalid number of items');
        END IF;
        
        -- Create order
        INSERT INTO orders (customer_id, status, created_at)
        VALUES (p_customer_id, gc_status_pending, SYSTIMESTAMP)
        RETURNING order_id INTO p_order_id;
        
        -- Add items
        FORALL i IN 1..p_items.COUNT
            INSERT INTO order_items (order_id, product_id, quantity, price)
            VALUES (p_order_id, p_items(i).product_id, p_items(i).quantity, p_items(i).price);
        
        COMMIT;
        
    EXCEPTION
        WHEN OTHERS THEN
            ROLLBACK;
            RAISE_APPLICATION_ERROR(-20002, 'Order creation failed: ' || SQLERRM);
    END;
    
    FUNCTION get_order_total(
        p_order_id IN NUMBER
    ) RETURN NUMBER IS
        v_total NUMBER;
    BEGIN
        SELECT SUM(quantity * price)
        INTO v_total
        FROM order_items
        WHERE order_id = p_order_id;
        
        RETURN NVL(v_total, 0) + calculate_tax(v_total);
    END;
    
    PROCEDURE cancel_order(
        p_order_id IN NUMBER,
        p_reason   IN VARCHAR2
    ) IS
    BEGIN
        UPDATE orders
        SET status = gc_status_cancelled,
            cancellation_reason = p_reason,
            cancelled_at = SYSTIMESTAMP
        WHERE order_id = p_order_id
          AND status = gc_status_pending;
        
        IF SQL%ROWCOUNT = 0 THEN
            RAISE_APPLICATION_ERROR(-20003, 'Order cannot be cancelled');
        END IF;
        
        COMMIT;
    END;
    
END order_mgmt;
/
```

**Error Handling Pattern:**
```sql
CREATE OR REPLACE PROCEDURE transfer_funds(
    p_from_account IN NUMBER,
    p_to_account   IN NUMBER,
    p_amount       IN NUMBER
) IS
    e_insufficient_funds EXCEPTION;
    PRAGMA EXCEPTION_INIT(e_insufficient_funds, -20001);
    
    v_from_balance NUMBER;
BEGIN
    -- Validate amount
    IF p_amount <= 0 THEN
        RAISE_APPLICATION_ERROR(-20002, 'Amount must be positive');
    END IF;
    
    -- Check balance
    SELECT balance INTO v_from_balance
    FROM accounts
    WHERE account_id = p_from_account
    FOR UPDATE;
    
    IF v_from_balance < p_amount THEN
        RAISE_APPLICATION_ERROR(-20001, 'Insufficient funds');
    END IF;
    
    -- Perform transfer
    UPDATE accounts SET balance = balance - p_amount
    WHERE account_id = p_from_account;
    
    UPDATE accounts SET balance = balance + p_amount
    WHERE account_id = p_to_account;
    
    -- Log transaction
    INSERT INTO transaction_log (from_account, to_account, amount, status)
    VALUES (p_from_account, p_to_account, p_amount, 'COMPLETED');
    
    COMMIT;
    
EXCEPTION
    WHEN e_insufficient_funds THEN
        ROLLBACK;
        -- Log failed transaction
        INSERT INTO transaction_log (from_account, to_account, amount, status, error_msg)
        VALUES (p_from_account, p_to_account, p_amount, 'FAILED', 'Insufficient funds');
        COMMIT;
        RAISE;
        
    WHEN OTHERS THEN
        ROLLBACK;
        -- Log error
        INSERT INTO error_log (error_code, error_message, procedure_name)
        VALUES (SQLCODE, SQLERRM, 'transfer_funds');
        COMMIT;
        RAISE_APPLICATION_ERROR(-20099, 'Transfer failed: ' || SQLERRM);
END;
/
```

---

## Naming Conventions

### OCI Resources

| Resource Type | Naming Pattern | Example |
|---------------|----------------|---------|
| Compartment | `{env}-{purpose}` | `prod-database`, `dev-app` |
| VCN | `vcn-{region}-{purpose}` | `vcn-ash-prod` |
| Subnet | `subnet-{region}-{tier}` | `subnet-ash-db` |
| Route Table | `rt-{purpose}` | `rt-prod-public` |
| Security List | `sl-{purpose}-{direction}` | `sl-prod-ingress` |
| NSG | `nsg-{purpose}` | `nsg-db-tier` |
| Compute Instance | `host-{role}-{number}` | `host-db-01` |
| Database | `db-{env}-{name}` | `db-prod-crm` |
| Bucket | `bucket-{purpose}-{env}` | `bucket-backups-prod` |
| Load Balancer | `lb-{purpose}-{env}` | `lb-app-prod` |

### Database Objects

| Object Type | Naming Pattern | Example |
|-------------|----------------|---------|
| Table | `{schema}_{table_name}` | `HR_EMPLOYEES` |
| Index | `IDX_{table}_{columns}` | `IDX_EMP_DEPT_ID` |
| Sequence | `SEQ_{table_name}` | `SEQ_EMPLOYEES` |
| Trigger | `TRG_{table}_{action}` | `TRG_EMP_INS_UPD` |
| Package | `PKG_{functional_area}` | `PKG_HR_MANAGEMENT` |
| Procedure | `P_{action}_{object}` | `P_CALCULATE_SALARY` |
| Function | `F_{action}_{object}` | `F_GET_EMP_NAME` |
| View | `VW_{purpose}` | `VW_EMP_DETAILS` |
| Materialized View | `MV_{purpose}` | `MV_SALES_SUMMARY` |
| Constraint (PK) | `PK_{table}` | `PK_EMPLOYEES` |
| Constraint (FK) | `FK_{table}_{ref_table}` | `FK_EMP_DEPT` |
| Constraint (UK) | `UK_{table}_{columns}` | `UK_EMP_EMAIL` |
| Constraint (CK) | `CK_{table}_{condition}` | `CK_EMP_SALARY` |

---

## Terraform Standards

### Module Structure

```hcl
modules/
├── network/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── README.md
├── compute/
├── database/
└── security/
```

### Resource Naming

```hcl
# Always use descriptive names with environment prefix
resource "oci_core_vcn" "prod_main_vcn" {
  compartment_id = var.compartment_id
  display_name   = "vcn-${var.region}-${var.environment}"
  cidr_block     = var.vcn_cidr
  
  freeform_tags = {
    project     = var.project_name
    environment = var.environment
    owner       = var.owner
  }
}

# Use data sources for existing resources
data "oci_identity_compartment" "target" {
  id = var.compartment_id
}

# Use locals for complex expressions
locals {
  common_tags = {
    project     = var.project_name
    environment = var.environment
    managed_by  = "terraform"
  }
}
```

---

*Reference Version: 5.0.0 | Updated: 2026-03-21*
