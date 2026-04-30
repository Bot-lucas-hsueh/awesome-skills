# Example: Video Quality Optimization at 1 Mbps

## Scenario

**Context:** Enterprise customers in Asia-Pacific reporting pixelated video and audio dropouts during peak hours. Users are on 1 Mbps connections with 15% packet loss during network congestion.

**Business Impact:** 
- 23% increase in quality-related support tickets
- 3 enterprise deals at risk
- NPS score dropped from 72 to 68

## Analysis

### Initial State

```
Current Configuration:
├── Video: 720p@30fps requiring 2.5 Mbps
├── Audio: Stereo, 128kbps
├── Network: 1 Mbps available, 15% packet loss
├── Codec: H.264 (single layer)
└── Buffer: 100ms fixed

Problems:
├── Video: Severe degradation (insufficient bandwidth)
├── Audio: Occasional dropouts (bandwidth competition)
├── Packet Loss: No recovery mechanism
└── Latency: Buffer underruns causing freezes
```

### Root Cause Analysis

| Issue | Cause | Impact |
|-------|-------|--------|
| Pixelation | Bandwidth insufficient for 720p | Poor video quality |
| Audio dropouts | Video consuming all bandwidth | Communication breakdown |
| Frozen video | Packet loss without FEC | Meeting disruption |
| High latency | Buffer underruns | Awkward conversation gaps |

## Solution

### Implementation Plan

```
Phase 1: SVC Encoding (Week 1)
├── Replace H.264 with VP8 SVC
├── Configure 3 quality layers:
│   ├── Layer 1 (Base): 180p@15fps, 300kbps
│   ├── Layer 2 (Enhancement): 360p@30fps, 600kbps
│   └── Layer 3 (Enhancement): 720p@30fps, 1.6Mbps
└── Deploy to canary region (APAC)

Phase 2: Adaptive Bitrate (Week 2)
├── Implement bandwidth estimation
├── Dynamic layer selection based on available bandwidth
└── Audio priority enforcement

Phase 3: FEC and Jitter Buffer (Week 3)
├── Add Forward Error Correction (20% redundancy)
├── Implement adaptive jitter buffer (100-400ms)
└── Audio-specific FEC (more aggressive)

Phase 4: Global Rollout (Week 4)
├── Deploy to all regions
├── Monitor metrics
└── Customer communication
```

### Technical Details

#### SVC Configuration

```javascript
// SVC Layer Configuration
const svcConfig = {
  layers: [
    {
      id: 0,
      resolution: { width: 320, height: 180 },
      frameRate: 15,
      bitrate: 300000,  // 300 kbps
      dependency: null  // Base layer, no dependency
    },
    {
      id: 1,
      resolution: { width: 640, height: 360 },
      frameRate: 30,
      bitrate: 600000,  // 600 kbps
      dependency: 0     // Depends on layer 0
    },
    {
      id: 2,
      resolution: { width: 1280, height: 720 },
      frameRate: 30,
      bitrate: 1600000, // 1.6 Mbps
      dependency: 1     // Depends on layer 1
    }
  ]
};

// Bandwidth-based layer selection
function selectLayer(availableBandwidth) {
  if (availableBandwidth > 2000000) {
    return 2; // Full 720p
  } else if (availableBandwidth > 1000000) {
    return 1; // 360p
  } else {
    return 0; // 180p base layer
  }
}
```

#### Adaptive Bitrate Algorithm

```python
class AdaptiveBitrateController:
    def __init__(self):
        self.current_layer = 0
        self.bandwidth_estimate = 1000000  # Start conservative
        self.loss_rate = 0
        
    def update_metrics(self, rtt, loss_rate, jitter):
        """Update network metrics every 100ms"""
        self.loss_rate = loss_rate
        
        # Estimate available bandwidth using GCC (Google Congestion Control)
        self.bandwidth_estimate = self.estimate_bandwidth(rtt, loss_rate)
        
        # Adjust video layer based on bandwidth
        self.adapt_layer()
        
    def adapt_layer(self):
        """Select appropriate SVC layer"""
        if self.bandwidth_estimate < 500000:  # < 500kbps
            self.current_layer = 0
            self.enable_audio_priority()
        elif self.bandwidth_estimate < 1200000:  # < 1.2Mbps
            self.current_layer = 1
        else:
            self.current_layer = 2
            
    def enable_audio_priority(self):
        """Ensure audio quality even when video degrades"""
        # Reserve 64kbps minimum for audio
        self.audio_bitrate = min(64000, self.bandwidth_estimate * 0.3)
        self.video_bitrate = self.bandwidth_estimate - self.audio_bitrate
```

#### Forward Error Correction

```python
class FECController:
    def __init__(self):
        self.fec_enabled = True
        self.redundancy_rate = 0.2  // 20% default
        
    def calculate_fec_rate(self, loss_rate):
        """Adjust FEC redundancy based on network conditions"""
        if loss_rate < 0.01:  // < 1% loss
            return 0  // No FEC needed
        elif loss_rate < 0.03:  // 1-3% loss
            return 0.15  // 15% redundancy
        elif loss_rate < 0.05:  // 3-5% loss
            return 0.25  // 25% redundancy
        else:  // > 5% loss
            return 0.40  // 40% redundancy (aggressive)
            
    def apply_fec(self, media_packets, loss_rate):
        """Generate FEC packets for recovery"""
        fec_rate = self.calculate_fec_rate(loss_rate)
        fec_packets = []
        
        for packet_group in self.group_packets(media_packets, 10):
            // XOR-based FEC for simplicity
            fec_packet = self.generate_xor_fec(packet_group)
            fec_packets.append(fec_packet)
            
        return media_packets + fec_packets
```

## Results

### Metrics Improvement

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Quality Complaints** | 23% ticket increase | 85% reduction | Major improvement |
| **Video MOS** | 2.8/5 | 4.2/5 | +50% |
| **Audio Dropouts** | 15% of calls | <1% of calls | -93% |
| **Meeting Completion Rate** | 87% | 97% | +10 points |
| **NPS Score** | 68 | 74 | +6 points |

### Bandwidth Efficiency

```
At 1 Mbps Connection:

Before:
├── Video Attempted: 2.5 Mbps (720p)
├── Video Actual: ~800kbps (degraded)
├── Audio: 128kbps
├── Total: ~930kbps
└── Quality: Poor (pixelated, frozen)

After:
├── Video: 600kbps (360p SVC layer 1)
├── Audio: 64kbps (priority guaranteed)
├── FEC: 130kbps (20% redundancy)
├── Total: ~800kbps
└── Quality: Good (smooth, consistent)
```

### CPU Impact

| Component | Before | After | Delta |
|-----------|--------|-------|-------|
| **Encode CPU** | 15% | 18% | +3% (SVC overhead) |
| **Decode CPU** | 12% | 14% | +2% (SVC decode) |
| **FEC CPU** | 0% | 2% | +2% (new) |
| **Total CPU** | 27% | 34% | +7% |

*Acceptable trade-off for significant quality improvement*

## Key Principles Applied

1. **SVC (Scalable Video Coding)**
   - Single stream provides multiple qualities
   - Server selects appropriate layer per participant
   - No transcode needed

2. **Adaptive Bitrate**
   - Real-time bandwidth estimation
   - Dynamic quality adjustment
   - Audio priority enforcement

3. **Forward Error Correction**
   - Recover lost packets without retransmission
   - Redundancy rate adapts to network
   - Audio gets more aggressive FEC

4. **Graceful Degradation**
   - Reduce quality before dropping calls
   - Maintain audio at all costs
   - Smooth transitions between layers

## Lessons Learned

### What Worked
- SVC encoding was the key enabler for quality at low bandwidth
- Audio priority ensured communication remained possible
- Adaptive FEC prevented the "death spiral" of retransmissions

### What Didn't
- Initial FEC at fixed 20% wasted bandwidth on good networks
- SVC added CPU overhead that affected older devices
- Layer switching too aggressively caused visible quality jumps

### Iterations Made
1. **Week 2:** Made FEC adaptive based on actual loss rate
2. **Week 3:** Added hysteresis to layer switching (prevent flickering)
3. **Week 4:** Optimized SVC encoder for mobile CPUs

## Rollout Strategy

| Region | Week | Notes |
|--------|------|-------|
| APAC (pilot) | 1 | Highest complaint volume |
| EMEA | 2 | Similar network conditions |
| Americas | 3 | Lower priority (better bandwidth) |
| Global | 4 | Full deployment |

## Related Documentation

- [SVC Technical Specification](https://tools.ietf.org/html/rfc6190)
- [WebRTC Bandwidth Estimation](https://webrtc.googlesource.com/src/+/refs/heads/main/modules/congestion_controller/)
- [Zoom's E2EE Whitepaper](https://zoom.us/security)
