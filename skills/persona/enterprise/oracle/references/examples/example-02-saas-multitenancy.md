# Example 2: SaaS Multi-Tenancy Architecture

## Context

Cloud SaaS provider serving 1,000+ enterprise customers with strict data isolation
requirements and varying performance needs.

## Architecture Decision Matrix

| Option | Isolation Level | Cost Efficiency | Management Complexity | Best For |
|--------|----------------|-----------------|----------------------|----------|
| **PDB per Tenant** | High | Medium | Medium | 100-500 tenants |
| **Schema per Tenant** | Medium | High | Low | <100 tenants |
| **ADB per Tenant** | Maximum | Low | High | Enterprise customers |
| **Hybrid** | Flexible | Optimized | Medium | Mixed requirements |

## Recommended Solution: Hybrid Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SaaS Multi-Tenancy Architecture                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              Enterprise Tier (100 tenants)                   │   │
│  │    ┌──────────┐  ┌──────────┐  ┌──────────┐                │   │
│  │    │  ADB-1   │  │  ADB-2   │  │  ADB-N   │  (Dedicated)  │   │
│  │    │Tenant 001│  │Tenant 002│  │Tenant 100│                │   │
│  │    └──────────┘  └──────────┘  └──────────┘                │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              Business Tier (400 tenants)                     │   │
│  │         ┌─────────────────────────────────────┐              │   │
│  │         │     Container Database (CDB)        │              │   │
│  │         │  ┌────────┐ ┌────────┐ ┌────────┐  │              │   │
│  │         │  │ PDB-1  │ │ PDB-2  │ │ PDB-N  │  │ (Pluggable)  │   │
│  │         │  │Tenant  │ │Tenant  │ │Tenant  │  │              │   │
│  │         │  │  101   │ │  102   │ │  500   │  │              │   │
│  │         │  └────────┘ └────────┘ └────────┘  │              │   │
│  │         └─────────────────────────────────────┘              │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              Standard Tier (500 tenants)                     │   │
│  │         ┌─────────────────────────────────────┐              │   │
│  │         │    Shared Schema Multi-Tenancy      │              │   │
│  │         │  (Row-level security per tenant)    │              │   │
│  │         └─────────────────────────────────────┘              │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Implementation

### Enterprise Tier: Autonomous Database per Tenant

```hcl
# Terraform for tenant provisioning
variable "tenant_configs" {
  type = map(object({
    tier = string
    cpu_min = number
    cpu_max = number
    storage_tb = number
  }))
  
  default = {
    "tenant_001" = { tier = "enterprise", cpu_min = 4, cpu_max = 16, storage_tb = 10 }
    "tenant_002" = { tier = "enterprise", cpu_min = 2, cpu_max = 8, storage_tb = 5 }
  }
}

# Create Autonomous Database per enterprise tenant
resource "oci_database_autonomous_database" "enterprise_tenant" {
  for_each = var.tenant_configs
  
  compartment_id              = var.compartment_id
  db_name                     = upper(substr(each.key, 0, 8))
  display_name                = "SaaS-${each.key}"
  db_workload                 = "OLTP"
  db_version                  = "19c"
  license_model               = "BRING_YOUR_OWN_LICENSE"
  
  # Isolated infrastructure
  autonomous_database_infrastructure_type = "DEDICATED"
  
  # Auto-scaling configuration
  cpu_core_count              = each.value.cpu_min
  data_storage_size_in_tbs    = each.value.storage_tb
  is_auto_scaling_enabled     = true
  
  # Backup and security
  backup_retention_period_in_days = 60
  is_data_guard_required      = true
  
  # Tags for cost allocation
  defined_tags = {
    "SaaS.TenantID" = each.key
    "SaaS.Tier"     = each.value.tier
  }
}
```

### Business Tier: Pluggable Database per Tenant

```sql
-- Container Database setup
CREATE PLUGGABLE DATABASE tenant_101
    ADMIN USER tenant_admin IDENTIFIED BY password
    FILE_NAME_CONVERT = ('/pdbseed/', '/tenant_101/')
    STORAGE (MAXSIZE 100G MAX_SHARED_TEMP_SIZE 20G);

ALTER PLUGGABLE DATABASE tenant_101 OPEN;

-- Configure resource limits per PDB
ALTER SESSION SET CONTAINER = tenant_101;
ALTER SYSTEM SET cpu_min_count = 2;
ALTER SYSTEM SET cpu_count = 8;
ALTER SYSTEM SET sga_target = 4G;
ALTER SYSTEM SET pga_aggregate_limit = 2G;

-- Create tenant schema
CREATE USER app_schema IDENTIFIED BY password
    DEFAULT TABLESPACE users
    QUOTA UNLIMITED ON users;

GRANT CREATE SESSION, CREATE TABLE, CREATE SEQUENCE,
    CREATE TRIGGER, CREATE PROCEDURE, CREATE VIEW
TO app_schema;
```

**Automated PDB Provisioning:**

```python
import cx_Oracle

def provision_pdb_tenant(tenant_id, config):
    """Provision new PDB for tenant"""
    
    conn = cx_Oracle.connect("sys/password@cdb as sysdba")
    cursor = conn.cursor()
    
    # Create PDB
    cursor.execute(f"""
        CREATE PLUGGABLE DATABASE tenant_{tenant_id}
            ADMIN USER tenant_admin IDENTIFIED BY {config['admin_password']}
            FILE_NAME_CONVERT = ('/pdbseed/', '/tenant_{tenant_id}/')
            STORAGE (MAXSIZE {config['max_storage']}G)
    """)
    
    # Open PDB
    cursor.execute(f"ALTER PLUGGABLE DATABASE tenant_{tenant_id} OPEN")
    
    # Save state
    cursor.execute(f"""
        ALTER PLUGGABLE DATABASE tenant_{tenant_id}
        SAVE STATE INSTANCES = ALL
    """)
    
    # Switch to PDB context
    cursor.execute(f"ALTER SESSION SET CONTAINER = tenant_{tenant_id}")
    
    # Set resource limits
    cursor.execute(f"ALTER SYSTEM SET cpu_min_count = {config['cpu_min']}")
    cursor.execute(f"ALTER SYSTEM SET cpu_count = {config['cpu_max']}")
    
    # Create application schema
    cursor.execute(f"""
        CREATE USER {config['schema_name']} IDENTIFIED BY {config['schema_password']}
        DEFAULT TABLESPACE users
        QUOTA UNLIMITED ON users
    """)
    
    # Grant privileges
    cursor.execute(f"GRANT DB_DEVELOPER_ROLE TO {config['schema_name']}")
    
    conn.commit()
    return f"tenant_{tenant_id}"
```

### Standard Tier: Schema-Based Multi-Tenancy

```sql
-- Shared schema with row-level security
CREATE TABLE orders (
    order_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    tenant_id VARCHAR2(50) NOT NULL,
    customer_id NUMBER,
    order_date DATE DEFAULT SYSDATE,
    total_amount NUMBER(10,2),
    status VARCHAR2(20)
);

-- Create tenant context
CREATE OR REPLACE CONTEXT tenant_ctx USING tenant_security_pkg;

-- Security package
CREATE OR REPLACE PACKAGE tenant_security_pkg IS
    PROCEDURE set_tenant(p_tenant_id VARCHAR2);
    FUNCTION get_tenant RETURN VARCHAR2;
END;
/

CREATE OR REPLACE PACKAGE BODY tenant_security_pkg IS
    PROCEDURE set_tenant(p_tenant_id VARCHAR2) IS
    BEGIN
        DBMS_SESSION.set_context('tenant_ctx', 'tenant_id', p_tenant_id);
    END;
    
    FUNCTION get_tenant RETURN VARCHAR2 IS
    BEGIN
        RETURN NVL(SYS_CONTEXT('tenant_ctx', 'tenant_id'), 'UNKNOWN');
    END;
END;
/

-- Row-level security policy
CREATE OR REPLACE FUNCTION tenant_rls_predicate(
    p_schema IN VARCHAR2,
    p_table IN VARCHAR2
) RETURN VARCHAR2 IS
BEGIN
    RETURN 'tenant_id = ''' || 
           NVL(SYS_CONTEXT('tenant_ctx', 'tenant_id'), 'NONE') || 
           '''';
END;
/

BEGIN
    DBMS_RLS.add_policy(
        object_schema => 'APP_SCHEMA',
        object_name => 'ORDERS',
        policy_name => 'TENANT_ISOLATION',
        function_schema => 'APP_SCHEMA',
        policy_function => 'tenant_rls_predicate',
        statement_types => 'SELECT,INSERT,UPDATE,DELETE'
    );
END;
/

-- Application sets tenant context on connection
BEGIN
    tenant_security_pkg.set_tenant('TENANT_501');
END;
/

-- Now queries are automatically filtered
SELECT * FROM orders; -- Only sees TENANT_501 data
```

### Cross-Tier Migration

```sql
-- Migrate tenant from Standard to Business tier
BEGIN
    -- Export from schema-based
    DBMS_DATAPUMP.open(
        operation => 'EXPORT',
        job_mode => 'SCHEMA',
        remote_link => NULL,
        job_name => 'MIGRATE_TENANT_501',
        version => 'LATEST'
    );
    
    DBMS_DATAPUMP.add_file(
        handle => job_handle,
        filename => 'tenant_501.dmp',
        directory => 'DATA_PUMP_DIR'
    );
    
    DBMS_DATAPUMP.metadata_filter(
        handle => job_handle,
        name => 'SCHEMA_EXPR',
        value => 'IN (''TENANT_501'')'
    );
    
    DBMS_DATAPUMP.start_job(job_handle);
END;
/

-- Import to PDB
-- Connect to tenant_501 PDB
impdp tenant_admin/password@tenant_501 \
    DIRECTORY=DATA_PUMP_DIR \
    DUMPFILE=tenant_501.dmp \
    SCHEMAS=tenant_501 \
    REMAP_SCHEMA=tenant_501:app_schema
```

## Tenant Metadata Management

```sql
-- Central tenant registry
CREATE TABLE tenant_registry (
    tenant_id VARCHAR2(50) PRIMARY KEY,
    tenant_name VARCHAR2(200) NOT NULL,
    tier VARCHAR2(20) CHECK (tier IN ('enterprise', 'business', 'standard')),
    deployment_type VARCHAR2(20) CHECK (deployment_type IN ('ADB', 'PDB', 'SCHEMA')),
    db_name VARCHAR2(100),
    schema_name VARCHAR2(100),
    created_at TIMESTAMP DEFAULT SYSTIMESTAMP,
    status VARCHAR2(20) DEFAULT 'ACTIVE',
    max_storage_gb NUMBER,
    max_cpu NUMBER,
    max_users NUMBER
);

-- Tenant usage tracking
CREATE TABLE tenant_usage (
    tenant_id VARCHAR2(50),
    snapshot_time TIMESTAMP,
    storage_used_gb NUMBER,
    cpu_utilization_pct NUMBER,
    active_sessions NUMBER,
    query_count NUMBER,
    PRIMARY KEY (tenant_id, snapshot_time)
);
```

## Performance Isolation

```sql
-- Resource plan for multi-tenant CDB
BEGIN
    DBMS_RESOURCE_MANAGER.create_pending_area();
    
    -- Create CDB resource plan
    DBMS_RESOURCE_MANAGER.create_cdb_plan(
        plan => 'SAAS_TENANT_PLAN',
        comment => 'Resource plan for SaaS tenants'
    );
    
    -- Directives for each tenant PDB
    FOR tenant IN (SELECT tenant_id FROM tenant_registry WHERE tier = 'business') LOOP
        DBMS_RESOURCE_MANAGER.create_cdb_profile(
            profile => 'PROFILE_' || tenant.tenant_id,
            description => 'Resource profile for ' || tenant.tenant_id,
            memory_limit => 4, -- 4GB memory limit
            io_mbps_limit => 100 -- 100 MB/s I/O limit
        );
        
        DBMS_RESOURCE_MANAGER.set_cdb_profile_directive(
            plan => 'SAAS_TENANT_PLAN',
            profile => 'PROFILE_' || tenant.tenant_id,
            shares => 100,
            utilization_limit => 80,
            io_mbps_limit => 100
        );
    END LOOP;
    
    DBMS_RESOURCE_MANAGER.submit_pending_area();
END;
/
```

## Key Learnings

1. **Tiered Architecture**: Match isolation level to customer needs and willingness to pay
2. **Automation**: Automate provisioning, monitoring, and migration between tiers
3. **Row-Level Security**: Schema-based multi-tenancy requires careful RLS implementation
4. **Resource Management**: Prevent noisy neighbor problems with CPU/memory/I/O limits
5. **Monitoring**: Track per-tenant usage for billing and capacity planning

---

*Example Version: 5.0.0*
