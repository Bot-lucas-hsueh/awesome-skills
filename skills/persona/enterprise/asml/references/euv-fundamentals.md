# EUV Lithography Fundamentals

> Core principles of Extreme Ultraviolet lithography technology

---

## Introduction to EUV

Extreme Ultraviolet (EUV) lithography uses light with a wavelength of **13.5 nanometers**—roughly 1/14th the wavelength of DUV (193 nm) systems. This shorter wavelength enables printing of features at the 7nm node and below, where DUV multi-patterning becomes economically impractical.

---

## Physics of EUV

### Wavelength and Resolution

The fundamental relationship governing lithography resolution is the **Rayleigh Criterion**:

```
CD (Critical Dimension) = k1 × λ / NA

Where:
- CD = minimum feature size (nm)
- k1 = process factor (0.25-0.35 for production)
- λ = wavelength (nm)
- NA = numerical aperture
```

### Resolution Evolution

| Technology | λ (nm) | NA | CD (k1=0.3) |
|------------|--------|-----|-------------|
| i-line | 365 | 0.60 | 183 nm |
| KrF | 248 | 0.80 | 93 nm |
| ArF dry | 193 | 0.85 | 68 nm |
| ArFi | 193 | 1.35 | 43 nm |
| EUV | 13.5 | 0.33 | 12 nm |
| EUV High-NA | 13.5 | 0.55 | 8 nm |

### Why 13.5 nm?

The 13.5 nm wavelength was selected because:

1. **Lithium-based plasma** emits strongly at 13.5 nm
2. **Mo/Si multilayer mirrors** have peak reflectivity (~70%) at this wavelength
3. **Atmospheric absorption** is manageable in vacuum
4. **Optical properties** balance resolution and manufacturability

---

## EUV Source Technology

### Laser-Produced Plasma (LPP)

**Process:**
```
1. Tin droplet generation (30-50 μm diameter)
2. Pre-pulse laser (shapes droplet)
3. Main CO2 laser pulse (hits tin)
4. Plasma formation (T ~ 500,000°C)
5. EUV emission at 13.5 nm
6. Collector mirror captures EUV
```

### Source Power Evolution

| Generation | Power | Year | WPH Capability |
|------------|-------|------|----------------|
| Pre-production | 10W | 2010 | <10 |
| NXE:3100 | 100W | 2012 | 60 |
| NXE:3300B | 200W | 2015 | 100 |
| NXE:3400C | 250W | 2019 | 160 |
| Current | 300W+ | 2024 | 185+ |
| Target | 600W | 2026 | 220+ |

### Key Source Components

| Component | Function | Challenge |
|-----------|----------|-----------|
| Droplet Generator | Creates tin droplets at 50-100 kHz | Stability, lifetime |
| CO2 Laser | 20-30 kW average power | Efficiency, cooling |
| Collector Mirror | Collects EUV (13.5 nm), rejects IR | Debris, reflectivity |
| Vacuum Chamber | Maintain 10⁻⁶ mbar | Contamination control |

---

## EUV Optics

### All-Reflective Design

Unlike DUV systems that use lenses, EUV requires **mirrors** because:
- All materials absorb 13.5 nm light
- Only multilayer mirrors provide sufficient reflectivity

### Mirror Technology

**Mo/Si Multilayer Mirror:**
- Alternating layers of Molybdenum and Silicon
- ~40 layer pairs
- ~70% reflectivity per mirror
- Atomic-scale precision (±0.01 nm)

### Projection Optics

**NXE:3400C/3600D Optical Chain:**

| Mirror | Function | NA |
|--------|----------|-----|
| Illuminator | Collect and shape | - |
| Reticle | Pattern reflection | - |
| POB-1 to POB-6 | Projection (6 mirrors) | 0.33 |
| Wafer | Image plane | - |

**Reflectivity Loss:**
- 6 mirrors × 70% = ~11.8% transmission
- Source power 250W → Wafer ~30W effective

**High-NA Evolution (EXE:5000):**
- 4-mirror design (improved transmission)
- NA = 0.55
- Anamorphic magnification (4×/8×)

---

## EUV Masks

### Reflective Mask Architecture

Unlike DUV transmission masks, EUV masks are **reflective**:

```
Cross-section:
┌─────────────────────────────┐
│  Absorber (Ta-based)        │ ← Pattern defined here
├─────────────────────────────┤
│  Mo/Si Multilayer (40 pairs)│ ← Reflective coating
├─────────────────────────────┤
│  Substrate (ULP glass)      │ ← Low thermal expansion
└─────────────────────────────┘
```

### Mask Specifications

| Parameter | Requirement |
|-----------|-------------|
| Substrate flatness | <50 nm |
| Multilayer uniformity | <0.2% |
| Defect size | <30 nm (programmable) |
| Pattern placement | <2 nm |
| Reflectivity | >65% |

### Reticle 4× Magnification

EUV uses **4× reduction** (vs 4× for DUV):
- Mask features are 4× larger than wafer features
- Eases mask fabrication
- Reduces mask impact of defects

Example:
- 28 nm wafer feature → 112 nm on mask
- 7 nm wafer feature → 28 nm on mask

---

## Metrology and Control

### In-Situ Metrology

EUV systems include integrated sensors:

| Sensor | Purpose |
|--------|---------|
| Aerial Image Sensor | Monitor image quality |
| Spot Sensor | Source monitoring |
| Slit Sensor | Illumination uniformity |
| Wafer Table Sensors | Position, temperature |

### Key Performance Metrics

| Metric | Definition | Typical Spec |
|--------|------------|--------------|
| CDU (CD Uniformity) | Feature size variation | <1.0 nm (3σ) |
| Overlay | Layer-to-layer alignment | <1.5 nm (MAS) |
| LER | Line edge roughness | <2 nm |
| Dose Uniformity | Exposure consistency | <0.5% |

### Productivity Metrics

| Metric | Definition |
|--------|------------|
| WPH (Wafers Per Hour) | Throughput metric |
| Availability | Uptime percentage |
| Dose | Energy delivered (mJ/cm²) |

---

## Process Considerations

### Resist Requirements

**EUV-specific challenges:**

| Challenge | Cause | Mitigation |
|-----------|-------|------------|
| Photon shot noise | Low photon count | Higher absorption resist |
| Stochastic defects | Random photon distribution | Process optimization |
| Chemical blur | Acid diffusion | Controlled chemistry |

**Resist Performance Targets:**

| Parameter | Target |
|-----------|--------|
| Resolution | <13 nm L/S |
| Sensitivity | 20-30 mJ/cm² |
| LER | <2 nm |
| DOF latitude | >100 nm |

### Track Integration

EUV requires specialized track systems:
- Vacuum interface (no air gap)
- Clean environment (fewer particles)
- Temperature control (thermal stability)
- Resist coating optimization

---

## Comparison: EUV vs DUV

| Aspect | EUV | DUV (ArFi) |
|--------|-----|------------|
| Wavelength | 13.5 nm | 193 nm |
| Optics | Reflective (mirrors) | Refractive (lenses) |
| Environment | Vacuum | Air/N₂ |
| Mask type | Reflective | Transmissive |
| Source | LPP plasma | Excimer laser |
| Single-exp limit | ~13 nm | ~38 nm |
| Throughput | 160-220 wph | 275-330 wph |
| Cost per tool | ~€150M | ~€60M |
| Patterning at 7nm | Single exposure | SAQP (4×) |

---

## Economic Analysis

### Cost Per Wafer

**7nm Metal Layer Example:**

| Approach | Steps | Equipment | Cost/Wafer |
|----------|-------|-----------|------------|
| DUV SAQP | 4 litho + 3 etch | 4 scanners | ~$180 |
| EUV SE | 1 litho + 1 etch | 1 scanner | ~$65 |
| **Savings** | **75% fewer steps** | | **~64%** |

### Total Cost of Ownership

| Factor | EUV Impact |
|--------|------------|
| Capital cost | Higher per tool |
| Floor space | Reduced (fewer tools) |
| Cycle time | Reduced |
| Yield | Improved (simpler process) |
| Overall | **Lower at <10nm nodes** |

---

## Future Directions

### Beyond High-NA

| Technology | Concept | Status |
|------------|---------|--------|
| Hyper-NA (0.75) | Further NA increase | Research |
| New wavelengths | 6.x nm | Fundamental research |
| Directed self-assembly | Hybrid patterning | Development |
| High-NA + Multi-patterning | Extendibility | Planning |

### Source Roadmap

| Target | Power | Application |
|--------|-------|-------------|
| 2025 | 400W | Improved WPH |
| 2027 | 600W | High-NA support |
| 2030 | 1000W | Future nodes |

---

## Summary

EUV lithography is the **critical enabler** for advanced semiconductor manufacturing:

✓ **Only viable technology** for <10nm single exposure  
✓ **Mature production technology** — 10+ years HVM experience  
✓ **Monopoly position** — ASML sole supplier  
✓ **Clear roadmap** — High-NA extends capability to 1nm  
✓ **Economic imperative** — Lower cost than multi-patterning  

Understanding EUV is essential for anyone working in advanced semiconductor process technology.

---

*References: ASML technical documentation, SPIE proceedings, semiconductor industry reports*
