## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| Atmospheric contamination | 🔴 Critical | Processing without atmospheric correction (using TOA instead of SR) inflates spectral indices and causes systematic classification bias, particularly for NDVI in hazy conditions | Always apply Sen2Cor for Sentinel-2 or LEDAPS for Landsat; verify with pseudo-invariant calibration sites |
| Training data temporal mismatch | 🔴 Critical | Labels collected in one season applied to imagery from a different phenological stage cause systematic misclassification of croplands and deciduous forests | Use multi-temporal feature stacks; stratify training data across seasons; validate with temporally independent test sets |
| SAR layover and shadow artifacts | 🟡 High | Mountainous terrain creates geometric distortions (layover, foreshortening, shadow) in SAR imagery that appear as spurious land cover change | Apply terrain correction with local incidence angle mask; exclude slopes >30° from quantitative analysis |
| Spatial autocorrelation in validation | 🟡 High | Using spatially adjacent pixels in train/test split inflates accuracy metrics due to spatial autocorrelation; true accuracy is often 10-20% lower | Use spatial blocking for train/test split; minimum separation of 500m between train and test polygons |
| Geographic domain shift | 🟡 High | Models trained in one ecoregion (temperate forest) fail when applied to similar classes in another ecoregion (tropical forest) | Test transfer learning performance across ecoregions before operational deployment; consider continual learning |
| Change detection false positive rate | 🟢 Medium | Bidirectional reflectance distribution function (BRDF) effects between acquisitions at different solar angles masquerade as surface change | Use BRDF-normalized reflectance (NBAR products) for multi-temporal analysis; restrict to nadir-looking acquisitions |

---
