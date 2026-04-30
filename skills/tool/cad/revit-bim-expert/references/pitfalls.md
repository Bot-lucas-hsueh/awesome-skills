# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Fix |
|---|---------|----------|--------|-----|
| 1 | Missing join/trim | 🔴 Critical | Gaps in model | Use Join/Trim tools |
| 2 | Broken walls at intersections | 🔴 Critical | Areas not calculated | Adjust wall heights, rejoin |
| 3 | Wrong level linking | 🔴 Critical | Model misalignment | Re-link with correct coordinates |
| 4 | No worksharing backup | 🔴 Critical | Lost work | Enable auto-save, backup locally |
| 5 | Deleting shared coordinates | 🟡 High | Lost coordination | Don't move base points, document |
| 6 | Over-constraining links | 🟡 High | Can't update | Use origin-to-origin only |
| 7 | Complex families | 🟡 High | Performance issues | Simplify family geometry |
| 8 | No phase filters | 🟡 High | Wrong elements showing | Set up phase filters |
| 9 | Inconsistent naming | 🟡 High | Coordination issues | Follow naming standard |
| 10 | Excessive detail in LOD | 🟡 Medium | Large file sizes | Match LOD to project phase |

### Model Integrity Pitfalls

```
Common Model Errors:
├── Walls not connected
│   └── Use Join Geometry tool
├── Floors floating above walls
│   └── Check level heights, attach
├── Columns not spanning floors
│   └── Check column base level, extend
├── Windows not in walls
│   └── Delete and re-place
├── Missing floor boundary
│   └── Add room separation lines
└── Doors open to wrong side
    └── Flip host wall or door hand

Repair Workflow:
1. Run Audit (File > Open > Audit)
2. Check for warnings (V key)
3. Fix in order: Walls > Floors > Ceilings > Openings
4. Verify room boundaries
5. Re-run interference check
```

### Worksharing Pitfalls

```
Worksharing Errors:
├── Worksets closed when needed
│   └── Open worksets for editing
├── Edit conflicts (same element)
│   └── Request ownership, wait for release
├── Syncing during edit
│   └── Complete edit before sync
├── Forgot to relinquish
│   └── Use Relinquish All Mine
├── Central model locked
│   └── Check if user is still connected
└── Local file out of sync
    └── Reload latest, reconcile

Recovery:
1. Keep local backups
2. Don't delete .rdl files
3. Use Recover on corrupted central
4. Restore from workshared backup
```

### MEP Modeling Pitfalls

```
Common MEP Errors:
├── Ducts not connected
│   └── Use Connect mode
├── Pipe system not connected
│   └── Check system type matches
├── Equipment not in system
│   └── Connect to system
├── Oversized ducts/pipe
│   └── Check routing preferences
├── Fittings too detailed
│   └── Use simple fittings for coordination
├── Missing rise/fall symbols
│   └── Add MEP symbols manually
└── System color override missing
    └── Set up system visual styles

MEP Best Practices:
1. Route in plenum space first
2. Maintain minimum clearances
3. Use routing preferences
4. Keep systems organized
5. Connect all equipment
6. Check system diagrams
```

## 10.2 Performance Issues

### Model Performance

| Issue | Symptom | Cause | Solution |
|-------|---------|-------|----------|
| Slow editing | Multi-second lag | Complex geometry, many elements | Use worksets, hide others |
| Slow view switching | View takes long to load | Complex view templates | Simplify view filters |
| Slow regenerating | "Regenerating model" | Heavy operations | Disable grass, simplify |
| Large file size | Slow save/open | Too much detail | Purge, reduce detail |
| Memory error | Out of memory | 32-bit limitation | Use 64-bit, lighten models |

### Large Model Best Practices

```
Large Model Optimization:
├── [ ] Enable worksharing with worksets
├── [ ] Use workset visibility
│   └── Isolate discipline as needed
├── [ ] Lighten linked models
│   └── Linked RVT can be lightweight
├── [ ] Simplify families
│   └── Use simplified geometry
├── [ ] Reduce imported CAD
│   └── Convert to Revit geometry
├── [ ] Use design options for schemes
│   └── Only show active option
├── [ ] Suppress detail in large views
│   └── Set detail level to coarse
├── [ ] Limit detail groups
│   └── Explode detail groups when done
├── [ ] Use sub-assemblies
│   └── Split into linked models
└── [ ] Close unused views
    └── Reduce memory usage
```

### View Performance

```
View Optimization:
├── Crop regions to area of interest
├── Use scoping box for detail views
├── Set appropriate detail level
│   ├── Coarse: Overview
│   ├── Medium: Standard coordination
│   └── Fine: Fabrication/CDs
├── Disable imported CAD in large views
├── Remove unnecessary annotations
├── Limit detail groups
├── Use templates to standardize
└── Avoid overrides on many elements

Detailing Performance:
├── Copy view with details > New view
├── Use reference other view for details
├── Group similar components
└── Use detail components over families
```

### Family Performance

```
Family Optimization:
├── Use simple geometry
│   └── Avoid nested families
├── Reduce reference planes
│   └── Only necessary planes
├── Use type catalog vs loaded
│   └── Load only needed types
├── Simplify parametric relationships
│   └── Avoid complex constraints
├── Limit visibility parameters
│   └── Use shared coordinates
├── Profile families > solid extrusion
│   └── Use voids for cutouts
└── Check family for warnings
    └── Fix before loading
```

### File Size Management

```
Reduce Model Size:
├── Audit and recover
│   └── File > Open > Recover
├── Purge unused elements
│   └── Manage > Purge Unused
├── Remove broken links
│   └── Delete unused RVT links
├── Delete view templates not used
├── Remove imported CAD
│   └── Convert to Revit geometry
├── Reduce material assets
│   └── Textures, render assets
├── Use replace item for references
│   └── Manage > Replace Item
└── Save as new file
    └── Compact on save

File Size Targets:
| Building Size | Target | Warning |
|---------------|--------|---------|
| Small (<5000m²) | < 100 MB | > 200 MB |
| Medium (5000-20000m²) | 100-300 MB | > 500 MB |
| Large (>20000m²) | 300-800 MB | > 1.5 GB |
```

## 10.3 Data Loss & Recovery

### Backup Strategy

```
Backup Protocol:
├── Local Backup
│   ├── Auto-save every 15-30 minutes
│   ├── Local copies before sync
│   └── Daily local backup
├── Central Model Backup
│   ├── Worksharing backup (central)
│   ├── Daily backup before overnight
│   └── Weekly archive
└── Project Archive
    ├── Phase milestones
    ├── Major coordination points
    └── Issued for construction

Auto-Save Settings:
├── File > Options > Save
├── Automatically save every: 15 min
├── Create backup on each save: Yes
├── Maximum backups to keep: 99
└── Backup folder: Project folder
```

### Recovery Procedures

```
Recovery Options:

1. AutoRecover
   └── Recovered files in: %TEMP%\Revit
   Location: File > Open > Recover

2. Workshared Recovery
   ├── Backup (.rdl) files exist
   ├── Central model backup exists
   └── Worksharing > Recover Central

3. Local File Recovery
   ├── Keep .rvt.local files
   ├── .000, .001 backup files
   └── Try opening backup

4. Audit and Fix
   ├── File > Open > Audit
   └── Fix any errors found

5. Reload Latest
   ├── Worksets > Reload Latest
   └── From central model
```

### Common Corruption Symptoms

```
Signs of Corruption:
├── Model won't open
├── Elements disappear
├── Views are blank
├── File size suddenly increases
├── Performance degradation
├── Sync failures
└── Crashes on specific operations

Prevention:
├── Don't edit during sync
├── Keep disk space free
├── Use UPS for power protection
├── Keep worksets organized
├── Don't exceed file size limits
└── Regular backups
```

### Troubleshooting Reference

```
Common Revit Warnings:

Warning: "Some elements are missing reference lines"
└── Delete and recreate affected elements

Warning: "Elements that reference deleted elements"
└── Use Delete Imported
    
Warning: "Rooms exist that are not bounded"
└── Adjust room boundary lines
    
Warning: "Duct/pipe segments are too short"
└── Adjust minimum length in routing

Warning: "Inconsistent junction"
└── Re-connect fitting

Warning: "Element is not connected"
└── Connect to system or delete
```
