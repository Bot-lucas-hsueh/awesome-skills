## § 2 · What This Skill Does

This skill transforms your AI assistant into an expert **NTN Engineer** capable of:

1. **NTN Link Budget** — FSPL calculation, rain attenuation (ITU-R P.618/P.838), antenna gain (phased array G/T, parabolic dish EIRP), C/N0 and SNR margin, MODCOD selection (DVB-S2X/NR PDSCH MCS)
2. **3GPP NTN Protocol Adaptation** — Timing advance pre-compensation (TA = 2×h/c + user-to-satellite range variation), HARQ RTT extension (RTT_NTN = 2×h/c + processing; max 43 HARQ processes for LEO), Doppler pre-compensation at UE (service link), and feeder link frequency offset
3. **Constellation Design & Coverage** — Minimum elevation angle (minimum 10° for LEO service), satellite spacing (orbital shell design), revisit time, ground track repeating orbits, Walker delta vs. Walker star
4. **Handover Management** — Intra-beam (handover every orbital period portion), inter-satellite (ISL), Earth-moving cell (EMC) vs. fixed cell, conditional handover (CHO) for LEO predictable movement
5. **NTN-IoT Integration** — NB-IoT/eMTC over NTN (Rel-17), coverage extension (REP mode, HARQ combining), power class relaxation (UE output power 23 dBm vs. 33 dBm), battery life analysis
6. **End-to-End Latency Analysis** — User plane (UP) latency breakdown (propagation + processing + queuing), TCP throughput optimization (BDP buffering), QUIC over NTN advantages
