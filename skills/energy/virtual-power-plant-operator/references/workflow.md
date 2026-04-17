## § 8 · Standard Workflow

### 8.1 Day-Ahead Market Bidding

```
Phase 1: Forecast Analysis
├── Retrieve 24-hour load forecast
├── Retrieve 24-hour renewable generation forecast
├── Retrieve day-ahead market prices
└── [✓ Done]: Forecast data assembled

Phase 2: Optimization
├── Run dispatch optimization model
├── Apply grid constraints
├── Apply DER operational constraints
└── [✓ Done]: Optimal dispatch determined

Phase 3: Bidding
├── Submit hourly energy bids to ISO
├── Submit capacity offers if participating in capacity market
├── Submit ancillary service offers
└── [✓ Done]: Market bids submitted

Phase 4: Review
├── Review accepted bids
├── Calculate expected revenue
├── Identify real-time exposure
└── [✓ Done]: Bidding complete
```

### 8.2 Demand Response Event Execution

```
Step 1: Receive Signal
  → Receive dispatch signal from ISO/utility or internal trigger

Step 2: Assess Capability
  → Verify available DR capacity
  → Check participant availability
  → Calculate expected load reduction

Step 3: Execute Dispatch
  → Send OpenADR signals to enrolled endpoints
  → Activate behind-the-meter resources
  → Monitor actual response

Step 4: Verify and Report
  → Compare actual vs. committed reduction
  → Report performance to ISO/utility
  → Calculate settlement
```

---
