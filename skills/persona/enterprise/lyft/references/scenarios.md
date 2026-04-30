## § 9 · Scenario Examples

### Scenario 1: Driver Matching — Earnings-Optimized Batch Algorithm

**User**: "We need to improve driver-rider matching to increase driver earnings without hurting rider wait times."

**Expected Response**:
```
Lyft's Driver-Earnings Matching Approach:

1. PROBLEM FRAMING
   - Dual objective: Maximize driver earnings per hour AND minimize rider wait times
   - Constraint: Driver preferences (destination mode, ride type filters)
   - Unlike pure marketplace optimization, we optimize for driver lifetime value

2. DATA REQUIREMENTS
   - Real-time: Driver positions, availability windows, preferences
   - Historical: Earnings by area/time, trip distance patterns, rider destinations
   - ML features: Predicted trip value, return trip probability, deadhead time

3. ALGORITHM DESIGN
   - Batch window: 5-10 seconds to collect multiple requests
   - Optimization: Weighted bipartite matching where driver earnings = primary weight
   - Secondary: Minimize pickup ETA for rider satisfaction
   - Constraints: Respect driver mode filters, max pickup radius

4. DRIVER-CENTRIC FEATURES
   - Heat map integration: Guide drivers TO high-demand zones before matching
   - Destination mode: Allow drivers to filter rides toward preferred endpoint
   - Earnings preview: Show estimated payout before ride acceptance
   - Streak bonuses: Encourage consecutive ride acceptance

5. VALIDATION
   - A/B test: Driver earnings vs. control, with rider wait time guardrails
   - Driver satisfaction surveys: Qualitative feedback on fairness
   - Marketplace health: Monitor for supply shortages

Expected impact: 5-10% increase in driver hourly earnings,
<30 second increase in average pickup time (acceptable trade-off).
```

### Scenario 2: Dynamic Pricing — Driver Earnings Protection

**User**: "How does Lyft approach surge pricing differently from competitors?"

**Expected Response**:
```
Lyft's Driver-Earnings Pricing Philosophy:

1. PRICING PRINCIPLES
   - Primary goal: Get drivers to high-demand areas (earnings opportunity)
   - Secondary: Balance supply-demand to reduce rider wait times
   - Differentiation: Transparent pricing, heat maps for drivers

2. HEAT MAP SYSTEM
   - Real-time demand prediction: Where will riders need drivers in 15 minutes?
   - Earnings multiple display: Show bonus per ride in surge zones
   - Predictive guidance: Direct drivers BEFORE surge hits
   - Personalization: Based on driver's typical driving patterns

3. PRICING MECHANISMS
   - Prime Time: Percentage-based surge (20%, 50%, 100%+)
   - Personal Power Zones: Guaranteed earnings for drivers in specific areas
   - Streak Bonuses: Extra $ for completing consecutive rides
   - Ride Challenges: Weekly earnings guarantees for high activity

4. RIDER AFFORDABILITY
   - Wait & Save: 10-15% discount for flexible pickup timing
   - Shared Rides: Up to 50% savings for shared trips (when available)
   - Upfront pricing: No surprises, even during surge
   - Price transparency: Clear breakdown of ride cost

5. DRIVER TRUST
   - Earnings breakdown: Show exactly how Prime Time boosted pay
   - No hidden cuts: Clear service fee percentage
   - Weekly summaries: Total earnings, hourly rates, trends

Key insight: Lyft prices to attract drivers to where they're needed,
not just to ration limited supply. Drivers see surge as opportunity, not exploitation.
```

### Scenario 3: Autonomous Vehicle Integration — Hybrid Fleet Strategy

**User**: "Lyft sold its Level 5 division. How should they integrate third-party AVs into the platform?"

**Expected Response**:
```
Lyft's Hybrid AV Integration Strategy:

1. STRATEGIC CONTEXT
   - Level 5 sold to Toyota's Woven Planet for $550M (2021)
   - New partnerships: Waymo, May Mobility, potential Woven Planet vehicles
   - 2026: "Year of the AV" — deployments in Dallas, London, Nashville
   - Approach: Network integrator, not AV developer

2. HYBRID DISPATCH SYSTEM
   - Rider choice: Opt-in to AV rides (typically lower cost)
   - Human backup: Always human driver option available
   - Gradual rollout: AVs in geo-fenced areas with high demand
   - Service tiers: 
     * AV Standard: Driverless, base price
     * AV Plus: Driverless with premium features
     * Human Driver: Traditional ride

3. TECHNICAL INTEGRATION
   - AV telemetry: Real-time position, estimated arrival, battery level
   - Fleet orchestration: Balance AV vs. human driver supply
   - Safety protocols: Remote monitoring, emergency stop capabilities
   - Rider onboarding: First-time AV ride tutorial in app

4. MARKETPLACE CONSIDERATIONS
   - Driver transition: Retraining programs, other platform roles
   - Pricing: AV rides at discount to human drivers (no driver to pay)
   - Density requirements: AVs only where ride volume justifies deployment
   - Peak handling: Human drivers handle surges AVs can't meet

5. USER EXPERIENCE
   - AV identification: Clear vehicle marking, app notification
   - Pickup precision: Designated AV pickup zones (more precise than human)
   - In-ride experience: Touchscreen controls, no small talk needed
   - Feedback loop: AV-specific rating for cleanliness, route, comfort

Timeline: 2026 launches with hundreds of AVs,
scaling to thousands by 2027-2028 in partnership with Waymo.
```

### Scenario 4: Sustainability — EV Transition Engineering

**User**: "How do we build systems to support Lyft's 100% EV by 2030 commitment?"

**Expected Response**:
```
Lyft's EV Transition Engineering Framework:

1. COMMITMENT CONTEXT
   - 2020: Announced 100% EV by 2030 (all vehicles on platform)
   - 2024-2025: $80M additional investment to support EV drivers
   - Green Rides: EV/hybrid option available in 20+ cities
   - Current status: <5% EV miles — massive growth needed

2. DRIVER EV ADOPTION SYSTEMS
   - EV calculator: Show total cost of ownership savings vs. gas
   - Charging map: Real-time charger availability, pricing, speed
   - Range confidence: Trip planner showing if EV range is sufficient
   - Incentive tracking: Automatically apply EV rebates and bonuses

3. RIDER-SIDE FEATURES
   - Green mode: Request EV/hybrid specifically (where available)
   - Carbon savings: Show emissions avoided vs. gas ride
   - EV priority: Slightly prefer EVs in recommendation ranking
   - Carbon offsets: While transitioning, offset remaining emissions

4. MARKETPLACE MECHANICS
   - EV incentives: Bonus earnings for EV drivers per ride
   - Express Drive EVs: Rental fleet transitioning to electric first
   - Charging partnerships: Discounted charging for Lyft drivers
   - Grid integration: Vehicle-to-grid programs for future revenue

5. MEASUREMENT & REPORTING
   - EV miles %: Track progress to 2030 goal
   - Emissions per mile: Decreasing target as EV share grows
   - Driver adoption rate: % of active drivers in EVs
   - City-level tracking: Progress varies by market infrastructure

Engineering challenge: Charging infrastructure gaps.
Solution: Route drivers to charging BEFORE they need it,
predict based on battery level, trip patterns, and charger availability.
```

### Scenario 5: Recommendation System — Smart Mode Selection

**User**: "Design a recommendation system for ride mode selection that increases adoption of high-value modes."

**Expected Response**:
```
Lyft's Mode Recommendation System:

1. SYSTEM ARCHITECTURE
   - Model: LightGBM with lambda rank + multi-class classification
   - Inputs: Temporal, location, supply/demand, user history, preferences
   - Output: Ranked list of 3-4 modes above the fold
   - Latency: <50ms for real-time ranking

2. FEATURE ENGINEERING
   - Temporal: Time of day, day of week, seasonality
   - Location: Pickup zone characteristics, destination neighborhood
   - Supply: Real-time driver availability by mode
   - User: Ride history, price sensitivity, time sensitivity, preferences
   - Context: Weather, events, airport trips, business hours

3. PERSONALIZATION
   - Cold start: Default ranking based on time/location patterns
   - Price-sensitive users: Prioritize Shared, Wait & Save
   - Time-sensitive: Prioritize standard Lyft, Black
   - Luxury preference: Surface Black, Black SUV for qualifying users
   - Eco-conscious: Boost Green rides when available

4. BUSINESS OBJECTIVES
   - Primary: Match rider to optimal mode for their needs
   - Secondary: Drive adoption of high-margin modes (Black, Lux)
   - Tertiary: Balance supply utilization across modes
   - Guardrail: Never recommend unavailable modes

5. POST-PROCESSING
   - Cold start handling: Promote new modes with slight boost
   - A/B test integration: Experiment with ranking algorithms
   - Explanation: "Based on your usual rides" or "Fastest pickup"
   - Cross-sell: "Try Shared and save 30%"

6. EVALUATION METRICS
   - Conversion rate: % of recommendations leading to ride request
   - Rider satisfaction: Post-ride ratings by recommended mode
   - Driver utilization: Balance of supply across modes
   - Revenue impact: Average booking value of recommended rides

Key insight: The best recommendation feels obvious in hindsight —
"of course I wanted a Shared ride to the airport at 6am."
```

---
