# High-NA EUV Technical Deep Dive

> TWINSCAN EXE:5000 / EXE:5200 Technology Reference

---

## Executive Summary

High-NA EUV represents the next evolutionary step in semiconductor lithography, increasing numerical aperture from 0.33 to 0.55. This 67% NA increase delivers approximately **1.7× resolution improvement**, enabling single-exposure patterning for 2nm logic and advanced DRAM nodes.

---

## Fundamental Physics

### Numerical Aperture Relationship

```
Resolution (CD) = k1 × λ / NA

Where:
- k1 = process factor (typically 0.25-0.35)
- λ = wavelength (13.5 nm for EUV)
- NA = numerical aperture
```

### Resolution Comparison

| System | NA | Single-Exp Resolution | Theoretical Limit |
|--------|-----|----------------------|-------------------|
| NXE:3400C | 0.33 | ~13 nm | ~10 nm |
| NXE:3600D | 0.33 | ~13 nm | ~10 nm |
| NXE:3800E | 0.33 | ~13 nm | ~10 nm |
| **EXE:5000** | **0.55** | **~8 nm** | **~6 nm** |

### Depth of Focus Trade-off

Higher NA reduces depth of focus (DOF):

```
DOF ∝ λ / NA²
```

| System | Approximate DOF |
|--------|-----------------|
| 0.33 NA | ~120 nm |
| 0.55 NA | ~70 nm |

**Mitigation:**
- Advanced focus control systems
- Improved wafer flatness requirements
- Focus mapping and correction

---

## Optical System Design

### Anamorphic Imaging

High-NA EUV uses **anamorphic optics** to manage field size:

| Dimension | 0.33 NA | 0.55 NA |
|-----------|---------|---------|
| Field Width | 26 mm | 26 mm |
| Field Height | 33 mm | 16.5 mm |
| Field Area | 858 mm² | 429 mm² (half) |

**Impact:** Large chips require stitching of two half-fields.

### Projection Optics Box (POB)

| Component | Specification |
|-----------|---------------|
| Mirror Count | 4 mirrors (vs 6 in 0.33 NA) |
| Mirror Material | Zerodur with Mo/Si multilayer |
| Surface Quality | <30 pm RMS roughness |
| Wavefront Error | <0.05 nm RMS |

### Illuminator System

| Feature | Specification |
|---------|---------------|
| Pupil Fill Ratio | >20% (current), >10% (evolution) |
| Transmission | Higher via mirror removal |
| Flexibility | Multi-point, freeform illumination |

---

## System Specifications

### EXE:5000 (First Generation)

| Parameter | Specification |
|-----------|---------------|
| NA | 0.55 |
| Resolution | 8 nm (half-pitch) |
| Throughput | ≥150 wafers/hour |
| Overlay | <1.5 nm |
| CDU (full wafer) | <0.60 nm |
| CDU (intra-field) | <0.55 nm |
| Image Contrast | 40% improvement vs 0.33 NA |

### EXE:5200 (Next Generation)

| Parameter | Target |
|-----------|--------|
| Throughput | >200 wafers/hour |
| Productivity | High-volume manufacturing |
| Availability | 2026-2027 |

### Physical Characteristics

| Attribute | Value |
|-----------|-------|
| Total Weight | >150 metric tons |
| Shipping Crates | 250+ crates |
| Containers | 43 freight containers |
| Installation Time | 6+ months |
| Cleanroom Space | Significant expansion vs NXE |
| System Price | ~€350 million |

---

## Performance Benefits

### Logic Applications

| Layer Type | 0.33 NA Approach | 0.55 NA Approach | Benefit |
|------------|------------------|------------------|---------|
| Random Vias | LELELE (3 exp) | Single exposure | 20% cost reduction |
| 2D Metal | Multi-patterning | Direct patterning | Design freedom |
| Cut/Block | SADP/SAQP | Single exposure | Process simplification |

### DRAM Applications

| Feature | 0.33 NA | 0.55 NA | Improvement |
|---------|---------|---------|-------------|
| Capacitor Contact | Triple patterning | Single exposure | 30% cost benefit |
| Dose Required | High | 70% lower | Throughput gain |
| Process Complexity | High | Low | Yield improvement |

### Cost of Patterning Analysis

**2nm Logic Node Example:**

| Cost Component | Multi-Pattern 0.33 NA | High-NA 0.55 NA |
|----------------|----------------------|-----------------|
| Litho cost/layer | ~$1.8M | ~$1.2M |
| Process steps | 3× exposure + etch | 1× exposure + etch |
| Cycle time | 3-4 days | 1 day |
| Defect risk | Multiplicative | Lower |
| **Total Benefit** | Baseline | **20-35% reduction** |

---

## Manufacturing Challenges

### 1. Stitching for Large Chips

**Challenge:** Half-field size requires stitching for chips >429 mm²

**Solution Approach:**
- Precise field-to-field matching (<0.5 nm)
- In-die stitching optimization
- OPC for stitching boundaries
- Aerial image cross-talk modeling

**Status:** Demonstrated successfully on NXE platform

### 2. Mask Technology

**Requirements:**

| Feature | 0.33 NA | 0.55 NA |
|---------|---------|---------|
| Absorber | Ta-based | Low-n materials |
| Reflectivity | Standard | Optimized |
| Black Border | Critical | Ultra-critical |
| Defect Specs | Tighter | Strictest |

**New Mask Materials:**
- Low refractive index (low-n) absorbers
- Improved line-end control
- Enhanced resolution

### 3. Resist Requirements

**Challenges at High-NA:**

| Issue | Impact | Mitigation |
|-------|--------|------------|
| Photon shot noise | Stochastic defects | Higher absorption resist |
| Resist blur | CD uniformity | Reduced blur chemistry |
| Sensitivity | Throughput | Chemical amplification |

**Target Performance:**
- Resolution: <10 nm lines/spaces
- LER (Line Edge Roughness): <2 nm
- Sensitivity: <20 mJ/cm²

### 4. Source Power Scaling

| Milestone | Power | Status |
|-----------|-------|--------|
| Current | ~250W | Production |
| Demonstrated | 600W | Lab |
| Target | >1000W | Development |
| Future | ~2000W | Research |

**Technology Path:**
- 1μm laser pre-pulse (vs 10μm)
- Better droplet control
- Enhanced collector efficiency

---

## Customer Adoption Status

### Public Commitments

| Customer | High-NA Status | Timeline |
|----------|---------------|----------|
| Intel | First mover | EXE:5000 installed (2024) |
| TSMC | Committed | 2nm node adoption |
| Samsung | Ordered | 2nm process development |
| SK Hynix | Evaluating | DRAM application |

### Intel Progress Report (2024)

- **Installation:** Oregon D1X fab
- **Transport:** 43 containers, 250+ crates
- **First Images:** 10nm dense lines printed
- **Status:** Coarse calibration complete
- **Next:** Full specification operation

---

## Roadmap

### EUV Product Timeline

| Year | 0.33 NA | 0.55 NA |
|------|---------|---------|
| 2022 | NXE:3600D HVM | EXE:5000 build |
| 2023 | Volume production | Integration |
| 2024 | NXE:3800E | First shipments |
| 2025 | NXE:3800E ramp | Customer R&D |
| 2026 | NXE:4000F | EXE:5000 HVM, EXE:5200 |
| 2027+ | Continued | Volume ramp |

### Technology Evolution

```
2024-2025: High-NA introduction (EXE:5000)
    ↓
2026-2027: Volume manufacturing (EXE:5200)
    ↓
2028+: NEXT platform development
    ↓
Beyond: Hyper-NA (0.75+) research
```

---

## Competitive Landscape

### Market Position

ASML maintains **100% market share** in EUV lithography:

| Competitor | EUV Status |
|------------|------------|
| Nikon | No EUV development |
| Canon | No EUV development |
| Other | No viable alternatives |

**Moat Sustainability:**
- 20+ years development investment
- $10B+ cumulative R&D
- Ecosystem lock-in (optics, masks, resist)
- Customer co-dependence

---

## Summary

High-NA EUV represents a **controlled evolution** rather than revolution:

✓ **Proven technology** — Based on 0.33 NA foundation  
✓ **Customer validated** — All major foundries committed  
✓ **Economics compelling** — 20-35% cost reduction  
✓ **Timeline confirmed** — HVM by 2026-2027  

The technology enables the industry to continue Moore's Law scaling through the angstrom era (2nm → 1.4nm → 1nm).

---

*Technical sources: ASML Investor Day 2024, SPIE papers, EXE:5000 specifications*
