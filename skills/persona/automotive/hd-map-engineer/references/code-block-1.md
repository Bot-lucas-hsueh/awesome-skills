# code Example

```
         HD MAP ARCHITECTURE
         ===================

  MAP CREATION (Offline)              MAP CONSUMPTION (Online)
  +--------------------+              +-----------------------------+
  | LiDAR Survey Passes|              |  AV Map Server              |
  | (HDL-SLAM, LIO-SAM)|              |  REST/gRPC tile API         |
  +--------+-----------+              +------+----------------------+
           |                                 |
  +--------v-----------+              +------v----------------------+
  | Ground Intensity   |              |  Map Localization           |
  | Reflectance Map    |              |  NDT
  +--------+-----------+              |  <10cm lateral accuracy     |
           |                          +------+----------------------+
  +--------v-----------+                     |
  | Lane Annotation     |              +------v----------------------+
  | (RoadRunner/JOSM)   |              |  Map-Aware Planner          |
  | OpenDRIVE
  +--------+-----------+              |  Regulatory element lookup  |
           |                          +-----------------------------+
  +--------v-----------+
  | Map QA Pipeline    |     ONLINE MAP PREDICTION (MapTR)
  | Topology checks    |     +-----------------------------+
  | Geometry validity  |     |  Camera input -> BEV encoder|
  +--------+-----------+     |  MapTR transformer decoder  |
           |                 |  Vectorized map output      |
  +--------v-----------+     |  (lane dividers, boundaries)|
  | Map Tile Server    |<----|  Use when HD map unavailable|
  | Versioned tiles    |     +-----------------------------+
  | Freshness SLA      |
  +--------------------+

  ACCURACY TARGETS:
  Offline HD Map:   < 10cm lateral, < 0.3m absolute (GPS-referenced)
  Online MapTR:     ~60-70% IoU (nuScenes), < 30cm lane boundary error
```
