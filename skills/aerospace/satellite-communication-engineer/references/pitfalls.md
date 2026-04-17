## § 10 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Forgetting Rain Fade in Ka-Band Budget
**❌ BAD**: Link budget calculated at clear-sky; deployed system fails in rain
```
# Wrong: ignoring rain fade entirely
C_N = EIRP + G_T - FSPL - k - BW  # Clear sky only
margin = C_N - required_C_N       # Margin looks fine... until rain
```
**✅ GOOD**: Apply ITU-R P.618 rain fade margin for target availability
```python
# Rain fade margin for 99.9% availability, Ka-band, CONUS mid-latitude
# from ITU-R P.618 tables
rain_fade_margin_dB = {
    "Ka": {20: 8.5, 30: 6.5, 40: 5.5, 50: 4.5, 60: 3.5},  # dB vs elevation angle°
    "Ku": {20: 4.0, 30: 3.0, 40: 2.5, 50: 2.0, 60: 1.5}
}
margin = clear_sky_margin - rain_fade_margin_dB["Ka"][elevation_deg]
# margin must be ≥ 1 dB for acceptable availability
```
**Why it matters**: Ka-band rain outages can be 8-12 dB at low elevation angles in tropical climates. Ignoring this makes the system unusable in heavy rain.

