## § 9 · Gotchas & Anti-Patterns

### #EP1: Treating Connections as Symmetric

❌ **Wrong**: Assuming all connections are equal bidirectional relationships.

✅ **Right**: Model connection strength and directionality. A CEO connecting to an employee has different semantics than peer-to-peer connections.

---

### #EP2: Ignoring Graph Connectivity

❌ **Wrong**: Building recommendation systems without considering the social graph structure.

✅ **Right**: Use graph algorithms (PageRank, community detection, shortest path) to leverage network effects and trust propagation.

---

### #EP3: Batch Processing for Real-Time Features

❌ **Wrong**: Running hourly batch jobs for features that members expect immediately (notifications, feed updates).

✅ **Right**: Use Kafka + Samza for event-driven architectures. Members expect real-time in social products.

---

### #EP4: Naive Skill Matching

❌ **Wrong**: String matching for skills ("ML" ≠ "Machine Learning" ≠ "ml").

✅ **Right**: Build a comprehensive skill taxonomy with embeddings. Handle synonyms, abbreviations, and related skills.

---

### #EP5: Notification Spam

❌ **Wrong**: Sending every event as a notification without rate limiting or personalization.

✅ **Right**: Implement sophisticated throttling, batching, and ML-based engagement prediction. Notification fatigue kills product trust.

---

### #EP6: Ignoring Professional Context

❌ **Wrong**: Treating LinkedIn like Facebook — optimizing purely for engagement.

✅ **Right**: Maintain professional quality standards. Viral but unprofessional content damages the brand and member trust.

---

### #EP7: Underestimating Graph Scale

❌ **Wrong**: Running O(n²) algorithms on a graph with billions of edges.

✅ **Right**: Use approximate algorithms, sampling, and distributed graph processing. Pre-compute common traversals.

---

### #EP8: Static Skill Taxonomies

❌ **Wrong**: Building a fixed skill taxonomy that doesn't evolve with the market.

✅ **Right**: Continuously detect emerging skills (e.g., "Prompt Engineering" in 2023, "Generative AI" in 2024) using NLP on job postings.

---
