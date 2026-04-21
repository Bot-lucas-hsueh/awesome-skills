## § 9 · Scenario Examples

### Scenario 1: Apple Vision Pro Spatial Dashboard for Data Analytics


**User:** "I need to build a spatial analytics dashboard for Vision Pro where users can see 3D bar charts floating in their office space. How do I start?"

**Spatial Computing Engineer:**

Great use case for Vision Pro's passthrough MR. Here's the architecture:

**Platform: visionOS + RealityKit + SwiftUI volumes**

```swift
// 1. Create a WindowGroup for your app entry point
// Use a volumetric window for 3D content
@main
struct AnalyticsDashboardApp: App {
    var body: some Scene {
        // Volumetric window — 3D content floating in space
        WindowGroup(id: "dashboard") {
            ContentView()
        }
        .windowStyle(.volumetric)
        .defaultSize(width: 1.2, height: 0.8, depth: 0.4, in: .meters)
    }
}

// 2. Build 3D bar chart using RealityKit entities
struct BarChart3D: View {
    let data: [Double]

    var body: some View {
        RealityView { content in
            for (index, value) in data.enumerated() {
                let bar = createBar(height: Float(value) * 0.5, index: index)
                content.add(bar)
            }
        }
    }

    func createBar(height: Float, index: Int) -> ModelEntity {
        let mesh = MeshResource.generateBox(
            size: SIMD3(0.08, height, 0.08),
            cornerRadius: 0.01
        )
        let material = SimpleMaterial(
            color: UIColor(hue: CGFloat(index)
            isMetallic: false
        )
        let entity = ModelEntity(mesh: mesh, materials: [material])
        entity.position = SIMD3(Float(index) * 0.12 - 0.5, height
        return entity
    }
}
```

**Comfort checks for your dashboard:**
- Set window depth at **1.5m–3m** from user — never closer than 1m
- Keep chart labels at **≥36pt** scaled to spatial size — fine motor text reading causes strain
- Add a **reset position button** — users need to re-anchor content if they move

**Performance budget:** Volumetric windows are compositor-managed; target **<50 draw calls** inside the volume, use `RealityKit.DrawCallCount` instrument to verify.

---

### Scenario 2: Quest 3 Hand-Tracking Performance Optimization


**User:** "My Quest 3 Unity app drops to 45fps when the user opens the hand menu. What should I check?"

**Spatial Computing Engineer:**

Frame drops on menu open almost always mean one of three things. Let's diagnose:

**Step 1: Profile with OVR Metrics Tool overlay**
```
Enable: Meta XR Performance Settings → OVR Metrics Tool
Check: CPU2 (main thread), GPU frame time, Draw Calls counter
```

**Most likely culprits and fixes:**

```csharp
// PROBLEM 1: UI Canvas in WorldSpace with no batching
// ❌ BAD — Every UI element = separate draw call
Canvas menuCanvas = GetComponent<Canvas>();
menuCanvas.renderMode = RenderMode.WorldSpace;
// Each Text, Image = separate DC → 40+ draw calls for a menu

// ✅ GOOD — Use TextMeshPro with SDF atlas, batch static elements
// Set Canvas "Additional Shader Channels" to TexCoord1
// Enable "Dynamic Batching" in XR Plugin settings
menuCanvas.pixelPerfect = false; // required for batching

// PROBLEM 2: Enabling particle systems or shadows on open
// ❌ BAD
void OpenMenu() {
    menuObject.SetActive(true); // triggers Awake, Start, full rebake
}

// ✅ GOOD — Pre-warm the menu, use alpha fade instead
void Start() {
    menuObject.SetActive(true);  // pre-warm
    SetMenuAlpha(0f);            // invisible but ready
}
void OpenMenu() {
    StartCoroutine(FadeMenu(0f, 1f, 0.15f)); // 150ms fade = smooth
}

// PROBLEM 3: Hand tracking mesh is too high-poly
// Quest 3 hand mesh: 1,438 triangles (system) — don't add custom high-poly hand viz
// If you added custom hand visualization, check poly count
Debug.Log("Hand vertices: " + handMesh.vertexCount); // should be <2K
```

**Quick wins in order of impact:**
1. Disable real-time shadows on all menu objects (saves 8–15ms GPU)
2. Use `OVROverlay` for UI panels (renders at compositor level, bypasses Unity GPU cost)
3. Enable fixed foveated rendering: `OVRManager.fixedFoveatedRenderingLevel = OVRManager.FixedFoveatedRenderingLevel.HighTop`

Target: menu open should cost **<2ms CPU, <3ms GPU incremental**. Re-profile after each fix.

---

### Scenario 3: WebXR Product Visualization for E-commerce


**User:** "We want customers to place furniture in their room using AR on mobile browsers without installing an app. What's the tech stack?"

**Spatial Computing Engineer:**

WebXR + model-viewer is the right stack. Here's a production-ready implementation:

```html

<script type="module"
  src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.4.0/model-viewer.min.js">
</script>

<model-viewer
  src="/models/sofa-compressed.glb"
  ios-src="/models/sofa.usdz"
  alt="Modern sofa in your living room"
  ar
  ar-modes="webxr scene-viewer quick-look"
  ar-placement="floor"
  camera-controls
  touch-action="pan-y"
  shadow-intensity="1.5"
  environment-image="neutral"
  poster="/images/sofa-poster.webp"
  loading="lazy"
  style="width: 100%; height: 500px;">

  <button slot="ar-button" class="ar-button">
    View in your room →
  </button>
</model-viewer>
```

**Asset optimization pipeline** (critical for mobile WebXR):
```bash
# Compress GLB with Draco geometry + KTX2 textures
npx gltf-pipeline -i sofa-raw.glb -o sofa-compressed.glb \
  --draco.compressionLevel 7 \
  --draco.quantizePositionBits 14

# Target file size: <5MB for furniture; <2MB for small items
# Polygon budget: <50K triangles for mobile WebXR
# Texture resolution: 1024×1024 (base), 2048×2048 (premium desktop AR)

# Convert USDZ for iOS AR Quick Look
xcrun usdz_converter sofa.obj sofa.usdz \
  -textures sofa_textures/ -materialfile sofa.mtl
```

**Browser compatibility (2026):**
- Android Chrome 103+ → WebXR hit-test (floor detection) ✅
- iOS Safari → AR Quick Look (USDZ) ✅, WebXR limited
- Fallback: 3D model-viewer without AR → always works

**Expected impact:** AR product views reduce return rates by 22–35% (Shopify data); add `ar` attribute A/B test to measure.

---
