## § 5 · Decision Frameworks

### Aircraft Sizing Methodology

```
Step 1: Define Mission Profile
├── Segments: taxi, takeoff, climb, cruise, descent, landing
├── Payload: passengers × 95kg + cargo
├── Reserve: 45 min hold + 200 nm divert
└── Fuel fraction by segment

Step 2: Estimate Takeoff Weight
├── WTO = WPAYLOAD + WFUEL + WEMPTY
├── Solve iteratively: WTO affects L/D, SFC, structure
└── Convergence: ΔWTO < 0.1%

Step 3: Select Design Point
├── W/S vs T/W trade space
├── Constraint lines: takeoff, climb, cruise, landing
└── Optimize for minimum DOC or maximum payload-range
```

### Configuration Trade Process

| Configuration | Pros | Cons | Applications |
|---------------|------|------|--------------|
| Low Wing | Easy gear, good ditching | Limited prop clearance | Transport jets |
| High Wing | Ground clearance, cargo | Heavy landing gear | Regional, cargo |
| T-tail | Clean flow, deep stall risk | Heavy, flutter | Business jets |
| Conventional | Simple, light | Interference drag | Most aircraft |

📄 **Full Details**: [references/09-decision-frameworks.md](references/09-decision-frameworks.md)

---
