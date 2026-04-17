## § 4 · Core Philosophy

### Mental Model: The Spatial Computing Stack

```
┌─────────────────────────────────────────────────────┐
│           HUMAN PERCEPTION LAYER                    │
│   Comfort  ·  Presence  ·  Ergonomics  ·  Safety   │
├─────────────────────────────────────────────────────┤
│           SPATIAL UI
│   3D Layout  ·  Gaze  ·  Hand Tracking  ·  Voice   │
├─────────────────────────────────────────────────────┤
│           APPLICATION LOGIC LAYER                   │
│   Scene Graph  ·  Physics  ·  State Management      │
├─────────────────────────────────────────────────────┤
│           TRACKING & SENSING LAYER                  │
│   SLAM  ·  LiDAR  ·  IMU  ·  Depth Camera  ·  GPS  │
├─────────────────────────────────────────────────────┤
│           RENDERING LAYER                           │
│   Metal / Vulkan / WebGL
├─────────────────────────────────────────────────────┤
│           HARDWARE LAYER                            │
│   Vision Pro · Quest 3 · HoloLens 2 · Phone AR     │
└─────────────────────────────────────────────────────┘
```

### Guiding Principles

1. **Frame Budget is Sacred** — Every feature costs frame time. If it doesn't fit in the render budget, it doesn't ship. Profile before committing to architecture.

2. **Spatial Comfort Over Aesthetics** — A beautiful UI that causes motion sickness or eye strain fails its users. Comfort constraints (depth, angular velocity, field-of-view) override visual design preferences.

3. **Graceful Degradation Across Hardware** — XR hardware spans $300 phones to $3500 headsets. Build for the lowest capable device with progressive enhancement for premium hardware.

---

