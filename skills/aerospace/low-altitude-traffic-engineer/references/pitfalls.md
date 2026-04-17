## § 10 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Treating UTM Like Ground Traffic Control
**❌ BAD**: Designing a UTM that directly commands aircraft maneuvers (like a highway traffic management system directing cars to change lanes on command)
```
// Wrong design: UTM issues direct movement commands
utm.send_command(aircraft_id, "TURN_LEFT_HEADING_270")
utm.send_command(aircraft_id, "DESCEND_TO_FL_005")
```
**✅ GOOD**: UTM provides conflict advisories; pilots/autopilots retain authority and decide how to comply
```
// Correct: UTM issues advisory, aircraft reports compliance
utm.issue_conflict_advisory(aircraft_id, {
  "conflict_time": "T+45s",
  "conflicting_vehicle": "UAS-4821",
  "recommended_action": "EXPEDITE_CLIMB",
  "mandatory_compliance_time": "T+30s"
})
// Aircraft autopilot selects maneuver; reports trajectory update
```
**Why it matters**: UTM lacks the authority, liability framework, and real-time aircraft state knowledge to safely command maneuvers. Operators are responsible for their aircraft.

