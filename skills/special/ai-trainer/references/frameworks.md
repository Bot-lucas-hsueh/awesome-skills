## § 7 · Standards & Reference

### Training Data Quality Metrics

| Metric / 指标 | Formula / 公式 | Target
|--------------|---------------|--------------|
| Inter-Annotator Agreement (IAA) | Cohen's κ = (P_o - P_e)
| Annotation Error Rate | errors_found
| Dataset Coverage | task_categories_with_examples
| Response Length Distribution | stddev(response_length)
| SFT Data Diversity | 1 - (duplicate_ngrams
| Preference Pair Clarity | pairs_with_clear_winner
| Reward Model Accuracy | correct_rankings

### RLHF Data Format Standards

```json
// SFT example format
{
  "id": "sft_20260304_001",
  "prompt": "Explain how transformers work to a 10-year-old",
  "response": "...",
  "task_category": "explanation",
  "quality_score": 4.2,
  "annotator_id": "ann_042",
  "annotation_time_sec": 185
}

// Preference pair format
{
  "id": "pref_20260304_001",
  "prompt": "Write a Python function to sort a list",
  "chosen": "def sort_list(lst):\n    return sorted(lst)\n\n# Example:\n# sort_list([3,1,2]) → [1,2,3]",
  "rejected": "you can use sort function",
  "chosen_rating": {"helpful": 5, "correct": 5, "safe": 5},
  "rejected_rating": {"helpful": 2, "correct": 3, "safe": 5},
  "annotator_id": "ann_017",
  "preference_strength": "clear"  // "clear" | "slight" | "ambiguous"
}
```

### Alignment Dimensions Priority

For most use cases, apply this priority order (per Anthropic Constitutional AI research):
```
1. Harmless — never assist with clearly harmful requests
2. Honest — don't fabricate information; express uncertainty appropriately
3. Helpful — maximize usefulness within safety/honesty constraints
```

---
