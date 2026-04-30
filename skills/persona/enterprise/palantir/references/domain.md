## § 6 · Domain Knowledge

### 6.1 Ontology Modeling Framework

```python
# Foundry Ontology Structure Example
# Object Type: Aircraft
{
  "objectType": "Aircraft",
  "properties": [
    {"name": "tailNumber", "type": "string", "primaryKey": true},
    {"name": "model", "type": "string"},
    {"name": "manufacturer", "type": "string"},
    {"name": "maxRangeNauticalMiles", "type": "integer"},
    {"name": "lastMaintenanceDate", "type": "date"},
    {"name": "operationalStatus", "type": "enum", 
     "values": ["ACTIVE", "MAINTENANCE", "RETIRED"]}
  ],
  "links": [
    {"to": "Airline", "type": "operatedBy", "cardinality": "manyToOne"},
    {"to": "Flight", "type": "assignedTo", "cardinality": "oneToMany"},
    {"to": "MaintenanceEvent", "type": "hasHistory", "cardinality": "oneToMany"}
  ],
  "actions": [
    {"name": "ScheduleMaintenance", 
     "parameters": ["date", "maintenanceType", "facility"]},
    {"name": "UpdateStatus",
     "parameters": ["newStatus", "reason"],
     "validation": "statusTransitionValid()"}
  ]
}
```

### 6.2 AIP Logic Workflow Pattern

```yaml
# AIP Logic: Supply Chain Risk Assessment
workflow:
  name: supplier_risk_assessment
  trigger: 
    type: scheduled
    cron: "0 6 * * *"
  
  steps:
    - name: identify_at_risk_suppliers
      action: query_ontology
      query: |
        SELECT supplier, COUNT(*) as delayed_shipments
        FROM Supplier JOIN Shipment ON Supplier.id = Shipment.supplierId
        WHERE Shipment.status = 'DELAYED' 
          AND Shipment.delayDays > 7
        GROUP BY supplier
        HAVING COUNT(*) > 3
    
    - name: enrich_with_external_data
      action: llm_extraction
      model: gpt-4
      input: |
        Search news and financial reports for {{supplier.name}}.
        Extract: financial health, geopolitical risks, natural disasters.
      output_schema:
        - risk_score: integer(1-10)
        - risk_factors: array[string]
        - recommendation: string
    
    - name: create_risk_alert
      action: create_object
      object_type: SupplyChainRisk
      properties:
        supplier: "{{steps.identify_at_risk_suppliers.supplier}}"
        riskScore: "{{steps.enrich_with_external_data.risk_score}}"
        automatedAssessment: "{{steps.enrich_with_external_data.recommendation}}"
    
    - name: notify_procurement_team
      action: send_notification
      condition: "{{steps.enrich_with_external_data.risk_score}} > 7"
      channel: workshop_inbox
      recipients: ["procurement_managers"]
```

### 6.3 Government Contracts Knowledge

| Contract Type | Typical Value | Key Requirements |
|--------------|---------------|------------------|
| **IDIQ (Indefinite Delivery)** | $100M-$10B | Multiple award; task order competition |
| **SBIR/STTR** | $50K-$2M | Small business innovation research |
| **OTAs (Other Transaction Authority)** | Variable | Rapid prototyping; flexible terms |
| **CIO-SP4** | $40B ceiling | Government-wide IT services |
| **Defense Enterprise** | $100M+ | IL5/IL6 accreditation; CMMC compliance |

### 6.4 Palantir Financial Intelligence (2024-2025)

| Metric | Value | Context |
|--------|-------|---------|
| **Revenue FY2025** | $4.48B | +56% YoY growth |
| **Q4 2025 Revenue** | $1.41B | +70% YoY growth |
| **Market Cap** | $380B+ | S&P 500 inclusion Sept 2024 |
| **US Commercial Revenue Growth (Q4 2025)** | +137% YoY | Explosive AIP-driven growth |
| **Government Revenue** | ~45% of total | Defense, intelligence, health |
| **Employees** | ~4,200 | High revenue-per-employee model |
| **Net Dollar Retention** | 139% | Industry-leading expansion |
| **AIP Bootcamp Conversion** | >70% | Prospect to customer rate |
| **First Profitable Year** | 2023 | GAAP profitable |

---
