# Standard Workflow

## 8.1 Project Workflow

### Phase 1: Template Setup

```
BIM Project Template Workflow
├── 1. Configure Project Settings
│   ├── Project Units (Meters, mm, etc.)
│   ├── Snapping increments
│   ├── Base point and survey point
│   └── Phase settings
├── 2. Set Up Levels
│   ├── Define building levels
│   ├── Level names (Level 1, Level 2, etc.)
│   ├── Elevation values
│   └── Grid lines
├── 3. Configure Worksets
│   ├── Create discipline worksets
│   ├── Set visibility by workset
│   └── Define workset permissions
├── 4. Load Family Libraries
│   ├── Architectural families
│   ├── Structural families
│   ├── MEP families
│   └── Annotation families
├── 5. Set Up Annotations
│   ├── Dimension styles
│   ├── Text styles
│   ├── Tag styles
│   └── Symbol libraries
├── 6. Configure Sheets
│   ├── Title block family
│   ├── Sheet templates
│   ├── View templates
│   └── Revision schedules
├── 7. Set Up Phases
│   ├── Existing/Demo/New
│   ├── Phase filters
│   └── Phase mapping
└── 8. Define Parameters
    ├── Shared parameters
    ├── Project parameters
    └── Global parameters
```

### Phase 2: Design Development

```
Design Development Workflow
├── 1. Architectural Model
│   ├── Import conceptual mass
│   ├── Build from mass
│   ├── Walls, floors, roofs
│   ├── Doors, windows
│   └── Stairs, railings
├── 2. Structural Model
│   ├── Import architect model
│   ├── Add structural grids
│   ├── Structural columns
│   ├── Foundations
│   ├── Beams, decks
│   └── Connections
├── 3. MEP Systems
│   ├── Import architect model
│   ├── HVAC systems
│   │   ├── Ductwork
│   │   ├── Equipment
│   │   └── Controls
│   ├── Plumbing systems
│   │   ├── Piping
│   │   ├── Fixtures
│   │   └── Equipment
│   ├── Electrical systems
│   │   ├── Power
│   │   ├── Lighting
│   │   └── Communications
└── 4. Documentation
    ├── Floor plans
    ├── Reflected ceiling plans
    ├── Elevations
    ├── Sections
    └── Details
```

### Phase 3: Drawing Production

```
Drawing Production Workflow
├── 1. Create View Templates
│   ├── Plan view template
│   ├── Ceiling plan template
│   ├── Section view template
│   └── Detail view template
├── 2. Set Up Drawing Sheets
│   ├── Insert title block
│   ├── Place views on sheets
│   ├── Adjust scale
│   └── Align views
├── 3. Add Annotations
│   ├── Dimensions
│   ├── Tags (doors, windows, rooms)
│   ├── Text notes
│   ├── Keynotes
│   └── Symbols
├── 4. Room and Area Planning
│   ├── Place rooms
│   ├── Set room boundaries
│   ├── Add room tags
│   └── Create area plans
├── 5. Create Schedules
│   ├── Door schedule
│   ├── Window schedule
│   ├── Room finish schedule
│   ├── Equipment schedule
│   └── Quantity takeoffs
└── 6. Issue Drawing Set
    ├── Coordinate sheets
    ├── Set issue parameters
    └── Export to PDF/DWG
```

## 8.2 Collaboration Workflow

### Worksharing Setup

```
Worksharing Workflow
├── 1. Enable Worksharing
│   ├── Collaborate > Worksets
│   ├── Enable Worksharing
│   └── Create central model
├── 2. Workset Structure
│   ├── Create worksets by discipline
│   ├── Set workset visibility
│   └── Assign elements to worksets
├── 3. Team Collaboration
│   ├── Create Local (Ctrl+Shift+L)
│   ├── Open from central
│   ├── Edit with worksets
│   └── Sync changes
├── 4. Ownership Management
│   ├── Borrow elements (for editing)
│   ├── Release elements (after edit)
│   ├── Relinquish all
│   └── Request ownership
└── 5. Conflict Prevention
    ├── Check for warnings
    ├── Use workset visibility
    └── Regular syncs
```

### Linked Model Coordination

```
Linked Model Workflow
├── 1. Link Models
│   ├── Insert > Link Revit
│   ├── Browse to central/local
│   ├── Positioning: Auto - Origin to Origin
│   └── Workset: Manage links
├── 2. Coordination Views
│   ├── Create coordination view
│   ├── Load all links
│   ├── Set up worksets
│   └── View filters
├── 3. Copy/Monitor Elements
│   ├── Select host elements
│   ├── Copy to linked model
│   ├── Monitor changes
│   └── Alert on conflicts
├── 4. Coordination Tools
│   ├── Interference Detection
│   ├── Clash Review
│   └── Coordination Reports
└── 5. Coordination Meeting Workflow
    ├── Update links (Reload Latest)
    ├── Run clash detection
    ├── Review conflicts
    └── Assign issues
```

### Shared Coordinates

```
Shared Coordinates Setup
├── 1. Define Project Base Point
│   ├── Survey Point: True north, coordinates
│   ├── Project Base Point: Project origin
│   └── Base point visibility
├── 2. Link Models with Coordinates
│   ├── Match coordinates to site
│   ├── Use "Auto - Origin to Origin" for first
│   ├── Use "Auto - By Shared Coordinates" for others
│   └── Verify positions
├── 3. Publish Coordinates
│   ├── From host model
│   ├── Publish to A360/BIM 360
│   └── Other disciplines consume
├── 4. Consume Coordinates
│   ├── When linking
│   ├── Select published coordinates
│   └── Verify alignment
└── 5. Maintain Coordinates
    ├── Don't move base point after publish
    ├── Document any moves
    └── Re-publish if needed
```

## 8.3 QA/QC Workflow

### Model Quality Checklist

```
Pre-Coordination Review:
├── [ ] All levels created and named
├── [ ] Grids placed and labeled
├── [ ] Walls connected properly
├── [ ] Doors and windows in walls
├── [ ] Floors and roofs joined
├── [ ] Stairs code compliant
├── [ ] Railings code compliant
├── [ ] Rooms placed and tagged
├── [ ] Areas calculated
├── [ ] Model validated
│   ├── Warnings resolved
│   ├── No missing imports
│   └── No broken links
└── [ ] Worksets organized
```

### Drawing Quality Checklist

```
Drawing Quality Review:
├── [ ] Correct view range settings
├── [ ] Appropriate crop regions
├── [ ] View scale matches sheet
├── [ ] Dimensions correct and complete
├── [ ] Tags placed and correct
├── [ ] Text notes readable
├── [ ] Line weights appropriate
├── [ ] Hatching correct
├── [ ] Title block complete
│   ├── Drawing title
│   ├── Sheet number
│   ├── Revision
│   ├── Scale
│   └── Date
├── [ ] Room data accurate
├── [ ] Schedules match views
└── [ ] Issue status updated
```

### MEP Coordination Checklist

```
MEP Coordination Review:
├── [ ] Duct/pipe routing clearance
│   ├── 150mm minimum for duct
│   ├── 50mm minimum for pipe
│   └── 100mm for cable tray
├── [ ] Structural clearance
│   ├── 50mm from beam flanges
│   └── 75mm from slab edge
├── [ ] Equipment clearance
│   ├── Maintenance access
│   ├── Service clearance
│   └── Replacement clearance
├── [ ] Code compliance
│   ├── Headroom minimums
│   ├── Equipment spacing
│   └── Accessibility
├── [ ] Clash detection run
├── [ ] Interference issues resolved
└── [ ] Fabrication model coordination
```

### BIM Execution Plan

```
BIM Execution Plan Structure:
├── 1. Project Information
│   ├── Project name and number
│   ├── Project team
│   ├── BIM goals and uses
│   └── Project delivery method
├── 2. BIM Goals and Uses
│   ├── Design intent visualization
│   ├── Coordination and clash detection
│   ├── Quantity takeoffs
│   ├── Energy analysis
│   └── Construction documentation
├── 3. Project Delivery
│   ├── Delivery method
│   ├── Communication protocol
│   └── Meeting schedule
├── 4. Model Structure
│   ├── LOD matrix
│   ├── Model organization
│   └── Element naming
├── 5. Collaboration
│   ├── Worksharing protocol
│   ├── File naming convention
│   ├── File exchange schedule
│   └── Coordinate system
├── 6. Quality Control
│   ├── Model audit process
│   ├── Clash detection process
│   └── Issue resolution
├── 7. Deliverables
│   ├── Drawing outputs
│   ├── Model outputs
│   ├── Data outputs
│   └── Format specifications
└── 8. Technology
    ├── Software versions
    ├── File format standards
    └── Data storage
```

### Issue Tracking

```
Issue Resolution Workflow:
├── 1. Issue Identified
│   ├── Clash detected
│   ├── Design conflict
│   └── Coordination finding
├── 2. Issue Logged
│   ├── Issue ID number
│   ├── Description
│   ├── Location (coordinate)
│   ├── Priority (High/Med/Low)
│   ├── Responsible party
│   └── Due date
├── 3. Issue Assigned
│   ├── Engineer reviews
│   ├── Solution proposed
│   └── Approved
├── 4. Issue Resolved
│   ├── Model updated
│   ├── Local synced
│   └── Issue closed
└── 5. Issue Verified
    └── Re-clash check
```
