# Workday Architecture Reference

## Object Management Services (OMS) Deep Dive

### Core Services Districts

```
┌─────────────────────────────────────────────────────────────────┐
│                    OMS SERVICES LAYOUT                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  DISTRICT 1: TRANSACTION DISTRICT                                │
│  ├── Transaction Service (core CRUD)                            │
│  ├── Workflow Service (business processes)                      │
│  └── Notification Service (alerts, emails)                      │
│                                                                  │
│  DISTRICT 2: REPORTING DISTRICT                                  │
│  ├── Reporting Services (read-only queries)                     │
│  ├── Analytics Service (Prism integration)                      │
│  └── Dashboard Service (real-time metrics)                      │
│                                                                  │
│  DISTRICT 3: SEARCH DISTRICT                                     │
│  ├── Global Search (Elasticsearch)                              │
│  ├── Prompt Service (dropdown values)                           │
│  └── Query Intent Analyzer (ML-based ranking)                   │
│                                                                  │
│  DISTRICT 4: INTEGRATION DISTRICT                                │
│  ├── API Gateway (REST/SOAP)                                    │
│  ├── EIB Engine (bulk data)                                     │
│  └── Studio Runtime (complex integrations)                      │
│                                                                  │
│  DISTRICT 5: CACHE DISTRICT                                      │
│  ├── Apache Ignite Fabric                                       │
│  ├── Index Service                                              │
│  └── Session Management                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### In-Memory Architecture Benefits

| Aspect | Traditional RDBMS | Workday OMS |
|--------|-------------------|-------------|
| Query Latency | 10-100ms (disk I/O) | <1ms (memory) |
| Joins | SQL joins at query time | Pre-wired relationships |
| Scalability | Vertical (bigger servers) | Horizontal (more nodes) |
| Complex Logic | Stored procedures | Native Xpresso methods |
| Data Integrity | Foreign key constraints | Object graph validation |

### Persistence Layer Details

```
Primary Metadata Store (PostgreSQL)
├── Object definitions
├── Security policies
├── Business process configs
└── Audit trails

Document Store (NoSQL)
├── Attachments
├── Reports output
├── Large documents
└── Versioned content

Analytics Warehouse (Prism)
├── Aggregated metrics
├── Historical trends
├── ML training data
└── External data blends
```

## Xpresso Runtime Environment

### Compilation Pipeline

```
Source Xpresso → Parser → AST → Bytecode → JVM Execution
                    ↓
              Metadata Validation
                    ↓
           Dependency Resolution
                    ↓
            Hot Deployment
```

### Transaction Boundaries

```xpresso
// Automatic transaction management
@Transactional
public void promoteEmployee(Employee emp, Position newPos) {
    // All changes within this method are atomic
    emp.position = newPos;
    emp.salary = newPos.salaryRange.midpoint;
    emp.compensationHistory.add(new CompensationChange());
    
    // If any step fails, entire transaction rolls back
    Workflow.create("Promotion Approval")
        .assignTo(newPos.manager)
        .start();
}
```

## Effective Dating Implementation

### Time-Based Data Models

```
Effective Dated Object Structure:
┌─────────────────────────────────────┐
│ Object Instance ID                  │
├─────────────────────────────────────┤
│ Segment 1: 2020-01-01 to 2021-06-30│
│   - Field values for period 1       │
├─────────────────────────────────────┤
│ Segment 2: 2021-07-01 to 2022-12-31│
│   - Field values for period 2       │
├─────────────────────────────────────┤
│ Segment 3: 2023-01-01 to 9999-12-31│
│   - Field values for period 3       │
└─────────────────────────────────────┘
```

### Query Patterns

```xpresso
// Current view (default)
Employee emp = Employee.getCurrent("emp_123");

// Historical snapshot
Employee emp2020 = Employee.asOf("2020-06-01").get("emp_123");

// Future projection
Employee empFuture = Employee.asOf("2025-01-01").get("emp_123");

// Change detection
List<Change> changes = Employee.changesBetween(
    "2020-01-01", 
    "2024-01-01"
).forEmployee("emp_123");
```

## Security Architecture

### Domain Security Model

```
Security Hierarchy:
Domain (e.g., "Worker Data")
  └── Security Policy (e.g., "Manager View")
        └── Role Assignment
              ├── User Group: Managers
              └── Permissions: View, Modify (own team)
```

### Context-Aware Security

```xpresso
// Manager sees only direct reports
@Secured("Worker Data Domain")
public List<Employee> getTeamMembers(Manager mgr) {
    // Automatically filtered by security context
    return mgr.directReports;
}

// HR sees all employees in region
@Secured("Worker Data Domain:HR_View")
public List<Employee> getRegionalEmployees(Region region) {
    return Employee.where(e -> e.region == region);
}
```

## Scalability Patterns

### Horizontal Scaling

```
Tenant Sharding:
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  Tenant A   │  │  Tenant B   │  │  Tenant C   │
│  (Small)    │  │  (Medium)   │  │  (Large)    │
│             │  │             │  │             │
│  1 OMS Node │  │  2 OMS Nodes│  │  10 OMS Nodes│
└─────────────┘  └─────────────┘  └─────────────┘
       │                │                │
       └────────────────┴────────────────┘
                    │
            ┌───────┴───────┐
            │  Load Balancer │
            └───────────────┘
```

### Read Replicas

```
Write Operations → Primary OMS → Persistence
                       ↓
Read Operations → Reporting Services (Replicas)
                       ↓
              Distributed Cache
```
