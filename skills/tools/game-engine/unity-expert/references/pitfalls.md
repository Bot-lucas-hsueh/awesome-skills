# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Quick Fix |
|---|---------|----------|-----------|
| 1 | **Not using GetComponent in Awake** | 🔴 High | Cache components in Awake, not Update |
| 2 | **Using FindObjectsOfType in Update** | 🔴 High | Cache references on Start/Awake |
| 3 | **Destroying objects instead of pooling** | 🔴 High | Use object pooling for bullets/effects |
| 4 | **Not disabling physics in sleep** | 🟡 Medium | Set Rigidbody.isKinematic when stationary |
| 5 | **Large textures without compression** | 🔴 high | Set max size, use compression |
| 6 | **Ignoring RaycastAll performance** | 🟡 Medium | Use single Raycast when possible |
| 7 | **String comparisons in hot paths** | 🟡 Medium | Use enums, tags as integers |
| 8 | **Not using Coroutine properly** | 🟡 Medium | Don't use while(true), use custom timing |
| 9 | **Physics on triggers without needed events** | 🟡 Medium | Disable "Collide" events when not needed |
| 10 | **UI Canvas rebuilding every frame** | 🔴 High | Cache GraphicRegistry references |

## 10.2 Performance Anti-Patterns

### Scripting Anti-Patterns
| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| GetComponent in Update | Severe | Cache in Awake |
| GameObject.Find in Update | Severe | Cache on Start |
| String operations in loops | High | Use StringBuilder or cache |
| LINQ in hot paths | High | Use for-loops instead |
| Boxing/unboxing (int to object) | Medium | Avoid object collections |
| Delegate allocations in Update | Medium | Cache delegate references |

### Rendering Anti-Patterns
| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Realtime lights on everything | High | Bake static lighting |
| Too many real-time shadows | High | Use 1-2 shadow-casting lights |
| Post-processing on mobile | High | Minimize effects on mobile |
| High-poly meshes in scenes | Medium | Use LOD, culling |
| Transparent overdraw | High | Minimize alpha-blended UI |

### Physics Anti-Patterns
| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Mesh colliders on everything | High | Use primitive colliders |
| Physics in FixedUpdate vs Update | Medium | Always use FixedUpdate |
| Continuous collision detection | Medium | Only on fast objects |
| Too many Rigidbodies | High | Use Kinematic where possible |

## 10.3 Memory Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Not releasing Addressables | High | Always call Addressables.Release() |
| Large textures uncompressed | High | UseCrunch compression, limit size |
| Audio clips loaded into memory | Medium | Load on demand, compress |
| Large asset bundles | High | Split into smaller bundles |
| No resource unloading | High | Resources.UnloadUnusedAssets() |

## 10.4 Networking Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| NetworkTransform on everything | High | Only on moving objects |
| High NetworkSendRate | High | Reduce update frequency |
| Unoptimized RPC payloads | Medium | Compress data, batch updates |
| Not using [Command] correctly | High | Use for client->server |
| No server-side validation | Critical | Validate all inputs server-side |

## 10.5 UI Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Deep Canvas hierarchy | High | Flatten UI structure |
| Camera.main calls in UI | Medium | Cache camera reference |
| Layout Groups everywhere | High | Only where needed |
| No UI atlas packing | Medium | Use Sprite Atlas |
| Event System in Update | Low | Use event-driven callbacks |

## 10.6 Best Practices Checklist

- [ ] Use IL2CPP for builds (not Mono)
- [ ] Profile with Unity Profiler early
- [ ] Use Addressables for dynamic loading
- [ ] Bake static lighting for non-moving objects
- [ ] Use object pooling for frequently spawned objects
- [ ] Cache all GetComponent references in Awake
- [ ] Use ScriptableObject for configuration data
- [ ] Implement proper versioning for save games
- [ ] Test on target device, not just editor
- [ ] Use conditional compilation for platform code
- [ ] Enable "Enter Play Mode Options" for faster iteration
- [ ] Use Package Manager for dependency management