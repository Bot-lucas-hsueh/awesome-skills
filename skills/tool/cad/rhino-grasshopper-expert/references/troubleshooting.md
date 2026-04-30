# Troubleshooting

## 8.1 Common Geometry Errors

| Error | Cause | Solution |
|-------|-------|----------|
| **"Unable to create surface"** | Non-planar or crossing curves | Simplify curves; use Rebuild first |
| **"Surface edge mismatch"** | Gaps between curves | Extend curves before lofting; check endpoints |
| **"Naked edge"** | Open surface boundary | Use EdgeSrf for gaps; Join to close |
| **"Ambiguous surface"** | Multiple valid solutions | Rebuild with fewer control points |
| **"Not a valid curve"** | Self-intersecting or degenerate | Delete and redraw; use SelBadObjects |
| **"Cannot scale in one direction"** | Invalid input for non-uniform scale | Check for locked geometry; Unlock first |

## 8.2 Grasshopper Errors

| Error | Cause | Fix |
|-------|-------|-----|
| **"Data conversion failed"** | Type mismatch (e.g., Point vs Vector) | Use compatible components; check input types |
| **"Null reference"** | Empty input or missing data | Ensure upstream components output data |
| **"Path mismatch"** | Flattened vs grafted mismatch | Use Path Mapper or Simplify |
| **"Solution exception: divide by zero"** | Zero-length vector | Add IsNull check before division |
| **"Runtime error: out of memory"** | Massive data trees | Reduce mesh resolution; simplify algorithm |
| **"1-manifold mesh required"** | Non-manifold mesh input | Use Detox or Weaverbird to repair |

### Debugging Grasshopper

```text
Workflow:
1. Isolate sections — Disable wires to isolate problem areas
2. Panel debug — Add Panel to inspect data at each step
3. Custom preview — Color points/curves to visualize geometry
4. Watch component — Monitor specific data values
5. Bake test — Bake intermediate geometry to Rhino to verify
```

## 8.3 NURBS Surface Issues

| Symptom | Cause | Fix |
|---------|-------|-----|
| **Surface kinks** | Control points not aligned | Use MatchSrf with G1/G2 |
| **Bulges at edges** | Mismatched knot vectors | Rebuild both curves to same degree |
| **Reflections show seams** | Continuity break | Rebuild and BlendSrf |
| **Hard to edit** | Too many control points | Rebuild with lower degree |
| **Surface oscillates** | Degree too high for data | Lower degree; more points |

## 8.4 Mesh Issues

| Issue | Solution |
|-------|----------|
| **Holes in mesh** | Fill holes (MeshFillHole command) |
| **Inverted normals** | Mesh → Flip Mesh Direction |
| **Non-manifold edges** | Use ExtractNonManifoldMesh; repair manually |
| **Too dense** | Mesh → ReduceMesh (target face count) |
| **Faceted appearance** | Mesh → Smooth Mesh |
| **Hammerhead artifacts** | Increase angular tolerance; subdivide |

## 8.5 Performance Optimization

| Problem | Solution |
|---------|----------|
| **Slow viewport** | Display → Switch to Wireframe for large models |
| **Slow Rebuild** | Use degree 3 instead of 5; fewer points |
| **Slow Boolean** | Pre-simplify geometry; avoid micro-surfaces |
| **GH slow to solve** | Disable preview on static components |
| **GH memory leak** | Remove unused components; use Clusters |
| **Large STL export** | Reduce mesh resolution; use STL export options |

## 8.6 Import/Export Issues

| Issue | Fix |
|-------|-----|
| **STEP import shows gaps** | Increase tolerance in import dialog |
| **OBJ loses materials** | Export as 3DM for full material support |
| **DXF layers missing** | Check layer mapping in export options |
| **STL wrong scale** | Verify units match (mm vs inches) |
| **Rhino → Revit fails** | Use Rhino Inside; or export SAT/IFC |

## 8.7 Command Reference

| Command | Function |
|---------|----------|
| `SelDup` | Find duplicate geometry |
| `SelBadObjects` | Find invalid objects |
| `RebuildCrv` | Reduce control points on curves |
| `RebuildSrf` | Reduce control points on surfaces |
| `MatchSrf` | Adjust surface continuity |
| `MergeAllMeshes` | Combine meshes into one |
| `ReduceMesh` | Decimate mesh face count |
| `MeshBoolean` | Boolean operations on meshes |
| `Sweep2` | Two-rail sweep |
| `NetworkSrf` | Surface from curve network |
| `EdgeSrf` | Surface from 4 edges |
| `ExtractPlySrf` | Get control point surface from SubD |

## 8.8 Grasshopper Component Tips

| Task | Approach |
|------|----------|
| Debug data | Right-click → Stream Filter |
| Reorder list | Sort list, then use Shift Paths |
| Flatten tree | Path Mapper: {A;B;C} → {A} |
| Graft item | Right-click input → Graft |
| Bake with layer | GrasshopperPlayer with Rhino options |
| Make reusable | Select components → Make Cluster |
| Document definition | Add Cluster inputs/outputs descriptions |

## 8.9 Tolerance Issues

| Tolerance | Use Case | Setting |
|-----------|----------|---------|
| 0.001mm | Precision tooling | Document Properties → Units |
| 0.01mm | General modeling | Default for most work |
| 0.1mm | Architectural concept | Lower precision acceptable |
| 1.0mm | Rapid prototyping | For coarse geometry |

Change tolerance: `Units` command → Document Properties → Tolerance

## 8.10 Keyboard Shortcuts

| Shortcut | Command |
|----------|---------|
| `F10` | Show control points |
| `F11` | Hide control points |
| `F5` | Refresh display |
| `Ctrl+Shift+N` | New layer |
| `Ctrl+L` | Show layer dialog |
| `Enter` | Repeat last command |
| `Escape` | Cancel/deselect |
| `Tab` | Object snap toggle |
| `Ortho` | Shift+drag for orthogonal |
