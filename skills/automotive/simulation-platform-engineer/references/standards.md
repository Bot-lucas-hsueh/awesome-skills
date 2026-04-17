## § 7 Standards & Reference

### Domain Frameworks

- **ASAM OpenSCENARIO 2.0**: Scenario DSL standard; use for all scenario authoring to ensure tool interoperability
- **ASAM OpenDRIVE 1.7**: Road network description; mandatory for lane-level map representation
- **ISO 21448 (SOTIF)**: Safety of the Intended Functionality; drives scenario selection for perception boundary cases
- **ISO 26262**: Functional safety; simulation used to verify ASIL-classified functions
- **UN Regulation 157 (ALKS)**: Automated Lane Keeping System type approval; defines simulation acceptance criteria
- **IEEE 2846**: Formal model for AV safety assumptions; informs scenario parameter bounds

### Key Metrics Table

| Metric | Definition | Target Range |
|--------|-----------|--------------|
| **Scenario Coverage Index (SCI)** | % of ODD parameter combinations covered by test scenarios | >85% for production release |
| **VMT-equivalent** | Virtual miles driven per real test mile (simulation multiplier) | >1000x for highway; >500x for urban |
| **Edge Case Detection Rate** | % of known critical scenarios caught by regression suite | >95% |
| **Sensor Model RMSE** | Point cloud density error vs. real sensor | <5% point density deviation |
| **CI Pipeline Latency** | Wall-clock time for full nightly regression | <8 hours for 500 scenarios |
| **Scenario Replay Fidelity** | Sensor output correlation between sim and real on same trajectory | >0.85 Pearson correlation |
| **Mean Scenario Execution Time** | Average time per scenario in headless mode | <60s for behavioral; <300s for perception |

---

## Phase 1: Scenario Library Design

**Activities:**
- Analyze ODD definition and extract testable parameters (weather, time-of-day, traffic density, road type, NPC count)
- Mine real-world incident databases and edge-case logs for scenario seeds
- Define combinatorial coverage matrix using Scenic or custom sampler
- Author baseline scenarios in OpenSCENARIO 2.0 with parameterized actor behaviors

**Done Criteria:**
- [ ] ODD parameter space fully enumerated with 3-level grid (min/nominal/max)
- [ ] Scenario library contains >200 parameterized base scenarios
- [ ] Each scenario has defined pass/fail oracle (KPI threshold, collision check, comfort metric)
- [ ] Scenarios version-controlled in Git with semantic versioning

**FAIL Criteria:**
- Scenarios hardcode sensor/weather parameters instead of using parameterized injection
- No pass/fail oracle defined (scenarios produce data but no automated evaluation)
- Map assets not validated against OpenDRIVE schema

**Template — Scenario YAML Header:**
```yaml
scenario_id: "URB_INT_001"
version: "2.1.0"
category: "urban_intersection"
ood_parameters:
  weather: [clear, rain_light, rain_heavy, fog]
  time_of_day: [dawn, day, dusk, night]
  ego_speed_mps: [5, 10, 15]
  npc_count: [2, 8, 20]
oracle:
  type: "collision_free + comfort"
  max_deceleration_mps2: 4.0
  collision_threshold: false
```

### Phase 2: Sensor Model Integration & Validation

**Activities:**
- Integrate LiDAR model with configurable beam count, range, angular resolution, noise sigma
- Implement camera ISP pipeline: lens distortion, motion blur, sensor noise (Gaussian + Poisson)
- Validate sensor outputs against Waymo/nuScenes real-world logs; compute RMSE and KL-divergence
- Document fidelity envelope: conditions where sim sensor diverges from real

**Done Criteria:**
- [ ] LiDAR point density RMSE < 5% vs. real sensor on held-out validation set
- [ ] Camera noise model validated on at least 3 lighting conditions
- [ ] Radar RCS model matches real-world returns for vehicle/pedestrian/cyclist classes
- [ ] Fidelity report published with quantitative metrics per sensor modality

**FAIL Criteria:**
- Sensor model validated only on training data (no held-out set)
- No quantitative fidelity metrics — only visual inspection

### Phase 3: CI/CD Regression Pipeline

**Activities:**
- Deploy CARLA server pool on Kubernetes; configure headless rendering per instance
- Implement ScenarioRunner orchestration with parallel execution and result aggregation
- Build KPI dashboard: SCI trend, failure heatmap by scenario category, daily VMT-equivalent
- Configure nightly regression trigger; alert on SCI regression >2% or new collision failure

**Done Criteria:**
- [ ] 500 scenarios execute in <8 hours on 20-node cluster
- [ ] Failure artifacts (scenario log, sensor recordings, ego trace) auto-archived on failure
- [ ] KPI dashboard live with 7-day trend for SCI, VMT-eq, and edge case detection rate
- [ ] RNG seed and simulator version logged for every test run

**FAIL Criteria:**
- Nightly regression non-deterministic (different results on re-run with same seed)
- Failed scenarios not reproducible due to missing artifact archiving

---

