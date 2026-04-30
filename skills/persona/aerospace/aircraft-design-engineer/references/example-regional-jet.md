# Example 1: Regional Jet Conceptual Design

## Project Context

**Aircraft Type:** 90-seat regional jet  
**Mission:** 1,500 nm range, Mach 0.78 cruise  
**Market:** Replace aging CRJ900/E190 fleets  
**Development Timeline:** 2025-2035

---

## Step 1: Requirements Definition

### Customer Requirements

| Parameter | Requirement | Source |
|-----------|-------------|--------|
| Passengers | 90 (2-class) | Market analysis |
| Range | 1,500 nm + reserves | Route studies |
| Cruise Speed | Mach 0.78 | Competitive |
| Field Length | 5,000 ft (SL, ISA) | Airport constraints |
| Operating Altitude | FL410 | Airspace |
| Engines | 2 turbofans | ETOPS 120 target |

### Design Constraints

- Certification: CS-25 / Part 25
- Environmental: ICAO Chapter 14 noise
- Ramp weight: <100,000 lbs for gate class

---

## Step 2: Initial Sizing

### Mission Profile Analysis

```
Segment          Weight Fraction    Cumulative
Takeoff & Climb  0.970              0.970
Cruise           0.925              0.897
Descent & Land   0.995              0.893
Taxi & Reserve   0.990              0.884
```

### Takeoff Weight Estimation

```
First Guess:
Payload: 90 pax × 95 kg = 8,550 kg
Crew: 4 × 80 kg = 320 kg
Useful load: 8,870 kg

Assume OEW/MTOW = 0.55
Fuel fraction = 1 - 0.884 = 0.116

Solving iteratively:
MTOW ≈ 42,500 kg (93,700 lb)
OEW ≈ 23,400 kg
Fuel ≈ 4,900 kg
```

---

## Step 3: Wing Sizing

### Design Point Selection

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Wing Loading (W/S) | 120 lb/ft² | Balance of field & cruise |
| Thrust Loading (T/W) | 0.32 | Single-engine climb |
| Aspect Ratio | 9.5 | Induced drag vs weight |
| Sweep (Λ) | 25° | Transonic drag |

### Wing Geometry

```
Wing Area (S) = MTOW / (W/S)
              = 93,700 / 120 = 781 ft² = 72.5 m²

Span (b) = √(AR × S) = √(9.5 × 781) = 86 ft (26.2 m)

Root Chord (Cr) = 2S / [b(1+λ)] = ... (detailed calc)
Tip Chord (Ct) = λ × Cr
Mean Aerodynamic Chord (MAC) = ...
```

---

## Step 4: Configuration Trade Study

### Wing Position

| Configuration | Pros | Cons | Selection |
|---------------|------|------|-----------|
| Low Wing | Landing gear storage, stability | Engine ground clearance | **SELECTED** |
| High Wing | Cargo capacity, rough field | Heavier landing gear | |

### Tail Configuration

| Configuration | Pros | Cons | Selection |
|---------------|------|------|-----------|
| Conventional | Proven, lighter | Larger tail area | **SELECTED** |
| T-tail | Smaller V-tail | Deep stall risk | |
| Cruciform | Compromise | Complexity | |

### Engine Placement

| Position | Pros | Cons | Selection |
|----------|------|------|-----------|
| Rear Fuselage | Wing efficiency | CG challenges, noise | |
| Wing-Mounted | Standard, CG | Wing structure | **SELECTED** |

---

## Step 5: Performance Verification

### Initial Performance Estimates

| Parameter | Target | Estimate | Status |
|-----------|--------|----------|--------|
| Range | 1,500 nm | 1,580 nm | ✓ Met |
| Cruise M | 0.78 | 0.78 | ✓ Met |
| Takeoff Field | 5,000 ft | 4,800 ft | ✓ Met |
| Landing Field | 4,500 ft | 4,200 ft | ✓ Met |
| Climb Rate | 2,500 fpm | 2,800 fpm | ✓ Met |

### Drag Polar (Preliminary)

```
CD = CD0 + CL²/(π × AR × e)

Where:
CD0 = 0.020 (clean configuration)
e = 0.85 (Oswald efficiency)
AR = 9.5

At Cruise: CL ≈ 0.45
CD = 0.020 + 0.45²/(π × 9.5 × 0.85) = 0.020 + 0.008 = 0.028
L/D = 0.45/0.028 = 16.1
```

---

## Step 6: Iteration & Refinement

### Weight Refinement

Based on detailed component estimates:
- Wing: 12% MTOW
- Fuselage: 10% MTOW
- Empennage: 2.5% MTOW
- Propulsion: 8% MTOW
- Systems: 12% MTOW
- Furnishings: 6% MTOW

Updated OEW = 43% MTOW (improvement from initial 55%)

### Final Sizing

```
MTOW: 40,000 kg (88,200 lb)
OEW:  17,200 kg (37,900 lb)
Fuel: 4,600 kg (10,100 lb)
Payload: 9,000 kg (19,800 lb)

Wing Area: 70 m² (753 ft²)
Span: 25.8 m (84.6 ft)
Engines: 2 × 12,000 lbf turbofans
```

---

## Lessons Learned

1. **Iteration is essential**: First estimate was 6% heavy on OEW
2. **Wing loading drives everything**: Trade between field and cruise
3. **Engine selection critical**: Availability and fuel burn dominate economics
4. **Start conservative**: Design margins essential for certification

---

**Document Version:** 1.0  
**Date:** 2026-03-22  
**Classification:** Example/Training
