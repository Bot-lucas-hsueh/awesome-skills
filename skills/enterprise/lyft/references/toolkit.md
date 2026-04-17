## § 6 · Professional Toolkit

### 6.1 Core Frameworks

| Framework | Application | Threshold |
|-----------|-------------|-----------|
| **Dynamic Pricing** | Balance supply-demand with driver earnings focus | <100ms latency for price calculation |
| **Batch Matching** | Globally optimize driver-rider pairs for earnings + wait time | Sub-second matching decisions |
| **Recommendation Engine** | LightGBM with lambda rank for mode selection | <50ms for personalized ranking |
| **Driver Heat Maps** | Predict demand to guide driver positioning | Real-time updates every 2 minutes |

### 6.2 Machine Learning Components

| Component | Purpose | Scale |
|-----------|---------|-------|
| **Recommendation Model** | LightGBM with lambda rank + multi-class classification | Millions of predictions/day |
| **Pricing Elasticity** | Predict demand response to price changes | City-level models |
| **ETA Prediction** | Route-based arrival time estimation | Billions of trips/year training data |
| **Fraud Detection** | Payment and trust/safety ML | Real-time scoring |

### 6.3 Driver Tools

| Tool | Purpose | Target |
|------|---------|--------|
| **Earnings Estimator** | Predict hourly earnings by time/location | Accurate within 15% |
| **Heat Map** | Show high-demand areas | Updated every 2 minutes |
| **Destination Mode** | Filter rides toward driver destination | 20% of driver usage |
| **Express Drive** | Vehicle rental program for drivers | 10,000+ vehicles in fleet |

---
