## § 6 · Professional Toolkit

| Tool | Purpose |
|------|---------|
| **SNAP (ESA Sentinel Application Platform)** | Official SAR processing: Sentinel-1 calibration, InSAR, coherence estimation, terrain correction; supports Graph Builder for batch processing |
| **Google Earth Engine** | Cloud-scale geospatial analysis; Sentinel-2, Landsat, MODIS image collections; harmonic regression time series; global-scale ML inference |
| **rasterio** | Python raster I/O; reads/writes GeoTIFF with CRS, transforms; windowed reading for large tiles; reprojection and resampling |
| **geopandas** | Vector geospatial operations; spatial joins, buffers, zonal statistics with raster; shapefile and GeoJSON I/O |
| **torchgeo** | PyTorch-native geospatial dataset loaders; handles CRS-aware sampling, patch extraction, multi-sensor fusion for DL training |
| **GDAL/OGR** | Core raster and vector processing library; raster warping, format conversion, VRT virtual mosaics, overviews |
| **QGIS** | Desktop GIS for visualization, manual validation, and ground truth digitizing; supports Python scripting via PyQGIS |
| **PyTorch + SegFormer** | Semantic segmentation backbone; Swin-T and MiT encoders pretrained on ImageNet, fine-tuned on remote sensing datasets |
| **scikit-learn** | Traditional ML classifiers (Random Forest, SVM, Gradient Boosting) for smaller datasets; confusion matrix, Kappa calculation |
| **sen2cor** | ESA's atmospheric correction processor for Sentinel-2; converts L1C TOA to L2A Surface Reflectance |

---
