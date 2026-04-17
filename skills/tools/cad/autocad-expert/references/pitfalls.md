# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Fix |
|---|---------|----------|--------|-----|
| 1 | Wrong units (mm vs inches) | 🔴 Critical | Wrong scale entire drawing | Check UNITS at start |
| 2 | Dimension scale mismatch | 🔴 Critical | Dimensions wrong on plot | Set DIMSCALE = plot scale |
| 3 | Exploding dimensions | 🔴 Critical | Lose associativity | Never EXPLODE dimensions |
| 4 | Using 0,0 as base point | 🟡 High | Xrefs shift | Use survey base point |
| 5 | Nested xrefs without paths | 🟡 High | Missing references | Use relative paths |
| 6 | Hard-coded plot scales | 🟡 High | Replot required | Use annotative scaling |
| 7 | Plotting from model space | 🟡 High | Wrong scale | Use layout/paperspace |
| 8 | Overwriting template | 🟡 High | Lost settings | Save template as new file |
| 9 | Non-standard layer names | 🟡 High | Coordination issues | Follow office standard |
| 10 | Missing sheet border | 🟡 Medium | Rejected deliverable | Include title block |

### Dimension Pitfalls

```
Common Dimension Errors:
├── DIMLFAC set wrong (usually -1 for paperspace dims)
├── DIMASSOC = 0 (non-associative)
├── Dimension style not annotative
├── Using linear dims on angled objects
├── Dimensions not updating after edit
└── Decimal places inconsistent

Correct approach:
1. Set DIMASSOC = 2 (fully associative)
2. Create annotative dimension styles
3. Match DIMSCALE to viewport scale
4. Use associative dimensions
5. Never explode dimensions
```

### Layer Pitfalls

```
Common Layer Errors:
├── Objects on wrong layer
├── Layer locked/ frozen accidentally
├── Color = BYLAYER violated
├── Linetype = BYLAYER violated
├── Lineweight = BYLAYER violated
├── Layer created but not used
├── Duplicate layer names (case differences)
└── Offending layers (cannot be deleted)

Prevention:
- Audit layers regularly (LAYERCHECK)
- Use layer states to save/restore
- Never use layer 0 unless appropriate
- Filter layers by discipline
```

### Reference File Pitfalls

```
Common XREF Problems:
├── Missing xref after move
├── Orphaned xrefs (deleted source)
├── Path type: Full vs Relative
├── Nested xref load order
├── Xref overlaid instead of attached
├── Circular xref references
└── Version mismatch (DWG format)

Solutions:
1. Use relative paths: File > External References > Path Type
2. Bind xrefs before archiving: XREF > Bind
3. Audit with XREF command regularly
4. Keep xref names short, no spaces
```

## 10.2 Performance Issues

### Drawing Performance

| Issue | Symptom | Cause | Solution |
|-------|---------|-------|----------|
| Slow regeneration | Delay after zoom/pan | Too many hatches, complex geometry | Use HATCHRESET, simplify geometry |
| Large file size | Slow save/load | Embedded images, excess blocks | PURGE all, compress images |
| Slow selection | Delay picking objects | Too many objects, complex selection | Use ISOLATE, reduce view |
| Slow dimensioning | Lag when placing dims | Large dimension styles | Create simpler styles |
| Crash on save | Save fails, corruption | Full disk, network issue | Save locally first |

### Optimization Commands

```autocad
; Performance tuning
OPTIONS
; Performance tab:
; - Hardware acceleration: ON
; - Object selection cursor: Simple
; - Point display: 3D, reduced points
; - Geometry in tooltips: OFF

; Regenerate all
( Command "REGENALL" )

; Clean up
PURGE ALL (purge all unused)
AUDIT Y (fix errors)
-EXPLODEALL (explode proxy objects)

; Hatch optimization
HATCHRESET
HATCHEDIT > Recompute boundary
```

### Large File Management

```
Large Drawing Best Practices:
├── Keep files < 50MB
├── Break into discipline files
├── Use xrefs for reference data
├── External link blocks vs embedded
├── Raster images: clip or reduce
├── Use proxies for non-native objects
├── Save in 2018 DWG format
└── Regular AUDIT and PURGE

When file is too large:
1. Audit: AUDIT Y
2. Purge: PURGE ALL
3. Reduce: -EXTERNALREFERENCES > Detach unused
4. Explode: EXPLODE blocks
5. Audit again: AUDIT Y
```

### Viewport Performance

```
Paper Space Performance:
├── Minimize viewports on sheets
├── Turn off unused layers in vports
│   └── LAYERVPFFZ (viewport freeze)
├── Avoid 3D views in layout
├── Use REGENMODE 0 for faster regen
└── Lock viewports after setup

3D Performance:
├── Hide instead of isolate
├── Use visual styles (2D Wireframe)
├── Reduce detail levels
├── Limit dynamic UCS usage
└── Use region operations sparingly
```

## 10.3 File Corruption & Recovery

### Prevention

```
Backup Strategy:
├── AutoSave: Every 10-15 minutes
│   └── OPTIONS > Open and Save > AutoSave path
├── Incremental saves: _bak, _abk, _bbk...
├── Network backup to server
├── Version control (BIM 360, AutoCAD Web)
└── Before major operations, save copy

Drawing Recovery:
├── Backup folder: %TEMP%
├── Use DWWGRECOV command
├── Recover after crash: RECOVER command
└── Use Drawing Recovery Manager
```

### Recovery Commands

```autocad
; Open backup file
; File > Open > Select .bak or .sv$ file

; Recover drawing
RECOVER
; Select damaged file
; AutoCAD audits and reports

; Salvage drawing
DWWGRECOV
; Attempts to recover salvageable data

; Audit and fix
AUDIT Y
; Y = fix errors automatically
```

### Common Corruption Symptoms

```
Signs of Corruption:
├── Cannot open file
├── Missing objects after save
├── Unexpected geometry changes
├── Symbol tables corrupted
├── Dimension styles lost
├── Blocks missing
└── Layers disappeared

Recovery Steps:
1. Try opening .bak file
2. Try DXF export/import
3. Try RECOVER command
4. Try WBLOCK to extract geometry
5. Try Recover Block manager
6. Restore from last known good
```
