## 8. Standard Workflow

### Phase 1 — Digital Twin Architecture Design

```
Step 1: Asset Discovery and Physics Characterization
  - Enumerate all physical assets in scope with hierarchy
    (site -> line -> cell -> machine -> component)
  - Document failure modes (FMEA), operating envelope, and sensor inventory
  - [✓ Done] FMEA complete; sensor map covers >= 95% of critical failure modes
  - [✗ FAIL] Critical failure mode has no observable sensor signal
             -> add sensor or identify proxy measurement

Step 2: Data Architecture Design
  - Select synchronization frequency per asset class (Gate 1 decision)
  - Design Kafka topic hierarchy or MQTT topic tree
  - Define InfluxDB/TimescaleDB schema: measurements, tags (metadata), fields (values)
  - [✓ Done] Schema reviewed; cardinality estimated; retention policy defined
  - [✗ FAIL] Unbounded tag cardinality in InfluxDB -> redesign schema to cap tag values

Step 3: Twin Model Design
  - Author DTDL interfaces for each asset class
  - Define twin graph relationships (contains, feeds, monitors, controls)
  - Select platform: Azure Digital Twins for graph queries, TwinMaker for spatial scenes
  - [✓ Done] DTDL validated with dtdl-validator CLI; graph connectivity verified
  - [✗ FAIL] DTDL model missing required telemetry fields -> update and re-validate

Step 4: OT/IT Security Architecture
  - Apply Purdue Model segmentation; define DMZ components
  - Select protocol translation points (OPC-UA -> MQTT -> Kafka)
  - Define data diode placement for safety-critical segments
  - [✓ Done] Security architecture reviewed by OT security specialist
  - [✗ FAIL] Direct cloud connectivity from PLC network -> mandatory DMZ insertion
```

### Phase 2 — Predictive Maintenance Implementation

```
Step 1: Feature Engineering from Time-Series
  - Extract statistical features: RMS, kurtosis, FFT peaks, trend slopes
    over rolling windows
  - Apply domain knowledge: vibration frequencies corresponding to bearing
    defect frequencies (BPFO, BPFI, BSF from manufacturer geometry specs)
  - [✓ Done] Features validated with domain expert (maintenance engineer)
  - [✗ FAIL] Features derived from intuition only
             -> must correlate with known failure physics

Step 2: Model Training and Validation
  - Split data chronologically: train on earliest 70%, validate on next 15%,
    test on latest 15%
  - Train RUL model (LSTM, temporal CNN, or gradient boosting); tune on
    validation set
  - Evaluate: RMSE, MAE, prediction horizon accuracy at 7-day and 30-day horizons
  - [✓ Done] Test RMSE <= baseline -20%; false alarm rate < 5% on held-out faults
  - [✗ FAIL] Model trained and tested on same temporal window
             -> data leakage; re-split chronologically

Step 3: Twin Integration and Alert Pipeline
  - Deploy model as microservice; subscribe to twin telemetry via Kafka consumer
  - Write predictions back to Azure Digital Twins as computed properties
  - Configure Grafana alerts: maintenance required, degraded confidence, anomaly
  - [✓ Done] End-to-end test: inject synthetic fault signal -> verify alert fires
             within 2x sample interval
  - [✗ FAIL] Alert latency > 10x sample interval -> optimize model inference
             or stream processing topology

Step 4: Feedback Loop and Continuous Improvement
  - Log all maintenance actions with timestamps and technician findings
  - Compare predicted RUL to actual time-to-failure from maintenance records
  - Schedule quarterly model recalibration if MAPE drift > 2%
  - [✓ Done] Feedback loop operational; retraining pipeline tested end-to-end
  - [✗ FAIL] No mechanism to capture actual failure dates
             -> implement CMMS (maintenance log) integration
```

---

