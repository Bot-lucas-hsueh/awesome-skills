## § 4 — Core Philosophy

→ See [references/code-block-1.md](references/code-block-1.md) for the sensitivity hierarchy diagram.

**Guiding Principle 1 — Sensitivity Is Meaningless Without Systematics**: A quantum sensor achieving 10^−16 g/√Hz statistical sensitivity is useless if systematic errors contribute 10^−12 g bias uncertainty. Systematic error characterization must match or exceed statistical precision; the two cannot be traded off.

**Guiding Principle 2 — Allan Deviation Is the Complete Story**: A single-shot sensitivity number answers "how well can I measure in one shot?" but the Allan deviation answers "how well can I measure over hours of averaging?" — the operationally relevant quantity for most applications. Never report sensitivity without Allan deviation.

**Guiding Principle 3 — Quantum Advantage Must Survive the Detection Chain**: Spin squeezing and entanglement-enhanced sensing provide theoretical sensitivity gains of √N or N. In practice, detection loss, readout inefficiency, and decoherence during state preparation erode these gains. Always compute net sensitivity gain including all efficiency factors before claiming quantum advantage.

---
