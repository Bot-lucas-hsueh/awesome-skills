# Now Assist & AI Integration

## Overview
Now Assist is ServiceNow's generative AI platform, embedded across all workflows.

## Now Assist Capabilities

### For ITSM
| Feature | Description |
|---------|-------------|
| Incident Summarization | Auto-generate incident summaries |
| Resolution Notes | Draft resolution notes for agents |
| Code Generation | Generate scripts and queries |
| Knowledge Article | Auto-create from resolved incidents |

### For HRSD
| Feature | Description |
|---------|-------------|
| Case Summarization | Summarize employee cases |
| Response Generation | Draft responses to employees |
| Knowledge Search | AI-powered knowledge discovery |

### For Creator
| Feature | Description |
|---------|-------------|
| Flow Generation | Create flows from natural language |
| Script Assistance | Generate and explain scripts |
| Form Builder | Suggest form layouts |

## Predictive Intelligence

### Capabilities
- **Categorization:** Auto-categorize incidents/requests
- **Routing:** Intelligent assignment
- **Resolution:** Suggest solutions from knowledge
- **Similarity:** Find similar records

### Configuration
```yaml
Setup Steps:
  1. Enable ML Framework plugin
  2. Define prediction targets
  3. Train models with historical data
  4. Set confidence thresholds
  5. Deploy to production

Model Types:
  - Classification: Categorize, route
  - Similarity: Find similar records
  - Regression: Predict resolution time
```

## Virtual Agent

### NLU Models
```yaml
Intent Detection:
  - Password Reset
  - Software Request
  - Access Request
  - Incident Creation

Entity Extraction:
  - Application names
  - User IDs
  - Dates
  - Priority levels
```

### Conversation Flow
```
User: "I need to reset my password"
  ↓
Intent: password_reset (confidence: 0.95)
  ↓
Action: Trigger Password Reset flow
  ↓
Virtual Agent: "I've initiated a password reset. Check your email..."
```

## Integration Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   NOW ASSIST                             │
├─────────────────────────────────────────────────────────┤
│  User Interface: Chat, Forms, Portals                   │
├─────────────────────────────────────────────────────────┤
│  AI Services:                                           │
│  • Natural Language Processing                          │
│  • Text Generation                                      │
│  • Code Generation                                      │
│  • Summarization                                        │
├─────────────────────────────────────────────────────────┤
│  Now LLM: ServiceNow's multimodal model                 │
│  (Can process text, images, structured data)            │
├─────────────────────────────────────────────────────────┤
│  Enterprise Data: CMDB, Workflows, Knowledge            │
└─────────────────────────────────────────────────────────┘
```

## Implementation Best Practices

### Data Privacy
- AI models respect ACLs
- Data stays within tenant
- No training on customer data without opt-in

### Change Management
```yaml
Rollout Strategy:
  1. Pilot with power users
  2. Measure adoption and satisfaction
  3. Gather feedback
  4. Expand to broader audience
  5. Continuous improvement

Success Metrics:
  - Self-service rate increase
  - Average handle time reduction
  - Agent satisfaction scores
  - Knowledge article usage
```

### Prompt Engineering
```yaml
Good Prompts:
  - Specific and contextual
  - Include relevant record data
  - Set output format expectations
  - Provide examples

Example:
  "Summarize this incident for an executive:
   Number: {number}
   Description: {short_description}
   Work notes: {work_notes}
   Format: 3 bullet points, max 50 words each"
```

## Licensing
- Now Assist is a premium SKU
- Priced per user or per use case
- Available as add-on to existing products
- Pro Plus includes full Now Assist capabilities
