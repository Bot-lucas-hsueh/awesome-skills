# Standard Workflow

## 8.1 Project Workflow

### Phase 1: Template Setup

```
Template Configuration Workflow
├── 1. System Options (Tools > Options > System Options)
│   ├── Default Template (set part/assembly/drawing)
│   ├── Reference Geometry (ambient/light)
│   ├── Drawings (default sheet size)
│   └── Backup/Auto-save settings
├── 2. Document Properties
│   ├── Units (MMGS, IPS, etc.)
│   ├── Drafting Standard (ISO, ANSI, JIS)
│   ├── Dimensioning Standard
│   ├── Material Properties
│   └── Detailing Options
├── 3. Feature Tree Organization
│   ├── Consistent naming conventions
│   ├── Folder structure for large assemblies
│   └── Configuration folders
├── 4. Standard Components Library
│   ├── Fasteners (ISO/ANSI)
│   ├── Bearings
│   ├── Electrical connectors
│   └── Standard profiles
├── 5. Custom Library Creation
│   ├── FeatureScope library
│   ├── Toolbox (built-in)
│   └── Custom design library
└── 6. Save as Template (.prtdot, .asmdot, .drwdot)
```

### Phase 2: Part Creation

```
Part Creation Workflow
├── 1. Start from template (Ctrl+N)
├── 2. Create base sketch
│   ├── Select plane (Front, Top, Right)
│   ├── Set units display
│   └── Begin sketching
├── 3. Define profile geometry
│   ├── Use construction centerlines
│   ├── Apply geometric relations
│   ├── Add dimensions
│   └── Close profile
├── 4. Create base feature
│   ├── Extrude Boss/Base (blind, through all, etc.)
│   ├── Revolve (rotational parts)
│   ├── Sweep (沿路径)
│   └── Loft (过渡)
├── 5. Add features
│   ├── Cut features
│   ├── Holes (Hole Wizard)
│   ├── Fillets and chamfers
│   ├── Draft (mold parting)
│   └── Shell (hollow parts)
├── 6. Apply materials
│   ├── Assign from library
│   └── Define custom materials
└── 7. Configure (if needed)
    ├── Design tables
    ├── Configurations
    └── Suppress states
```

### Phase 3: Assembly Workflow

```
Assembly Workflow
├── 1. Start assembly from template
├── 2. Insert first component (ground)
│   ├── First part = origin/grounded
│   └── Insert Component (Ctrl+M)
├── 3. Add subsequent components
│   ├── Drag from browser or file
│   ├── Use Smart Mates for auto-alignment
│   └── Add Mate commands
├── 4. Apply mates
│   ├── Coincident (surface/plane contact)
│   ├── Concentric (axial alignment)
│   ├── Parallel (surface parallel)
│   ├── Distance (offset)
│   ├── Angle (rotation)
│   └── Width (centered in slot)
├── 5. Organize assembly
│   ├── Use folders in FeatureManager
│   ├── Rename components
│   ├── Color code by status
│   └── Use display states
└── 6. Validate assembly
    ├── Move/Rotate components
    ├── Interference detection
    ├── Clearance verification
    └── Mass properties check
```

### Phase 4: Drawing Documentation

```
Drawing Creation Workflow
├── 1. Start from drawing template
├── 2. Insert model
│   ├── Drag from browser
│   └── Select template view
├── 3. Create views
│   ├── Standard 3-View (Front, Top, Right)
│   ├── Isometric view
│   ├── Section views
│   ├── Detail views
│   └── Broken views
├── 4. Add dimensions (Model Items)
│   ├── Import from 3D model
│   ├── Add additional dimensions
│   └── Add GD&T symbols
├── 5. Add annotations
│   ├── Surface finish (ISO/ASME)
│   ├── Geometric tolerances
│   ├── Weld symbols
│   ├── Leader text
│   └── Balloons (for assemblies)
├── 6. Add notes and tables
│   ├── General notes
│   ├── Revision table
│   ├── Bill of Materials (BOM)
│   └── Hole/Thread specifications
└── 7. Final review and print
    ├── Check all views
    ├── Verify dimensions
    └── Export to PDF/DXF
```

## 8.2 Collaboration Workflow

### Top-Down Assembly Design

```
Top-Down Workflow
├── 1. Create skeleton model
│   ├── Master skeleton part
│   ├── Define reference geometry
│   ├── Coordinate systems
│   └── Interface planes
├── 2. Layout sketches
│   ├── Define component envelopes
│   ├── Define clearance zones
│   └── Define motion paths
├── 3. Insert skeleton into assembly
│   ├── New Assembly
│   ├── Insert skeleton first
│   └── Ground skeleton
├── 4. Create components in context
│   ├── Insert > New Part
│   ├── Edit in assembly context
│   └── Reference skeleton geometry
├── 5. Link sketches to skeleton
│   ├── Convert entities
│   ├── Link dimensions
│   └── Maintain parametric relationships
└── 6. Component independence
    └── Make independent when complete
```

### Bottom-Up Assembly Design

```
Bottom-Up Workflow
├── 1. Design individual parts
│   ├── Create parts independently
│   ├── Apply standard interfaces
│   └── Maintain design intent
├── 2. Create sub-assemblies
│   ├── Group related parts
│   ├── Apply sub-assembly mates
│   └── Test sub-assembly
├── 3. Create top-level assembly
│   ├── Insert sub-assemblies
│   ├── Apply inter-sub-assembly mates
│   └── Verify fit and function
└── 4. Manage inter-part references
    ├── Virtual components
    ├── External references
    └── Rebuild management
```

### Design Tables & Configurations

```
Configuration Workflow
├── 1. Design part with parameters
│   ├── Add global variables
│   ├── Use equations
│   └── Define dimensions
├── 2. Create design table
│   ├── Insert > Tables > Design Table
│   ├── Excel opens in embedded mode
│   └── Define configurations
├── 3. Edit design table
│   ├── Column: Dimension names ($value)
│   ├── Column: Suppression state ($state)
│   ├── Column: Custom properties ($PRP:)
│   └── Row: Configuration name
├── 4. Manage configurations
│   ├── Add new configuration
│   ├── Delete configuration
│   ├── Suppress features per config
│   └── Rename configurations
└── 5. Extract configuration data
    ├── BOM by configuration
    └── Custom properties report
```

## 8.3 QA/QC Workflow

### Part Validation Checklist

```
Part Quality Checklist
├── [ ] Units correct (MMGS/IPS)
├── [ ] Material assigned
├── [ ] Mass properties reasonable
├── [ ] Geometry validates design intent
├── [ ] Draft angles specified (molded parts)
├── [ ] Wall thickness consistent
├── [ ] Fillet sizes appropriate
├── [ ] Hole specifications correct
│   ├── Tap drill vs clearance
│   ├── Thread depth
│   └── Counterbore/d countersink
├── [ ] Custom properties filled
│   ├── Part Number
│   ├── Description
│   ├── Material
│   └── Revision
├── [ ] Drawings match model
└── [ ] No rebuild errors
```

### Assembly Validation

```
Assembly Quality Checklist
├── [ ] All mates fully defined
├── [ ] No redundant mates
├── [ ] No broken references
├── [ ] Interference check passed
├── [ ] Clearance distances verified
├── [ ] Motion range verified
├── [ ] Component positions logical
├── [ ] Fastener patterns complete
├── [ ] Standard parts used
├── [ ] BOM accurate
├── [ ] Configuration as designed
└── [ ] Lightweight resolved
```

### Drawing Review

```
Drawing Quality Checklist
├── [ ] All views aligned
├── [ ] Dimensions match 3D model
├── [ ] Tolerances specified
├── [ ] Units displayed correctly
├── [ ] Drawing scale specified
├── [ ] Title block complete
│   ├── Part/Assembly number
│   ├── Description
│   ├── Revision
│   ├── Scale
│   ├── Drawn by/Date
│   └── Checked by/Date
├── [ ] Section views have cutting lines
├── [ ] Detail views have callout circles
├── [ ] Surface finish specified
├── [ ] GD&T symbols correct
├── [ ] Revision table updated
├── [ ] Notes complete
└── [ ] Bill of Materials correct
```

### Revision Control

```
Revision Workflow
├── 1. Increment revision
│   ├── Tools > Equations > Revision
│   ├── Update custom property
│   └── Change revision in title block
├── 2. Document changes
│   ├── ECN (Engineering Change Notice)
│   ├── ECO (Engineering Change Order)
│   └── Change description
├── 3. Update affected files
│   ├── Part revisions
│   ├── Assembly references
│   └── Drawing links
├── 4. Archive previous version
│   ├── PDM vault revision history
│   ├── Manual file naming: _RevA, _RevB
│   └── Archive folder structure
└── 5. Notify stakeholders
    ├── Design team
    ├── Manufacturing
    └── Procurement
```
