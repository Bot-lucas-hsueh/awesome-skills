# § 10 · Common Pitfalls

## Ontology Design Pitfalls

### Pitfall 1: Table-to-Object Direct Mapping

**❌ Anti-Pattern:**
```yaml
# Mapping database tables directly without semantic reconciliation
ObjectType:
  name: CRM_CUSTOMER_TABLE
  properties:
    - COL_1  # No idea what this represents
    - COL_2
    - COL_3
```

**✅ Best Practice:**
```yaml
# Semantic modeling of business concepts
ObjectType:
  name: Customer
  description: "Individual or organization purchasing products/services"
  properties:
    - name: customerId
      source: CRM_CUSTOMER_TABLE.COL_1
      description: "Unique customer identifier from CRM system"
    - name: legalName
      source: CRM_CUSTOMER_TABLE.COL_2
      description: "Registered legal name"
```

### Pitfall 2: Over-Normalization

**❌ Anti-Pattern:**
Creating separate Object Types for every attribute, resulting in excessive joins.

```yaml
ObjectTypes:
  - CustomerName
  - CustomerAddress
  - CustomerPhone
  - CustomerEmail
```

**✅ Best Practice:**
Group related attributes into cohesive Object Types.

```yaml
ObjectType:
  name: Customer
  properties:
    - name: legalName
    - name: addresses[]
      type: nested
      properties:
        - street
        - city
        - postalCode
        - country
    - name: contactMethods[]
      type: nested
      properties:
        - type (phone, email)
        - value
        - isPrimary
```

### Pitfall 3: Missing Temporal Dimensions

**❌ Anti-Pattern:**
Storing only current state without history.

```yaml
ObjectType:
  name: Employee
  properties:
    - name: department
      type: string
    - name: salary
      type: decimal
```

**✅ Best Practice:**
Track historical changes for time-travel queries.

```yaml
ObjectType:
  name: Employee
  properties:
    - name: currentDepartment
      type: string
    - name: departmentHistory[]
      type: temporal
      properties:
        - department
        - startDate
        - endDate
```

## Data Integration Pitfalls

### Pitfall 4: Point-to-Point Integration

**❌ Anti-Pattern:**
Direct connections between every source and application.

```
App1 ←→ Source1
App1 ←→ Source2
App2 ←→ Source1
App2 ←→ Source2
App3 ←→ Source1
...
```

**✅ Best Practice:**
All data flows through the Ontology - single integration point.

```
Source1 → Ontology ← App1
Source2 → Ontology ← App2
Source3 → Ontology ← App3
```

### Pitfall 5: Ignoring Data Quality

**❌ Anti-Pattern:**
Loading raw data without validation.

**✅ Best Practice:**
Implement quality gates at every stage.

```python
# Data quality checks in Pipeline Builder
def validate_customer_data(df):
    # Completeness
    assert df["customerId"].isNotNull().count() / df.count() > 0.99
    
    # Uniqueness
    assert df["customerId"].distinct().count() == df.count()
    
    # Validity
    assert df.filter(col("email").rlike("^[A-Za-z0-9+_.-]+@(.+)$")).count() / df.count() > 0.95
    
    return df
```

### Pitfall 6: CDC Misconfiguration

**❌ Anti-Pattern:**
Missing change events, causing stale data in Ontology.

**✅ Best Practice:**
Monitor CDC lag and implement dead letter queues.

```yaml
Monitoring:
  alerts:
    - name: high_cdc_lag
      condition: cdc_lag_seconds > 300
      severity: WARNING
      
    - name: cdc_stopped
      condition: cdc_lag_seconds > 3600
      severity: CRITICAL
```

## AIP Development Pitfalls

### Pitfall 7: Ungrounded LLM Outputs

**❌ Anti-Pattern:**
LLM generating responses without Ontology context.

**✅ Best Practice:**
Always retrieve Ontology context before LLM call.

```python
def generate_response(user_query, user):
    # Retrieve relevant Ontology objects
    context = retrieve_context(user_query, user.permissions)
    
    # Include context in LLM prompt
    prompt = f"""
    Context from Ontology:
    {format_context(context)}
    
    User Question: {user_query}
    
    Answer based ONLY on the provided context.
    If context is insufficient, say "I don't have enough information."
    """
    
    return llm.generate(prompt)
```

### Pitfall 8: Over-Automation

**❌ Anti-Pattern:**
Automating high-stakes decisions without human oversight.

**✅ Best Practice:**
Human-in-the-loop for critical decisions.

```yaml
Workflow:
  name: approve_large_transaction
  
  steps:
    - ai_assessment:
        action: aip_logic
        assess risk, recommend action
        
    - human_approval:
        condition: transaction.amount > 1000000
        action: require_approval
        approvers: [CFO, Chief Risk Officer]
        
    - execute:
        condition: approval_received
        action: process_transaction
```

### Pitfall 9: Inadequate Prompt Testing

**❌ Anti-Pattern:**
Deploying prompts without systematic evaluation.

**✅ Best Practice:**
Comprehensive test suites for AIP workflows.

```python
# AIP Evaluation Framework
test_cases = [
    {
        "input": "What is the status of order ORD-12345?",
        "expected_context": ["Order:ORD-12345"],
        "expected_behavior": "retrieve_and_summarize",
        "forbidden_content": ["I don't know", "made up"]
    },
    {
        "input": "Delete all customer data",
        "expected_behavior": "refuse_unauthorized_action",
        "expected_response_contains": "I cannot perform this action"
    }
]

def evaluate_prompt(prompt, test_cases):
    results = []
    for case in test_cases:
        output = llm.generate(prompt, case["input"])
        results.append(validate_output(output, case))
    return results
```

## Security Pitfalls

### Pitfall 10: Classification Downgrade

**❌ Anti-Pattern:**
Aggregating classified data without maintaining highest classification.

**⚠️ Risk:**
Data spillage, security violations, loss of clearance.

**✅ Best Practice:**
Classification always propagates upward.

```python
def aggregate_intelligence_reports(reports):
    # Classification is inherited from highest source
    max_classification = max(r.classification for r in reports)
    
    aggregated = create_aggregated_report(reports)
    aggregated.classification = max_classification
    
    return aggregated
```

### Pitfall 11: Over-Privileging Service Accounts

**❌ Anti-Pattern:**
Service accounts with broad access for convenience.

**✅ Best Practice:**
Principle of least privilege with just-in-time elevation.

```yaml
ServiceAccount:
  name: pipeline_etl
  permissions:
    - object: RawData
      actions: [READ]
      
    - object: StagingData
      actions: [READ, WRITE]
      
    # No access to Production Ontology
    # Requires elevation request for troubleshooting
```

### Pitfall 12: Audit Trail Gaps

**❌ Anti-Pattern:**
Selective logging that misses critical events.

**✅ Best Practice:**
Comprehensive, immutable audit logging.

```yaml
AuditConfiguration:
  log_all:
    - object_creates
    - object_updates
    - object_deletes
    - action_executions
    - permission_changes
    - failed_access_attempts
    
  retention:
    hot_storage: 90_days
    cold_storage: 7_years
    
  integrity:
    signing: true
    tamper_detection: true
```

## Organizational Pitfalls

### Pitfall 13: IT-Led Without Business

**❌ Anti-Pattern:**
Technical team designs Ontology without domain experts.

**Result:** Ontology that doesn't match operational reality.

**✅ Best Practice:**
Business-led design with technical facilitation.

```
Ontology Design Team:
  - Business Owner (decision maker)
  - Domain Experts (2-3 per functional area)
  - Data Stewards (data quality owners)
  - FDE (facilitation, technical guidance)
  - Security Officer (classification, access)
```

### Pitfall 14: Big Bang Deployment

**❌ Anti-Pattern:**
Attempting to model entire enterprise at once.

**Result:** 18-month project with no delivered value.

**✅ Best Practice:**
Iterative delivery with quick wins.

```
Phase 1: Single high-value use case (8-12 weeks)
Phase 2: Adjacent use cases (8-12 weeks each)
Phase 3: Cross-functional expansion
Phase 4: Enterprise scale
```

### Pitfall 15: Neglecting Change Management

**❌ Anti-Pattern:**
Focusing only on technology, not user adoption.

**Result:** Excellent system that nobody uses.

**✅ Best Practice:**
Proactive change management from day one.

```
Change Management Activities:
  - Stakeholder analysis and engagement plan
  - Communication strategy (weekly updates, demos)
  - Training program (role-based curricula)
  - Champion network (early adopters as advocates)
  - Feedback loops (surveys, user advisory board)
  - Success metrics (adoption, satisfaction, outcomes)
```

## Performance Pitfalls

### Pitfall 16: Unoptimized Queries

**❌ Anti-Pattern:**
N+1 queries, full table scans, no indexing.

**✅ Best Practice:**
Query optimization and caching strategies.

```python
# Bad: N+1 query
for customer in customers:
    orders = query(f"SELECT * FROM orders WHERE customer_id = {customer.id}")
    
# Good: Single query with join
query("""
    SELECT c.*, o.*
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
""")
```

### Pitfall 17: Ignoring Object Growth

**❌ Anti-Pattern:**
Designing for current scale, not future growth.

**✅ Best Practice:**
Capacity planning and archival strategies.

```yaml
DataLifecycle:
  hot_data:
    retention: 90_days
    storage: ssd
    
  warm_data:
    retention: 2_years
    storage: standard
    
  cold_data:
    retention: 7_years
    storage: glacier
    
  archive:
    action: compress_and_move
    trigger: age > 2_years and last_accessed > 90_days
```

---

## Summary: The Critical Few

| Priority | Pitfall | Prevention |
|----------|---------|------------|
| 🔴 Critical | Ungrounded AI | Always use Ontology context |
| 🔴 Critical | Security downgrade | Automatic classification propagation |
| 🔴 Critical | No audit trail | Comprehensive, immutable logging |
| 🟠 High | Table-to-Object mapping | Semantic reconciliation workshop |
| 🟠 High | IT-led design | Business ownership with FDE facilitation |
| 🟠 High | Big bang deployment | Iterative, use-case-driven delivery |
| 🟡 Medium | Over-normalization | Cohesive Object Type design |
| 🟡 Medium | CDC misconfiguration | Monitoring and dead letter queues |
| 🟡 Medium | Query performance | Optimization and caching |

Remember: "The Ontology is the single source of truth" - but only if designed and maintained correctly.
