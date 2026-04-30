# Scenario Examples

## 9.1 Project Scenarios

### Scenario: Architectural Floor Plan

**User:** "I need to draw a 120 sqm residential floor plan with rooms labeled."

**Expert:**
> **Architectural Floor Plan Workflow:**
>
> 1. **Set up layers first:**
>    ```
>    A-WALL-CONSTR (walls)
>    A-WALL-DIMS (dimensions)
>    A-ANNO-ROOM (room labels)
>    A-FLOR-FINI (floor finish)
>    A-DOOR (doors)
>    A-WINDOW (windows)
>    ```
>
> 2. **Draw walls using PLINE or LINE:**
>    - Wall thickness typically 150mm (internal) or 200mm (external)
>    - Use OFFSET for parallel walls
>    - Use FILLET for corners
>
> 3. **Insert doors from tool palette:**
>    - Single door: 900mm width typical
>    - Double door: 1500mm width typical
>
> 4. **Add dimensions:**
>    - Use DIMLINEAR for room dimensions
>    - Set dim scale for 1:100 or 1:50
>    - Include wall centerlines for framing
>
> 5. **Label rooms:**
>    - Use MTEXT for room names
>    - Add area text (calculate from geometry)
>
> ```autocad
> ; Draw 3x4m room
> PLINE
> 0,0
> 3000,0
> 3000,4000
> 0,4000
> C (close)
>
> ; Dimension the room
> DIMLINEAR
> (select first extension line origin)
> (select second extension line origin)
> (specify dimension line location)
> ```

### Scenario: Structural Framing Plan

**User:** "How do I create a structural steel framing plan?"

**Expert:**
> **Steel Framing Workflow:**
>
> 1. **Create steel layers:**
>    ```
>    S-FRAME-WBEAM (wide flange beams)
>    S-FRAME-HBEAM (HSS beams)
>    S-FRAME-COLUMN (columns)
>    S-FRAME-BRACE (bracing)
>    S-FRAME-PLT (base plates)
>    ```
>
> 2. **Draw beams:**
>    - Use LWPOLYLINE for centerlines
>    - Draw actual shapes offset from CL
>    - Use HATCH for steel sections
>
> 3. **Add WWR labels:**
>    ```
>    W14x90 = W (wide flange) 14" depth, 90 lb/ft
>    HSS6x6x3/8 = 6" square tube, 0.375" wall
>    ```
>
> 4. **Column grid:**
>    - Use LINE with ORTHO for grid
>    - Label with ABC/123 system
>
> ```autocad
> ; Draw beam with centerline
> LAYER set S-FRAME-WBEAM
> LINE
> 0,0 6000,0
> ; Draw beam outline
> LAYER set S-FRAME-WBEAM-SHPE
> OFFSET 75 (half depth from CL)
> ```

### Scenario: Mechanical HVAC Layout

**User:** "I need to show duct routing on a floor plan."

**Expert:**
> **HVAC Duct Workflow:**
>
> 1. **Set up duct layers:**
>    ```
>    M-DUCT-SUPP (supply duct)
>    M-DUCT-RETN (return duct)
>    M-DUCT-EXHT (exhaust duct)
>    M-DUCT-DIFF (diffusers)
>    M-DUCT-FITG (fittings)
>    ```
>
> 2. **Draw duct routes:**
>    - Main ducts: 400mm x 200mm typical
>    - Branch ducts: 200mm x 100mm typical
>    - Use PLINE for routes
>    - OFFSET for parallel runs
>
> 3. **Add fittings:**
>    - Elbows (mitered or radius)
>    - Tees and wyes
>    - Reducers
>
> 4. **Label ductwork:**
>    ```
>    24x8 SUPP = 24"x8" supply duct
>    18" RA = 18" return air
>    ```
>
> 5. **Add diffuser symbols:**
>    - Use blocks from tool palette
>    - Label with CFM values

## 9.2 Deliverables

### Construction Document Set

```
Drawing Deliverable Checklist
├── Cover Sheet
│   ├── Project title
│   ├── Drawing index
│   ├── Revision table
│   └── Consultant info
├── Coordinate Sheet
│   ├── Site plan
│   ├── Benchmark locations
│   └── Grid system
├── Architectural Sheets
│   ├── A-001: Cover & Index
│   ├── A-101: Floor Plans
│   ├── A-102: Ceiling Plans
│   ├── A-201: Elevations
│   ├── A-301: Sections
│   ├── A-401: Wall Sections
│   ├── A-501: Details
│   └── A-601: Schedules
├── Structural Sheets
│   ├── S-001: General Notes
│   ├── S-101: Foundation Plan
│   ├── S-201: Framing Plans
│   └── S-301: Details
├── MEP Sheets
│   ├── M-101: Mechanical Plans
│   ├── E-101: Electrical Plans
│   └── P-101: Plumbing Plans
└── Plot Configuration
    ├── Sheet size: A1 or A0
    ├── Scale: 1:100 (plans), 1:50 (details)
    └── PDF output with layers preserved
```

### PDF Publishing

```autocad
; Batch publish to PDF
PUBLISH
; Or use script for consistent output:
; pubscript.scr
-FILE (choose DST sheet list)
-PDF (select plotter)
-ALL (include all sheets)
-COLOR (preserve colors)
-yes (open when done)
```

## 9.3 Automation

### AutoCAD Scripts

```autocad
; setup_metric.scr - Configure new drawing for metric
; Run with: SCRIPT setup_metric.scr

; Set units to millimeters
UNITS
2 4 (Decimal, 4 decimal places)
; Set limits
LIMITS
0,0
420000,297000 (A3 landscape in mm)
; Set layer
-LAYER
M A-WALL-CONSTR C 1 A-WALL-CONSTR
M A-WALL-DIMS C 2 A-WALL-DIMS
M A-DOOR C 7 A-DOOR
M A-WINDOW C 7 A-WINDOW
M A-ANNO-TEXT C 7 A-ANNO-TEXT
; Dimension style
-DIMSTYLE
R METRIC
ST METRIC
D
SCALE 1.0000
; Text style
STYLE METRIC arial.ttf 0 0.7 0 N N N
REGEN
```

### AutoLISP Routines

```lisp
; LayerCount.lsp - Count objects per layer
(defun c:LayerCount (/ ss lst)
  (princ "\nSelect objects: ")
  (if (setq ss (ssget))
    (progn
      (setq lst (list))
      (repeat (sslength ss)
        (setq ent (ssname ss 0))
        (setq lay (cdr (assoc 8 (entget ent))))
        (if (assoc lay lst)
          (setq lst (subst (cons lay (1+ (cdr (assoc lay lst))))
                          (assoc lay lst) lst))
          (setq lst (cons (cons lay 1) lst)))
        (ssdel ent ss))
      (foreach x lst
        (princ (strcat (car x) ": " (itoa (cdr x)) "\n"))))
  (princ))

; QuickOffset.lsp - Offset with fixed distance
(defun c:QOffset (/ dis)
  (setq dis (getreal "\nOffset distance: "))
  (command "OFFSET" dis)
  (princ))
```

### AutoHotkey Automation

```autohotkey
#IfWinActive, ahk_exe acad.exe
; Quick dimension toggle
^d::
Send !n{right}{down}{enter}
return

; Layer isolate
^l::
Send !h{right}{down}
return

; Quick save
^s::Send !f{up}{enter}
return

; Cycle through layer filters
#IfWinActive
```
