## § 8 · Standard Workflow

### Phase 1: Spatial Requirements & Platform Selection

```
Input: Business use case, target user, hardware constraints
Output: Platform decision, interaction model spec, performance budget

Steps:
  1.1 Define use case type: training, visualization, collaboration, navigation, gaming
  1.2 Identify target hardware: phone AR, standalone headset, tethered PC VR, passthrough MR
  1.3 Select rendering framework: Unity / Unreal / RealityKit
  1.4 Define performance budget: FPS target, CPU/GPU ms, draw call limit, memory ceiling
  1.5 Choose interaction model: hand tracking, controller, gaze+pinch, voice, hybrid

[✓ Done] Platform decision doc with hardware requirements and performance budget signed off
[✗ FAIL] Missing FPS target → cannot make render architecture decisions; block Phase 2
```

### Phase 2: Spatial Architecture & Content Pipeline

```
Input: Platform decision, performance budget
Output: Scene graph design, asset pipeline, tracking integration spec

Steps:
  2.1 Design scene graph: world anchors, spatial entities, UI volumes, physics layers
  2.2 Set up asset pipeline: USDZ (Apple), glTF 2.0 (Web/Android), FBX (Unity/Unreal)
  2.3 Integrate tracking: ARKit World Tracking, ARCore GeospatialAPI, or OpenXR anchors
  2.4 Set LOD levels: 3 LOD tiers (full / medium
  2.5 Design spatial UI layout: depth, scale, field-of-view placement, hand interaction zones

[✓ Done] Scene architecture diagram + asset pipeline documented; LOD plan approved
[✗ FAIL] No LOD strategy → will exceed draw call budget on standalone hardware; block Phase 3
```

### Phase 3: Implementation & Rendering Optimization

```
Input: Architecture spec, asset pipeline
Output: Working XR application at target frame rate

Steps:
  3.1 Implement core tracking loop: pose updates, anchor management, drift correction
  3.2 Build spatial UI with interaction system: hand rays, gaze dwell, pinch gestures
  3.3 Profile with platform profiler: Xcode Instruments (visionOS), Snapdragon Profiler (Quest),
      Unity Profiler, Chrome DevTools WebXR
  3.4 Optimize: batch static draw calls, enable GPU instancing, compress textures (ASTC/BC7)
  3.5 Implement comfort features: comfort vignette, teleportation, boundary visualization

[✓ Done] Target FPS sustained for 10+ minutes; no motion sickness reports in 5-user comfort test
[✗ FAIL] CPU or GPU over budget → profile and cut features; never ship above frame budget
```

### Phase 4: Multi-User & Deployment

```
Input: Working single-user XR app
Output: Published XR application (App Store / Play Store

Steps:
  4.1 Add shared spatial anchors if multi-user: Apple SharePlay, Photon Fusion, or WebRTC
  4.2 Implement accessibility: alternative input modes, contrast options, text scaling
  4.3 Security review: camera data handling, network traffic encryption, auth for multiplayer
  4.4 Platform certification: Apple App Review, Meta Quest Store review, or WebXR HTTPS deploy
  4.5 Analytics: frame rate telemetry, session length, interaction heatmaps

[✓ Done] App passes platform review; frame telemetry shows p95 FPS ≥ target in production
[✗ FAIL] Platform cert failure → address specific feedback; never push non-compliant build to users
```

---

