# CMDB & CSDM Guide

## Configuration Management Database (CMDB)

### Overview
The CMDB is ServiceNow's central repository for IT assets (Configuration Items).

### CI Classes Hierarchy
```
cmdb_ci
├── cmdb_ci_hardware
│   ├── cmdb_ci_computer
│   │   ├── cmdb_ci_server
│   │   ├── cmdb_ci_desktop
│   │   └── cmdb_ci_laptop
│   └── cmdb_ci_network_adapter
├── cmdb_ci_service
│   ├── cmdb_ci_appl
│   ├── cmdb_ci_database
│   └── cmdb_ci_web_site
├── cmdb_ci_cloud
│   ├── cmdb_ci_cloud_instance
│   └── cmdb_ci_cloud_container
└── cmdb_ci_virtualization
    └── cmdb_ci_vm_instance
```

### Key Fields
| Field | Purpose |
|-------|---------|
| name | Display name |
| sys_class_name | CI class |
| operational_status | Current state |
| install_status | Installation state |
| asset_tag | Physical tag |
| serial_number | Manufacturer serial |
| model_id | Reference to model |
| owned_by | Business owner |
| supported_by | Support group |

### Relationships
```javascript
// Create relationship
var rel = new GlideRecord('cmdb_rel_ci');
rel.parent = parentSysId;
rel.child = childSysId;
rel.type = 'Depends on::Used by';
rel.insert();

// Query relationships
var rel = new GlideRecord('cmdb_rel_ci');
rel.addQuery('parent', sysId);
rel.addQuery('type', 'CONTAINS', 'Depends on');
rel.query();
```

## Common Services Data Model (CSDM)

### Overview
CSDM is ServiceNow's standardized data model for IT services.

### Four Domains

#### 1. Foundation Data
- Users, Groups, Locations
- Standard data shared across all domains

#### 2. Design Data
- **Technical Services:** Applications, infrastructure
- **Application Services:** Business applications
- **Infrastructure Services:** Servers, network, storage
- **Cloud Services:** AWS, Azure, GCP resources

#### 3. Actual Data
- Discovered CIs from Discovery/Service Mapping
- Operational state of services

#### 4. Requirement Data
- Business Services
- Business Processes
- Service Offerings
- SLAs

### Service Model
```
Business Service
└── Application Service
    ├── Application
    │   ├── Application Component
    │   └── Database
    ├── Server
    │   ├── Virtual Server
    │   └── Physical Server
    └── Network
        ├── Load Balancer
        └── Firewall
```

## Service Mapping

### Top-Down Approach
1. Define business service
2. Identify entry points
3. Discover connections
4. Build dependency map

### Bottom-Up Approach
1. Start with infrastructure
2. Map to applications
3. Identify business services
4. Validate with stakeholders

### Discovery
```yaml
Discovery Methods:
  - SNMP: Network devices
  - SSH: Unix/Linux servers
  - WMI: Windows servers
  - REST APIs: Cloud resources
  - Agent-based: Detailed application data
```

## Best Practices

### Data Quality
```yaml
Required:
  - Name is unique and descriptive
  - Class is appropriate
  - Status is current
  - Owner is assigned

Recommended:
  - Asset tag populated
  - Model reference set
  - Relationships defined
  - Discovery data current
```

### Health Dashboard
Monitor these metrics:
- Duplicate CIs
- Orphaned CIs (no relationships)
- Stale CIs (not updated in 90 days)
- Required fields missing

### Reconciliation
```javascript
// Identify duplicates
var ga = new GlideAggregate('cmdb_ci');
ga.groupBy('serial_number');
ga.addHaving('COUNT', '>', 1);
ga.query();

while (ga.next()) {
    gs.info('Duplicate serial: ' + ga.serial_number);
}
```
