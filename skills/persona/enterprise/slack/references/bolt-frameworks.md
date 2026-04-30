# Bolt Frameworks Guide

> Official framework for building Slack apps quickly and securely.

---

## Overview

Bolt handles the foundational setup so you can focus on what makes your app unique.

### Features
- Authentication and OAuth handling
- Simplified API interfaces
- Automatic token validation
- Rate limiting and retry logic
- Event parsing and routing

### Available Languages
| Language | Package | Status |
|----------|---------|--------|
| JavaScript/TypeScript | `@slack/bolt` | Stable |
| Python | `slack-bolt` | Stable |
| Java | `bolt` | Stable |

---

## Bolt for JavaScript

### Installation
```bash
npm install @slack/bolt
```

### Basic App
```javascript
const { App } = require('@slack/bolt');

// Initialize app
const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  signingSecret: process.env.SLACK_SIGNING_SECRET,
  // For Socket Mode:
  // socketMode: true,
  // appToken: process.env.SLACK_APP_TOKEN
});

// Listen for messages
app.message('hello', async ({ message, say }) => {
  await say(`Hey there, <@${message.user}>!`);
});

// Slash command
app.command('/ticket', async ({ command, ack, respond }) => {
  await ack();
  await respond(`Creating ticket: ${command.text}`);
});

// Start server
(async () => {
  await app.start(process.env.PORT || 3000);
  console.log('⚡️ Bolt app is running!');
})();
```

### Event Handling
```javascript
// Message events
app.message(':wave:', async ({ message, say }) => {
  await say('Hello back! 👋');
});

// Reaction added
app.event('reaction_added', async ({ event, client }) => {
  if (event.reaction === 'ticket') {
    // Create ticket logic
  }
});

// App mention
app.event('app_mention', async ({ event, say }) => {
  await say({
    text: 'You mentioned me!',
    thread_ts: event.thread_ts || event.ts
  });
});

// Member joined
app.event('member_joined_channel', async ({ event, client }) => {
  if (event.channel === 'C1234567890') {
    await client.chat.postMessage({
      channel: event.channel,
      text: `Welcome, <@${event.user}>! 👋`
    });
  }
});
```

### Interactive Components
```javascript
// Button click
app.action('approve_button', async ({ ack, body, client }) => {
  await ack();
  
  // Update message to show approval
  await client.chat.update({
    channel: body.channel.id,
    ts: body.message.ts,
    blocks: [
      {
        type: 'section',
        text: {
          type: 'mrkdwn',
          text: '✅ Request approved by ' + body.user.name
        }
      }
    ]
  });
});

// Select menu
app.action('user_select', async ({ ack, body, action }) => {
  await ack();
  console.log('Selected user:', action.selected_user);
});

// View submission (modal)
app.view('create_task_modal', async ({ ack, body, view, client }) => {
  const values = view.state.values;
  const title = values.title_block.title_input.value;
  
  // Validate
  if (title.length < 3) {
    await ack({
      response_action: 'errors',
      errors: {
        title_block: 'Title must be at least 3 characters'
      }
    });
    return;
  }
  
  await ack(); // Success
  
  // Create task
  await createTask(title, values);
});
```

### Middleware
```javascript
// Custom middleware
const logRequests = async ({ logger, context, next }) => {
  logger.info(`Incoming request from team ${context.teamId}`);
  await next();
};

// Apply globally
app.use(logRequests);

// Apply to specific listeners
app.message('sensitive', authorizeAdmin, async ({ say }) => {
  await say('Admin command executed');
});

// Error handler
app.error(async (error) => {
  console.error('Global error handler:', error);
});
```

---

## Bolt for Python

### Installation
```bash
pip install slack-bolt
```

### Basic App (HTTP Mode)
```python
import os
from slack_bolt import App

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.message("hello")
def message_hello(message, say):
    say(f"Hey there, <@{message['user']}>!")

@app.command("/echo")
def handle_echo_command(ack, command, say):
    ack()
    say(f"Echo: {command['text']}")

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
```

### Socket Mode
```python
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("app_mention")
def handle_app_mention(event, say):
    say({
        "text": "You mentioned me!",
        "thread_ts": event.get("thread_ts", event["ts"])
    })

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
```

### Async Support
```python
import asyncio
from slack_bolt.async_app import AsyncApp

app = AsyncApp(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.message("weather")
async def message_weather(message, say, client):
    # Async I/O operations
    weather_data = await fetch_weather_async()
    await say(f"Current weather: {weather_data}")

async def fetch_weather_async():
    # Async HTTP request
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.weather.com/...') as resp:
            return await resp.text()

if __name__ == "__main__":
    app.start(port=3000)
```

### Class-Based Listeners
```python
from slack_bolt import App

class MyApp:
    def __init__(self):
        self.app = App()
        self.register_listeners()
    
    def register_listeners(self):
        @self.app.message("help")
        def handle_help(message, say):
            say("Available commands: ...")
        
        @self.app.action("approve")
        def handle_approval(ack, body, client):
            ack()
            self.process_approval(body)
    
    def process_approval(self, body):
        # Business logic
        pass
    
    def start(self):
        self.app.start(port=3000)

if __name__ == "__main__":
    MyApp().start()
```

---

## Bolt for Java

### Maven Dependency
```xml
<dependency>
  <groupId>com.slack.api</groupId>
  <artifactId>bolt</artifactId>
  <version>1.48.0</version>
</dependency>
<dependency>
  <groupId>com.slack.api</groupId>
  <artifactId>bolt-jetty</artifactId>
  <version>1.48.0</version>
</dependency>
```

### Basic App
```java
package hello;

import com.slack.api.bolt.App;
import com.slack.api.bolt.jetty.SlackAppServer;
import com.slack.api.model.event.MessageEvent;

public class MyApp {
    public static void main(String[] args) throws Exception {
        App app = new App();
        
        // Message listener
        app.message("hello", (req, ctx) -> {
            String user = req.getEvent().getUser();
            ctx.say("Hey there, <@" + user + ">!");
            return ctx.ack();
        });
        
        // Slash command
        app.command("/ticket", (req, ctx) -> {
            String text = req.getPayload().getText();
            ctx.respond("Creating ticket: " + text);
            return ctx.ack();
        });
        
        SlackAppServer server = new SlackAppServer(app);
        server.start();
    }
}
```

### Socket Mode
```java
package hello;

import com.slack.api.bolt.App;
import com.slack.api.bolt.socket_mode.SocketModeApp;

public class SocketModeAppExample {
    public static void main(String[] args) throws Exception {
        App app = new App();
        
        app.event(MessageEvent.class, (payload, ctx) -> {
            // Handle message
            return ctx.ack();
        });
        
        new SocketModeApp(app).start();
    }
}
```

### Spring Boot Integration
```java
@RestController
public class SlackController {
    
    @Autowired
    private App slackApp;
    
    @RequestMapping(value = "/slack/events", 
                    method = RequestMethod.POST, 
                    produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<String> events(@RequestBody String body,
                                          @RequestHeader("X-Slack-Signature") String signature,
                                          @RequestHeader("X-Slack-Request-Timestamp") String timestamp) {
        // Bolt handles verification internally
        return ResponseEntity.ok(slackApp.run(body));
    }
}
```

---

## Deployment Options

### Heroku
```javascript
// Procfile
web: node app.js
```

```javascript
// app.js - listen on PORT
const { App, ExpressReceiver } = require('@slack/bolt');

const receiver = new ExpressReceiver({
  signingSecret: process.env.SLACK_SIGNING_SECRET
});

const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  receiver
});

// Health check
receiver.router.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

(async () => {
  await app.start(process.env.PORT || 3000);
})();
```

### AWS Lambda
```javascript
const { AwsLambdaReceiver } = require('@slack/bolt');

const awsLambdaReceiver = new AwsLambdaReceiver({
  signingSecret: process.env.SLACK_SIGNING_SECRET
});

const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  receiver: awsLambdaReceiver
});

// Lambda handler
module.exports.handler = async (event, context) => {
  const handler = await awsLambdaReceiver.start();
  return handler(event, context);
};
```

### Docker
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
```

---

## Testing

### Local Development with ngrok
```bash
# Terminal 1: Start app
npm start

# Terminal 2: Expose locally
ngrok http 3000

# Copy ngrok URL to Slack app config
# https://xxxx.ngrok.io/slack/events
```

### Unit Testing (Python)
```python
from slack_bolt import App
from slack_bolt.request import BoltRequest
from slack_bolt.response import BoltResponse

def test_hello_message():
    app = App(process_before_response=True)
    
    @app.message("hello")
    def handle_hello(message, say):
        say(f"Hi <@{message['user']}>!")
    
    # Create test request
    request = BoltRequest(
        body={
            "type": "event_callback",
            "event": {
                "type": "message",
                "user": "U123",
                "text": "hello",
                "channel": "C123",
                "ts": "123456.789"
            }
        }
    )
    
    response = app.dispatch(request)
    assert response.status == 200
```

---

## Best Practices

### 1. Acknowledge Quickly
```javascript
// Always ack immediately
app.action('button', async ({ ack, body, client }) => {
  await ack(); // First!
  // Then do work
  await client.chat.update({...});
});
```

### 2. Use Threads
```javascript
app.event('app_mention', async ({ event, say }) => {
  await say({
    text: 'Processing your request...',
    thread_ts: event.ts // Keep it organized
  });
});
```

### 3. Handle Errors
```javascript
app.error(async (error) => {
  console.error(error);
  // Send to error tracking service
  await sentry.captureException(error);
});
```

### 4. Environment Configuration
```javascript
const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  signingSecret: process.env.SLACK_SIGNING_SECRET,
  logLevel: process.env.NODE_ENV === 'development' ? 'debug' : 'info'
});
```
