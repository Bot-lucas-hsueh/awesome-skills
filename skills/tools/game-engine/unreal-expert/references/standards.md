# Standards & Reference

## 7.1 Official Documentation

- [Unreal Engine Documentation](https://docs.unrealengine.com)
- [Epic Games Developer Community](https://dev.epicgames.com)
- [Unreal Engine API Reference](https://docs.unrealengine.com/en-US/API)
- [Blueprints API](https://docs.unrealengine.com/en-US/Engine/Blueprints)
- [C++ API Documentation](https://docs.unrealengine.com/en-US/Engine/Physics)
- [Niagara VFX System](https://docs.unrealengine.com/en-US/Engine/Niagara)
- [Sequencer & Movie Render Queue](https://docs.unrealengine.com/en-US/Engine/Sequencer)

## 7.2 Platform Compatibility

### Supported Platforms
| Platform | Support Level | Notes |
|----------|---------------|-------|
| Windows 10/11 | Full | Primary development platform |
| macOS | Full | Metal rendering support |
| Linux | Full | Vulkan rendering |
| PlayStation 5 | Full | Console development |
| Xbox Series X/S | Full | Console development |
| Nintendo Switch | Full | Mobile/console hybrid |
| iOS/Android | Full | Mobile deployment |
| HTML5 (WebGL) | Deprecated | Use Pixel Streaming instead |

### Version Notes
- UE 5.3+ requires Windows 10 version 1903 or later
- Metro co-app packaging required for Xbox
- Mobile: Minimum iOS 12, Android API 21

## 7.3 Common Commands & Workflows

### Blueprint Operations
| Action | Location | Notes |
|--------|----------|-------|
| Create Blueprint | Right-click Content Browser | Inherit from Actor, Pawn, Character |
| Compile Blueprint | Toolbar button or Ctrl+Alt+P | Always compile after changes |
| Open Level Blueprint | Toolbar "Blueprints" -> "Open Level Blueprint" | Level-wide logic |
| Create Custom Event | Event Graph -> Right-click | Callable from other Blueprints |
| Promote to Variable | Right-click variable pin | Creates new variable with type |

### C++ Project Commands
```bash
# Generate project files
uproject -generate
# Build development
Engine/Build/BatchFiles/Build.bat Development Win64 -Project="MyProject"
# Package for shipping
Engine/Build/BatchFiles/RunUAT.bat BuildCookRun -project=MyProject.uproject -platform=Win64 -build
```

### Shader Languages
- **HLSL** - Primary shader language in Unreal
- **Material Editor** - Visual shader graph (generates HLSL)
- **Niagara Modules** - Custom HLSL for particle systems

## 7.4 Engine Version Compatibility

| Engine Version | Status | Notes |
|----------------|--------|-------|
| UE 5.4 | Current | Latest stable, Chaos physics |
| UE 5.3 | Supported | Virtual Shadow Maps, Nanite production-ready |
| UE 5.2 | Supported | Lumen improvements, Crowd system |
| UE 5.1 | Supported | Lumen + Nanite out of beta |
| UE 5.0 | Legacy | Initial release with Lumen/Nanite |
| UE 4.27 | Extended | Still widely used, no longer updated |

### Plugin Compatibility
- Most marketplace plugins support UE 5.1+
- C++ plugins require recompilation per major version
- Blueprint-only plugins often forward-compatible