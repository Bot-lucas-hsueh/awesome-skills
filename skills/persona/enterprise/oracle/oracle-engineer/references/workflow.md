# Oracle Standard Workflows

## Database Migration Workflow

### Phase 1: Assessment (Week 1)
| Step | Action | Output | Validation |
|------|--------|--------|------------|
| 1.1 | Run OCI Migration Advisor | Assessment report | Compatibility score |
| 1.2 | Identify dependencies | Dependency map | No circular refs |
| 1.3 | Size target infrastructure | Sizing document | Performance baseline |
| 1.4 | Create migration plan | Project plan | Timeline approved |

### Phase 2: Preparation (Week 2)
| Step | Action | Output | Validation |
|------|--------|--------|------------|
| 2.1 | Provision OCI infrastructure | Cloud resources | Health checks pass |
| 2.2 | Configure network connectivity | VPN/FastConnect | Latency <10ms |
| 2.3 | Set up GoldenGate replication | Extract/Replicat | Replication lag <1s |
| 2.4 | Validate data types | Type mapping doc | No data loss risk |

### Phase 3: Migration (Week 3)
| Step | Action | Output | Validation |
|------|--------|--------|------------|
| 3.1 | Initial data load | Data Pump export/import | Row counts match |
| 3.2 | Enable replication | Real-time sync | Lag monitoring active |
| 3.3 | Application testing | Test results | 100% test pass |
| 3.4 | Performance tuning | Tuning recommendations | Query times met |

### Phase 4: Cutover (Week 4)
| Step | Action | Output | Validation |
|------|--------|--------|------------|
| 4.1 | Final sync verification | Data checksum match | Zero divergence |
| 4.2 | Application switch | DNS cutover | <5 min downtime |
| 4.3 | Post-migration validation | Validation report | Business sign-off |
| 4.4 | Decommission source | Archive and cleanup | Cost savings verified |

## OCI Application Deployment Workflow

### Pre-Deployment
```bash
# 1. Validate Terraform
terraform validate
terraform plan -out=tfplan

# 2. Security scan
checkov --file main.tf
terraform-compliance -f features -p tfplan

# 3. Cost estimation
oci estimate-cost --terraform-plan tfplan
```

### Deployment
```bash
# 1. Infrastructure deployment
terraform apply tfplan

# 2. Application deployment
kubectl apply -f k8s-manifests/

# 3. Database migration
liquibase update --changelog-file=changelog.xml

# 4. Smoke tests
./scripts/smoke-test.sh
```

### Post-Deployment
```bash
# 1. Health verification
oci compute instance list --compartment-id $COMP_ID
kubectl get pods -n production

# 2. Monitoring setup
oci monitoring alarm create --alarm-config alarm.json

# 3. Backup verification
oci bv backup list --volume-id $VOLUME_ID
```

## Autonomous Database Provisioning Workflow

### Step 1: Requirements Gathering
```yaml
Workload Type: OLTP / Data Warehouse / JSON
Performance Tier: Dedicated / Serverless
Compute: 2-128 ECPUs (auto-scaling Y/N)
Storage: 1-128 TB
Network: Public / Private Endpoint
Backup: 7-60 days retention
```

### Step 2: Creation
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
  --license-model BRING_YOUR_OWN_LICENSE
```

### Step 3: Configuration
```sql
-- Create application schema
CREATE USER app_schema IDENTIFIED BY "SecurePassword123!"
DEFAULT TABLESPACE DATA
QUOTA UNLIMITED ON DATA;

GRANT CREATE SESSION, CREATE TABLE, CREATE SEQUENCE, 
    CREATE TRIGGER, CREATE PROCEDURE TO app_schema;

-- Configure auto-scaling limits
BEGIN
  DBMS_CLOUD_ADMIN.SET_AUTO_SCALING(
    max_cpu_core_count => 8,
    max_storage_tbs => 10
  );
END;
/
```

### Step 4: Monitoring Setup
```bash
# Enable Operations Insights
oci opsi database-insights enable \
  --database-id $ADB_ID \
  --compartment-id $COMPARTMENT_ID

# Configure alerts
oci monitoring alarm create \
  --display-name "High CPU Alert" \
  --metric-compartment-id $COMPARTMENT_ID \
  --namespace oci_autonomous_database \
  --query "CpuUtilization[5m].mean() > 80" \
  --destinations '["$TOPIC_OCID"]'
```
