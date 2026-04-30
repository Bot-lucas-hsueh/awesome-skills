# Agent Swarm Guide

> Building autonomous multi-agent systems with Kimi K2.5's Agent Swarm capabilities.

## What is Agent Swarm?

Agent Swarm is Kimi K2.5's capability to decompose complex tasks into parallel sub-tasks executed by dynamically instantiated, domain-specific agents.

```
Traditional: Single model → Sequential reasoning → Output
             [A] → [B] → [C] → [D]

Agent Swarm: Manager model → Task decomposition → Parallel execution
             ┌─→ [Agent 1] ─┐
    [Query] ─┼─→ [Agent 2] ─┼─→ [Synthesis] → Output
             ├─→ [Agent 3] ─┤
             └─→ [Agent 4] ─┘
```

### Key Innovations

1. **Dynamic Agent Instantiation**: Creates agents on-demand for specific sub-tasks
2. **Proactive Context Control**: Reduces context overflow without summarization
3. **Parallel Execution**: 200-300 sequential tool calls with stable performance
4. **Self-Directed Coordination**: Agents coordinate without predefined workflows

## Architecture

```
┌─────────────────────────────────────────────┐
│           User Query                        │
└──────────────┬──────────────────────────────┘
               ↓
┌─────────────────────────────────────────────┐
│        Manager Agent (Kimi K2.5)            │
│  • Analyzes query complexity                │
│  • Determines decomposition strategy        │
│  • Instantiates specialized agents          │
└──────────────┬──────────────────────────────┘
               ↓
┌─────────────────────────────────────────────┐
│         Agent Pool                          │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐        │
│  │Research │ │Code     │ │Analysis │  ...   │
│  │Agent    │ │Agent    │ │Agent    │        │
│  └────┬────┘ └────┬────┘ └────┬────┘        │
│       └───────────┼───────────┘              │
│                   ↓                          │
│            Parallel Execution                │
└───────────────────┬──────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│        Result Synthesis                     │
│  • Aggregate agent outputs                  │
│  • Resolve conflicts                        │
│  • Generate final response                  │
└─────────────────────────────────────────────┘
```

## Agent Types

### 1. Research Agent

```python
class ResearchAgent:
    """Specialized for information gathering"""
    
    def __init__(self):
        self.tools = [WebSearch(), BrowseWebsite(), ReadPDF()]
    
    def execute(self, query: str) -> ResearchResult:
        # Parallel web search across multiple sources
        sources = self.tools[0].search(query, num_results=20)
        
        # Browse top sources in parallel
        contents = parallel_map(
            self.tools[1].browse, 
            sources[:10]
        )
        
        # Synthesize findings
        return self.synthesize(contents)
```

### 2. Code Agent

```python
class CodeAgent:
    """Specialized for code generation and debugging"""
    
    def __init__(self):
        self.tools = [CodeExecutor(), Linter(), TestRunner()]
    
    def execute(self, task: CodingTask) -> CodeResult:
        # Generate code
        code = self.generate(task.description)
        
        # Lint and fix
        lint_errors = self.tools[1].lint(code)
        code = self.fix_errors(code, lint_errors)
        
        # Test
        test_results = self.tools[2].run_tests(code, task.tests)
        
        return CodeResult(code=code, tests=test_results)
```

### 3. Analysis Agent

```python
class AnalysisAgent:
    """Specialized for data analysis and visualization"""
    
    def __init__(self):
        self.tools = [DataLoader(), StatisticalAnalyzer(), ChartGenerator()]
    
    def execute(self, data: DataSource, question: str) -> AnalysisResult:
        # Load data
        df = self.tools[0].load(data)
        
        # Analyze
        stats = self.tools[1].analyze(df, question)
        
        # Generate visualizations
        charts = self.tools[2].generate(stats)
        
        return AnalysisResult(statistics=stats, visualizations=charts)
```

## Implementation with Kimi K2.5

### Basic Swarm Pattern

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_MOONSHOT_API_KEY",
    base_url="https://api.moonshot.cn/v1"
)

def agent_swarm(query: str) -> str:
    """Use Kimi K2.5's built-in Agent Swarm capability"""
    
    response = client.chat.completions.create(
        model="kimi-k2.5",  # Agent Swarm enabled
        messages=[{
            "role": "user",
            "content": query
        }],
        tools=[
            {"type": "web_search"},
            {"type": "code_interpreter"},
            {"type": "file_reader"}
        ],
        # K2.5 automatically determines:
        # - Whether to use Agent Swarm
        # - How many agents to spawn
        # - Task decomposition strategy
    )
    
    return response.choices[0].message.content

# Example: Complex research task
result = agent_swarm("""
Research the impact of AI on healthcare in 2025.
I need:
1. Clinical applications (diagnosis, treatment)
2. Economic impact (cost savings, market size)
3. Ethical considerations (privacy, bias)
4. Technical challenges (data quality, integration)

Compile a comprehensive report with citations.
""")
```

### Custom Agent Definition

```python
# Define specialized agents via function calling
functions = [
    {
        "name": "research_agent",
        "description": "Gathers information from web sources",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "sources": {"type": "array", "items": {"type": "string"}},
                "depth": {"type": "string", "enum": ["shallow", "medium", "deep"]}
            },
            "required": ["query"]
        }
    },
    {
        "name": "analysis_agent",
        "description": "Analyzes data and extracts insights",
        "parameters": {
            "type": "object",
            "properties": {
                "data": {"type": "string"},
                "analysis_type": {"type": "string", "enum": ["trend", "comparison", "anomaly"]}
            },
            "required": ["data", "analysis_type"]
        }
    },
    {
        "name": "synthesis_agent",
        "description": "Combines multiple analyses into coherent output",
        "parameters": {
            "type": "object",
            "properties": {
                "inputs": {"type": "array", "items": {"type": "string"}},
                "output_format": {"type": "string", "enum": ["report", "summary", "presentation"]}
            },
            "required": ["inputs"]
        }
    }
]

response = client.chat.completions.create(
    model="kimi-k2.5",
    messages=[{"role": "user", "content": complex_query}],
    functions=functions,
    function_call="auto"  # Let K2.5 decide when to call agents
)
```

## Benchmarks

### BrowseComp (Web Research)

| Model | Score |
|-------|-------|
| Kimi K2.5 | 78.4% |
| GPT-5.2 Pro | 75.2% |
| Claude Opus 4.5 | 72.1% |

### WideSearch (Deep Research)

| Model | Score |
|-------|-------|
| Kimi K2.5 | 82.3% |
| GPT-5.2 Pro | 79.1% |
| Claude Opus 4.5 | 76.8% |

### Humanity's Last Exam (HLE)

| Model | Score (with tools) |
|-------|-------------------|
| Kimi K2.5 | 50.2% |
| Claude Opus 4.5 | 34.2% |
| GPT-5 | 24.9% |

## Best Practices

### 1. Task Decomposition

```python
def decompose_task(query: str) -> List[SubTask]:
    """Break complex query into parallel sub-tasks"""
    
    # Let K2.5 analyze and decompose
    analysis = client.chat.completions.create(
        model="kimi-k2.5",
        messages=[{
            "role": "user",
            "content": f"""Decompose this query into parallel sub-tasks:
            
            Query: {query}
            
            Output format: JSON array of sub-tasks with:
            - task_id
            - description
            - agent_type (research|code|analysis|creative)
            - dependencies (list of task_ids)
            """
        }],
        response_format={"type": "json_object"}
    )
    
    return json.loads(analysis.choices[0].message.content)["subtasks"]
```

### 2. Context Management

```python
class SwarmContextManager:
    """Proactive context control for long-running agent swarms"""
    
    def __init__(self, max_context: int = 256000):
        self.max_context = max_context
        self.agent_contexts = {}
    
    def allocate_context(self, agent_id: str, priority: int):
        """Dynamically allocate context budget to agents"""
        base_allocation = self.max_context // len(self.agent_contexts)
        
        # Priority agents get more context
        if priority > 5:
            return int(base_allocation * 1.5)
        return base_allocation
    
    def compress_if_needed(self, agent_id: str):
        """Compress context before overflow"""
        current_tokens = self.count_tokens(agent_id)
        if current_tokens > self.max_context * 0.9:
            self.summarize_and_archive(agent_id)
```

### 3. Result Aggregation

```python
def aggregate_results(agent_outputs: List[AgentOutput]) -> str:
    """Synthesize multiple agent outputs into coherent response"""
    
    synthesis_prompt = f"""
    Synthesize the following agent outputs into a coherent response:
    
    {'\n\n---\n\n'.join(f"Agent {i+1}:\n{output.content}" 
                      for i, output in enumerate(agent_outputs))}
    
    Guidelines:
    - Resolve any conflicting information
    - Maintain logical flow
    - Cite which agent provided which information
    - Add an executive summary at the top
    """
    
    response = client.chat.completions.create(
        model="kimi-k2.5",
        messages=[{"role": "user", "content": synthesis_prompt}]
    )
    
    return response.choices[0].message.content
```

## Use Cases

### 1. Comprehensive Research Report

```
Query: "Analyze the state of quantum computing in 2025"

Swarm Execution:
├─ Research Agent 1: Technical advances (hardware, algorithms)
├─ Research Agent 2: Commercial applications (finance, pharma)
├─ Research Agent 3: Key players (IBM, Google, startups)
├─ Analysis Agent: Market size projections
└─ Synthesis Agent: Compile comprehensive report

Result: 20-page report with citations, charts, and recommendations
```

### 2. Code Architecture Review

```
Query: "Review this microservices architecture"

Swarm Execution:
├─ Code Agent 1: Analyze API design patterns
├─ Code Agent 2: Check security vulnerabilities
├─ Code Agent 3: Evaluate scalability bottlenecks
├─ Analysis Agent: Cost estimation
└─ Synthesis Agent: Prioritized recommendations

Result: Detailed review with actionable fixes
```

### 3. Multi-Document Analysis

```
Query: "Compare Q1-Q4 earnings reports across 5 companies"

Swarm Execution:
├─ Research Agent 1: Extract Q1 data
├─ Research Agent 2: Extract Q2 data
├─ Research Agent 3: Extract Q3 data
├─ Research Agent 4: Extract Q4 data
├─ Analysis Agent: Comparative analysis
└─ Synthesis Agent: Investment recommendations

Result: Comparative dashboard + written analysis
```

## Limitations

| Limitation | Description | Mitigation |
|------------|-------------|------------|
| Tool call limit | 200-300 stable sequential calls | Batch operations, cache results |
| Context per agent | Shared 256K context | Use k2.5-long (2M) for deep tasks |
| Coordination overhead | Agent communication adds latency | Minimize agent count, optimize routing |
| Result quality variance | Agent outputs may vary in quality | Implement quality gates, retry logic |

## Future Directions

1. **Hierarchical Swarms**: Manager agents spawning sub-manager agents
2. **Persistent Agents**: Long-lived agents with memory across sessions
3. **Cross-Model Swarms**: Kimi agents collaborating with other models
4. **Specialized Training**: Fine-tuned expert agents for specific domains

---

*Agent Swarm guide for Kimi K2.5 | Updated: 2026-03-21*
