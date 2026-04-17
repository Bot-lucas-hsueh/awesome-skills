# Standards & Reference

## 7.1 Official Documentation

- [Unity Documentation](https://docs.unity3d.com)
- [Unity Manual](https://docs.unity3d.com/Manual/index.html)
- [Unity Scripting API](https://docs.unity3d.com/ScriptReference/index.html)
- [Unity Learn](https://learn.unity.com)
- [Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-manager-ui@latest)
- [Unity Asset Store](https://assetstore.unity.com)
- [Unity Best Practices Guide](https://unity.com/resources)

## 7.2 Platform Compatibility

### Supported Platforms
| Platform | Support Level | Notes |
|----------|---------------|-------|
| Windows | Full | Primary dev platform, DirectX 12 |
| macOS | Full | Metal rendering, Apple Silicon native |
| Linux | Full | OpenGL/Vulkan |
| WebGL | Full | Build for web, WebAssembly |
| iOS | Full | Metal, ARKit integration |
| Android | Full | Vulkan/OpenGL ES, ARM64 |
| PlayStation 4/5 | Full | Pro license required |
| Xbox One/Series | Full | ID@Xbox program |
| Nintendo Switch | Full | Unity Pro + platform add-on |
| VR/AR | Full | XR Interaction Toolkit |

### Version Notes
- Unity 2022 LTS: Recommended for production
- Unity 6 (2023): Latest with improved performance
- URP: Universal Render Pipeline for cross-platform
- HDRP: High Definition Render Pipeline for PC/console

## 7.3 Common Commands & Workflows

### Editor Operations
| Action | Shortcut | Notes |
|--------|----------|-------|
| Play | Ctrl+P | Enter Play Mode |
| Pause | Ctrl+Shift+P | Toggle pause |
| Stop | Ctrl+Shift+S | Exit Play Mode |
| Build | Ctrl+Shift+B | Open Build Settings |
| Search | Ctrl+K | Project window search |
| Create Script | Ctrl+Shift+A | Add component |

### Scripting Patterns
```csharp
// MonoBehaviour template
using UnityEngine;

public class MyClass : MonoBehaviour
{
    [SerializeField] private float speed;
    private Rigidbody rb;
    
    private void Awake() { rb = GetComponent<Rigidbody>(); }
    private void FixedUpdate() { /* Physics */ }
    private void Update() { /* Per-frame logic */ }
}

// Singleton pattern
public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }
    private void Awake() => Instance = this;
}
```

### Shader Languages
- **ShaderLab** - Unity's shader format
- **HLSL** - For Surface Shaders, Compute Shaders
- **GLSL** - For OpenGL-specific shaders
- **Shader Graph** - Visual node-based editor (URP/HDRP)

## 7.4 Engine Version Compatibility

| Unity Version | Status | Notes |
|---------------|--------|-------|
| 2022.3 LTS | Current | Long-term support, recommended |
| 2023.1 | Current | Latest feature release |
| 2021.3 LTS | Supported | Extended support |
| 2020.3 LTS | Legacy | Still functional |
| 2019.4 LTS | Legacy | Limited support |

### Package Compatibility
| Package | Min Version | Notes |
|---------|-------------|-------|
| URP | 12.0+ | Unity 2021+ |
| HDRP | 12.0+ | Requires DX12/Metal |
| XR Interaction Toolkit | 2.0+ | For VR/AR |
| Addressables | 1.19+ | Asset loading |
| Entities (ECS) | 1.0+ | DOTS framework |