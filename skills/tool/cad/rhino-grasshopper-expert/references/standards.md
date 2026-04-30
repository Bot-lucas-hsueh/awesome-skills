# Standards & Reference

## 7.1 Official Documentation

- [Rhino 3D Documentation](https://docs.mcneel.com/rhino/7/help/en-us/index.htm) — Full command reference and user guide
- [Rhino Developer Documentation](https://developer.rhino3d.com/) — RhinoCommon API, SDK, and plugin development
- [Grasshopper Official Website](https://www.grasshopper3d.com/) — Component documentation and tutorials
- [Grasshopper GitHub](https://github.com/mcneel/grasshopper) — Component source code and examples
- [Rhino Inside Reference](https://www.rhino3d.com Inside/) — Rhino integration with Revit/AutoCAD
- [Rhino3D TV](https://www.rhino3d.tv/) — Video tutorials from McNeel
- [McNeel Forum](https://discourse.mcneel.com/) — Community support and discussions
- [Food4Rhino](https://www.food4rhino.com/) — Plugin ecosystem and resources

## 7.2 NURBS Modeling Standards

### Degree and Control Points

| Application | Degree | Control Points | Tolerance |
|-------------|--------|----------------|-----------|
| Simple curves | 2–3 | 4–8 | 0.01mm |
| Architectural | 3 | 6–12 | 0.1mm |
| Automotive Class-A | 5 | 12–24 | 0.001mm |
| Industrial design | 3–5 | 8–16 | 0.01mm |
| Sculpted organic | 3 | Variable | 0.1mm |

### Continuity Standards

| Level | Description | Use Case |
|-------|-------------|----------|
| **G0 (Position)** | Curves touch; corner visible | Draft geometry, construction |
| **G1 (Tangent)** | Smooth tangent; no kink | General surfaces, blends |
| **G2 (Curvature)** | Smooth curvature; reflection continuity | Product design |
| **G3 (Flow)** | Acceleration continuity | Automotive, high-end design |
| **G4 (Bump)** | Subtle acceleration changes | Premium Class-A surfaces |

### Surface Building Commands

| Command | Input | Output |
|---------|-------|--------|
| **Loft** | 2+ profile curves | Smooth surface between profiles |
| **Sweep1** | 1 rail + profile | Surface along single path |
| **Sweep2** | 2 rails + profile | Surface between two paths |
| **NetworkSrf** | Grid of curves | Surface through curve network |
| **Patch** | Points or curves | Fitted surface (uses Splop) |
| **ExtrudeCrv** | Planar curve | Surface along normal |
| **Rebuild** | Existing curve/surface | Reduce/add control points |
| **MatchSrf** | Two surfaces | Adjust continuity |
| **BlendSrf** | Two surface edges | G1/G2 blended surface |

## 7.3 Grasshopper Standards

### Data Tree Convention

| Pattern | Meaning | Example |
|---------|---------|---------|
| `{0}` | Item at index 0 | First item in list |
| `{0;0}` | Item at [0][0] | First row, first column |
| `{0;1}` | Item at [0][1] | First row, second column |
| `{i}` | All items at level i | Entire list at level 1 |
| `Flatten` | Single flat list | {0;0;0}, {0;0;1} → {0}, {1} |

### Component Organization

| Category | Key Components | Purpose |
|----------|---------------|---------|
| **Params** | Slider, Panel, Number | User input |
| **Math** | Range, Series, Graph Mapper | Data generation |
| **Vec** | Unit Vector, Cross Product | Direction math |
| **Crv** | Divide, Offset, Rebuild | Curve operations |
| **Srf** | Divide Domain, Isotrim | Surface subdivision |
| **Mesh** | Mesh Sphere, Wb | Mesh generation |
| **Intersect** | Curve|Surface, Solid | Boolean operations |
| **Util** | Graft, Flatten, Shift | Data management |
| **Display** | Custom Preview, Text | Visualization |

### Best Practices

- **Graft inputs** — When connecting multiple items to one input, graft to maintain structure
- **Flatten sparingly** — Flatten destroys hierarchy; use Path Mapper instead
- **Cluster groups** — Encapsulate sub-algorithms into clusters for reusability
- **Internalize data** — Right-click component → Internalise data for portable files
- **Naming conventions** — Label groups and clusters with descriptive names
- **Slider ranges** — Set appropriate Min/Max to prevent unexpected values

## 7.4 Mesh Standards

| Application | Max Edge Length | Triangle Count |
|-------------|----------------|----------------|
| 3D printing | 0.05–0.1mm | 500K–2M |
| Rendering | 0.5–2mm | 100K–500K |
| CFD analysis | 1–5mm | Variable |
| Architectural viz | 2–5mm | 50K–200K |
| FEM analysis | 1–10mm | Depends on mesh |

### Mesh Repair Priority

1. **Remove Duplicates** — Merge coincident vertices
2. **Fill Holes** — Close gaps in mesh
3. **Fix Normals** — Ensure consistent outward normals
4. **Weld Vertices** — At mesh edges (threshold: 0.01–0.1mm)
5. **Reduce Mesh** — If too dense for purpose

## 7.5 File Formats

| Format | Extension | Use Case |
|--------|-----------|----------|
| **Rhino 3DM** | .3dm | Native format, includes history |
| **STEP** | .stp/.step | Cross-CAD exchange |
| **IGES** | .igs | Surface exchange |
| **OBJ** | .obj | Rendering, exchange |
| **STL** | .stl | 3D printing |
| **FBX** | .fbx | Animation, game engines |
| **DXF** | .dxf | 2D/3D CNC exchange |
| **3DS** | .3ds | Legacy import |
| **SKP** | .skp | SketchUp interchange |

## 7.6 Rhino Version Compatibility

| Version | Status | Notes |
|---------|--------|-------|
| Rhino 5 | Legacy | Mac version available |
| Rhino 6 | Legacy | WIP improvements |
| Rhino 7 | Current | SubD modeling added |
| Rhino 8 | Current | Enhanced SubD, modeling aid |
| Rhino WIP | Beta | Experimental features |

## 7.7 Common Pitfalls

- **Naked edges** — Ensure all mesh/surface edges are joined or sealed
- **Unjoined curves** — Use CurveBoolean before sweeping
- **Duplicate geometry** — SelDup to find overlapping objects
- **Bad surface normals** — Use Flip to correct direction
- **Control point misalignment** — Rebuild curves before blending
- **GH slider bloat** — Too many sliders slows Grasshopper; use clusters
- **Data tree mismatch** — Graft/Flatten to align incompatible data paths
