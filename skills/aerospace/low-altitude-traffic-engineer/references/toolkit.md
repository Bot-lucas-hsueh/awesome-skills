## § 6 Professional Toolkit

### Core UTM Platforms & Standards
| Tool
|----------------|---------|-------------|
| **ASTM F3548 UTM Standard** | US UTM interoperability framework; defines USS roles, DSS interface, and strategic conflict detection API | Design any US-market UTM system; required for FAA integration |
| **EASA U-Space Regulations (EU 2021/664-666)** | European U-Space service definitions (geo-awareness, flight authorization, traffic info, U2 protocols) | Any EU airspace deployment; defines USS certification requirements |
| **OpenAPI UTM Specification (NASA/GUTMA)** | REST API schema for UTM data exchange (flight plans, constraints, telemetry) | Implement USS-to-USS or USS-to-FIMS interfaces |
| **ASTM F3411 Remote ID** | Broadcast and Network RID message formats and performance requirements | Remote ID compliance; enforcement integration |
| **AIXM/FIXM** | Aeronautical Information Exchange Model for geofencing, NOTAMs, and aeronautical data exchange | Airspace data integration with ANSPs; constraint publication |
| **NASA UTM Research Platform** | Open-source UTM simulation and research testbed | Algorithm development, academic research, early-stage testing |
| **ArcGIS
| **OpenSky Network** | Live ADS-B data feed for manned traffic situational awareness | Real-world manned aircraft density analysis; integration testing |
| **SUMO
| **Python / shapely

### Monitoring & Analysis Tools
| Tool | Purpose |
|------|---------|
| **FlightAware
| **Prometheus + Grafana** | UTM system performance monitoring; latency histograms for CD&R algorithms |
| **ELK Stack (Elasticsearch/Logstash/Kibana)** | UTM event logging, post-incident analysis, compliance auditing |

---
