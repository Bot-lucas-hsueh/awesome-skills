## § 9 · Common Pitfalls

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Overfitting** | Model doesn't generalize | Cross-validation, simpler models |
| **Data Snooping** | Peeking at test set | Strict train/validation/test split |
| **Ignoring Class Imbalance** | Model predicts majority class | SMOTE, class weights, proper metrics |
| **Feature Leakage** | Future information in features | Time-aware feature engineering |
| **Multiple Testing** | False positives from many tests | Bonferroni, FDR correction |
| **Black Box Models** | Can't explain predictions | SHAP, LIME, simpler models |

---
