# Standard Workflow

## 8.1 Project Setup Workflow

### Phase 1: Initialization
```
Project Setup:
├── 1. Launch Epic Games Launcher
├── 2. Select "Games" category template
├── 3. Choose template (Blank, First Person, Third Person, Top Down)
├── 4. Select target platform (Mobile/Desktop/Console)
├── 5. Choose quality preset (Maximum Quality/Balanced/Performance)
├── 6. Configure starter content (Include/Exclude)
└── 7. Create project in desired directory
```

### Phase 2: Editor Configuration
```
Editor Setup:
├── 1. Project Settings -> Input
│   ├── Configure axis mappings
│   └── Configure action mappings
├── 2. Project Settings -> Platforms
│   ├── Set default platform
│   └── Configure platform-specific options
├── 3. Editor Preferences -> Content Browser
│   ├── Set default asset directory
│   └── Configure auto-save interval
└── 4. Enable required plugins (Niagara, Chaos, etc.)
```

### Phase 3: Version Control Setup
```
Version Control:
├── 1. Enable Git or Perforce plugin
├── 2. Configure .gitignore for UE-specific files:
│   ├── Binaries/, Build/, DerivedDataCache/
│   ├── Intermediate/, Saved/, *.uproject
│   └── Exclude .git/lfs for large binary assets
├── 3. Set up LFS for .uasset, .umap, .wav, .png
└── 4. Create project template in source control
```

## 8.2 Asset Pipeline

### Import Pipeline
```
Asset Import Workflow:
├── 1. Drag assets into Content Browser
│   ├── FBX models: Import mesh + skeleton + animations
│   ├── Textures: Auto-detect sRGB vs linear
│   └── Audio: Import as Sound Wave or Sound Cue
├── 2. Configure import settings
│   ├── Mesh: Import mesh, skeletal mesh, or both
│   ├── Animations: Import as animation sequence
│   └── Materials: Auto-create or use existing
├── 3. Set up LODs (Level of Detail)
│   └── Use "Apply LOD Settings" tool
└── 4. Configure compression (ASTC for mobile, BC for desktop)
```

### Asset Optimization
| Asset Type | Optimization | Tool |
|------------|--------------|------|
| 3D Meshes | Enable Nanite for high-poly | Nanite Settings in Mesh |
| Textures | Use mipmaps, set max size | Texture Editor -> Mip Gen Settings |
| Audio | Compress to Ogg Vorbis | Sound Wave -> Compression |
| Animations | Create Animation Blueprint | Asset Actions -> Create |

### Asset Management
```
Asset Organization:
Content/
├── Audio/          # Sound effects, music
├── Characters/     # Character models, animations
├── Environment/    # Props, architecture, landscapes
├── Materials/      # Material instances, functions
├── Particles/      # Niagara systems
├── UI/             # UMG widgets, fonts
└── Blueprints/     # Blueprint classes
```

## 8.3 Build & Deployment

### Development Build
```
Development Build:
├── 1. Package Settings
│   ├── File -> Package Project -> Development
│   └── Platform selection (Win64, Mac, etc.)
├── 2. Launch Options
│   ├── Play In Editor (PIE)
│   ├── Standalone Game
│   └── Launch on Device (mobile/console)
└── 3. Debugging
    ├── Ctrl+Shift+.: Session Frontend
    └── Enable "Debug Game" builds for breakpoints
```

### Shipping Build
```
Shipping Build Workflow:
├── 1. Project Settings
│   ├── Packaging -> Full Rebuild
│   └── Packaging -> For Distribution: Yes
├── 2. Build Configuration
│   └── File -> Package Project -> Shipping
├── 3. Signing
│   ├── iOS: Configure provisioning profile
│   ├── Android: Configure keystore
│   └── Console: Set up platform SDK
└── 4. Platform-specific packaging
    ├── Windows: .exe + .pak files
    ├── Mobile: .ipa (iOS), .apk (Android)
    └── Console: DevKit/Retail build
```

### Platform Deployment
| Platform | Output | Tool |
|----------|--------|------|
| Windows | .exe + .pak | Direct distribution |
| Mac | .app bundle | Notarize for distribution |
| iOS | .ipa | TestFlight/App Store |
| Android | .aab/.apk | Google Play |
| Console | .pak | Platform SDK |