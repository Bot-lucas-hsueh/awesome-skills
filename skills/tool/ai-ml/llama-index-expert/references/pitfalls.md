# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Fix |
|---|---------|----------|--------|-----|
| 1 | **Using default `SimpleDirectoryReader` without configuring chunk_size** | 🔴 High | Too-large or too-small chunks; poor retrieval precision/recall | Tune `chunk_size=512` and `chunk_overlap=50` based on document structure |
| 2 | **Not handling API key security** | 🔴 High | Exposed keys in code, logs, or git history | Use environment variables + dotenv; never log API keys |
| 3 | **Using `similarity_top_k=1` for complex queries** | 🟡 Medium | Misses relevant context; low recall | Use `similarity_top_k=5` or higher + reranking |
| 4 | **Ignoring token limits (context window)** | 🔴 High | Truncated responses, missing context | Use `response_mode="compact"` and monitor chunk sizes |
| 5 | **Storing raw PII in vector DB** | 🔴 High | GDPR/CCPA violations | Filter PII before indexing; use data masking |
| 6 | **Not persisting index between runs (rebuilding every time)** | 🟡 Medium | Slow startup, wasted API calls | Serialize index to disk or use cloud vector DB |
| 7 | **Using the same chunk_size for all document types** | 🟡 Medium | Code/docs get fragmented; long-form articles truncated | Use `SemanticSplitterNodeParser` or document-type-specific configs |
| 8 | **Not setting `show_progress=False` in production** | 🟡 Medium | Unnecessary thread overhead, log noise | Set `show_progress=False` in `from_documents()` |
| 9 | **Re-embedding on every query** | 🟡 Medium | Wasted API calls, high latency | Cache embeddings; use pre-computed embeddings where possible |
| 10 | **Ignoring metadata in retrieval** | 🟡 Medium | Cannot filter by date/source/category | Pass metadata at index time; use `MetadataFilters` at query time |

## 10.2 Anti-Patterns

### Anti-Pattern: Naive Chunking

```python
# BAD: Default chunking with no overlap
documents = SimpleDirectoryReader("./data").load_data()
# All documents chunked with default settings

# GOOD: Semantic chunking based on content structure
from llama_index.core.node_parser import SemanticSplitterNodeParser

splitter = SemanticSplitterNodeParser(
    buffer_size=1,
    breakpoint_percentile_threshold=95,
    embed_model=OpenAIEmbedding(model="text-embedding-3-small"),
)

# BETTER: Document-type-aware chunking
from llama_index.core.node_parser import (
    MarkdownNodeParser,
    HTMLNodeParser,
)

markdown_parser = MarkdownNodeParser(
    include_metadata=True,
    include_prev_next_rel=True,
)

nodes = markdown_parser.get_nodes_from_documents(markdown_docs)
```

### Anti-Pattern: No Query Filtering

```python
# BAD: Retrieve all documents regardless of metadata
query_engine = index.as_query_engine(similarity_top_k=10)

# GOOD: Filter by relevant metadata
from llama_index.core.vector_stores import MetadataFilter, MetadataFilters

query_engine = index.as_query_engine(
    similarity_top_k=5,
    filters=MetadataFilters(
        filters=[
            MetadataFilter(key="category", operator="==", value="technical"),
            MetadataFilter(key="date", operator=">=", value="2024-01-01"),
        ]
    ),
)
```

### Anti-Pattern: Storing Everything in Memory

```python
# BAD: Rebuilding index on every API call
@app.post("/query")
async def query(req: QueryRequest):
    docs = SimpleDirectoryReader("./data").load_data()
    index = VectorStoreIndex.from_documents(docs)  # Rebuilds every time!
    return index.as_query_engine().query(req.question)

# GOOD: Load index once at startup, reuse
index = None

@app.on_event("startup")
async def startup():
    global index
    documents = SimpleDirectoryReader("./data").load_data()
    index = VectorStoreIndex.from_documents(documents)

@app.post("/query")
async def query(req: QueryRequest):
    return index.as_query_engine().query(req.question)
```

### Anti-Pattern: Ignoring Token Counts

```python
# BAD: No token budget management
query_engine = index.as_query_engine(similarity_top_k=20)
response = query_engine.query("Explain everything about X")
# May exceed context window with large top_k

# GOOD: Compact mode with token budget
query_engine = index.as_query_engine(
    similarity_top_k=10,
    response_mode="compact",  # Packs as many text chunks as fit in context
    context_window=4096,       # Explicit token budget
    num_output=512,           # Reserve space for response
)
```

### Anti-Pattern: No Structured Output for Extraction Tasks

```python
# BAD: Free-form text extraction
response = query_engine.query(
    "Extract all person names mentioned in the document"
)
names = response.response  # Parse string — fragile

# GOOD: Structured extraction with Pydantic
from llama_index.core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

class PersonList(BaseModel):
    people: List[str]

parser = PydanticOutputParser(output_cls=PersonList)
query_engine = index.as_query_engine(
    output_parser=parser,
    respond_only=True,
)
response = query_engine.query("Extract all person names")
people: PersonList = parser.parse(str(response))
# people.people is a typed list
```

### Anti-Pattern: Skipping Evaluation

```python
# BAD: Deploying without measuring quality
query_engine = index.as_query_engine()
# "Looks good to me" — subjective, no baseline

# GOOD: Measure with RAGAS or TruLens
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy

eval_results = evaluate(
    eval_dataset,
    metrics=[faithfulness, answer_relevancy],
    llm=OpenAI(model="gpt-4o"),
)

# Track over time
if eval_results["faithfulness"] < 0.7:
    alert_team("Retrieval quality degraded!")
```

### Anti-Pattern: Hardcoding Prompt Templates

```python
# BAD: Fragile, hard to update
qa_prompt = """Answer based on context: {context}. Question: {query_str}"""

# GOOD: Use LlamaIndex PromptTemplate with customization
from llama_index.core import PromptTemplate

template = PromptTemplate(
    "Context information is below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context, answer the query.\n"
    "Query: {query_str}\n"
    "Answer: "
)

query_engine = index.as_query_engine(
    text_qa_template=template,
)
```

## 10.3 Performance Pitfalls

| Pitfall | Symptom | Solution |
|---------|---------|----------|
| **Slow embedding on large corpora** | Indexing takes hours | Batch embedding with `embed_batch_size=100`, use async pipeline |
| **High API costs** | LLM costs skyrocketing | Cache responses, use cheaper models for retrieval, enable `use_cache=True` |
| **Embedding model mismatch** | Poor retrieval quality | Use same embedding model for indexing and querying |
| **No async support** | Blocking I/O, low throughput | Use `VectorStoreIndex.from_documents_async()`, `query_engine.aquery()` |
| **Memory pressure from large indexes** | OOM on large documents | Use `VectorStoreIndex` with external vector DB (not in-memory), enable pagination |
| **Cold start latency** | Slow first query after deploy | Pre-warm index: call a dummy query at startup |
