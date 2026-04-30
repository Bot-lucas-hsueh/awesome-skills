# Scenario Examples

## 9.1 SQL Agent for Database Queries

**User:** "Build an agent that can query a database"

**LangChain Expert:**
> **SQL Agent Implementation:**
>
> ```python
> from langchain_community.agent_toolkits import create_sql_agent
> from langchain_community.utilities import SQLDatabase
> from langchain_openai import ChatOpenAI
>
> # Connect to database
> db = SQLDatabase.from_uri("sqlite:///Chinook.db")
>
> # Create agent
> agent_executor = create_sql_agent(
>     llm=ChatOpenAI(model="gpt-4", temperature=0),
>     db=db,
>     verbose=True,
>     top_k=10
> )
>
> # Query natural language
> result = agent_executor.invoke(
>     "What are the top 5 albums by sales amount?"
> )
>
> # The agent will:
> # 1. Identify the question intent
> # 2. Inspect database schema
> # 3. Write and execute SQL
> # 4. Return results
> ```

## 9.2 Multi-Modal Document Analysis

**User:** "Analyze PDFs with tables and images"

**LangChain Expert:**
> **Multi-Modal Pipeline:**
>
> ```python
> from langchain_community.document_loaders import UnstructuredPDFLoader
> from langchain_openai import ChatOpenAI
>
> # Load PDF with tables
> loader = UnstructuredPDFLoader("document.pdf", mode="elements")
> docs = loader.load()
>
> # Separate text and tables
> text_docs = [d for d in docs if d.metadata["type"] == "text"]
> table_docs = [d for d in docs if d.metadata["type"] == "table"]
>
> # Process tables with structured extraction
> from langchain_experimental.tabular_synthetic_data import (
>     create_synthetic_tabular_data
> )
>
> # Analyze each element
> for doc in table_docs:
>     # Extract table data
>     table_data = doc.page_content
>     analysis_prompt = f"Analyze this table: {table_data}"
>     response = llm.invoke(analysis_prompt)
> ```

## 9.3 Tool Calling with OpenAI

**User:** "Use function calling with GPT-4"

**LangChain Expert:**
> **Tool Calling Implementation:**
>
> ```python
> from langchain_openai import ChatOpenAI
> from langchain_core.tools import tool
> from langchain_core.messages import HumanMessage
>
> @tool
> def get_weather(location: str) -> str:
>     """Get current weather for a location."""
>     # Actual weather API call
>     return f"Weather in {location}: Sunny, 72°F"
>
> llm = ChatOpenAI(model="gpt-4-0613")
>
> # Bind tools to model
> llm_with_tools = llm.bind_tools([get_weather])
>
> # First call
> messages = [HumanMessage(content="What's the weather in Paris?")]
> response = llm_with_tools.invoke(messages)
>
> # Response contains tool call
> print(response.tool_calls)
> # [{'name': 'get_weather', 'args': {'location': 'Paris'}, 'id': '...'}]
>
> # Execute tool
> tool_result = get_weather.invoke(response.tool_calls[0]["args"])
>
> # Continue conversation with result
> messages.append(response)
> messages.append(HumanMessage(content="", tool_call_id=response.tool_calls[0]["id"],
>                               name="get_weather"))
> final_response = llm_with_tools.invoke(messages)
> ```

## 9.4 Streaming Chat Interface

**User:** "Build a streaming chat interface"

**LangChain Expert:**
> **Streaming Implementation:**
>
> ```python
> from langchain_openai import ChatOpenAI
> from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
>
> llm = ChatOpenAI(
>     model="gpt-4",
>     streaming=True,
>     callbacks=[StreamingStdOutCallbackHandler()]
> )
>
> # For async streaming
> async def stream_response():
>     from langchain_core.callbacks import AsyncIteratorCallbackHandler
>
>     handler = AsyncIteratorCallbackHandler()
>
>     async_llm = ChatOpenAI(
>         model="gpt-4",
>         streaming=True,
>         callbacks=[handler]
>     )
>
>     async def run():
>         task = asyncio.create_task(
>             async_llm.agenerate(["Tell me about quantum computing"])
>         )
>         async for token in handler.aiter():
>             print(token, end="", flush=True)
>         await task
>
>     await run()
> ```

## 9.5 Evaluation Framework

**User:** "Evaluate RAG system quality"

**LangChain Expert:**
> **RAG Evaluation Pipeline:**
>
> ```python
> from langchain.evaluation import (
>     load_evaluator,
>     ContextualCompressionEvaluator
> )
> from langchain.evaluation.criteria import LabeledCriteriaCriterionFramework
>
> # Create evaluators
> # Faithfulness evaluator
> faithfulness_evaluator = load_evaluator(
>     "faithfulness",
>     llm=llm
> )
>
> # Answer relevance evaluator
> relevance_evaluator = load_evaluator(
>     "answer_relevance",
>     llm=llm
> )
>
> # Evaluate RAG chain
> test_questions = [
>     "What is LangChain?",
>     "How do I create an agent?",
>     "What are vector stores?"
> ]
>
> results = []
> for question in test_questions:
>     answer = qa_chain.invoke({"query": question})
>
>     faithfulness = faithfulness_evaluator.evaluate_strings(
>         input=question,
>         prediction=answer["result"]
>     )
>
>     relevance = relevance_evaluator.evaluate_strings(
>         input=question,
>         prediction=answer["result"]
>     )
>
>     results.append({
>         "question": question,
>         "answer": answer["result"],
>         "faithfulness": faithfulness,
>         "relevance": relevance
>     })
> ```
