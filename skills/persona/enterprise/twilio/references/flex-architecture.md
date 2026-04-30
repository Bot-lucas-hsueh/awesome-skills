# Twilio Flex Architecture Guide

## Flex Platform Overview

Twilio Flex is a **fully programmable cloud contact center platform** built on React and Redux. It provides:

- **Omnichannel**: Voice, chat, SMS, WhatsApp, email in unified interface
- **Programmability**: Every pixel customizable via plugins
- **Scale**: Supports thousands of concurrent agents
- **Integration**: Native CRM connectors, custom APIs

## Architecture Components

### Runtime Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     AGENT WORKSTATION                            │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐ │
│  │  Flex UI     │ │  Headset     │ │  CRM Integration         │ │
│  │  (Browser)   │ │  (WebRTC)    │ │  (Salesforce, etc.)      │ │
│  └──────┬───────┘ └──────────────┘ └──────────────────────────┘ │
└─────────┼───────────────────────────────────────────────────────┘
          │ WebSocket (WSS)
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    TWILIO CLOUD PLATFORM                         │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐ │
│  │  Sync        │ │  Conversations│ │  TaskRouter              │ │
│  │  (State)     │ │  (Channels)   │ │  (Routing)               │ │
│  └──────────────┘ └──────────────┘ └──────────────────────────┘ │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐ │
│  │  Voice       │ │  Studio       │ │  Functions               │ │
│  │  (PSTN/SIP)  │ │  (Flows)      │ │  (Business Logic)        │ │
│  └──────────────┘ └──────────────┘ └──────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Inbound Interaction** → Phone number or messaging endpoint
2. **Studio Flow** → IVR, data dip, queue selection
3. **TaskRouter** → Skills-based routing to appropriate agent
4. **Flex UI** → Agent receives task, accepts, handles interaction
5. **CRM** → Screen pop, activity logging
6. **Post-Call** → Wrap-up, disposition, survey

## Flex UI Architecture

### Component Hierarchy

```
MainContainer
├── RootContainer
│   ├── MainHeader
│   │   ├── UserCard
│   │   ├── MainHeaderNotifications
│   │   └── MainHeaderMenu
│   ├── Sidebar
│   │   └── SideNavigation
│   ├── AgentDesktopView
│   │   ├── TaskList
│   │   │   └── TaskListItem
│   │   ├── TaskCanvas
│   │   │   ├── TaskCanvasHeader
│   │   │   ├── TaskInfoPanel
│   │   │   ├── MessagingCanvas (Chat/SMS)
│   │   │   │   └── MessageListItem
│   │   │   └── CallCanvas (Voice)
│   │   │       └── CallControls
│   │   └── CRMContainer
│   └── SupervisorDesktopView
│       ├── TeamsView
│       ├── QueueStats
│       └── RealTimeStats
```

### Plugin Architecture

**Plugin Entry Point**:
```javascript
import { FlexPlugin } from '@twilio/flex-plugin';

export default class MyPlugin extends FlexPlugin {
  name = 'MyPlugin';

  init(flex, manager) {
    // Plugin initialization
    this.registerComponents(flex);
    this.configureActions(flex);
    this.setupEventHandlers(manager);
  }
}
```

**Plugin Capabilities**:

| Capability | API | Use Case |
|------------|-----|----------|
| Add Components | `flex.*.add()` | Custom UI elements |
| Replace Components | `flex.*.replace()` | Override default behavior |
| Remove Components | `flex.*.remove()` | Hide unwanted elements |
| Modify Actions | `flex.Actions.replaceAction()` | Custom business logic |
| Add Actions | `flex.Actions.registerAction()` | New functionality |
| Event Handling | `manager.*.on()` | React to state changes |
| Redux State | `manager.store` | Access/modify state |

## TaskRouter Integration

### Workflow Configuration

```json
{
  "task_routing": {
    "filters": [
      {
        "filter_friendly_name": "Sales Queue",
        "expression": "selected_product=='sales'",
        "targets": [
          {
            "queue": "WQ_sales",
            "priority": 5,
            "timeout": 300,
            "expression": "skills HAS 'sales'"
          }
        ]
      },
      {
        "filter_friendly_name": "Support Queue",
        "expression": "selected_product=='support'",
        "targets": [
          {
            "queue": "WQ_support_tier1",
            "priority": 3,
            "timeout": 60,
            "expression": "skills HAS 'support' AND support_tier=='1'"
          },
          {
            "queue": "WQ_support_tier2",
            "priority": 2,
            "timeout": 120,
            "expression": "skills HAS 'support' AND support_tier=='2'"
          }
        ]
      }
    ],
    "default_filter": {
      "queue": "WQ_general"
    }
  }
}
```

### Skills-Based Routing

**Worker Attributes**:
```json
{
  "contact_uri": "client:agent_001",
  "full_name": "Jane Smith",
  "image_url": "https://.../avatar.jpg",
  "skills": ["sales", "premium_support", "spanish"],
  "languages": ["en", "es"],
  "support_tier": "2",
  "department": "customer_success",
  "max_tasks": 3
}
```

**Task Attributes**:
```json
{
  "selected_product": "support",
  "customer_tier": "premium",
  "language": "es",
  "issue_type": "billing",
  "customer_value": 50000,
  "callback_number": "+1234567890"
}
```

**Routing Expression Operators**:

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal | `language == 'en'` |
| `!=` | Not equal | `tier != 'basic'` |
| `<` `>` | Comparison | `customer_value > 10000` |
| `IN` | In array | `skills IN ['sales', 'support']` |
| `HAS` | Array contains | `skills HAS 'spanish'` |
| `AND` `OR` | Logical | `skills HAS 'sales' AND tier == 'premium'` |

## Studio Integration

### Common Flow Patterns

**IVR with Data Dip**:
```
[Trigger] → [Gather Input] → [HTTP Request] → [Split]
                                      ↓
                              [Record Lookup]
                                      ↓
                   ┌──────────────────┼──────────────────┐
                   ↓                  ↓                  ↓
              [VIP Queue]       [Standard Queue]   [Voicemail]
```

**Chat to Video Escalation**:
```
[Chat Trigger] → [Send Message] → [Wait for Agent]
                                          ↓
                              [Flex: Add to Chat]
                                          ↓
                              [Agent requests video]
                                          ↓
                              [Send Video Link to Customer]
                                          ↓
                              [Both join Video Room]
```

### Studio Widgets

| Widget | Purpose | Key Config |
|--------|---------|------------|
| `trigger` | Entry point | Type: incoming_call, incoming_message |
| `say_play` | TTS/Audio | Text, language, voice |
| `gather_input_on_call` | DTMF/Speech | Timeout, num_digits, speech recognition |
| `make_http_request` | API call | URL, method, auth |
| `split_based_on` | Conditional | Variable, conditions |
| `send_to_flex` | Route to agent | Workflow, channel, attributes |
| `record_voicemail` | Voicemail | Transcribe, max_length |
| `run_function` | Execute Function | Service, environment, function |
| `send_message` | SMS/Chat | Body, from, to |

## Flex Plugins Development

### Project Structure

```
my-flex-plugin/
├── src/
│   ├── components/
│   │   ├── CustomTaskListItem.jsx
│   │   ├── CustomerProfileCard.jsx
│   │   └── RealTimeMetrics.jsx
│   ├── actions/
│   │   ├── customTransfer.js
│   │   └── createFollowUpTask.js
│   ├── listeners/
│   │   ├── taskAccepted.js
│   │   └── reservationCreated.js
│   ├── utils/
│   │   ├── api.js
│   │   └── constants.js
│   ├── states/
│   │   └── customReducer.js
│   ├── MyPlugin.js
│   └── index.js
├── public/
│   └── appConfig.js
├── package.json
└── webpack.config.js
```

### State Management

**Accessing State**:
```javascript
const { store } = manager;

// Current worker
const worker = store.getState().flex.worker;

// Active tasks
const tasks = store.getState().flex.worker.tasks;

// Current view
const view = store.getState().flex.view;

// Session data
const session = store.getState().flex.session;
```

**Subscribing to State Changes**:
```javascript
store.subscribe(() => {
  const state = store.getState();
  const taskCount = Object.keys(state.flex.worker.tasks).length;
  
  // Update UI based on state
  updateTaskCounter(taskCount);
});
```

**Custom Redux Actions**:
```javascript
// Action types
const SET_CUSTOMER_CONTEXT = 'SET_CUSTOMER_CONTEXT';

// Action creator
const setCustomerContext = (customer) => ({
  type: SET_CUSTOMER_CONTEXT,
  payload: customer
});

// Reducer
const customReducer = (state = {}, action) => {
  switch (action.type) {
    case SET_CUSTOMER_CONTEXT:
      return { ...state, customer: action.payload };
    default:
      return state;
  }
};

// Register with Flex
manager.store.addReducer('custom', customReducer);
```

### Custom Components

**Task List Item Override**:
```javascript
import React from 'react';
import { TaskListItem } from '@twilio/flex-ui';

const CustomTaskListItem = (props) => {
  const { task } = props;
  const customerName = task.attributes.customer_name || 'Unknown';
  const priority = task.priority || 0;
  
  return (
    <div className={`task-item priority-${priority}`}>
      <TaskListItem {...props} />
      <div className="customer-info">
        <span className="customer-name">{customerName}</span>
        <span className="wait-time">
          Wait: {formatDuration(task.age)}
        </span>
      </div>
    </div>
  );
};

flex.TaskListItem.default.props.replace(CustomTaskListItem);
```

**Panel Component**:
```javascript
import React, { useEffect, useState } from 'react';

const Customer360Panel = ({ task }) => {
  const [customer, setCustomer] = useState(null);
  
  useEffect(() => {
    if (task?.attributes?.customer_id) {
      fetchCustomerData(task.attributes.customer_id)
        .then(setCustomer);
    }
  }, [task]);
  
  if (!customer) return <div>Loading...</div>;
  
  return (
    <div className="customer-360">
      <header>
        <img src={customer.avatar} alt="" />
        <h3>{customer.name}</h3>
        <span className={`tier tier-${customer.tier}`}>
          {customer.tier}
        </span>
      </header>
      <section>
        <h4>Lifetime Value</h4>
        <p>${customer.ltv.toLocaleString()}</p>
      </section>
      <section>
        <h4>Recent Orders</h4>
        <ul>
          {customer.recent_orders.map(order => (
            <li key={order.id}>{order.date} - ${order.total}</li>
          ))}
        </ul>
      </section>
    </div>
  );
};

// Add to Task Canvas
flex.TaskCanvasTabs.Content.add(
  <flex.Tab label="Customer 360" key="customer-360">
    <Customer360Panel />
  </flex.Tab>
);
```

## Deployment

### Build Process

```bash
# Install dependencies
npm install

# Development server
npm start

# Production build
npm run build

# Deploy to Flex
npm run deploy
```

### Environment Configuration

```javascript
// appConfig.js
const appConfig = {
  pluginService: {
    enabled: true,
    url: '/plugins'
  },
  sso: {
    accountSid: process.env.REACT_APP_ACCOUNT_SID
  },
  ytdlpOptions: {
    // YT-DLP configuration
  },
  logLevel: 'info',
  flexConfig: {
    serverlessServiceSids: ['ZS...'],
    functionUrl: 'https://...twil.io'
  }
};
```

### Version Management

| Environment | Plugin Version | Notes |
|-------------|----------------|-------|
| Development | 1.0.0-dev | Local testing |
| Staging | 1.0.0-rc.1 | Pre-release |
| Production | 1.0.0 | Live version |

### Rollback Strategy

```bash
# List deployed plugins
twilio flex:plugins:list:plugin-versions --name my-plugin

# Deploy specific version
twilio flex:plugins:deploy --version 1.0.0 --changelog "Rollback to stable"

# Release to environment
twilio flex:plugins:release --plugin my-plugin@1.0.0
```

## Best Practices

### Performance

1. **Lazy Loading**: Load heavy components on demand
2. **Memoization**: Use React.memo for pure components
3. **Debouncing**: Throttle rapid state updates
4. **Pagination**: Limit list renders

### Security

1. **No Secrets in Frontend**: Use Functions for API keys
2. **Validate Webhooks**: Verify Twilio signatures
3. **CSP Headers**: Prevent XSS
4. **Input Sanitization**: Escape user input

### Testing

```javascript
// Component test with @twilio/flex-ui testing utilities
import { mount } from '@twilio/flex-ui/testing';

test('CustomTaskListItem renders', () => {
  const task = {
    sid: 'WT123',
    attributes: { customer_name: 'John Doe' }
  };
  
  const wrapper = mount(<CustomTaskListItem task={task} />);
  expect(wrapper.text()).toContain('John Doe');
});
```

### Monitoring

```javascript
// Custom analytics tracking
manager.events.addListener('taskAccepted', (task) => {
  analytics.track('Task Accepted', {
    task_sid: task.sid,
    queue_sid: task.queueSid,
    channel: task.channelType,
    wait_time: task.age
  });
});
```
