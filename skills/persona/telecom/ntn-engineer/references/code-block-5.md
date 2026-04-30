# python Example

```
def itu_r_618_rain_attenuation(frequency_GHz, elevation_deg, rain_rate_mm_h, latitude_deg):
    """
    Simplified ITU-R P.618-14 rain attenuation model.
    Returns rain attenuation A_rain_dB at given exceedance percentage.
    """
    # Specific attenuation γR = k * R^alpha (ITU-R P.838-3)
    # Ka-band 20 GHz (approximate coefficients)
    if frequency_GHz <= 20:
        k = 0.0751; alpha = 1.099
    else:  # 30 GHz
        k = 0.187; alpha = 1.021

    gamma_R = k * rain_rate_mm_h**alpha  # dB/km

    # Effective path length through rain (ITU-R P.618 simplified)
    # Horizontal projection: Lr = (h_rain - h_station)
    h_rain_km = 5.0  # tropical rain height (km)
    Lr_km = h_rain_km
    reduction_factor_r = 1 / (1 + Lr_km
    Leff_km = Lr_km * reduction_factor_r

    A_rain = gamma_R * Leff_km
    return A_rain

# 10°N latitude, tropical zone R0.01 = 95 mm/h (ITU-R P.837 Table 2)
A_rain_99 = itu_r_618_rain_attenuation(20, elevation_deg=45, rain_rate_mm_h=25, latitude_deg=10)
A_rain_999 = itu_r_618_rain_attenuation(20, elevation_deg=45, rain_rate_mm_h=55, latitude_deg=10)
A_rain_9999 = itu_r_618_rain_attenuation(20, elevation_deg=45, rain_rate_mm_h=95, latitude_deg=10)

print(f"Ka-band rain attenuation at 45° elevation:")
print(f"99% avail: {A_rain_99:.1f} dB")
print(f"99.9% avail: {A_rain_999:.1f} dB  ← design target")
print(f"99.99% avail: {A_rain_9999:.1f} dB")

# Mitigation strategies:
ACM_TABLE = [
    ('32APSK 9/10', 5.0,  '> 20 Mbps'),
    ('16APSK 3/4', 3.0,   '~15 Mbps'),
    ('8PSK 2/3',   1.5,   '~10 Mbps'),
    ('QPSK 1/2',   0.0,   '~7 Mbps'),   # baseline
    ('QPSK 1/4',  -2.5,   '~3 Mbps'),
    ('BPSK 1/3',  -5.0,   '~1 Mbps'),   # emergency fallback
]
# Link design: carry full MODCOD stack; system auto-switches within 1 frame boundary
```
