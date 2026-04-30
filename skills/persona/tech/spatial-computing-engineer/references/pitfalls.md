## § 10 · Common Pitfalls

### Pitfall 1: Static Batching Broken by Runtime Instantiation


❌ **BAD**
```csharp
// Instantiate at runtime → Unity cannot static batch
GameObject obj = Instantiate(prefab, position, rotation);
obj.isStatic = true; // too late! Static flag ignored after runtime instantiation
```

✅ **GOOD**
```csharp
// Use GPU Instancing for repeated objects
// Assign Material with GPU Instancing enabled
// → 1 draw call for 1000 identical objects
material.enableInstancing = true;
Graphics.DrawMeshInstanced(mesh, 0, material, matrices);
```

**Why it matters:** Each un-batched draw call on Quest 3 costs ~0.5ms GPU; 50 extra calls = 25ms overhead = drop from 90Hz to 40Hz.

---

### Pitfall 2: UI Depth Inside 1 Meter


❌ **BAD**
```swift
// Placing UI 0.5m from camera — common mistake for "large" appearance
entity.position = SIMD3(0, 0, -0.5)
```

✅ **GOOD**
```swift
// Minimum 1.2m; 2m ideal for sustained reading comfort
entity.position = SIMD3(0, 0, -2.0)
// Scale up instead of moving closer: text size should be ~1.2° visual angle minimum
let scaledSize: Float = 2.0 * tan(1.2 * .pi / 180) // ~0.042m = 4.2cm text height at 2m
```

**Why it matters:** Vergence-accommodation conflict at <1m causes eye strain within 5–10 minutes; users abandon the app, not the hardware.

---

### Pitfall 3: Not Handling Tracking Loss


❌ **BAD**
```swift
// No tracking state check → AR content teleports on tracking loss
session.run(configuration)
// ... directly render without checking trackingState
```

✅ **GOOD**
```swift
func session(_ session: ARSession, cameraDidChangeTrackingState camera: ARCamera) {
    switch camera.trackingState {
    case .normal:
        hideTrackingLostUI()
    case .limited(let reason):
        showTrackingLostUI(reason: "\(reason)") // tell user: move to brighter area
    case .notAvailable:
        pauseARContent() // don't render stale anchors
    }
}
```

**Why it matters:** Un-handled tracking loss causes AR content to jump erratically — severe enough to cause motion sickness in VR contexts.

---

### Pitfall 4: World-Space UI Text Too Small


❌ **BAD:** UI text scaled to match physical size expectations (e.g., 12pt at 0.3m = looks right but causes squinting)

✅ **GOOD:** Calculate minimum visual angle: text height = `distance × tan(1.2°)`. At 2m depth, minimum text height = **4.2cm in world units**. Use `TextMeshPro` with SDF rendering — never raster text in world space.

**Why it matters:** Users tilt or move toward illegible text, breaking immersion and causing neck strain.

---

### Pitfall 5: Missing Comfort Vignette in Artificial Locomotion


❌ **BAD:** Smooth joystick locomotion with full field of view → induces motion sickness in ~60% of users

✅ **GOOD:**
```csharp
// Apply comfort vignette when moving
void Update() {
    float speed = locomotionProvider.currentMoveSpeed;
    float vignetteStrength = Mathf.Lerp(0, 0.7f, speed
    comfortVignette.SetStrength(vignetteStrength); // OVR Comfort Vignette component
}
```

**Why it matters:** Peripheral vision suppression during artificial movement reduces vestibular mismatch; reduces sickness reports by ~50% in studies.

---

### Pitfall 6: Ignoring Accessibility in XR


❌ **BAD:** Hand-tracking only interaction — excludes users with motor disabilities, in cold environments (hand tracking degrades in <10°C), or wearing gloves

✅ **GOOD:** Always implement at minimum two input modalities: hand tracking + gaze+dwell, or hand tracking + voice command. Follow visionOS Accessibility API guidelines.

**Why it matters:** ~15% of users have some form of motor disability; XR platforms legally require accessibility compliance in EU/US markets.

---

## § 11 · Integration with Other Skills

### Integration 1: Spatial Computing + AI/ML Engineer


**Workflow:** On-device AI (Core ML

- Use `ARKit` Scene Geometry + `Vision` framework for real-time object classification in camera feed
- Run depth estimation models (MiDaS, DepthPro) locally for markerless occlusion without LiDAR
- Outcome: AR content realistically occludes behind detected furniture without LiDAR hardware

### Integration 2: Spatial Computing + Backend Developer


**Workflow:** Persistent world anchors backed by cloud spatial anchor services.

- Azure Spatial Anchors
- Backend stores anchor IDs with metadata; spatial computing client resolves anchors on session start
- Outcome: Multi-user AR where content placed by one user persists for all users across days

### Integration 3: Spatial Computing + UX Designer


**Workflow:** Spatial UI design system with 3D component library.

- Designer provides spatial layout specs in Figma with depth layer annotations
- Engineer implements in RealityKit
- Shared vocabulary: viewing distance, billboard vs world-space, field-of-view percentage
- Outcome: Spatial UI that passes comfort review first try, not after 3 rounds of sickness reports

---

## § 12 · Scope & Limitations

### Use When

- Building AR apps for iPhone, iPad, Android phones, or head-mounted displays (Vision Pro, Quest, HoloLens)
- Designing spatial UI for mixed reality business applications (manufacturing, medical, training)
- Optimizing XR application performance for standalone headsets with fixed GPU budgets
- Prototyping WebXR experiences accessible via browser without app installation
- Integrating LiDAR/depth sensors for environment reconstruction or measurement AR tools

### Do NOT Use When

- Designing 2D flat-screen UI (use UX Designer skill instead — spatial principles don't transfer)
- Building game engines from scratch (spatial computing builds on engines; use graphics/engine engineers)
- Hardware manufacturing or optics design for headsets (this is software/SDK-level expertise)
- Enterprise infrastructure or backend services unrelated to XR (use Backend Developer skill)
- Regulatory certification of medical AR devices (FDA SaMD requires dedicated regulatory specialists)

### Alternatives

- **Game development without XR**: Use Unity or Unreal Engineer skills focused on 2D/flat-screen
- **3D visualization (non-interactive)**: Use Blender + three.js without XR interaction layer
- **Computer Vision (non-XR)**: Use AI/ML Engineer skill for OpenCV, image classification pipelines

---

## § 13 · How to Use This Skill

### Quick Install

```
Read https://theneoai.github.io/awesome-skills/skills/tech/spatial-computing-engineer/SKILL.md and install
```

### Trigger Words

| English | 中文 |
|---------|------|
| "spatial computing engineer" | "空间计算工程师" |
| "AR development" / "VR app" / "XR engineer" | "AR开发" / "VR应用"
| "Apple Vision Pro" / "visionOS" | "苹果Vision Pro"
| "ARKit" / "ARCore" / "WebXR" | "ARKit集成"
| "SLAM" / "point cloud" / "LiDAR AR" | "SLAM算法"
| "3D rendering" / "render optimization" | "3D渲染"
| "hand tracking" / "spatial UI" | "手势追踪"

---

## § 14 · Quality Verification

### Self-Checklist

```
[✓] Specified target platform and correct SDK (ARKit/ARCore/WebXR/OpenXR)
[✓] Provided FPS target and draw call budget before implementation
[✓] Checked UI depth is ≥1.2m (AR) or comfort zone compliant (VR)
[✓] Verified tracking state handling (loss / limited
[✓] Included profiler step before optimization recommendation
[✓] Provided at least 2 input modalities (accessibility)
[✓] Cited specific API names, SDK versions, hardware specs
[✓] Included comfort risk for any locomotion or camera motion
```

### Test Cases

**Test 1:** "How do I place a virtual object on a real table with ARKit?"
- Expected: ARKit WorldTracking + plane detection → raycast to ARPlaneAnchor → AnchorEntity placement in RealityKit

**Test 2:** "My Quest 3 app renders at 45fps, how do I fix it?"
- Expected: Systematic profiler approach → identify CPU/GPU bottleneck → specific fixes (batching, instancing, LOD, shadow disable)

**Test 3:** "Build a WebAR experience for product try-on that works on iPhone Safari"
- Expected: model-viewer + USDZ for iOS AR Quick Look, GLB + WebXR for Android, <5MB asset budget, accessibility fallback

---

## § 15 · Version History

| Version / 版本 | Date / 日期 | Changes
|----------------|-------------|-------------------|
| 3.0.0 | 2026-03-04 | Full 16-section rewrite to 9.5/10 Exemplary standard; added visionOS/Android XR coverage, performance budgets, 3 scenario examples, 6 pitfalls, comfort metrics |
| 2.0.0 | 2026-02-16 | Added ARKit/ARCore/WebXR toolkit, SLAM integration guidance |
| 1.0.0 | 2026-02-16 | Initial release with basic XR framework overview |

---

## § 16 · License & Author

| Field / 字段 | Value
|-------------|-----------|
| **License** | MIT with Attribution |
| **Author** | neo.ai |
| **Repository** | [theneoai/awesome-skills](https://github.com/theneoai/awesome-skills) |
| **Skill URL** | `https://theneoai.github.io/awesome-skills/skills/tech/spatial-computing-engineer/SKILL.md` |
| **Category** | tech |
| **Verified By** | Expert Review — 2026-03-04 |

```
MIT License — Copyright (c) 2026 neo.ai
Permission is hereby granted, free of charge, to any person obtaining a copy of this skill
to use, copy, modify, and distribute, subject to the condition that attribution is preserved.
```
