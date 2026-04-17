# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | Using stuff chain with large documents | 🔴 High | Use map_reduce or refiner chain |
| 2 | Not setting retrieval k value | 🟡 Medium | Set appropriate k based on chunk size |
| 3 | Ignoring prompt injection risks | 🔴 High | Sanitize and validate inputs |
| 4 | Using deprecated LCAP / old chains | 🟡 Medium | Migrate to LCEL syntax |
| 5 | No source document tracking | 🟡 Medium | Enable document_retriever_chain |
| 6 | Hardcoding API keys | 🔴 High | Use environment variables |
| 7 | Not handling parsing errors | 🟡 Medium | Add error handling in output parsers |
| 8 | Ignoring token limits | 🔴 High | Monitor context length |
| 9 | Not caching expensive operations | 🟡 Medium | Use InMemoryCache or Redis |
| 10 | Missing conversation memory | 🟡 Medium | Add memory to chat chains |

## 10.2 Common Errors and Solutions

### Context Length Exceeded

```python
# Problem: Input exceeds model context limit
# Solution 1: Use map_reduce chain type
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="map_reduce",  # Process documents in batches
    retriever=retriever
)

# Solution 2: Use refine chain (sequential)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="refine",
    retriever=retriever
)

# Solution 3: Compress context before retrieval
from langchain.retrievers import ContextualCompressionRetriever
from langchain_cohere import CohereRerank

compressor = CohereRerank(model="rerank-multilingual-v2.0", top_n=3)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)
```

### Slow Retrieval

```python
# Problem: Slow vector search
# Solution: Optimize chunking and use MMR

retriever = vectorstore.as_retriever(
    search_type="mmr",  # Maximal Marginal Relevance
    search_kwargs={
        "k": 5,
        "fetch_k": 20,  # Fetch more, then select diverse
        "lambda_mult": 0.5  # Balance relevance vs diversity
    }
)

# Alternative: Use hybrid search
from langchain.retrievers import EnsembleRetriever

bm25_retriever = BM25Retriever.from_documents(docs)
vector_retriever = vectorstore.as_retriever()

ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.3, 0.7]
)
```

### Model Hallucination

```python
# Solution: Add source tracking and response validation

# Enable source documents in response
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True  # Return source docs
)

result = qa_chain.invoke({"query": "What is X?"})

# Validate against sources
if result["source_documents"]:
    sources = "\n".join([doc.page_content[:200] for doc in result["source_documents"]])
    print(f"Sources:\n{sources}")

# Use ConstitutionalChain for self-correction
from langchain.chains import ConstitutionalChain

principles = [
    "The response should not invent information not in the context."
]

constitutional_chain = ConstitutionalChain.from_llm(
    llm=llm,
    constitutional_principles=principles,
    chain=qa_chain
)
```

## 10.3 Memory Best Practices

```python
# Don't use BufferMemory for long conversations
# Use SummaryMemory instead

from langchain.memory import ConversationSummaryMemory

memory = ConversationSummaryMemory(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    memory_key="chat_history",
    return_messages=True
)

# Clear memory when needed
memory.clear()

# Check token usage
from langchain.memory.token_buffer import TokenBufferMemory

memory = TokenBufferMemory(
    llm=llm,
    max_token_limit=2000
)
```

## 10.4 Token Optimization

```python
# Estimate tokens before sending
def count_tokens(text: str, model: str = "gpt-4") -> int:
    """Rough token estimation."""
    return len(text) // 4  # ~4 chars per token

# Trim long contexts
MAX_TOKENS = 6000  # Leave room for response

def truncate_context(context: str) -> str:
    if count_tokens(context) > MAX_TOKENS:
        # Truncate to fit
        max_chars = MAX_TOKENS * 4
        return context[:max_chars]
    return context

# Use shorter context
prompt = PromptTemplate(
    template="Context: {context}\nQuestion: {question}",
    input_variables=["context", "question"]
)
```

## 10.5 Security Best Practices

```python
# Never hardcode API keys
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not set")

# Sanitize user inputs for SQL agents
from langchain_community.agent_toolkits import create_sql_agent

# Configure allowed tables and SQL execution
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    allowed_tools=["schema", "list_tables", "query"],
    top_k=10
)

# Use read-only database connection
db = SQLDatabase.from_uri(
    "postgresql://user:pass@host/db",
    include_tables=["orders", "customers"]  # Whitelist tables
)
```
