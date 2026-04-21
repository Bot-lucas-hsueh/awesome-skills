## 8. Standard Workflow

### Phase 1 — Data Acquisition and Preprocessing

**Steps:**
1. Define area of interest (AOI) as GeoJSON polygon; reproject to WGS84 (EPSG:4326).
2. Query satellite data catalog: Copernicus Open Access Hub (Sentinel), USGS EarthExplorer (Landsat), Planet Explorer (Planet).
3. Filter by cloud cover (<10% for optical), date range, and orbit direction (ascending/descending for SAR).
4. Download and apply radiometric calibration: Sen2Cor for Sentinel-2 L1C to L2A; SNAP calibration graph for Sentinel-1 sigma-naught.
5. Apply terrain correction: Range-Doppler terrain correction with SRTM 1-arc DEM for SAR; orthorectification already applied for Sentinel-2.
6. Mosaic multiple tiles; clip to AOI; generate cloud mask using SCL band (Sentinel-2) or Fmask algorithm.

**[✓ Done]** criteria: Surface reflectance values in range [0, 1]; SAR sigma-naught in range [-30, +5] dB; cloud mask applied; spatial resolution and projection verified.
**[✗ FAIL]** criteria: DN values outside expected range — check calibration step; systematic spatial offsets >2 pixels — check DEM accuracy and co-registration.

### Phase 2 — Feature Engineering and Model Training

**Steps:**
1. Compute spectral indices: NDVI = (NIR-Red)/(NIR+Red); MNDWI = (Green-SWIR1)/(Green+SWIR1); NDBI = (SWIR1-NIR)/(SWIR1+NIR).
2. For SAR: compute VV/VH ratio, multi-temporal coherence, and dual-pol decomposition (Entropy, Alpha) using Cloude-Pottier decomposition.
3. Stack features into multi-band raster; generate patch dataset using torchgeo GeoDataset with spatial stratification.
4. Split training/validation/test using spatial blocking (minimum 500m buffer between blocks).
5. Train segmentation model: SegFormer-B3 or U-Net with ResNet-50 backbone; use weighted cross-entropy for class imbalance.
6. Monitor training: validation mIoU should improve monotonically for first 50 epochs; use early stopping on plateau.

**[✓ Done]** criteria: Validation mIoU >0.75 on held-out spatial blocks; no individual class IoU below 0.60.
**[✗ FAIL]** criteria: Validation accuracy plateauing below 0.70 — check label quality, class balance, and learning rate schedule.

### Phase 3 — Accuracy Assessment and Product Delivery

**Steps:**
1. Collect independent validation samples using stratified random sampling: minimum 50 points per class.
2. Compute confusion matrix, per-class producer/user accuracy, overall accuracy, and Kappa coefficient.
3. Generate confidence map from model softmax probabilities; mask low-confidence predictions (<0.70) as "uncertain".
4. Perform spatial error analysis: identify systematic error patterns by land cover type, slope, and cloud proximity.
5. Export final products as Cloud-Optimized GeoTIFF (COG) with EPSG:4326 and embedded metadata.
6. Document processing chain with input data dates, software versions, parameter settings, and accuracy metrics.

**[✓ Done]** criteria: Kappa >0.85; all deliverables in COG format; accuracy report with confusion matrix attached.
**[✗ FAIL]** criteria: Kappa <0.75 — return to Phase 2; identify misclassified samples and augment training data.

---
