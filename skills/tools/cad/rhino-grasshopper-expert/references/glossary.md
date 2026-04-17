# Glossary

## A

- **Arc** — Portion of a circle; defined by center-radius-angle or 3 points
- **Asymptote** — Line a curve approaches but never reaches (rational NURBS)

## B

- **Bezier Curve** — Polynomial curve defined by control points; basis for NURBS
- **BlendSrf** — Creates a smooth surface between two surface edges
- **Boolean** — Set operations (Union, Difference, Intersection) on solids/surfaces
- **BRep (Boundary Representation)** — Geometry defined by boundaries (faces, edges, vertices)

## C

- **CPlane (Construction Plane)** — Reference plane for 2D drawing; adjustable via CPlane command
- **Control Point (CV)** — Vertex of the control polygon defining a NURBS curve/surface
- **Control Polygon** — Connected line segments through control points
- **Crease** — Sharp edge where surface tangent changes abruptly

## D

- **Degree** — Polynomial order of NURBS basis function; degree 3 = cubic
- **Divide** — Splits curve into equal segments (points at each division)
- **Domain** — Range of parameter values (t) for a curve/surface (e.g., 0 to 1)

## E

- **EdgeSrf** — Creates a surface from 3 or 4 edge curves
- **Extrude** — Extends curve perpendicular to its plane to create surface/solid

## F

- **Face** — Individual surface of a BRep body
- **Flip** — Reverses surface normal direction or curve direction
- **Freeform** — Unconstrained NURBS surface; any shape possible
- **Fillet** — Rounded edge (solid) or blended curve (surface)

## G

- **G0 (Position)** — Geometric continuity level 0; curves just touch
- **G1 (Tangent)** — Geometric continuity level 1; smooth tangent
- **G2 (Curvature)** — Geometric continuity level 2; smooth curvature reflection
- **Graft** — Grasshopper operation creating one branch per item
- **Grasshopper** — Visual scripting environment for parametric design in Rhino

## H

- **Helix** — Spiral curve around an axis; parameters: turns, pitch, radius

## I

- **IGES** — Neutral file format for exchanging NURBS geometry between CAD systems
- **InterpCrv (Interpolate Curve)** — Curve passing through specified points

## K

- **Kangaroo** — Physics engine plugin for Grasshopper (form-finding, simulation)
- **Karamba** — Structural analysis plugin for Grasshopper
- **Knot** — Parameter value where basis functions overlap; affects curve shape
- **Knot Vector** — Sequence of parameter values defining NURBS basis functions

## L

- **Ladybug** — Environmental analysis plugin for Grasshopper (sun, wind, energy)
- **Loft** — Surface between two or more profile curves
- **Loxodrome** — Curve maintaining constant bearing; used in Ship Hatch patterns

## M

- **MatchSrf** — Adjusts surface edge to match continuity with adjacent surface
- **Mesh** — Faceted geometry; triangles or quads; vs NURBS smooth surfaces
- **Mullion** — Structural bar in curtain wall systems (architectural glazing)

## N

- **NURBS (Non-Uniform Rational B-Splines)** — Mathematical representation for curves and surfaces
- **Naked Edge** — Unjoined surface boundary; open edge of a solid

## O

- **Offset** — Geometry at constant distance from original (curve/surface normal)

## P

- **Patch** — Surface fitted through points or curves; uses spline approximation
- **Periodicity** — Curve/surface that joins smoothly end-to-end (closed)
- **Plane** — 2D infinite surface; base for construction and drawing
- **Point Edit** — Direct manipulation of NURBS control points
- **Polyline** — Connected straight line segments

## R

- **Rail** — Path curve for sweep operations
- **Rebuild** — Resample curve/surface with new control point count/degree
- **RhinoCommon** — .NET SDK for Rhino plugin development
- **Ruled Surface** — Surface between two curves; linear interpolation

## S

- **Shatter** — Splits curve at parameter values into separate segments
- **Simplify** — Reduce curve complexity by removing redundant points
- **Solid** — Closed BRep with no naked edges; used for Boolean operations
- **Span** — Portion of curve between two knots
- **SubD (Subdivision Surface)** — Smooth surface from control cage; between mesh and NURBS
- **Sweep1** — Surface along single rail curve with profile
- **Sweep2** — Surface between two rail curves with profile

## T

- **Tangent** — Direction of curve at a point; slope
- **Trim** — Remove portion of surface/plane using boundary curve
- **Twist** — Rotation around curve tangent

## U

- **UnifyMeshNormals** — Force all mesh faces to same normal direction

## V

- **Viewport** — 3D view window; multiple viewports supported (4-view layout)
- **ViewportRotation** — Rotate parallel view without changing target

## W

- **Weaverbird** — Mesh editing plugin for Grasshopper (subdivision, smoothing)
- **Weighted Control Point** — NURBS control point with weight factor; affects local influence

## X

- **Xform** — Transformation matrix; applies translation, rotation, scale

## Y

- **Yield** — Grasshopper feature: pauses solver for real-time interaction
