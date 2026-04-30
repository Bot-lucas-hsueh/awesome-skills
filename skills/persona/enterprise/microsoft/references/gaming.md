# Microsoft Gaming Reference

## Xbox Division Overview

### Key Metrics
| Metric | Value |
|--------|-------|
| Game Pass Subscribers | 34M+ |
| Xbox Cloud Gaming Users | 100M+ monthly active |
| Xbox Live Users | 100M+ |
| Content & Services Revenue | Growing (part of $54.6B Personal Computing) |

### Acquisitions
| Company | Year | Price | Key Franchises |
|---------|------|-------|----------------|
| Mojang (Minecraft) | 2014 | $2.5B | Minecraft |
| ZeniMax Media | 2021 | $7.5B | Elder Scrolls, Fallout, Doom |
| Activision Blizzard | 2023 | $68.7B | Call of Duty, World of Warcraft, Candy Crush |

### First-Party Studios
- **30+ studios** across Xbox Game Studios, Bethesda, Activision Blizzard
- Notable franchises: Halo, Forza, Gears of War, Minecraft, Call of Duty, Overwatch, Diablo

## Xbox Cloud Gaming (xCloud)

### Technical Specs
| Spec | Value |
|------|-------|
| Streaming Quality | Up to 1080p 60fps |
| Latency Target | <20ms |
| Hardware | Custom Xbox Series X server blades |
| Regions | 54 Azure regions |
| Games | 400+ titles |
| Touch Controls | 150+ games |

### Architecture
```
User Device (Phone/PC/Console)
    ↓
Azure Edge POP (nearest location)
    ↓
Custom Xbox Series X Server Blade
├── Game execution
├── Video encoding
└── Input processing
    ↓
Game Streaming (H.264/AV1)
```

### Game Pass Tiers
| Tier | Price | Cloud Gaming |
|------|-------|--------------|
| Game Pass Core | $9.99/month | No |
| Game Pass Console | $10.99/month | No |
| Game Pass PC | $9.99/month | No |
| Game Pass Ultimate | $16.99/month | Yes |

## Developer Platform

### Xbox GDK (Game Development Kit)
- Unified development environment
- PC and Xbox targeting
- Integrated debugging
- Performance profiling

### ID@Xbox
- Independent developer program
- Free development kits
- Publishing support
- Marketing assistance

### Azure PlayFab
- Live game services backend
- Player authentication
- Leaderboards
- Multiplayer servers
- Analytics

## Cross-Platform Strategy

### Play Anywhere
- Buy once, play on Xbox and PC
- Shared save files
- Cross-play multiplayer

### Cloud Saves
- Automatic synchronization
- Cross-device continuity

### Xbox App
- PC game downloads
- Cloud gaming access
- Social features
- Game Pass discovery

---

**Last Updated**: 2026-03-21
