## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Unvalidated Thermodynamics** | 🔴 High | Using incorrect EOS (e.g., Peng-Robinson for polar mixtures) leads to 30-50% error in VLE predictions; column flooding, product off-spec | Require experimental data or validated property package; always cross-check with NIST ThermoDATA |
| **Runaway Reaction** | 🔴 High | Exothermic reactions without adequate cooling lead to thermal runaway; pressurization → vessel failure; documented in 40% of chemical accidents | Apply reaction calorimetry data (RC1), design with adequate safety margin, specify emergency quenching |
| **Relief Valve Under-sizing** | 🔴 High | Undersized PSV fails to relieve during overpressure; vessel rupture → explosion; API 520/521 compliance mandatory | Use conservative values (1.1× design pressure for fire case); verify with process simulation |
| **Corrosion/Materials Failure** | 🔴 High | Wrong material selection (e.g., carbon steel for chloride service) leads to rapid corrosion, leak, fire | Reference NACE/AMPP guidelines, require corrosion allowance, specify corrosion monitoring |
| **Heat Exchanger Fouling** | 🟡 Medium | 15-30% heat transfer degradation from fouling; oversized exchangers hide the problem until turndown | Specify design foul factor 1.5× clean, include online cleaning capability |
| **Scale-Up Errors** | 🟡 Medium | Lab data without scale-up basis → commercial failure; heat/mass transfer coefficients scale non-linearly | Apply dimensional analysis, validate with pilot data, document scale-up rationale |
| **Environmental Non-Compliance** | 🟡 Medium | Emission estimates off by 2-3× → permit denial, startup delays | Use EPA emission factors, validate with stack testing, include safety margin in permit applications |

**⚠️ IMPORTANT
- Process safety recommendations are based on general engineering principles. Specific applications must be validated by licensed Professional Engineer (PE) per local regulations.

- Process simulation results require engineering judgment. Never accept simulator output without validating against pilot data or reference sources.

---
