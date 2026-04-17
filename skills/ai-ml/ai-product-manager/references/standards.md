## 7. Standards & Reference

### 7.1 AI Product Frameworks

| Framework / 框架 | When to Use / 使用场景 | Key Steps
|-----------------|----------------------|-------------------|
| **Jobs-To-Be-Done for AI** | Defining the user problem before selecting AI approach | 1. Identify the job → 2. Current solution pain → 3. Define "done" → 4. Evaluate AI fit |
| **AI Feature Tiering** | Determining appropriate autonomy level for AI feature | 1. Map error cost → 2. Assess user trust baseline → 3. Assign tier (Copilot/Autopilot/Pilot) → 4. Define tier graduation criteria |
| **Build / Buy
| **Shadow Mode Testing** | Pre-launch validation without user impact | 1. Route live traffic → model → 2. Compare model output vs. human decision → 3. Measure agreement rate → 4. Define go-live threshold |

### 7.2 AI Product Metrics

| Metric / 指标 | Definition / 定义 | Target / 目标 | Frequency
|--------------|-----------------|--------------|-----------------|
| **AI Adoption Rate** | % of eligible users who engage with AI feature >2x/week | >30% in first month | Weekly |
| **AI Accuracy** | Task-specific correctness rate; defined per use case (not a universal number) | Defined per error severity tier | Daily |
| **AI Override Rate** | % of times users undo, ignore, or correct an AI suggestion | <30% for good human-AI alignment; >50% signals model or UX problem | Daily |
| **AI Trust Score** | NPS measured specifically for the AI feature (separate from product NPS) | >40 NPS for AI feature (track trend, not absolute) | Monthly |
| **AI Feature Engagement** | Time saved per user per week attributable to AI assistance | Benchmark against pre-AI baseline; target >15 min/week for productivity features | Weekly |
| **Graceful Degradation Rate** | % of low-confidence outputs successfully routed to human review or fallback | >95% (near-zero user-facing model failures) | Daily |

### 7.3 Evaluation Framework for AI Products

```
Layer 1: Offline Metrics (离线指标) — Lab performance
├── Classification: Precision, Recall, F1, AUC-ROC (per class, not just overall)
├── Generation (LLM): ROUGE-L, BERTScore, human preference rate (pairwise)
├── Ranking: NDCG@K, MRR, Hit@K
└── Gate: Must pass offline threshold before shadow mode

Layer 2: Online Metrics (在线指标) — Real user signal
├── AI Adoption Rate, Override Rate, AI Trust Score
├── Safety: Harmful output rate, refusal accuracy
├── Performance: P50/P95/P99 latency, error rate, cost per inference
└── Gate: Must show positive lift vs. control before full rollout

Layer 3: User Perception (用户感知) — Qualitative signal
├── AI feature-specific NPS (not blended with product NPS)
├── Qualitative interviews: "When did AI help? When did it frustrate?"
├── Session replay analysis: Where do users abandon AI suggestions?
└── Gate: Qualitative confirms quantitative; no major trust concerns
```

### 7.4 AI UX Patterns

| Pattern / 模式 | Use When / 使用场景 | Implementation
|---------------|-------------------|---------------------|
| **Confidence Scoring** | User needs to calibrate trust in AI output | Show confidence as plain language ("High confidence", "Not sure — verify this") not raw percentages |
| **AI Explanation** | High-stakes decisions; regulated domains | Show top 2-3 factors that drove the AI output; link to source documents for RAG |
| **Human-in-the-Loop Escalation** | Low-confidence output; high-error-cost scenarios | Route below-threshold confidence to human review queue; never silently drop the request |
| **Progressive Disclosure** | Users have varying AI literacy levels | Default: simple AI output; "Why?" button reveals explanation; settings allow turning AI off entirely |

---

