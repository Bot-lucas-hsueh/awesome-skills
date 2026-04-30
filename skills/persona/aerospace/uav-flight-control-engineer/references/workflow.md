# Standard Workflow

## 8.1 Autonomous System Development

```
Phase 1: Requirements
├── ODD definition (Operational Design Domain)
├── Safety requirements
├── Performance metrics
├── Regulation compliance
└── Fail-safe modes

Phase 2: Architecture
├── Sensor suite selection
├── Compute platform
├── Perception stack
├── Prediction and planning
├── Control systems
└── V2X (if applicable)

Phase 3: Development
├── Simulation (CARLA, LGSVL)
├── Closed-course testing
├── Public road testing
├── Shadow mode validation
└── Safety driver training

Phase 4: Validation
├── SOTIF analysis
├── Scenario-based testing
├── Statistical validation
├── Edge case coverage
└── Regulatory submission
```

## 8.2 Safety-Critical Design

1. Define fail-safe states
2. Implement redundancy
3. Monitor system health
4. Detect anomalies
5. Execute safe stop
