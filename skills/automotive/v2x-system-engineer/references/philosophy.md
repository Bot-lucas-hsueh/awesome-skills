## § 4 Core Philosophy

### Mental Model: V2X Safety Message Lifecycle

```
VEHICLE A (Ego)              VEHICLE B (Remote)
┌────────────────────┐       ┌──────────────────────┐
│  Generate BSM      │       │  Receive BSM          │
│  (GPS + IMU data)  │       │  (Authentication OK?) │
│  Sign with cert    │──────►│  Validate position    │
│  10 Hz broadcast   │       │  Fuse with local data │
└────────────────────┘       │  Assess threat        │
                             │  Trigger warning (if  │
                             │  TTC < threshold)     │
                             └──────────────────────┘

End-to-End Latency Budget (SAE J2945/1 requirement: < 100 ms):
  GPS measurement latency:    20 ms
  BSM generation:             5 ms
  MAC/PHY transmission:       10 ms
  RF propagation:             0.1 ms (negligible)
  Reception + parsing:        5 ms
  Authentication:             3 ms
  Application processing:     10 ms
  Total nominal:              53 ms  ✓ (<<100ms requirement)
  3-sigma worst case:         ~80 ms ✓
```

### Guiding Principles

1. **Direct Communication for Safety, Network for Convenience**: Safety-critical V2X applications (PCW, EEBL, LTA) must use direct radio communication (DSRC or C-V2X PC5) to meet <100ms latency; value-added services (parking, fuel, traffic management) can use V2N
2. **Message Authenticity is Non-Negotiable**: Unauthenticated V2X messages cannot be used for safety decisions; IEEE 1609.2 ECDSA P-256 authentication is mandatory for all safety applications in public deployments
3. **Cooperative Perception Multiplies Sensor Range**: A properly designed CPM system extends effective sensor range from ~200m to 400-500m (via relay through vehicles ahead); this is the highest-value V2X application for autonomous driving systems

---

