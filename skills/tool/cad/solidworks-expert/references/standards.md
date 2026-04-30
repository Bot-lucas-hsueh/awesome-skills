# Standards & Reference

## 7.1 Official Documentation

- [SolidWorks Help Documentation](https://help.solidworks.com/2024/English/SolidWorks/sldworks/HDEFAULT.htm)
- [SolidWorks API Reference](https://help.solidworks.com/2024/English/api/sldworksapi/SolidWorks_Interop.html)
- [SolidWorks 3DEXPERIENCE Academy](https://www.3ds.com/solutions/3dexperience-world)
- [SolidWorks Subscription Services](https://www.solidworks.com/sw/support)
- [SolidWorks Certification](https://www.solidworks.com/sw/certification.htm)
- [PDMWorks Enterprise (ENOVIA)](https://www.3ds.com/products-services/enovia/)

## 7.2 Standards & Naming Conventions

### Part File Naming

```
[Project]-[Discipline]-[Type]-[Number]-[Revision]
```

| Element | Example | Notes |
|---------|---------|-------|
| Project | PRJ123 | Project code |
| Discipline | MECH, ELEC, TOOL | Engineering discipline |
| Type | PART, ASSY, DRW | File type abbreviation |
| Number | 001-999 | Sequential number |
| Revision | A, B, C... | Revision letter |

**Example:** `PRJ123-MECH-PART-001-A.SLDPRT`

### Assembly Structure

```
Top Level Assembly (TLA)
├── Sub-Assembly 1
│   ├── Sub-Part 1.1
│   ├── Sub-Part 1.2
│   └── Standard Parts (fasteners)
├── Sub-Assembly 2
│   ├── Sub-Part 2.1
│   └── Purchased Part 2.2
└── Purchased Components
```

### Feature Tree Organization

```
Part Feature Tree:
├── Origin
├── Sketch 1 (Base Profile)
│   ├── Lines
│   ├── Arcs
│   └── Relations
├── Base Feature (Extrude/Boss)
├── Sketch 2 (Cut Profile)
├── Cut Feature
├── Fillets
├── Chamfers
├── Holes
├── Drafts
└── Shells
```

### Material Standards

| Material Family | SolidWorks Database | Typical Applications |
|-----------------|---------------------|----------------------|
| Aluminum | 6061-T6, 7075-T6 | Lightweight structures |
| Steel | AISI 1018, AISI 304 | General purpose |
| Stainless | 304, 316 | Corrosion resistance |
| Plastics | ABS, Nylon, Delrin | Consumer products |
| Composites | Carbon Fiber, GFRP | High strength/light |

## 7.3 Common Feature Commands

### Sketch Commands

| Command | Description | Shortcut |
|---------|-------------|----------|
| Sketch | Enter sketch mode | S |
| Line | Draw line segments | L |
| Rectangle | Draw rectangle | R |
| Circle | Draw circle | C |
| Arc | Draw tangent arc | A |
| Spline | Draw B-spline | Shift+S |
| Slot | Draw oblong slot | Shift+Alt+S |
| Centerline | Construction geometry | Ctrl+Shift+Alt+C |
| Smart Dimension | Add dimensions | Shift+S |
| Add Relation | Apply constraints | Ctrl+1 |
| Display/Delete Relations | Edit constraints | Ctrl+2 |
| Sketch Fillet | Round corners | G |
| Sketch Chamfer | Bevel corners | Shift+G |

### Feature Commands

| Command | Description | Shortcut |
|---------|-------------|----------|
| Extruded Boss/Base | Create 3D from profile | Boss-Extrude |
| Extruded Cut | Remove material | Cut-Extrude |
| Revolved Boss/Base | Create rotational part | Boss-Revolve |
| Revolved Cut | Remove rotational material | Cut-Revolve |
| Swept Boss/Base | Sweep along path | Boss-Sweep |
| Lofted Boss/Base | Blend between profiles | Boss-Loft |
| Hole Wizard | Create standardized holes | Hole Wizard |
| Fillet | Round edges | F |
| Chamfer | Bevel edges | Shift+C |
| Shell | Create hollow part | Shell |
| Draft | Add draft angles | Draft |
| Rib | Add structural rib | Rib |
| Dorsal | Add gusset | Dorsal |
| Mirror | Mirror features | Mirror |
| Linear Pattern | Pattern in one direction | LPattern |
| Circular Pattern | Pattern around axis | CPattern |
| Curve Driven Pattern | Pattern along curve | CurvePtn |

### Assembly Commands

| Command | Description | Shortcut |
|---------|-------------|----------|
| Insert Component | Add part to assembly | Ctrl+M |
| Mate | Constrain parts | M |
| Smart Mate | Auto-mate components | Shift+M |
| Move Component | Free movement | M (when no mate selected) |
| Rotate Component | Free rotation | R (when no mate selected) |
| Mirror Component | Create mirrored part | Mirror Component |
| Replace Component | Swap part | Replace Component |
| Edit Part | Edit in context | Double-click part |
| Edit Assembly | Return to assembly | Return to Assembly |

### Drawing Commands

| Command | Description | Shortcut |
|---------|-------------|----------|
| Drawing View | Insert standard view | Drawing View |
| Projected View | Create projected view | Projected View |
| Section View | Create section cut | Section View |
| Detail View | Create detail callout | Detail View |
| Broken View | Break long parts | Broken View |
| Alternate Position | Show motion range | Alternate Position |
| Model Items | Import dimensions | Insert > Model Items |
| Annotations | Add symbols/text | Annotation toolbar |

## 7.4 Version Compatibility

| Version | Release Year | File Format | Notes |
|---------|--------------|-------------|-------|
| SolidWorks 2020 | 2019 | sldprt/sldasm 28 | PDM 2020 |
| SolidWorks 2021 | 2020 | sldprt/sldasm 29 | 2021 SP5+ required |
| SolidWorks 2022 | 2021 | sldprt/sldasm 30 | 2022 SP0-4 compatibility |
| SolidWorks 2023 | 2022 | sldprt/sldasm 31 | 2023 SP5+ recommended |
| SolidWorks 2024 | 2023 | sldprt/sldasm 32 | 2024 current |

### Cross-Version Compatibility

- SolidWorks saves to last major version by default
- Save As options for older versions (back to SW 2006)
- Parasolid interchange (.x_t) for neutral format
- IGES (.igs) for surface geometry
- STEP (.stp) for solid geometry interchange
- eDrawings for version-free viewing

## 7.5 File Formats

| Format | Extension | Description | Use Case |
|--------|-----------|-------------|----------|
| Part | .sldprt | Native part file | 3D solid model |
| Assembly | .sldasm | Native assembly | Multi-part product |
| Drawing | .slddrw | Native drawing | 2D documentation |
| Part Template | .prtdot | Part template | Start new parts |
| Assembly Template | .asmdot | Assembly template | Start new assemblies |
| Drawing Template | .drwdot | Drawing template | Start new drawings |
| Sheet Format | .slddrt | Sheet format | Title block/layout |
| Block | .sldblk | Drawing block | Symbol library |
| Design Table | .xls/.xltb | Excel design table | Configurations |
| eDrawing | .easm/.eprt | Viewer format | Collaboration |
| Parasolid | .x_t/.x_b | Siemens geometry | Interop |
| IGES | .igs/.iges | Initial Graphics | Surface exchange |
| STEP | .stp/.step | ISO standard | 3D CAD exchange |
| STL | .stl | Stereolithography | 3D printing |
| 3D PDF | .pdf | Adobe 3D PDF | Viewing without CAD |
| DXF/DWG | .dxf/.dwg | 2D exchange | 2D CAD exchange |
| IDF | .emn/.pro | PCB interchange | Electronics |

### File Size Guidelines

| File Type | Typical Size | Large Warning |
|-----------|--------------|---------------|
| Simple Part | < 5 MB | > 20 MB |
| Complex Part | 5-50 MB | > 100 MB |
| Simple Assembly | < 20 MB | > 50 MB |
| Complex Assembly | 20-200 MB | > 500 MB |
| Large Assembly | 200-500 MB | > 1 GB |
| Drawing | < 10 MB | > 25 MB |
