## § 4 · Domain Knowledge

### ARINC Standards

| Standard | Purpose | Applications |
|----------|---------|--------------|
| ARINC 429 | Two-wire data bus | Legacy aircraft, sensors |
| ARINC 664 (AFDX) | Ethernet for aviation | A380, B787, A350 |
| ARINC 653 | OS partitioning | IMA platforms |
| ARINC 661 | CDS widget standard | Display systems |
| ARINC 702 | GPS/GBAS | Navigation receivers |

### Flight Control System Types

```
Conventional (Mechanical):
├── Direct cable linkage
├── No power assistance
└── Light aircraft only

Power-Assisted (Hydraulic):
├── Hydraulic boost
├── Manual reversion capability
└── Business jets, regional aircraft

Fly-By-Wire (Digital):
├── Side stick/yoke → sensors → computers → actuators
├── Flight envelope protection
├── Automatic trim, load alleviation
└── All modern airliners

Fly-By-Light (Optical):
├── Fiber optic data transmission
├── EMI immunity
├── Military applications
└── Limited civil use
```

📄 **Full Details**: [references/08-domain-knowledge.md](references/08-domain-knowledge.md)

---
