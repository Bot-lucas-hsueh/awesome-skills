## 10. Common Pitfalls

### Anti-Pattern 1: Static Snapshot as "Digital Twin"

❌ BAD:
```
"Our digital twin is a 3D model of the factory floor
 that we update whenever there is a major equipment change."
```
A static 3D model with manual updates is a BIM (Building Information Model) or as-built model, not a digital twin. It carries no live data, cannot reflect current operational state, and provides no predictive capability.

✅ GOOD:
```
Our factory twin streams OPC-UA data from 200 PLCs at 1Hz.
Twin state is updated within 500ms of physical state change.
Stale data beyond 5 seconds triggers a visual staleness warning on all dashboards.
Data age is displayed prominently alongside every sensor reading.
```

---

### Anti-Pattern 2: Physics-Free ML Model for Safety-Critical Decisions

❌ BAD:
```python
# "Our pressure vessel twin uses pure ML for failure prediction"
model = XGBoostClassifier()
model.fit(historical_sensor_data, failure_labels)
# Deployed to recommend vessel venting — no physics constraints,
# no uncertainty quantification, no safe-operating-envelope enforcement
```
A black-box ML model trained on historical data will fail confidently on out-of-distribution conditions — exactly the novel scenarios that matter most for safety-critical applications.

✅ GOOD:
```python
# Physics-informed hybrid: ML for residual modeling, physics for hard constraints
physics_model = PressureVesselFEM(geometry, material_properties)
residual_model = GaussianProcessRegressor()  # uncertainty-aware predictions

predicted_pressure, uncertainty = residual_model.predict(sensor_features)
safe_limit = physics_model.burst_pressure * 0.80  # 20% safety margin

# Hard constraint: physics envelope enforced regardless of ML output
if predicted_pressure + 2 * uncertainty > safe_limit:
    trigger_safety_interlock()
    alert_operator("Safety limit approached — human review required")
```

---

### Anti-Pattern 3: Single Point of Failure for IoT Data Ingestion

❌ BAD:
```yaml
# Single MQTT broker, no redundancy, no monitoring
mqtt_broker: mosquitto-prod-01:1883
# If broker fails: all 500 sensors lose their data path
# Twin goes stale with no alert; maintenance team discovers hours later
```

✅ GOOD:
```yaml
# Clustered MQTT with Kafka as durable buffer
mqtt_cluster:
  - mosquitto-01:1883
  - mosquitto-02:1883  # load-balanced, automatic failover
kafka_topics:
  sensors.raw:        # retention: 7 days (buffer against downstream outages)
  sensors.validated:  # post-quality-check stream
monitoring:
  - alert: ingestion_rate_drops_below 95% of expected_rate -> PagerDuty
  - alert: broker_consumer_lag_exceeds 10s -> auto-scale consumer group
  - alert: twin_data_age_exceeds 5x_sample_interval -> ops dashboard warning
```

---

### Anti-Pattern 4: No Data Validation (Garbage-In, Garbage-Out)

❌ BAD:
```python
# Raw sensor values passed directly to twin and ML model without validation
twin.update_property("temperature", sensor_reading)
# Sensor stuck at -999.0 (hardware disconnection sentinel value)
# Twin shows -999C; ML model predicts catastrophic imminent failure
# Operations team responds to false emergency; production halted unnecessarily
```

✅ GOOD:
```python
def validate_sensor(reading, sensor_config, prev_reading):
    if reading is None or reading == sensor_config.error_sentinel:
        return SensorQuality.MISSING
    if not (sensor_config.min_valid <= reading <= sensor_config.max_valid):
        return SensorQuality.OUT_OF_RANGE
    if abs(reading - prev_reading) > sensor_config.max_rate_of_change:
        return SensorQuality.SPIKE
    return SensorQuality.VALID

quality = validate_sensor(reading, config, prev)
twin.update_property("temperature", reading if quality == SensorQuality.VALID else None)
twin.update_property("temperature_quality", quality.value)
twin.update_property("temperature_last_valid_ts", datetime.utcnow() if quality == SensorQuality.VALID else unchanged)
# Dashboard shows data quality indicator; ML model skips MISSING/OUT_OF_RANGE inputs
```

---

### Anti-Pattern 5: Twin Without Change Management (Physical Changes Not Reflected)

❌ BAD:
```
Physical event: Bearing replaced with different OEM model
  - Old bearing BPFO: 87.3 Hz (from original geometry)
  - New bearing BPFO: 94.1 Hz (different ball count, different pitch diameter)

Digital twin: Still configured with original bearing defect frequency thresholds
  - Anomaly detector monitors 87.3 Hz band for fault energy
  - New bearing's actual fault frequency (94.1 Hz) is never monitored

Result: Bearing fails 8 months after replacement without any twin alert
  - $180K unplanned downtime incident
  - Post-mortem reveals twin was monitoring the wrong frequency for 8 months
```

✅ GOOD:
```
CMMS (Maintenance Management System) integration:
  - Work order completion triggers webhook to twin update API
  - Replacement part number looked up in component library
  - New bearing geometry -> auto-recalculate BPFO, BPFI, BSF defect frequencies
  - Twin bearing model properties updated within 15 minutes of work order close
  - ML model feature thresholds recalibrated for new component within 24h
  - Change event logged in twin audit trail: timestamp, technician ID, old/new values
  - Supervisor notification: "Twin model updated following maintenance WO-48271"
```

---

