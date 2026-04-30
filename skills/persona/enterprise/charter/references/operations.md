# Charter Communications - Operations Reference

## Network Architecture

### HFC Network Topology

```
[Headend/Hub] ←→ [Fiber] ←→ [Optical Node] ←→ [Coax] ←→ [Tap] ←→ [Home]
                    ↑              ↑              ↑           ↑
               Core network   500-2000 homes   4-8 homes    CPE
                              (node split
                               target: 100)
```

**Headend/Hub:**
- Central facility receiving video, internet, voice feeds
- CMTS (Cable Modem Termination System) management
- Power backup, cooling, security
- Hub consolidation ongoing (reduce from 1,000+ to ~400)

**Optical Node:**
- Converts fiber (optical) to coax (RF)
- Serves 100-500 homes (target 100 post-split)
- Hardened for outdoor environment
- Remote PHY: Moving PHY layer to node (DAA)

**Distribution Plant:**
- Trunk coax: 0.750" diameter, minimal taps
- Feeder: 0.500" diameter, primary distribution
- Drop: 0.375" diameter, individual homes
- Amplifiers every 1,500-2,000 feet

### Service Delivery Process

**Internet Activation:**
1. Provisioning system authorizes MAC address
2. DHCP assigns IP from regional pool
3. Speed profile applied (config file)
4. CMTS registers modem
5. Service active

**Video Activation:**
1. Conditional Access System (CAS) authorization
2. Entitlements pushed to CableCARD or box
3. Channel map delivered
4. VOD catalog available
5. DVR service (if subscribed) activated

**Mobile Activation:**
1. eSIM or physical SIM provisioned
2. Number port or new assignment
3. Verizon network profile pushed
4. WiFi calling enabled
5. Spectrum WiFi auto-connect configured

### Field Operations

**Technician Types:**
| Type | Specialization | Training |
|------|---------------|----------|
| Premises Tech | In-home installation/repair | 6 weeks |
| Lineman | Outside plant construction | 8 weeks |
| Drop Tech | Service drops, reconnects | 4 weeks |
| Network Tech | Headend, hub, node work | 12 weeks |
| WiFi Tech | Advanced home networking | 6 weeks + certs |

**Dispatch Priorities:**
1. **P1 - Outage**: Node down, multiple customers affected
2. **P2 - No Service**: Single customer total loss
3. **P3 - Impaired**: Degraded service (slow speeds, pixelation)
4. **P4 - Install**: New customer installation
5. **P5 - Upgrade**: Service changes, equipment swaps

**Key Metrics:**
- First Call Resolution: Target 90%
- Mean Time to Repair: <24 hours
- Schedule adherence: ±2 hours
- Repeat dispatch: <8%

### Customer Support Tiers

**Tier 0 - Self-Service:**
- My Spectrum app
- Online account management
- Automated troubleshooting
- Service outage maps
- Appointment scheduling

**Tier 1 - Technical Support:**
- Basic troubleshooting scripts
- Account lookup and verification
- Billing inquiries
- Schedule technician dispatch
- Equipment swaps by mail

**Tier 2 - Advanced Technical:**
- Signal level analysis
- CMTS diagnostics
- Network issue escalation
- Retention offers
- Complex billing resolution

**Tier 3 - Field Operations:**
- Premises technician dispatch
- Network maintenance
- Construction coordination
- Emergency response

### Service Quality Standards

**Internet Performance:**
| Metric | Standard | Measurement |
|--------|----------|-------------|
| Download speed | >95% of tier | Speedtest |
| Upload speed | >95% of tier | Speedtest |
| Latency | <50ms | Ping test |
| Packet loss | <1% | 24-hour monitoring |
| Jitter | <10ms | Real-time apps |
| Uptime | 99.9% | Monthly |

**Video Quality:**
- Channel availability: 99.99%
- VOD success rate: >95%
- Picture quality: No macroblocking
- Audio sync: ±40ms

**Voice Quality:**
- MOS score: >4.0
- Call completion: >99.5%
- E911: 100% availability

## Equipment Standards

**Modems (Customer Owned or Leased):**
| Model | Standard | Max Speed |
|-------|----------|-----------|
| Spectrum E31 | DOCSIS 3.1 | 1 Gbps |
| Spectrum E31U | DOCSIS 3.1 | 1 Gbps + Voice |
| Spectrum E31T | DOCSIS 3.1 | 1 Gbps + TV |

**Routers:**
- Spectrum Wave 2 (AC router)
- Spectrum WiFi 6 (AX router)
- Spectrum WiFi 6E (Tri-band)

**Video Equipment:**
- Spectrum Receiver (HD/DVR)
- Apple TV 4K (for TV Stream)
- CableCARD (for TiVo/3rd party)

**Mobile:**
- BYOD supported
- Spectrum Mobile devices
- eSIM capable
