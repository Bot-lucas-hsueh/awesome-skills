## § 10 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Relying on V2N for Safety Applications
**❌ BAD**: Using cellular network (V2N) for collision warning or intersection safety because it's simpler to deploy
**✅ GOOD**: Measure actual latency before assuming V2N is sufficient:
```python
# V2N latency breakdown (typical 4G/5G network):
cellular_latency = {
    "app_to_stack": 5,       # ms
    "LTE_uplink": 15,        # ms (including scheduling delay)
    "backhaul": 5,           # ms
    "cloud_processing": 20,  # ms (if safety server in cloud)
    "backhaul_return": 5,    # ms
    "LTE_downlink": 15,      # ms
    "stack_to_app": 5,       # ms
    "total": 70,             # ms (nominally OK)
    "95th_percentile": 150,  # ms (violates SAE J2945 < 100ms)
}
# V2N cannot guarantee <100ms 95th percentile latency → not suitable for safety
```

---

### Anti-Pattern 2: Ignoring Channel Congestion in Dense Deployments
**❌ BAD**: Testing V2X system with 5 vehicles on a test track; deploying on urban highway with 500 vehicles
**✅ GOOD**: Simulate and test under realistic vehicle density:
```
V2X channel load analysis:
  BSM rate: 10 Hz × 500 vehicles × 400 bytes/BSM = 1.6 Mbps effective load
  DSRC 10MHz channel capacity: ~6 Mbps (at 6 Mbps base rate, QPSK 1/2)
  Channel Busy Ratio (CBR): 1.6/6 = 27% → acceptable

  But: at intersection with 500 vehicles in 300m radius:
    ALL vehicles hear ALL others → single collision domain
    CBR can spike to 80-90% → DCC must reduce rate to 4-5 Hz
    At 4 Hz BSM rate: latency increases to 250ms → safety degraded

Mitigation: DCC transmit power reduction + rate adaptation; test at peak density
```

---

### Anti-Pattern 3: GPS Accuracy Assumption
**❌ BAD**: Implementing cooperative perception assuming all vehicles have ≤ 1m GPS accuracy
**✅ GOOD**: Standard automotive GPS (NMEA, single-constellation) has 3-5m accuracy in open sky, 10-20m in urban canyon:
```
GPS accuracy impact on cooperative tracking:
  Sender GPS error: 3m (1σ)
  Receiver GPS error: 3m (1σ)
  Total position uncertainty: √(3² + 3²) = 4.2m combined

  If vehicle is in adjacent lane (3.5m away):
    → 4.2m position uncertainty exceeds lane width
    → Cannot determine which lane a remote vehicle is in

V2X cooperative perception requires:
  RTK-corrected GPS (≤ 0.3m accuracy) OR
  SBAS-corrected GPS (1.5m accuracy with integrity) OR
  V2X position accuracy service (ETSI TR 103 869)
```

---

### Anti-Pattern 4: Skipping IEEE 1609.2 in "Internal" Deployments
**❌ BAD**: "We only use V2X within our company fleet, so we don't need certificate-based security"
**✅ GOOD**: IEEE 1609.2 authentication is necessary even in fleet deployments:
- Prevents message injection from unauthorized devices on the road
- Provides non-repudiation for safety event logging
- Required for future public network interoperability
- Certificate overhead is small (20-30 bytes + ~2ms signing latency)
Skipping security creates vulnerability to BSM injection attacks that could trigger false braking events.

---

### Anti-Pattern 5: Treating DSRC and C-V2X as Interchangeable
**❌ BAD**: Switching from DSRC to C-V2X assuming the application layer stays the same
**✅ GOOD**: DSRC and C-V2X differ at MAC/PHY but SAE J2735 message layer is compatible:
```
What stays the same:
  ✓ SAE J2735 message set (BSM, SPAT, MAP)
  ✓ SAE J2945 performance requirements
  ✓ IEEE 1609.2 security (can be applied to both)
  ✓ Application logic (GLOSA algorithm, PCW algorithm)

What changes:
  ✗ MAC/PHY configuration (802.11p OFDM vs. 3GPP NR sidelink)
  ✗ Channel access method (CSMA/CA for DSRC vs. sensing-based SPS for C-V2X)
  ✗ Resource scheduling (distributed for DSRC; semi-persistent for LTE-V2X Mode 4)
  ✗ Coexistence management (different spectrum sharing rules)

Direct hardware swap between DSRC and C-V2X OBU requires re-validation of:
  → MAC latency (different access mechanisms)
  → Range performance (C-V2X generally better NLOS)
  → DCC algorithm (must match PHY characteristics)
```
