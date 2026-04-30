# Unitree Competition Guide

## World Humanoid Robot Games 2025

### Overview
The inaugural World Humanoid Robot Games were held in Beijing in August 2025, featuring 280 teams from 16 countries competing in 26 sports events. Unitree dominated the competition.

### Unitree Performance

| Medal | Count | Events |
|-------|-------|--------|
| 🥇 Gold | 4 | 400m dash, 1500m race, 100m hurdles, 4×100m relay |
| 🥈 Silver | — | Multiple events |
| 🥉 Bronze | — | Multiple events |
| **Total** | **11** | Top of medal table |

### Competition Events

#### Track Events (Unitree H1)

| Event | H1 Performance | Notes |
|-------|---------------|-------|
| 400m Dash | 1:28 | Gold medal, world record |
| 1500m Race | 6:34:40 | Gold medal, world record |
| 100m Hurdles | — | Gold medal |
| 4×100m Relay | — | Gold medal (team event) |

**Performance Analysis:**
- Speed: 4.78 m/s logged during competition
- Internal tests have exceeded 5 m/s
- Limiting factor: Battery life for endurance events

#### Other Events

- **Group Dance**: 9 H1 robots in 3D-printed terracotta warrior armor — 92 points, 1st place
- **Kickboxing**: Demonstration of balance and defensive maneuvers
- **Football/Soccer**: Team coordination and ball control
- **Gymnastics**: Balance and flexibility demonstrations

### G1 in Competition

Independent teams using G1 platform also performed well:
- 1 Gold medal
- 1 Silver medal  
- 1 Bronze medal

This demonstrates the versatility and capability of the G1 platform for competition use.

---

## RoboCup Humanoid League

### Overview
RoboCup is the premier international robotics competition, with the Humanoid League specifically for bipedal robots.

### G1-Comp Configuration

Unitree offers a G1-Comp package specifically for RoboCup competition:

| Feature | Specification |
|---------|--------------|
| DOF | 25-45 (competition optimized) |
| Height | ~130 cm |
| Weight | ~35 kg |
| Battery Life | ~2 hours |
| Special Features | Enhanced balance, kick optimization |

### Competition Categories

1. **Soccer** — Team coordination, ball handling, goal scoring
2. **Technical Challenges** — Balance, walking, obstacle avoidance
3. **Drop-In Games** — Ad-hoc team formation

### Training Recommendations

```
ROBOCUP PREPARATION (3-6 months):

Month 1: Hardware Setup
├── Firmware update to latest version
├── Joint calibration and backlash compensation
├── G1-Comp configuration if available
└── Footwear selection (grip optimization)

Month 2: Basic Locomotion
├── Walking stability optimization
├── Running gait development
├── Direction change quickness
└── Fall recovery training

Month 3: Soccer Skills
├── Ball detection and tracking
├── Kicking mechanics (power vs accuracy)
├── Dribbling control
└── Passing coordination

Month 4: Team Coordination
├── Multi-robot communication
├── Position assignment algorithms
├── Dynamic role switching
└── Formation maintenance

Month 5: Game Strategy
├── Opponent behavior prediction
├── Adaptive positioning
├── Set-piece strategies
└── Time management (battery)

Month 6: Competition Prep
├── Rule compliance verification
├── Referee signal recognition
├── Stress testing (full games)
└── Backup robot preparation
```

---

## Training Methodology

### Gait Optimization for Competition

```python
# Competition gait parameters
COMPETITION_GAIT = {
    # Sprint optimization
    'stance_duration': 0.25,      # Short for quick steps
    'swing_height': 0.08,         # Lower for speed
    'step_length': 0.4,           # Maximize stride
    'body_height': 0.6,           # Slightly lower for stability
    
    # PD gains (tuned for responsiveness)
    'kp': 80.0,                   # Higher for tracking
    'kd': 2.0,                    # Damping for stability
    
    # Terrain adaptation
    'adaptive_foot_placement': True,
    'compliance_control': True,
}
```

### Speed Optimization

1. **Motor Tuning**
   - Maximize torque output within thermal limits
   - Monitor temperature continuously
   - Implement dynamic current limiting

2. **Gait Policy Training**
   - Focus on forward velocity reward
   - Minimize vertical COM oscillation
   - Optimize swing foot trajectory

3. **Hardware Preparation**
   - Lightweight battery packs for sprint events
   - Rubber foot pads for track grip
   - Aerodynamic considerations

### Endurance Optimization

1. **Energy Management**
   - Efficient gait selection (trot vs bound)
   - Regenerative braking where possible
   - Battery swap strategy for long events

2. **Thermal Management**
   - Pre-cooling before events
   - Airflow optimization
   - Duty cycle management

---

## Competition Day Checklist

### Pre-Event (Day Before)

- [ ] Full system diagnostic
- [ ] Joint calibration verification
- [ ] Battery charge to 100% (multiple spares)
- [ ] Firmware version check
- [ ] Backup configuration saved
- [ ] Tool kit prepared
- [ ] Spare parts (fuses, connectors, etc.)

### Pre-Run (30 minutes before)

- [ ] Battery at 80%+ charge
- [ ] Joint temperature check (<40°C)
- [ ] Communication test
- [ ] Emergency stop verification
- [ ] Warm-up sequence executed
- [ ] Operator briefed on course

### Post-Run

- [ ] Cool-down period (allow joints to cool)
- [ ] Visual inspection for damage
- [ ] Log data download
- [ ] Battery charging
- [ ] Notes for optimization

---

## Common Issues & Solutions

### Performance Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| Slow acceleration | Gait policy too conservative | Increase velocity tracking reward |
| Overheating | Sustained high torque | Implement thermal throttling |
| Unstable at speed | Insufficient damping | Increase derivative gains |
| Falls on turns | COM management | Improve turning gait policy |

### Competition-Specific Challenges

| Challenge | Mitigation |
|-----------|------------|
| Unfamiliar surfaces | Train on varied terrains; bring test mats |
| Crowd interference | Robust perception; ignore distractions |
| Time pressure | Practice under timed conditions |
| Adversarial opponents | Defensive behaviors; collision avoidance |

---

## Key Success Factors

Based on 2025 World Humanoid Robot Games results:

1. **Mechanical Design**
   - M107 motor performance critical
   - Torque density enables dynamic moves
   - Lightweight structure for agility

2. **Control Software**
   - Well-tuned gait policies
   - Fast response to disturbances
   - Robust fall recovery

3. **Operator Skill**
   - Teleoperation for complex events
   - Quick decision making
   - Emergency response training

4. **Preparation**
   - Extensive real-world testing
   - Backup systems ready
   - Team coordination practiced

---

## Future Competitions

### Anticipated Events 2026+

- **DARPA Robotics Challenge** (potential revival)
- **Amazon Robotics Challenge**
- **World Robot Olympiad**
- **China Robotics Competition**

### Trends

- Increasing autonomy (less teleoperation)
- More complex manipulation tasks
- Team coordination emphasis
- Real-world application scenarios

---

*Last Updated: 2026-03-21*
