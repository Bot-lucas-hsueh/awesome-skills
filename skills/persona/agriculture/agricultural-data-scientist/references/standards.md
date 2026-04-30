## 7. Standards & Reference

### 7.1 Remote Sensing Indices

| Index | Formula | Application |
|-------|---------|-------------|
| **NDVI** | (NIR-Red)/(NIR+Red) | Vegetation health, biomass |
| **EVI** | 2.5(NIR-Red)/(NIR+6Red-7.5Blue+1) | Improved over NDVI for high biomass |
| **NDWI** | (Green-NIR)/(Green+NIR) | Water content, drought stress |
| **NDRE** | (NIR-RedEdge)/(NIR+RedEdge) | Nitrogen status, chlorophyll |

### 7.2 Model Performance Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **R² (coefficient of determination)** | 1 - SS_res/SS_tot | >0.7 for operational use |
| **RMSE** | √(mean(predicted-actual)²) | <10% of mean yield |
| **MAPE** | mean(|actual-predicted|/actual) | <15% |
| **Bias** | mean(predicted-actual) | Close to 0 |

### 7.3 Data Quality Thresholds

| Data Type | Required Completeness | Accuracy Target |
|-----------|----------------------|-----------------|
| Yield data | >95% of field | ±5% |
| Weather data | >90% of days | ±0.5°C temp, ±2mm rain |
| Satellite imagery | >80% cloud-free | Per sensor specs |
| Soil data | 1 sample per 5 ha | Standard lab accuracy |
