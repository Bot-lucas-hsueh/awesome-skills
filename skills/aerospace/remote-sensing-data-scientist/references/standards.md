## § 7 · Standards & Reference

**Key Datasets and Benchmark Metrics:**

| Dataset | Sensor | Resolution | Key Task | Target Metric |
|---------|--------|-----------|----------|---------------|
| BigEarthNet | Sentinel-1+2 | 10-60m | Multi-label classification | F1-score > 0.88 |
| SpaceNet 7 | Planet | 4m | Multi-temporal building change | F1 > 0.40 |
| DeepGlobe | Satellite | 0.5m | Road/building/land cover | mIoU > 0.72 |
| DOTA-v2 | Aerial | 0.1-1m | Object detection | mAP50 > 0.50 |
| SEN12MS | Sentinel-1+2, MODIS | 10m | LULC classification | OA > 0.85 |
| UC Merced | Aerial | 0.3m | Scene classification | Accuracy > 0.98 |

**Accuracy Standards:**

| Metric | Formula | Acceptable | Good | Excellent |
|--------|---------|-----------|------|---------|
| Overall Accuracy | Correctly classified
| Kappa Coefficient | (Po - Pe)
| mIoU (segmentation) | Mean IoU across classes | >0.65 | >0.75 | >0.85 |
| Change F1 Score | 2xPxR
| Retrieval RMSE | sqrt(sum(pred-obs)^2/n) | Context-dependent | <15% CV | <8% CV |

**Processing Standards:**

| Standard | Document | Application |
|----------|----------|-------------|
| ESA Sentinel-2 Processing | SNAP SUM | L1C to L2A atmospheric correction |
| CEOS CARD4L | CEOS-ARD | Analysis-Ready Data specifications |
| OGC GeoTIFF | OGC 19-008r4 | Raster exchange format |
| EPSG 4326

---

## Phase 1 — Data Acquisition and Preprocessing

**Steps:**
1. Define area of interest (AOI) as GeoJSON polygon; reproject to WGS84 (EPSG:4326). [✓] Done when: | [✗] FAIL if:
2. Query satellite data catalog: Copernicus Open Access Hub (Sentinel), USGS EarthExplorer (Landsat), Planet Explorer (Planet). [✓] Done when: | [✗] FAIL if:
3. Filter by cloud cover (<10% for optical), date range, and orbit direction (ascending/descending for SAR). [✓] Done when: | [✗] FAIL if:
4. Download and apply radiometric calibration: Sen2Cor for Sentinel-2 L1C to L2A; SNAP calibration graph for Sentinel-1 sigma-naught. [✓] Done when: | [✗] FAIL if:
5. Apply terrain correction: Range-Doppler terrain correction with SRTM 1-arc DEM for SAR; orthorectification already applied for Sentinel-2. [✓] Done when: | [✗] FAIL if:
6. Mosaic multiple tiles; clip to AOI; generate cloud mask using SCL band (Sentinel-2) or Fmask algorithm. [✓] Done when: | [✗] FAIL if:

**[✓ Done]** criteria: Surface reflectance values in range [0, 1]; SAR sigma-naught in range [-30, +5] dB; cloud mask applied; spatial resolution and projection verified.
**[✗ FAIL]** criteria: DN values outside expected range — check calibration step; systematic spatial offsets >2 pixels — check DEM accuracy and co-registration.

### Phase 2 — Feature Engineering and Model Training

**Steps:**
1. Compute spectral indices: NDVI = (NIR-Red)/(NIR+Red); MNDWI = (Green-SWIR1)/(Green+SWIR1); NDBI = (SWIR1-NIR)/(SWIR1+NIR). [✓] Done when: | [✗] FAIL if:
2. For SAR: compute VV/VH ratio, multi-temporal coherence, and dual-pol decomposition (Entropy, Alpha) using Cloude-Pottier decomposition. [✓] Done when: | [✗] FAIL if:
3. Stack features into multi-band raster; generate patch dataset using torchgeo GeoDataset with spatial stratification. [✓] Done when: | [✗] FAIL if:
4. Split training/validation/test using spatial blocking (minimum 500m buffer between blocks). [✓] Done when: | [✗] FAIL if:
5. Train segmentation model: SegFormer-B3 or U-Net with ResNet-50 backbone; use weighted cross-entropy for class imbalance. [✓] Done when: | [✗] FAIL if:
6. Monitor training: validation mIoU should improve monotonically for first 50 epochs; use early stopping on plateau. [✓] Done when: | [✗] FAIL if:

**[✓ Done]** criteria: Validation mIoU >0.75 on held-out spatial blocks; no individual class IoU below 0.60.
**[✗ FAIL]** criteria: Validation accuracy plateauing below 0.70 — check label quality, class balance, and learning rate schedule.

### Phase 3 — Accuracy Assessment and Product Delivery

**Steps:**
1. Collect independent validation samples using stratified random sampling: minimum 50 points per class. [✓] Done when: | [✗] FAIL if:
2. Compute confusion matrix, per-class producer/user accuracy, overall accuracy, and Kappa coefficient. [✓] Done when: | [✗] FAIL if:
3. Generate confidence map from model softmax probabilities; mask low-confidence predictions (<0.70) as "uncertain". [✓] Done when: | [✗] FAIL if:
4. Perform spatial error analysis: identify systematic error patterns by land cover type, slope, and cloud proximity. [✓] Done when: | [✗] FAIL if:
5. Export final products as Cloud-Optimized GeoTIFF (COG) with EPSG:4326 and embedded metadata. [✓] Done when: | [✗] FAIL if:
6. Document processing chain with input data dates, software versions, parameter settings, and accuracy metrics. [✓] Done when: | [✗] FAIL if:

**[✓ Done]** criteria: Kappa >0.85; all deliverables in COG format; accuracy report with confusion matrix attached.
**[✗ FAIL]** criteria: Kappa <0.75 — return to Phase 2; identify misclassified samples and augment training data.

---

