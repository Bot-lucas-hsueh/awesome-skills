# § 7 · Domain Knowledge Reference

## 7.1 Ontology Design Principles

### The 5 Ws of Object Types

1. **What** is this entity? (Clear business definition)
2. **Who** owns it? (Business owner, technical owner)
3. **Where** does the data come from? (Source systems)
4. **When** is it updated? (Freshness SLAs)
5. **Why** does it exist? (Operational use cases)

### Object Type Design Best Practices

**Naming Conventions:**
- Use PascalCase for Object Type names (e.g., `PurchaseOrder`, `Aircraft`)
- Use camelCase for property names (e.g., `orderNumber`, `tailNumber`)
- Singular names preferred (e.g., `Employee` not `Employees`)

**Property Design:**
```yaml
Property Types:
  - name: primaryIdentifier
    type: string
    primaryKey: true
    description: "Unique identifier from source system"
    
  - name: status
    type: enum
    values: [ACTIVE, INACTIVE, PENDING]
    default: PENDING
    
  - name: createdAt
    type: timestamp
    immutable: true
    
  - name: amount
    type: decimal
    precision: 19
    scale: 4
    validators:
      - type: range
        min: 0
        max: 999999999999.9999
```

### Link Type Design

**Direction Matters:**
```
# Good: Clear semantic direction
Employee.reportsTo → Manager
Manager.manages → Employee

# Good: Symmetric relationships
Person.marriedTo ↔ Person
Organization.partneredWith ↔ Organization
```

**Cardinality:**
- One-to-One: Person ↔ Passport
- One-to-Many: Department → Employee
- Many-to-Many: Student ↔ Course (via Enrollment)

**Temporal Links:**
```yaml
LinkType:
  name: employedAt
  from: Employee
  to: Company
  properties:
    - name: startDate
      type: date
    - name: endDate
      type: date
    - name: isCurrent
      type: boolean
      formula: endDate IS NULL
```

## 7.2 Security Implementation

### Classification Handling

```python
# Classification propagation
@classified
def classify_object(source_objects):
    """
    Classification is inherited from highest classified source
    """
    max_classification = Classification.UNCLASSIFIED
    for obj in source_objects:
        if obj.classification > max_classification:
            max_classification = obj.classification
    return max_classification
```

### Access Control Patterns

**Role-Based Access Control (RBAC):**
```yaml
PermissionModel:
  roles:
    - name: DataAnalyst
      permissions:
        - object: Transaction
          actions: [READ]
          conditions:
            - property: region
              in: user.authorized_regions
              
    - name: DataSteward
      permissions:
        - object: "*"
          actions: [READ, WRITE]
          conditions:
            - classification: "<= user.clearance_level"
```

**Attribute-Based Access Control (ABAC):**
```yaml
Policy:
  name: manager_can_view_team_data
  effect: ALLOW
  principals:
    - role: Manager
  actions:
    - READ
  resources:
    - objectType: Employee
  condition:
    expression: resource.department == principal.department
```

## 7.3 Data Quality Framework

### Quality Dimensions

| Dimension | Metric | Threshold |
|-----------|--------|-----------|
| Completeness | % non-null required fields | > 99% |
| Uniqueness | % duplicate primary keys | 0% |
| Validity | % values in allowed ranges | > 99.5% |
| Timeliness | Age of most recent data | < SLA |
| Consistency | % cross-reference matches | > 99% |

### Great Expectations Integration

```python
# Data quality suite for Ontology objects
expectations = [
    {
        "expectation_type": "expect_column_values_to_not_be_null",
        "kwargs": {"column": "primaryIdentifier"}
    },
    {
        "expectation_type": "expect_column_values_to_be_unique",
        "kwargs": {"column": "primaryIdentifier"}
    },
    {
        "expectation_type": "expect_column_values_to_be_between",
        "kwargs": {
            "column": "amount",
            "min_value": 0,
            "max_value": 1000000000
        }
    }
]
```

## 7.4 AIP Prompt Engineering

### System Prompt Template

```
You are an AI assistant for {{organization_name}} operating within Palantir Foundry.
You have access to the following Ontology objects:
{{available_object_types}}

Your responses must:
1. Ground all statements in Ontology data
2. Cite specific Object IDs for any claims
3. Respect classification and access controls
4. Flag uncertainty with confidence scores
5. Escalate when human judgment is required

DO NOT:
- Make up data not in the Ontology
- Access objects above user's clearance
- Provide advice that could violate regulations
```

### Context Retrieval Pattern

```python
def get_llm_context(query, user):
    # Retrieve relevant objects
    similar_objects = vector_search(query, ontology_index)
    
    # Filter by permissions
    accessible_objects = [
        obj for obj in similar_objects 
        if user.can_read(obj)
    ]
    
    # Format context
    context = format_for_llm(accessible_objects)
    
    return context
```
