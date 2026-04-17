## § 7 · Standard Workflow

### 7.1 Program Setup and Verification

```
Phase 1: Program Review (15 min)
├── Load program into CNC control
├── Verify machine model matches program post-processor
├── Check tool list against available tooling (length, diameter, type)
├── Review work coordinate offsets (G54-G59)
├── Identify subprograms/macros
└── [✓] Checkpoint: Program compatible with machine

Phase 2: Tool Setup (30-45 min)
├── Install tools in correct pockets per tool list
├── Touch off each tool to establish length offset (G43 H#)
├── Verify tool diameter against program (G41/G42)
├── For multi-axis: verify rotary axis orientation
├── Record all offset values on setup sheet
└── [✓] Checkpoint: All tool offsets verified

Phase 3: Workpiece Setup (20-30 min)
├── Secure workpiece in appropriate fixture
├── Locate datum surfaces against fixture stops
├── Verify work coordinate origin with edge finder/probe
├── Check clearance for tool travel (G53, G28 reference)
├── Verify part fits in machine envelope
└── [✓] Checkpoint: Work coordinates set and verified

Phase 4: Dry Run (10-20 min)
├── Set machine to dry-run mode (no spindle, 100% rapid)
├── Execute program to verify no collisions
├── Check all tool changes are accessible
├── Verify work coordinate moves are correct
├── Observe clearance planes are adequate
└── [✓] Checkpoint: No collisions detected

Phase 5: First-Part Verification (30-60 min)
├── Run single-block mode for first part
├── Stop at each tool change, verify tool installed
├── Measure first article against drawing
├── Adjust offsets as needed (wear offsets)
├── If dimensions good → approve for production
└── [✓] Checkpoint: First part within tolerance
```

### 7.2 Troubleshooting Common Issues

```
CHATTER/VIBRATION:
├── Reduce DOC (depth of cut) by 25%
├── Increase or decrease speed 10-15% to find resonance-free zone
├── Use shorter tool stick-out (reduce L/D ratio)
├── Check workholding rigidity (add clamps/supports)
└── Verify machine level and tram

POOR SURFACE FINISH:
├── Increase spindle speed (within limits)
├── Reduce feed rate (finer stepover)
├── Use sharper tool or different coating (TiAlN for heat)
├── Check for tool wear (replace if wear land >0.010")
├── Verify coolant concentration and flow

DIMENSIONAL ERRORS:
├── Verify tool length offsets (re-touch if uncertain)
├── Check work coordinate origin (re-verify datum)
├── Measure for thermal expansion (let machine warm up)
├── Verify correct offset radius/diameter in program
├── Check for tool deflection (reduce stick-out)

TOOL BREAKAGE:
├── Reduce feed rate (chip load too high)
├── Increase speed (if too slow causing rubbing)
├── Check for chips packing in cut (improve evacuation)
├── Verify correct tool grade for material
└── Check for tool runout (collet condition)
```

---
