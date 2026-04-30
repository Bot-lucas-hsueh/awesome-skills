# Standards & Reference

## 7.1 Official Documentation

- [AutoCAD Help Documentation](https://help.autodesk.com/view/ACADLT/2024/ENU/)
- [AutoCAD .NET API Reference](https://help.autodesk.com/view/ACADLT/2024/ENU/?guid=GUID-PARAMS)
- [AutoCAD Online Learning Path](https://www.autodesk.com/learn/topics/autocad)
- [AutoCAD Best Practices Blog](https://Autodesk.com/blogs/autocad)
- [AutoCAD Customization Guide](https://help.autodesk.com/view/ACADLT/2024/ENU/?guid=GUID-5F5B0E6F-4B0E-4F6E-A9D2-4E3D8C1B7F9A)

## 7.2 Layer Standards & Naming Conventions

### Standard Layer Naming Structure

```
[Prefix]-[Discipline]-[Type]-[Status]
```

| Prefix | Discipline | Type | Status |
|--------|------------|------|--------|
| A | Architectural | WALL | CONSTR |
| S | Structural | COL | EXIST |
| M | Mechanical | DUCT | DEMO |
| E | Electrical | LIGHT | PROJ |
| P | Plumbing | PIPE | NENT |
| F | Fire Protection | SPRNKR | REF |

### Standard AutoCAD Layer Colors (ACI)

| Color | Layer Purpose | Example |
|-------|---------------|---------|
| 1 Red | Primary object layer | A-WALL-CONSTR |
| 2 Yellow | Secondary/dimension | A-WALL-DIMS |
| 3 Green | Primary dimension | A-WALL-DIMS-PRIMARY |
| 4 Cyan | Grid/bubble | A-GRID |
| 5 Blue | Reference/demolition | A-WALL-EXIST |
| 7 White/Black | Default objects | A-WALL-PROJ |
| 9 Dark gray | Annotations | A-ANNO-TEXT |

### Text Styles

| Style Name | Font | Height | Width |
|------------|------|--------|-------|
| STANDARD | arial.ttf | 0 | 0.7 |
| DIM | arial.ttf | 0 | 0.7 |
| ANNO | isocp.ttf | 3.5 | 0.7 |
| TITLE | arialbd.ttf | 0 | 0.85 |

## 7.3 Common Commands Reference

### Drawing Commands

| Command | Full Name | Description | Shortcut |
|---------|-----------|-------------|----------|
| LINE | Line | Draw straight line segments | L |
| PLINE | Polyline | Draw connected line/arc segments | PL |
| ARC | Arc | Draw arc segments | A |
| CIRCLE | Circle | Draw circles | C |
| ELLIPSE | Ellipse | Draw ellipses | EL |
| SPLINE | Spline | Draw B-spline curves | SPL |
| HATCH | Hatch | Fill enclosed areas | H |
| REGION | Region | Create regions from closed loops | REG |

### Editing Commands

| Command | Full Name | Description | Shortcut |
|---------|-----------|-------------|----------|
| OFFSET | Offset | Create parallel copies | O |
| TRIM | Trim | Trim objects to boundaries | TR |
| EXTEND | Extend | Extend objects to boundaries | EX |
| FILLET | Fillet | Create rounded corners | F |
| CHAMFER | Chamfer | Create beveled corners | CHA |
| MIRROR | Mirror | Create mirrored copies | MI |
| ARRAY | Array | Create rectangular/polar arrays | AR |
| MOVE | Move | Move objects | M |
| COPY | Copy | Copy objects | CO |
| ROTATE | Rotate | Rotate objects | RO |
| SCALE | Scale | Scale objects | SC |
| EXPLODE | Explode | Break blocks/arrays | X |
| STRETCH | Stretch | Stretch objects | S |
| LENGTHEN | Lengthen | Change object lengths | LEN |

### Annotation Commands

| Command | Full Name | Description | Shortcut |
|---------|-----------|-------------|----------|
| DIMLINEAR | Linear Dimension | Create linear dimensions | DLI |
| DIMALIGNED | Aligned Dimension | Create aligned dimensions | DAL |
| DIMRADIUS | Radius Dimension | Create radius dimensions | DRA |
| DIMDIAMETER | Diameter Dimension | Create diameter dimensions | DDI |
| DIMANGULAR | Angular Dimension | Create angular dimensions | DAN |
| LEADER | Leader | Create leader annotations | LE |
| MTEXT | Multiline Text | Create text paragraphs | MT |
| TEXT | Single Line Text | Create single-line text | DT |
| TABLE | Table | Insert tables | TB |

### View & Navigation Commands

| Command | Full Name | Description | Shortcut |
|---------|-----------|-------------|----------|
| ZOOM | Zoom | Magnify view | Z |
| PAN | Pan | Slide view | P |
| REGEN | Regenerate | Regenerate display | RE |
| VIEW | View | Save/restore named views | V |
| VPORTS | Viewports | Create model space viewports | VP |
| UCS | User Coordinate System | Define coordinate systems | UCS |

## 7.4 Version Compatibility

| Version | Release Year | DWG Support | Notes |
|---------|--------------|-------------|-------|
| AutoCAD LT 2020 | 2019 | 2018 | 64-bit only |
| AutoCAD LT 2021 | 2020 | 2018 | 2021 DWG |
| AutoCAD LT 2022 | 2021 | 2018 | 2022 DWG |
| AutoCAD LT 2023 | 2022 | 2018 | 2023 DWG |
| AutoCAD LT 2024 | 2023 | 2018 | 2024 DWG |
| AutoCAD 2020 | 2019 | 2018 | Full AutoCAD |
| AutoCAD 2021 | 2020 | 2018 | 2021 DWG |
| AutoCAD 2022 | 2021 | 2018 | 2022 DWG |
| AutoCAD 2023 | 2022 | 2018 | 2023 DWG |
| AutoCAD 2024 | 2023 | 2018 | 2024 DWG |

### Interoperability Notes

- DWG format version 2018 is the recommended save format (backward compatible with 2013+)
- DXF is ASCII-based exchange format for third-party interoperability
- DWF/DWFx are lightweight viewing formats
- PDFs can be attached as underlays (PDFUNDERLAY)

## 7.5 File Formats

| Format | Extension | Description | Interop |
|--------|-----------|-------------|---------|
| Drawing | .dwg | Native AutoCAD format | Create/Edit |
| Drawing Exchange | .dxf | ASCII/binary exchange | Import/Export |
| Drawing Web Format | .dwf/.dwfx | Lightweight viewing | View/Print |
| AutoCAD Batch Plot | .bpj | Batch plotting settings | Batch |
| Layer Standard | .lay | Layer template | Import |
| Linetype | .lin | Linetype definition | Import |
| Plot Style | .ctb/.stb | Plot style tables | Assign |
| Sheet Set | .dst | Sheet set definition | Manage |
| Block | .dwg | External block file | Xref |
| Template | .dwt | Drawing template | New |

### Template Standards

```
ACAD.dwt     - Standard Imperial (inches)
ACADISO.dwt  - Standard Metric (mm)
Architectural Desktop templates use MVS/IMPERIAL equivalents
```
