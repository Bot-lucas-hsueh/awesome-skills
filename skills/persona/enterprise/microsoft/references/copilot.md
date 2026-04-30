# Microsoft Copilot Reference

## Copilot Product Family

### Microsoft 365 Copilot
- **Users**: 100M+ monthly active
- **Pricing**: $30/user/month (requires E3/E5 license)
- **Key Features**:
  - Document generation (Word, PowerPoint)
  - Data analysis (Excel)
  - Email drafting (Outlook)
  - Meeting summaries (Teams)
  - Enterprise search (Business Chat)

### GitHub Copilot
- **Users**: 15M+ total, 4.7M+ paid subscribers
- **Pricing**:
  - Individual: $10/month or $100/year
  - Business: $19/user/month
  - Enterprise: $39/user/month
- **Capabilities**:
  - Code completion
  - Copilot Chat (natural language coding)
  - Copilot Workspace (task-oriented coding)
  - Copilot CLI (command line assistance)

### Security Copilot
- **Target**: SOC analysts, security teams
- **Integration**: Microsoft Sentinel, Defender
- **Capabilities**:
  - Threat investigation
  - Incident response
  - Threat intelligence
  - Natural language queries

### Copilot Studio
- **Organizations**: 230,000+ using it
- **Agents Created**: 1M+ custom agents
- **Features**:
  - No-code/low-code agent builder
  - Custom knowledge sources
  - Power Platform integration
  - Enterprise governance

## Plugin Development

### Manifest Structure
```json
{
  "name": "CRM Plugin",
  "description": "Access customer data",
  "functions": [
    {
      "name": "getCustomer",
      "description": "Retrieve customer by ID",
      "parameters": {
        "customerId": {
          "type": "string",
          "description": "Customer identifier"
        }
      }
    }
  ]
}
```

### Authentication Options
| Method | Use Case |
|--------|----------|
| OAuth 2.0 | User-delegated access |
| API Key | Service-to-service |
| SSO | Enterprise integration |

### Response Format
```json
{
  "type": "AdaptiveCard",
  "body": [
    {
      "type": "TextBlock",
      "text": "Customer Details"
    },
    {
      "type": "FactSet",
      "facts": [
        {"title": "Name:", "value": "Contoso Inc"},
        {"title": "Revenue:", "value": "$50M"}
      ]
    }
  ],
  "actions": [
    {
      "type": "Action.Submit",
      "title": "View Full Profile"
    }
  ]
}
```

## Agent Architecture

### Types of Agents
| Type | Description | Example |
|------|-------------|---------|
| Declarative | Rule-based, workflow | Expense approval |
| Custom | AI-powered, conversational | Sales assistant |
| Autonomous | Goal-driven, multi-step | Project coordinator |

### Agent Components
```
Trigger
├── Intent recognition
├── Entity extraction
├── Action selection
├── External API calls
├── Response generation
└── Follow-up handling
```

## Prompt Engineering Best Practices

### System Prompts
- Be specific about role and context
- Define output format clearly
- Include examples (few-shot)
- Set boundaries and constraints

### Safety Considerations
- Implement content filtering
- Add human oversight loops
- Monitor for jailbreak attempts
- Log all interactions

## Integration Points

### Microsoft Graph
```
GET https://graph.microsoft.com/v1.0/me
Authorization: Bearer {token}
```

### Teams Integration
- Message extensions
- Task modules
- Conversational bots
- Proactive messaging

### Outlook Integration
- Compose add-ins
- Read add-ins
- Meeting extensions

---

**Last Updated**: 2026-03-21
