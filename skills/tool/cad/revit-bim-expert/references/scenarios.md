# Scenario Examples

## 9.1 Project Scenarios

### Scenario: Architectural BIM Coordination

**User:** "How do I set up a multi-story office building BIM model?"

**Expert:**
> **Multi-Story Building Workflow:**
>
> 1. **Create levels first:**
>    ```
>    Level 1: ±0.000
>    Level 2: +3.500
>    Level 3: +7.000
>    Level 4: +10.500
>    Roof: +14.000
>    ```
>
> 2. **Structure grid:**
>    ```
>    Grid A-H (horizontal)
>    Grid 1-6 (vertical)
>    Number grids at entry
>    Extend beyond building
>    ```
>
> 3. **Build architectural model:**
>    ```
>    Walls: Use wall types by assembly
>    Floors: Multi-story, stacked
>    Roofs: Top level only
>    Core elements: Stairs, elevator
>    ```
>
> 4. **Create worksets:**
>    ```
>    A-Doors: Architectural doors
>    A-Windows: Curtain wall/windows
>    A-Interiors: Partitions, FF&E
>    A-Stairs: Vertical circulation
>    A-Annotations: 2D drafting
>    ```
>
> 5. **Create typical floor:**
>    ```
>    Model one complete floor
>    Copy/Monitor to other levels
>    Adjust for differences
>    ```

### Scenario: Structural BIM Workflow

**User:** "How do I coordinate structural columns and beams with architecture?"

**Expert:**
> **Structural-Architectural Coordination:**
>
> 1. **Link architect model:**
>    ```
>    Insert > Link Revit
>    Position: Auto - Origin to Origin
>    Workset: Linked Models
>    ```
>
> 2. **Set up structural grids:**
>    ```
>    Copy/monitor architect grids
>    Add structural grids
>    Align to grid intersections
>    ```
>
> 3. **Place structural columns:**
>    ```
>    At grid intersections
>    Use structural column type
>    Extend to floor levels
>    Place foundations below
>    ```
>
> 4. **Model beams:**
>    ```
>    Create beam system
>    Select floor boundary
>    Assign beam type
>    Add secondary beams
>    ```
>
> 5. **Connect beams to columns:**
>    ```
>    Add beam connections
>    Use connection families
>    Check geometry
>    ```
>
> 6. **Coordination checks:**
>    ```
>    Run interference detection
>    Check beam-wall clearance
>    Verify floor openings
>    ```

### Scenario: MEP BIM Coordination

**User:** "How do I route HVAC ductwork in a coordinated model?"

**Expert:**
> **MEP Coordination Workflow:**
>
> 1. **Import coordination model:**
>    ```
>    Link architect (for reference)
>    Link structural (for ceilings)
>    Set worksets visible
>    ```
>
> 2. **Set up ceiling spaces:**
>    ```
>    Add ceiling in architect model
>    Or use structural ceiling
>    Define plenum space
>    ```
>
> 3. **Route main ducts:**
>    ```
>    Use MEP Routing
>    Select system type: Supply Air
>    Set duct size constraints
>    Route through plenum
>    ```
>
> 4. **Add branches:**
>    ```
>    Use Takeoffs
>    Connect to equipment
>    Add fittings
>    Auto-connect where possible
>    ```
>
> 5. **Check clearances:**
>    ```
>    MEP Systems > Check Clearance
>    Set minimum clearance rules
>    Resolve conflicts
>    ```
>
> 6. **Coordination review:**
>    ```
>    Export to Navisworks
>    Run clash detection
>    Document issues
>    Resolve and recheck
>    ```

## 9.2 Deliverables

### BIM Deliverable Matrix

```
Project Deliverables by Phase:

Schematic Design:
├── Concept model (LOD 100-200)
├── Area calculations
├── Preliminary BIM visualization
└── Massing studies

Design Development:
├── Coordinated model (LOD 300)
├── Clash detection reports
├── Energy analysis
├── Preliminary schedules
└── DD drawing set

Construction Documents:
├── Coordinated model (LOD 350)
├── Final clash reports
├── IFC model for fabricators
├── CD drawing set
├── Door/Window schedules
└── Room/Finishes schedules

Construction:
├── Issued for Construction model
├── Shop drawing model (LOD 400)
├── Construction sequence model
├── As-built model
└── OFI resolution

Facility Management:
├── FM handover model (LOD 500)
├── COBie data
├── Asset register
├── Maintenance schedules
└── Warranty documentation
```

### IFC Export Specification

```
IFC Export Settings:
├── IFC Version: IFC4x2 (or project standard)
├── Space Boundaries: At Boundary Elements
├── Tessellation: Fine (for coordination)
├── Include 2D geometry: Yes
├── Include linked models: Yes
├── Export linked models as: Separate files
├── Export schedules: Yes
├── Export room relationships: Yes
└── Include shared parameters: Yes

Naming Convention:
[ProjectCode]_[Discipline]_[Version].ifc
Example: PRJ001_ARCH_1.0.ifc
```

### Drawing Deliverables

```
Drawing Set Structure:
├── Architectural
│   ├── G-001: Cover Sheet
│   ├── G-002: Drawing Index
│   ├── G-003: Code Summary
│   ├── G-004: Site Plan
│   ├── A-101: Level 1 Plan
│   ├── A-102: Level 2 Plan
│   ├── A-201: Elevations
│   ├── A-301: Sections
│   ├── A-401: Wall Sections
│   ├── A-501: Details
│   └── A-601: Schedules
├── Structural
│   ├── S-001: General Notes
│   ├── S-101: Foundation Plan
│   ├── S-201: Framing Plans
│   └── S-301: Details
├── MEP
│   ├── M-001: MEP Index
│   ├── M-101: Mechanical Plans
│   ├── E-101: Electrical Plans
│   └── P-101: Plumbing Plans
└── Specifications (via specifications software)
```

## 9.3 Automation

### Dynamo Scripts

```python
# Dynamo: Create Levels from Excel
# Read level names and elevations from Excel
# Create levels in Revit

import clr
clr.AddReference('RevitNodes')
clr.AddReference('RevitAPI')
from Revit.Elements import *
from Revit import Transaction
import Revit

# Get Excel data
filePath = IN[0]
data = System.Array[System.Array[str]](GetExcelData(filePath))

# Transaction to create levels
with Transaction(doc, "Create Levels") as t:
    t.Start()
    for row in data:
        name = row[0]
        elevation = float(row[1])
        Level.Create(doc, elevation)
    t.Commit()

OUT = "Levels created successfully"
```

```python
# Dynamo: Rename Rooms by Zone
# Input: zone number prefix

zone_prefix = IN[0]
all_rooms = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()

with Transaction(doc, "Rename Rooms") as t:
    t.Start()
    for room in all_rooms:
        level_name = room.Level.Name
        room_num = room.Number
        new_name = "{}-{}".format(zone_prefix, room_num)
        room.get_Parameter(BuiltInParameter.ROOM_NAME).Set(new_name)
    t.Commit()

OUT = "Rooms renamed"
```

```python
# Dynamo: Place Doors at Grid Intersections
# Place doors on all wall-grid intersections

# Get all grids
grids = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Grids).ToElements()

# Get all walls
walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

# Get door family
door_type = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).FirstElement()

with Transaction(doc, "Place Doors") as t:
    t.Start()
    for wall in walls:
        for grid in grids:
            # Get intersection point
            intersection = grid.Curve.Intersect(wall.Location.Curve)
            if intersection:
                point = intersection[0]
                # Place door
                Door.Create(doc, wall.Id, door_type.Id, point)
    t.Commit()
```

### Revit Macros (C#)

```csharp
// Macro: Set Shared Parameters
using System;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using Autodesk.Revit.Attributes;

public class SetSharedParams : IExternalCommand
{
    public Result Execute(
        ExternalCommandData commandData,
        ref string message,
        ElementSet elements)
    {
        UIDocument uidoc = commandData.Application.ActiveUIDocument;
        Document doc = uidoc.Document;
        
        // Get shared parameter file
        DefinitionFile defFile = doc.Application.OpenSharedParameterFile();
        
        // Get or create parameter group
        DefinitionGroup group = defFile.Groups.get_Item("Project Parameters");
        
        // Get parameter definition
        ExternalDefinition paramDef = group.Definitions.get_Item("Mark") 
            as ExternalDefinition;
        
        // Add to project
        Category category = doc.Settings.Categories.get_Item(
            BuiltInCategory.OST_Doors);
        
        Binding binding = doc.Application.Create.NewTypeBinding(
            new CategorySet());
        binding.Categories.Insert(category);
        
        doc.ParameterBindings.Insert(paramDef, binding);
        
        return Result.Succeeded;
    }
}
```

### Revit API (Python via pyRevit)

```python
# pyRevit: Batch Update Parameters
# Update instance parameter for all elements

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

# Get all walls
walls = FilteredElementCollector(doc)\
    .OfCategory(BuiltInCategory.OST_Walls)\
    .WhereElementIsNotElementType()\
    .ToElements()

# Get parameter
param_name = "Comments"

with Transaction(doc, "Batch Update Comments") as t:
    t.Start()
    for wall in walls:
        param = wall.get_Parameter(param_name)
        if param and not param.IsReadOnly:
            param.Set("Coordinated - " + str(wall.Id.IntegerValue))
    t.Commit()

print("Updated {} walls".format(len(walls)))
```

### Schedule Formulas

```
Schedule Calculated Parameters:

Wall Area (with openings):
=[Length] * [Height] - [Host: Host Instance Comments]

Wall Volume:
=[Length] * [Height] * [Volume Parameter]

Room Finish Area:
=[Area] + [Ceiling Height] * [Perimeter] * [Finish Factor]

Cost Calculation:
=([Quantity] * [Unit Cost]) + [Fixed Cost]

Percentage Complete:
=[Completed Items] / [Total Items] * 100

MEP Duct Length (from routing):
=Built In: Duct Length Parameter
```

### Design Options Automation

```python
# Dynamo: Create Design Options
# Set up design options for multiple schemes

# Get current document
doc = __revit__.ActiveUIDocument.Document

# Define design options
options = [
    ("Option A", "Primary scheme"),
    ("Option B", "Alternate scheme"),
    ("Option C", "Value engineering")
]

# Create design option set
with Transaction(doc, "Create Design Options") as t:
    t.Start()
    
    # Create option set
    option_set = DesignOptionSet.Create(doc)
    
    for option_name, option_desc in options:
        option = DesignOption.Create(option_set.Id, option_name)
        option.Name = option_desc
    
    t.Commit()
```
