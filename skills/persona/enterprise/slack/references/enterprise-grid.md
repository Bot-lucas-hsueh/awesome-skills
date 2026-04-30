# Enterprise Grid Guide

> Comprehensive guide to Slack's solution for large-scale organizations.

---

## Overview

Enterprise Grid connects multiple Slack workspaces into a single organization, enabling:
- Unified user identity across workspaces
- Cross-workspace collaboration
- Centralized administration and compliance

### Key Capabilities

| Feature | Description |
|---------|-------------|
| **Workspace Management** | Up to unlimited workspaces per org |
| **Shared Channels** | Collaborate across workspaces |
| **Unified Identity** | One profile, all workspaces |
| **Centralized Billing** | Single invoice for entire org |
| **Org-wide Controls** | Consistent policies everywhere |
| **Data Residency** | EU, US, AU, JP, CA, DE regions |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    ENTERPRISE GRID ORG                         │
│                     slack.enterprise.com                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  Workspace   │  │  Workspace   │  │  Workspace   │         │
│  │   (US-East)  │  │   (EU-West)  │  │  (APAC)      │         │
│  │              │  │              │  │              │         │
│  │  #general    │  │  #general    │  │  #general    │         │
│  │  #eng-ny     │  │  #eng-berlin │  │  #eng-tokyo  │         │
│  │  #sales-amer │  │  #sales-emea │  │  #sales-apac │         │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘         │
│         │                  │                  │                 │
│         └──────────────────┼──────────────────┘                 │
│                            │                                    │
│              ┌─────────────┴─────────────┐                      │
│              │      SHARED CHANNELS      │                      │
│              │                           │                      │
│              │  #company-announcements   │                      │
│              │  #leadership-updates      │                      │
│              │  #security-incidents      │                      │
│              │  #help-it                 │                      │
│              └───────────────────────────┘                      │
│                                                                  │
│  ORG-WIDE:                                                       │
│  • Single sign-on (SSO)                                         │
│  • Unified user directory                                       │
│  • Cross-workspace search                                       │
│  • Centralized app management                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Administration

### Org-level Settings

```json
{
  "enterprise": {
    "id": "E1234567890",
    "name": "Acme Corporation",
    "domain": "acme",
    
    "security": {
      "sso": {
        "provider": "okta",
        "enforced": true,
        "session_duration": 43200
      },
      "two_factor": {
        "required_for": ["admin", "owner"],
        "enforced_globally": false
      },
      "session_management": {
        "custom_duration": true,
        "max_duration": 2592000
      }
    },
    
    "compliance": {
      "data_residency": "multi_region",
      "retention": {
        "messages": "indefinite",
        "files": "7_years",
        "logs": "1_year"
      },
      "dlp": {
        "enabled": true,
        "patterns": [
          "credit_card",
          "ssn",
          "api_key"
        ]
      },
      "discovery": {
        "enabled": true,
        "export_formats": ["pdf", "json", "csv"]
      }
    }
  }
}
```

### Workspace Provisioning

```python
from slack_sdk import WebClient

class GridAdmin:
    def __init__(self, admin_token):
        self.client = WebClient(token=admin_token)
    
    def create_workspace(self, name, description, region):
        """Create new workspace in Grid organization"""
        response = self.client.admin_workspaces_create(
            team_name=name,
            team_description=description,
            region=region  # us, eu, au, jp, ca, de
        )
        return response["team_id"]
    
    def add_user_to_workspace(self, user_id, workspace_id):
        """Add existing org user to workspace"""
        return self.client.admin_users_assign(
            team_id=workspace_id,
            user_id=user_id
        )
    
    def create_shared_channel(self, name, workspace_ids):
        """Create channel shared across multiple workspaces"""
        # Create in primary workspace
        channel = self.client.conversations_create(
            name=name,
            is_private=False
        )
        channel_id = channel["channel"]["id"]
        
        # Share with other workspaces
        for ws_id in workspace_ids[1:]:
            self.client.admin_conversations_setTeams(
                channel_id=channel_id,
                target_team_ids=[ws_id],
                org_channel=True
            )
        
        return channel_id
```

---

## Migration Strategy

### From Single Workspace to Grid

```
Phase 1: Planning (Weeks 1-2)
├── Inventory existing channels
├── Identify workspace boundaries
├── Plan shared channel strategy
└── Communication plan

Phase 2: Setup (Weeks 3-4)
├── Create Grid organization
├── Configure SSO and security
├── Create workspaces
└── Set up shared channels

Phase 3: Migration (Weeks 5-8)
├── Migrate users in batches
├── Move channels to appropriate workspaces
├── Archive redundant channels
└── Update app configurations

Phase 4: Optimization (Weeks 9-12)
├── Monitor usage patterns
├── Refine workspace structure
├── Train power users
└── Gather feedback
```

### Channel Migration Script
```python
import json
from slack_sdk import WebClient

class GridMigration:
    def __init__(self, source_token, grid_admin_token):
        self.source = WebClient(token=source_token)
        self.grid = WebClient(token=grid_admin_token)
    
    def analyze_workspace(self):
        """Analyze existing workspace structure"""
        channels = self.source.conversations_list(
            types="public_channel,private_channel",
            exclude_archived=True
        )
        
        analysis = {
            "total_channels": 0,
            "by_prefix": {},
            "inactive": [],
            "shared_externally": []
        }
        
        for channel in channels["channels"]:
            analysis["total_channels"] += 1
            
            # Categorize by prefix
            prefix = channel["name"].split("-")[0]
            analysis["by_prefix"].setdefault(prefix, []).append(channel)
            
            # Check activity
            history = self.source.conversations_history(
                channel=channel["id"],
                limit=1
            )
            if history["messages"]:
                last_message = float(history["messages"][0]["ts"])
                # If older than 90 days, mark inactive
                import time
                if time.time() - last_message > 90 * 24 * 3600:
                    analysis["inactive"].append(channel)
            
            # Check if shared externally
            if channel.get("is_shared"):
                analysis["shared_externally"].append(channel)
        
        return analysis
    
    def generate_migration_plan(self, analysis):
        """Generate migration plan based on analysis"""
        plan = {
            "workspaces": {},
            "shared_channels": [],
            "archives": []
        }
        
        # Group channels by prefix for workspace assignment
        for prefix, channels in analysis["by_prefix"].items():
            if prefix in ["announcements", "general", "random"]:
                plan["shared_channels"].extend([c["id"] for c in channels])
            elif prefix in ["sales", "marketing", "support"]:
                plan["workspaces"].setdefault("go-to-market", []).extend(channels)
            elif prefix in ["eng", "dev", "infra"]:
                plan["workspaces"].setdefault("engineering", []).extend(channels)
            else:
                plan["workspaces"].setdefault("general", []).extend(channels)
        
        # Mark inactive for archival
        plan["archives"] = [c["id"] for c in analysis["inactive"]]
        
        return plan
```

---

## Security & Compliance

### Data Loss Prevention (DLP)

```python
def configure_dlp_policies(org_id):
    """Configure DLP policies for Grid org"""
    
    policies = [
        {
            "name": "Credit Card Detection",
            "pattern": r"\b(?:\d{4}[ -]?){3}\d{4}\b",
            "action": "flag",
            "notify": ["security@company.com"]
        },
        {
            "name": "API Key Detection",
            "pattern": r"(sk_live_|pk_live_|api[_-]?key)[\s:=]+['\"]?[a-zA-Z0-9]{32,}['\"]?",
            "action": "block",
            "message": "API keys should not be shared in Slack"
        },
        {
            "name": "SSN Detection",
            "pattern": r"\b\d{3}-\d{2}-\d{4}\b",
            "action": "flag",
            "auto_redact": True
        }
    ]
    
    return policies
```

### Audit Logging

```python
class GridAuditor:
    def __init__(self, token):
        self.client = WebClient(token=token)
    
    def get_audit_logs(self, start_date, end_date, actions=None):
        """Retrieve audit logs for compliance"""
        logs = []
        cursor = None
        
        while True:
            response = self.client.admin_auditLog(
                oldest=start_date,
                latest=end_date,
                action=actions,  # ['user_login', 'file_download', etc.]
                cursor=cursor
            )
            
            logs.extend(response.get("entries", []))
            cursor = response.get("response_metadata", {}).get("next_cursor")
            
            if not cursor:
                break
        
        return logs
    
    def generate_compliance_report(self, month):
        """Generate monthly compliance report"""
        import calendar
        
        # Get month range
        year, month_num = map(int, month.split("-"))
        _, last_day = calendar.monthrange(year, month_num)
        
        start = f"{month}-01 00:00:00"
        end = f"{month}-{last_day} 23:59:59"
        
        # Query audit logs
        logs = self.get_audit_logs(start, end)
        
        report = {
            "period": month,
            "total_events": len(logs),
            "by_action": {},
            "by_user": {},
            "suspicious_activities": []
        }
        
        for log in logs:
            action = log["action"]
            user = log["actor"]["user"]["name"]
            
            report["by_action"][action] = report["by_action"].get(action, 0) + 1
            report["by_user"][user] = report["by_user"].get(user, 0) + 1
            
            # Flag suspicious activities
            if action in ["user_password_reset", "owner_transferred"]:
                report["suspicious_activities"].append(log)
        
        return report
```

---

## Multi-Region Deployment

### Data Residency Configuration

```json
{
  "regions": {
    "primary": "us",
    "workspaces": [
      {
        "id": "T0001",
        "name": "acme-us",
        "region": "us",
        "data_residency": "aws-us-east-1"
      },
      {
        "id": "T0002",
        "name": "acme-eu",
        "region": "eu",
        "data_residency": "aws-eu-west-1",
        "compliance": ["GDPR"]
      },
      {
        "id": "T0003",
        "name": "acme-au",
        "region": "au",
        "data_residency": "aws-ap-southeast-2"
      }
    ],
    "shared_channels": {
      "region": "us",
      "replication": ["eu", "au"]
    }
  }
}
```

---

## Best Practices

### 1. Workspace Strategy
```
Recommended Structure:
├── Global (shared channels only)
│   ├── #company-announcements
│   └── #general
├── Engineering
│   ├── #eng-frontend
│   ├── #eng-backend
│   └── #eng-sre
├── Go-to-Market
│   ├── #sales-north-america
│   ├── #marketing
│   └── #customer-success
├── Regional
│   ├── #berlin-office
│   └── #tokyo-office
└── Project-Based (temporary)
    ├── #proj-2024-redesign
    └── #proj-api-migration
```

### 2. Channel Naming Conventions
```
#org-[name]          → Organization-wide channels
#ws-[workspace]-[name] → Workspace-specific
#proj-[name]          → Project channels (time-boxed)
#team-[name]          → Team channels
#ext-[partner]-[name] → External/Slack Connect
```

### 3. Access Control
- Use workspace membership for broad access
- Use private channels for sensitive topics
- Use user groups for role-based permissions
- Regular access reviews (quarterly)

### 4. Monitoring
- Track cross-workspace adoption
- Monitor shared channel usage
- Review app installations
- Audit external sharing
