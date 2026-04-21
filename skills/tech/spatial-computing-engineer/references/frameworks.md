## § 7 · Standards & Reference

### XR Performance Budgets by Platform

| Platform
|----------------|-----------|-----------|-----------|-----------|----------------|
| Apple Vision Pro | 90 Hz | <4ms | <7ms | <100 | <500K/frame |
| Meta Quest 3 | 72/90 Hz | <6ms | <8ms | <150 | <750K/frame |
| HoloLens 2 | 60 Hz | <8ms | <10ms | <100 | <250K/frame |
| WebXR (mobile) | 60 Hz | <8ms | <12ms | <50 | <100K/frame |
| PC VR (SteamVR) | 90 Hz | <4ms | <6ms | <500 | <2M/frame |

### Comfort Zones & Ergonomics

| Parameter / 参数 | Recommended Range / 推荐范围 | Violation Effect
|-----------------|-----------------------------|-----------------------------|
| UI depth (AR) | 1.2m – 5.0m | Vergence-accommodation conflict → eye strain |
| Angular velocity (VR locomotion) | <30°/s turn speed | Vestibular mismatch → motion sickness |
| Field of view usage | ±30° horizontal, ±20° vertical | Neck strain, missed content |
| Hand tracking confidence threshold | ≥0.8 (ARKit) | Ghost interactions, missed gestures |
| Gaze dwell time | 0.8s – 1.5s | <0.8s = accidental; >1.5s = frustrating |
| Interpupillary distance range | 55mm – 75mm (software IPD) | Incorrect IPD → double vision, headache |

### Industry Frameworks

- **OpenXR (Khronos)** — Cross-vendor XR runtime standard (2019–present); mandatory for multi-platform
- **MRTK 3 (Microsoft)** — Mixed Reality Toolkit for HoloLens 2 + Unity; interaction model reference
- **Apple visionOS HIG** — Human Interface Guidelines for Vision Pro; spatial UI design standard
- **WebXR Device API (W3C)** — Browser XR standard; use Immersive Web Working Group specs
- **Meta Presence Platform** — Spatial anchors, scene understanding, passthrough API for Quest

---
