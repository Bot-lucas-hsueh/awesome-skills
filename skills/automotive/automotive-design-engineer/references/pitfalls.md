## § 10 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Styling Sign-Off Before Engineering Hard Points
**❌ BAD**: Design studio locks exterior styling without engineering hard points defined
**✅ GOOD**: Engineering hard points must be approved before styling development begins:
```
Critical hard points that lock before styling:
  ✓ Front crash structure (crumple zone minimum length: 400-500mm)
  ✓ Side structure (rocker height, B-pillar width minimum)
  ✓ Pedestrian protection zone (hood leading edge height, grille keep-out)
  ✓ ADAS sensor mounting positions (with FOV envelopes)
  ✓ H-point and roof height (regulatory sight lines)

Common mistake: styling sets hood line at 750mm above ground → fails pedestrian
protection ECE R127 (head form drop angle requirement) → styling change needed
at design freeze (2 years into program, $50M tooling investment at risk)
```

