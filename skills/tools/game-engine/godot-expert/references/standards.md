# Standards & Reference

## 7.1 Official Documentation

- [Godot Documentation](https://docs.godotengine.org)
- [Godot API Reference](https://docs.godotengine.org/en/stable/classes/index.html)
- [Godot Engine Homepage](https://godotengine.org)
- [Godot Wiki](https://github.com/godotengine/godot/wiki)
- [Godot Shaders Reference](https://docs.godotengine.org/en/stable/shaders/index.html)
- [Godot Best Practices](https://docs.godotengine.org/en/stable/tutorials/best_practices/index.html)
- [Godot Asset Library](https://godotengine.org/asset-library)

## 7.2 Platform Compatibility

### Supported Platforms
| Platform | Support Level | Notes |
|----------|---------------|-------|
| Windows | Full | Primary dev platform |
| macOS | Full | Apple Silicon + Intel |
| Linux | Full | X11 + Wayland |
| HTML5/WebGL | Full | Export to WebAssembly |
| iOS | Full | Mobile export |
| Android | Full | Mobile export |
| Windows (UWP) | Full | Microsoft Store |
| PlayStation 4 | Full | Console export (requires license) |
| PlayStation 5 | Full | Console export (requires license) |
| Nintendo Switch | Full | Console export (requires license) |
| Xbox | Full | GDK/XDK integration |
| VR/AR | Full | OpenXR support |

### Version Notes
- Godot 4.x: Current, Vulkan renderer
- Godot 3.x: OpenGL ES, still supported
- Forward+ renderer: Desktop Vulkan (high-end)
- Mobile renderer: Vulkan/OpenGL ES 3.0
- Compatibility renderer: OpenGL ES 3.0 (mobile-friendly)

## 7.3 Common Commands & Workflows

### Editor Operations
| Action | Shortcut | Notes |
|--------|----------|-------|
| Play | F5 | Run main scene |
| Debug | F6 | Run current scene |
| Stop | F7 | Stop execution |
| Quick Run | F5 | Play from main scene |
| Save | Ctrl+S | Save scene |
| Build | Ctrl+Shift+B | Export project |

### GDScript Patterns
```gdscript
# Basic Node script
extends Node

@export var speed: float = 100.0
@onready var sprite: Sprite2D = $Sprite2D

func _ready() -> void:
    print("Node ready")

func _physics_process(delta: float) -> void:
    position += Vector2.RIGHT * speed * delta

# Signal connection (auto-connect)
func _on_button_pressed() -> void:
    print("Button pressed")

# Static typing (recommended)
var health: int = 100
var velocity: Vector2 = Vector2.ZERO

# Export variables (inspectable)
@export_category("Movement")
@export var max_speed: float = 200.0
```

### Shader Languages
- **GDScript** - Primary scripting
- **Godot Shader Language (.gdshader)** - Visual + text shaders
- **Shader Graph** - Visual node editor (Godot 4.x)
- **VisualShader** - Node-based (Godot 3.x)

## 7.4 Engine Version Compatibility

| Godot Version | Status | Notes |
|---------------|--------|-------|
| Godot 4.3 | Current | Latest stable |
| Godot 4.2 | Supported | Forward+ renderer stable |
| Godot 4.1 | Supported | Many fixes |
| Godot 4.0 | Legacy | Initial 4.x |
| Godot 3.6 | Supported | LTS, GDScript 2.0 ready |

### Compatibility Notes
- Godot 4.x requires Vulkan-capable GPU for Forward+
- Use "Compatibility" renderer for older hardware
- GDScript 2.0 (Godot 4.x) has breaking changes from GDScript 1.x
- C# support in Godot 4.x requires .NET SDK