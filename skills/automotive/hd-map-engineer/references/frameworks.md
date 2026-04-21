## 7. Standards & Reference

**7.1 Key Formats and Frameworks:**

| Format/Framework | Version | Key Features | Use Case |
|-----------------|---------|-------------|---------|
| OpenDRIVE | 1.6 (ASAM) | Road/junction topology, lane sections, road objects, signals | Simulation (CARLA), planning tools, interchange format |
| Lanelet2 | v1.2 | Lanelet topology, routing graph, regulatory elements, OSM-based | Autoware, open-source AV stacks, production maps |
| HERE HD Live Map | v3 | Real-time map updates, NDS format, cloud-synced | Commercial L3/L4 systems with OTA map updates |
| OpenStreetMap | — | Crowd-sourced road network; free but SD resolution | Base map layer, map gap detection, crowdsourcing workflows |
| NDS (Navigation Data Standard) | 2.x | Tile-based, compressed, efficient for embedded | Production navigation chips and embedded AV systems |
| Apollo HD Map | v2 | Protobuf-based, Baidu Apollo integration | Apollo-based robotaxi deployments |

**7.2 Key Metrics and Targets:**

| Metric | Formula | Target Value | Notes |
|--------|---------|-------------|-------|
| Lateral localization accuracy | abs(lateral_error) in map frame vs. ground truth | < 10 cm | Minimum for lane-level positioning |
| Absolute position accuracy | sqrt(dx^2 + dy^2) vs. surveyed reference | < 0.3 m | GPS-anchored map accuracy |
| Online MapTR IoU (lane divider) | Intersection
| Online MapTR Chamfer Distance | Mean min-dist between predicted and GT polylines | < 0.5 m | Vectorized prediction quality |
| Map annotation density | Map elements per km^2 (lane lines, signs, markings) | > 500 elements/km^2 urban | Completeness target |
| Map freshness SLA | Time since last verification of map segment | < 48 h construction zone, < 30 days stable road | Fleet crowdsource update target |
| Localization dropout rate | Fraction of frames with NDT fitness < threshold | < 0.1% | NDT fitness threshold: 0.5 |
| Tile loading latency | Time to load map tiles for current position | < 50 ms | Streaming tile server requirement |

---
