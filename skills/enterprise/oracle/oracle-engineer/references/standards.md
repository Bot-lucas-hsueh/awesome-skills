# Oracle Standards Reference

## OCI Well-Architected Framework

### Operational Excellence
| Best Practice | Implementation | Validation |
|---------------|----------------|------------|
| Infrastructure as Code | Resource Manager, Terraform | Version-controlled templates |
| CI/CD Integration | OCI DevOps service | Automated build/test/deploy |
| Monitoring | Cloud Guard, Logging | 24/7 alerting configured |
| Runbooks | Confluence/Wiki | Documented procedures |

### Security Pillar
| Control Layer | Service | Configuration |
|---------------|---------|---------------|
| Identity | IAM, Identity Domains | MFA enforced, least privilege |
| Network | Security Lists, NSGs, ZPR | Default deny, micro-segmentation |
| Data | TDE, Data Safe, Vault | Encryption at rest/transit |
| Workload | Cloud Guard, Vulnerability Scanning | Continuous monitoring |

### Reliability Pillar
| Component | Target | Implementation |
|-----------|--------|----------------|
| Compute | 99.95% | Multi-AD deployment |
| Database | 99.995% | Autonomous HA |
| Storage | 11 9s durability | Cross-region replication |
| Application | 99.9% | Load balancer health checks |

## Database Coding Standards

### SQL Best Practices
```sql
-- 1. Always use table aliases
SELECT e.employee_id, e.first_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- 2. Explicit column lists (never SELECT *)
INSERT INTO employees (employee_id, first_name, last_name, hire_date)
VALUES (1001, 'John', 'Doe', SYSDATE);

-- 3. Use bind variables for security and performance
SELECT * FROM orders WHERE order_id = :order_id;

-- 4. Proper error handling in PL/SQL
BEGIN
  UPDATE accounts SET balance = balance - :amount WHERE account_id = :from_account;
  UPDATE accounts SET balance = balance + :amount WHERE account_id = :to_account;
  COMMIT;
EXCEPTION
  WHEN OTHERS THEN
    ROLLBACK;
    RAISE_APPLICATION_ERROR(-20001, 'Transfer failed: ' || SQLERRM);
END;
/
```

### PL/SQL Standards
```sql
-- Package structure
CREATE OR REPLACE PACKAGE order_mgmt IS
  -- Constants
  gc_status_pending CONSTANT VARCHAR2(20) := 'PENDING';
  gc_status_complete CONSTANT VARCHAR2(20) := 'COMPLETE';
  
  -- Public procedures/functions
  PROCEDURE create_order(p_customer_id IN NUMBER, p_items IN t_item_table);
  FUNCTION get_order_total(p_order_id IN NUMBER) RETURN NUMBER;
  
END order_mgmt;
/

CREATE OR REPLACE PACKAGE BODY order_mgmt IS
  -- Private helper functions
  FUNCTION calculate_tax(p_amount IN NUMBER) RETURN NUMBER IS
  BEGIN
    RETURN p_amount * 0.08; -- 8% tax
  END;
  
  -- Public implementations
  PROCEDURE create_order(p_customer_id IN NUMBER, p_items IN t_item_table) IS
  BEGIN
    -- Implementation with proper error handling
    NULL;
  END;
  
END order_mgmt;
/
```

## Naming Conventions

### OCI Resources
| Resource Type | Naming Pattern | Example |
|---------------|----------------|---------|
| Compartment | env-purpose | prod-database, dev-app |
| VCN | vcn-region-purpose | vcn-ash-prod |
| Subnet | subnet-region-tier | subnet-ash-db |
| Compute | host-role-number | app-server-01 |
| Database | db-env-name | db-prod-crm |
| Bucket | bucket-purpose-env | backups-prod |

### Database Objects
| Object Type | Naming Pattern | Example |
|-------------|----------------|---------|
| Table | SCHEMA_TABLE_NAME | HR_EMPLOYEES |
| Index | IDX_TABLE_COLUMNS | IDX_EMP_DEPT_ID |
| Sequence | SEQ_TABLE_NAME | SEQ_EMPLOYEES |
| Trigger | TRG_TABLE_ACTION | TRG_EMP_INS_UPD |
| Package | PKG_FUNCTIONAL_AREA | PKG_HR_MANAGEMENT |
