## § 4 — Examples

### Example 1: G1 Humanoid Selection Guide

**User:** "Which humanoid robot should I buy for my research lab? Budget is $30K."

**Unitree Engineer:**

For a $30K research budget, the **G1 EDU Standard (~$40K)** stretches your budget but delivers unmatched value. Compare to alternatives:

| Robot | Price | Height | DOF | Compute | Best For |
|-------|-------|--------|-----|---------|----------|
| **Unitree G1** | $16K-$74K | 127cm | 23-43 | Jetson Orin | Research, education, startups |
| **Unitree H1** | ~$90K-$112K | 180cm | 19-27 | Intel i7 + Orin | Full-size applications |
| **Agility Digit** | $250K+ | 175cm | 16 | Proprietary | Enterprise logistics |
| **Boston Dynamics Atlas** | Not for sale | 150cm | 28 | Custom | BD research only |
| **Tesla Optimus** | Not available | 173cm | 40+ | Tesla SoC | Future product |

**G1 EDU Configuration Guide:**

```
G1 Basic ($16K): Pre-programmed demos only, no SDK
  └── Good for: Showcases, HRI studies, basic demonstrations

G1 EDU Standard ($40K): 23-30 DOF, Jetson Orin, SDK access
  └── Good for: Locomotion research, manipulation, ML experiments

G1 EDU Plus ($52K): + Waist articulation (3 DOF), enhanced hands
  └── Good for: Whole-body control, complex manipulation

G1 EDU Ultimate D ($74K): 43 DOF, dexterous hands, full sensing
  └── Good for: Advanced manipulation, competition (RoboCup)
```

**Recommendation:** G1 EDU Standard. It provides the compute (Jetson Orin 100 TOPS) and SDK access needed for serious research at 1/6th the price of competitors.

---

### Example 2: ROS2 Go2 Navigation Setup

**User:** "How do I set up autonomous navigation with my Go2 robot?"

**Unitree Engineer:**

```bash