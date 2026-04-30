# T-Mobile 5G Network Technical Specifications

## Overview

T-Mobile operates America's largest and fastest 5G network, built on a "layer cake" strategy combining low-band, mid-band, and mmWave spectrum for comprehensive coverage and capacity.

## Network Architecture

### The Layer Cake Strategy

```
┌─────────────────────────────────────────────────────────────┐
│  mmWave (28/39 GHz)                                        │
│  • Ultra-high capacity                                      │
│  • Dense urban areas, stadiums, venues                      │
│  • 1+ Gbps speeds, limited range                            │
├─────────────────────────────────────────────────────────────┤
│  Mid-Band / Ultra Capacity 5G (2.5 GHz, 1.9 GHz, 2.1 GHz)  │
│  • Speed + coverage balance                                 │
│  • 300M+ people covered                                     │
│  • 100-400 Mbps typical speeds                              │
├─────────────────────────────────────────────────────────────┤
│  Low-Band (600 MHz)                                         │
│  • Nationwide coverage                                      │
│  • Building penetration                                     │
│  • 30-100 Mbps speeds, extends 4G coverage                  │
└─────────────────────────────────────────────────────────────┘
```

## Spectrum Portfolio

### Current Holdings

| Band | Frequency | Type | Use Case | Coverage |
|------|-----------|------|----------|----------|
| 600 MHz (n71) | 617-698 MHz | Low-band | Nationwide 5G | 325M+ people |
| 2.5 GHz (n41) | 2496-2690 MHz | Mid-band | Ultra Capacity 5G | 300M+ people |
| 1.9 GHz (n25) | 1850-1915 MHz | Mid-band | Capacity, indoor | Urban/suburban |
| 2.1 GHz (n66) | 2110-2155 MHz | Mid-band | Capacity supplement | Nationwide |
| 28 GHz (n261) | 27.5-28.35 GHz | mmWave | Ultra-dense capacity | Select venues |
| 39 GHz (n260) | 37-40 GHz | mmWave | Ultra-dense capacity | Select venues |

### Spectrum Depth Advantage

**Sub-6 GHz Spectrum per Million Subscribers:**
- T-Mobile: 3.1 MHz
- AT&T: 2.7 MHz
- Verizon: 2.1 MHz

*Source: T-Mobile Q4 2024 Earnings*

This 45% advantage over Verizon enables:
- Higher speeds during congestion
- Better indoor coverage
- More consistent performance
- Future capacity headroom

## Technical Specifications

### 5G Standalone (SA) Core

**Architecture:**
- Cloud-native, containerized core
- Multi-vendor environment (Nokia, Ericsson)
- Distributed edge computing capabilities
- Network slicing support

**Capabilities:**
- Ultra-low latency (<10ms end-to-end)
- Massive IoT support (mMTC)
- URLLC (Ultra-Reliable Low Latency Communications)
- Dynamic network resource allocation

### Radio Access Network (RAN)

**Macro Cell Specifications:**
- Carrier aggregation: Up to 5 carriers (5CA)
- MIMO: 64T64R massive MIMO on mid-band
- Beamforming: Dynamic beam management
- Cell range: 1-10 miles (depending on band)

**Small Cell Specifications:**
- Density: 41,000+ small cell/DAS sites
- mmWave small cells: Ultra-dense urban
- Indoor solutions: DAS, femtocells
- Backhaul: Fiber, microwave

### Speed Benchmarks

**Typical Performance (2024):**

| Network Type | Download | Upload | Latency |
|--------------|----------|--------|---------|
| 5G UC (n41) | 100-400 Mbps | 20-50 Mbps | 15-30ms |
| 5G Extended Range (n71) | 30-100 Mbps | 10-25 Mbps | 20-40ms |
| LTE Advanced | 20-80 Mbps | 5-20 Mbps | 30-50ms |
| mmWave (n261/n260) | 500 Mbps - 2 Gbps | 50-200 Mbps | 10-20ms |

*Note: Actual speeds vary by location, device, and network load*

## Network Performance Awards

### Opensignal (2024)
- 5G Availability
- 5G Coverage Experience
- 5G Download Speed
- 5G Upload Speed
- 5G Video Experience
- 5G Live Video Experience
- 5G Games Experience
- 5G Voice App Experience

*5th consecutive year winning all categories*

### Ookla Speedtest Awards (2024)
- Fastest 5G Network in the US
- Most Consistent 5G Network
- Most Available 5G Network
- Best 5G Gaming Experience
- Best 5G Video Experience

### RootMetrics (2024)
- Top performer in multiple metro markets
- Strong reliability scores nationwide

## Network Infrastructure

### Physical Infrastructure

**Cell Sites:**
- Macro sites: 102,000+
- Small cells/DAS: 41,000+
- Total towers and structures: Industry-leading density

**Backhaul:**
- Fiber connections: Majority of sites
- Microwave: Rural and remote locations
- Capacity: 10Gbps+ per site (typical)

**Power & Resilience:**
- Battery backup: Standard 4-8 hours
- Generator backup: Critical sites
- Hardened sites: 1,375+ (disaster-resistant)

### Geographic Coverage

**5G Coverage (as of 2024):**
- Total 5G: 325M+ people (98% of US population)
- 5G Ultra Capacity: 300M+ people (90% of US population)
- Rural 5G: Significant expansion ongoing

**Coverage by State (Selected):**
- Florida: 100% 5G coverage (average 266.7 Mbps)
- California: Comprehensive UC 5G in metro areas
- Texas: Major metro and highway coverage
- New York: Full NYC metro + upstate expansion

## Advanced Features

### 5G Advanced Capabilities

**Carrier Aggregation:**
- 5G + 5G aggregation (n71 + n41)
- 5G + LTE aggregation (EN-DC)
- Dynamic spectrum sharing (DSS) where needed

**Network Slicing:**
- Enterprise private network slices
- Public safety priority slicing
- IoT optimized slices

**VoNR (Voice over New Radio):**
- 5G-native voice calling
- Improved voice quality (EVS codec)
- Faster call setup

### Emerging Technologies

**AI-RAN (2025+):**
- Partnership with NVIDIA, Ericsson, Nokia
- AI-powered network optimization
- Predictive capacity management
- Energy efficiency improvements

**Satellite Integration:**
- Starlink partnership for direct-to-cell
- Text messaging via satellite
- Emergency alerts and connectivity
- Expanding to voice and data

**Edge Computing:**
- Distributed edge nodes nationwide
- Ultra-low latency for applications
- Enterprise edge solutions

## Network Evolution Roadmap

### 2025 Priorities
1. **US Cellular Integration**: Expand coverage in rural markets
2. **Spectrum Expansion**: Deploy additional 2.5GHz carriers
3. **AI-RAN Deployment**: Begin AI-powered network optimization
4. **Satellite Service**: Expand Starlink text to voice/data

### 2026-2027 Targets
1. **5G-Advanced**: Full 3GPP Release 18 features
2. **Ultra Capacity Expansion**: 330M+ people coverage
3. **Fiber Integration**: Complement wireless with fiber where appropriate
4. **IoT Scale**: Massive machine-type communications deployment

## Competitive Comparison

### T-Mobile vs Verizon vs AT&T (5G)

| Metric | T-Mobile | Verizon | AT&T |
|--------|----------|---------|------|
| 5G Coverage | 325M+ | ~270M | ~285M |
| Ultra Capacity 5G | 300M+ | ~200M | ~175M |
| Avg Download Speed | 200+ Mbps | 150 Mbps | 120 Mbps |
| Spectrum Depth | 3.1 MHz/sub | 2.1 MHz/sub | 2.7 MHz/sub |
| 5G Awards (2024) | 15+ | 2-3 | 1-2 |

*Sources: Opensignal, Ookla, carrier reports*

## Key Network Statistics

**Daily Network Metrics:**
- Data traffic: Petabytes per day
- Voice minutes: Billions per day
- Text messages: Billions per day
- Connected devices: 100M+

**Reliability Metrics:**
- Network uptime: 99.99%+
- Call completion rate: 99%+
- Data session success: 98%+

---

*Last Updated: March 2025*
*Sources: T-Mobile technical documentation, FCC filings, third-party benchmarks*
