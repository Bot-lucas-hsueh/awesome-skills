## § 4 · Core Philosophy

```
              BRAIN-COMPUTER INTERFACE SYSTEM ARCHITECTURE
              ============================================

  Neural Activity           Recording Front-End          Signal Processing
  +---------------+        +------------------+         +------------------+
  | Spikes (AP)   |--Utah--| Electrode Array  |--Intan--| Spike Detection  |
  | LFP (1-300Hz) |--ECoG--| Impedance <100kΩ |--RHD---|  Kilosort3       |
  | EEG (<100Hz)  |--Cap---| 30 kSPS/ch ADC   |--OEphys| ICA Artifact Rej |
  +---------------+        +------------------+         +--------+---------+
                                                                  |
                           +-------------------------------+      |
                           |    Neural Decoder             |<-----+
                           |  Kalman / LSTM
                           |  Feature: FR, LFP band power  |
                           |  Output: position, intent,    |
                           |  phoneme, grasp type          |
                           +-------------+-----------------+
                                         |
         +-------------------------------+-------------------------------+
         |                              |                               |
  +------v-------+             +--------v--------+           +----------v--------+
  | Motor Output |             | Communication   |           | Neurostimulation  |
  | Robotic arm  |             | Speech synth    |           | DBS / SCS
  | Cursor ctrl  |             | Keyboard BCI    |           | Seizure abort     |
  +------+-------+             +--------+--------+           +----------+--------+
         |                              |                               |
         +------------------------------+-------------------------------+
                                        |
                                  FEEDBACK LOOP
                                  (Visual / Somatosensory

  SIGNAL QUALITY PYRAMID:
    ^  Single-unit spikes (highest info, invasive: Utah/Neuropixels)
   ^^  Multi-unit activity + LFP (moderate, ECoG semi-invasive)
  ^^^  EEG/ECoG beta/gamma bands (lower info, non-invasive/low-invasive)
 ^^^^  fNIRS
```

**Guiding Principles:**

1. **Signal Quality Determines Decoding Ceiling** — no algorithm compensates for fundamentally poor signal quality. The information content of the neural recording (Shannon mutual information between neural state and decoder output) sets an absolute upper bound on BCI performance. Invest first in electrode impedance reduction, mechanical stability, and noise floor minimization before optimizing decoder complexity.

2. **Stationarity is the Clinical Bottleneck** — the greatest unsolved challenge in chronic BCI is signal non-stationarity. Neural tuning properties shift daily; glial encapsulation evolves over weeks; the patient's brain reorganizes in response to BCI use. Every chronic BCI system must include an online adaptation strategy as a first-class design requirement, not an afterthought.

3. **Safety-First Closed-Loop Design** — a closed-loop BCI that delivers stimulation is a safety-critical system. The stimulator is the actuator of a control loop that acts on human tissue. Apply hardware failsafes (current limiting, charge dump, watchdog timers), software interlocks (stimulation-off on signal loss), and FDA-compliant risk analysis (ISO 14971) before any human experiment.

---

