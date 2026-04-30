# Michelangelo ML Platform

## Overview

Michelangelo is Uber's end-to-end Machine Learning-as-a-Service (MLaaS) platform that enables teams across the company to build, deploy, and operate machine learning models at scale.

**Key Stats:**
- ~400 active ML projects
- 20,000+ model training jobs per month
- 5,000+ unique models in production
- 10M+ real-time predictions per second at peak

---

## Evolution

### Michelangelo 1.0 (2016-2019)
- Focus: Predictive ML for tabular data
- Primary algorithms: XGBoost, tree-based models
- Use cases: ETA prediction, pricing, risk assessment

### Michelangelo 2.0 (2019-2023)
- Re-architected for Deep Learning
- 60%+ of top-tier models now use DL
- Support for complex neural architectures

### Michelangelo 3.0 (2023-Present)
- LLM platform integration
- Generative AI support
- Advanced feature engineering

---

## Core Components

### 1. Palette Feature Store

| Attribute | Detail |
|-----------|--------|
| Features | 20,000+ shareable features |
| Computation | Batch (Spark) + Near-real-time (Samza) |
| Consistency | Unified transformation DSL |
| Retrieval | <10ms latency |

**Naming Convention:**
```
{entity}_{attribute}_{aggregation}_{window}

Examples:
- rider_avg_trips_per_week_4w
- driver_acceptance_rate_30d
- trip_distance_miles
```

### 2. Gallery (Model Registry)
- Central repository for all production models
- Model versioning and lineage tracking
- Metadata management
- Collaboration hub for data scientists

### 3. Manifold (Visual Debugging)
- Interactive model analysis
- Performance visualization
- Bias detection
- Feature importance analysis

### 4. PyML
- Python prototyping framework
- Rapid iteration environment
- Notebook integration
- Experiment tracking

### 5. Deep Learning Serving
- Triton inference server
- GPU acceleration
- <10ms latency for single predictions
- Batch prediction support

### 6. Canvas Training Framework
- Distributed training orchestration
- Auto-retraining workflows
- Hyperparameter tuning
- Model validation pipelines

### 7. LLM Platform
- Fine-tuning capabilities
- Model serving infrastructure
- Evaluation frameworks
- Support for GPT-4, Llama, custom models

---

## Model Lifecycle

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Train     │───→│   Deploy    │───→│   Serve     │
│   (Canvas)  │    │  (Gallery)  │    │(Michelangelo│
└─────────────┘    └─────────────┘    └──────┬──────┘
                                              │
                    ┌─────────────────────────┘
                    ↓
              ┌─────────────┐
              │  Monitor    │
              │ (Manifold)  │
              └──────┬──────┘
                     │
                     ↓
              ┌─────────────┐
              │  Retrain    │
              │  (Auto)     │
              └─────────────┘
```

---

## Key Use Cases

| Use Case | Model Type | Scale |
|----------|------------|-------|
| ETA Prediction | DeepETA (Neural Network) | Millions/sec |
| Dynamic Pricing | Gradient Boosting | Millions/sec |
| Demand Forecasting | Time Series (RNN) | Global cities |
| Fraud Detection | Ensemble | All transactions |
| Driver Matching | Tree-based | 30M+/min |
| Route Optimization | Graph algorithms | All trips |

---

## References

- [Meet Michelangelo: Uber's ML Platform](https://www.uber.com/blog/michelangelo-machine-learning-platform/)
- [From Predictive to Generative](https://www.uber.com/blog/generative-ai-michelangelo/)
- [DeepETA at Uber](https://www.uber.com/blog/deepeta-how-uber-predicts-arrival-times/)
