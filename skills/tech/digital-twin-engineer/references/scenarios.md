## 9. Scenario Examples

### Scenario 1 — Factory CNC Machine Twin for Predictive Maintenance

**User:** We have 50 CNC machines in our factory. We want to predict spindle bearing failures 2 weeks in advance. Where do we start?

**Digital Twin Engineer:**

Good use case with clear ROI. Let me run through the 5 gates first.

Gate 1 (Sync Frequency): Bearing failure prediction at a 2-week horizon does not require sub-100ms latency. 1-second vibration samples streamed to cloud every 60 seconds is sufficient.

Gate 2 (Data Volume): 50 machines x 4 vibration axes x 1 sample/sec = 200 data points/sec. Low volume — MQTT to a single Mosquitto broker is adequate. No Kafka needed at this scale.

Gate 3 (Physics Fidelity): Feature-based ML (FFT, envelope analysis) rather than full FEM simulation is appropriate. Bearing defect frequencies are deterministic from geometry — extract BPFO, BPFI, BSF from manufacturer specs.

Gate 4 (Edge vs. Cloud): Run FFT feature extraction on an edge industrial PC per machine cluster to reduce bandwidth. Push statistical features to cloud, not raw vibration waveforms.

Gate 5 (ROI): At $50K per unplanned downtime incident, preventing 5 incidents/year across 50 machines = $250K/year. Platform cost for Azure Digital Twins at this scale is approximately $15K/year. Clear positive ROI.

**Recommended architecture:**

```
[Vibration Sensor] -> [Edge PC: FFT features via Node-RED]
    -> [MQTT/Mosquitto] -> [Azure IoT Hub]
    -> [InfluxDB: feature time-series]
    -> [Azure Digital Twins: CNC machine graph]
    -> [ML Model: LSTM RUL] -> [Grafana Alert Dashboard]
```

**DTDL for CNC spindle:**
```json
{
  "@id": "dtmi:factory:CNCSpindle;1",
  "@type": "Interface",
  "contents": [
    { "@type": "Telemetry", "name": "vibrationRMS", "schema": "double" },
    { "@type": "Telemetry", "name": "bpfoAmplitude", "schema": "double" },
    { "@type": "Property", "name": "predictedRUL_days", "schema": "integer" },
    { "@type": "Property", "name": "maintenanceAlert", "schema": "boolean" }
  ]
}
```

Start with 3 months of historical vibration data on 5 pilot machines before scaling to all 50. Validate that pilot model predictions match actual maintenance events before fleet-wide deployment.

---

### Scenario 2 — Building Energy Optimization Twin

**User:** We manage a 40-story commercial building. We want a digital twin to optimize HVAC energy consumption while maintaining comfort.

**Digital Twin Engineer:**

Building energy twins are well-suited to this problem. Here are the key design decisions.

**Data sources to integrate:**
- BACnet/IP (your BMS) via Node-RED protocol translation to MQTT to time-series DB
- Weather API (outdoor temp, humidity, solar irradiance forecast at 15-minute intervals)
- Occupancy sensors (CO2 proxy or PIR) per zone
- Energy meters (electrical sub-metering per floor)

**Twin model approach:** EnergyPlus or TRNSYS for physics-based thermal simulation; calibrate against 12 months of actual consumption data. Target: simulation error < 10% on monthly energy totals.

**Optimization control loop:**
```
[Weather Forecast] + [Occupancy Prediction]
    -> [Thermal Simulation (EnergyPlus ROM)]
    -> [HVAC Setpoint Optimizer (MPC)]
    -> [BMS Commands via BACnet]
    -> [Measurement] -> [Twin Update] -> [Loop]
```

Model Predictive Control (MPC) with a 24-hour horizon and 15-minute timesteps typically delivers 15–25% energy reduction vs. reactive control. Use Ansys Twin Builder to generate the ROM from your full EnergyPlus model — this reduces simulation time from hours to milliseconds, enabling real-time MPC.

**Expected outcomes:** 15–25% HVAC energy reduction; comfort KPIs (PMV index) maintained at -0.5 to +0.5 throughout.

---

### Scenario 3 — Supply Chain Twin for Disruption Simulation

**User:** We want to build a supply chain digital twin to simulate the impact of a key supplier going offline and identify mitigation options.

**Digital Twin Engineer:**

This is a decision-support twin rather than a real-time synchronization twin. The architecture is different from industrial IoT twins.

**Twin type:** Discrete event simulation (not physics-based) using AnyLogic or SimPy (Python), updated daily from ERP/WMS data feeds.

**Key entities to model:** Suppliers (capacity, lead time, reliability distribution), transportation lanes (transit time, disruption probability), inventory nodes (WIP, finished goods by SKU), demand signals (orders, statistical forecasts).

**Disruption simulation workflow:**
1. Pull current inventory positions and demand signals from ERP via REST API
2. Update AnyLogic twin model with current state snapshot
3. Trigger scenario: set target supplier capacity to 0% for N days
4. Run 1,000 Monte Carlo replications (approximately 30-second runtime on 8-core server)
5. Output: probability distribution of stockout events, revenue impact, and recovery time by mitigation strategy (alternate supplier, safety stock increase, demand shaping)

**Pre-built scenario library to build first:** Single supplier failure, port closure (transit lane down), demand surge (+30%), and compound disruption (two simultaneous events).

The engineering value here is in the scenario library and calibrated distributions, not real-time sync. Focus effort on accurate lead-time distributions from 2+ years of historical ERP data.

---

### Scenario 4 (Anti-Pattern) — Batch-Update Twin Presented as Real-Time

**User:** Our digital twin updates every 4 hours from our data warehouse ETL job. Is this a real-time digital twin?

**Digital Twin Engineer:**

No — and this distinction matters operationally. What you have is a periodic snapshot model, not a digital twin in the technical sense.

A digital twin, per ISO 23247, maintains a live-synchronized virtual representation whose state reflects the physical asset's current state within a defined and bounded latency. A 4-hour update cycle means operators viewing the "twin" may be seeing state that is up to 4 hours old. Any predictive alert fired during that window may be based on conditions that have already changed — or worsened.

**The specific danger:** If your twin surfaces a "no alert" status, operators may interpret this as "currently healthy" when the physical asset may have entered an alarm condition in the past 4 hours. This false confidence can delay intervention.

**Your three options:**

1. **Reframe scope honestly:** Call it an "operational analytics dashboard" — it is a valid and useful tool, but the wrong label creates dangerous expectations
2. **Upgrade to near-real-time:** Replace ETL with CDC (Change Data Capture) from source systems feeding into a Kafka pipeline with 60-second twin refresh — achievable without replacing the warehouse
3. **Hybrid approach:** Near-real-time streaming for safety and maintenance signals; 4-hour batch acceptable for business performance KPIs that do not drive operational decisions

Never present batch-refresh dashboards as real-time digital twins to operations teams. The consequences of stale-data decisions in industrial settings can include equipment damage, product quality failures, and safety incidents.

---

