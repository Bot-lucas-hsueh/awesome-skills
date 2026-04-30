# 6th Generation Waymo Driver Technical Specifications

## Overview
Released August 2024. Production deployment began early 2026.

## Sensor Suite

### Cameras: 13 units (down from 29 in 5th gen)
- **Resolution:** 17 megapixels
- **Range:** 500 meters
- **Features:** 
  - High dynamic range (HDR)
  - Low-light sensitivity
  - Custom lenses and optomechanical engineering
- **Coverage:** 360° overlapping fields of view

### LiDAR: 4 units (down from 5 in 5th gen)
- **Type:** Custom-designed, built in California
- **Range:** Up to 500 meters
- **Coverage:** 360° bird's eye view
- **Capabilities:**
  - Precise depth measurement
  - Operates in complete darkness
  - Dust/rain penetration
  - Detects objects 300m+ away

### Radar: 6 units
- **Type:** Imaging radar
- **Capabilities:**
  - Velocity measurement
  - All-weather operation
  - Penetrates fog, rain, snow
  - Detects through occlusions (e.g., parked cars)

### External Audio Receivers (EARs)
- Emergency vehicle siren detection
- Horn detection
- Directional audio localization

## Cost Improvements

| Metric | 5th Gen | 6th Gen | Improvement |
|--------|---------|---------|-------------|
| Total sensors | 40+ | 23 | **42% reduction** |
| Estimated Driver cost | ~$40,000 | <$20,000 | **>50% reduction** |
| Camera count | 29 | 13 | 55% reduction |
| LiDAR count | 5 | 4 | 20% reduction |

## Compute Platform

### Processing
- **Custom Google TPUs** for ML inference
- **Sensor fusion engine** for multi-modal perception
- **Real-time trajectory planning**
- **Fail-operational redundancy**

### HD Maps
- **Centimeter-level accuracy**
- **Continuously updated**
- **Semantic understanding** (lanes, signs, signals)

## Vehicle Platforms

### Current Production

| Platform | Description | Status |
|----------|-------------|--------|
| **Jaguar I-PACE** | Premium EV SUV | Current fleet backbone |
| **Zeekr RT / "Ojai"** | Purpose-built robotaxi | Scaling production |
| **Hyundai IONIQ 5** | Mass-market EV | 50,000 unit order |

### Zeekr "Ojai" Specifications
- **Origin:** Geely (China), designed in Sweden
- **Type:** Purpose-built robotaxi
- **Features:**
  - Flat floor for easy entry/exit
  - Low step-in height
  - Integrated B-pillar doors
  - Designed specifically for autonomous ride-hailing

### Hyundai Partnership
- **Order size:** 50,000 units (largest AV vehicle order in history)
- **Testing began:** Late 2025
- **Production:** Scaling through 2026

## Manufacturing

### Waymo Driver Factory
- **Location:** Metro Phoenix, Arizona
- **Capacity:** Tens of thousands of units per year (scaling)
- **Integration:** Full Waymo Driver assembly and calibration

### Quality Assurance
- **Cpk >1.33** on critical dimensions
- **Automated sensor calibration**
- **End-to-end system testing**

---

*Last Updated: March 2026*
