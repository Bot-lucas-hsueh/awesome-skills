# Block Kit Guide

> Complete guide to Slack's UI framework for rich, interactive messages.

---

## Block Kit Basics

Block Kit is a JSON-based UI framework for building app surfaces in Slack.

```json
{
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Hello, world!"
      }
    }
  ]
}
```

### Block Types Overview

| Block | Purpose | Max per Message |
|-------|---------|-----------------|
| `section` | Text with optional accessory | 100 |
| `divider` | Visual separator | 100 |
| `image` | Image display | 100 |
| `actions` | Interactive elements | 100 |
| `context` | Metadata/accessory elements | 100 |
| `file` | File display | 100 |
| `header` | Large header text | 100 |
| `video` | Embedded video | 100 |
| `rich_text` | Rich text formatting | 100 |
| `input` | Form input fields | - |

---

## Core Blocks

### Section Block

```json
{
  "type": "section",
  "text": {
    "type": "mrkdwn",
    "text": "*Bold* and _italic_ text with <https://slack.com|links>"
  },
  "fields": [
    {
      "type": "mrkdwn",
      "text": "*Priority:*\nHigh"
    },
    {
      "type": "mrkdwn",
      "text": "*Status:*\nIn Progress"
    }
  ],
  "accessory": {
    "type": "button",
    "text": {
      "type": "plain_text",
      "text": "View"
    },
    "value": "view_123"
  }
}
```

### Header Block

```json
{
  "type": "header",
  "text": {
    "type": "plain_text",
    "text": "🚀 Deployment Status",
    "emoji": true
  }
}
```

### Context Block

```json
{
  "type": "context",
  "elements": [
    {
      "type": "image",
      "image_url": "https://example.com/user.png",
      "alt_text": "User avatar"
    },
    {
      "type": "mrkdwn",
      "text": "Posted by <@U123456>"
    }
  ]
}
```

---

## Interactive Components

### Buttons

```json
{
  "type": "actions",
  "elements": [
    {
      "type": "button",
      "text": {
        "type": "plain_text",
        "text": "Approve",
        "emoji": true
      },
      "style": "primary",
      "value": "approve_123",
      "action_id": "approve_request"
    },
    {
      "type": "button",
      "text": {
        "type": "plain_text",
        "text": "Reject",
        "emoji": true
      },
      "style": "danger",
      "value": "reject_123",
      "action_id": "reject_request"
    },
    {
      "type": "button",
      "text": {
        "type": "plain_text",
        "text": "Learn More"
      },
      "url": "https://example.com"
    }
  ]
}
```

**Button Styles:**
- `primary` - Green
- `danger` - Red
- Default - White

### Select Menus

```json
{
  "type": "section",
  "text": {
    "type": "mrkdwn",
    "text": "Select an option:"
  },
  "accessory": {
    "type": "static_select",
    "placeholder": {
      "type": "plain_text",
      "text": "Select an item"
    },
    "options": [
      {
        "text": {
          "type": "plain_text",
          "text": "Option 1"
        },
        "value": "option_1"
      }
    ],
    "action_id": "select_option"
  }
}
```

**Select Types:**
| Type | Use Case |
|------|----------|
| `static_select` | Predefined options |
| `external_select` | Dynamic options via API |
| `users_select` | User selection |
| `conversations_select` | Channel selection |
| `channels_select` | Public channel selection |
| `multi_*_select` | Multiple selections |

### Input Fields

```json
{
  "type": "input",
  "block_id": "title_block",
  "element": {
    "type": "plain_text_input",
    "action_id": "title_input",
    "placeholder": {
      "type": "plain_text",
      "text": "Enter a title"
    }
  },
  "label": {
    "type": "plain_text",
    "text": "Title"
  },
  "hint": {
    "type": "plain_text",
    "text": "Max 100 characters"
  }
}
```

**Input Types:**
| Element | Description |
|---------|-------------|
| `plain_text_input` | Single/multi-line text |
| `checkboxes` | Multiple checkboxes |
| `radio_buttons` | Single selection |
| `datepicker` | Date picker |
| `timepicker` | Time picker |
| `number_input` | Numeric input |
| `url_text_input` | URL input |
| `email_text_input` | Email input |

---

## Composition Objects

### Text Objects

```json
// Mrkdwn
{
  "type": "mrkdwn",
  "text": "*Bold* _italic_ `code` ~strikethrough~",
  "verbatim": false
}

// Plain Text
{
  "type": "plain_text",
  "text": "Hello World",
  "emoji": true
}
```

### Confirmation Dialog

```json
{
  "confirm": {
    "title": {
      "type": "plain_text",
      "text": "Are you sure?"
    },
    "text": {
      "type": "mrkdwn",
      "text": "This action cannot be undone."
    },
    "confirm": {
      "type": "plain_text",
      "text": "Yes, delete"
    },
    "deny": {
      "type": "plain_text",
      "text": "Cancel"
    },
    "style": "danger"
  }
}
```

### Option Groups

```json
{
  "type": "static_select",
  "option_groups": [
    {
      "label": {
        "type": "plain_text",
        "text": "Group 1"
      },
      "options": [...]
    }
  ]
}
```

---

## Surface Types

### Messages

```json
{
  "channel": "C1234567890",
  "blocks": [...],
  "text": "Fallback text for notifications"
}
```

### Modals

```json
{
  "trigger_id": "1234567890.123456",
  "view": {
    "type": "modal",
    "callback_id": "modal_submit",
    "title": {
      "type": "plain_text",
      "text": "Create Task"
    },
    "submit": {
      "type": "plain_text",
      "text": "Create"
    },
    "close": {
      "type": "plain_text",
      "text": "Cancel"
    },
    "blocks": [...]
  }
}
```

### Home Tab

```json
{
  "user_id": "U1234567890",
  "view": {
    "type": "home",
    "blocks": [
      {
        "type": "section",
        "text": {
          "type": "mrkdwn",
          "text": "Welcome to your app home!"
        }
      }
    ]
  }
}
```

### App Surface Limits

| Surface | Block Limit | Character Limits |
|---------|-------------|------------------|
| Message | 100 blocks | 3,000 text |
| Modal | 100 blocks | 5,000 title |
| Home | 100 blocks | 3,000 text |

---

## Best Practices

### 1. Progressive Disclosure
```json
[
  {
    "type": "section",
    "text": {
      "type": "mrkdwn",
      "text": "*Deployment Complete* ✅"
    }
  },
  {
    "type": "actions",
    "elements": [
      {
        "type": "button",
        "text": {"type": "plain_text", "text": "View Details"},
        "value": "show_details"
      }
    ]
  }
]
// On click, update with full details
```

### 2. Consistent Patterns
- Use `callback_id` for modal identification
- Use `action_id` for interactive elements
- Group related actions in `actions` blocks

### 3. Accessibility
- Always provide `alt_text` for images
- Use `plain_text` for critical information
- Include fallback text in messages

### 4. Error Handling
```json
{
  "response_action": "errors",
  "errors": {
    "title_block": "Title is required and must be unique"
  }
}
```
