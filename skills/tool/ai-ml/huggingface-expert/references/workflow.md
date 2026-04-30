# Standard Workflow

## 8.1 NLP Project Workflow

```
Phase 1: Task Analysis
├── Identify task type (classification, generation, etc.)
├── Determine data requirements
└── Select appropriate model family

Phase 2: Data Preparation
├── Load or create dataset
├── Tokenize with appropriate tokenizer
├── Split train/val/test
└── Format for Trainer or custom loop

Phase 3: Model Development
├── Load pretrained model
├── Configure for task (head, loss)
├── Apply PEFT if fine-tuning
└── Verify forward pass

Phase 4: Training
├── Set up Trainer or custom loop
├── Configure logging and callbacks
├── Train with appropriate hyperparameters
└── Monitor GPU memory

Phase 5: Evaluation & Deployment
├── Evaluate on test set
├── Push to Hub if needed
└── Export for inference
```

## 8.2 Text Classification Fine-tuning Workflow

```python
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    TrainingArguments, Trainer
)
from datasets import load_dataset

# Load data
dataset = load_dataset("glue", "sst2")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenize
def tokenize(examples):
    return tokenizer(
        examples["sentence"],
        truncation=True,
        padding="max_length",
        max_length=128
    )

dataset = dataset.map(tokenize, batched=True)

# Load model
model = AutoModelForSequenceClassification.from_pretrained(
    "bert-base-uncased",
    num_labels=2
)

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=32,
    learning_rate=2e-5,
    warmup_steps=100,
    logging_dir="./logs",
    logging_steps=10,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="accuracy"
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],
    compute_metrics=lambda p: {
        "accuracy": (p.predictions[0].argmax(-1) == p.label_ids).mean()
    }
)

trainer.train()
```

## 8.3 RAG Workflow with HuggingFace

```python
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

# Step 1: Load documents
loader = TextLoader("document.txt")
docs = loader.load()

# Step 2: Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# Step 3: Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Step 4: Create vector store
vectorstore = FAISS.from_documents(chunks, embeddings)

# Step 5: Create retrieval chain
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 4}
)

# Step 6: Create QA chain with HuggingFace model
qa_chain = pipeline(
    "question-answering",
    model="distilbert-base-uncased-distilled-squad"
)

def answer(question):
    docs = retriever.get_relevant_documents(question)
    context = " ".join([doc.page_content for doc in docs])
    return qa_chain(question=question, context=context)
```

## 8.4 Model Deployment Workflow

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load and quantize for deployment
model_id = "meta-llama/Llama-2-7b-chat-hf"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Save for inference
model.save_pretrained("./llama2-7b-deployment")
tokenizer.save_pretrained("./llama2-7b-deployment")

# For inference server (e.g., text-generation-inference)
# tgi --model-id meta-llama/Llama-2-7b-chat-hf --port 8080
```

## 8.5 Distributed Training Workflow

```python
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from datasets import load_dataset
from accelerate import Accelerator

accelerator = Accelerator()

# Load model and data
model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

dataset = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")

def tokenize(examples):
    return tokenizer(examples["text"], return_tensors="pt")

dataset = dataset.map(tokenize, batched=True, remove_columns=["text"])

# Prepare with Accelerator
model, dataset = accelerator.prepare(model, dataset)

# Training arguments
training_args = TrainingArguments(
    output_dir="./output",
    per_device_train_batch_size=8,
    gradient_accumulation_steps=4,
    max_steps=1000,
    logging_steps=100,
    bf16=True,
    dataloader_num_workers=4
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False)
)

trainer.train()
```
