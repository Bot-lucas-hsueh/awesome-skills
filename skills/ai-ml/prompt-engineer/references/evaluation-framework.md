## § 6 · Evaluation Framework

### 6.1 LLM-as-Judge Prompt Template

```
You are an expert evaluator. Rate the following response on a 1-5 scale.

Criteria:
- Accuracy (1-5): Is the information factually correct?
- Relevance (1-5): Does it directly address the question?
- Completeness (1-5): Are all important aspects covered?
- Clarity (1-5): Is it easy to understand?

Question: {question}
Response: {response}
Reference answer (if available): {reference}

For each criterion, provide:
1. Score (1-5)
2. One-sentence justification
3. Specific improvement suggestion

Output as JSON:
{"accuracy": {"score": X, "reason": "...", "improvement": "..."},
 "relevance": {"score": X, ...},
 "completeness": {"score": X, ...},
 "clarity": {"score": X, ...},
 "overall": X}
```

### 6.2 Regression Test Suite Structure

```python
# Minimal eval harness (pseudo-code)
test_cases = [
    {
        "id": "factual_01",
        "input": "What is the capital of France?",
        "expected_contains": ["Paris"],
        "expected_not_contains": ["London", "Berlin"],
        "eval_type": "exact_match"
    },
    {
        "id": "reasoning_01",
        "input": "If A > B and B > C, is A > C?",
        "eval_type": "llm_judge",
        "rubric": "Answer must be 'yes' with correct transitive reasoning"
    }
]

for case in test_cases:
    response = call_llm(prompt_template, case["input"])
    score = evaluate(response, case)
    log_result(case["id"], score, response)
```

---

