## § 4 · Core Philosophy

```
[Code block moved to code-block-1.md]
```

**Guiding Principle 1 — Information-Theoretic Security as the North Star**: QKD's unique value is unconditional security against computationally unbounded adversaries. Compromising this (e.g., using computationally-secure error correction codes that leak information) defeats the purpose. Every component of the QKD pipeline must be analyzed for information leakage, not just the quantum channel.

**Guiding Principle 2 — Hardware Determines Protocol**: The choice of QKD protocol must be driven by available hardware. SNSPD enables MDI-QKD over 300+ km; InGaAs APD limits MDI-QKD to <100 km at practical rates. Quantum memories with T2 > 1 ms are required for repeater nodes. Protocol design is inseparable from hardware characterization.

**Guiding Principle 3 — Classical Infrastructure is the Weak Link**: The quantum channel is often not the attack surface. Authentication of the classical post-processing channel, key management system security, and trusted-node physical security are the dominant vulnerabilities in real deployments. Quantum security ends where classical security fails.

---

