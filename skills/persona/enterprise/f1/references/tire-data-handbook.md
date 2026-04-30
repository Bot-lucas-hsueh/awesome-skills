# Tire Data Handbook

## Pirelli F1 Tire Range (2024)

### Compound Characteristics

#### C1 - Hard (White)

**Technical Specifications:**
- Rubber compound: Hardest in range
- Working range: 90-110°C
- Peak performance window: 10-25 laps
- Degradation rate: -0.02s/lap (stable phase)

**Strategic Use:**
- High degradation tracks (Barcelona, Silverstone)
- Long stints with consistent pace
- Safety car periods requiring extended tire life
- Two-stop strategies as second stint tire

**Optimal Conditions:**
- Hot track temperatures (>35°C ambient)
- Smooth asphalt surfaces
- Rear-limited tracks

**Warning Signs:**
- Temperatures below 85°C: poor grip, graining risk
- Temperatures above 115°C: blistering, rapid degradation

---

#### C2 - Medium (Yellow)

**Technical Specifications:**
- Rubber compound: Medium-hard
- Working range: 95-115°C
- Peak performance window: 8-20 laps
- Degradation rate: -0.03s/lap (stable phase)

**Strategic Use:**
- Race start tire (most common choice)
- One-stop strategies (if tire life sufficient)
- Balanced tracks requiring compromise
- Mixed conditions intermediate choice

**Optimal Conditions:**
- Moderate temperatures (25-35°C ambient)
- Variable track surfaces
- Neutral balance tracks

**Warning Signs:**
- Cold temperatures: surface graining
- Overheating: shoulder blistering

---

#### C3 - Soft (Red)

**Technical Specifications:**
- Rubber compound: Medium-soft
- Working range: 105-125°C
- Peak performance window: 5-15 laps
- Degradation rate: -0.05s/lap (after initial peak)

**Strategic Use:**
- Qualifying (Q2 mandatory if advancing to Q3)
- Final stint attacking position
- Tracks requiring maximum mechanical grip
- Short first stints for undercut strategies

**Optimal Conditions:**
- Cool temperatures (<30°C ambient)
- Street circuits (Monaco, Singapore)
- High mechanical grip requirements

**Warning Signs:**
- Rapid lap time drop-off after 8-10 laps
- Grain pattern on surface
- Rear tire overheating on traction zones

---

#### C4 - Supersoft (Red*)

**Technical Specifications:**
- Rubber compound: Soft
- Working range: 110-130°C
- Peak performance window: 4-12 laps
- Degradation rate: -0.08s/lap (after peak)

**Strategic Use:**
- Qualifying maximum attack
- Very short stints in race
- Maximum grip requirement scenarios

**Note:** Selected for street circuits and low-degradation tracks

---

#### C5 - Ultrasoft (Red**)

**Technical Specifications:**
- Rubber compound: Softest available
- Working range: 115-135°C
- Peak performance window: 3-10 laps
- Degradation rate: -0.12s/lap (rapid after peak)

**Strategic Use:**
- Qualifying only (extremely rare in race)
- Monaco Q3 mandatory
- Absolute maximum one-lap performance

**Note:** Highest risk of overheating and degradation

---

## Wet Weather Tires

### Intermediate (Green)

**Technical Specifications:**
- Tread pattern: 4 grooves
- Working range: 80-110°C
- Dispersion capacity: Up to 25L/second at 300 km/h

**Usage Guidelines:**
- Damp track conditions
- Light rain, no standing water
- Transition conditions (drying track)
- Lap time crossover with slicks: 2-4 seconds slower

**Optimal Conditions:**
- Track not fully dry
- No standing water
- Temperatures above 10°C

---

### Full Wet (Blue)

**Technical Specifications:**
- Tread pattern: Deep grooves with optimized channels
- Working range: 60-90°C
- Dispersion capacity: Up to 65L/second at 300 km/h

**Usage Guidelines:**
- Heavy rain conditions
- Standing water on track
- Safety concerns with intermediates

**Optimal Conditions:**
- Heavy rainfall
- Significant standing water
- Temperatures above 5°C

---

## Tire Management Strategies

### Temperature Management

**Warming Phase (First 2-3 laps):**
- Gradual build-up of temperature
- Avoid aggressive inputs
- Monitor surface vs. carcass temperatures

**Optimal Window Maintenance:**
- Consistent pace to maintain heat
- Avoid extended following (overheating risk)
- Adjust driving style for conditions

**Cooling (End of Stint):**
- Temperature drop reduces degradation
- Risk: going below minimum operating window
- Manage if extending stint unexpectedly

### Degradation Types

**Graining:**
- Cause: Cold tires, aggressive inputs
- Appearance: Tearing on surface
- Effect: Loss of grip, vibration
- Solution: Heat management, driving style adjustment

**Blistering:**
- Cause: Overheating, excessive camber
- Appearance: Bubbles on surface
- Effect: Rapid performance loss
- Solution: Temperature reduction, setup change

**Flat Spotting:**
- Cause: Wheel lock-up
- Appearance: Flat section on tire
- Effect: Vibration, reduced contact patch
- Solution: Avoid lock-ups, manage damaged tire

---

## Compound Selection Strategy

### Track Selection Matrix

| Track Type | Typical Selection | Strategy |
|------------|-------------------|----------|
| High degradation | C1-C2-C3 | Two-stop likely |
| Medium degradation | C2-C3-C4 | One or two-stop |
| Low degradation | C3-C4-C5 | One-stop likely |
| Street circuit | C3-C4-C5 | Safety car probability |
| High speed | C1-C2-C3 | Rear tire management |

### Stint Length Modeling

**Example: 55-lap race, Medium degradation track**

| Strategy | Stint 1 | Stint 2 | Stint 3 | Total Time* |
|----------|---------|---------|---------|-------------|
| One-stop | S (18) | H (37) | - | Base |
| Two-stop | S (15) | M (20) | M (20) | +8 seconds |
| Two-stop (alt) | M (22) | S (12) | M (21) | +12 seconds |

*Relative to optimal one-stop with traffic consideration

---

*Data based on Pirelli F1 tire specifications and team data (2024)*
