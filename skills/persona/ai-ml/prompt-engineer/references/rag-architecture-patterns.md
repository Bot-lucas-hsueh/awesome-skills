## § 5 · RAG Architecture Patterns

### 5.1 Chunking Strategy Decision Matrix

| Document Type | Recommended Chunk Size | Overlap | Strategy |
|--------------|----------------------|---------|----------|
| Technical docs | 512 tokens | 10% | Fixed-size with sentence boundary |
| Legal
| Code | By function/class | 0% | AST-aware chunking |
| Conversations | By turn | 5% | Fixed-size |
| Tables

### 5.2 Context Injection Patterns

```
Pattern 1: Direct injection (simple)
  System: "Answer using the following context:\n\n{context}\n\nContext ends here."
  Risk: Model may ignore context if it contradicts training data

Pattern 2: Citation-required (more reliable)
  System: "Answer ONLY from the provided context. Cite [Doc X] for each claim.
          If the context doesn't contain the answer, say 'Not found in context.'"
  Benefit: Reduces hallucination; auditable

Pattern 3: Compression before injection (for long contexts)
  Step 1: Compress each retrieved chunk: "Summarize the key facts from this passage
          relevant to: {query}"
  Step 2: Inject compressed summaries + source references
  Benefit: Fits more sources in context window
```

### 5.3 Retrieval Quality Checklist

- [ ] Embedding model trained on domain-similar data
- [ ] Chunk size validated against retrieval precision (not just recall)
- [ ] Hybrid search (dense + sparse) for factual queries
- [ ] Re-ranking step for top-k candidates
- [ ] Relevance score threshold to filter low-quality hits
- [ ] Metadata filtering for recency or source credibility

---
