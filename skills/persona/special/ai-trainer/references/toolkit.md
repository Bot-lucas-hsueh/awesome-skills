## § 6 · Professional Toolkit

| Tool / 工具 | Purpose / 用途 | When to Use
|------------|---------------|----------------------|
| **Scale AI
| **Label Studio** | Open-source annotation tool, highly configurable | Custom annotation interfaces; self-hosted for data privacy |
| **Argilla** | NLP-focused annotation platform with model-in-the-loop | SFT data collection with active learning; integrates with HuggingFace |
| **OpenAI Evals** | Evaluation framework for model quality assessment | Measuring training data quality; benchmarking model improvements |
| **Eleuther LM Evaluation Harness** | Standardized benchmark evaluation | Track model performance vs benchmarks after training data changes |
| **NLTK / spaCy** | Text processing and linguistic analysis | Analyzing prompt/response diversity; detecting distribution gaps |
| **Pandas + Jupyter** | Data analysis and visualization | Dataset quality audits; coverage analysis; IAA calculation |
| **Cohen's Kappa Calculator** | Inter-annotator agreement measurement | Measuring annotation consistency; target κ ≥ 0.75 before scaling |
| **Constitutional AI (Anthropic)** | Self-critique and revision framework for RLAIF | Generating AI-assisted training data for safety alignment |
| **TGI
| **Weights & Biases** | Training run tracking and data versioning | Tracking which training data version produced which model checkpoint |
| **Hugging Face Datasets** | Dataset hosting, versioning, and sharing | Managing SFT/RLHF datasets with version control |

---
