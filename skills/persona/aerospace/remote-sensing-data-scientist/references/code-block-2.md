# Code Block 2: Multi-Temporal Crop Classification & Uncertainty

## Multi-Temporal Crop Classification

```python
import torch
import torch.nn as nn
from torch.utils.data import Dataset

class TemporalCropDataset(Dataset):
    """
    Dataset for multi-temporal crop classification.
    Creates 12 monthly composites from Sentinel-2 time series.
    """
    def __init__(self, image_stack, labels, temporal_bands=[2,3,4,8,11,12]):
        """
        Args:
            image_stack: (T, C, H, W) temporal stack of Sentinel-2
            labels: (H, W) land cover labels
            temporal_bands: band indices for temporal features
        """
        self.image_stack = image_stack
        self.labels = labels
        self.temporal_bands = temporal_bands
    
    def __len__(self):
        return self.labels.max() + 1
    
    def __getitem__(self, idx):
        # Extract temporal features for class idx pixels
        class_mask = (self.labels == idx)
        
        # Monthly temporal signatures (example for 4 classes)
        temporal_features = self.image_stack[:, self.temporal_bands, :, :]
        
        return temporal_features, class_mask

class SegFormerWithLSTM(nn.Module):
    """SegFormer encoder with LSTM temporal fusion."""
    def __init__(self, encoder_name='mit_b2', num_classes=10, hidden_size=256):
        super().__init__()
        self.encoder = SegFormerEncoder(encoder_name)
        self.lstm = nn.LSTM(
            input_size=256, hidden_size=hidden_size,
            num_layers=2, batch_first=True, bidirectional=True
        )
        self.classifier = nn.Conv2d(hidden_size * 2, num_classes, 1)
    
    def forward(self, temporal_images):
        """
        Args:
            temporal_images: (B, T, C, H, W) batch of temporal image stacks
        """
        B, T, C, H, W = temporal_images.shape
        
        # Process each timestep through SegFormer
        spatial_features = []
        for t in range(T):
            feat = self.encoder(temporal_images[:, t])
            spatial_features.append(feat)
        
        # Stack and apply LSTM
        spatial_features = torch.stack(spatial_features, dim=1)  # (B, T, C, H, W)
        B, T, C, H, W = spatial_features.shape
        
        # Reshape for LSTM: (B*H*W, T, C)
        spatial_features = spatial_features.permute(0, 3, 4, 1, 2)
        spatial_features = spatial_features.reshape(B*H*W, T, C)
        
        # LSTM
        lstm_out, _ = self.lstm(spatial_features)
        
        # Use final hidden state
        temporal_features = lstm_out[:, -1, :]  # (B*H*W, hidden*2)
        
        # Reshape back to spatial
        temporal_features = temporal_features.reshape(B, H, W, -1)
        temporal_features = temporal_features.permute(0, 3, 1, 2)
        
        return self.classifier(temporal_features)
```

## Uncertainty Estimation

```python
import torch
import numpy as np

def compute_uncertainty(model, image_patches, n_mc=30):
    """
    Monte Carlo dropout for uncertainty estimation.
    
    Args:
        model: Trained model with dropout
        image_patches: Input patches (B, C, H, W)
        n_mc: Number of Monte Carlo samples
    """
    model.train()  # Enable dropout
    
    predictions = []
    with torch.no_grad():
        for _ in range(n_mc):
            pred = model(image_patches)
            predictions.append(pred)
    
    predictions = torch.stack(predictions)  # (n_mc, B, num_classes, H, W)
    
    # Mean prediction
    mean_pred = predictions.mean(dim=0)
    
    # Uncertainty as std
    uncertainty = predictions.std(dim=0)  # (B, num_classes, H, W)
    
    # Class-specific uncertainty
    predicted_class = mean_pred.argmax(dim=1)  # (B, H, W)
    
    return mean_pred, uncertainty, predicted_class

def export_with_uncertainty(predictions, uncertainty, output_path):
    """
    Export classification map with confidence scores.
    
    Args:
        predictions: (H, W) predicted class IDs
        uncertainty: (H, W) uncertainty scores
        output_path: Output GeoTIFF path
    """
    import rasterio
    from rasterio.transform import from_bounds
    
    # Low confidence mask
    low_confidence = uncertainty > 0.3  # Threshold
    
    # Create output: class + confidence
    output = np.stack([
        predictions.astype(np.uint8),
        (uncertainty * 255).astype(np.uint8),
        (low_confidence * 255).astype(np.uint8)  # Low confidence flag
    ], axis=0)
    
    with rasterio.open(output_path, 'w', ...) as dst:
        dst.write(output)
```
