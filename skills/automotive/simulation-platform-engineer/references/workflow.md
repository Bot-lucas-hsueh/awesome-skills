# AV Simulation — Troubleshooting

## Sensor Simulation Issues

### LiDAR Point Cloud Density Too Low vs. Real Data

**Symptom:** Simulated point cloud has noticeably fewer points than real LiDAR data (e.g., 80% of expected density). Perception model performance degrades on synthetic data.

**Diagnosis:**
```bash
# Count points per frame
python3 -c "
import open3d as o3d
pcd = o3d.io.read_point_cloud('sim_lidar.pcd')
print(f'Point count: {len(pcd.points)}')

# Compare with expected density from real sensor spec
# For a 128-beam LiDAR at 10Hz, expect ~1.3M points/sec
# Per frame at 10Hz: ~130,000 points for a 128-channel sensor
"

# Compute point density by range
python3 -c "
import numpy as np
pc = np.load('sim_lidar.npy')
ranges = np.linalg.norm(pc[:,:3], axis=1)
# Bin by range and count
for r_min, r_max in [(0,20), (20,50), (50,100)]:
    mask = (ranges >= r_min) & (ranges < r_max)
    print(f'{r_min}-{r_max}m: {mask.sum()} points')
"
```

**Common causes and fixes:**

| Cause | Fix |
|-------|-----|
| Beam count too low | Increase `channels` attribute (e.g., 32→128) |
| Rotation frequency mismatch | Set `rotation_frequency` to match real sensor (e.g., 10Hz, 20Hz) |
| Atmospheric attenuation not modeled | Implement range-dependent point dropout |
| Lidar position too low | Adjust z-offset to match real sensor mount height |
| Vehicle occlusion by self-body | Disable self-intersection or mount LiDAR above vehicle roof |

**Fidelity validation:**
```bash
# Compare point density RMSE across range bins
python3 compare_lidar.py \
  --sim sim_lidar.npy \
  --real nuScenes_lidar.npy \
  --bins 10 20 50 100

# Target: <5% point density deviation per bin
```

### Camera Rendering Artifacts (Unreal Engine)

**Symptom:** Camera images show artifacts: lens distortion mismatch, incorrect HDR/tone-mapping, motion blur absence, or specular highlights that don't match real camera.

**Fix:**
```python
# Configure CARLA camera with realistic ISP pipeline
camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')
camera_bp.set_attribute('image_size_x', '1920')
camera_bp.set_attribute('image_size_y', '1080')
camera_bp.set_attribute('fov', '90')  # Horizontal FOV

# Enable chromatic aberration for realism
camera_bp.set_attribute('chromatic_aberration_intensity', '0.5')
camera_bp.set_attribute('chromatic_aberration_offset', '0.003')

# Motion blur — needs simulation timestep matching real shutter speed
# Shutter speed 1/120s → delta_seconds should be ≤0.0083s per frame
world.tick(delta_seconds=0.0083)
```

**HDR mismatch fix:**
```python
# Real cameras capture HDR; tonemapping is a major sim-to-real gap source
# Use ACES tonemapping in Unreal Engine settings
# Or apply histogram equalization post-processing for domain adaptation

import cv2
def apply_histogram_adaptation(sim_img, real_ref_img):
    sim_yuv = cv2.cvtColor(sim_img, cv2.COLOR_RGB2YUV)
    sim_yuv[:,:,0] = cv2.equalizeHist(sim_yuv[:,:,0])
    return cv2.cvtColor(sim_yuv, cv2.COLOR_YUV2RGB)
```

### Radar Multipath and Clutter

**Symptom:** Simulated radar shows too clean returns — no multipath ghosts, no ground bounce, no clutter from guardrails.

**Fix:**
```python
# Add multipath simulation for realistic radar
radar_bp = world.get_blueprint_library().find('sensor.radar.true_positive')
# Range resolution: 0.25m, azimuth FOV: 35°, range max: 100m
radar_bp.set_attribute('range_max', '100')
radar_bp.set_attribute('noise_altitude_blindspot', '0.5')  # Ground bounce
radar_bp.set_attribute('noise_clutter_standard_deviation', '0.1')

# For infrastructure radar: simulate multipath from overpasses
# Track: 4+ distinct propagation paths per object
# Real: RCS values vary ±3dB due to aspect angle
```

## OpenSCENARIO / OpenDRIVE Issues

### OpenSCENARIO 2.0 DSL Parse Failures

**Symptom:** `ValueError: Failed to parse OpenSCENARIO 2.0 XML` or scenario runner fails to load scenario.

**Diagnosis:**
```bash
# Validate OpenSCENARIO XML schema
xmllint --schema OpenSCENARIO_v2.0.xsd scenario.xosc --noout

# Check version declaration
head -5 scenario.xosc
# Must be: <?xml version="1.0" encoding="UTF-8"?>
# And root element: <OpenScenario>
```

**Common fixes:**
```xml
<!-- WRONG: Missing namespace or wrong schema version -->
<OpenScenario xmlns="http://xsd.audi.cn/OSI1">
  <FileHeader version="1.0"/>
</OpenScenario>

<!-- CORRECT: OpenSCENARIO 2.0 -->
<?xml version="1.0" encoding="UTF-8"?>
<OpenScenario xmlns="http://psi.hq.audi/IS/2023/08/OpenSCENARIO2">
  <FileHeader version="2.0.0"/>
</OpenScenario>

<!-- WRONG: Invalid action in Maneuver -->
<Private entityRef="ego">
  <Maneuver name="cut_in">
    <Action name="lane_change">
      <Distance value="50"/>  <!-- Not valid for LaneChangeAction -->
    </Action>
  </Maneuver>
</Private>

<!-- CORRECT: LaneChangeAction with RoutingAction -->
<Private entityRef="ego">
  <Maneuver name="cut_in">
    <Actions>
      <RoutingAction>
        <LaneChangeAction laneOffset="1" targetLane="2">
          <Transition dynamics="linear" value="1.0"/>
        </LaneChangeAction>
      </RoutingAction>
    </Actions>
  </Maneuver>
</Private>
```

### OpenDRIVE Map Not Loading in CARLA

**Symptom:** CARLA fails to import OpenDRIVE file with "Failed to parse road network" or empty world.

**Fix:**
```bash
# Validate OpenDRIVE schema
xmllint --schema OpenDRIVE_v1.7.xsd map.xodr --noout

# Check common issues
python3 validate_opendrive.py map.xodr

# Typical issues:
# 1. Missing <planView> with <geometry>
# 2. Invalid lane linkage (successor/predecessor mismatch)
# 3. Non-numeric elevation profile values
```

**Common fixes:**
```xml
<!-- WRONG: Missing planView geometry -->
<road name="road1" length="100">
  <!-- Missing <link> and <planView> -->
</road>

<!-- CORRECT -->
<road name="road1" length="100">
  <link>
    <predecessor elementType="road" elementId="0"/>
  </link>
  <planView>
    <geometry s="0" x="0" h="0" length="100">
      <line/>
    </geometry>
  </planView>
  <lanes>
    <laneSection s="0">
      <left><lane id="1" type="driving"><link><predecessor id="1"/></link></lane></left>
      <center><lane id="0" type="driving"/></center>
      <right><lane id="-1" type="driving"><link><predecessor id="-1"/></link></lane></right>
    </laneSection>
  </lanes>
</road>
```

### SUMO-CoSimulation Lane ID Mismatch

**Symptom:** Vehicles in SUMO don't match positions in CARLA. Ego vehicle in CARLA has wrong lane assignment.

**Fix:**
```python
# SUMO Traci API — sync lane IDs
import traci

# Get SUMO lane ID for CARLA waypoint
sumo_lane_id = traci.vehicle.getLaneID(veh_id='car1')
# Format: "road1_0" (roadID_laneIndex)

# Map to CARLA lane
carla_lane_id = sumo_lane_id.split('_')[1]  # Extract lane index

# Set CARLA vehicle to matching lane
carla_vehicle.set_velocity(...)
```

## CI/CD Pipeline Issues

### Nightly Regression Taking > 24 Hours

**Symptom:** The 500-scenario regression suite runs for 28+ hours, blocking the morning deployment.

**Diagnosis:**
```bash
# Measure per-scenario execution time
python3 benchmark_scenarios.py --suite regression --output timing.json

# Find the slowest 10% of scenarios
jq '[.scenarios | sort_by(.duration) | .[-50:]]' timing.json
```

**Common causes and fixes:**

| Cause | Fix |
|-------|-----|
| Full CARLA render for behavioral tests | Use SUMO co-simulation for NPC-only scenarios (10x faster) |
| Insufficient parallelization | Scale Kubernetes pods; use Gantry scheduling |
| GPU starvation | Allocate dedicated GPU nodes; max 2 CARLA instances per GPU |
| Data upload bottleneck | Stream sensor data to S3 asynchronously; don't block on upload |
| Overly long scenario timeouts | Set per-scenario timeout based on complexity tier |

**Optimization pipeline:**
```yaml
# kubernetes-carla-scaler.yaml
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: 20  # 20 parallel CARLA pods
  template:
    spec:
      containers:
      - name: carla
        image: carla/carla:0.9.15
        resources:
          limits:
            nvidia.com/gpu: 0.5  # 2 instances per GPU
            memory: "16Gi"
        args: ["/bin/bash", "-c",
               "./CarlaUE4.sh -RenderOffScreen -fps=20"]
---
# Behavioral scenarios: headless SUMO, no GPU
# Perception scenarios: CARLA + GPU, 1 per GPU
# Scale behavioral pods to 50, perception to 10
```

### Non-Deterministic Scenario Failures

**Symptom:** A scenario fails in nightly CI but passes when re-run locally with the same scenario file.

**Diagnosis:**
```bash
# Check if seed was logged
cat scenario_results/failed_run/manifest.json | jq '.seed'

# Re-run with explicit seed
python3 run_scenario.py \
  --scenario URB_INT_001 \
  --seed 42 \
  --simulator-version 0.9.15

# Compare NPC behavior
diff <(jq '.npc_trajectories' run_a.json) \
     <(jq '.npc_trajectories' run_b.json)
```

**Fix:**
```python
# Always set deterministic NPC behavior
traffic_manager = world.get_traffic_manager(8000)
traffic_manager.set_global_distance_to_leading_vehicle(2.0)

# Set random seed for reproducible NPC behavior
traffic_manager.random_seed = 42

# For scenario actors, set fixed initial positions
actor.set_transform(carla.Transform(
    carla.Location(x=100, y=-3, z=0.1),
    carla.Rotation(pitch=0, yaw=180, roll=0)
))
```

**Non-reproducibility checklist:**
- [ ] Simulator version logged in every run manifest
- [ ] RNG seed set and recorded
- [ ] NPC behavior seed fixed
- [ ] Weather parameters fixed (not random)
- [ ] Delta time step fixed (not variable)
- [ ] GPU driver version pinned

### CARLA Server Crash During Regression

**Symptom:** CARLA server dies mid-scenario. Results in partial runs and no data for failed scenario.

**Fix:**
```python
# Implement watchdog for CARLA process
import subprocess
import time

def run_scenario_with_watchdog(scenario_file, timeout=600):
    proc = subprocess.Popen(['./CarlaUE4.sh', '-RenderOffScreen'])
    try:
        result = run_scenario(scenario_file, timeout=timeout)
    except TimeoutError:
        # Kill and restart CARLA
        proc.terminate()
        proc.wait()
        raise
    finally:
        proc.terminate()
        proc.wait()

# Archive crash dump
    if proc.returncode != 0:
        save_crash_dump(proc.pid, scenario_file)
        raise RuntimeError(f"CARLA crashed during {scenario_file}")
```

**Recovery strategy:**
```bash
#!/bin/bash
# carla-restart.sh — restart crashed CARLA instances
for pod in $(kubectl get pods -l app=carla | grep CrashLoopBackOff | awk '{print $1}'); do
  kubectl delete pod $pod
done
# Kubernetes will restart pods with CrashLoopBackOff status
```

## Sim-to-Real Gap Issues

### Perception Model Generalizes Poorly from Sim to Real

**Symptom:** Model trained on synthetic data has 10-15% lower mAP on real nuScenes/ Waymo validation set.

**Systematic diagnostic:**
```python
# Step 1: Isolate which modality has the gap
# Run ablation: test with each sensor modality separately
test_lidar_only = perception_model.predict(lidar_only=True)
test_camera_only = perception_model.predict(camera_only=True)
test_fusion = perception_model.predict(fusion=True)

# If gap disappears with LiDAR-only: camera rendering is the issue
# If gap persists: point cloud density or map encoding mismatch

# Step 2: Compute per-class AP delta
for cls in ['car', 'pedestrian', 'cyclist']:
    sim_ap = compute_ap(synthetic_results, class=cls)
    real_ap = compute_ap(real_results, class=cls)
    delta[cls] = real_ap - sim_ap
    print(f"{cls}: sim={sim_ap:.3f} real={real_ap:.3f} gap={delta[cls]:.3f}")

# Typically: cyclist has largest gap (thin profile, high variance)
```

**Gap closing strategies:**
```python
# Strategy 1: Domain Randomization
# Randomize lighting, texture, weather in sim to force robust features
def randomize_domain(world):
    world.set_weather(carla.WeatherParameters(
        cloudiness=np.random.uniform(0, 100),
        precipitation=np.random.uniform(0, 50),
        sun_altitude_angle=np.random.uniform(10, 80)
    ))

# Strategy 2: Realistic Texture Augmentation
# Replace procedural textures with photorealistic PBR materials

# Strategy 3: Domain Adaptation (GAN)
# Train CycleGAN to translate sim images to real style
# Apply before feeding to perception model

# Strategy 4: Domain Gap Metric Tracking
# Compute FID score between sim and real image distributions
# Track FID across iterations; target FID < 15
```

### Ego Pose Drift in Log Replay

**Symptom:** When replaying real-world logs through the AV stack in simulation, the ego vehicle diverges from the ground truth trajectory within seconds.

**Fix:**
```python
# Use closed-loop replay with perception-in-the-loop
# Instead of open-loop trajectory injection, use Waymo Open Dataset logs
# with the sensor data fed through the actual perception stack

# If open-loop is required, tune PID controller for trajectory tracking
from CarlaPIDController import PIDLongitudinalController

longitudinal_controller = PIDLongitudinalController(K_P=1.0, K_I=0.1, K_D=0.05)
lateral_controller = PIDLateralController()  # Stanley controller

def closed_loop_step(current_pose, target_pose, dt):
    v_error = target_pose.speed - current_pose.speed
    throttle = longitudinal_controller.run_step(v_error, dt)
    steer = lateral_controller.run_step(current_pose, target_pose)
    return throttle, steer
```

## Scenario Authoring Issues

### Scenario Library Coverage Gaps

**Symptom:** SCI dashboard shows <85% coverage. Certain ODD parameters have no test scenarios.

**Fix:**
```python
# Use Scenic to generate missing scenarios
from scenic import Simulator

simulator = Simulator(
    backend='carla',
    carla_host='localhost',
    carla_port=2000
)

# Define scenario space with parameter ranges
scenario = simulator.generate(
    scenario_model=cut_in_scenario,
    params={
        'ego_speed': (25, 33, 5),     # min, max, steps
        'npc_speed': (20, 40, 5),
        'weather': ['clear', 'rain_light', 'rain_heavy'],
        'time_of_day': ['day', 'night', 'dusk']
    },
    max_scenarios=500,
    verbosity=2
)

# Generate coverage report
sci = simulator.compute_scenario_coverage_index(
    ocd_params=['ego_speed', 'npc_speed', 'weather', 'time_of_day'],
    executed_scenarios=scenario_results
)
print(f"SCI: {sci:.1%}")  # Target: >85%
```

### Scenario Execution Timeout

**Symptom:** Scenario hangs at 300 seconds, blocking CI pipeline.

**Fix:**
```python
# Set per-scenario timeout based on type
TIMEOUTS = {
    'behavioral': 60,    # NPC logic only
    'perception': 300,   # Sensor capture and inference
    'planning': 180,     # End-to-end planning
    'critical': 600      # Extended edge cases
}

def execute_scenario(scenario_file, scenario_type='behavioral'):
    timeout = TIMEOUTS[scenario_type]
    try:
        result = run_with_timeout(scenario_file, timeout=timeout)
        return result
    except TimeoutError:
        # Log failure but don't block pipeline
        save_partial_results(scenario_file, partial_trace)
        mark_scenario_timeout(scenario_file)
        return {'status': 'timeout', 'timeout': timeout}
```

## Map Authoring Issues

### Junction Geometry Causing Unrealistic NPC Behavior

**Symptom:** SUMO or CARLA NPCs slow down unexpectedly at junctions or fail to complete turns.

**Fix:**
```xml
<!-- In OpenDRIVE, ensure junction connections are properly defined -->
<junction id="junc_1" name="Main_Intersection">
  <connection id="0" incomingRoad="road1" connectingRoad="road2"
              contactPoint="start">
    <laneLink fromLane="1" toLane="-1"/>
  </connection>
</junction>

<!-- For SUMO: configure junction access type -->
<edge id="road1">
  <lane id="road1_0" allow="private emergency authority bus taxi">
    <!-- Vehicles restricted to specific types -->
  </lane>
</edge>
```

**Testing junction coverage:**
```python
# Count junction scenarios vs. total
junction_count = sum(1 for s in scenarios if 'junction' in s.category)
junction_pct = junction_count / len(scenarios) * 100
print(f"Junction coverage: {junction_pct:.1f}%")  # Target: >15%

# If <15%: add intersection crossing, left turn, right turn, U-turn scenarios
```
