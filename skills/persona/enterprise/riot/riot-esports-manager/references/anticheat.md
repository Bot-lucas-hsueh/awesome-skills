# Riot Esports Manager — Anti-Cheat Protocol

Full reference for §7.1 (Anti-Cheat Framework). Riot's multi-layer detection and enforcement system.

## Vanguard System Tiers

```
Tier 1 — Client-Side Integrity
├── File hash verification (game files unmodified)
├── Memory scanning (detects in-memory DLL injection)
└── Behavioral heuristics (aimbot movement patterns)

Tier 2 — Kernel-Level Detection (Vanguard)
├── Ring 0 driver running at boot
├── Detects kernel-level cheats, driver exploits
└── Blocks unsigned drivers from injecting

Tier 3 — Behavioral Analysis
├── Machine learning on 50M+ player sessions
├── Anomaly detection on APM, accuracy, reaction time
└── Pattern matching on replays (wall hacks, fog of war)

Tier 4 — Manual Investigation
├── Replay review by trained analysts
├── Player interview (if behavioral flag triggered)
└── Cross-reference with betting anomaly data

Tier 5 — Law Enforcement
├── Cooperation with gambling regulators
├── Share evidence for criminal prosecution
└── Public ban announcements (deterrence)
```

## Detection-to-Ban Workflow

```
Anomaly Detected (automated)
├── Priority 1: Immediate temp ban (24–72h) pending review
├── Priority 2: Flag for analyst queue (48–168h)
└── Priority 3: Monitor only (14-day observation)

Analyst Review
├── Clear: Remove flag, no action
├── Suspicious: Temp ban + player notification
└── Confirmed: Permanent ban + evidence documented

Appeal Process (player-initiated)
├── Submit appeal within 5 business days
├── Technical review by 3rd party analyst
├── Decision within 10 business days
└── Final ruling by Commissioner

Public Communication
├── Monthly ban report (aggregated stats)
├── Individual ban announcements for pro players
└── Transparency report annually
```

## Pro Player Additional Protocols

Pro players are held to a higher standard due to:
- Access to competitive integrity systems
- Proximity to betting markets
- Role model obligations to amateur community

**Additional requirements:**
- Mandatory anti-cheat education (annual)
- Proactive disclosure of gaming peripherals/software changes
- Periodic hardware audit during live events
- Immediate reporting of any cheating approaches received
