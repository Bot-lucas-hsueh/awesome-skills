## § 3 · Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|--------------------|------------|
| Stale map in construction zone | 🔴 Critical | AV follows map into blocked lane or reversed traffic | Real-time construction zone detection from cameras; local map override; 48h freshness SLA with alert |
| Map localization divergence | 🔴 Critical | Vehicle localizes to wrong lane (adjacent) causing dangerous lane departure | Dual-mode localization: LiDAR-to-map + GNSS; disagreement > 0.5m triggers safety alert |
| Missing regulatory elements (stop line, speed limit) | 🔴 Critical | AV runs stop line or exceeds speed limit due to missing annotation | Automated completeness audit: flag any intersection without stop lines; human review gate |
| Coordinate system error causing systematic offset | 🟡 High | All map positions off by fixed offset if UTM zone/datum mismatch | Always store map in WGS84 with explicit datum; validate by overlaying on satellite imagery |
| Online map prediction error (MapTR) | 🟡 High | Predicted lane boundary diverges from ground truth in complex intersection | Use offline HD map when available as prior; online prediction as fallback only; evaluate on nuScenes IoU |
| Map tile version mismatch in fleet | 🟡 High | Different vehicles use different map versions at same location, inconsistent behavior | Centralized map version control with per-tile hash; version check before mission start |
| High map file size impacting memory | 🟢 Medium | Loading full region map exhausts compute memory budget on embedded SoC | Tile-based streaming: load only tiles within 500m radius + look-ahead 2km; evict LRU tiles |

> **IMPORTANT**: HD maps for autonomous driving are safety-critical infrastructure. Map pipelines must include automated QA gates, human review for annotation errors, and freshness monitoring before use in production AV deployment. Map errors are a root cause of AV incidents.

---
