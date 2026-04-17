# Troubleshooting Guide

## 8.1 Reducer Selection Errors

### Motor Shaft Diameter Mismatch

**Symptoms:** Motor shaft doesn't fit the reducer input bore. Installation is impossible without modification.

**Diagnosis:**
1. Verify the motor shaft diameter matches the reducer's standard bore size
2. Check IEC or NEMA motor frame standard (IEC: 56-355mm, NEMA: 56-449T)
3. Confirm keyway dimensions and shaft projection length against reducer catalog spec
4. Verify reducer manufacturer uses metric or imperial bore sizing

**Solutions:**
- Use an adapter/bushing (bore adapter) to bridge the size difference
- Specify the correct motor frame size from the reducer manufacturer's compatibility list
- If non-standard motor, specify custom input bore with tolerance (H7)
- Always confirm bore, keyway, and pilot diameter simultaneously

### Insufficient Torque for Application

**Symptoms:** Reducer selected based on catalog torque rating, but joint stalls or skips during operation. Motor draws excessive current.

**Diagnosis:**
1. Check if catalog torque is nominal (continuous) vs. maximum (intermittent). Operating torque should be 60-80% of nominal rating for reliability.
2. Verify acceleration torque calculation includes inertia ratio (load inertia / motor inertia). Inertia ratio >3:1 causes servo instability.
3. Confirm reduction ratio — is the ratio correct for the required output speed and torque?
4. Check for shock loading or reversing operation, which dramatically reduces effective torque capacity.

**Solutions:**
- Re-select reducer with 30-50% higher torque rating than calculated peak torque
- Add a gearbox with higher reduction ratio if speed allows
- Use a two-stage reducer for high inertia ratio applications
- For servo applications: target inertia ratio <3:1 using a larger motor or planetary first stage

### Output Speed Too High or Too Low

**Symptoms:** Joint moves too fast or too slow. Throughput of the robot cycle is off.

**Diagnosis:**
1. Calculate expected output speed: Input speed / Total reduction ratio
2. Verify input speed is correct (motor rated speed × inverter frequency / 60 Hz)
3. Check if reducer has a different ratio stamped vs. catalog (some are custom ratios)

**Solutions:**
- For harmonic drives: ratio is fixed (30:1, 50:1, 80:1, 100:1, 120:1, 160:1, 200:1)
- For RV reducers: multiple ratio options (27:1 to 192:1). Select next available ratio.
- Add belt/coupling speed adjustment between motor and reducer
- Specify variable frequency drive (VFD) with adjustable speed control

## 8.2 Harmonic Drive Issues

### Excessive Backlash

**Symptoms:** Robot arm has visible play at the joint. Positioning accuracy degrades, especially under load reversals.

**Diagnosis:**
1. Measure backlash with dial indicator: fix input, rotate output in both directions. Record total angular play.
2. Check if backlash exceeds manufacturer specification (typically <1 arc-min for precision, <3 arc-min for standard harmonic drives)
3. Inspect flexspline for fatigue cracks, discoloration, or deformation — causes increased backlash over time
4. Verify wave generator bearings are not worn or preload lost

**Solutions:**
- If backlash exceeds spec on a new reducer: return under warranty, check installation alignment
- If backlash developed over time: replace the flexspline (wear item). Life varies by load and cycles but typically 10,000-20,000 hours under rated conditions
- Ensure proper lubrication: insufficient grease causes accelerated wear
- Check for misalignment in input/output shaft coupling causing uneven load distribution

### High Operating Temperature

**Symptoms:** Reducer case temperature exceeds 70-80°C during continuous operation. Thermal shutdown or degraded accuracy.

**Diagnosis:**
1. Check ambient temperature — harmonic drives de-rate significantly above 40°C ambient
2. Verify lubrication — wrong grease viscosity or insufficient grease causes friction heating
3. Check mounting orientation — horizontal vs. vertical affects heat dissipation and oil distribution
4. Verify if the duty cycle exceeds the thermal rating (S6 continuous vs. S1 intermittent)

**Solutions:**
- Add heat dissipation measures: aluminum mounting flange, forced air cooling, thermal shunts
- Reduce cycle rate or add cooling idle periods between cycles
- Specify harmonic drive with larger frame size for thermal margin
- Use synthetic lubricant rated for higher temperature (consult manufacturer)
- Check that output torque does not continuously exceed 80% of rated torque

### Noise and Vibration

**Symptoms:** Unusual whining, howling, or resonant vibration from the harmonic drive.

**Diagnosis:**
1. Check input speed — harmonic drives have speed-dependent noise characteristics. Operating below minimum speed can cause irregular noise.
2. Verify alignment between motor and reducer input — angular and parallel misalignment generates noise
3. Check for gear contact pattern issues — improper preload of wave generator bearings
4. Inspect for contamination in the reducer (metal particles in grease)

**Solutions:**
- Use flexible coupling between motor and harmonic drive input
- Ensure proper input shaft alignment within 0.05mm TIR
- Replace contaminated lubricant
- If noise is inherent at certain speeds: adjust operating speed away from resonant frequency
- Check wave generator assembly — replace if bearings are noisy

## 8.3 RV Reducer Issues

### Output Shaft Runout Exceeds Specification

**Symptoms:** Mounted flange has eccentricity >0.02mm. Causes planetary carrier misalignment, uneven load distribution.

**Diagnosis:**
1. Mount reducer on precision V-block and measure output flange runout with dial indicator
2. Check mounting bolt torque — over-tightening can distort the housing
3. Verify the mating surface on the robot arm is machined flat (within 0.02mm)

**Solutions:**
- Re-face the robot arm mounting surface if flatness exceeds spec
- Use calibrated torque wrench for mounting bolts, follow specified sequence (cross-wise pattern)
- Replace reducer if runout exceeds tolerance and persists after re-mounting

### Oil Leakage at Output Seal

**Symptoms:** Grease or oil observed around output shaft area. Oil mist on surrounding components.

**Diagnosis:**
1. Check if seal is damaged during installation (lip nicked or rolled)
2. Verify oil level — overfilling causes pressure buildup and seal blowout
3. Check shaft surface finish — seal lip requires Ra 0.2-0.8 μm surface finish
4. Inspect for thermal expansion causing seal compression set

**Solutions:**
- Replace output shaft seal with manufacturer-specified part (Viton or PTFE lip seal)
- Ensure shaft surface finish meets Ra 0.4 μm minimum
- Fill to specified oil level, not above
- Apply anti-seize compound to shaft before seal installation
- For horizontal mounting: position drain plug at lowest point

### Torsional Vibration Resonance

**Symptoms:** System vibrates at specific speeds. Causes position errors in servo control loops.

**Diagnosis:**
1. Perform frequency response analysis on motor-reducer-load system
2. Calculate torsional natural frequency of the system — if it coincides with operating speeds, resonance occurs
3. Check damping ratio — harmonic drives have low inherent damping

**Solutions:**
- Add a torsional damper or柔性联轴器 (flexible coupling) at input
- Change operating speed to avoid resonance frequency
- Use a two-stage gearbox to lower natural frequency below operating range
- Tune servo drive to add damping at the problematic frequency

## 8.4 Lubrication Problems

### Grease Hardening or Contamination

**Symptoms:** Grease in harmonic drive turns dark, hard, or contains metal particles. Output stiffness decreases.

**Diagnosis:**
1. Check operating temperature history — temperatures >100°C accelerate grease degradation
2. Inspect for contamination: water (condensation), cleaning solvents, or incompatible grease mixed in
3. Count operating hours — most harmonic drive greases last 5,000-10,000 hours under rated conditions

**Solutions:**
- Replace all internal grease per manufacturer procedure. Harmonic drive requires precision re-greasing.
- Ensure correct grease type (typically synthetic hydrocarbon or PFPE-based)
- Never mix grease types — incompatible thickeners can cause hardening
- After re-greasing: run-in period at reduced load (30% rated) for 50-100 hours

### Insufficient Lubrication in RV Reducer

**Symptoms:** Increased starting torque, intermittent stick-slip motion, premature wear on cycloidal discs.

**Diagnosis:**
1. Check oil level with sight glass or dipstick — oil should be at the center of the sight glass when stationary
2. Verify oil viscosity grade — too high viscosity causes drag; too low causes wear
3. Check for oil degradation (dark color, burned smell, metal particles)

**Solutions:**
- Top up or replace with manufacturer-specified oil grade (typically ISO VG 150-460 gear oil)
- For horizontal RV reducers: ensure oil circulates properly to all bearings
- Change oil at specified intervals (typically 5,000-10,000 hours or annually)
- Use oil analysis (spectrographic) for critical applications to determine change interval

## 8.5 Mounting & Integration

### Input Coupling Misalignment

**Symptoms:** Motor bearing fails prematurely. Input shaft of reducer shows wear marks. Motor runs hot.

**Diagnosis:**
1. Measure angular misalignment with dial indicator on both sides of coupling
2. Check parallel offset between motor shaft and reducer input shaft
3. Verify coupling selection — is the coupling rated for the torque and misalignment?

**Solutions:**
- Use flexible coupling (Oldham or jaw type) to accommodate misalignment up to 0.1mm
- Re-align motor mounting plate using dial indicator
- Replace worn coupling with new one — couplings lose their flexibility after extended use
- Set coupling hub push-off distance per manufacturer spec

### Resonance in Motor-Drive System

**Symptoms:** Motor vibrates, control cabinet breaker trips intermittently. Servo drive shows overcurrent faults.

**Diagnosis:**
1. Bode plot analysis of drive — check if mechanical resonance frequency coincides with control loop bandwidth
2. Measure mechanical resonance with accelerometer at motor mount

**Solutions:**
- Add mechanical filter (harmonic isolator) between motor and reducer
- Reduce servo loop bandwidth below resonance frequency (at cost of response time)
- Add notch filter in servo drive at resonance frequency
- Increase damping by using flexible coupling
