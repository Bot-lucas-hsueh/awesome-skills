# § 9 · Scenario Examples Reference

## Scenario Expansion: Healthcare Network Analysis

**Use Case:** Hospital network seeking to optimize patient flow, reduce readmissions, and improve population health outcomes.

**Ontology Extension:**

```yaml
ObjectTypes:
  Patient:
    properties:
      - mrn (Medical Record Number)
      - demographics
      - riskScore
      - socialDeterminants[]
      
  Encounter:
    properties:
      - encounterId
      - type (inpatient, outpatient, emergency)
      - admissionDate
      - dischargeDate
      - diagnosisCodes[]
      
  CareTeam:
    properties:
      - teamId
      - primaryPhysician
      - specialists[]
      - careCoordinator
      
  RiskFactor:
    properties:
      - factorId
      - category (clinical, behavioral, social)
      - severity
      - interventionStatus

LinkTypes:
  - Patient.hasEncounter → Encounter
  - Encounter.assignedTo → CareTeam
  - Patient.hasRiskFactor → RiskFactor
  - Encounter.followedBy → Encounter
```

**AIP Use Case: Readmission Risk Prediction**

```python
workflow: readmission_risk_assessment
trigger: patient_discharge

steps:
  - gather_patient_history:
      query: |
        MATCH (p:Patient {mrn: $mrn})-[:hasEncounter]->(e:Encounter)
        OPTIONAL MATCH (p)-[:hasRiskFactor]->(r:RiskFactor)
        RETURN p, collect(e) as encounters, collect(r) as risk_factors
  
  - predict_readmission:
      model: readmission_risk_v2
      input: patient_history
      output: risk_score, top_factors, confidence
  
  - generate_care_plan:
      action: aip_logic
      prompt: |
        Patient: {{patient.mrn}}
        Risk score: {{risk_score}}/100
        Primary risk factors: {{top_factors}}
        
        Generate personalized care transition plan:
        1. Follow-up appointment timing and specialty
        2. Medication reconciliation priorities
        3. Home care services needed
        4. Social support resources
        5. Warning signs to watch for
      
  - schedule_interventions:
      action: create_objects
      objects:
        - type: CareTask
          properties:
            patient: "{{patient.mrn}}"
            taskType: "FOLLOW_UP_CALL"
            dueDate: "{{discharge_date + 2_days}}"
            assignedTo: "{{care_coordinator}}"
```

---

## Scenario Expansion: Manufacturing Quality Control

**Use Case:** Automotive manufacturer reducing defect rates through real-time quality monitoring and predictive maintenance.

**Ontology Extension:**

```yaml
ObjectTypes:
  ProductionLine:
    properties:
      - lineId
      - productType
      - shiftSchedule
      - throughputTarget
      
  QualityInspection:
    properties:
      - inspectionId
      - timestamp
      - defectType
      - severity
      - rootCause
      
  Sensor:
    properties:
      - sensorId
      - type (vibration, temperature, pressure)
      - location
      - calibrationDate
      
  MaintenanceEvent:
    properties:
      - eventId
      - type (predictive, preventive, corrective)
      - scheduledDate
      - actualDate
      - partsReplaced[]

LinkTypes:
  - ProductionLine.monitoredBy → Sensor
  - ProductionLine.produces → QualityInspection
  - Sensor.triggers → MaintenanceEvent
  - MaintenanceEvent.addresses → QualityInspection
```

**AIP Use Case: Predictive Quality Control**

```yaml
workflow: predictive_quality_alert
trigger: sensor_anomaly_detected

steps:
  - analyze_sensor_patterns:
      query: |
        MATCH (s:Sensor {sensorId: $sensorId})-[:generates]->(r:Reading)
        WHERE r.timestamp > now() - interval '1 hour'
        RETURN collect(r) as recent_readings
  
  - predict_defect_probability:
      model: quality_prediction_model
      input:
        sensor_readings: recent_readings
        line_context: production_line_state
      output: defect_probability, predicted_defect_type, time_to_failure
  
  - decision_support:
      action: aip_logic
      condition: defect_probability > 0.7
      prompt: |
        ALERT: High defect probability detected
        Line: {{line_id}}
        Probability: {{defect_probability}}%
        Predicted issue: {{predicted_defect_type}}
        ETA: {{time_to_failure}}
        
        Recommend:
        1. Immediate action (stop line/adjust parameters)
        2. Maintenance scheduling
        3. Batch quarantine requirements
        4. Root cause investigation steps
      
  - execute_response:
      action: conditional
      if: defect_probability > 0.9
      then:
        - action: stop_production_line
        - action: notify_quality_manager
        - action: create_maintenance_ticket
      else:
        - action: schedule_increased_monitoring
        - action: alert_line_supervisor
```

---

## Scenario Expansion: Cybersecurity Threat Hunting

**Use Case:** Critical infrastructure operator detecting and responding to advanced persistent threats (APTs).

**Ontology Extension:**

```yaml
ObjectTypes:
  Asset:
    properties:
      - assetId
      - type (server, workstation, network_device)
      - criticality
      - networkSegment
      - vulnerabilities[]
      
  Alert:
    properties:
      - alertId
      - type (IDS, EDR, SIEM)
      - severity
      - timestamp
      - rawData
      
  ThreatActor:
    properties:
      - actorId
      - attribution
      - tactics[]
      - techniques[] (MITRE ATT&CK)
      
  Incident:
    properties:
      - incidentId
      - status (detected, investigating, contained, resolved)
      - impactAssessment
      - responseActions[]

LinkTypes:
  - Alert.targets → Asset
  - Alert.indicates → ThreatActor
  - Alert.partOf → Incident
  - Asset.communicatesWith → Asset
```

**AIP Use Case: Threat Intelligence Enrichment**

```python
workflow: threat_intelligence_analysis
trigger: high_severity_alert

steps:
  - enrich_alert:
      query: |
        MATCH (a:Alert {alertId: $alertId})-[:targets]->(asset:Asset)
        OPTIONAL MATCH (asset)-[:communicatesWith]->(connected:Asset)
        RETURN a, asset, collect(connected) as connected_assets
  
  - analyze_ioc:
      action: threat_intelligence_lookup
      indicators:
        - ip_addresses: alert.source_ips
        - file_hashes: alert.file_hashes
        - domains: alert.domains
      
  - generate_hypothesis:
      action: aip_logic
      prompt: |
        Security Alert Analysis:
        
        Alert Type: {{alert.type}}
        Target Asset: {{asset.assetId}} (Criticality: {{asset.criticality}})
        Connected Assets: {{connected_assets_count}}
        
        Threat Intelligence:
        - Known malicious IPs: {{ti.malicious_ips}}
        - Malware families: {{ti.malware_families}}
        - Threat actor attribution: {{ti.attribution}}
        
        Generate:
        1. Attack hypothesis (TTPs based on MITRE ATT&CK)
        2. Lateral movement risk assessment
        3. Recommended containment actions
        4. Investigation priorities
        5. Threat hunting queries for similar activity
      
  - auto_response:
      action: conditional
      if: ti.confidence > 0.8 and asset.criticality == "CRITICAL"
      then:
        - action: isolate_asset
        - action: block_indicators
        - action: escalate_to_soc
```
