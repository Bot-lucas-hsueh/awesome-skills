## § 7 · Standard Workflow

### Phase 1: Detection & Triage (0-1 hour)

```
├── Alert validation (false positive check)
├── Initial scope assessment
├── Severity classification
├── Response team activation
└── [✓ Done]: Incident declared, team mobilized
    [✗ FAIL]: Insufficient information → gather more data
```

### Phase 2: Containment (1-4 hours)

```
├── Short-term containment (isolate affected systems)
├── Evidence preservation (memory dumps, disk images)
├── System backups before changes
├── Communication to stakeholders
└── [✓ Done]: Attack stopped, evidence secured
    [✗ FAIL]: Containment failed → escalate, seek help
```

### Phase 3: Investigation (4-48 hours)

```
├── Forensic analysis (disk, memory, network)
├── Timeline reconstruction
├── IOC identification
├── Scope determination (affected systems, data)
└── [✓ Done]: Root cause identified, full scope known
    [✗ FAIL]: Attribution unclear → continue analysis
```

### Phase 4: Eradication & Recovery (48-72 hours)

```
├── Remove malware and backdoors
├── Patch exploited vulnerabilities
├── Reset all compromised credentials
├── Restore from clean backups
└── [✓ Done]: Systems clean, operations restored
    [✗ FAIL]: Persistence detected → re-eradicate
```

### Phase 5: Post-Incident (1-2 weeks)

```
├── Executive briefing
├── Regulatory notifications (if required)
├── Lessons learned session
├── Security improvements implementation
└── [✓ Done]: Report delivered, improvements in progress
    [✗ FAIL]: No improvements → missed opportunity
```

---
