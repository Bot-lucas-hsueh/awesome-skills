# Zoom Video Architecture Deep Dive

## System Overview

Zoom's video architecture is built for **massive scale** (300M+ daily participants) with **low latency** (<150ms) and **high reliability** (99.99% uptime). The foundation is a **Selective Forwarding Unit (SFU)** architecture that routes video without transcoding.

## Architecture Components

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                              │
│  (Web, Desktop, Mobile, Rooms, PSTN)                            │
└────────────────────────────┬────────────────────────────────────┘
                             │ WebSocket (Signaling)
                             │ UDP/TCP (Media)
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                     MEDIA ROUTING LAYER                          │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │           SFU (Selective Forwarding Unit)               │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐              │   │
│  │  │ Video    │  │ Audio    │  │ Screen   │              │   │
│  │  │ Router   │  │ Router   │  │ Share    │              │   │
│  │  └──────────┘  └──────────┘  └──────────┘              │   │
│  │                                                         │   │
│  │  • Receives all participant streams                    │   │
│  │  • Routes to appropriate recipients                    │   │
│  │  • No transcoding (CPU efficient)                      │   │
│  │  • SVC layer selection                                 │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                   INFRASTRUCTURE LAYER                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Data Centers │  │ Cloud Burst  │  │ Load Balancer│          │
│  │ (13+ Global) │  │ (AWS/Oracle) │  │ (Geo-DNS)    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

## SFU vs MCU Architecture

### Multipoint Control Unit (MCU)

```
MCU Approach:
┌─────────┐
│ Alice   │───┐
│ 720p    │   │    ┌──────────┐    ┌─────────┐
└─────────┘   ├───→│  Server  │───→│ Alice   │
              │    │  (MCU)   │    │ 720p    │
┌─────────┐   │    │          │    └─────────┘
│  Bob    │───┤    │ • Decode │
│ 720p    │   │    │ • Mix    │    ┌─────────┐
└─────────┘   │    │ • Encode │───→│  Bob    │
              │    └──────────┘    │ 720p    │
┌─────────┐   │                      └─────────┘
│  Carol  │───┘                      ┌─────────┐
│ 720p    │─────────────────────────→│ Carol   │
└─────────┘                          │ 720p    │
                                     └─────────┘

Characteristics:
• Server CPU: Very High (decode + mix + encode)
• Bandwidth: Low per participant (single stream)
• Latency: Higher (server processing time)
• Scale: Limited (~100 participants)
• Quality: Uniform (everyone gets same)
```

### Selective Forwarding Unit (SFU)

```
SFU Approach (Zoom's Choice):
┌─────────┐
│ Alice   │───┐
│ SVC     │   │    ┌──────────┐    ┌─────────┐
└─────────┘   ├───→│  Server  │───→│ Alice   │
              │    │  (SFU)   │    │ 720p    │
┌─────────┐   │    │          │    └─────────┘
│  Bob    │───┤    │ • Route  │
│ SVC     │   │    │ • Select │    ┌─────────┐
└─────────┘   │    │   layers │───→│  Bob    │
              │    └──────────┘    │ 360p    │
┌─────────┐   │                      └─────────┘
│  Carol  │───┘                      ┌─────────┐
│ SVC     │─────────────────────────→│ Carol   │
└─────────┘                          │ 180p    │
                                     └─────────┘

Characteristics:
• Server CPU: Minimal (routing only)
• Bandwidth: Higher per participant (multiple streams)
• Latency: Lower (no server processing)
• Scale: 15x MCU (1,000+ participants)
• Quality: Adaptive (each gets appropriate quality)
```

## Scalable Video Coding (SVC)

### How SVC Works

SVC encodes a single video stream with multiple quality layers:

```
┌─────────────────────────────────────────────────────────┐
│                  SVC Stream Structure                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Layer 3 (Enhancement):  720p@30fps  ─────────────────  │
│  Layer 2 (Enhancement):  360p@30fps  ─────────          │
│  Layer 1 (Base):         180p@15fps  ───                │
│                                                         │
│  Total Bitrate: ~2.5 Mbps                               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Quality Adaptation

| Network Condition | Layers Used | Resolution | Bitrate |
|-------------------|-------------|------------|---------|
| Excellent (>5 Mbps) | All 3 | 720p@30fps | 2.5 Mbps |
| Good (2-5 Mbps) | Layers 1+2 | 360p@30fps | 1.0 Mbps |
| Fair (1-2 Mbps) | Layer 1 only | 180p@15fps | 0.5 Mbps |
| Poor (<1 Mbps) | Layer 1 + FEC | 180p@15fps | 0.5 Mbps |

## Media Transport Protocols

### WebRTC Stack

```
┌─────────────────────────────────────────────────────────┐
│                   APPLICATION LAYER                      │
│            (Zoom Client - JavaScript/C++/Swift)         │
├─────────────────────────────────────────────────────────┤
│                   SIGNALING LAYER                        │
│                 (WebSocket over TLS)                     │
├─────────────────────────────────────────────────────────┤
│                    WEBRTC STACK                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  getUserMedia│  │ RTCPeerConnection │  │ DataChannel │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│                   TRANSPORT LAYER                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │  RTP (Real-time Transport Protocol)              │   │
│  │  RTCP (RTP Control Protocol)                     │   │
│  ├─────────────────────────────────────────────────┤   │
│  │  DTLS (Datagram TLS) - Encryption               │   │
│  │  UDP (Primary) / TCP (Fallback)                 │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### ICE (Interactive Connectivity Establishment)

```
ICE Connection Process:

1. Host Candidates (Local IP)
   192.168.1.100:12345 ──────┐
                             │
2. Server Reflexive (STUN)   │
   Public IP discovered      │
   203.0.113.50:54321 ──────┤
                             ├──→ Best path selected
3. Relay (TURN)              │
   Via TURN server           │
   turn.zoom.us:3478 ────────┘
```

## Encryption & Security

### Transport Encryption (Standard)

```
┌─────────────────────────────────────────────────────────┐
│              AES-256 GCM Encryption                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Client ──[AES-256-GCM]──→ Zoom Server                 │
│                                                         │
│  • Keys managed by Zoom infrastructure                 │
│  • Industry-leading encryption standard                │
│  • Enables cloud recording, phone dial-in              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### End-to-End Encryption (Optional)

```
┌─────────────────────────────────────────────────────────┐
│              E2EE Cryptographic Design                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Key Exchange:  Curve25519 (Elliptic Curve)            │
│  Signing:       Ed25519 (EdDSA)                        │
│  Symmetric:     AES-256 GCM                            │
│  Key Derivation: HKDF (HMAC-based)                     │
│                                                         │
│  ┌─────────┐                    ┌─────────┐            │
│  │ Alice   │←──── E2EE ────────→│  Bob    │            │
│  │ (Host)  │   Direct Keys     │         │            │
│  └─────────┘                    └─────────┘            │
│                                                         │
│  ⚠️ Trade-offs: No cloud recording, no phone dial-in   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Network Adaptation

### Adaptive Bitrate Algorithm

```
Bandwidth Estimation Loop:

┌──────────┐     ┌───────────────┐     ┌──────────┐
│ Measure  │────→│   Estimate    │────→│  Adapt   │
│  RTT     │     │  Bandwidth    │     │ Quality  │
│  Loss    │     │  Available    │     │  Layer   │
│  Jitter  │     │               │     │          │
└──────────┘     └───────────────┘     └──────────┘
     ↑                                        │
     └────────────────────────────────────────┘
              Feedback Loop (every 100ms)
```

### Forward Error Correction (FEC)

| Network Condition | FEC Strategy | Redundancy |
|-------------------|--------------|------------|
| Stable (<1% loss) | None | 0% |
| Mild (1-3% loss) | Audio only | 20% |
| Moderate (3-5% loss) | Audio + Video base layer | 30% |
| Severe (>5% loss) | Aggressive FEC | 50% |

### Jitter Buffer Management

```
Jitter Buffer Adaptation:

Network jitter detected
        │
        ↓
┌───────────────┐
│  Low Jitter   │ → 100ms buffer (lower latency)
│  (<20ms var)  │
└───────────────┘
        │
        ↓
┌───────────────┐
│  Med Jitter   │ → 200ms buffer (balanced)
│  (20-50ms)    │
└───────────────┘
        │
        ↓
┌───────────────┐
│  High Jitter  │ → 400ms buffer (smooth playback)
│  (>50ms)      │
└───────────────┘
```

## Data Center Architecture

### Global Distribution

| Region | Data Centers | Latency Target |
|--------|--------------|----------------|
| Americas | 5+ | <50ms |
| EMEA | 4+ | <50ms |
| APAC | 4+ | <50ms |

### Traffic Routing

```
Geo-DNS Routing:

User in Tokyo
     │
     ↓
┌────────────┐
│ DNS Query  │
└────────────┘
     │
     ↓
┌────────────────────────┐
│  Anycast BGP           │
│  Route to nearest DC   │
│  → Tokyo Data Center   │
└────────────────────────┘
     │
     ↓
┌────────────────────────┐
│  Health Check          │
│  If Tokyo is healthy   │
│    → Route to Tokyo    │
│  If Tokyo is degraded  │
│    → Route to Singapore│
└────────────────────────┘
```

## Performance Targets

| Metric | Target | Measurement |
|--------|--------|-------------|
| **First Frame** | <2 seconds | Time to first video frame |
| **Join Time** | <10 seconds | Meeting entry to participation |
| **Latency** | <150ms | End-to-end media delay |
| **Audio Quality** | >4.5 MOS | Mean Opinion Score |
| **Video Quality** | >4.0/5 | User-reported quality |
| **Uptime** | 99.99% | Service availability |
| **Packet Loss Recovery** | <1% perceived | After FEC/retransmission |

## Scalability Metrics

| Resource | Pre-COVID | Peak COVID | Current |
|----------|-----------|------------|---------|
| Daily Participants | 10M | 300M+ | 300M+ |
| Concurrent Meetings | 1M | 30M+ | 20M+ |
| Peak Bandwidth | 100 Gbps | 3 Tbps | 2 Tbps |
| Data Center Capacity | 50% utilized | 90%+ | 60% |

## Client Architecture

### Platform Support

| Platform | Technology | Features |
|----------|------------|----------|
| **Web** | WebRTC, WebAssembly | Full functionality, no install |
| **Desktop (Win/Mac)** | C++ native | Best performance, E2EE |
| **Mobile (iOS/Android)** | Native (Swift/Kotlin) | Optimized for mobile networks |
| **Rooms** | Custom hardware | Dedicated meeting room experience |
| **PSTN** | SIP trunking | Phone dial-in/out |

### Video Pipeline

```
Capture → Encode (SVC) → Encrypt → Packetize → Send
                                            ↑
Receive → Decrypt → Decode → Render ────────┘
         (Jitter Buffer)  (Display)
```
