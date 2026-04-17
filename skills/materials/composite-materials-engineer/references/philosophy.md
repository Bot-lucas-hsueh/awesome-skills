## § 4 Core Philosophy

### Design-Manufacturing-Analysis Triangle

```
                    ┌─────────────────────┐
                    │   STRUCTURAL        │
                    │   PERFORMANCE       │
                    │   (Analysis)        │
                    └──────────┬──────────┘
                               │
                    Failure criteria │ CLT
                    FEA validation  │ Test correlation
                               │
              ┌────────────────┼────────────────┐
              │                │                │
    ┌─────────┴──────┐         │        ┌───────┴────────┐
    │  MATERIAL      │         │        │ MANUFACTURING  │
    │  SELECTION     │─────────┘        │  PROCESS       │
    │  (Properties)  │   Producibility  │  (Quality)     │
    └────────────────┘   Trade-offs     └────────────────┘
         Fiber/Matrix                    Autoclave/RTM/OOA
         Architecture                    Tooling/Cure
         Allowables                      NDT/Inspection
```

### Three Governing Principles

**Principle 1 — The Building Block Approach is Non-Negotiable**
Structural confidence in composites is established through a hierarchy of tests from material coupons to full-scale structure. Skipping levels without technical justification introduces unquantified risk. Every analysis result should be traceable to validated allowables at the appropriate level of the building block pyramid.

**Principle 2 — The Weakest Link is Always the Matrix**
Fiber-dominated properties (tensile, compressive along fiber direction) are predictable and reliable. Matrix-dominated properties (transverse tensile, interlaminar shear, compressive after impact) are sensitive to process quality, environmental conditioning, and damage. Design strategies that place critical load paths in fiber-dominated orientations and minimize reliance on matrix-dominated properties produce more robust structures.

**Principle 3 — Manufacturing is Part of the Design**
A composite structure is not defined by its drawing alone — it is defined by the drawing AND the manufacturing process AND the inspection criteria. Tolerances, fiber waviness, void content limits, and cure cycle parameters are as important as ply angles and thicknesses. The Design for Manufacturability (DfM) review is a structural review, not just a production review.

---

