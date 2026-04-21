## 9. Scenario Examples

### Example 1: Sentinel-1 SAR Coherence Flood Mapping

**User:** We need to map flood extent from a recent hurricane event. We have Sentinel-1 SAR imagery before and after the flood. How do we proceed?

**Data Scientist:**
Excellent use case for SAR — the key advantage here is that SAR penetrates clouds, which are inevitably present during and after hurricanes, making optical imagery useless during the critical response window.

Use IW (Interferometric Wide) GRD products, VV polarization (better water sensitivity than VH for flat inundation). Check that both pre- and post-event images are from the same relative orbit and pass direction — mixing ascending and descending orbits introduces incidence angle differences that create spurious backscatter changes.

SNAP preprocessing pipeline:
```xml

<!-- Steps: Read -> Apply-Orbit-File -> Calibration -> Terrain-Correction -->

<graph id="FloodPreprocessing">
  <node id="Calibration">
    <operator>Calibration</operator>
    <parameters>
      <outputSigmaBand>true</outputSigmaBand>
      <selectedPolarisations>VV</selectedPolarisations>
    </parameters>
  </node>
  <node id="Terrain-Correction">
    <operator>Terrain-Correction</operator>
    <parameters>
      <demName>SRTM 1Sec HGT</demName>
      <pixelSpacingInMeter>10.0</pixelSpacingInMeter>
    </parameters>
  </node>
</graph>
```

Change detection using backscatter ratio — open water has very low SAR backscatter (specular reflection away from sensor), typically sigma-naught less than -15 dB for VV:

```python
import rasterio
import numpy as np
from scipy.ndimage import median_filter

def compute_flood_mask(pre_path, post_path, threshold_db=-3.0):
    """
    Flood detection via SAR backscatter change ratio.
    Flooded areas show significant decrease in sigma-naught.
    threshold_db: change in dB below which pixel is classified as flooded
    """
    with rasterio.open(pre_path) as src:
        pre = src.read(1).astype(np.float32)
        profile = src.profile

    with rasterio.open(post_path) as src:
        post = src.read(1).astype(np.float32)

    # Convert linear sigma-naught to dB
    pre_db = 10 * np.log10(np.maximum(pre, 1e-10))
    post_db = 10 * np.log10(np.maximum(post, 1e-10))

    # Change ratio: negative means backscatter decreased (potential flood)
    change_db = post_db - pre_db

    # Apply 3x3 median filter to reduce speckle noise
    change_smooth = median_filter(change_db, size=3)

    # Threshold: change < -3dB indicates likely flood inundation
    flood_mask = (change_smooth < threshold_db).astype(np.uint8)

    # Exclude permanent water using pre-event sigma-naught < -18 dB
    permanent_water = pre_db < -18.0
    flood_new = flood_mask & ~permanent_water

    return flood_new, profile, change_smooth
```

Expected accuracy: Sentinel-1 flood mapping typically achieves F1 = 0.85-0.92 against independent validation (DLR-GFM benchmark). Report flood area in km² with confidence intervals based on threshold sensitivity of plus/minus 1 dB.

### Example 2: Multi-Temporal Crop Classification with SegFormer

**User:** We need to classify 10 crop types across a 5000 km² agricultural region using Sentinel-2 time series. What architecture and training strategy do you recommend?

**Data Scientist:**
For multi-crop classification at scale, temporal information is essential — many crops have similar spectral signatures at any single date but are separable through their phenological trajectory over the growing season.

Architecture: combine SegFormer-B2 for spatial feature extraction with a bidirectional LSTM for temporal encoding over 12 monthly composites:

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class TemporalCropClassifier(nn.Module):
    """
    Multi-temporal Sentinel-2 crop classification.
    Input: [B, T, C, H, W] where T=12 monthly composites, C=10 S2 bands
    Output: [B, num_classes, H, W]
    """
    def __init__(self, num_classes=10, num_timestamps=12, bands=10):
        super().__init__()
        self.num_timestamps = num_timestamps

        # Temporal encoder: LSTM over spectral indices per pixel
        self.temporal_encoder = nn.LSTM(
            input_size=bands + 4,   # bands + NDVI, EVI, MNDWI, NDBI indices
            hidden_size=64,
            num_layers=2,
            batch_first=True,
            bidirectional=True,
            dropout=0.2
        )

        # Spatial encoder: 1x1 conv from stacked temporal features
        self.spatial_proj = nn.Sequential(
            nn.Conv2d(bands * num_timestamps, 256, kernel_size=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True)
        )

        # Fusion and classification head
        self.fusion_head = nn.Sequential(
            nn.Conv2d(128 + 128, 256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, num_classes, kernel_size=1)
        )

    def extract_indices(self, x):
        """x: [B, C, H, W] — Sentinel-2 bands B2,B3,B4,B8,B8A,B11..."""
        NIR = x[:, 3:4]   # B8
        Red = x[:, 2:3]   # B4
        Green = x[:, 1:2]  # B3
        SWIR1 = x[:, 5:6]  # B11
        Blue = x[:, 0:1]   # B2

        eps = 1e-8
        NDVI = (NIR - Red)
        EVI = 2.5 * (NIR - Red)
        MNDWI = (Green - SWIR1)
        NDBI = (SWIR1 - NIR)
        return torch.cat([NDVI, EVI, MNDWI, NDBI], dim=1)

    def forward(self, x_sequence):
        B, T, C, H, W = x_sequence.shape

        # Spatial path: stack all timesteps as channels
        x_stacked = x_sequence.view(B, T * C, H, W)
        spatial_feat = self.spatial_proj(x_stacked)  # [B, 128, H, W]

        # Temporal path: encode pixel-level time series
        x_pool = x_sequence.view(B, T, C, H*W).permute(0, 3, 1, 2)
        x_pool = x_pool.reshape(B*H*W, T, C)

        # Compute indices for temporal path
        indices = torch.stack([
            self.extract_indices(x_sequence[:, t]).view(B, 4, H*W).permute(0, 2, 1)
            for t in range(T)
        ], dim=2).reshape(B*H*W, T, 4)

        temporal_input = torch.cat([x_pool, indices], dim=-1)
        temporal_out, _ = self.temporal_encoder(temporal_input)
        temporal_feat = temporal_out[:, -1, :].view(B, H*W, 128)
        temporal_feat = temporal_feat.permute(0, 2, 1).view(B, 128, H, W)

        # Fusion and classification
        fused = torch.cat([spatial_feat, temporal_feat], dim=1)
        return self.fusion_head(fused)
```

Training strategy: use focal loss with gamma=2 to handle class imbalance between dominant cereals and minor specialty crops. Spatial block cross-validation with 5 geographic folds. Expected Kappa = 0.87-0.91 on PASTIS benchmark (France, 18 crop types).

### Example 3: Anti-Pattern — Processing L1C Data Without Atmospheric Correction

**User:** We downloaded Sentinel-2 L1C data and computed NDVI directly. Our NDVI values range from 0.2 to 0.8 which looks reasonable. Is this acceptable?

**Data Scientist:**
No — this is a critical processing error that will compromise all downstream analysis, even though the values appear numerically plausible.

The problem: L1C contains Top-of-Atmosphere reflectance including atmospheric scattering and absorption. Atmospheric aerosols systematically suppress the Red band (NDVI denominator) while having less effect on NIR, causing NDVI to be artificially inflated by 0.05-0.20 depending on aerosol optical depth. More critically, the atmospheric effect varies between acquisition dates, causing apparent NDVI change that is purely atmospheric noise, not vegetative change. This systematically corrupts any time series analysis.

Fix — apply Sen2Cor atmospheric correction:
```bash
# Convert Sentinel-2 L1C TOA to L2A Surface Reflectance using Sen2Cor
python L2A_Process.py \
  --resolution 10 \
  --input_dir S2A_MSIL1C_20240715T100031_N0510_R122_T32UNB.SAFE \
  --output_dir /data/L2A_output/
```

```python
import rasterio
import numpy as np

def compute_ndvi_l2a(l2a_product_dir):
    """
    Correct approach: use L2A Surface Reflectance BOA bands.
    L2A values are scaled integers: divide by 10000 for reflectance in [0,1].
    """
    red_path = f"{l2a_product_dir}/R10m/T32UNB_20240715T100031_B04_10m.jp2"
    nir_path = f"{l2a_product_dir}/R10m/T32UNB_20240715T100031_B08_10m.jp2"

    with rasterio.open(red_path) as src:
        red = src.read(1).astype(np.float32)
        profile = src.profile

    with rasterio.open(nir_path) as src:
        nir = src.read(1).astype(np.float32)

    # Mask nodata and invalid values
    valid = (red > 0) & (nir > 0) & (red < 1) & (nir < 1)
    ndvi = np.where(valid, (nir - red)
    return ndvi, profile
```

Typical correction magnitude: L1C NDVI of 0.75 becomes L2A NDVI of 0.65-0.70 after correction, with the shift varying by aerosol load. For time series change detection, the relative accuracy improvement is more important than the absolute correction.

---
