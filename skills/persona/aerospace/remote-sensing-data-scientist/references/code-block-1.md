# Code Block 1: Sentinel-1 SAR Flood Mapping & Spatial CV

## Sentinel-1 SAR Flood Mapping

```python
import numpy as np

def flood_detection(pre_event, post_event, threshold_ratio=0.5):
    """
    Detect flood extent using pre/post Sentinel-1 SAR backscatter ratio.
    
    Args:
        pre_event: Pre-event sigma-naught in dB
        post_event: Post-event sigma-naught in dB
        threshold_ratio: Backscatter ratio threshold (default: 0.5 = -3dB)
    """
    # Convert dB to linear
    pre_linear = 10 ** (pre_event / 10)
    post_linear = 10 ** (post_event / 10)
    
    # Backscatter ratio
    ratio = post_linear / pre_linear
    
    # Flood mask: significant decrease in backscatter
    # Open water has very low SAR backscatter (specular reflection)
    flood_mask = ratio < threshold_ratio
    
    # Filter by absolute post-event level
    # Water typically < -15 dB for VV polarization
    water_threshold = -15  # dB
    flood_mask = flood_mask & (post_event < water_threshold)
    
    return flood_mask, ratio

def compute_flood_area(flood_mask, pixel_spacing_m=10):
    """Compute flood extent in km²."""
    flood_pixels = np.sum(flood_mask)
    pixel_area_m2 = pixel_spacing_m ** 2
    flood_area_km2 = (flood_pixels * pixel_area_m2) / 1e6
    return flood_area_km2
```

## Spatial Cross-Validation

```python
from sklearn.model_selection import GroupKFold
import geopandas as gpd

def spatial_cv_split(gdf, n_splits=5):
    """
    Spatially blocked cross-validation for geospatial ML.
    
    CRITICAL: Use spatial blocking, not random splitting!
    Random splitting inflates accuracy by 10-20% due to spatial autocorrelation.
    """
    # Create spatial blocks using grid
    gdf['block_id'] = (
        (gdf.geometry.centroid.x // 10000).astype(int) * 10000 +
        (gdf.geometry.centroid.y // 10000).astype(int)
    )
    
    gkf = GroupKFold(n_splits=n_splits)
    for train_idx, test_idx in gkf.split(gdf, groups=gdf['block_id']):
        yield train_idx, test_idx

# Usage
for train_idx, test_idx in spatial_cv_split(labels_gdf):
    model.fit(features[train_idx], labels[train_idx])
    predictions = model.predict(features[test_idx])
    accuracy = compute_accuracy(predictions, labels[test_idx])
    print(f"Fold accuracy: {accuracy:.3f}")  # Expect lower than random split
```

## Spatial Block Cross-Validation

```python
import numpy as np
from sklearn.model_selection import KFold

def spatial_block_cv(raster, labels, block_size=100, n_folds=5):
    """
    Spatial block cross-validation for raster classification.
    
    Creates spatial blocks to prevent data leakage from adjacent pixels.
    """
    h, w = raster.shape[:2]
    n_blocks_h = h // block_size
    n_blocks_w = w // block_size
    
    # Create block grid
    blocks = []
    for i in range(n_blocks_h):
        for j in range(n_blocks_w):
            row_start, row_end = i * block_size, (i + 1) * block_size
            col_start, col_end = j * block_size, (j + 1) * block_size
            blocks.append((i, j, row_start, row_end, col_start, col_end))
    
    # Spatial fold assignment
    np.random.seed(42)
    block_indices = np.arange(len(blocks))
    np.random.shuffle(block_indices)
    fold_sizes = len(blocks) // n_folds
    
    kf = KFold(n_splits=n_folds)
    for fold_idx, (train_idx, test_idx) in enumerate(kf.split(block_indices)):
        train_blocks = [blocks[i] for i in train_idx]
        test_blocks = [blocks[i] for i in test_idx]
        yield train_blocks, test_blocks
```
