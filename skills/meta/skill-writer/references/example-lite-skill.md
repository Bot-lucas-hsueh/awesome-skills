# Example 1: Create Lite Skill

## Context

User wants a simple weather lookup skill that calls an API and returns formatted results.

## User Input

"Create a skill that gets weather information for a city. I want to use OpenWeatherMap API."

## Assessment

- Scope: Single capability (weather lookup)
- Complexity: Simple API wrapper
- Tier: **Lite** (50-150 lines)

## Created Skill

### SKILL.md (85 lines)

```markdown
---
name: weather-lookup
description: 'Get current weather for any city using OpenWeatherMap API. Triggers: "weather", "get weather", "what\'s the weather".'
license: MIT
metadata:
  author: user@example.com
  version: 1.0.0
  updated: '2026-03-22'
  tags: [weather, api, utility]
  tier: lite
---

# Weather Lookup

## One-Liner

Get current weather conditions for any city worldwide using OpenWeatherMap API.

---

## § 1 · System Prompt

You are a Weather Data Interface. Your job is to fetch and format weather information.

**API Details**:
- Endpoint: `api.openweathermap.org/data/2.5/weather`
- Free tier: 60 calls/minute, 1M calls/month
- Response format: JSON

**Output Format**:
- Temperature (°C/°F)
- Conditions (clear, rain, clouds, etc.)
- Humidity (%)
- Wind speed (m/s)

---

## § 2 · Usage

**Trigger**: "What's the weather in [city]?"

**Parameters**:
- `city` (required): City name
- `units` (optional): metric/imperial

---

## § 3 · Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| City not found | Invalid city name | Ask for clarification |
| API limit exceeded | >60 calls/min | Wait 1 minute |
| Network error | Connectivity | Retry once |

---

## § 4 · Example

**User**: "Weather in Tokyo"

**Response**:
```
Tokyo, JP: 18°C, partly cloudy
Humidity: 65%
Wind: 3.5 m/s NE
```
```

## Key Design Decisions

1. **Lite Tier**: Single capability, 85 lines
2. **Specific Data**: OpenWeatherMap API details, rate limits
3. **Error Handling**: Table with specific causes and solutions
4. **One Example**: Sufficient for Lite tier
5. **No §1.1/1.2/1.3**: Lite tier doesn't require full System Prompt structure
