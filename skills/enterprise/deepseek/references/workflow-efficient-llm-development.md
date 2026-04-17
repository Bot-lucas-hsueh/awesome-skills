## § 3 — Workflow: Efficient LLM Development

### 3.1 DeepSeek Development Lifecycle

```
PHASE 1: ARCHITECTURE INNOVATION ✓/✗
├── Identify efficiency bottleneck in current SOTA
├── Design novel component (MLA, MoE variant, precision)
├── Mathematical proof of efficiency gain
├── Small-scale validation (1B-10B parameters)
├── Cost projection: target <1/10th industry standard
├── ✗ ABORT → No breakthrough efficiency → restart
└── Deliverable: Architecture proposal with efficiency proof

PHASE 2: LARGE-SCALE TRAINING ✓/✗
├── Fire-Flyer II cluster allocation
├── FP8 mixed precision implementation
├── Aux-loss-free MoE load balancing
├── 14.8T tokens training run (V3 example)
├── Real-time monitoring: loss, routing balance, throughput
├── ✗ ABORT → Instability, cost overrun, loss divergence
└── Deliverable: Trained checkpoint <$6M, stable convergence

PHASE 3: REASONING ENHANCEMENT (R1 track) ✓/✗
├── Cold-start: curated CoT examples (small SFT)
├── GRPO large-scale RL for reasoning emergence
├── Rejection sampling for high-quality SFT data
├── Second RL stage for human preference alignment
├── Verify: self-verification, reflection, CoT quality
└── Deliverable: Reasoning model matching o1

PHASE 4: OPEN-SOURCE RELEASE ✓/✗
├── Benchmark vs GPT-4/o1/Claude on MMLU/GSM8K/HumanEval
├── MIT license preparation
├── HuggingFace model upload
├── Technical report publication
├── Community engagement plan
└── Deliverable: Global impact, 1M+ downloads
```

### 3.2 Decision Trees

**Training Precision Decision:**
```
Model size < 7B? 
  ├─ Yes → BF16 (simpler, sufficient)
  └─ No → FP8 viable?
      ├─ Infrastructure supports? → Yes → FP8 (1.2× speedup)
      └─ No → BF16 fallback
```

**MoE vs Dense Decision:**
```
Target parameters > 100B?
  ├─ Yes → MoE (671B total, 37B active)
  │         └─ Shared + routed experts
  │         └─ Aux-loss-free balancing
  └─ No → Dense (simpler, sufficient)
```

**Release Strategy Decision:**
```
Safety evaluation passed?
  ├─ Yes → MIT license (maximum impact)
  │         └─ Full weights
  │         └─ Technical report
  │         └─ API for accessibility
  └─ No → Delay, address safety issues
```

---
