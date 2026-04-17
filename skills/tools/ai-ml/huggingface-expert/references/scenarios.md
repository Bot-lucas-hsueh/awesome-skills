# Scenario Examples

## 9.1 Building a Sentiment Classifier

**User:** "Fine-tune BERT for sentiment classification on my data"

**HuggingFace Expert:**
> **Complete Fine-tuning Pipeline:**
>
> ```python
> from transformers import (
>     AutoModelForSequenceClassification,
>     AutoTokenizer,
>     TrainingArguments, Trainer
> )
> from datasets import load_dataset
>
> # Load your data
> dataset = load_dataset("csv", data_files="sentiment_data.csv")
> dataset = dataset.rename_column("text", "sentence")
> dataset = dataset.rename_column("label", "label")
>
> tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
>
> def tokenize_fn(examples):
>     return tokenizer(
>         examples["sentence"],
>         truncation=True,
>         padding="max_length",
>         max_length=256
>     )
>
> dataset = dataset.map(tokenize_fn, batched=True)
>
> model = AutoModelForSequenceClassification.from_pretrained(
>     "bert-base-uncased",
>     num_labels=2
> )
>
> training_args = TrainingArguments(
>     output_dir="./sentiment_model",
>     num_train_epochs=3,
>     per_device_train_batch_size=16,
>     learning_rate=2e-5,
>     evaluation_strategy="epoch",
>     save_strategy="epoch",
>     load_best_model_at_end=True
> )
>
> trainer = Trainer(
>     model=model,
>     args=training_args,
>     train_dataset=dataset["train"],
>     eval_dataset=dataset["test"],
> )
>
> trainer.train()
> model.push_to_hub("my-username/sentiment-model")
> ```

## 9.2 Zero-Shot Classification

**User:** "Classify text without training data"

**HuggingFace Expert:**
> **Zero-Shot Pipeline:**
>
> ```python
> from transformers import pipeline
>
> classifier = pipeline(
>     "zero-shot-classification",
>     model="facebook/bart-large-mnli"
> )
>
> text = "The new iPhone has an amazing camera and battery life."
>
> labels = ["technology", "sports", "politics", "entertainment"]
>
> result = classifier(text, candidate_labels=labels)
> # Output: {'labels': ['technology', 'entertainment', 'sports', 'politics'],
> #          'scores': [0.94, 0.02, 0.02, 0.02]}
> ```

## 9.3 Text Generation with Chat Models

**User:** "Generate responses with Llama 2 in chat format"

**HuggingFace Expert:**
> **Chat Template Generation:**
>
> ```python
> from transformers import AutoModelForCausalLM, AutoTokenizer
> import torch
>
> model_id = "meta-llama/Llama-2-7b-chat-hf"
>
> tokenizer = AutoTokenizer.from_pretrained(model_id)
> model = AutoModelForCausalLM.from_pretrained(
>     model_id,
>     torch_dtype=torch.bfloat16,
>     device_map="auto"
> )
>
> messages = [
>     {"role": "system", "content": "You are a helpful assistant."},
>     {"role": "user", "content": "Explain quantum computing in simple terms."}
> ]
>
> input_ids = tokenizer.apply_chat_template(
>     messages,
>     return_tensors="pt"
> ).to("cuda")
>
> with torch.no_grad():
>     outputs = model.generate(
>         input_ids,
>         max_new_tokens=256,
>         temperature=0.7,
>         do_sample=True,
>         pad_token_id=tokenizer.pad_token_id
>     )
>
> response = tokenizer.decode(
>     outputs[0][input_ids.shape[1]:],
>     skip_special_tokens=True
> )
> print(response)
> ```

## 9.4 PEFT LoRA Fine-tuning

**User:** "Fine-tune Llama 2 with LoRA for my use case"

**HuggingFace Expert:**
> **QLoRA Fine-tuning:**
>
> ```python
> from transformers import (
>     AutoModelForCausalLM, AutoTokenizer,
>     TrainingArguments, Trainer,
>     DataCollatorForLanguageModeling
> )
> from peft import (
>     LoraConfig, get_peft_model,
>     prepare_model_for_kbit_training
> )
> from bitsandbytes import BitsAndBytesConfig
> import torch
>
> # Quantization config
> bnb_config = BitsAndBytesConfig(
>     load_in_4bit=True,
>     bnb_4bit_compute_dtype=torch.bfloat16,
>     bnb_4bit_use_double_quant=True,
>     bnb_4bit_quant_type="nf4"
> )
>
> # Load model
> model = AutoModelForCausalLM.from_pretrained(
>     "meta-llama/Llama-2-7b-hf",
>     quantization_config=bnb_config,
>     device_map="auto"
> )
> model = prepare_model_for_kbit_training(model)
>
> # LoRA config
> lora_config = LoraConfig(
>     r=64,
>     lora_alpha=128,
>     target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
>     lora_dropout=0.1,
>     bias="none",
>     task_type="CAUSAL_LM"
> )
>
> model = get_peft_model(model, lora_config)
> model.print_trainable_parameters()
>
> # Train
> training_args = TrainingArguments(
>     output_dir="./lora_llama2",
>     num_train_epochs=3,
>     per_device_train_batch_size=8,
>     gradient_accumulation_steps=4,
>     learning_rate=2e-4,
>     bf16=True,
>     logging_steps=10
> )
>
> trainer = Trainer(
>     model=model,
>     args=training_args,
>     train_dataset=tokenized_dataset,
>     data_collator=DataCollatorForLanguageModeling(tokenizer, mlm=False)
> )
>
> trainer.train()
> model.save_pretrained("./lora_adapter")
> ```

## 9.5 Embedding Generation for RAG

**User:** "Generate embeddings for my documents"

**HuggingFace Expert:**
> **Embedding Pipeline:**
>
> ```python
> from sentence_transformers import SentenceTransformer
>
> model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
>
> # Single sentences
> embeddings = model.encode([
>     "What is machine learning?",
>     "Deep learning uses neural networks.",
>     "Natural language processing deals with text."
> ])
>
> # Document embedding
> def get_document_embedding(text, chunk_size=500):
>     chunks = [text[i:i+chunk_size] 
>               for i in range(0, len(text), chunk_size)]
>     chunk_embeddings = model.encode(chunks)
>     return chunk_embeddings.mean(axis=0)  # Average pooling
>
> # Similarity search
> import numpy as np
>
> def find_similar(query, documents, top_k=3):
>     query_emb = model.encode([query])
>     doc_embs = model.encode(documents)
>     
>     similarities = np.dot(doc_embs, query_emb.T).flatten()
>     top_indices = similarities.argsort()[-top_k:][::-1]
>     
>     return [(documents[i], similarities[i]) 
>             for i in top_indices]
> ```
