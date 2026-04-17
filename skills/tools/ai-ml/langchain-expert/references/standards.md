# Standards & Reference

## 7.1 Official Documentation

- [LangChain Documentation](https://python.langchain.com/docs)
- [LangChain Python API](https://api.python.langchain.com/)
- [LangChain Expression Language](https://python.langchain.com/docs/expression_language/)
- [LangChain Hub](https://smith.langchain.com/hub)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangChain Community](https://github.com/langchain-ai/langchain/tree/master/libs/community)

## 7.2 Installation

```bash
# Core LangChain
pip install langchain>=0.1.0
pip install langchain-core>=0.1.0
pip install langchain-community>=0.0.10

# Specific integrations
pip install langchain-openai>=0.0.5
pip install langchain-anthropic>=0.1.0
pip install langchain-google-vertexai>=0.0.5

# Vector stores
pip install faiss-cpu
pip install chromadb
pip install pgvector

# Document loaders
pip install pypdf
pip install unstructured

# Development
pip install langchain[dev]  # Includes all extras
```

## 7.3 Model Providers Reference

```python
# OpenAI
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
llm = ChatOpenAI(model="gpt-4", temperature=0.7)

# Anthropic
from langchain_anthropic import ChatAnthropic
llm = ChatAnthropic(model="claude-3-opus-20240229")

# Google Vertex AI
from langchain_google_vertexai import ChatVertexAI
llm = ChatVertexAI(model="gemini-pro")

# Azure OpenAI
from langchain_openai import AzureChatOpenAI
llm = AzureChatOpenAI(
    azure_deployment="gpt-4",
    api_version="2024-02-01"
)

# Local models (Ollama)
from langchain_community.chat_models import ChatOllama
llm = ChatOllama(model="llama2")
```

## 7.4 Prompt Templates

```python
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate

# Basic prompt template
prompt = PromptTemplate(
    template="Explain {topic} to a {audience}.",
    input_variables=["topic", "audience"]
)

# Chat prompt template
chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessagePromptTemplate.from_template("{question}")
])

# Few-shot prompt
few_shot_prompt = PromptTemplate(
    template="Input: {input}\nOutput: {output}",
    input_variables=["input", "output"],
    examples=[
        {"input": "Hello", "output": "Hi there!"},
        {"input": "Goodbye", "output": "See you later!"}
    ]
)
```

## 7.5 Chain Types Reference

| Chain Type | Use Case | Key Parameters |
|-----------|----------|----------------|
| LLMChain | Simple sequential logic | llm, prompt |
| ConversationChain | Chat with memory | llm, memory |
| RetrievalQA | Q&A over documents | llm, retriever |
| ConstitutionalChain | Apply principles | chains, principles |
| SelfAskWithSearchChain | Multi-step reasoning | llm, search_engine |

## 7.6 Vector Store Reference

```python
from langchain_community.vectorstores import Chroma, FAISS
from langchain_openai import OpenAIEmbeddings

# Chroma (persistent)
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=OpenAIEmbeddings(),
    persist_directory="./chroma_db"
)
vectorstore.persist()

# FAISS (in-memory)
vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=OpenAIEmbeddings()
)

# Retrieval
retriever = vectorstore.as_retriever(
    search_type="mmr",           # "similarity", "mmr"
    search_kwargs={"k": 4, "fetch_k": 20}
)
```

## 7.7 Memory Types Reference

```python
from langchain.memory import (
    ConversationBufferMemory,
    ConversationSummaryMemory,
    ConversationBufferWindowMemory,
    VectorStoreRetrieverMemory
)

# Simple buffer
memory = ConversationBufferMemory(memory_key="chat_history")

# With summary (for long conversations)
memory = ConversationSummaryMemory(llm=llm)

# Window (keep last N messages)
memory = ConversationBufferWindowMemory(k=5)

# Vector-backed (semantic retrieval)
memory = VectorStoreRetrieverMemory(retriever=retriever)
```
