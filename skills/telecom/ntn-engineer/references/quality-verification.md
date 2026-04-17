## ✅ Quality Verification

To verify this skill is working correctly, ask:

> "Calculate the maximum Doppler shift for a LEO satellite at 600 km altitude transmitting at Ka-band 20 GHz. How does this compare to 5G NR 15 kHz subcarrier spacing? Is pre-compensation required?"

**Expected response elements:**
- Satellite velocity: v = sqrt(GM/r) = sqrt(3.986e14 / (6971e3)) ≈ 7,558 m/s
- Maximum Doppler: fD = v/c × f = 7558/3e8 × 20e9 ≈ 504 kHz
- Ratio to SCS: 504 kHz
- Conclusion: MANDATORY pre-compensation (residual budget ≤ 1.5 kHz = 0.1 × SCS)
- Method: UE uses GNSS position + satellite ephemeris broadcast in SIB1 (3GPP Rel-17)

**Red flags (skill not working):**
- Stating Doppler is small or negligible for LEO Ka-band
- Not computing the ratio to SCS (the critical comparison)
- Suggesting post-compensation at gNB instead of pre-compensation at UE
