## § 9 · Scenario Examples

### Example 1: Marketplace Optimization — Dynamic Pricing Algorithm

**User**: "We need to design a surge pricing algorithm for a new market with high demand volatility."

**Response:**
```
UBER'S DYNAMIC SUPPLY PRICING (DSP) APPROACH

1. PROBLEM FRAMING
   Multi-objective optimization:
   • Minimize rider wait times (target: <5 min avg)
   • Maximize driver utilization (target: >70%)
   • Ensure geographic coverage (target: 95% areas served)
   • Maintain affordability (target: <2x base rate surge cap)
   
   Constraint: SUTVA violations common — treated users 
   cannibalize supply from control in undersupplied markets.

2. DATA REQUIREMENTS
   Real-time:
   • Supply: Driver positions, online status, destination mode
   • Demand: Ride requests, cancellation rates, app opens
   • External: Weather, events, traffic incidents
   
   Historical:
   • Price elasticity by geo-temporal segment
   • Cross-elasticity between neighboring regions
   • Driver response to heatmaps/surge multipliers

3. ALGORITHM DESIGN
   Prediction Layer:
   • ML models forecast demand/supply imbalance 5-15 min ahead
   • Gradient Boosting Regression: 99% accuracy for demand
   
   Optimization Layer:
   • Multi-objective optimization with constraints
   • Prices as signals to move supply BEFORE shortages occur
   
   Mechanism Design:
   • Geofenced zones with independent multipliers
   • Color-coded heatmaps: purple (surge) → red (highest)
   • Driver app: Show predicted demand in destination mode

4. PLATFORM INTEGRATION
   • Feature store: Palette for elasticity features
   • Model serving: Michelangelo online prediction (<50ms)
   • Feedback loop: Real-time driver positioning via GPS

5. VALIDATION
   • Causal inference: Switchback experiments for network effects
   • Marketplace model: Estimate incremental organic bookings (IOB)
   • Guardrails: Max price change velocity, geographic smoothing

Expected Impact: 10-20% reduction in ETAs during peak,
15-25% improvement in driver utilization.
```

---

### Example 2: Geospatial Engineering — DeepETA Architecture

**User**: "Our ETA predictions are inaccurate in dense urban environments. How would Uber's DeepETA approach help?"

**Response:**
```
DEEPETA: UBER'S PRODUCTION ETA MODEL

1. MODEL ARCHITECTURE
   • Linear transformers: O(n) complexity vs O(n²) attention
   • Embedding tables: Billions of parameters, <1% touched per prediction
   • Multi-task learning: Predicts multiple time horizons simultaneously
   • Self-attention networks: Weigh real-time factors dynamically

2. FEATURE ENGINEERING
   Route Features:
   • Distance, turn complexity, road types
   • Segment-wise traversal times from routing engine
   
   Temporal Features:
   • Time of day, day of week, holidays
   • Seasonal patterns, events
   
   Real-time Features:
   • Traffic speed, incidents, weather
   • Live GPS coordinates
   
   Geospatial Features:
   • H3 hexagon embeddings at multiple resolutions
   • Origin/destination quantized into multi-resolution grids
   • Multiple feature hashing to handle billions of locations

3. TRAINING DATA
   • 1+ billion trips for training
   • 100+ million parameters
   • Continuous retraining on recent trips via Canvas framework

4. SERVING OPTIMIZATION
   • Michelangelo Triton inference server
   • GPU acceleration for batch predictions
   • Sub-10ms latency for single prediction
   • Hybrid approach: Physical routing engine + ML residual prediction

5. ACCURACY IMPROVEMENTS
   • 15-30% error reduction vs XGBoost predecessor
   • Better edge cases: Unusual routes, extreme traffic
   • Confidence intervals for uncertainty quantification
   • Asymmetric Huber loss: Control underprediction vs overprediction cost

Key Insight: Deep learning excels at Uber's data scale.
Simpler models may suffice for smaller datasets.
```

---

### Example 3: ML Platform — Feature Store Design (Palette)

**User**: "We're building a feature store. What lessons from Michelangelo's Palette should we apply?"

**Response:**
```
PALETTE FEATURE STORE PRINCIPLES

1. ORGANIZATION
   • 20,000+ features organized by domain and use case
   • Naming convention: {entity}_{attribute}_{aggregation}_{window}
     Example: rider_avg_trips_per_week_4w
   • Clear ownership: Feature owners for quality and documentation

2. COMPUTATION MODES
   Batch:
   • Spark jobs for historical training data
   • Full backfills, point-in-time correctness
   
   Near-Real-Time:
   • Samza streaming for online features
   • Kafka for event ingestion
   • Feature updates within seconds
   
   Consistency:
   • Same transformation logic in both paths
   • Unified DSL prevents training-serving skew

3. SHARING MECHANISM
   Discovery:
   • Searchable catalog with lineage tracking
   • Feature documentation and examples
   
   Reuse:
   • Features shared across Mobility, Delivery, Freight
   • Standardized entities: rider, driver, trip, order
   
   Quality:
   • Automated validation on new features
   • Drift detection and alerting
   • Freshness checks for streaming features

4. INTEGRATION POINTS
   Training:
   • Direct connection to Michelangelo training pipelines
   • Point-in-time joins for historical features
   
   Serving:
   • Low-latency (<10ms) feature retrieval
   • Batch fetch for multiple entities
   
   Monitoring:
   • Feature drift alerts
   • Coverage and null rate tracking

5. GOVERNANCE
   Tiering:
   • Critical features: Higher SLAs, 99.99% availability
   • Experimental features: Lower SLAs, faster iteration
   
   Deprecation:
   • Lifecycle management for obsolete features
   • Usage analytics identify candidates
   
   Privacy:
   • PII handling per GDPR/CCPA
   • Access controls and audit logging

Anti-pattern: Each team building their own features
without sharing → leads to duplication and inconsistency.
```

---

### Example 4: Matching Optimization — Batch vs. Greedy

**User**: "Our current matching assigns the nearest driver to each request. Why is this suboptimal?"

**Response:**
```
WHY GREEDY MATCHING FAILS

GREEDY APPROACH (Suboptimal):
- Assign closest available driver to each incoming request
- Ignores global efficiency
- Example: Driver A is slightly closer to Rider 1, 
  but Driver B is MUCH closer to Rider 2.
  Greedy assigns A→1, leaving 2 with long wait.

UBER'S BATCH MATCHING (Optimal):
- Collect requests over small time window (2-5 seconds)
- Formulate as weighted bipartite matching problem
- Solve using Hungarian algorithm or approximation
- Objective: Minimize total wait time across ALL riders

IMPLEMENTATION:

1. Graph Construction
   Nodes: Riders (R) and Drivers (D)
   Edges: E(r,d) = predicted wait time + ETA uncertainty
   Weights: Combination of distance, ETA, driver rating

2. Constraints
   • Driver capacity (can only take 1 trip at a time)
   • Rider preferences (vehicle type, shared/pool)
   • Service tier matching (UberX, Black, etc.)
   • Destination mode (drivers heading home)

3. Optimization
   • Hungarian algorithm: O(n³) for exact solution
   • Approximation algorithms for large markets
   • Distributed matching for geographic sharding
   • Re-optimize as new information arrives

4. Handling Uber Pool
   • Multi-rider, multi-stop optimization
   • Sequence pickups and drop-offs efficiently
   • Balance cost savings vs. trip time extension

BUSINESS IMPACT:
• 10-15% reduction in average wait times
• Better driver utilization (fewer idle minutes)
• Improved marketplace liquidity in sparse areas
• Higher completion rates (fewer cancellations)

SCALING CHALLENGES:
• Computational complexity for large markets
• Real-time requirements (decisions in <100ms)
• Driver position updates every 2-4 seconds
• Handling rider/driver dropouts during batch window
```

---

### Example 5: Microservices Boundaries & Domain Design

**User**: "We're splitting our monolith. How does Uber define service boundaries?"

**Response:**
```
UBER'S MICROSERVICES APPROACH (Domain-Driven Design)

1. DOMAIN BOUNDARIES
   
   Mobility Domain:
   • Ride request, matching, pricing, trip execution
   • ETA calculation, route optimization
   • Driver status, earnings
   
   Delivery Domain:
   • Restaurant/merchant search
   • Order management, preparation time estimation
   • Courier matching, delivery tracking
   
   Freight Domain:
   • Shipper/carrier matching
   • Load tracking, freight pricing
   • Carrier onboarding, document management
   
   Platform Domain:
   • Identity, authentication
   • Payments, fraud detection
   • Notifications, communications
   • Maps, geocoding

2. SERVICE OWNERSHIP PRINCIPLES
   • "You build it, you run it" — DevOps culture
   • Single team owns service end-to-end
   • API contracts: Versioned, documented, backward-compatible
   • Clear SLAs defined per service tier

3. PLATFORM SHARING (75% of Engineering)
   • Common services: Identity, payments, fraud
   • Shared ML: Michelangelo serves all business lines
   • Shared data infrastructure: Kafka, Hadoop, Pinot
   • Shared experimentation: XP platform

4. COMMUNICATION PATTERNS
   Synchronous:
   • gRPC for internal service calls
   • <100ms timeout for critical paths
   • Circuit breakers for cascading failure prevention
   
   Asynchronous:
   • Kafka for event-driven architecture
   • Eventual consistency for non-critical operations
   • Avoid distributed transactions

5. DATA ISOLATION
   • Each service owns its data
   • No direct database access across services
   • Event sourcing for cross-domain data needs
   • CQRS for read-heavy operations

6. SCALE CONSIDERATIONS
   • Stateless services for horizontal scaling
   • Caching: Redis for hot data, CDN for static assets
   • Database sharding by geography
   • Read replicas for query-heavy services

Anti-pattern: Creating too many nano-services
→ operational overhead exceeds benefits.

Target: 10-50 engineers per service domain.
```

---
