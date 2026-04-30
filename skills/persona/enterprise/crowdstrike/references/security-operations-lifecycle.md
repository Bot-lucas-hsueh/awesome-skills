## 7. Security Operations Lifecycle

```
PHASE 1: PREVENT
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Deploy      │───→│ Configure   │───→│ Enable      │───→│ Validate    │
│ Sensors     │ ✓  │ Policies    │ ✓  │ ML Models   │ ✓  │ Coverage    │ ✓
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
     │                                                    ↓
     │                                           ┌─────────────┐
     │                                           │ 100% Target │
     │                                           │ Sensor Uptime│
     │                                           └─────────────┘
     ↓
PHASE 2: DETECT & HUNT
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Monitor     │───→│ Analyze     │───→│ Hunt        │───→│ Validate    │
│ Threat Graph│ ✓  │ IOAs/IOCs   │ ✓  │ Hypotheses  │ ✓  │ Threats     │ ✓
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
     │                                                    ↓
     │                                           ┌─────────────┐
     │                                           │ <1 min MTTD │
     │                                           └─────────────┘
     ↓
PHASE 3: RESPOND (1-10-60 SLA)
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Contain     │───→│ Eradicate   │───→│ Recover     │───→│ Improve     │
│ (Isolate)   │ ✓  │ Threat      │ ✓  │ Systems     │ ✓  │ Defenses    │ ✓
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
     │                                                    ↓
     │                                           ┌─────────────┐
     │                                           │ <60 min MTTR│
     │                                           └─────────────┘
```
