# Standards & Reference

## 7.1 Official Documentation

- [Revit Help Documentation](https://help.autodesk.com/view/RVT/2024/ENU/)
- [Revit API Reference](https://www.revitapidocs.com/2024/)
- [Revit Architecture Forum](https://forums.autodesk.com/t5/revit-architecture-forum/bd-p/117)
- [Revit Structure Forum](https://forums.autodesk.com/t5/revit-structure-forum/bd-p/118)
- [Revit MEP Forum](https://forums.autodesk.com/t5/revit-mep-forum/bd-p/119)
- [Revit BIM Management](https://www.autodesk.com/revit/bim-management)
- [Revit Learning Pathways](https://www.autodesk.com/training-center/revit)
- [Revit Certification](https://www.autodesk.com/certification/revit)

## 7.2 BIM Standards & Naming Conventions

### Project Organization (LOD 300+)

```
Project Browser Organization:
├── Project Parameters
│   ├── Shared Parameters
│   ├── Project Parameters
│   └── Global Parameters
├── Families
│   ├── Architectural
│   │   ├── Walls
│   │   ├── Doors
│   │   ├── Windows
│   │   ├── Curtain Walls
│   │   ├── Roofs
│   │   └── Stairs
│   ├── Structural
│   │   ├── Columns
│   │   ├── Framing
│   │   ├── Foundations
│   │   └── Connections
│   ├── MEP
│   │   ├── Mechanical
│   │   ├── Electrical
│   │   └── Plumbing
│   └── Annotation
│       ├── Tags
│       ├── Symbols
│       └── Detail Components
├── Linked Models
│   ├── Architecture
│   ├── Structure
│   └── MEP Coordination
└── Sheets (all sheets)
```

### Element Naming Standards

| Element Type | Naming Format | Example |
|--------------|---------------|---------|
| Wall Type | [Function]-[Thickness] | Generic - 200mm |
| Door Family | [Type]-[Width]x[Height] | Single - 900x2100 |
| Window Family | [Type]-[Width]x[Height] | Fixed - 1200x1500 |
| Column | [Size]-[Type] | W310x97 |
| Beam | [Type]-[Size] | W16x26 |
| Room | [Level]-[Number] | Level 1 - 101 |

### Shared Parameters

```
Common Shared Parameters:
├── Project Information
│   ├── Project Name
│   ├── Project Number
│   ├── Project Address
│   ├── Client Name
│   └── Phase
├── Element Data
│   ├── Mark
│   ├── Description
│   ├── Material
│   ├── Manufacturer
│   ├── Cost
│   └── Issue Date
├── Coordination
│   ├── Level of Development
│   ├── Linked Model
│   ├── Design Status
│   ├── Issue Status
│   └── Federated By
└── MEP Specific
    ├── System Type
    ├── Flow Rate
    ├── Velocity
    ├── Pressure
    └── Equipment Tag
```

### Workset Standards

```
Workset Organization by Discipline:
Architectural Worksets:
├── A-Walls
├── A-Floors
├── A-Roofs
├── A-Ceilings
├── A-Doors
├── A-Windows
├── A-Stairs
├── A-Railings
├── A-Furniture
└── A-Annotations

Structural Worksets:
├── S-Foundations
├── S-Columns
├── S-Walls
├── S-Floors
├── S-Framing
└── S-Connections

MEP Worksets:
├── M-HVAC
├── M-Piping
├── M-Equipment
├── E-Power
├── E-Lighting
├── E-Communications
├── P-Plumbing
└── P-Fixtures

Common Worksets:
├── C-Coordination
├── C-Site
└── C-Reference
```

## 7.3 Common Revit Commands

### Building Elements

| Command | Description | Location |
|---------|-------------|----------|
| Wall | Create architectural wall | Architecture > Build > Wall |
| Floor | Create floor slab | Architecture > Build > Floor |
| Roof | Create roof by footprint/extrusion | Architecture > Build > Roof |
| Ceiling | Create ceiling plane | Architecture > Build > Ceiling |
| Door | Place door family | Architecture > Build > Door |
| Window | Place window family | Architecture > Build > Window |
| Component | Place loadable family | Architecture > Build > Component |
| Stairs | Create stairs by sketch | Architecture > Circulation > Stairs |
| Railing | Create railing system | Architecture > Circulation > Railing |
| Column | Place architectural column | Architecture > Build > Column |
| Curtain Wall | Create curtain wall | Architecture > Build > Curtain Wall |

### Structure Elements

| Command | Description | Location |
|---------|-------------|----------|
| Structural Column | Place structural column | Structure > Foundation > Column |
| Beam | Create beam system | Structure > Structure > Beam |
| Framing | Place beam/framing element | Structure > Structure > Framing |
| Foundation | Create foundation elements | Structure > Foundation |
| Wall Foundation | Create wall foundation | Structure > Foundation > Wall Foundation |
| Isolated Foundation | Create pad footing | Structure > Foundation > Isolated Foundation |
| Slab Foundation | Create mat foundation | Structure > Foundation > Slab |
| Truss | Create structural truss | Structure > Structure > Truss |
| Connection | Add structural connections | Structure > Connections |

### Annotation & Documentation

| Command | Description | Location |
|---------|-------------|----------|
| Dimension | Place dimension | Annotate > Dimension > Aligned |
| Text | Add text note | Annotate > Text > Text |
| Tag | Tag element by category | Annotate > Tag > Tag by Category |
| Keynote | Add keynote | Annotate > Tag > Material Tag |
| Detail Line | Draw 2D detail lines | Annotate > Detail > Detail Line |
| Section | Create section view | View > Create > Section |
| Elevation | Create elevation view | View > Create > Elevation |
| Callout | Create detail callout | View > Create > Callout |
| Schedule | Create schedule/quantity | View > Create > Schedule/Quantities |
| Sheet | Create drawing sheet | View > Create > Sheet |

### Collaboration Tools

| Command | Description | Location |
|---------|-------------|----------|
| Link CAD | Import/Link DWG, DGN, DWF | Insert > Link CAD |
| Link Revit | Link RVT model | Insert > Link Revit |
| Workset | Manage worksets | Collaborate > Worksets |
| Copy/Monitor | Monitor linked model elements | Collaborate > Copy/Monitor |
| Coordination Review | Coordination verification | Add-Ins > BIM 360 |
| Publish | Publish to BIM 360/ACC | Collaborate > Publish |

## 7.4 Version Compatibility

| Version | Release Year | File Format | RVT Compatibility |
|---------|--------------|-------------|-------------------|
| Revit 2020 | 2019 | 2020 | Save to 2019/2018 |
| Revit 2021 | 2020 | 2021 | Save to 2020/2019 |
| Revit 2022 | 2021 | 2022 | Save to 2021/2020 |
| Revit 2023 | 2022 | 2023 | Save to 2022/2021 |
| Revit 2024 | 2023 | 2024 | Save to 2023/2022 |

### Interoperability

```
Import/Export Formats:
├── DWG (AutoCAD) - Full round-trip
├── DXF - 2D data exchange
├── DGN (MicroStation) - Bentley format
├── IFC - Industry Foundation Classes
│   └── IFC2x3, IFC4, IFC4x1, IFC4x2, IFC4x3
├── gbXML - Energy analysis data
├── COBie - Construction Operations data
├── SKP (SketchUp) - Import only
├── DWF/DWFx - Markup and review
├── PDF - Export only
├── NWC/NWD - Navisworks cache
└── FBX - 3D interchange

Recommended Versions:
├── IFC: IFC4x2 (current standard)
├── DWG: 2018 (widest compatibility)
└── DWF: 2018 or later
```

## 7.5 File Formats

| Format | Extension | Description | Use Case |
|--------|-----------|-------------|----------|
| Project | .rvt | Native Revit project | Primary project file |
| Family | .rfa | Loadable family library | Components, families |
| Template | .rvt | Project template | Start new projects |
| Family Template | .rft | Family template | Create new families |
| Library | .rvt | Family library | Grouped families |
| Workshared | .rvt + .rdl | Central model | Team collaboration |
| Backup | .000, .001 | Auto-save backup | Recovery |
| Journal | .log | Operation history | Troubleshooting |
| Export CAD | .dwg, .dxf, .dgn | 2D drawings | Deliverables |
| Export 3D | .dwg 3D, .ifc | 3D model | Coordination |
| Navisworks | .nwc, .nwf | Cache files | Clash detection |
| BIM 360 | Cloud | Collaboration | Teamwork |

### Workshared Project Files

```
Central Model Files:
├── Project.rvt (central model - server)
├── Project.rvt (local copy - user)
├── Project.rvt.rdl (workshared data lock)
└── Project-Username.rvt (local file)

User Workflow:
1. Sync with central (get latest)
2. Edit locally
3. Relinquish ownership
4. Sync to central (push changes)
```

### File Size Guidelines

| Project Type | Typical Size | Large Warning |
|--------------|--------------|---------------|
| Small (< 5000 m²) | < 50 MB | > 100 MB |
| Medium (5000-20000 m²) | 50-150 MB | > 300 MB |
| Large (> 20000 m²) | 150-500 MB | > 1 GB |
| Campus/Multi-building | 500 MB-2 GB | > 5 GB |

### LOD Levels (BIM)

| LOD | Level | Description | Elements |
|-----|-------|-------------|----------|
| LOD 100 | Conceptual | Approximate geometry | Area, volume |
| LOD 200 | Approximate | Generic systems | Schematic systems |
| LOD 300 | Detailed | Specific components | Actual equipment |
| LOD 350 | Detailed | With connections | Coordinated MEP |
| LOD 400 | Fabrication | Shop-ready | Fabrication drawings |
| LOD 500 | As-Built | Field verified | Facility management |
