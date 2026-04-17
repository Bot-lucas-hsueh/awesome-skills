# Troubleshooting

## 8.1 Common Errors & Solutions

### Sketch Errors

| Error | Cause | Fix |
|-------|-------|-----|
| **Sketch shows orange (under-constrained)** | Missing dimensions or constraints | Add dimensions or constraints to fully define |
| **Sketch shows blue (over-constrained)** | Conflicting constraints | Right-click sketch → Show/Remove Constraints |
| **"Cannot create feature"** | Sketch has open contours | Use Edit Sketch to close contours; check for gaps |
| **"Invalid profile"** | Self-intersecting sketch | Rebuild with smaller segments or use construction lines |
| **Sketch lines turn gray** | Sketch is not active | Double-click sketch to edit |

### Feature Errors

| Error | Cause | Fix |
|-------|-------|-----|
| **"Operation failed" on Extrude** | Profile not planar or intersecting | Check sketch planarity; verify extrude direction |
| **"Feature failed to rebuild"** | Upstream feature deleted or broken | Open Timeline, right-click broken feature, fix or delete |
| **Hole not thru-all** | Blind depth vs. Through All vs. To selected | Change depth type in Hole dialog |
| **Fillet fails on sharp corner** | Zero-radius edge or inflection | Use 0.1mm minimum; break sharp edges with chamfer first |
| **Shell leaves open areas** | Thin walls or gaps | Check wall thickness; use Thicken feature instead |

### Import/Export Errors

| Error | Cause | Fix |
|-------|-------|-----|
| **STL import is mesh only** | No BRep conversion | Use Mesh tab → Create Base Feature or Mesh to BRep |
| **STEP loses features** | Faceted geometry | Re-export from source as IGES or Parasolid |
| **Large STL exports slow** | Resolution too high | Lower mesh refinement (0.01–0.05mm) |
| **DXF layers missing** | Layer mapping issue | Check Export Options → Layer mapping |

## 8.2 Performance Issues

### Slow Model Response

| Symptom | Cause | Solution |
|---------|-------|----------|
| Timeline slow to scroll | Deep feature history (100+) | Use Delete Features to flatten; suppress unused features |
| Rebuild takes long | Complex fillets/chamfers | Apply fillets last; use simpler radius values |
| Large assembly lag | Many components loaded | Use Design Representations (simplified bodies) |
| Sketch drag slow | Over-constrained sketch | Simplify constraints; use construction geometry |

### Memory & Storage

| Issue | Solution |
|-------|----------|
| Cloud storage full | Purge old versions via Data Panel → right-click version → Delete |
| Large file size | Use Compress Design; remove unused sketches and components |
| Crash on open | Rename .f3d to .zip; extract temp.f3d; open and resave |

## 8.3 CAM Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| **G-code too large** | Too many small moves | Increase Minimum Arc Radius; reduce tolerance |
| **Toolpath gouges surface** | Incorrect tool or stock | Verify tool diameter; check "Use Inside" for pockets |
| **Drilling misses depth** | Retract plane too high | Set retract plane above top of stock |
| **Adaptive leaves material** | Tool diameter wrong | Verify tool in Tool Database matches physical tool |
| **3D adaptive crashes** | Complex geometry | Reduce tool stepover; split operation into regions |

## 8.4 Simulation Errors

| Error | Cause | Fix |
|-------|-------|-----|
| **"Mesh failed"** | Geometry too thin | Increase minimum wall thickness; simplify model |
| **Results show red (failure)** | Loads exceed strength | Increase material thickness; reduce loads; change material |
| **"Contact required"** | Parts need mating | Add Contact sets in study setup |
| **Thermal study slow** | Fine mesh | Increase mesh element size; reduce analysis steps |

## 8.5 Cloud & Sync

| Issue | Solution |
|-------|----------|
| **Sync conflict** | Open version history; choose Keep Local or Keep Cloud |
| **Offline changes lost** | Enable local data copies (Preferences → General → Make a local copy) |
| **Cannot access team drive** | Check account permissions; IT may need to grant access |
| **Update pending** | Restart Fusion 360; check internet connection |

## 8.6 Debug Workflow

1. **Check Timeline** — Gray or warning icons indicate broken features
2. **Use Feature Diagnostics** — Right-click feature → What Went Wrong?
3. **Suppress downstream** — Isolate problems by suppressing features below
4. **Simplify sketch** — Rebuild complex sketches from scratch if unfixable
5. **Repair mesh** — Use Analyze → Body Information for non-manifold edges

## 8.7 Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+E` | Extrude |
| `Ctrl+Shift+R` | Revolve |
| `D` | Dimension |
| `F` | Fillet |
| `R` | Rotate view |
| `H` | Hole |
| `S` | Shell |
| `Ctrl+Z` | Undo |
| `Space` | Orient view |
