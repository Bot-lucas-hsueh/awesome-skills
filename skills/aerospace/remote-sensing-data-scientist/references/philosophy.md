## § 4 · Core Philosophy

```
         REMOTE SENSING DATA SCIENCE MENTAL MODEL
         ==========================================

  Raw Satellite Data              Feature Engineering              Decision Output
  +------------------+           +-------------------+           +------------------+
  | Sentinel-1 SAR   |--Calib.-->| σ° backscatter    |           | Land Cover Map   |
  | Sentinel-2 MSI   |--Sen2Cor->| NDVI, EVI, NDWI   |--Model--->| Change Detection |
  | Landsat-8/9 OLI  |--LEDAPS-->| Texture features  |           | Biomass Estimate |
  | Planet SuperDove |--TOAR---->| SAR coherence     |           | Flood Extent     |
  +------------------+           +-------------------+           +------------------+
          |                               |                              |
          v                               v                              v
  Data Quality Gates              Algorithm Selection            Accuracy Validation
  - Cloud cover %                 - Supervised classif.          - Kappa coefficient
  - SAR coherence                 - Change detection             - mIoU per class
  - Radiometric stability         - Regression retrieval         - F1 score change
  - Geometric accuracy            - Geospatial DL               - RMSE retrieval

  SPATIAL SCALE PYRAMID:
       ^  Field validation (cm-m, UAV/field survey)
      ^^  Very high resolution (0.5-3m, Planet, WorldView)
     ^^^  High resolution (10m, Sentinel-2, Planet)
    ^^^^  Medium resolution (30m, Landsat)
   ^^^^^  Coarse resolution (250m-1km, MODIS, VIIRS)
```

**Guiding Principles:**

1. **Physics Before Statistics** — radiometric calibration and atmospheric correction are non-negotiable preprocessing steps, not optional enhancements. A statistically sophisticated model built on uncalibrated data is scientifically meaningless. Ground every feature in physical units (reflectance, sigma-naught in dB, surface temperature in Kelvin) before any ML step.

2. **Spatial Integrity in Validation** — accuracy assessment must respect spatial autocorrelation. Random pixel-level train/test splits yield optimistic accuracy due to spectral similarity of neighboring pixels. Always use spatially blocked cross-validation with a minimum distance buffer between training and validation polygons, and report the spatial blocking configuration explicitly.

3. **Change vs. Noise is the Central Challenge** — every change detection algorithm must explicitly account for sensor noise, phenological variation, and atmospheric variability before flagging surface change. The signal-to-noise ratio for real land cover change is often less than 10% above seasonal background variation. Multi-temporal compositing, radiometric normalization, and careful threshold calibration are required for production-grade systems.

---

