# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | Using `padding=True` without `truncation=True` | 🔴 High | Always set max_length |
| 2 | Not setting pad_token for causal models | 🔴 High | `tokenizer.pad_token = tokenizer.eos_token` |
| 3 | Training with mixed precision incorrectly | 🟡 Medium | Use `bf16=True` or `fp16=True` in TrainingArguments |
| 4 | Forgetting to set `device_map` for large models | 🔴 High | Use `device_map="auto"` for multi-GPU |
| 5 | Loading full model when only need embeddings | 🟡 Medium | Use AutoModel with specific head |
| 6 | Not using `remove_columns` before set_format | 🟡 Medium | Remove string columns before tensor conversion |
| 7 | Using default learning rate without tuning | 🟡 Medium | Start with 1e-5 to 3e-5 for fine-tuning |
| 8 | Ignoring tokenizer max_model_length | 🔴 High | Match tokenizer config with model |
| 9 | Forgetting gradient checkpointing for large models | 🟡 Medium | Enable with `gradient_checkpointing=True` |
| 10 | Not using peft for fine-tuning LLMs | 🟡 Medium | Use QLoRA for efficiency |

## 10.2 Common Error Solutions

### CUDA Out of Memory

```python
# Solution 1: Reduce batch size
per_device_train_batch_size=4

# Solution 2: Use gradient accumulation
gradient_accumulation_steps=8

# Solution 3: Enable gradient checkpointing
training_args = TrainingArguments(
    gradient_checkpointing=True,
    ...
)

# Solution 4: Use 8-bit or 4-bit quantization
bnb_config = BitsAndBytesConfig(load_in_8bit=True)

# Solution 5: Use CPU offloading
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    load_in_8bit=True
)
```

### Tokenizer Mismatch

```python
# Problem: vocab size mismatch
# Solution: Always use matching tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Don't do this:
model = AutoModel.from_pretrained("bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("roberta-base")
```

## 10.3 Memory Optimization Best Practices

```python
# For large models, use these settings together
training_args = TrainingArguments(
    per_device_train_batch_size=2,
    gradient_accumulation_steps=16,
    gradient_checkpointing=True,
    fp16=False,
    bf16=True,  # or fp16=True for older GPUs
    max_grad_norm=0.3,
    learning_rate=1e-4,
)

# For 80GB A100 with 7B model:
# batch_size=8, gradient_accumulation=8, total_batch=64
```

## 10.4 Tokenization Best Practices

```python
# Always specify truncation and max_length
encoded = tokenizer(
    text,
    truncation=True,
    max_length=512,
    padding="max_length",
    return_tensors="pt"
)

# For paired inputs
encoded = tokenizer(
    premise,
    hypothesis,
    truncation=True,
    max_length=256,
    padding="max_length"
)

# Handle special tokens
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
```

## 10.5 HuggingFace Hub Best Practices

```python
# Login before pushing
from huggingface_hub import login
login(token="hf_your_token")

# Push model
model.push_to_hub("username/model-name")
tokenizer.push_to_hub("username/model-name")

# Use private repos for proprietary models
model.push_to_hub("username/private-model", private=True)

# Load from private repo
from huggingface_hub import HfApi
api = HfApi()
api.login("hf_your_token")

model = AutoModel.from_pretrained("username/private-model")
```

## 10.6 Dataset Best Practices

```python
# Don't load entire dataset into memory
dataset = load_dataset("bigscience/Pile", split="train")
dataset = dataset.with_format("pandas")
dataset = dataset.to_iterable_dataset()  # Streaming

# For custom datasets, save in Arrow format
dataset.save_to_disk("./my_dataset")
dataset = load_from_disk("./my_dataset")

# Use memory mapping for large datasets
dataset = load_dataset(
    "dataset_path",
    streaming=True
)
```
