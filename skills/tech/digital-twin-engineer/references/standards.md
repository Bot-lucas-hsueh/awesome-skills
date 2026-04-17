## 7. Standards & Reference

### ISO 23247 — Manufacturing Digital Twin Architecture

```
Layer 4: Service Layer          [Applications, APIs, User Interfaces]
              │
Layer 3: Data Layer             [Twin Models, Analytics, Historical Store]
              │
Layer 2: Communication Layer    [OPC-UA, MQTT, REST/WebSocket, Kafka]
              │
Layer 1: Device Layer           [PLCs, Sensors, Actuators, Edge Nodes]
              │
Layer 0: Physical Assets        [Machines, Products, Processes]
```

### OPC-UA Information Model
- **Namespace**: Organizes node types by domain (e.g., `urn:manufacturer:machine:v1`)
- **Node Classes**: Object, Variable, Method, ObjectType, VariableType, ReferenceType, DataType, View
- **Security Modes**: None / Sign
- **Subscription Model**: MonitoredItems with configurable sampling interval (minimum 100ms for most PLCs)

### DTDL (Digital Twins Definition Language) Schema
```json
{
  "@context": "dtmi:dtdl:context;3",
  "@id": "dtmi:example:CNCMachine;1",
  "@type": "Interface",
  "displayName": "CNC Machine",
  "contents": [
    { "@type": "Property", "name": "spindleSpeed", "schema": "double", "unit": "revolutionsPerMinute" },
    { "@type": "Telemetry", "name": "vibrationRMS", "schema": "double", "unit": "metrePerSecondSquared" },
    { "@type": "Relationship", "name": "isPartOf", "target": "dtmi:example:ProductionLine;1" }
  ]
}
```

### Key Metrics and Target Ranges

| Metric | Target | Warning | Critical |
|--------|--------|---------|----------|
| Twin Synchronization Latency | < 100ms (real-time) | 100–500ms | > 500ms |
| Prediction Accuracy (RMSE) | Domain-specific baseline -20% | At baseline | > Baseline +10% |
| Anomaly Detection False Alarm Rate | < 5% | 5–15% | > 15% |
| Simulation Fidelity Score (vs. physical) | > 95% | 90–95% | < 90% |
| Data Freshness (max sensor age in twin) | < 2x sample interval | 2–5x | > 5x |
| Sensor Data Completeness | > 99.5% | 98–99.5% | < 98% |
| Model Calibration Drift (quarterly) | < 2% MAPE change | 2–5% | > 5% |

---

