# Verizon 5G Technical Specifications

## 5G Spectrum Portfolio

### C-Band (3.7-3.98 GHz)
| Attribute | Specification |
|-----------|---------------|
| **Band** | n77 |
| **Spectrum Acquired** | 161 MHz average nationwide (140-200 MHz per market) |
| **Auction Cost** | $52.9 billion (2021) |
| **Coverage** | 250M+ people by end of 2024 |
| **Use Case** | Primary 5G coverage layer, suburban/rural |
| **Typical Speeds** | 100-400 Mbps down, 20-50 Mbps up |
| **Latency** | <20ms typical, <10ms edge optimized |

### mmWave (28 GHz, 39 GHz)
| Attribute | Specification |
|-----------|---------------|
| **Bands** | n260, n261 |
| **Coverage** | Dense urban, stadiums, airports, venues |
| **Use Case** | High-capacity zones, FWA dense urban |
| **Typical Speeds** | 1-4 Gbps down, 100+ Mbps up |
| **Latency** | <10ms, <5ms with MEC |
| **Range** | ~1,000 feet typical |

### Low-Band (700 MHz, 850 MHz)
| Attribute | Specification |
|-----------|---------------|
| **Use Case** | Nationwide coverage layer |
| **Characteristics** | Building penetration, rural coverage |
| **Typical Speeds** | 25-75 Mbps (comparable to good 4G) |

## 5G Network Architecture

### RAN (Radio Access Network)
```
┌─────────────────────────────────────────────────────────────┐
│                    5G RAN Architecture                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│  │   gNodeB    │    │   gNodeB    │    │   gNodeB    │      │
│  │  (Macro)    │    │  (Small)    │    │  (mmWave)   │      │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘      │
│         │                  │                  │              │
│         └──────────────────┼──────────────────┘              │
│                            │                                │
│         ┌──────────────────┴──────────────────┐             │
│         │      Front Haul (eCPRI/25G+)        │             │
│         └──────────────────┬──────────────────┘             │
│                            │                                │
│  ┌─────────────────────────┴─────────────────────────┐       │
│  │               DU (Distributed Unit)               │       │
│  │         RLC/MAC/PHY layer processing              │       │
│  └─────────────────────────┬─────────────────────────┘       │
│                            │                                │
│         ┌──────────────────┴──────────────────┐             │
│         │       Mid Haul (F1/10G+)            │             │
│         └──────────────────┬──────────────────┘             │
│                            │                                │
│  ┌─────────────────────────┴─────────────────────────┐       │
│  │                CU (Central Unit)                  │       │
│  │           RRC/PDCP layer processing               │       │
│  └─────────────────────────┬─────────────────────────┘       │
│                            │                                │
│         ┌──────────────────┴──────────────────┐             │
│         │      Back Haul (IP/MPLS/100G+)      │             │
│         └──────────────────┬──────────────────┘             │
│                            │                                │
│                    ┌───────┴───────┐                        │
│                    │    5G Core    │                        │
│                    └───────────────┘                        │
└─────────────────────────────────────────────────────────────┘
```

### 5G Core (5GC) Components

| Component | Function | Vendor |
|-----------|----------|--------|
| **AMF** | Access and Mobility Management | Ericsson/Samsung |
| **SMF** | Session Management | Ericsson/Samsung |
| **UPF** | User Plane Function (packet routing) | Ericsson/Samsung |
| **PCF** | Policy Control Function | Ericsson/Samsung |
| **UDM** | Unified Data Management | Ericsson/Samsung |
| **AUSF** | Authentication Server Function | Ericsson/Samsung |
| **NRF** | NF Repository Function | Ericsson/Samsung |

## Key Performance Indicators (KPIs)

### Radio KPIs
| KPI | Target | Measurement |
|-----|--------|-------------|
| **RSRP** | >-90 dBm (good), >-100 dBm (acceptable) | Reference Signal Received Power |
| **RSRQ** | >-10 dB (good), >-15 dB (acceptable) | Reference Signal Received Quality |
| **SINR** | >20 dB (good), >10 dB (acceptable) | Signal to Interference + Noise Ratio |
| **Throughput** | >100 Mbps (C-band), >1 Gbps (mmWave) | DL/UL speed test |
| **Latency** | <20ms (RAN), <10ms (edge) | RTT measurement |

### Network KPIs
| KPI | Target | Critical Threshold |
|-----|--------|-------------------|
| **Availability** | 99.999% | <99.99% triggers investigation |
| **Call Setup Success** | >99.5% | <99% triggers escalation |
| **Handover Success** | >98% | <95% triggers optimization |
| **Packet Loss** | <0.1% | >0.5% triggers investigation |
| **Jitter** | <5ms | >10ms triggers QoS review |

## Deployment Phases

### Phase 1: NSA (Non-Standalone)
- Uses 4G EPC (Evolved Packet Core)
- 5G NR for user plane only
- Control plane on LTE
- Faster initial deployment

### Phase 2: SA (Standalone)
- Full 5G Core (5GC)
- Control plane on 5G
- Network slicing enabled
- Lower latency capabilities

### Phase 3: Advanced 5G
- Full network slicing
- URLLC (Ultra-Reliable Low Latency)
- mMTC (Massive Machine Type Communication)
- 5G-Advanced features

## Equipment Vendors

| Vendor | Equipment Type | Deployment |
|--------|---------------|------------|
| **Ericsson** | RAN (Radio), Core | Primary nationwide |
| **Samsung** | RAN (vRAN), Core | Select markets |
| **Nokia** | RAN, Core | Secondary vendor |
| **Cisco** | Transport, Core IP | Backbone infrastructure |
| **Juniper** | Transport, Core IP | Backbone infrastructure |

## Security Specifications

### Encryption
| Layer | Algorithm | Key Length |
|-------|-----------|------------|
| **Air Interface** | AES-256 | 256-bit |
| **Backhaul** | MACsec/IPsec | 256-bit |
| **Core** | TLS 1.3 | 256-bit |

### Authentication
- 5G AKA (Authentication and Key Agreement)
- EAP-AKA' for non-3GPP access
- SUCI (Subscription Concealed Identifier) for privacy

## Private 5G Specifications

### Spectrum Options
| Option | Spectrum | Use Case |
|--------|----------|----------|
| **CBRS** | 3.55-3.7 GHz (n48) | General enterprise, shared spectrum |
| **Licensed** | C-band (n77) | Large enterprises, guaranteed QoS |
| **mmWave** | 28/39 GHz | Dense indoor, high capacity |

### MEC (Multi-access Edge Computing)
| Parameter | Specification |
|-----------|---------------|
| **Latency** | <10ms application latency |
| **Compute** | Kubernetes-based edge cloud |
| **Storage** | NVMe SSD, distributed |
| **Connectivity** | Direct 5G anchor, local breakout |

## References

- 3GPP TS 38.300 (NR; NR and NG-RAN Overall Description)
- 3GPP TS 23.501 (5G System Architecture)
- Verizon Technical Standards (internal)
- O-RAN Alliance Specifications
