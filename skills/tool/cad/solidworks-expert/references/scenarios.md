# Scenario Examples

## 9.1 Project Scenarios

### Scenario: Sheet Metal Enclosure

**User:** "How do I create a sheet metal enclosure with bends and louvers?"

**Expert:**
> **Sheet Metal Workflow:**
>
> 1. **Start sheet metal part:**
>    - New Part > Sheet Metal template
>    - Or Features > Sheet Metal > Base Flange
>
> 2. **Set sheet metal parameters:**
>    ```
>    Base Flange/Tab:
>    - Profile: Draw rectangle/shape
>    - Thickness: 1.5mm (material gauge)
>    - Bend Radius: 0.5mm (typically 0.3-0.5x thickness)
>    - Auto Relief: Yes (for cutouts)
>    ```
>
> 3. **Add features:**
>    - Edge Flanges (automatic bending)
>    - Hem Flanges (folded edges)
>    - Jogs (offset bends)
>    - Sketch Bend (user-defined bend)
>    - Cross Break (anti-buckling)
>
> 4. **Add louvers:**
>    ```
>    Insert Features > Sheet Metal > Louver
>    - Select face
>    - Draw louver profile
>    - Specify height
>    - Add relief options
>    ```
>
> 5. **Add ventilation/cutouts:**
>    - Use Extruded Cut
>    - Remember: cuts perpendicular to face
>    - Add bend relief if needed
>
> ```solidworks
> ' Sheet Metal Properties
> ' SW 2024 API Example
> Dim swApp As SldWorks.SldWorks
> Dim swModel As SldWorks.ModelDoc2
> Dim swPart As SldWorks.PartDoc
> 
> Set swApp = Application.SldWorks
> Set swModel = swApp.ActiveDoc
> Set swPart = swModel
> 
> ' Set material
> swPart.SetMaterial2 "C:\materials\Database.sldmat", "6061 Alloy"
> 
> ' Set sheet metal properties
> swPart.SetSheetMetalParams 0.0015, 0.0005  ' thickness, bend radius
> ```

### Scenario: Plastic Injection Molded Part

**User:** "What features do I need for an injection molded part?"

**Expert:**
> **Injection Mold Design Checklist:**
>
> 1. **Draft Analysis:**
>    ```
>    Tools > Evaluate > Draft Analysis
>    - Pull Direction: Define
>    - Minimum Draft: 1° typical
>    - Check all faces
>    - Fix negative draft areas
>    ```
>
> 2. **Wall Thickness:**
>    - Nominal: 2-3mm for ABS/PP
>    - Rib thickness: 0.6x nominal wall
>    - Boss diameter: 2x nominal wall
>    - Avoid thick sections (sink marks)
>
> 3. **Corner Radii:**
>    ```
>    Interior corners: R > 0.5 x wall thickness
>    Exterior corners: R > 1.5 x wall thickness
>    ```
>
> 4. **Add Features:**
>    - Shell with proper thickness
>    - Snap fits (integrated)
>    - Living hinges (thin flex areas)
>    - Gussets for strength
>
> 5. **Mold Considerations:**
>    - Undercuts (need slides/cores)
>    - Bosses for cores
>    - Gate locations
>    - Ejector pin locations
>    - Vent locations

### Scenario: Large Mechanical Assembly

**User:** "How do I manage a 500-part industrial machine assembly?"

**Expert:**
> **Large Assembly Best Practices:**
>
> 1. **Structure:**
>    ```
>    Machine_Assembly (Top Level)
    ├── Frame_Subassy
    │   ├── Frame_Base
    │   ├── Frame_Vertical
    │   └── Frame_Crossmembers
    ├── Drive_Subassy
    │   ├── Motor
    │   ├── Gearbox
    │   ├── Couplings
    │   └── Drive_Shaft
    ├── Conveyor_Subassy
    │   ├── Frame
    │   ├── Rollers
    │   └── Belting
    ├── Electrical_Subassy
    │   ├── Control_Panel
    │   ├── Wiring_Harness
    │   └── Sensors
    └── Hardware
        └── Fasteners (from Toolbox)
    ```
>
> 2. **Performance:**
>    - Use SpeedPak (simplified graphics)
>    - Enable Large Assembly Mode
>    - Use component patterns instead of mates
>    - Suppress invisible components
>    - Enable lightweight by default
>
> 3. **Display States:**
>    ```
>    Master: Full assembly
>    Frame_Only: Structural components
>    Drive_Only: Power transmission
>    Wireframe: Clearance check
>    Phantom: Reference only
    ```
>
> 4. **Virtual Components:**
>    - Use for purchased parts
>    - Placeholder geometry only
>    - Update when CAD received

## 9.2 Deliverables

### Manufacturing Deliverables

```
Part Deliverable Package:
├── 3D CAD Model (.sldprt)
│   └── All configurations
├── 2D Drawing (.slddrw)
│   ├── Multi-sheet as needed
│   ├── GD&T per ASME Y14.5
│   └── Material callout
├── PDF Drawing
│   └── Print-ready, searchable
├── STEP File (.stp)
│   └── For CAM/gantry systems
├── IGES File (.igs)
│   └── Legacy CAM compatibility
├── STL File (.stl)
│   └── 3D printing prototype
├── BOM (.xlsx)
│   ├── Part number
│   ├── Description
│   ├── Quantity
│   ├── Material
│   ├── Surface finish
│   └── Revision
└── Analysis Reports (if applicable)
    ├── FEA results
    ├── Tolerance stack-up
    └── Mold flow analysis
```

### Bill of Materials

```solidworks
' BOM Table Properties
' Configure via Table Anchor

BOM Columns:
| Item | Part Number | Description | Qty | Material | Finish | Revision |
|------|-------------|-------------|-----|----------|--------|----------|
| 1 | PRJ-001 | Base Plate | 1 | AISI 1018 | Mill | A |
| 2 | PRJ-002 | Support Bracket | 4 | AISI 304 | Passivate | A |
| 3 | STD-M8-HEX | M8x25 Hex Bolt | 16 | SS316 | - | - |
```

## 9.3 Automation

### SOLIDWORKS Macros (VBA)

```vba
' AddCustomProperties.bas
' Add standard custom properties to part

Sub AddStandardProps()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    
    ' Add custom properties
    swPart.AddCustomInfo3 "Project", "Text", "PROJECT-001"
    swPart.AddCustomInfo3 "Description", "Text", ""
    swPart.AddCustomInfo3 "Material", "Text", swPart.GetMaterialValueName
    swPart.AddCustomInfo3 "Revision", "Text", "A"
    swPart.AddCustomInfo3 "Drawn By", "Text", ""
    swPart.AddCustomInfo3 "Date", "Date", Format(Date, "yyyy-mm-dd")
    swPart.AddCustomInfo3 "Mass", "Double", swPart.GetMassProperties(1)(0)
    
    swApp.SendMsgToUser "Custom properties added."
End Sub

' BatchExportPDF.bas
' Export all drawings to PDF

Sub BatchExportPDF()
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swView As SldWorks.View
    
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    
    If swModel.GetType <> swDRAWINGSHEET Then
        MsgBox "Please open a drawing."
        Exit Sub
    End If
    
    Set swDraw = swModel
    swDraw.Extension.SaveAs swDraw.GetPathName & ".pdf", _
        swSaveAsVersion.swSaveAsPDF, swSaveAsOptions.swSaveAsOptions_Silent, Nothing, 0, 0
    
    MsgBox "PDF exported."
End Sub
```

### SOLIDWORKS API (C#)

```csharp
// CreateSimplePart.cs
// Create a simple extruded part using API

using SolidWorksAPI;

public class PartCreator
{
    public static void CreatePart(ISldWorks swApp, string path)
    {
        // Create new part
        IModelDoc2 swModel = swApp.NewDocument(
            @"C:\ProgramData\SolidWorks\Templates\Part.prtdot", 
            0, 0, 0);
        
        // Select front plane
        swModel.Extension.SelectByID2("Front Plane", "PLANE", 0, 0, 0, false, 0, null, 0);
        
        // Start sketch
        swModel.SketchManager.InsertSketch(true);
        
        // Draw rectangle
        swModel.SketchManager.CreateCenterRectangle(0, 0, 0, 0.05, 0.03, 0);
        
        // Close sketch
        swModel.SketchManager.InsertSketch(true);
        
        // Select sketch
        swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
        
        // Create extrude
        swModel.FeatureManager.FeatureExtrusion2(
            true,  // blind direction
            false, // auto extend
            0,     // direction 1
            0.02,  // depth
            0.0,   // draft angle
            false, // draft outward
            false, // cap in direction 1
            0,     // direction 2
            0.0,   // depth 2
            0.0,   // draft angle 2
            false, // draft outward 2
            false, // flip side cut
            false, // both directions
            0,     // arc/relief type
            0,     // arc/relief height
            0);    // arc/relief angle
        
        // Save
        swModel.SaveAs(path);
    }
}
```

### Design Table Automation

```
Design Table Structure (Excel):
+------------------+--------+--------+--------+
|                  | $PRPDWS | $PRPDWS | $PRPDWS|
|                  | Width  | Height | Depth  |
+------------------+--------+--------+--------+
| Default          | 100    | 50     | 30     |
+------------------+--------+--------+--------+
| Small            | 80     | 40     | 25     |
+------------------+--------+--------+--------+
| Large            | 150    | 75     | 45     |
+------------------+--------+--------+--------+

Key:
$PRPDWS = Dimension name from PropertyManager
$STATE = SUPPRESSED/UNSUPPRESSED
$CONFIGURATION = Config name
$DESCRIPTION = Config description
```

### File Export Automation

```csharp
// BatchExport.cs
// Export multiple parts to STEP

public void BatchExportSTEP(string[] filePaths, string outputFolder)
{
    foreach (string filePath in filePaths)
    {
        // Open part
        int errors = 0;
        int warnings = 0;
        IModelDoc2 swModel = swApp.OpenDoc6(
            filePath, 2, 1, "", ref errors, ref warnings);
        
        // Export as STEP
        string stepPath = Path.Combine(outputFolder, 
            Path.GetFileNameWithoutExtension(filePath) + ".stp");
        
        swModel.Extension.SaveAs(stepPath, 0, 1, null, 0, 0);
        
        // Close without saving
        swApp.CloseDoc(filePath);
    }
}
```
