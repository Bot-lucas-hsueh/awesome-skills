# python Example

```
def build_deploy_message(status, environment, deployer, version):
    status_emoji = "✅" if status == "success" else "❌"
    status_text = "Successful" if status == "success" else "Failed"
    
    return {
        "blocks": [
            {
                "type": "header",
                "text": {"type": "plain_text", "text": f"🚀 Deploy {status_text} — {environment}"}
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*Environment:*\n{environment}"},
                    {"type": "mrkdwn", "text": f"*Version:*\n{version}"},
                    {"type": "mrkdwn", "text": f"*Deployed by:*\n{deployer}"},
                    {"type": "mrkdwn", "text": f"*Status:*\n{status_emoji} {status_text}"}
                ]
            },
            {"type": "divider"},
            {
                "type": "actions",
                "elements": [
                    {"type": "button", "text": {"type": "plain_text", "text": "View Logs"}, "url": f"https://logs.example.com/{version}"},
                    {"type": "button", "text": {"type": "plain_text", "text": "Rollback"}, "action_id": "rollback"}
                ]
            }
        ]
    }

def standup_form_blocks():
    return [
        {"type": "input", "block_id": "yesterday", "label": {"type": "plain_text", "text": "What did you do yesterday?"}, "element": {"type": "plain_text_input", "action_id": "yesterday_input", "multiline": True}},
        {"type": "input", "block_id": "today", "label": {"type": "plain_text", "text": "What will you do today?"}, "element": {"type": "plain_text_input", "action_id": "today_input", "multiline": True}},
        {"type": "input", "block_id": "blockers", "label": {"type": "plain_text", "text": "Any blockers?"}, "element": {"type": "plain_text_input", "action_id": "blockers_input", "multiline": True}}
    ]

def incident_form_modal():
    return {
        "type": "modal",
        "callback_id": "incident_modal",
        "title": {"type": "plain_text", "text": "Create Incident"},
        "submit": {"type": "plain_text", "text": "Create"},
        "blocks": [
            {"type": "input", "block_id": "title_block", "label": {"type": "plain_text", "text": "Title"}, "element": {"type": "plain_text_input", "action_id": "title_input"}},
            {"type": "input", "block_id": "severity_block", "label": {"type": "plain_text", "text": "Severity"}, "element": {"type": "static_select", "action_id": "severity_input", "options": [
                {"text": {"type": "plain_text", "text": "P1 - Critical"}, "value": "P1"},
                {"text": {"type": "plain_text", "text": "P2 - High"}, "value": "P2"},
                {"text": {"type": "plain_text", "text": "P3 - Medium"}, "value": "P3"}
            ]}}
        ]
    }
```
