# Standards & Reference

## 7.1 Official Documentation

- [Fusion 360 Help](https://help.autodesk.com/view/fusion360/ENU/) — Full product documentation and user guides
- [Fusion 360 API Documentation](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-255976DE-CF53-4428-84F3-4F51B9E860D8) — Scripting and add-in development reference
- [Fusion 360 CAM Reference](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-0F65F4F2-34E3-4A33-81BD-6E0F1EB9DA4E) — Manufacturing and toolpath documentation
- [Fusion 360 Blog](https://www.autodesk.com/products/fusion-360/blog) — Tips, tutorials, and feature announcements
- [Autodesk University](https://www.autodesk.com/autodesk-university/) — Video courses and certifications
- [Fusion 360 Sketch Best Practices](https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-89E49518-EB8B-4AE0-BB49-1B4E0F9C1D21) — Constraint and dimension guidelines

## 7.2 Modeling Standards

### Sketch Constraints

| Constraint | When to Use | Avoid |
|------------|-------------|-------|
| **Coincident** | Points on geometry | Overusing — use construction lines |
| **Concentric** | Circular edges sharing center | Mating separate circles |
| **Collinear** | Lines on same vector | Misaligned reference edges |
| **Horizontal/Vertical** | Align to axis | Non-axis-aligned geometry |
| **Symmetry** | Mirror designs | Asymmetric features |
| **Tangent** | Smooth transitions | Sharp internal corners |

### Feature Creation Order

1. **Base Sketch** — Create base profile first, fully constrained
2. **Extrude/Revolve** — Add/remove base material
3. **Hole Features** — Threaded, clearance, or tap holes
4. **Derived Features** — Pockets, pads, ribs
5. **Surface Cleanup** — Fillet (inside edges first), chamfer (outside)
6. **Pattern Features** — Linear/circular patterns for repeatable geometry
7. **Thread Features** — Add threads last (model threads or cosmetic)

### Tolerance Standards

| Application | Tolerance | Standard |
|-------------|-----------|----------|
| Precision machined | ±0.01mm | H7/h7 fit |
| General machined | ±0.05mm | H8/h8 fit |
| Sheet metal | ±0.2mm | Bend deduction |
| 3D printed | As-printed | ±0.1–0.3mm |
| Assembled parts | Functional fit | ISO 286 fit system |

## 7.3 CAM Standards

### Tool Selection

| Operation | End Mill | Settings |
|-----------|----------|----------|
| Roughing | 4-flute carbide | 35% stepover, 0.5mm axial depth |
| Finishing | 3-flute carbide | 10% stepover, 0.1mm axial depth |
| 3D Adaptive | High helix | 30% stepover, full depth |
| Engraving | V-bit / ballnose | 0.05mm stepover |
| Drilling | HSS or carbide | Peck cycle for deep holes |

### Toolpath Best Practices

- **Stock to leave** — 0.2–0.5mm for finishing passes
- **Lead-in/Lead-out** — Use radius entries to protect tool
- **Coolant** — Flood for steel, air blast for aluminum, mist for plastic
- **Feeds & Speeds** — Calculate via manufacturer recommended SFM and chip load
- **Collision Avoidance** — Enable tool holder collision checking in Simulation tab

## 7.4 File Management

| Format | Use Case | Notes |
|--------|----------|-------|
| **Fusion 360 native (.f3d)** | Full parametric model | Cloud-synced |
| **STEP (.stp)** | Cross-CAD exchange | Best for solids |
| **IGES (.igs)** | Surface exchange | May lose features |
| **STL** | 3D printing / meshes | No parametric data |
| **OBJ** | Rendering | Preserves meshes |
| **DXF** | 2D drawings / laser | Layer support |
| **G-code (.nc)** | CNC machining | Post-process per machine |

## 7.5 Version Compatibility

| Version | Status | Notes |
|---------|--------|-------|
| 2021.x | Legacy | No longer supported by Autodesk |
| 2022.x | Legacy | Limited support |
| 2023.x | Current | Recommended |
| 2024.x | Current | Latest features |
| 2025.x | Beta | Early access |

## 7.6 Common Pitfalls

- **Over-constrained sketches** — Remove redundant constraints; use Auto Constrain sparingly
- **Feature suppression cascades** — Use "Delete Features" to prevent broken histories
- **Shell before extrude** — Never extrude through a shelled body; extrude first
- **Large mesh imports** — Use Mesh to BRep for conversion, then edit parametrically
- **Cloud sync conflicts** — Always sync before major edits; use local copies for offline work
