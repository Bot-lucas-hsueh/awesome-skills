# CNC Operator — Standards & Reference

## Industry Standards & Certification Bodies

### Standards Organizations

**ISO (International Organization for Standardization)** — Global standards body. Key CNC-relevant standards: ISO 6983 (NC programming), ISO 13399 (cutting tool data).

**ASME (American Society of Mechanical Engineers)** — North American standards. ASME Y14.5 (GD&T), ASME B5.54 (CNC machine evaluation).

**ANSI (American National Standards Institute)** — Coordinates US standards. ANSI B11.9 (safety requirements for machine tools).

**DIN (Deutsches Institut für Normung)** — German standards. DIN 66025 (NC programming, basis for ISO 6983).

**JIS (Japanese Industrial Standards)** — Japanese manufacturing standards. JIS B 0170 for cutting tool terminology.

### CNC Programming Standards

**ISO 6983 (DIN 66025)** — NC programming language standard. Defines G-codes and M-codes syntax. Although largely followed, manufacturers add proprietary codes.

**ISO 13399** — Cutting tool data representation and exchange. Enables tool data transfer between CAM and CNC.

**STEP-NC (ISO 10303)** — Advanced CNC programming standard connecting CAD/CAM directly to CNC without post-processing.

### Machine Tool Evaluation

**ASME B5.54** — Methods for Evaluating CNC Machine Tools. Includes accuracy testing (linear, positioning) and repeatability.

**VDI 3441** — Statistical testing of machine tool positioning accuracy.

**ISO 9283** — Manipulating industrial robots — performance criteria and related test methods.

### Quality Standards

**ASME Y14.5** — Dimensioning and Tolerancing. US standard for GD&T symbols and rules.

**ISO 1101** — Geometrical product specifications — tolerancing principles.

**CMM Calibration** — ISO 10360 series for coordinate measuring machine performance verification.

### Safety Standards

**ANSI B11.TR3** — Risk assessment for machine tools.

**ISO 12100** — Safety of machinery — general principles for design.

**NFPA 79** — Electrical standard for industrial machinery.

## Professional Certifications

**NIMS (National Institute for Metalworking Skills)** — Machinist certifications: CNC Turning, CNC Milling, CNC Programming. Website: nims-skills.org

**Mastercam Certification** — CAM software certification for CNC programmers.

** Haas Factory Outlet (HFO) Training** — Machine-specific operator training.

**Society of Manufacturing Engineers (SME)** — Manufacturing engineering certifications.

## Machining Data References

### Speed and Feed Formulas

**Spindle Speed (RPM):** RPM = (SFM × 12) / (π × Diameter)

**Feed Rate:** Feed Rate = RPM × IPR × Number of Flutes

**Material Removal Rate (MRR):** MRR (in³/min) = DOC × WOC × Feed Rate

### Surface Feet per Minute (SFM) Reference

| Material | Carbide SFM | HSS SFM |
|----------|------------|---------|
| Aluminum 6061 | 800-1000 | 300-400 |
| Aluminum 7075 | 600-800 | 250-350 |
| Carbon Steel 1018 | 200-300 | 80-100 |
| Stainless 304 | 100-150 | 40-60 |
| Stainless 316 | 80-120 | 30-50 |
| Titanium Ti-6Al-4V | 80-120 | 30-50 |
| Brass | 200-400 | 200-400 |
| Cast Iron | 150-250 | 60-100 |
| Tool Steel | 100-150 | 40-60 |

### Tool Geometry Reference

**Carbide Insert Grades:**
- PVD-coated: General purpose, sharp edges
- CVD-coated: Wear-resistant, interrupted cuts
- Uncoated: Non-ferrous, finishing

**Coating Colors:**
- TiN (Gold): General purpose
- TiAlN (Purple/Black): High-temp alloys
- ZrN (Silver): Aluminum, non-ferrous
- Diamond: Composites, graphite

### G-Code Quick Reference

| Code | Function |
|------|----------|
| G00 | Rapid positioning |
| G01 | Linear interpolation (feed) |
| G02 | Circular interpolation CW |
| G03 | Circular interpolation CCW |
| G04 | Dwell |
| G17-G19 | Plane selection (XY/XZ/YZ) |
| G20 | Inch units |
| G21 | Metric units |
| G28 | Return to home |
| G40 | Cancel cutter compensation |
| G41/G42 | Cutter compensation left/right |
| G43 | Tool length offset |
| G54-G59 | Work coordinate systems |
| G80 | Cancel canned cycle |
| G81-G89 | Canned drilling cycles |
| G90 | Absolute positioning |
| G91 | Incremental positioning |

### M-Code Quick Reference

| Code | Function |
|------|----------|
| M00 | Program stop (optional) |
| M01 | Program stop (optional, with operator confirmation) |
| M02 | End of program |
| M03 | Spindle on CW |
| M04 | Spindle on CCW |
| M05 | Spindle stop |
| M06 | Tool change |
| M08 | Coolant on |
| M09 | Coolant off |
| M30 | End of program and rewind |

## Technical Publications

**Machinery's Handbook** — The bible of machining. Every machinist's reference. Industrial Press.

**Modern Machine Shop** — Trade publication with practical machining articles. Website: mmsonline.com

**The CNC Cookbook** — Online resource for CNC programming and machining. Website: cnccookbook.com
