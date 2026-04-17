# Standard Workflow

## 8.1 Project Setup Workflow

### Phase 1: Initialization
```
Project Setup:
├── 1. Unity Hub -> New Project
├── 2. Select template:
│   ├── 3D (Built-in RP)
│   ├── 3D (URP) - Recommended
│   ├── 3D (HDRP)
│   ├── 2D
│   └── Microgame (starter kit)
├── 3. Configure:
│   ├── Project name
│   └── Save location
├── 4. Editor version selection
│   ├── 2022.3 LTS (stable)
│   └── 2023.x (latest features)
└── 5. Create project
```

### Phase 2: Project Configuration
```
Project Settings:
├── 1. Player Settings (Ctrl+Shift+S)
│   ├── Company name, Product name
│   ├── Bundle Identifier (mobile)
│   ├── Version, Build number
│   └── Icon set
├── 2. Quality Settings
│   ├── URP: Quality -> URP Asset
│   ├── Texture quality, VSync
│   └── Anti-aliasing: 4x or 8x
├── 3. Editor Settings
│   ├── Refresh mode: Visible, Auto
│   ├── Asset pipeline: V2
│   └── Enter Play Mode settings
└── 4. Tagging & Layers
    ├── Add custom tags
    └── Add custom layers (32-63)
```

### Phase 3: Package Setup
```
Package Manager:
├── 1. Essential packages:
│   ├── Post Processing (if URP built-in)
│   ├── ProBuilder (level design)
│   └── TextMeshPro
├── 2. XR Setup:
│   ├── XR Plugin Management
│   ├── XR Interaction Toolkit
│   └── OpenXR + Oculus Integration
├── 3. Addressables setup:
│   ├── Install Addressables package
│   ├── Create Addressable Groups
│   └── Configure labels
└── 4. Version control ready:
    ├── Enable "Visible Meta Files"
    └── Add .gitignore entries
```

## 8.2 Asset Pipeline

### Import Pipeline
```
Asset Import Workflow:
├── 1. Drag files into Project window
│   ├── FBX: Mesh + animations
│   ├── PSD: Sprites + layers
│   ├── Audio: WAV, MP3, OGG
│   └── Textures: PNG, TGA, PSD
├── 2. Configure import settings:
│   ├── Mesh: Read/Write, Generate colliders
│   ├── Animation: Animator Controller
│   ├── Sprite: Sprite mode (Single/Multiple)
│   └── Audio: Force to mono, load type
├── 3. Apply naming conventions:
│   ├── Art: art_chr_hero_idle
│   ├── Prefabs: pref_ab_rock_large
│   └── Scripts: cls_player_controller
└── 4. Set up asset labels for Addressables
```

### Asset Optimization
| Asset Type | Optimization | Setting |
|------------|--------------|---------|
| Textures | Compression | Max Size, Use Crunch Compression |
| Meshes | Mesh Compression | Low/Medium, Optimize mesh |
| Audio | Force to mono | For sound effects |
| Audio | Sample rate | 22k for dialog, 44k for music |
| Animations | Animation compression | Keyframe reduction |

### Asset Organization
```
Assets/
├── Art/
│   ├── Models/
│   ├── Textures/
│   ├── Materials/
│   └── Animations/
├── Audio/
│   ├── Music/
│   └── SFX/
├── Prefabs/
├── Scenes/
├── Scripts/
│   ├── Editor/
│   └── Runtime/
├── Shaders/
├── UI/
└── Resources/
    └── (Runtime loaded assets)
```

## 8.3 Build & Deployment

### Development Build
```
Development Build:
├── 1. Build Settings (Ctrl+Shift+B)
│   ├── Switch Platform (if needed)
│   ├── Development Build: Yes
│   ├── Script Debugging: Yes
│   └── Autoconnect Profiler: Yes
├── 2. Player Settings
│   ├── Scripting Backend: IL2CPP (recommended)
│   ├── API Compatibility: .NET Standard 2.1
│   └── Managed Stripping Level: Low/Medium
└── 3. Testing
    ├── Run in Editor (Enter Play Mode)
    ├── Build and Run (target device)
    └── Use Profiler (Ctrl+Shift+P)
```

### Shipping Build
```
Shipping Build Workflow:
├── 1. Pre-build checklist:
│   ├── Remove debug code, logs
│   ├── Disable Development Build
│   ├── Set Managed Stripping Level: High
│   └── Enable "Strip Engine Code"
├── 2. Code optimization:
│   ├── IL2CPP code generation
│   ├── Enable "Enable Exceptions: None"
│   └── Set "C++ Compiler Configuration": Master
├── 3. Platform-specific:
│   ├── iOS: Configure signing, set IL2CPP
│   ├── Android: Configure keystore, split APKs
│   ├── PC: Set destination folder
│   └── WebGL: Configure memory, enable decompression
└── 4. Post-build:
    ├── Test on actual device
    ├── Verify asset bundles
    └── Run performance profiling
```

### Platform Deployment
| Platform | Output | Distribution |
|----------|--------|--------------|
| Windows | .exe | Direct, Steam, Epic |
| macOS | .app | Direct, Steam, App Store |
| Linux | .x86_64 | Direct, Steam |
| WebGL | HTML5 | itch.io, Simmer |
| iOS | .ipa | TestFlight, App Store |
| Android | .aab | Google Play |
| Console | .pak | Platform portal |