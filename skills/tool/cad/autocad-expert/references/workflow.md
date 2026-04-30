# Standard Workflow

## 8.1 Project Workflow

### Phase 1: Template Setup

```
Template Creation Workflow
├── 1. Start from default template (ACADISO.dwt)
├── 2. Set up drawing units (UNITS)
│   ├── Type: Decimal
│   ├── Precision: 0.00
│   └── Units: Millimeters/Meters
├── 3. Configure layers (LAYER)
│   ├── Create layer structure by discipline
│   ├── Assign layer colors (ACI)
│   ├── Assign linetypes
│   └── Set lineweights
├── 4. Set up dimension styles (DIMSTYLE)
│   ├── Scale for model/paper space
│   ├── Set text height
│   ├── Configure tolerances
│   └── Assign arrows
├── 5. Create text styles (STYLE)
├── 6. Set up title block
│   ├── Create border block
│   ├── Add title block attributes
│   └── Insert into layout
├── 7. Configure viewport settings
└── 8. Save as project template (.dwt)
```

### Phase 2: Drafting Workflow

```
Drafting Workflow
├── 1. Open project template
├── 2. Set up coordinate system
│   ├── Establish origin point
│   ├── Configure UCS if needed
│   └── Set snap intervals (OSNAP)
├── 3. Create geometry
│   ├── Use appropriate precision
│   ├── Apply layer standards
│   └── Maintain consistent snap
├── 4. Add annotations
│   ├── Dimensions (use associative)
│   ├── Text labels
│   ├── Leaders and notes
│   └── Symbols
└── 5. Save regularly (.dwg)
```

### Phase 3: Plotting Workflow

```
Plotting Workflow
├── 1. Configure page setup (PAGESETUP)
│   ├── Select plotter/printer
│   ├── Set paper size
│   ├── Configure plot area (Layout/Window)
│   ├── Set plot offset
│   └── Plot scale (usually 1:1 for models)
├── 2. Apply plot style (CTB or STB)
│   ├── Color-dependent (CTB) - Traditional
│   └── Named plot styles (STB) - Modern
├── 3. Preview plot (PREVIEW)
├── 4. Plot to PDF or plotter
└── 5. Archive plot log
```

## 8.2 Collaboration Workflow

### External References (XREF)

```
XREF Workflow
├── Attach Reference
│   ├── File > Attach DWG
│   ├── Path type: Relative (preferred)
│   └── Insertion point, scale, rotation
├── Reference Types
│   ├── Overlay - Isolated, won't load nested
│   └── Attachment - Includes nested refs
├── Manage References
│   ├── XREF manager (XR)
│   ├── Reload - Update from disk
│   ├── Detach - Remove reference
│   └── Bind - Convert to block
└── Best Practices
    ├── Use relative paths
    ├── Keep xref names simple
    └── Maintain folder structure
```

### Block Management

```
Block Workflow
├── Create Block (B)
│   ├── Define base point
│   ├── Select objects
│   ├── Convert to block
│   └── Assign name (prefix with discipline)
├── Insert Block (I)
│   ├── Specify insertion point
│   ├── Set scale factors
│   └── Specify rotation
├── Edit Block Definition
│   ├── Block Editor (BEDIT)
│   ├── Dynamic blocks allow parameters
│   └── Save changes (BMAKE)
└── Purge Unused
    └── PURGE command removes unused defs
```

### Sheet Set Management

```
Sheet Set Workflow
├── Create Sheet Set (SHEETSET)
│   ├── Choose template
│   ├── Name the set
│   └── Define resource locations
├── Add Sheets
│   ├── Layouts to include
│   ├── Create new sheets
│   └── Subset organization
├── Resource Drawing
│   ├── Title block resource
│   ├── Sheet list table
│   └── Callout blocks
├── Publish
│   ├── Single PDF
│   ├── Multi-sheet PDF
│   └── DWF/DWFx
└── Archive
    └── Bundle entire sheet set
```

## 8.3 QA/QC Workflow

### Quality Checklist

```
Pre-Submission Review
├── [ ] Units correct (metric/imperial)
├── [ ] Layer standards followed
├── [ ] Dimension styles consistent
├── [ ] Text heights appropriate for scale
├── [ ] Scale bar if not 1:1
├── [ ] North arrow on plans
├── [ ] Title block complete
├── [ ] Coordinates match project base
├── [ ] No duplicate layers
├── [ ] Unused blocks purged
├── [ ] Xrefs loaded correctly
├── [ ] DWG version compatible
└── [ ] File size reasonable (<50MB typical)
```

### Layer Audit Process

```python
# Layer Report Script (AutoLISP)
(defun c:LayerReport ( / layerData)
  (setq layerData (tblnext "LAYER" T))
  (while layerData
    (princ (strcat (cdr (assoc 2 layerData)) 
                   " | Color: " 
                   (itoa (cdr (assoc 62 layerData)))
                   " | Lt: "
                   (cdr (assoc 6 layerData))
                   "\n"))
    (setq layerData (tblnext "LAYER")))
  (princ))
```

### Coordination Review

```
Inter-Discipline Review
├── Overlay drawings in model space
├── Check for conflicts
│   ├── Structural vs Architectural
│   ├── MEP vs Architectural
│   └── Structural vs MEP
├── Create conflict log
│   ├── Issue number
│   ├── Description
│   ├── Location (coordinates)
│   ├── Priority (High/Med/Low)
│   └── Status (Open/Resolved)
└── Issue RFI if needed
```

### Revision Control

```
Drawing Revision Workflow
├── Increment revision block
│   ├── Add revision cloud
│   ├── Circle affected areas
│   └── Update revision table
├── Document changes
│   ├── Create issue log
│   ├── Record change descriptions
│   └── Note date and author
├── Archive previous version
│   ├── Add suffix: _RevA, _RevB
│   ├── Store in project archive folder
│   └── Maintain backup copy
└── Notify team of updates
```
