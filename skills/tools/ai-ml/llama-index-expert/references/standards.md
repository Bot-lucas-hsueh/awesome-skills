# Standards & Reference

## 7.1 Official Documentation

- [LlamaIndex Documentation](https://docs.llamaindex.ai/en/latest/)
- [LlamaIndex API Reference](https://docs.llamaindex.ai/en/latest/api_reference/)
- [LlamaIndex GitHub](https://github.com/run-llama/llama_index)
- [LlamaIndex Discord Community](https://discord.gg/llamaindex)
- [LlamaIndex Cookbooks (Examples)](https://github.com/run-llama/llama-cookbook)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Sentence Transformers (HuggingFace)](https://www.sbert.net/docs/sentence_transformer/)
- [Qdrant Vector DB](https://qdrant.tech/documentation/)
- [Weaviate Documentation](https://weaviate.io/developers/weaviate)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Pinecone Documentation](https://docs.pinecone.io/)
- [Redis Stack (Vector Search)](https://redis.io/docs/interact/search-and-query/)

## 7.2 Configuration Reference

### Basic LlamaIndex Setup

```python
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings,
    PromptTemplate,
)
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.storage.storage_context import StorageContext
import chromadb

# LLM Configuration
Settings.llm = OpenAI(
    model="gpt-4o",
    temperature=0.1,
    max_tokens=1024,
    api_key="sk-...",
)

# Embedding Configuration
Settings.embed_model = OpenAIEmbedding(
    model="text-embedding-3-small",
    api_key="sk-...",
)

# Global chunk settings
Settings.chunk_size = 512
Settings.chunk_overlap = 50
```

### Vector Store Configuration

```python
# ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = chroma_client.get_or_create_collection("documents")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

# Qdrant
from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client

qdrant_client = qdrant_client.QdrantClient(host="localhost", port=6333)
vector_store = QdrantVectorStore(
    collection_name="documents",
    client=qdrant_client,
    enable_rotation=True,
    distance_func="Cosine",
)

# Pinecone
from llama_index.vector_stores.pinecone import PineconeVectorStore
import pinecone

pinecone.init(api_key="...", environment="us-east-1")
vector_store = PineconeVectorStore(
    index_name="production-index",
    pinecone_parser=None,
)

# Weaviate
from llama_index.vector_stores.weaviate import WeaviateVectorStore
import weaviate

auth_config = weaviate.AuthApiKey(api_key="...")
client = weaviate.Client(url="http://localhost:8080", auth_client_secret=auth_config)
vector_store = WeaviateVectorStore(
    weaviate_client=client,
    index_name="Document",
    text_key="content",
)
```

### Index Configuration

```python
from llama_index.core import (
    VectorStoreIndex,
    SummaryIndex,
    TreeIndex,
    KeywordTableIndex,
)

# Vector Index (semantic search)
index = VectorStoreIndex.from_documents(
    documents,
    vector_store=vector_store,
    show_progress=True,
    include_embeddings=True,
)

# Summary Index (LLM-based summarization)
summary_index = SummaryIndex.from_documents(documents)

# Tree Index (hierarchical summarization)
tree_index = TreeIndex.from_documents(documents)

# Keyword Table Index (exact keyword match)
keyword_index = KeywordTableIndex.from_documents(documents)
```

### Service Context (Advanced)

```python
from llama_index.core import ServiceContext
from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

service_context = ServiceContext.from_defaults(
    llm=Anthropic(model="claude-3-5-sonnet-20241022"),
    embed_model=HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5"),
    chunk_size=1024,
    chunk_overlap=128,
    context_window=4096,
    num_output=512,
    wrapper_limit=10,
)

# Use with specific index
index = VectorStoreIndex.from_documents(
    documents,
    service_context=service_context,
)
```

## 7.3 Common Commands / Patterns

### Basic RAG Pipeline

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load documents
documents = SimpleDirectoryReader(
    input_dir="./data",
    recursive=True,
    required_exts=[".pdf", ".docx", ".txt", ".md", ".html"],
    exclude=["*.tmp"],
).load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine(
    similarity_top_k=3,
    vector_store_query_mode="default",
    alpha=None,
    verbose=True,
)

response = query_engine.query("What are the key findings from the report?")
print(response)
print(f"Sources: {[n.node.metadata for n in response.source_nodes]}")
```

### Query Engines with Filters

```python
from llama_index.core.vector_stores import MetadataFilter, MetadataFilters

query_engine = index.as_query_engine(
    similarity_top_k=5,
    filters=MetadataFilters(
        filters=[
            MetadataFilter(key="category", operator="==", value="research"),
            MetadataFilter(key="year", operator=">=", value=2023),
        ]
    ),
    response_mode="compact",
    refine_template=PromptTemplate(...),
)

response = query_engine.query("What methodology was used?")
```

### Async Operations

```python
import asyncio
from llama_index.core import VectorStoreIndex

async def build_index_async():
    index = await VectorStoreIndex.from_documents_async(documents)
    return index

async def query_async(index, query):
    query_engine = index.as_query_engine()
    return await query_engine.aquery(query)

async def main():
    index = await build_index_async()
    response = await query_async(index, "Summarize the main points")
    print(response)

asyncio.run(main())
```

### Multi-Document Query Engine

```python
from llama_index.core import VectorStoreIndex
from llama_index.core.tools import QueryEngineTool, ToolMetadata

tools = [
    QueryEngineTool(
        query_engine=reports_index.as_query_engine(),
        metadata=ToolMetadata(
            name="quarterly_reports",
            description="Financial reports from Q1-Q4 2024",
        ),
    ),
    QueryEngineTool(
        query_engine=policy_index.as_query_engine(),
        metadata=ToolMetadata(
            name="policy_documents",
            description="Internal company policies and procedures",
        ),
    ),
]

from llama_index.core.query_engine import RouterQueryEngine
from llama_index.core.selectors import LLMSingleSelector

query_engine = RouterQueryEngine(
    selector=LLMSingleSelector(),
    tools=tools,
)
```

### ReRanker Integration

```python
from llama_index.core.postprocessor import SentenceTransformerRerank

postprocessor = SentenceTransformerRerank(
    model="cross-encoder/ms-marco-MiniLM-L-12-v2",
    top_n=3,
    device="cpu",
)

query_engine = index.as_query_engine(
    similarity_top_k=10,
    node_postprocessors=[postprocessor],
)
```

## 7.4 Version Compatibility

| LlamaIndex | Status | Python | LLM Support |
|------------|--------|--------|-------------|
| 0.11.x | Latest | 3.9+ | OpenAI, Anthropic, Gemini, Ollama, Azure, Cohere |
| 0.10.x | Stable | 3.8+ | OpenAI, Anthropic, Ollama, Azure |
| 0.9.x | Legacy | 3.8+ | OpenAI, Azure |
| 0.8.x | EOL | 3.8+ | OpenAI only |

| Component | Min Version | Notes |
|-----------|-------------|-------|
| openai | 1.0+ | Required for LlamaIndex 0.10+ |
| tiktoken | 0.4+ | Token counting |
| anthropic | 0.25+ | Claude models |
| chromadb | 0.4+ | Local vector store |
| qdrant-client | 1.7+ | Qdrant integration |
| llama-index-vector-stores-\* | Match LlamaIndex | Specific vector DB |
| llama-index-llms-\* | Match LlamaIndex | Specific LLM |

| Embedding Model | Dim | Notes |
|-----------------|-----|-------|
| text-embedding-3-small | 1536 | OpenAI, cost-efficient |
| text-embedding-3-large | 3072 | OpenAI, higher quality |
| text-embedding-ada-002 | 1536 | Legacy, still supported |
| bge-small-en-v1.5 | 512 | HuggingFace, local |
| bge-base-en-v1.5 | 768 | HuggingFace, local |
| sentence-transformers/all-MiniLM-L6-v2 | 384 | Fast, local |
