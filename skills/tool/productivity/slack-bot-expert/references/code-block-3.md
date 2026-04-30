# python Example

```
# Incoming Webhook — Send messages from external systems
import requests

def send_webhook_message(channel_webhook_url, message):
    payload = {
        "text": message,
        "blocks": [
            {"type": "section", "text": {"type": "mrkdwn", "text": message}}
        ]
    }
    response = requests.post(channel_webhook_url, json=payload)
    response.raise_for_status()

# GitHub webhook → Slack (Flask example)
from flask import Flask, request, jsonify
import hmac, hashlib, os

app = Flask(__name__)

@app.route("/github-webhook", methods=["POST"])
def github_webhook():
    # Verify signature
    signature = request.headers.get("X-Hub-Signature-256")
    if not hmac.compare_digest(
        f"sha256={hmac.new(os.environ['GITHUB_WEBHOOK_SECRET'].encode(), request.data, hashlib.sha256).hexdigest()}",
        signature or ""
    ):
        return jsonify({"error": "Invalid signature"}), 401
    
    event = request.headers.get("X-GitHub-Event")
    data = request.json
    
    if event == "push":
        branch = data["ref"].split("/")[-1]
        commits = data["commits"]
        author = commits[-1]["author"]["name"]
        message = commits[-1]["message"]
        url = data["repository"]["html_url"]
        
        send_webhook_message(
            os.environ["DEVOPS_WEBHOOK"],
            f"📦 *Push to `{branch}`*\n{author}: {message}\n<{url}|View on GitHub>"
        )
    
    elif event == "pull_request":
        pr = data["pull_request"]
        action = data["action"]
        title = pr["title"]
        author = pr["user"]["login"]
        url = pr["html_url"]
        
        emoji = "✅" if pr["merged"] else "🔀"
        send_webhook_message(
            os.environ["DEVOPS_WEBHOOK"],
            f"{emoji} *PR {action}:* <{url}|{title}> by @{author}"
        )
    
    return jsonify({"ok": True})
```
