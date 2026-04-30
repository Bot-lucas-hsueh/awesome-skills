# AV Simulation — Real-World Scenarios

## Scenario 1: Building a 10,000-Scenario Regression Suite for Highway Pilot

**Context:** A team of 8 engineers is developing a Highway Pilot (ALKS L3) feature. They need to validate the AV stack against 10,000+ scenarios before regulatory submission under UN R157. Currently they run 200 scenarios manually, which takes 3 days.

**Steps:**

1. **Enumerate the ODD parameter space:**
```yaml
# ODD parameters from UN R157 scope
road_type: [divided_multilane_highway]
ego_speed_mps: [10, 15, 20, 25, 30]  # ALKS: 0-60 km/h = 0-16.67 m/s
weather: [clear, rain_light, fog_light]  # EN 1947 conditions
time_of_day: [day, night, dawn_dusk]
npc_scenario: [cut_in_slow, cut_in_fast, tailgating, emergency_braking, vehicle_stopped]
npc_count: [1, 2, 3, 5]
inter_object_distance_m: [20, 40, 60, 100]
```

2. **Compute coverage matrix:**
```python
# Full factorial: 1 × 5 × 3 × 3 × 5 × 4 × 4 = 10,800 combinations
# Use combinatorial coverage (not full factorial) to reduce to ~3,000 core cases
from itertools import product

params = {
    'ego_speed': [10, 20, 30],
    'weather': ['clear', 'rain_light', 'fog_light'],
    'npc_scenario': ['cut_in_slow', 'cut_in_fast', 'vehicle_stopped'],
    'npc_count': [1, 2, 5],
    'distance': [40, 100]
}
# Orthogonal array (Taguchi L9): 9 base scenarios × 3 weather × 3 times_of_day = 81
# Scale with domain randomization to 10,000+ instances
```

3. **Author base scenarios in OpenSCENARIO 2.0:**
```xml
<OpenScenario>
  <FileHeader version="2.0.0" author="simulation-team"/>
  <ParameterDeclarations>
    <ParameterDeclaration name="ego_init_speed" parameterType="double" value="20"/>
    <ParameterDeclaration name="npc_cut_in_ttc" parameterType="double" value="2.5"/>
  </ParameterDeclarations>
  <Catalogs>
    <VehicleCatalog path="vehicle_catalog/"/>
  </Catalogs>
  <Entities>
    <Object name="ego">
      <Vehicle object="vehicle.ego"/>
    </Object>
    <Object name="npc">
      <Vehicle object="vehicle.nissan_leaf"/>
    </Object>
  </Entities>
  <Storyboard>
    <Story owner="ego">
      <Act>
        <ManeuverGroup maximumExecutionCount="1">
          <Actors selectTriggeringEntities="false">
            <EntityRef entity="ego"/>
          </Actors>
          <Maneuver name="highway_cruise">
            <Event name="start_cruise" priority="overwrite">
              <Action name="set_speed">
                <LongitudinalAction>
                  <SpeedAction>
                    <SpeedActionDynamics maxDeceleration="3.0" maxAcceleration="2.0" duration="0"/>
                    <SpeedActionTarget>
                      <AbsoluteTargetSpeed value="$ego_init_speed"/>
                    </SpeedActionTarget>
                  </SpeedAction>
                </LongitudinalAction>
              </Action>
            </Event>
          </Maneuver>
        </ManeuverGroup>
      </Act>
    </Story>
  </Storyboard>
</OpenScenario>
```

4. **Deploy on Kubernetes:**
```bash
# Deploy CARLA server pool
kubectl apply -f carla-cluster.yaml

# Run scenario suite with parallelization
python3 run_suite.py \
  --suite highway_pilot_regression \
  --parallel 50 \
  --output s3://av-regression/highway-pilot/run-2024-11-15/ \
  --timeout 120s

# Expected: 10,800 scenarios in ~4 hours on 50-node cluster
# VMT-equivalent: ~50M virtual miles
```

5. **Generate KPI dashboard:**
```bash
# Compute SCI
python3 compute_sci.py \
  --executed scenarios/run-2024-11-15/results.json \
  --odd odd_definitions.yaml

# Output:
# SCI: 94.7%
# VMT-equivalent: 52.3M miles
# Critical scenario pass rate: 78.3% (target: >95%)
# FAILURES: 23 critical scenarios — see failure_heat_map.html
```

**Outcome:** SCI = 94.7%, well above the 85% production threshold. 23 critical failures identified and routed to engineering for root cause analysis.

---

## Scenario 2: Quantifying and Closing the Camera Sim-to-Real Gap

**Context:** The ML team reports that a perception model trained on CARLA synthetic data has 12% lower mAP on real nuScenes data. They need to diagnose the gap and implement a fix.

**Diagnosis:**

1. **Modality isolation:**
```python
# Test which sensor modality causes the gap
# Run model on nuScenes val set with different input configurations

results = {
    'lidar_only': evaluate(model, lidar_only=True),      # Gap: 3%
    'camera_only': evaluate(model, camera_only=True),    # Gap: 9%
    'fusion': evaluate(model, fusion=True)               # Gap: 12%
}
# Camera is the primary gap source (9% vs 3%)
```

2. **Pixel-level analysis:**
```python
# Compute KL divergence on image histograms
sim_images = load_synthetic_batch('carla_highway/')
real_images = load_real_batch('nuscenes/')

kl_lum = kl_divergence_histograms(
    [img[:,:,0] for img in real_images],    # Real luminance
    [img[:,:,0] for img in sim_images]      # Sim luminance
)
# Result: KL = 0.31 (target: <0.15)
# HDR/tone-mapping is the primary camera gap
```

3. **Fix using domain randomization:**
```python
# Extend CARLA camera configuration
camera_bp.set_attribute('enable_postprocess', 'true')
camera_bp.set_attribute('hdr', 'true')

# Add domain randomization during data generation
def randomize_camera_conditions():
    return {
        'exposure_mode': random.choice(['manual', 'histogram']),
        'blur_amount': random.uniform(0, 2),  # Motion blur
        'gamma': random.uniform(1.8, 2.4),     # Tone mapping
        'chromatic_aberration': random.uniform(0, 0.005),
    }
# Generate 100,000 images with randomized conditions
```

4. **Fine-tune with CycleGAN:**
```python
# Train CycleGAN to translate sim → real
from cyclegan import CycleGAN

gan = CycleGAN(
    source_dir='carla_synthetic/',
    target_dir='nuscenes_real/',
    checkpoint_dir='cyclegan_checkpoints/'
)
gan.train(epochs=200)

# Apply trained model to synthetic data
translated_dataset = gan.translate('carla_new_batch/')
# FID after translation: 0.12 (target: <0.15)
```

5. **Validate the fix:**
```python
# Retrain model on translated synthetic data
model_v2 = train_perception_model(
    synthetic_data='translated_synthetic/',
    real_data='nuscenes_train/',
    validation='nuscenes_val/'
)

# Evaluate
mAP_sim_only = evaluate(model_v2, 'carla_test/')      # 0.67
mAP_real_only = evaluate(model_v2, 'nuscenes_val/')  # 0.71
gap = mAP_real_only - mAP_sim_only
# Gap: 4% (down from 12%) — acceptable for production
```

**Outcome:** Camera sim-to-real gap reduced from 12% to 4%. Model trained on translated synthetic data achieves 71% mAP on real nuScenes val set (vs 73% for real-only training — acceptable delta for production).

---

## Scenario 3: Emergency Sensor Degradation Testing — LiDAR Rain Failure

**Context:** The safety team needs to validate that the AV stack handles LiDAR sensor degradation in heavy rain. ASIL-B requirement: the system must detect sensor degradation and transition to safe state within 500ms.

**Design:**

1. **Rain degradation model:**
```python
# Model three rain effects on LiDAR:
# 1. Beam attenuation (droplets absorb/block beams)
# 2. Backscatter (returns from rain particles)
# 3. Wet surface multipath

def simulate_rain_effects(base_pointcloud, rain_mm_hr):
    # Attenuation: range reduction proportional to rainfall rate
    effective_range = base_range * np.exp(-0.05 * rain_mm_hr)
    
    # Backscatter: false returns near sensor
    backscatter_count = int(len(base_pointcloud) * rain_mm_hr * 0.01)
    backscatter = np.random.uniform(0, 3, (backscatter_count, 3))
    
    # Wet surface: additional returns from road surface
    wet_surface_returns = simulate_wet_puddle_reflections(base_pointcloud)
    
    return np.vstack([base_pointcloud * effective_range, backscatter, wet_surface_returns])
```

2. **Test matrix:**
```python
rain_intensity = [0, 5, 15, 30, 50, 80]   # mm/hr
object_distance = [15, 30, 50, 80]          # meters
object_class = ['vehicle', 'pedestrian', 'cyclist']

# Total: 6 × 4 × 3 = 72 degradation scenarios
# Evaluate: detection probability, degradation flag set, safe state transition time
```

3. **Execute in CARLA:**
```bash
python3 run_degradation_suite.py \
  --suite rain_sensor_degradation \
  --rain_rates 5,15,30,50,80 \
  --validate_safe_state \
  --max_transition_time_ms 500

# Results:
# Detection rate at 50mm/hr, 50m: 67% (below 90% threshold → FAIL)
# Safe state transition: 340ms (within 500ms → PASS)
# RECOMMENDATION: Add second LiDAR unit for redundancy above 30mm/hr
```

**Outcome:** System passes safe state transition requirements. Detection rate below 90% at 50mm/hr at 50m — operationally restrict ODD to 30mm/hr or implement sensor fusion fallback using radar.

---

## Scenario 4: Edge Case Mining from Real-World Fleet Incidents

**Context:** A fleet of 500 vehicles has logged 2 years of driving data. Analysis reveals 3 near-miss incidents that weren't in the current scenario library. The safety team needs these converted to regression scenarios.

**Incident-to-Scenario Pipeline:**

1. **Extract incident from log:**
```python
# Load Waymo-format log
from waymo_open_dataset import label_pb2

log = load_log('fleet_incident_2024_11_03_001.pb')
ego_traj = extract_ego_trajectory(log)
other_traj = extract_object_trajectory(log, object_id='id_42')

# Compute TTC at closest approach
ttc_min = compute_ttc(ego_traj, other_traj)
# Result: TTC = 0.8s (critical — below 1.0s threshold)
```

2. **Cluster similar scenarios:**
```python
# Cluster all log events by scenario type using trajectory similarity
from sklearn.cluster import DBSCAN

features = extract_scenario_features(all_logs)
clusters = DBSCAN(eps=0.3, min_samples=5).fit_predict(features)

# Find existing library coverage per cluster
for cluster_id in range(max(clusters)):
    cluster_scenarios = [s for s in all_scenarios if s.cluster == cluster_id]
    if len(cluster_scenarios) < 3:
        print(f"CLUSTER {cluster_id}: UNDERREPRESENTED — {len(cluster_scenarios)} scenarios")
        # New scenario category detected: "debris avoidance on curved road"
```

3. **Convert to concrete scenario:**
```python
# Extract parameters from real-world incident
new_scenario = {
    'type': 'debris_avoidance_curved',
    'ego_speed_mps': ego_traj.speed[incident_frame],
    'road_curvature': 0.02,  # 1/m
    'debris_position': other_traj.position[incident_frame],
    'TTC': 0.8,
    'weather': 'clear',
    'time_of_day': 'dusk'
}

# Author as OpenSCENARIO 2.0
scenario_xml = generate_openscenario(new_scenario)
save_scenario(scenario_xml, 'debris_avoidance_curved_v1.xosc')

# Add to regression suite
add_to_suite('debris_avoidance_curved_v1.xosc', 'critical_scenarios')
```

4. **Verify coverage improvement:**
```bash
# Re-compute SCI after adding new scenario category
python3 compute_sci.py --suite full_regression

# Before: SCI = 91.2% (missing debris scenarios)
# After:  SCI = 94.7%
```

**Outcome:** 3 near-miss incidents → 3 new regression scenarios. SCI improved by 3.5%. New scenario category "debris_avoidance_curved" added to all future regression runs.

---

## Scenario 5: GPU Oversubscription Debugging in Nightly CI

**Context:** The nightly regression suite started timing out after adding 50 new scenarios. 500 scenarios now take 26 hours instead of 7 hours. GPU utilization metrics show GPU oversubscription.

**Diagnosis:**
```bash
# Check GPU utilization per node
kubectl top pods -l app=carla --containers

# Output:
# pod/carla-node-3: nvidia.com/gpu: 95% (should be ~50% with 2 instances)
# pod/carla-node-7: nvidia.com/gpu: 98%

# The issue: 2 CARLA instances per GPU, but each is using full render mode
# Need to reduce to 1 instance per GPU OR switch to headless mode for behavioral tests
```

**Fix:**
```yaml
# Separate behavioral and perception scenario pools
apiVersion: v1
kind: ConfigMap
metadata:
  name: scenario-pool-config
data:
  behavioral.yaml: |
    pool_size: 30
    gpu_required: false
    carla_mode: headless  # No rendering
    timeout_per_scenario: 60s

  perception.yaml: |
    pool_size: 10
    gpu_required: true
    carla_mode: render
    timeout_per_scenario: 300s
```

```bash
# Update CI pipeline
python3 run_suite.py \
  --behavioral_pool behavioral.yaml \
  --perception_pool perception.yaml \
  --parallel behavioral:30,perception:10

# Result: 40 parallel instances (30 headless + 10 GPU)
# Total time: 7.2 hours (within 8-hour nightly window)
```

---

## Scenario 6: OpenDRIVE Map Validation for Urban Intersection

**Context:** A new urban map for downtown Chicago has 47 intersections. CARLA fails to load 3 of them with "road connectivity error". SUMO shows NPCs deadlocking at 2 intersections.

**Validation workflow:**

1. **Schema validation:**
```bash
xmllint --schema OpenDRIVE_v1.7.xsd downtown_chicago.xodr --noout
# Fails: 3 junction IDs reference non-existent roads
```

2. **Python debugging:**
```python
from lxml import etree
import opendrive.parse as parse

tree = etree.parse('downtown_chicago.xodr')
roads = {r.get('id'): r for r in tree.findall('.//road')}

# Find broken junction references
for junction in tree.findall('.//junction'):
    for conn in junction.findall('connection'):
        incoming = conn.get('incomingRoad')
        connecting = conn.get('connectingRoad')
        if incoming not in roads:
            print(f"BROKEN: junction {junction.get('id')} "
                  f"references nonexistent road {incoming}")
```

3. **Fix the broken connections:**
```xml
<!-- Before: Junction references road IDs that don't exist -->
<junction id="junc_main_42" name="Main_Clark_Intersection">
  <connection incomingRoad="road_abc" connectingRoad="road_xyz".../>
</junction>

<!-- After: Correct road IDs -->
<junction id="junc_main_42" name="Main_Clark_Intersection">
  <connection incomingRoad="road_main_west" connectingRoad="road_clark_south".../>
</junction>
```

4. **SUMO deadlock analysis:**
```python
# Simulate intersection in SUMO
sumo_cfg = 'intersection_42.sumocfg'
traci.start(['sumo-gui', '-c', sumo_cfg])

# Run 1000 vehicles through intersection
stats = traci.simulation.simulate(1000)

# Check for deadlocks
if stats.collisions > 0 or stats.teleports > 0:
    # Find conflicting vehicle routes
    deadlock_vehicles = traci.simulation.get_deadlock_vehicles()
    print(f"DEADLOCK: {deadlock_vehicles}")
    # Fix: Add route priority or traffic light phase adjustment
```

**Outcome:** All 47 intersections load successfully in CARLA. SUMO deadlocks resolved by adjusting traffic light phase timing and adding vehicle class restrictions.

---

## Scenario 7: Building Synthetic Training Dataset for 3D Detection

**Context:** The perception team needs 1 million labeled LiDAR frames for training a 3D object detector. Collecting real data costs $50/frame for annotation. Synthetic data from simulation costs $0.02/frame.

**Pipeline:**

1. **Define domain randomization space:**
```python
domain_params = {
    'weather': ['clear', 'rain_heavy', 'snow', 'fog_thick', 'sun_low'],
    'time_of_day': ['dawn', 'day', 'dusk', 'night'],
    'scene_complexity': ['simple', 'moderate', 'dense'],
    'object_count': {'car': (0, 8), 'pedestrian': (0, 15), 'cyclist': (0, 5)},
    'occlusion_level': [0.0, 0.3, 0.6],  # Fraction of object occluded
    'sensor_noise': [0.0, 0.01, 0.03]   # Std dev of point jitter
}

# Total combinatorial space: 5 × 4 × 3 × 3 × 3 × 3 = 1,620 base configurations
# Generate 600 instances per config = 972,000 frames
```

2. **Generate with ground truth annotation:**
```python
from carla_data_generator import CarlaDataGenerator

generator = CarlaDataGenerator(
    carla_host='localhost',
    carla_port=2000,
    output_dir='s3://synthetic-lidar-dataset/',
    annotation_format='openlabel'
)

# Generate with automatic ground truth
scenario = generator.create_randomized_scenario(domain_params)
world.tick()

# Capture LiDAR + camera + 3D bounding boxes
sensor_data = capture_step()
ground_truth = {
    'bounding_boxes_3d': extract_3d_boxes(sensor_data),
    'semantic_labels': extract_semantic_labels(sensor_data),
    'occlusion_flags': compute_occlusion(sensor_data),
    'ego_pose': sensor_data.ego_pose,
    'timestamp': sensor_data.timestamp
}

generator.save_frame(sensor_data, ground_truth)
```

3. **Validate fidelity against real data:**
```python
# Compare synthetic vs real nuScenes distribution
real_stats = compute_distribution('nuscenes_val/', modality='lidar')
synth_stats = compute_distribution('synthetic_1m/', modality='lidar')

# Per-class density
for cls in ['car', 'pedestrian', 'cyclist']:
    real_density = real_stats[cls]['density']
    synth_density = synth_stats[cls]['density']
    delta = abs(real_density - synth_density) / real_density
    print(f"{cls}: delta={delta:.2%}")  # Target: <10%

# car: delta=4.2% ✅
# pedestrian: delta=7.8% ✅
# cyclist: delta=12.3% ⚠️ — need more cyclist samples
```

4. **Address cyclist underrepresentation:**
```python
# Oversample cyclist configurations by 3x
for _ in range(3):
    generator.create_randomized_scenario(
        domain_params,
        forced_object_types={'cyclist': (2, 5)}
    )

# Re-validate
# cyclist: delta=6.1% ✅
```

**Outcome:** 1,000,000 synthetic frames generated at $0.02/frame = $20,000 total cost (vs $50M for equivalent real data). FID score vs nuScenes: 0.09 (target <0.15). Model trained on synthetic data: 71.2% mAP on real nuScenes val (vs 73.8% with real-only training).
