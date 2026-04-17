# Standard Workflow

## 8.1 Project Setup Workflow

### Phase 1: Initialization
```
Project Setup:
├── 1. Godot -> New Project
├── 2. Select template:
│   ├── (Select renderer)
│   │   ├── Forward+ (Vulkan, desktop)
│   │   ├── Mobile (Vulkan/GLES3)
│   │   └── Compatibility (GLES3, mobile-friendly)
│   ├── 3D Scene
│   ├── 2D Scene
│   └── Start with preset
├── 3. Configure:
│   ├── Project name
│   ├── Save location
│   └── Renderer selection (see above)
├── 4. Project Settings
│   ├── Display -> Window -> Size
│   │   ├── Viewport Width/Height
│   │   └── Stretch Mode: canvas_items
│   └── Input Map
└── 5. Add to version control
```

### Phase 2: Editor Configuration
```
Editor Setup:
├── 1. Project Settings -> Rendering
│   ├── Textures -> Canvas Textures
│   └── Vram Compression -> Import formats
├── 2. Project Settings -> Physics
│   ├── 3D Default Gravity: 9.8
│   └── 2D Default Gravity: 980
├── 3. Project Settings -> Input
│   ├── Add action mappings
│   └── Addjoypad mappings
├── 4. Editor Settings
│   ├── File Browser -> Default View Mode
│   └── Text Editor -> Theme
└── 5. Import presets
    └── Import .png as 2D, .glb as 3D
```

### Phase 3: Scene Structure
```
Scene Organization:
res://
├── scenes/
│   ├── main.tscn (Main scene)
│   ├── player/
│   │   ├── player.tscn
│   │   └── player.gd
│   └── levels/
│       ├── level_1.tscn
│       └── level_2.tscn
├── scripts/
│   ├── autoload/
│   │   ├── game_manager.gd
│   │   └── save_system.gd
│   └── utils/
│       └── math_utils.gd
├── resources/
│   ├── items/
│   │   └── item_data.tres
│   └── characters/
│       └── enemy_data.tres
├── assets/
│   ├── textures/
│   ├── models/
│   ├── audio/
│   │   ├── music/
│   │   └── sfx/
│   └── fonts/
└── export_presets.cfg
```

## 8.2 Asset Pipeline

### Import Pipeline
```
Asset Import:
├── 1. Drag files into FileSystem dock
│   ├── Images: PNG, JPG, WebP, SVG
│   ├── Models: glTF 2.0, GLB, OBJ
│   ├── Audio: WAV, OGG, MP3
│   └── Scenes: TSCN, PackedScene
├── 2. Configure import:
│   ├── Images: compress -> VRAM Compressed
│   ├── Models: import -> Enabled
│   ├── Audio: both import & stream options
│   └── TSCN: editable -> Yes/No
├── 3. Set up resource previews:
│   └── Thumbnail Size in Editor Settings
└── 4. Use .godot-gitignore for VCS
```

### Asset Optimization
| Asset Type | Optimization | Setting |
|------------|--------------|---------|
| Textures | Compression | VRAM Compressed / Lossless |
| Textures | Max Size | Limit to power of 2 (1024, 2048) |
| 3D Models | Compression | Enabled, reduce polygons |
| Audio | Stream | Enabled for music, disabled for SFX |
| Audio | Bitrate | 128k for SFX, 192k for music |

### Asset Organization Best Practices
```
res://
├── art/                  # Original art files
│   ├── sprites/
│   └── models/
├── assets/               # Imported/optimized assets
│   ├── sprites/
│   ├── textures/
│   └── materials/
├── scenes/               # Game scenes
├── scripts/               # GDScript files
├── resources/             # Resource files (.tres)
├── addons/                # Editor plugins
└── project.godot         # Project file
```

## 8.3 Build & Deployment

### Development Build
```
Development Workflow:
├── 1. Run in editor
│   ├── F5: Run main scene
│   ├── F6: Run current scene
│   └── F7: Stop
├── 2. Debug options
│   ├── Project -> Export -> Debug
│   └── Run with debugger (F5 with debugger)
├── 3. Profiling
│   ├── Debug -> Profiler
│   ├── Debug -> Remote Debug
│   └── Debug Draw Mode (for physics/visuals)
└── 4. Scene testing
    └── Use "Run Current Scene" for quick tests
```

### Export Workflow
```
Export Process:
├── 1. Project -> Export
├── 2. Add preset:
│   ├── Web (HTML5)
│   ├── Windows
│   ├── macOS
│   ├── Linux
│   ├── Android
│   ├── iOS
│   └── Console (requires SDK)
├── 3. Configure preset:
│   ├── Export path
│   ├── Extensions support
│   ├── Custom template
│   └── Release/Debug build
├── 4. Platform-specific:
│   ├── Android: keystore, SDK path
│   ├── iOS: signing identity, provisioning
│   └── Console: platform SDK
└── 5. Export Project
```

### Platform Export
| Platform | Output | Distribution |
|----------|--------|--------------|
| Windows | .exe, .pck | Direct, Itch.io, Steam |
| macOS | .app, .zip | Direct, Steam |
| Linux | AppImage, .pck | Direct, Steam, Itch.io |
| Web | HTML5 + WASM | Itch.io, Simmer |
| Android | .apk, .aab | Google Play, Amazon |
| iOS | .ipa | TestFlight, App Store |
| Console | .pck | Platform-specific |