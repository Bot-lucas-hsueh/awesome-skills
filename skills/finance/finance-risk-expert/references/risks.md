## § 3 · Risk Disclaimer

| Risk| Severity| Description| Mitigation|
|------------|-----------------|-------------------|---------------------|
| **Model Risk** | 🔴 High | Models may fail in unexpected conditions; backtesting is not prediction | Multiple model validation, manual overrides, model inventory management |
| **Regulatory Changes** | 🔴 High | Basel IV, CECL implementation timelines and requirements change | Stay current with regulatory publications, engage regulators early |
| **Data Quality** | 🟡 Medium | Risk models are only as good as input data; GIGO applies | Data quality frameworks, reconciliation,上游 validation |
| **Parameter Estimation Error** | 🟡 Medium | PD/LGD estimates have confidence intervals; point estimates mislead | Use confidence intervals, sensitivity analysis, expert judgment overlays |
| **Interpretability vs. Accuracy** | 🟢 Low | Complex ML models may outperform but lack explainability for regulators | Balance with interpretable models, use SHAP/LIME for explanation |

**⚠️ IMPORTANT:**
- This skill provides analysis and guidance — not definitive regulatory or investment advice
- Risk models are probabilistic estimates, not predictions; actual outcomes will vary
- Always involve legal and compliance teams for regulatory interpretations

---
