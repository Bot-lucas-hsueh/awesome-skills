# Standard Workflow

## 8.1 RAG Application Workflow

```
Phase 1: Document Ingestion
├── Load documents (PDF, HTML, txt)
├── Split into chunks (RecursiveCharacterTextSplitter)
├── Generate embeddings (OpenAI, HuggingFace, etc.)
└── Store in vector database

Phase 2: Retrieval Setup
├── Choose retrieval method (similarity, MMR)
├── Configure top-k and score threshold
└── Test retrieval quality

Phase 3: Chain Assembly
├── Select LLM
├── Design prompt template
├── Configure chain type (stuff, refine, map_reduce)
└── Add optional post-processing

Phase 4: Evaluation
├── Test with sample queries
├── Check source documents
├── Iterate on chunking strategy
└── Tune retrieval parameters
```

## 8.2 Basic RAG Implementation

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Step 1: Load documents
loader = PyPDFLoader("document.pdf")
pages = loader.load()

# Step 2: Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    separators=["\n\n", "\n", " ", ""]
)
docs = splitter.split_documents(pages)

# Step 3: Create vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embeddings)

# Step 4: Configure retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)

# Step 5: Create prompt
template = """Use the following context to answer the question.
If you don't know the answer, say you don't know.

Context: {context}
Question: {question}
Answer:"""

prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)

# Step 6: Create QA chain
llm = ChatOpenAI(model="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt}
)

# Step 7: Query
result = qa_chain.invoke({"query": "What is the main topic?"})
```

## 8.3 Agent with Tools Workflow

```python
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.tools import Tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Define tools
def search_wikipedia(query: str) -> str:
    """Search Wikipedia for information."""
    from wikipedia import wikipedia
    return wikipedia.summary(query, sentences=2)

def calculator(expression: str) -> str:
    """Evaluate a mathematical expression."""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

tools = [
    Tool(
        name="wikipedia",
        func=search_wikipedia,
        description="Search Wikipedia for factual information"
    ),
    Tool(
        name="calculator",
        func=calculator,
        description="Calculate mathematical expressions"
    )
]

# Create agent
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

agent = create_openai_functions_agent(llm, tools, prompt)
executor = AgentExecutor.from_agent_and_tools(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

# Run agent
result = executor.invoke({"input": "What is the population of Tokyo?"})
```

## 8.4 Conversational RAG Workflow

```python
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# History-aware retriever
history_aware_retriever = create_history_aware_retriever(
    llm, retriever, prompt
)

# Create QA and history chains
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(
    history_aware_retriever, question_answer_chain
)

# Add chat history
message_history = ChatMessageHistory()

conversational_chain = RunnableWithMessageHistory(
    rag_chain,
    lambda session_id: message_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)

# Query with history
result = conversational_chain.invoke(
    {"input": "What is LangChain?"},
    config={"configurable": {"session_id": "user123"}}
)
```

## 8.5 LCEL (LangChain Expression Language) Workflow

```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4")
parser = StrOutputParser()

# Simple chain
prompt = ChatPromptTemplate.from_template(
    "Tell me a joke about {topic}"
)

chain = prompt | llm | parser

# Chain with multiple steps
full_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | parser
)

# Async chain
result = await chain.ainvoke({"topic": "programming"})

# Batch processing
results = chain.batch([
    {"topic": "cats"},
    {"topic": "dogs"}
])
```

## 8.6 Output Parsing Workflow

```python
from langchain.output_parsers import (
    PydanticOutputParser,
    CommaSeparatedListOutputParser,
    DatetimeOutputParser,
    JsonOutputParser
)
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

# Define output schema
class MovieReview(BaseModel):
    title: str = Field(description="Movie title")
    rating: float = Field(description="Rating from 1-10")
    summary: str = Field(description="Brief summary")
    genres: List[str] = Field(description="List of genres")

parser = PydanticOutputParser(pydantic_object=MovieReview)

prompt = PromptTemplate(
    template="Review the movie {movie}.\n{format_instructions}",
    input_variables=["movie"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | llm | parser
result = chain.invoke({"movie": "Inception"})
```
