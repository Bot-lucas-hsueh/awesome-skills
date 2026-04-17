# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Quick Fix |
|---|---------|----------|-----------|
| 1 | **Not using type hints** | 🟡 Medium | Add type annotations: `var speed: float = 10.0` |
| 2 | **Using _process for physics** | 🔴 High | Use `_physics_process` for movement |
| 3 | **Not using `@onready`** | 🟡 Medium | Use `@onready var label: Label = $Label` |
| 4 | **NodePath strings instead of refs** | 🟡 Medium | Store node references, not paths |
| 5 | **Not disconnecting signals** | 🟡 Medium | Use `disconnect()` or check `is_connected()` |
| 6 | **Instantiating scenes in _process** | 🔴 High | Preload or use object pooling |
| 7 | **Forgetting to set collision layers** | 🔴 High | Configure collision_layer and collision_mask |
| 8 | **Not using groups for organization** | 🟡 Medium | Use `add_to_group("enemies")` for filtering |
| 9 | **Ignoring input in _input** | 🟡 Medium | Handle all input in `_input`, not nodes |
| 10 | **Not using resource files** | 🟡 Medium | Use .tres files for shared data |

## 10.2 Performance Anti-Patterns

### Scripting Anti-Patterns
| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| `get_node()` in `_process` | High | Cache with @onready |
| Finding nodes by name in loops | High | Use groups or references |
| `_process` for everything | Medium | Use signals where possible |
| String operations in hot paths | Medium | Use enums, cached strings |
| Lack of static typing | Medium | Add type hints everywhere |
| Not using `_delta` | High | Always multiply by delta |

### Rendering Anti-Patterns
| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Too many dynamic lights | High | Use bakeable lights |
| Real-time shadows everywhere | High | Bake static, limit dynamic |
| High-poly models in scenes | Medium | Use LOD, simplify meshes |
| Too many transparency layers | High | Minimize alpha blending |
| Particles on CPU | Medium | Use GPU particles |
| Post-processing on mobile | High | Reduce effects for mobile |

### Scene Structure Anti-Patterns
| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Deep scene tree | Medium | Flatten hierarchy |
| Too many nodes | Medium | Use MultiMesh for copies |
| Not using prefabs/instances | Medium | Reuse scene instances |
| Missing collision shapes | High | Add appropriate colliders |

## 10.3 Memory Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Not releasing resources | High | Use `.free()` or `queue_free()` |
| Creating nodes in Update | High | Pool objects, preload |
| Large textures uncompressed | High | Use VRAM compression |
| Audio streaming everything | Medium | Stream only music, preload SFX |
| Too many active RigidBodies | Medium | Sleep when not needed |

## 10.4 Networking Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Not using delta in network sync | High | Always use delta for interpolation |
| Authority issues | High | Only move objects you own |
| Not validating server data | Critical | Always validate on server |
| High network update rate | Medium | Use 15-30 updates/sec |
| No client-side prediction | Medium | Add predictive movement |

## 10.5 Common GDScript Pitfalls

### Syntax Issues
```gdscript
# WRONG: No type hints, missing underscore
func get_position():
    return position

# CORRECT: Type hints, proper naming
func get_position() -> Vector3:
    return global_position
```

### Signal Pitfalls
```gdscript
# WRONG: Not checking connection
button.pressed.disconnect(callable)

# CORRECT: Check first
if button.pressed.is_connected(callable):
    button.pressed.disconnect(callable)

# WRONG: Missing callable in connect
button.pressed.connect(my_method)  # Godot 4

# CORRECT: Use callable
button.pressed.connect(my_method.bind())
```

### Node Path Issues
```gdscript
# WRONG: String-based paths everywhere
var pos = get_node("../Player/Label").text

# CORRECT: Proper references
@onready var player_label: Label = $"../Player/Label"
var pos = player_label.text
```

## 10.6 Best Practices Checklist

- [ ] Use type hints in all GDScript
- [ ] Cache node references with @onready
- [ ] Use signals for loose coupling
- [ ] Store shared data in .tres resources
- [ ] Use groups for filtering objects
- [ ] Profile with built-in profiler
- [ ] Use object pooling for frequent spawns
- [ ] Bake static lighting for performance
- [ ] Use Compatibility renderer for mobile
- [ ] Test on target platform early
- [ ] Use version control (Git)
- [ ] Set proper export presets
- [ ] Handle window focus in games