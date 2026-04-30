# Scenario Examples

## 9.1 Real-World Use Cases

### Multi-Modal RAG Pipeline

**User:** "Build a RAG system that can answer questions about images in documents"

**Expert:**
```python
from llama_index.core import SimpleDirectoryReader
from llama_index.core.schema import ImageNode
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import MultiModalVectorIndexRetriever

# Load documents with images
documents = SimpleDirectoryReader(
    input_dir="./research",
    recursive=True,
    filename_as_id=True,
).load_data()

# Create multi-modal index
mm_llm = OpenAIMultiModal(
    model="gpt-4o",
    api_key="sk-...",
)

# Multi-modal embedding for images
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.embeddings.openai import OpenAIEmbedding

# Build index (stores both text and image embeddings)
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=OpenAIEmbedding(model="text-embedding-3-small"),
)

# Retrieve both text and image nodes
retriever = MultiModalVectorIndexRetriever(
    index=index,
    similarity_top_k=5,
)

# Query engine that uses retrieved images
query_engine = index.as_query_engine(
    similarity_top_k=5,
    multi_modal_llm=mm_llm,
)

response = query_engine.query(
    "What does the architecture diagram show?"
)
# Response includes analysis of both text and images
```

### Agentic RAG with Query Planning

**User:** "Build a RAG system where the LLM can decide when to query the vector store vs use tools"

**Expert:**
```python
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load and index documents
documents = SimpleDirectoryReader("./docs").load_data()
index = VectorStoreIndex.from_documents(documents)

# Create tools
query_engine = index.as_query_engine(similarity_top_k=5)

vector_tool = QueryEngineTool(
    query_engine=query_engine,
    metadata=ToolMetadata(
        name="search_docs",
        description="Search the documentation for information. "
                    "Use this when user asks about specific topics.",
    ),
)

# Calculator tool
from llama_index.core.tools import FunctionTool
import math

def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

calc_tool = FunctionTool.from_defaults(
    fn=calculator,
    name="calculator",
    description="Calculate mathematical expressions. Input: expression string.",
)

# Create ReAct agent
agent = ReActAgent.from_tools(
    tools=[vector_tool, calc_tool],
    llm=OpenAI(model="gpt-4o"),
    verbose=True,
)

response = agent.chat(
    "What is the compound interest on $10,000 at 5% for 10 years? "
    "Also find the definition of RAG from the docs."
)
```

### Structured Output Extraction

**User:** "Extract structured data (invoices) from PDFs using RAG"

**Expert:**
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class LineItem(BaseModel):
    description: str = Field(description="Item description")
    quantity: int = Field(description="Number of items")
    unit_price: float = Field(description="Price per unit")
    total: float = Field(description="Line item total")

class Invoice(BaseModel):
    invoice_number: str = Field(description="Invoice number")
    date: str = Field(description="Invoice date")
    vendor: str = Field(description="Vendor name")
    total_amount: float = Field(description="Total amount due")
    line_items: List[LineItem] = Field(description="List of line items")

parser = PydanticOutputParser(output_cls=Invoice)

from llama_index.core import PromptTemplate

template = """\
Extract the invoice information from the document.

{format_str}

Document: {context}
"""

prompt = PromptTemplate(
    template=template,
    output_parser=parser,
)

query_engine = index.as_query_engine(
    similarity_top_k=1,
)

response = query_engine.query(
    "Extract the invoice data including invoice number, date, vendor, "
    "line items, and total amount."
)

structured: Invoice = parser.parse(str(response))
print(f"Invoice #{structured.invoice_number}")
print(f"Vendor: {structured.vendor}")
print(f"Total: ${structured.total_amount}")
for item in structured.line_items:
    print(f"  - {item.description}: {item.quantity} × ${item.unit_price}")
```

### Query Decomposition (Sub-Questions)

**User:** "Answer complex questions by breaking them into sub-queries"

**Expert:**
```python
from llama_index.core import VectorStoreIndex
from llama_index.core.query_engine import SubQuestionQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata

# Create multiple indexes for different sources
finance_docs = SimpleDirectoryReader("./finance").load_data()
legal_docs = SimpleDirectoryReader("./legal").load_data()

finance_index = VectorStoreIndex.from_documents(finance_docs)
legal_index = VectorStoreIndex.from_documents(legal_docs)

# Create tools for each
tools = [
    QueryEngineTool(
        query_engine=finance_index.as_query_engine(),
        metadata=ToolMetadata(
            name="finance",
            description="Financial documents, reports, and filings",
        ),
    ),
    QueryEngineTool(
        query_engine=legal_index.as_query_engine(),
        metadata=ToolMetadata(
            name="legal",
            description="Legal contracts, agreements, and policies",
        ),
    ),
]

# Sub-question engine automatically decomposes
query_engine = SubQuestionQueryEngine.from_defaults(
    query_engine_tools=tools,
    llm=OpenAI(model="gpt-4o"),
)

response = query_engine.query(
    "What are the financial implications of the indemnification clause "
    "in the service agreement?"
)
# Automatically: queries finance index for financial implications
#             queries legal index for indemnification clause details
#             synthesizes final answer
```

## 9.2 Scaling Scenarios

### Scaling to Millions of Documents

| Scale | Strategy | Architecture |
|-------|----------|-------------|
| < 1,000 docs | Single ChromaDB instance, in-memory | All-in-one (loader → chunker → embedder → query) |
| 1K-100K docs | Pinecone/Qdrant cloud, embedding cache | Separate ingestion pipeline, batch embedding |
| 100K-1M docs | Qdrant with sharding, async embedding | Distributed workers, chunk queue (Kafka/Redis) |
| 1M+ docs | Hybrid search (vector + BM25), reranking | Multi-index with metadata routing |

### Distributed Ingestion Pipeline

```python
# Ingestion worker (can be horizontally scaled)
from llama_index.core import Document
from llama_index.core.ingestion import IngestionPipeline
from llama_index.transformers.openai import OpenAIEmbedding
import redis
import json

redis_client = redis.Redis(host="redis", port=6379)
embedding_model = OpenAIEmbedding(model="text-embedding-3-small")

pipeline = IngestionPipeline.from_defaults(
    transformations=[
        SentenceSplitter(chunk_size=512, chunk_overlap=50),
        embedding_model,
    ],
    vector_store=QdrantVectorStore(collection_name="docs"),
)

def process_document_task(task: dict):
    doc = Document(
        text=task["text"],
        metadata=task["metadata"],
    )
    pipeline.run(documents=[doc])

# Worker loop (run multiple instances)
while True:
    task = redis_client.blpop("embedding_queue")
    process_document_task(json.loads(task))
```

### Hybrid Search (Vector + Keyword)

```python
from llama_index.core.retrievers import QueryFusionRetriever
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.query_engine import RetrieverQueryEngine

# Vector index
vector_index = VectorStoreIndex.from_documents(documents)
vector_retriever = vector_index.as_retriever(similarity_top_k=10)

# BM25 / keyword index
from llama_index.core import KeywordIndex
keyword_index = KeywordIndex.from_documents(documents)
keyword_retriever = keyword_index.as_retriever(similarity_top_k=10)

# Fusion retriever (combine both)
fusion_retriever = QueryFusionRetriever(
    retrievers=[vector_retriever, keyword_retriever],
    mode=QueryFusionRetriever.Mode.RELATIVE_SCORE,
    similarity_top_k=5,
    num_queries=1,
)

query_engine = RetrieverQueryEngine.from_args(
    fusion_retriever,
    llm=OpenAI(model="gpt-4o"),
)
```

## 9.3 Integration Scenarios

### LlamaIndex + LangChain

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.query_engine import RetrieverQueryEngine

# Use LlamaIndex for indexing and retrieval
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)

# Use LangChain for the LLM chain
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda

lc_llm = ChatOpenAI(model="gpt-4o", temperature=0.1)

def get_retriever(query: str) -> str:
    response = index.as_query_engine().query(query)
    return "\n\n".join([n.node.text for n in response.source_nodes])

chain = RunnableLambda(get_retriever) | lc_llm | (lambda x: x.content)

result = chain.invoke("What is the main topic of the documents?")
```

### LlamaIndex + LangGraph (Agentic Workflow)

```python
from langgraph.graph import StateGraph, END
from llama_index.core import VectorStoreIndex
from typing import TypedDict

class AgentState(TypedDict):
    question: str
    context: str
    answer: str
    needs_clarification: bool

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

def retrieve(state: AgentState) -> AgentState:
    response = query_engine.query(state["question"])
    state["context"] = "\n\n".join([n.node.text for n in response.source_nodes])
    return state

def answer(state: AgentState) -> AgentState:
    prompt = f"Based on this context:\n{state['context']}\n\nAnswer: {state['question']}"
    response = llm.invoke(prompt)
    state["answer"] = response.content
    return state

graph = StateGraph(AgentState)
graph.add_node("retrieve", retrieve)
graph.add_node("answer", answer)
graph.add_edge("retrieve", "answer")
graph.add_edge("answer", END)
graph.set_entry_point("retrieve")
app = graph.compile()
```

### Document Warehousing (Multi-Index Query)

```python
from llama_index.core import VectorStoreIndex, SummaryIndex
from llama_index.core.query_engine import MultiIndexQueryEngine
from llama_index.core.selectors import LLMMultiSelector

# Create both a vector index and a summary index
vector_index = VectorStoreIndex.from_documents(documents)
summary_index = SummaryIndex.from_documents(documents)

# Multi-index query engine picks the best approach
query_engine = MultiIndexQueryEngine(
    indexes=[vector_index, summary_index],
    selector=LLMMultiSelector.from_defaults(),
)

# For factual questions: uses vector index (retrieval)
# For summarization: uses summary index
response = query_engine.query("Summarize the key points of the report")
```
