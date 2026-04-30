# DeepETA: ETA Prediction at Uber

## Abstract

DeepETA is Uber's deep learning-based system for predicting Estimated Time of Arrival (ETA). It uses neural networks to predict the residual between routing engine estimates and real-world observed outcomes, achieving 15-30% error reduction compared to previous XGBoost models.

---

## Problem Statement

### Limitations of Traditional Routing Engines

Traditional routing engines:
- Divide road network into weighted graph segments
- Use shortest-path algorithms (Dijkstra, A*)
- Cannot perfectly capture real-world conditions
- Don't account for route choice variability

### Hybrid Approach

```
┌─────────────────────────────────────────────────────────────┐
│                    ETA CALCULATION                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐     ┌─────────────────┐               │
│  │  Routing Engine │     │   DeepETA ML    │               │
│  │  (Physical      │  +  │   (Residual     │               │
│  │   Model)        │     │   Prediction)   │               │
│  │                 │     │                 │               │
│  │ • Map data      │     │ • Historical    │               │
│  │ • Real-time     │     │   trip data     │               │
│  │   traffic       │     │ • Spatial       │               │
│  │ • Segment-wise  │     │   features      │               │
│  │   times         │     │ • Temporal      │               │
│  │                 │     │   features      │               │
│  └────────┬────────┘     └────────┬────────┘               │
│           │                       │                         │
│           └───────────┬───────────┘                         │
│                       ↓                                     │
│              ┌─────────────────┐                           │
│              │  Final ETA      │                           │
│              │  Prediction     │                           │
│              └─────────────────┘                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Model Architecture

### Key Components

| Component | Description |
|-----------|-------------|
| **Embedding Layers** | Encode categorical features (location, time) |
| **Linear Transformers** | O(n) complexity vs O(n²) for standard attention |
| **Bias Adjustment Decoder** | Adjust predictions for different segments |
| **Multi-Task Learning** | Predict multiple time horizons |

### Feature Encoding

#### Geospatial Embeddings

Locations quantized into multi-resolution grids:

| Resolution | Cell Size | Use Case |
|------------|-----------|----------|
| Low | 1-10 km | City-level patterns |
| Medium | 100m-1km | Neighborhood patterns |
| High | 10-100m | Street-level patterns |

**Hashing Strategy:**
- Multiple feature hashing with independent hash functions
- Reduces collision impact vs single hashing
- Balances memory usage vs accuracy

### Feature Categories

| Category | Examples |
|----------|----------|
| **Route** | Distance, turn complexity, road types |
| **Temporal** | Hour, day of week, holidays, events |
| **Real-time** | Traffic speed, incidents, weather |
| **Geospatial** | H3 hexagon embeddings, origin/destination |
| **Trip Context** | Service type (X, Black, Pool), city |

---

## Training

### Dataset

| Attribute | Scale |
|-----------|-------|
| Training examples | 1+ billion trips |
| Model parameters | 100+ million |
| Retraining frequency | Continuous (online learning) |

### Loss Function: Asymmetric Huber Loss

**Purpose:** Control relative cost of underprediction vs overprediction

**Parameters:**
- `delta`: Controls robustness to outliers
- `omega`: Controls asymmetry (under vs over prediction cost)

```python
# Conceptual form
if |error| <= delta:
    loss = 0.5 * error²
else:
    loss = delta * (|error| - 0.5 * delta)

# Weighted by omega for asymmetry
```

### Business-Specific Configurations

| Use Case | Target | Asymmetry |
|----------|--------|-----------|
| Fare calculation | Mean | Balanced |
| Pickup ETA | Conservative | Penalize underprediction |
| Delivery ETA | Aggressive | Allow underprediction |

---

## Serving Architecture

### Latency Requirements

| Component | Target |
|-----------|--------|
| Routing engine | <50ms |
| DeepETA prediction | <10ms |
| Total ETA request | <100ms p99 |

### Infrastructure

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   User      │────→│   uRoute    │────→│   Routing   │
│   Request   │     │   Service   │     │   Engine    │
└─────────────┘     └──────┬──────┘     └──────┬──────┘
                           │                   │
                           │                   │
                           │            ┌──────┴──────┐
                           │            │  Base ETA   │
                           │            │  Prediction │
                           │            └──────┬──────┘
                           │                   │
                           │     ┌─────────────┘
                           │     │
                           │     ↓
                           │ ┌─────────────────────────┐
                           └→│   Michelangelo Online   │
                             │   Prediction Service    │
                             │                         │
                             │ • Feature retrieval     │
                             │ • Model inference       │
                             │ • Residual prediction   │
                             └───────────┬─────────────┘
                                         │
                                         ↓
                              ┌──────────────────────┐
                              │    Final ETA =       │
                              │    Base + Residual   │
                              └──────────────────────┘
```

### Hardware

| Component | Specification |
|-----------|--------------|
| Inference | GPU (NVIDIA T4/A10) |
| Feature store | Redis/Memcached cluster |
| Model serving | Triton Inference Server |

---

## Performance

### Accuracy Improvements

| Metric | XGBoost | DeepETA | Improvement |
|--------|---------|---------|-------------|
| Mean Absolute Error | Baseline | -15-30% | Significant |
| Tail accuracy (p95) | Baseline | -20-35% | Major |
| Edge cases | Poor | Good | Critical |

### Handling Edge Cases

| Scenario | DeepETA Advantage |
|----------|-------------------|
| Unusual routes | Learns from similar historical patterns |
| Extreme traffic | Real-time feature adaptation |
| Complex intersections | Spatial embedding captures complexity |
| Construction zones | Incident feature integration |

---

## Production Challenges

### 1. Feature Consistency
- Training-serving skew prevention via Palette
- Point-in-time correctness for historical features
- Real-time feature freshness monitoring

### 2. Model Updates
- Continuous retraining pipeline
- A/B testing for model versions
- Rollback mechanisms

### 3. Global Deployment
- Regional model variants
- City-specific fine-tuning
- Fallback strategies

---

## References

- [DeepETA Blog Post](https://www.uber.com/blog/deepeta-how-uber-predicts-arrival-times/)
- [DeepETA Research Paper](https://arxiv.org/abs/2202.02124)
- [Engineering Reliable Transportation with ML](https://www.uber.com/blog/machine-learning/)
