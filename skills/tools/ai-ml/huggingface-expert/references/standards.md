# Standards & Reference

## 7.1 Official Documentation

- [Hugging Face Documentation](https://huggingface.co/docs)
- [Transformers Library](https://huggingface.co/docs/transformers/)
- [Datasets Library](https://huggingface.co/docs/datasets/)
- [PEFT Library](https://huggingface.co/docs/peft/)
- [Hugging Face Hub API](https://huggingface.co/docs/hub/)
- [🤗 Accelerate](https://huggingface.co/docs/accelerate/)
- [Tokenizers](https://huggingface.co/docs/tokenizers/)

## 7.2 Installation & Version Reference

```bash
# Core packages
pip install transformers>=4.30.0
pip install datasets>=2.14.0
pip install accelerate>=0.20.0
pip install peft>=0.4.0
pip install bitsandbytes>=0.40.0  # Quantization
pip install peft>=0.7.0  # For 4-bit quantization
```

## 7.3 Pipeline Reference

### Available Pipeline Tasks

| Task | Description | Output Type |
|------|-------------|-------------|
| `text-generation` | Generate text | `GeneratedText` |
| `fill-mask` | Fill masked token | `FillMaskResult` |
| `ner` | Named Entity Recognition | `Entity` |
| `question-answering` | Extract from context | `QAResult` |
| `sentiment-analysis` | Classification | `SentimentResult` |
| `summarization` | Summarize text | `SummaryResult` |
| `translation_xx_to_yy` | Translation | `TranslationResult` |
| `zero-shot-classification` | Zero-shot labeling | `ClassificationResult` |

### Pipeline Parameters

```python
from transformers import pipeline

# Common parameters
pipe = pipeline(
    task="text-generation",
    model="gpt2",
    device=0,                    # GPU device (-1 for CPU)
    torch_dtype=torch.float16,   # Precision
    trust_remote_code=False,     # Allow custom models
    max_length=100,              # Max tokens
    temperature=0.7,             # Sampling temperature
    top_p=0.9,                   # Nucleus sampling
    do_sample=True,              # Sampling vs greedy
)
```

## 7.4 Model Loading Reference

### Auto Classes

```python
from transformers import (
    AutoModel, AutoModelForCausalLM,
    AutoModelForMaskedLM, AutoModelForSeq2SeqLM,
    AutoModelForQuestionAnswering, AutoModelForTokenClassification,
    AutoTokenizer, AutoConfig
)

# Load model for specific task
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

# Load config with specific settings
config = AutoConfig.from_pretrained(
    "bert-base-uncased",
    num_labels=3,
    hidden_dropout_prob=0.1
)
```

### Loading with Quantization

```python
from transformers import AutoModelForCausalLM
from transformers import BitsAndBytesConfig

# 4-bit quantization (QLoRA)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-v0.1",
    quantization_config=bnb_config,
    device_map="auto"
)
```

## 7.5 Dataset Loading Reference

```python
from datasets import load_dataset, DatasetDict, Dataset

# Load from Hub
dataset = load_dataset("imdb")
test_dataset = load_dataset("glue", "sst2", split="test")

# Load from local files
dataset = load_dataset("csv", data_files="train.csv")
dataset = load_dataset("json", data_files="data.json")

# Dataset operations
dataset = dataset.map(tokenize_function, batched=True)
dataset = dataset.filter(lambda x: x["label"] > 0)
dataset = dataset.train_test_split(test_size=0.2)
dataset.set_format(type="torch", columns=["input_ids", "label"])
```

## 7.6 PEFT/LoRA Reference

### LoRA Configuration

```python
from peft import LoraConfig, get_peft_model, TaskType

lora_config = LoraConfig(
    r=16,                         # Rank
    lora_alpha=32,                # Scaling factor
    target_modules=[              # Target attention layers
        "q_proj", "v_proj", 
        "k_proj", "o_proj"
    ],
    lora_dropout=0.05,
    bias="none",                  # "none", "all", "lora_only"
    task_type=TaskType.CAUSAL_LM
)

model = get_peft_model(base_model, lora_config)
model.print_trainable_parameters()
# Output: "trainable params: 4M || all params: 7B || trainable%: 0.05%"
```

### Saving and Loading Adapters

```python
# Save adapter
model.save_pretrained("./lora_adapter")

# Load adapter
from peft import PeftModel
model = PeftModel.from_pretrained(base_model, "./lora_adapter")
```
