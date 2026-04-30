# Riot Esports Manager — Broadcast Production Guide

Full reference for §7.3 (Fan Engagement) and §3 (Broadcast Technical Failure Risk).

## Multi-Language Production Stack

| Language | Region | Production Type | Observer Priority |
|----------|--------|----------------|------------------|
| English | Global / NA / OCE | Primary feed | Main cast |
| Korean | LCK | Primary + Global | Main cast |
| Mandarin | LPL | Primary + CN | Main cast |
| Spanish | LATAM / LLA | Co-stream | Backup observer |
| Portuguese | BR | Co-stream | Backup observer |
| Japanese | LJL | Co-stream | Backup observer |

## OBS Multi-Stream Setup

```
Main Output (1080p60, 8000kbps) → Primary CDN
├── Dedicated observer PC (RTX 4090, 32GB RAM)
├── Dual PC setup (game PC + stream PC)
├── NDI to secondary encoder
└── Backup: Local recording + cloud upload

Co-Stream Output (720p30, 3000kbps) → Partner platforms
├── In-game spectate mode
├── Low-latency delay (<3s)
└── Caster overlay template
```

## Observer Tool Configuration

### Camera Priority Hierarchy
```
1. Teamfight action (always top priority)
2. Key player perspective (ADC, jungler in moba)
3. Strategic overview (for map-level analysis)
4. Spectator reactions (camera cut to bench during pauses)
5. Crowd / venue (cultural moments)
```

### Production Checklist (Pre-Show)
- [ ] Stream test (all platforms, 30 min before)
- [ ] Audio mix check (game audio + caster + sound effects balanced)
- [ ] Observer communication channel open
- [ ] Replay system tested
- [ ] Technical director briefed on game flow
- [ ] Backup stream ready (at 10% quality)

## Disaster Recovery Protocol

| Failure Type | Detection | Recovery Time | Action |
|-------------|-----------|-------------|--------|
| Main stream outage | Auto-alert (30s) | <60s | Switch to backup encoder |
| Observer crash | TD verbal (10s) | <30s | Reconnect; if fail, restart client |
| Audio loss | Monitoring (15s) | <45s | Backup audio source |
| CDN failure | Regional monitoring | <3 min | Failover CDN; notify community |
| Full broadcast failure | Emergency alert | <5 min | Host standby + social comms |

**Community Communication Template:**
> "We're experiencing technical difficulties with the broadcast. Our team is actively working to restore service. Estimated resolution: [X] minutes. Updates will be posted every [Y] minutes on [Twitter account]."
