# Anti-Patterns

## Architecture Anti-Patterns

### 1. MCU at Scale

**The Pattern:** Using Multipoint Control Unit (MCU) architecture for meetings >100 participants.

**Why It's Wrong:**
```
MCU with 100 participants:
├── Server CPU: 100 × 600 units = 60,000 CPU units
├── Latency: 50-100ms added per hop
├── Cost: Prohibitive at scale
└── Failure mode: Cascading degradation

SFU with 100 participants:
├── Server CPU: 100 × 15 units = 1,500 CPU units (40x better)
├── Latency: 5-10ms (10x better)
├── Cost: Manageable
└── Failure mode: Graceful quality reduction
```

**The Fix:**
- Migrate to SFU architecture
- Implement SVC (Scalable Video Coding)
- Move complexity to clients (decode multiple streams)
- Use active speaker detection to optimize bandwidth

---

### 2. Stateful Video Servers

**The Pattern:** Storing session state on video routing servers.

**Why It's Wrong:**
```
Stateful Server Problem:
┌─────────────┐
│ User A      │────┐
│ Connected   │    │
│ to Server 1 │    │     Server 1 fails
└─────────────┘    │           │
                   │           ↓
┌─────────────┐    │     ┌─────────────┐
│ User B      │────┼────→│   Server 2  │
│ Connected   │    │     │  (No state) │
│ to Server 1 │────┘     └─────────────┘
└─────────────┘                  │
                          Meeting DROPS
                          State lost
                          Must reconnect
```

**The Fix:**
```
Stateless Server Solution:
┌─────────────┐
│ User A      │────┐
│ State in    │    │
│ Redis       │    │     Server 1 fails
└─────────────┘    │           │
                   │           ↓
┌─────────────┐    │     ┌─────────────┐     ┌─────────┐
│ User B      │────┼────→│   Server 2  │────→│  Redis  │
│ State in    │    │     │ (Fetches    │     │ (Shared │
│ Redis       │────┘     │  state)     │     │  state) │
└─────────────┘          └─────────────┘     └─────────┘
                                │
                          Meeting CONTINUES
                          Seamless failover
```

---

### 3. Ignoring Packet Loss

**The Pattern:** Treating packet loss as someone else's problem.

**Why It's Wrong:**
- Video freezes without recovery
- Audio dropouts ruin communication
- Users blame the product, not their network
- No graceful degradation

**The Fix:**
```python
# Implement Forward Error Correction (FEC)
class PacketLossRecovery:
    def __init__(self):
        self.fec_enabled = True
        
    def calculate_fec_rate(self, loss_rate):
        """Dynamic FEC based on network conditions"""
        if loss_rate < 0.01:
            return 0  # No loss, no FEC
        elif loss_rate < 0.03:
            return 0.15  # 15% redundancy
        elif loss_rate < 0.05:
            return 0.25  # 25% redundancy
        else:
            return 0.40  # 40% redundancy (aggressive)
            
    def apply_fec(self, media_packets, loss_rate):
        fec_rate = self.calculate_fec_rate(loss_rate)
        # Generate XOR-based FEC packets
        return media_packets + self.generate_fec_packets(
            media_packets, fec_rate
        )
```

---

### 4. Vertical Scaling Only

**The Pattern:** Buying bigger servers instead of adding more.

**Why It's Wrong:**
- Hardware limits (can't scale infinitely)
- Expensive (enterprise-grade servers)
- Single point of failure
- Long procurement cycles

**The Fix:**
```
Horizontal Scaling Approach:

Instead of:
  1 server: 64 cores, 256GB RAM ($50,000)
  
Use:
  16 servers: 4 cores, 16GB RAM each ($3,000 × 16 = $48,000)
  + Load balancer ($2,000)
  
Benefits:
  ✓ Scale by adding servers
  ✓ Fault tolerance (N-1 redundancy)
  ✓ Gradual capacity increase
  ✓ Use commodity hardware
```

---

### 5. Security as Afterthought

**The Pattern:** Adding encryption after product launch.

**Why It's Wrong:**
- Fundamental redesign often required
- Vulnerabilities in legacy code paths
- User trust permanently damaged
- Compliance violations

**The Fix:**
```
Security-First Development:

Design Phase:
□ Threat modeling completed
□ Encryption requirements defined
□ Compliance checklist (SOC 2, GDPR, HIPAA)
□ Security review gate

Implementation:
□ Secure coding standards enforced
□ SAST/DAST in CI/CD
□ Penetration testing before launch
□ Bug bounty program active

Operations:
□ Security monitoring 24/7
□ Incident response plan tested
□ Regular security audits
□ Vulnerability disclosure process
```

---

## Implementation Anti-Patterns

### 6. Synchronous Blocking Calls

**The Pattern:** Making blocking I/O calls in the video pipeline.

**Why It's Wrong:**
```python
# WRONG: Blocking database call in video path
def process_video_frame(frame):
    # This blocks the video pipeline!
    user_settings = db.query("SELECT * FROM users WHERE id = ?", user_id)
    apply_settings(frame, user_settings)
    return frame
    
# Result: Frame drops, stuttering video
```

**The Fix:**
```python
# RIGHT: Async or pre-fetched data
async def process_video_frame(frame):
    # Use cached settings, fetch async if needed
    user_settings = await cache.get_async(user_id)
    apply_settings(frame, user_settings)
    return frame

# Or pre-fetch:
class VideoProcessor:
    def __init__(self):
        self.settings_cache = {}
        
    async def prefetch_settings(self, user_ids):
        """Fetch before video processing starts"""
        settings = await db.query_many(user_ids)
        self.settings_cache.update(settings)
        
    def process_frame(self, frame):
        # Non-blocking cache access
        settings = self.settings_cache.get(user_id)
        apply_settings(frame, settings)
        return frame
```

---

### 7. Hardcoded Limits

**The Pattern:** Embedding magic numbers throughout the codebase.

**Why It's Wrong:**
- Can't adapt to different scenarios
- Code scattered everywhere
- No centralized configuration
- Requires redeploy to change

**The Fix:**
```python
# WRONG: Hardcoded limit
if participants > 100:  # Magic number
    reject_join()

# RIGHT: Configurable limit
from config import MAX_MEETING_SIZE

if participants > MAX_MEETING_SIZE:
    reject_join()
    
# config.py
class Config:
    MAX_MEETING_SIZE = int(os.getenv('MAX_MEETING_SIZE', 100))
    DEFAULT_VIDEO_QUALITY = os.getenv('DEFAULT_VIDEO_QUALITY', '720p')
    JITTER_BUFFER_MIN_MS = int(os.getenv('JITTER_BUFFER_MIN_MS', 100))
    
# Feature flags for gradual rollout
if feature_flags.is_enabled('increased_meeting_size'):
    max_size = 1000
else:
    max_size = 100
```

---

### 8. No Observability

**The Pattern:** Shipping code without metrics, logs, or tracing.

**Why It's Wrong:**
- Can't debug production issues
- No performance visibility
- Blind to user experience
- Reactive instead of proactive

**The Fix:**
```python
from opentelemetry import trace
from prometheus_client import Histogram, Counter

# Metrics
join_time = Histogram('meeting_join_seconds', 'Time to join meeting')
error_count = Counter('video_errors_total', 'Total video errors', ['type'])

# Tracing
tracer = trace.get_tracer(__name__)

class MeetingService:
    @join_time.time()
    def join_meeting(self, meeting_id, user_id):
        with tracer.start_as_current_span("join_meeting") as span:
            span.set_attribute("meeting.id", meeting_id)
            span.set_attribute("user.id", user_id)
            
            try:
                # ... join logic ...
                span.set_attribute("join.success", True)
                
            except Exception as e:
                span.set_attribute("join.success", False)
                span.set_attribute("error.message", str(e))
                error_count.labels(type=type(e).__name__).inc()
                raise
```

---

## Product Anti-Patterns

### 9. AI Without Context

**The Pattern:** Generic AI integration without leveraging Zoom's context.

**Why It's Wrong:**
```
Generic AI Response:
User: "What did we decide?"
AI: "I'm not sure which meeting you're referring to."

Result: Useless, frustrating experience
```

**The Fix:**
```
Context-Aware AI:
User: "What did we decide?"
AI: "In your current meeting 'Q1 Planning' (2:30 PM today), 
      the team decided:
      1. Budget cap: $500K
      2. Launch date: March 1
      3. Vendor selection by Feb 15"

Implementation:
├── Meeting transcript (real-time)
├── Participant list
├── Meeting title/agenda
├── Previous related meetings
├── Calendar context
└── User's role in meeting
```

---

### 10. Breaking E2EE for AI

**The Pattern:** Processing encrypted content for AI features.

**Why It's Wrong:**
- Violates end-to-end encryption promise
- Privacy breach
- Legal/compliance violations
- Trust destruction

**The Fix:**
```
E2EE-Respecting AI Design:

Meeting Type: E2EE
├── AI Companion: DISABLED
├── Recording: DISABLED  
├── Transcription: DISABLED
└── User notification: "AI features unavailable in E2EE"

Meeting Type: Standard
├── AI Companion: ENABLED (with consent)
├── Recording: Available
├── Transcription: Available
└── Privacy controls: Admin configurable

Clear Distinction:
┌─────────────┐    ┌─────────────┐
│   E2EE 🔒   │    │  Standard   │
│             │    │             │
│ No AI       │    │ AI Available│
│ No Recording│    │ Recording   │
│ Maximum     │    │ Balanced    │
│ Privacy     │    │ Features    │
└─────────────┘    └─────────────┘
```

---

## Process Anti-Patterns

### 11. Big Bang Deployment

**The Pattern:** Deploying to 100% of users at once.

**Why It's Wrong:**
- No rollback opportunity if issues found
- Affects all users simultaneously
- High stress, high risk
- Difficult to debug

**The Fix:**
```
Progressive Deployment:

Day 1: Canary (1% of traffic)
       ↓
       Monitor for 24 hours
       ↓
Day 2: 5% rollout
       ↓
       Monitor for 24 hours  
       ↓
Day 3: 25% rollout
       ↓
       Monitor for 24 hours
       ↓
Day 4: 100% rollout
       ↓
       Monitor continuously

Rollback triggers:
- Error rate > 0.1%
- Latency p99 > threshold
- Customer complaints spike
- Any SEV-2 or above incident
```

---

### 12. No Capacity Planning

**The Pattern:** Waiting for outages to scale.

**Why It's Wrong:**
- Reactive firefighting
- Poor user experience
- Emergency scaling costs more
- Team burnout

**The Fix:**
```
Proactive Capacity Planning:

Weekly:
├── Review growth trends
├── Project next 30 days
├── Identify bottlenecks
└── Order capacity if needed

Monthly:
├── 10x scenario planning
├── Cost optimization review
├── Performance regression check
└── Update capacity runbooks

Quarterly:
├── Architecture review
├── Scale testing
├── Disaster recovery drill
└── Budget planning

Always maintain:
├── 50% headroom minimum
├── Cloud burst agreements
├── Auto-scaling policies
└── On-call rotation
```

---

## Summary Table

| Anti-Pattern | Impact | Fix Priority |
|--------------|--------|--------------|
| MCU at Scale | High cost, poor scale | Critical |
| Stateful Servers | Single point of failure | Critical |
| Ignoring Packet Loss | Poor quality | High |
| Vertical Scaling Only | Scale ceiling | High |
| Security Afterthought | Compliance risk | Critical |
| Blocking Calls | Performance issues | Medium |
| Hardcoded Limits | Inflexibility | Medium |
| No Observability | Blind operations | High |
| AI Without Context | Poor UX | Medium |
| Breaking E2EE | Trust destruction | Critical |
| Big Bang Deploy | High risk | High |
| No Capacity Planning | Outages | Critical |
