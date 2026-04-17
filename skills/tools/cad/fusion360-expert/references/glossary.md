# Glossary

## A

- **Adaptive Clearing** — 3D CAM operation that clears material using efficient trochoidal toolpaths, adapting to geometry
- **As-Built Joint** — Feature that mates components based on current positions without formal constraints
- **Assembly Joint** — Kinematic constraint defining how two components move relative to each other

## B

- **Base Feature** — First solid feature created from a sketch; all other features are derived from it
- **Bend Allowance** — Formula accounting for material stretch during sheet metal bending
- **Body** — Individual solid or surface shape within a component
- **BOM (Bill of Materials)** — List of parts and quantities for an assembly
- **BRep (Boundary Representation)** — Geometric representation defining shape by its boundaries (faces, edges, vertices)

## C

- **Chamfer** — Angled edge treatment; defined by distance+angle or two distances
- **Component** — Reusable instance of a design within an assembly
- **Construction Geometry** — Non-physical sketch lines/points used as references
- **Constraint** — Rule governing sketch geometry (coincident, parallel, tangent, etc.)
- **Cosmetic Thread** — Visual representation of a thread, not modeled geometry

## D

- **Degree** — Polynomial order of NURBS curve/surface; higher = more complex shape
- **Design Intent** — Strategy for what changes vs. stays fixed when editing
- **Design History** — Timeline of features applied to a sketch
- **Design Representation** — Simplified version of a component for large assemblies
- **Direct Edit** — Modifying geometry directly without feature history
- **Draft Angle** — Taper on mold walls for part ejection
- **DXF (Drawing Exchange Format)** — 2D vector format for CAD interchange

## E

- **Extrude** — Feature adding/removing material by moving a profile along an axis
- **Extend** — Feature extending a surface to a boundary

## F

- **Face** — Flat or curved surface on a body
- **Feature** — Discrete modeling operation (extrude, fillet, hole, etc.)
- **Fillet** — Rounded edge; defined by radius value
- **Flatten** — Converting a 3D surface to 2D geometry (for sheet metal)
- **Form Shell** — Converting solid to sheet metal with uniform wall thickness

## G

- **G-code** — CNC machine programming language (RS-274)
- **G0** — Rapid positioning move
- **G1** — Linear feed move
- **G2/G3** — Circular interpolation (CW/CCW)

## H

- **Hole** — Feature creating cylindrical cuts; supports threaded, clearance, and tap types
- **Hybrid Modeling** — Mix of parametric (feature-based) and direct (mesh) editing

## I

- **IGES (Initial Graphics Exchange Specification)** — Neutral format for CAD geometry exchange
- **iMate** — Named contact point for component assembly
- **Intersect** — Feature creating geometry from the overlap of bodies or sketches

## J

- **Joint Origin** — Reference point defining component coordinate system

## L

- **Loft** — Feature creating a surface/body between two or more profiles
- **Local Component** — Component defined within the current file

## M

- **Mesh** — Faceted geometry (triangles/polygons); used for STL and subdivision modeling
- **Minimum Wall Thickness** — Thinnest section of a 3D-printed or molded part

## N

- **Nesting** — Arranging parts on a sheet for cutting to minimize waste
- **Non-Manifold** — Invalid geometry where edges share more than two faces

## O

- **Offset Plane** — Construction plane at a distance from a reference plane

## P

- **Patch** — Surface or solid created from planar sketch regions
- **Pattern** — Feature replicated in linear or circular arrangement
- **Parametric Modeling** — Geometry driven by dimensions and constraints
- **Pocket** — Internal cavity created by extruding a sketch profile inward
- **Profile** — Closed 2D sketch shape used to create features
- **Project** — Bringing 3D edges or points onto a sketch plane

## R

- **Rib** — Structural feature connecting walls; defined by thickness and depth
- **Revolve** — Feature creating cylindrical/symmetrical shapes by rotating a profile around an axis
- **Rule** — iLogic code for driving parametric changes

## S

- **Sculpt** — T-Spline direct modeling in Fusion 360
- **Shell** — Hollowing a solid with specified wall thickness
- **Sketch** — 2D drawing environment for creating profiles
- **Sweep** — Feature creating geometry by moving a profile along a path
- **Symmetry** — Constraint ensuring geometry mirrors across a centerline

## T

- **Tap** — Thread cutting operation; uses a tap tool
- **Thread** — Helical feature; modeled or cosmetic
- **Timeline** — Chronological list of features; enables non-destructive editing
- **T-Spline** — Subdivision surface format allowing smooth organic shapes
- **Tolerance** — Permissible variation in dimension

## U

- **Unsuppress** — Re-enabling a suppressed feature

## V

- **Version** — Cloud-saved snapshot of design state
- **Virtual Component** — Non-physical component for BOM or design reference

## W

- **Work Coordinate System (WCS)** — Reference frame for CAM operations
- **Work Feature** — Reference geometry (point, axis, plane) for modeling
