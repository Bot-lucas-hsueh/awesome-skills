# Standard Workflow

## 8.1 Development Workflow (Local → Production)

```
LlamaIndex RAG Development
├── 1. Environment Setup
│   ├── pip install llama-index (with extras: openai, chromadb, qdrant)
│   ├── Set API keys as environment variables (OPENAI_API_KEY, etc.)
│   └── Configure .env file with dotenv (NEVER commit to git)
│
├── 2. Data Ingestion
│   ├── Load documents (PDF, DOCX, TXT, HTML, Notion, Slack, etc.)
│   ├── Parse & extract text with LlamaReaders
│   ├── Split into chunks (SentenceSplitter, TokenTextSplitter)
│   └── Store in vector database (ChromaDB for dev, Qdrant/Pinecone for prod)
│
├── 3. Index Building
│   ├── Choose index type (VectorStoreIndex for RAG, SummaryIndex for summarization)
│   ├── Configure embedding model (OpenAI, HuggingFace local)
│   └── Set chunk_size, overlap based on document structure
│
├── 4. Query Engine Configuration
│   ├── Select similarity_top_k (3-10 typically)
│   ├── Choose response_mode (compact, refine, tree_summarize)
│   ├── Add postprocessors (reranking, similarity filtering)
│   └── Test with diverse query types
│
└── 5. Production Deployment
    ├── Containerize (Docker with GPU if using local models)
    ├── Deploy to cloud (Vercel, AWS Lambda, Azure Container Apps)
    ├── Set up proper API key management (Vault, AWS Secrets Manager)
    └── Implement rate limiting and caching
```

### Local Development with Dotenv

```bash
# .env (NEVER commit this file)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
PINECONE_API_KEY=...
QDRANT_API_KEY=...
```

```python
# config.py
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

import os
os.environ["OPENAI_API_KEY"]  # Available after load_dotenv
```

### Document Processing Pipeline

```python
from llama_index.core import Document
from llama_index.core.node_parser import (
    SentenceSplitter,
    SemanticSplitterNodeParser,
)
from llama_index.readers.file import PDFReader, DocxReader, MarkdownReader

# Option 1: Use built-in SimpleDirectoryReader
documents = SimpleDirectoryReader(
    input_dir="./data",
    filename_as_id=True,
    recursive=True,
).load_data()

# Option 2: Custom readers with metadata
pdf_reader = PDFReader()
custom_docs = []
for file in Path("./research").glob("*.pdf"):
    doc = pdf_reader.load_data(file=file)[0]
    doc.metadata = {
        "source": file.name,
        "category": "research",
        "year": 2024,
    }
    custom_docs.append(doc)

# Semantic chunking (better for RAG)
splitter = SemanticSplitterNodeParser(
    buffer_size=1,
    breakpoint_percentile_threshold=95,
    embed_model=OpenAIEmbedding(model="text-embedding-3-small"),
)
nodes = splitter.get_nodes_from_documents(documents)
```

## 8.2 Deployment / Production Workflow

```
Production Deployment
├── 1. Index Persistence
│   ├── Option A: Serialize index to disk (VectorStoreIndex.store_index)
│   ├── Option B: Cloud vector DB (Qdrant, Pinecone, Weaviate Cloud)
│   └── Option C: Redis + persistence (for small-scale)
│
├── 2. API Service
│   ├── FastAPI wrapper around query engine
│   ├── Async endpoints for better throughput
│   ├── Request validation (Pydantic models)
│   └── Structured output with output parsers
│
├── 3. Caching Strategy
│   ├── Embedding cache (disk-based, hash of text)
│   ├── LLM response cache (Redis, TTL=1hr)
│   └── Query result cache (similarity hash)
│
└── 4. Observability
    ├── Log query + response + latency
    ├── Track token usage (per-request cost)
    ├── Monitor embedding quality (relevance scores)
    └── Alert on high error rates
```

### FastAPI Deployment

```python
# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.query_engine import CitationQueryEngine
import os

app = FastAPI(title="RAG API", version="1.0")

# Load index at startup
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(similarity_top_k=5)

class QueryRequest(BaseModel):
    question: str
    top_k: int | None = 5

@app.post("/query")
async def query(req: QueryRequest):
    try:
        response = query_engine.query(req.question)
        return {
            "answer": str(response),
            "sources": [
                {"text": n.node.text[:200], "metadata": n.node.metadata}
                for n in response.source_nodes
            ],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok"}

# Run: uvicorn api:app --host 0.0.0.0 --port 8000
```

### Docker Configuration

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV PORT=8000

EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Async Query Engine

```python
import asyncio
from llama_index.core import VectorStoreIndex

class AsyncRAGService:
    def __init__(self, index: VectorStoreIndex):
        self.query_engine = index.as_query_engine(
            similarity_top_k=5,
            response_mode="compact",
        )

    async def query(self, question: str) -> dict:
        # Wrap sync query in async
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None, self.query_engine.query, question
        )
        return {
            "answer": str(response),
            "source_nodes": [
                {"text": n.node.text, "score": n.score}
                for n in response.source_nodes
            ],
        }
```

## 8.3 Monitoring & Evaluation

```
RAG Observability Stack
├── Tracing (OpenTelemetry)
│   ├── LlamaIndex callbacks for span tracing
│   ├── LLM token usage per request
│   └── Embedding latency
│
├── Evaluation
│   ├── Faithfulness (does answer match retrieved docs?)
│   ├── Answer Relevancy (does answer match question?)
│   ├── Context Precision & Recall
│   └── RAGAS metrics
│
└── Analytics
    ├── Query logs (question, answer, latency, cost)
    ├── Retrieval quality (avg similarity score)
    └── User feedback (thumbs up/down)
```

### Callback Tracing

```python
from llama_index.core.callbacks import (
    CallbackManager,
    LlamaDebugHandler,
    CBEventType,
)
from llama_index.core.callbacks.schema import CBEvent

llama_debug = LlamaDebugHandler(
    event_starts_to_ignore=[CBEventType.SCHEDULE],
    event_ends_to_ignore=[CBEventType.SCHEDULE],
)

Settings.callback_manager = CallbackManager([llama_debug])

# All LlamaIndex operations will be traced
query_engine.query("What is RAG?")
# Output:
# DEBUG: Event: CHUNKING - Duration: 0.123s
# DEBUG: Event: EMBEDDING_CREATE - Duration: 0.456s
# DEBUG: Event: LLM_CALL - Duration: 1.234s
```

### RAG Evaluation with RAGAS

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
)
from datasets import Dataset

eval_data = Dataset.from_dict({
    "user_input": ["question1", "question2"],
    "retrieved_contexts": [["context1"], ["context2"]],
    "response": ["answer1", "answer2"],
    "reference": ["expected1", "expected2"],
})

result = evaluate(
    eval_data,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
)
result.to_pandas()
```

### Token Usage Tracking

```python
from llama_index.core.callbacks.base import CallbackHandler

class TokenUsageHandler(CallbackHandler):
    def __init__(self):
        self.total_tokens = 0
        self.prompt_tokens = 0
        self.completion_tokens = 0

    def on_event_end(self, event_type, payload):
        if event_type == CBEventType.LLM:
            usage = payload.get("usage", {})
            self.prompt_tokens += usage.get("prompt_tokens", 0)
            self.completion_tokens += usage.get("completion_tokens", 0)
            self.total_tokens += usage.get("total_tokens", 0)

    def get_summary(self):
        return {
            "total_tokens": self.total_tokens,
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "estimated_cost_usd": (self.prompt_tokens / 1e6 * 0.15) + (self.completion_tokens / 1e6 * 0.6),
        }
```
