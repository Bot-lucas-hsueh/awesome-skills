# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Fix |
|---|---------|----------|--------|-----|
| 1 | Overconstrained sketches | 🔴 Critical | Rebuild failures | Check DOF, remove redundant relations |
| 2 | Full radius vs edge fillet | 🔴 Critical | Wrong geometry | Use "Full Round Fillet" when needed |
| 3 | Sweep with no guide curve | 🟡 High | Invalid sweep | Add guide curve or use different method |
| 4 | Non-manifold geometry | 🔴 Critical | Import issues | Check for zero-thickness areas |
| 5 | Missing hole wizard | 🟡 High | Non-standard holes | Use Hole Wizard for machined holes |
| 6 | Inconsistent units | 🟡 High | Wrong dimensions | Set document units at start |
| 7 | No draft on molded parts | 🔴 Critical | Cannot eject | Add 1-2° draft |
| 8 | Thick section transitions | 🟡 High | Sink marks | Use gradual transitions |
| 9 | Hard-coded dimensions | 🟡 High | Brittleness | Use equations and global variables |
| 10 | Deleting referenced features | 🔴 Critical | Rebuild errors | Check references before delete |

### Sketch Mistakes

```
Common Sketch Errors:
├── Underconstrained profile (blue lines)
│   └── Add dimensions or relations
├── Fully constrained but red lines showing
│   └── Conflicting constraints exist
├── Open profile for boss
│   └── Close the sketch
├── Extrude direction wrong
│   └── Flip direction or set to mid-plane
├── Self-intersecting sweep path
│   └── Simplify or rebuild path
└── Lofts with incompatible profiles
    └── Align vertices or use guide curves

Constraint Priority:
1. Geometric relations (COINCIDENT, PARALLEL, etc.)
2. Automatic relations (inferred)
3. Dimensions (driving dimensions)
4. Equations (parametric relationships)
```

### Feature Mistakes

```
Common Feature Errors:
├── Fillet fails on thin geometry
│   └── Use constant radius, smaller value
├── Shell fails with open geometry
│   └── Check for gaps in model
├── Draft fails on complex geometry
│   └── Check pull direction, simplify
├── Mirror feature wrong side
│   └── Use "Flip direction" option
├── Pattern direction wrong
│   └── Select correct edge/direction
└── Hole not through all
    └── Set "Through All" or correct depth

Feature Order Best Practices:
1. Sketch-based features first
2. Holes next
3. Fillets last (smaller to larger)
4. Chamfers after fillets
5. Shell before fillets
```

### Assembly Mistakes

```
Common Assembly Errors:
├── Over-defined component
│   └── Remove redundant mates
├── Mate appears broken (red)
│   └── Fix geometry or suppress mate
├── Component won't move
│   └── Fully defined by mates
├── Accidental mate to wrong surface
│   └── Delete and re-mate
├── Reference to deleted component
│   └── Resolve broken references
└── Circular reference
    └── Redesign structure

Mate Priority:
1. Ground/Fixed first
2. Primary location mates
3. Secondary alignment mates
4. Distance/Angle for clearance
```

## 10.2 Performance Issues

### Rebuild Performance

| Issue | Symptom | Cause | Solution |
|-------|---------|-------|----------|
| Slow rebuild | Multi-second lag | Complex geometry, many features | Simplify features, use patterns |
| Rebuild failure | Red exclamation | Invalid geometry | Fix sketch, remove conflicts |
| Slow save | Disk spinning | Large assembly, links | Save locally, sever links |
| Slow open | Long load time | Large files, lightweight | Use SpeedPak, lighten components |
| Slow graphics | Low FPS | Complex shading | Use RealView, reduce quality |

### Large Assembly Optimization

```
Large Assembly Performance Checklist:
├── [ ] Enable Large Assembly Mode
│   └── Tools > Options > System Options > Performance
├── [ ] Use SpeedPak for top-level
│   └── Tools > Assembly Tools > SpeedPak
├── [ ] Suppress unnecessary features
│   └── Use Display States
├── [ ] Replace with simplified versions
│   └── Virtual components
├── [ ] Lightweight by default
│   └── Component > Make Lightweight
├── [ ] Hide components not in view
│   └── Use Isolate/Hide
├── [ ] Avoid large imported surfaces
│   └── Simplify geometry
├── [ ] Use patterns instead of copies
│   └── Linear/Circular Pattern
├── [ ] Minimize fillets before release
│   └── Round only critical edges
└── [ ] Split into sub-assemblies
    └── Better organization and performance
```

### Graphics Performance

```
Graphics Optimization:
├── RealView Quality: Adjust in View Settings
├── Ambient Occlusion: Disable for performance
├── Shadows: Disable for large assemblies
├── Reflections: Disable except for render
├── Smoothness: Reduce for performance
├── Level of Detail: Enable LOD

Hardware Acceleration:
├── Tools > Options > System Options > Performance
├── Use Software OpenGL if issues
├── Update graphics drivers
└── Consider professional GPU
```

### File Size Management

```
Reduce File Size:
├── PURGE: Remove unused features/data
│   └── Tools > Purge Memory
├── Compress imported data
│   └── FeatureWorks, defeaturing
├── Remove history if not needed
│   └── Insert > Feature > Delete History
├── Reduce spline complexity
│   └── Simplify curves
├── Use Configurations instead of copies
│   └── Design Tables
└── Save as new file
    └── Re-save to compress

File Size Benchmarks:
| Part Complexity | Target Size |
|----------------|-------------|
| Simple (basic shapes) | < 5 MB |
| Medium (machined) | 5-20 MB |
| Complex (industrial) | 20-100 MB |
| Very Complex | > 100 MB |
```

## 10.3 Data Management

### PDM Best Practices

```
PDM/ShareFile Best Practices:
├── Check out before editing
├── Check in with descriptive comment
├── Keep files in vault (not local)
├── Use consistent naming convention
├── Set access permissions properly
├── Create revision correctly
│   └── Never overwrite released files
├── Archive old revisions
└── Regular backup verification

Version Control Workflow:
1. Check out file
2. Make changes
3. Rebuild all references
4. Update drawings
5. Verify BOM
6. Check in
7. Tag/label revision
```

### Import/Export Issues

```
Common Import Problems:
├── Parasolid (.x_t) import fails
│   └── Check Parasolid version
├── STEP (.stp) loses faces
│   └── Try different translator
├── IGES loses surfaces
│   └── Repair geometry after import
├── DXF/DWG units wrong
│   └── Set units during import
└── SolidWorks saves corrupt
    └── Try save to older format

Export Checklist:
├── Check units before export
├── Verify geometry integrity
├── Test import in destination system
├── Include metadata if needed
└── Archive original file
```

### Corruption Recovery

```
Corruption Prevention:
├── Enable Auto-recover
│   └── Tools > Options > Backup/AutoSave
├── Save regularly
├── Don't modify while saving
├── Keep disk space free
├── Use UPS to prevent power loss
└── Regular backups to vault

Recovery Options:
1. AutoRecover files: %TEMP%\SW[filename]
2. Try opening .sldprt.SLDBENCH, .sldprt.SLDWKSB
3. Save As to different format, re-save
4. Open in older version
5. Try repair install
6. Contact SOLIDWORKS support
```
