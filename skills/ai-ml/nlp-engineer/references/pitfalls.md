## § 9 · Common Pitfalls

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Prompt Injection** | Malicious input bypasses safety | Input sanitization, output filtering |
| **Hallucination** | False information presented as fact | RAG, citations, fact-checking |
| **Over-reliance on LLMs** | Using LLM where rules suffice | Rule-based + LLM hybrid |
| **Poor Chunking** | Lost context in RAG | Semantic chunking, overlap, metadata |
| **No Evaluation** | Can't measure improvement | Automated + human evaluation |
| **Prompt Hacking** | Users extracting system prompt | Input validation, rate limiting |

---
