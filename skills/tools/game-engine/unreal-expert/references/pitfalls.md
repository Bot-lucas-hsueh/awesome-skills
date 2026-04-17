# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Quick Fix |
|---|---------|----------|-----------|
| 1 | **Not compiling Blueprints before testing** | 🔴 High | Always compile (Ctrl+Alt+P) or use auto-compile |
| 2 | **Using Tick for everything** | 🔴 High | Use Timers, Events, or interpolation instead |
| 3 | **Overusing Cast nodes** | 🟡 Medium | Store references as specific type, avoid repeated casts |
| 4 | **Ignoring collision presets** | 🔴 High | Use proper collision channels (WorldStatic, Pawn, etc.) |
| 5 | **Heavy logic in Tick** | 🔴 High | Move to async tasks or use delta time caching |
| 6 | **Not using const functions** | 🟡 Medium | Mark read-only functions as const for optimization |
| 7 | **Skipping LOD setup** | 🔴 High | Configure LOD on all skeletal/static meshes |
| 8 | **Not optimizing materials** | 🔴 High | Reduce instruction count, use material instances |
| 9 | **Ignoring build warnings** | 🟡 Medium | Address all warnings before shipping |
| 10 | **Debug objects left in shipping build** | 🟡 Medium | Remove debug spheres, logs before package |

## 10.2 Performance Anti-Patterns

### Blueprint Performance
| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| GetAllActorsOfClass in Tick | Severe | Cache references on BeginPlay |
| String comparisons in loops | High | Use Enums or name comparisons |
| Physics in Tick | High | Use simulation ticks or sub-stepping |
| Construction Script logic | Medium | Move to BeginPlay |
| Heavy foreach loops | Medium | Use reverse for loops, break early |

### C++ Performance
| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Not using UProperty replication | High | Mark variables with UPROPERTY(Replicated) |
| Raw pointer usage | Medium | Use TWeakObjectPtr for observers |
| Heavy allocations in game thread | High | Use memory pools, async allocation |
| Not using const refs | Low | Use const FVector& in functions |
| Lock every frame | High | Use lock-free structures |

### Rendering Anti-Patterns
| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Overdraw from transparency | High | Minimize alpha-blended surfaces |
| Too many shadows | High | Use cascade shadow maps sparingly |
| Unused materials on models | Medium | Remove unused material slots |
| Nanite on simple geometry | Low | Only on high-poly meshes |
| Lumen on small scenes | Medium | Use baked lighting instead |

## 10.3 Memory & Physics Anti-Patterns

### Memory Issues
| Issue | Detection | Fix |
|-------|-----------|-----|
| Memory leaks | `stat mem` shows growth | Use `CollectGarbage()` periodically |
| Fragmentation | Profiler shows increasing allocation time | Use pool allocators |
| UObject proliferation | High object count | Pool frequently-used objects |
| Texture streaming | Pop-in, stutters | Preload critical textures |

### Physics Anti-Patterns
| Anti-Pattern | Impact | Fix |
|--------------|--------|-----|
| Complex mesh colliders everywhere | High | Use simplified primitives (Sphere, Box, Capsule) |
| Physics enabled on dormant objects | Medium | Set "Simulation Generates Hit Events" to false |
| Ragdolls always active | High | Blend to animation, enable physics on death |
| No physics profiling | Medium | Use Chaos Profiler, optimize step count |

## 10.4 Networking Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Unreliable replicated actors | High | Mark movement as unreliable, position reliable |
| Server authority ignored | Critical | Validate all state on server |
| Not using RepNotify | Medium | Use OnRep_ functions for client updates |
| Frequent RPC calls | Medium | Batch updates, use variable replication |
| No connection loss handling | High | Implement reconnect logic, state sync |

## 10.5 Best Practices Checklist

- [ ] Use version control (Git LFS for assets)
- [ ] Enable "Always Compile" in Blueprint settings
- [ ] Profile in Release build, not Debug
- [ ] Use Asset Manager for async loading
- [ ] Implement proper save system with versioning
- [ ] Set up CI/CD for automated builds
- [ ] Use Blueprint Function Libraries for shared functions
- [ ] Mark C++ classes with appropriate UCLASS specifiers
- [ ] Enable "Cook On The Fly" for development
- [ ] Test on target hardware early and often