## § 7 · Domain Knowledge Reference

### 7.1 Ontology Design Principles

**The 5 Ws of Object Types:**
1. **What** is this entity? (Clear business definition)
2. **Who** owns it? (Business owner, technical owner)
3. **Where** does the data come from? (Source systems)
4. **When** is it updated? (Freshness SLAs)
5. **Why** does it exist? (Operational use cases)

**Link Type Design:**
- Direction matters: `Employee.reportsTo` vs `Manager.manages`
- Cardinality: 1:1, 1:N, N:M with junction objects
- Temporal links: Valid from/to dates for historical tracking
- Confidence scoring: For inferred relationships

### 7.2 Security Implementation

```python
# Example: Row-level security in Ontology
@permissioned_view
class AircraftView:
    def can_read(self, user, aircraft):
        # Clearance check
        if aircraft.classification == "TOP SECRET":
            return user.clearance_level >= Classification.TOP_SECRET
        
        # Need-to-know (compartmented)
        if aircraft.program_access:
            return user.program_access.intersects(aircraft.program_access)
        
        # Organization scope
        return user.organization in aircraft.visible_to_organizations
    
    def can_write(self, user, aircraft, action):
        # Additional write controls
        if action == "ScheduleMaintenance":
            return user.role in ["MAINTENANCE_CHIEF", "FLEET_MANAGER"]
        return False
```

---
