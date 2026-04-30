# Example: SFU vs MCU Architecture Decision

## Context

**Decision Point (2012):** Designing the video architecture for group calls. Two main approaches exist:
- **MCU (Multipoint Control Unit)**: Server mixes all video streams
- **SFU (Selective Forwarding Unit)**: Server routes streams without transcoding

This was one of the most consequential architecture decisions in Zoom's history.

## Architecture Comparison

### MCU (Multipoint Control Unit)

```
MCU Architecture:

┌──────────┐
│  Alice   │──720p──┐
│ (Camera) │        │
└──────────┘        │
                    │
┌──────────┐        │      ┌──────────┐
│   Bob    │──720p──┼─────→│  Server  │
│ (Camera) │        │      │   MCU    │
└──────────┘        │      │          │
                    │      │ 1. Decode│
┌──────────┐        │      │ 2. Mix   │
│  Carol   │──720p──┘      │ 3. Encode│
│ (Camera) │               │          │
└──────────┘               └────┬─────┘
                                │
                    ┌───────────┼───────────┐
                    ↓           ↓           ↓
               ┌────────┐  ┌────────┐  ┌────────┐
               │  Alice │  │  Bob   │  │ Carol  │
               │  720p  │  │  720p  │  │  720p  │
               │(mixed) │  │(mixed) │  │(mixed) │
               └────────┘  └────────┘  └────────┘

Server Work Per Participant:
├── Decode: 720p@30fps = ~200 CPU units
├── Composite: Layout mixing = ~100 CPU units
├── Encode: 720p@30fps = ~300 CPU units
└── Total: ~600 CPU units per output stream

For 3 participants: 3 × 600 = 1,800 CPU units
For 100 participants: 100 × 600 = 60,000 CPU units
```

**MCU Pros:**
- Lower bandwidth per client (single stream)
- Works on low-power devices
- Easy to implement

**MCU Cons:**
- Massive server CPU requirements
- Higher latency (decode + encode time)
- Limited scale (~100 participants max)
- Expensive to operate

### SFU (Selective Forwarding Unit)

```
SFU Architecture (Zoom's Choice):

┌──────────┐
│  Alice   │──SVC──┐
│ (Camera) │720p   │
└──────────┘       │
                   │
┌──────────┐       │      ┌──────────┐
│   Bob    │──SVC──┼─────→│  Server  │
│ (Camera) │720p   │      │   SFU    │
└──────────┘       │      │          │
                   │      │ 1. Route │
┌──────────┐       │      │ 2. Select│
│  Carol   │──SVC──┘      │    layer │
│ (Camera) │720p          │          │
└──────────┘              └────┬─────┘
                               │
                    ┌──────────┼──────────┐
                    │          │          │
                    ↓          ↓          ↓
               ┌────────┐ ┌────────┐ ┌────────┐
               │  Alice │ │  Bob   │ │ Carol  │
               │ 720p   │ │ 360p   │ │ 180p   │
               │(Bob &  │ │(Alice &│ │(Alice  │
               │ Carol) │ │ Carol) │ │ & Bob) │
               └────────┘ └────────┘ └────────┘

Server Work Per Participant:
├── Routing: Packet forwarding = ~10 CPU units
├── Layer Selection: SVC layer choice = ~5 CPU units
└── Total: ~15 CPU units per stream

For 3 participants: 3 × 3 × 15 = 135 CPU units
For 100 participants: 100 × 100 × 15 = 150,000 CPU units
                   (but with 15x more capacity headroom)
```

**SFU Pros:**
- Minimal server CPU (routing only)
- Lower latency (no transcoding)
- Massive scale (1,000+ participants)
- Cost-effective
- Adaptive quality per participant

**SFU Cons:**
- Higher downstream bandwidth per client
- More client CPU (decode multiple streams)
- Requires SVC codec support

## Decision Analysis

### Quantitative Comparison

| Factor | MCU | SFU | Winner |
|--------|-----|-----|--------|
| **Server CPU / participant** | 600 units | 15 units | SFU (40x better) |
| **Latency** | 50-100ms added | 5-10ms added | SFU (10x better) |
| **Max participants** | ~100 | 1,000+ | SFU (10x better) |
| **Bandwidth (client)** | 2 Mbps | 4-6 Mbps | MCU (3x better) |
| **Client CPU** | Low | Moderate | MCU |
| **Implementation** | Simple | Complex | MCU |

### Zoom's Context (2012)

```
Market Conditions:
├── Bandwidth: Increasing (fiber, 4G emerging)
├── Device CPU: Rapidly improving (smartphones powerful)
├── Cloud Costs: Significant factor
├── Scale Ambitions: Massive (enterprise global)
└── Quality Focus: HD video required

Zoom's Bet:
├── Bandwidth will keep increasing ✓ (Correct)
├── Device CPU sufficient ✓ (Correct)
├── Server costs must be controlled ✓ (Correct)
└── Quality differentiation wins ✓ (Correct)
```

## Implementation Strategy

### Zoom's Hybrid Approach

```
Intelligent Client-Side Selection:

Server (SFU) receives:
├── Alice: SVC (180p/360p/720p layers)
├── Bob: SVC (180p/360p/720p layers)
└── Carol: SVC (180p/360p/720p layers)

Server forwards based on client capability:

Alice (High-end laptop, 10 Mbps):
├── Receives: Bob 720p, Carol 720p
└── Layout: Gallery view, high quality

Bob (Mid-range tablet, 5 Mbps):
├── Receives: Alice 360p, Carol 360p
└── Layout: Gallery view, medium quality

Carol (Low-end phone, 1 Mbps):
├── Receives: Alice 180p, Bob 180p
└── Layout: Active speaker focused

Bandwidth Optimization:
├── Total sent by each: 2.5 Mbps (SVC)
├── Total received varies by device
└── Server selects appropriate layers
```

### Active Speaker Detection

```
Bandwidth Optimization via Active Speaker:

Normal Layout (All Equal):
┌─────────┬─────────┐
│  Alice  │   Bob   │
│  360p   │  360p   │
├─────────┼─────────┤
│  Carol  │   Dan   │
│  360p   │  360p   │
└─────────┴─────────┘
Total received: 4 × 360p = ~4 Mbps

Active Speaker Layout (Bob speaking):
┌─────────────────┐
│       Bob       │
│      720p       │  ← High quality for speaker
├────────┬────────┤
│ Alice  │ Carol  │
│ 180p   │ 180p   │  ← Lower quality for others
└────────┴────────┘
Total received: 720p + 2 × 180p = ~2.5 Mbps
```

## Technical Implementation

### SVC Codec Configuration

```c
// VP8 SVC temporal layers configuration
typedef struct {
    int base_layer_bitrate;      // 300 kbps
    int enhancement_layer_1;     // +300 kbps (600 total)
    int enhancement_layer_2;     // +900 kbps (1.5 Mbps total)
    int temporal_layers;         // 3 layers (15/30fps)
} svc_config_t;

// Server layer selection logic
void select_layers(participant_t* dest, stream_t* source) {
    int available_bandwidth = dest->bandwidth_estimate;
    
    if (available_bandwidth > 1500) {
        source->selected_layers = ALL_LAYERS;      // 720p
    } else if (available_bandwidth > 700) {
        source->selected_layers = BASE + ENH_1;    // 360p
    } else {
        source->selected_layers = BASE_ONLY;       // 180p
    }
}
```

### Simulcast vs SVC

Zoom chose SVC over Simulcast:

```
Simulcast Approach:
├── Encode 3 separate streams (180p, 360p, 720p)
├── Send all 3 to server
├── Server picks one to forward
├── 3x encode cost on client
└── 3x upstream bandwidth

SVC Approach (Zoom's Choice):
├── Encode 1 stream with 3 layers
├── Send combined stream to server
├── Server picks layer to forward
├── 1.3x encode cost on client
└── 1x upstream bandwidth (more efficient)
```

## Trade-offs Accepted

### Higher Client Bandwidth

```
MCU Bandwidth (4 participants):
├── Upload: 2 Mbps (one stream)
├── Download: 2 Mbps (one mixed stream)
└── Total: 4 Mbps

SFU Bandwidth (4 participants):
├── Upload: 2.5 Mbps (one SVC stream)
├── Download: 6 Mbps (three 360p streams)
└── Total: 8.5 Mbps

Zoom's Assessment (2012):
├── "Bandwidth is increasing faster than server costs"
├── "4G and fiber will make this irrelevant"
└── Verdict: Acceptable trade-off ✓
```

### Higher Client CPU

```
MCU Client CPU:
├── Decode: 1 stream (mixed)
├── Composite: None (server does it)
└── Total: Low

SFU Client CPU:
├── Decode: 3+ streams (composited locally)
├── Composite: Local GPU/CPU
└── Total: Moderate

Zoom's Assessment (2012):
├── "Modern devices can handle 4+ video decodes"
├── "GPU acceleration increasingly available"
├── "Battery impact acceptable for quality"
└── Verdict: Acceptable trade-off ✓
```

## Results

### Scale Achievement

```
Zoom's SFU Performance:
├── Max participants per meeting: 1,000
├── COVID scale: 300M daily participants
├── Server efficiency: 15x vs MCU
└── Cost per participant: 1/10th of MCU approach
```

### Competitive Advantage

| Vendor | Architecture | Max Participants |
|--------|--------------|------------------|
| **Zoom** | SFU | 1,000 |
| **Microsoft Teams** | Hybrid | 1,000 (recently improved) |
| **Google Meet** | SFU | 500 |
| **Cisco WebEx** | MCU/SFU hybrid | 1,000 |

## Alternative Approaches

### Cascade SFU (Very Large Meetings)

For meetings >1,000 participants:

```
┌──────────┐
│  SFU 1   │───┐
│ (Host)   │   │
└──────────┘   │    ┌──────────┐
               ├───→│ Cascade  │
┌──────────┐   │    │   SFU    │
│  SFU 2   │───┘    │          │
│ (Region) │        │ Distributes│
└──────────┘        │ to sub-SFUs│
                    └──────────┘
                         │
                    ┌────┴────┐
                    ↓         ↓
               ┌────────┐ ┌────────┐
               │ SFU 3  │ │ SFU 4  │
               │(Users) │ │(Users) │
               └────────┘ └────────┘
```

## Lessons Learned

### What Worked

1. **Future-Proof Architecture**
   - Bandwidth did increase as predicted
   - Device CPU improved rapidly
   - 10-year-old decision still serving well

2. **Cost Efficiency**
   - Server costs remained manageable
   - Enabled free tier profitability
   - Competitive pricing advantage

3. **Quality Differentiation**
   - Adaptive quality became key feature
   - "It just works" reputation
   - Better than MCU competitors

### Challenges

1. **Mobile Optimization**
   - Early mobile clients struggled with CPU
   - Required codec optimization
   - Battery drain concerns

2. **Network Edge Cases**
   - Asymmetric bandwidth (fast down, slow up)
   - Corporate firewalls blocking UDP
   - Required TCP fallback

## Key Takeaways

1. **Bet on Technology Trends**
   - Bandwidth and CPU trends favored SFU
   - Don't over-optimize for current constraints

2. **Cost Structure Matters**
   - Server costs dominate at scale
   - Client resources are "free" (user pays)

3. **Quality is Differentiation**
   - Adaptive quality wins user satisfaction
   - Technical superiority becomes product superiority

4. **Architect for 10x**
   - SFU enabled 30x COVID growth
   - No architecture changes needed

## References

- [RFC 6190: RTP Payload Format for Scalable Video Coding](https://tools.ietf.org/html/rfc6190)
- [WebRTC SFU Architecture Guide](https://webrtc.org/getting-started/sfu-architecture)
- [Zoom Engineering Blog](https://blog.zoom.us)
- [Video Conferencing System Design (Design Gurus)](https://www.designgurus.io)
