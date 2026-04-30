## § 8 · Standard Workflow

### 8.1 Seismic Hazard Assessment

```
Phase 1: Source Identification
├── Identify active faults and source zones
├── Characterize earthquake recurrence ( Gutenberg-Richter)
├── Determine maximum magnitude for each source
└── Document source model uncertainty

Phase 2: Ground Motion Calculation
├── Select appropriate GMPE (accounting for site conditions)
├── Compute ground motion for all source-distance combinations
├── Apply logic tree to address model uncertainty
└── Generate hazard curves for multiple return periods

Phase 3: Risk Integration
├── Combine hazard with exposure data
├── Apply vulnerability functions by building type
├── Calculate expected losses (annualized)
└── Produce risk metrics for decision-making

Phase 4: Communication
├── Translate to non-technical audience
├── Provide actionable mitigation recommendations
└── Update as new data become available
```

### 8.2 Earthquake Early Warning Interpretation

```
When ShakeAlert issues an alert:
Step 1: Confirm alert parameters — Magnitude estimate, location, estimated shaking
Step 2: Identify lead time — Distance from epicenter determines warning seconds
Step 3: Translate to action — "Drop, Cover, Hold On" if significant shaking expected
Step 4: Communicate uncertainty — Initial alerts may underestimate magnitude
Step 5: Follow-up updates — Continue monitoring for revised alerts
```

---
