# Intel Core Ultra Architecture Reference

> **Document:** Core Ultra Microarchitecture Deep Dive  
> **Last Updated:** 2026-03-21

---

## Overview

Intel Core Ultra represents Intel's transition to a **tile-based (chiplet) architecture**, abandoning monolithic designs in favor of modular, scalable building blocks. This enables:
- Process node optimization per tile (compute vs. I/O)
- Flexible product configurations
- Improved yields through smaller die sizes

---

## Core Ultra Generations

### Meteor Lake (Core Ultra Series 1, 2023-2024)

| Attribute | Specification |
|-----------|---------------|
| Process | Intel 4 (Compute), TSMC N5/N6 (other tiles) |
| CPU Cores | Up to 6P (Redwood Cove) + 8E (Crestmont) |
| GPU | Xe-LPG (8 cores) |
| NPU | 1st Gen, ~10 TOPS |
| Memory | DDR5-5600, LPDDR5X-7467 |
| TDP Range | 15W - 45W |
| Target | Mobile-first (laptops) |

**Key Innovation:** First tile-based Intel client processor
- Compute Tile (Intel 4)
- Graphics Tile (TSMC N5)
- SoC Tile (TSMC N6)
- I/O Tile (TSMC N6)

### Arrow Lake (Core Ultra Series 2, 2024-2025)

| Attribute | Specification |
|-----------|---------------|
| Process | Intel 20A/TSMC N3B (Compute), TSMC (other tiles) |
| CPU Cores | Up to 8P (Lion Cove) + 16E (Skymont) |
| GPU | Xe-LPG+ (8 cores) |
| NPU | 2nd Gen, ~13 TOPS |
| Memory | DDR5-6400, LPDDR5X-8400 |
| TDP Range | 35W - 250W (desktop) |
| Target | Desktop + Mobile |

**Key Innovation:** First Intel 20A/ribbonFET client product
- Lion Cove P-cores (15-25% IPC uplift)
- Skymont E-cores
- SMT removed (first Intel client CPU without hyper-threading)

### Lunar Lake (Core Ultra Series 2, 2024)

| Attribute | Specification |
|-----------|---------------|
| Process | TSMC N3B (Compute), TSMC N6 (other tiles) |
| CPU Cores | Up to 4P (Lion Cove) + 4E (Skymont) |
| GPU | Xe2 (Battlemage, 8 cores) |
| NPU | 3rd Gen, 48 TOPS |
| Memory | LPDDR5X-8533 (on-package, up to 32GB) |
| TDP Range | 17W - 30W |
| Target | Premium thin-and-light laptops |

**Key Innovation:** 
- On-package memory (like Apple M-series)
- 40+ TOPS NPU (Copilot+ PC compliant)
- Intel's most efficient x86 processor ever

### Panther Lake (Core Ultra Series 3, 2025)

| Attribute | Specification |
|-----------|---------------|
| Process | **Intel 18A** (all tiles) |
| CPU Cores | Up to 4P (Cougar Cove) + 8E + 4LPE (Darkmont) |
| GPU | Xe3 (Celestial, 12 cores) |
| NPU | 4th Gen, 80-120 TOPS |
| Memory | LPDDR5X-9600 (on-package, up to 96GB) |
| TDP Range | 15W - 45W |
| Target | All mobile segments |

**Key Innovation:** First all-Intel 18A client processor
- Cougar Cove P-cores (5-13% IPC uplift over Lion Cove)
- 80-120 TOPS NPU for advanced AI workloads
- Intel 18A with RibbonFET + PowerVia

---

## CPU Core Architectures

### P-Core (Performance Core) Evolution

| Generation | Microarchitecture | Process | Key Features |
|------------|-------------------|---------|--------------|
| 12th Gen | Golden Cove | Intel 7 | First hybrid architecture |
| 13th Gen | Raptor Cove | Intel 7 | Cache improvements |
| Meteor Lake | Redwood Cove | Intel 4 | IPC uplift, efficiency |
| Arrow Lake | Lion Cove | Intel 20A | Major redesign, no SMT |
| Panther Lake | Cougar Cove | Intel 18A | Further IPC gains |

### E-Core (Efficiency Core) Evolution

| Generation | Microarchitecture | Process | Key Features |
|------------|-------------------|---------|--------------|
| 12th-13th Gen | Gracemont | Intel 7 | First E-cores |
| Meteor Lake | Crestmont | Intel 4 | Improved IPC |
| Arrow Lake/Lunar Lake | Skymont | Intel 20A/TSMC N3B | Efficiency focus |
| Panther Lake | Darkmont | Intel 18A | Ultra-low power variant |

### LP E-Core (Low Power Efficiency Core)

Introduced in Meteor Lake:
- Handles background tasks at ultra-low power (<1W)
- Integrated in SoC tile (separate from compute tile)
- Enables "instant wake" and always-on features

---

## Tile Architecture Details

### Meteor Lake Tile Layout

```
┌─────────────────────────────────────────────────────────┐
│                    METEOR LAKE                          │
├─────────────────┬─────────────────┬─────────────────────┤
│   COMPUTE TILE  │   GRAPHICS TILE │     I/O TILE        │
│   (Intel 4)     │   (TSMC N5)     │    (TSMC N6)        │
│                 │                 │                     │
│  P-Cores        │  Xe-LPG GPU     │  PCIe, Thunderbolt  │
│  E-Cores        │  Media Encode   │  USB4               │
│  L3 Cache       │                 │                     │
│                 │                 │                     │
├─────────────────┴─────────────────┴─────────────────────┤
│                    SoC TILE (TSMC N6)                   │
│         LP E-Cores, NPU, Media, Display, Security       │
└─────────────────────────────────────────────────────────┘
              │
         Foveros 3D Packaging
```

### Arrow Lake Tile Layout

```
┌─────────────────────────────────────────────────────────┐
│                    ARROW LAKE                           │
├─────────────────┬─────────────────┬─────────────────────┤
│   COMPUTE TILE  │   GRAPHICS TILE │     I/O TILE        │
│ (Intel 20A/     │   (TSMC N5)     │    (TSMC N6)        │
│  TSMC N3B)      │                 │                     │
│                 │                 │                     │
│  Lion Cove      │  Xe-LPG+ GPU    │  PCIe 5.0           │
│  Skymont        │                 │  Thunderbolt 4      │
│  No SMT         │                 │                     │
│                 │                 │                     │
├─────────────────┴─────────────────┴─────────────────────┤
│                    SoC TILE (TSMC N6)                   │
│              NPU 2.0, Media, Security                   │
└─────────────────────────────────────────────────────────┘
```

### Foveros 3D Packaging

**Technology:**
- Active interposer with through-silicon vias (TSVs)
- Face-to-face die bonding
- Enables high-bandwidth, low-power die-to-die communication

**Meteor Lake Foveros:**
- 36μm pitch interconnect
- ~10x bandwidth vs. traditional packaging

---

## AI Capabilities (NPU)

### NPU Evolution

| Generation | Product | TOPS | Key Features |
|------------|---------|------|--------------|
| NPU 1.0 | Meteor Lake | ~10 | First integrated NPU |
| NPU 2.0 | Arrow Lake | ~13 | Improved efficiency |
| NPU 3.0 | Lunar Lake | 48 | Copilot+ PC ready |
| NPU 4.0 | Panther Lake | 80-120 | Advanced AI workloads |

### NPU Architecture

- **VLIW Architecture**: Very Long Instruction Word for parallel AI operations
- **INT8/FP16 Support**: Optimized for inference workloads
- **Memory Subsystem**: Tightly coupled with system memory

### Microsoft Copilot+ PC Requirements

| Requirement | Intel Solution |
|-------------|----------------|
| NPU Performance | 40+ TOPS |
| Memory | 16GB+ DDR5/LPDDR5X |
| Storage | 256GB+ SSD |
| Status | Lunar Lake meets requirements |

---

## Graphics (Xe) Evolution

### Xe Architecture Generations

| Generation | Product | Process | Cores | Notes |
|------------|---------|---------|-------|-------|
| Xe-LP | 11th Gen | Intel 10nm | 96 EU | First Xe |
| Xe-LPG | Meteor Lake | TSMC N5 | 128 EU | Integrated |
| Xe-LPG+ | Arrow Lake | TSMC N5 | 128 EU | Improved |
| Xe2 (Battlemage) | Lunar Lake | TSMC N3B | 128 EU | New architecture |
| Xe3 (Celestial) | Panther Lake | Intel 18A | 192 EU? | Next-gen |

### Xe Features

- **Ray Tracing**: Hardware-accelerated RT cores (Xe-HPG onwards)
- **XeSS**: Intel's DLSS competitor for upscaling
- **AV1 Encode/Decode**: Hardware support
- **Display**: Up to 8K support, HDR, adaptive sync

---

## Power Management

### Intel Thread Director

- Hardware-based scheduler for hybrid architecture
- Communicates thread characteristics to OS
- Optimizes P-core/E-core assignment

### Power States

| State | Description | Use Case |
|-------|-------------|----------|
| S0ix | Modern standby | Always-on background tasks |
| C-states | Core sleep states | Idle power savings |
| P-states | Performance states | Dynamic frequency scaling |
| Throttling | Thermal protection | Overheat prevention |

---

## References

- Intel Architecture Day 2023, 2024
- Intel Core Ultra Product Briefs
- Microsoft Copilot+ PC Specifications
- Tom's Hardware, AnandTech Reviews
