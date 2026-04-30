# Charter Communications - Technical Reference

## DOCSIS Technology

### DOCSIS Evolution Comparison

| Feature | DOCSIS 3.0 | DOCSIS 3.1 | DOCSIS 4.0 |
|---------|------------|------------|------------|
| **Downstream** | 1 Gbps | 10 Gbps | 10 Gbps |
| **Upstream** | 100-200 Mbps | 1-2 Gbps | 6 Gbps |
| **Spectrum** | 1.2 GHz | 1.2 GHz | 1.8 GHz |
| **Technology** | Channel bonding | OFDM/OFDMA | FDX + ESD |
| **Latency** | ~10ms | ~5ms | <2ms |
| **Status** | Legacy | Current | Deploying |

### DOCSIS 3.1 Details

**Downstream (OFDM):**
- Frequency range: 108-1218 MHz (expandable to 1794 MHz)
- Channel bandwidth: Up to 192 MHz per channel
- Modulation: 4096-QAM (up to 16384-QAM)
- Multiple channels can be bonded

**Upstream (OFDMA):**
- Standard: 5-42 MHz (sub-split)
- Mid-split: 5-85 MHz
- High-split: 5-204 MHz
- Channel bandwidth: 6.4 MHz min, 96 MHz max
- Modulation: Up to 4096-QAM

**Charter's DOCSIS 3.1 Deployment:**
- Coverage: 100% of footprint
- Standard downstream: Up to 1 Gbps
- With high-split upstream: Up to 200 Mbps
- Target for multi-gig: DOCSIS 4.0 by 2027

### DOCSIS 4.0 (Full Duplex + Extended Spectrum)

**Extended Spectrum DOCSIS (ESD):**
- Downstream: Up to 1.8 GHz
- Upstream: Up to 684 MHz (separate bands)
- Symmetrical multi-gigabit capability

**Full Duplex DOCSIS (FDX):**
- Same frequency for upstream and downstream
- 108-684 MHz flexible band
- Requires new CPE and plant upgrades
- Charter evaluating both ESD and FDX

**Charter's DOCSIS 4.0 Roadmap:**
- Phase 1 (2024-2025): High-split preparation
- Phase 2 (2025-2026): Select market trials
- Phase 3 (2026-2027): Full deployment
- Target: Multi-gigabit symmetrical by 2027

## Network Architecture

### HFC Frequency Plan

```
Frequency Allocation (Standard):

5-42 MHz:    ████████ Upstream (data return path)
54-550 MHz:  ████████████████████████ Analog/SDV video
550-750 MHz:  ████████████████ Digital video
750-1002 MHz:  ████████████████ DOCSIS 3.0 downstream
1002-1218 MHz:  ████████ DOCSIS 3.1 downstream

High-Split Upgrade:
5-204 MHz:   ████████████████████████ Upstream
204-1002 MHz: ████████████████████████ Downstream
```

### Distributed Access Architecture (DAA)

**Traditional Architecture:**
```
CMTS (Headend) → Fiber → Node → Coax → Customer
     ↑
  All PHY here
```

**DAA with Remote PHY:**
```
vCMTS (Headend) → Fiber (Ethernet/IP) → R-PHY Node → Coax → Customer
                    ↑                          ↑
                 MAC only                    PHY moved here
```

**Benefits:**
- Reduced headend space/power
- Better signal quality (digital fiber)
- Flexible capacity allocation
- Path to virtualization

### Node Splitting

**Objective:** Reduce homes per node to increase bandwidth per customer

| Homes/Node | Bandwidth/Customer | Use Case |
|------------|-------------------|----------|
| 500+ | ~2 Mbps | Legacy |
| 250 | ~4 Mbps | Standard |
| 100 | ~10 Mbps | Target |
| 64 | ~16 Mbps | High-density |

**Charter Node Split Program:**
- Priority: High-utilization markets
- Investment: Part of $11.3B annual CAPEX
- Target: 100 homes/node in competitive areas

## CPE Equipment

### Cable Modems

**Spectrum E31 (DOCSIS 3.1):**
- Chipset: Broadcom BCM3390
- Downstream: 32×8 SC-QAM + 2×OFDM
- Upstream: 8×SC-QAM + 2×OFDMA
- Max speed: 2.5 Gbps (hardware capable)
- LAN: 2.5 Gbps Ethernet port
- WiFi: Integrated AX (WiFi 6)

**Spectrum E31U (with Voice):**
- Same as E31 plus:
- 2-line eMTA for voice service
- Battery backup support

### WiFi Equipment

**Spectrum WiFi 6 Router:**
- Standard: 802.11ax
- Bands: 2.4 GHz + 5 GHz
- Streams: 4×4
- Features: OFDMA, MU-MIMO, Beamforming
- Security: WPA3

**Spectrum WiFi 6E Router:**
- Adds 6 GHz band
- Less congestion, more channels
- Target: Power users, multi-gig tiers

### Video Equipment

**Spectrum Receiver:**
- 4K capable
- DVR: 150+ hours HD storage
- Whole-home streaming
- Voice remote with search

**Apple TV 4K (TV Stream):**
- Used for IP-delivered video
- Spectrum app integration
- Siri remote
- No traditional cable required

## Signal Levels & Quality

### DOCSIS Signal Requirements

**Downstream (at modem):**
| Parameter | Target | Acceptable Range |
|-----------|--------|------------------|
| Power | -5 dBmV | -15 to +15 dBmV |
| SNR | >35 dB | >33 dB minimum |
| MER | >35 dB | >33 dB minimum |

**Upstream (at CMTS):**
| Parameter | Target | Acceptable Range |
|-----------|--------|------------------|
| Power | 35-45 dBmV | 30-51 dBmV |
| SNR | >25 dB | >20 dB minimum |

### Common Issues

**Low downstream power:**
- Cause: Excessive splitters, long drops
- Fix: Remove splitters, upgrade cable

**High upstream power:**
- Cause: Poor return path, noise
- Fix: Check connections, isolate noise sources

**Low SNR:**
- Cause: Interference, bad connectors
- Fix: Check grounding, replace connectors

## WiFi Hotspot Network

**Spectrum WiFi:**
- 30M+ access points nationwide
- Dual-band (2.4 GHz + 5 GHz)
- Customer gateways broadcast secondary SSID
- Separate VLAN for guest traffic

**Mobile Offload:**
- Spectrum Mobile devices auto-connect
- ~85% of mobile data via WiFi
- Reduces Verizon MVNO costs
- Improves indoor coverage

**Security:**
- Isolated from customer home network
- WPA2-Enterprise authentication
- Bandwidth throttled per connection
