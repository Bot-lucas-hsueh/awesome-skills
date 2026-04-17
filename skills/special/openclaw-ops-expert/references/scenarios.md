## 9. Scenario Examples

### 9.1 Fresh Install on macOS

**User:** "我在 macOS 上刚装好了 Node 22，怎么安装 OpenClaw 并配置成开机自启？"

**OpenClaw Ops Expert:**
> **macOS 安装 + launchd 守护进程全流程**
>
> **Step 1: 安装**
> ```bash
> # 使用 npm 全局安装（不要用 sudo）
> npm install -g openclaw@latest
>
> # 验证安装
> openclaw --version
> ```
>
> **Step 2: 引导向导（含守护进程安装）**
> ```bash
> openclaw onboard --install-daemon
> # 向导会：
> # 1. 要求选择 AI 模型提供商（OpenAI / Anthropic
> # 2. 配置第一个渠道（建议先配 Telegram）
> # 3. 安装 launchd plist 到 ~/Library/LaunchAgents/
> # 4. 自动启动守护进程
> ```
>
> **Step 3: 验证守护进程状态**
> ```bash
> # 检查 launchd 是否在运行
> launchctl list | grep openclaw
>
> # 查看守护进程日志
> tail -f ~/Library/Logs/openclaw/gateway.log
>
> # 手动重启（如有需要）
> launchctl unload ~/Library/LaunchAgents/ai.openclaw.gateway.plist
> launchctl load ~/Library/LaunchAgents/ai.openclaw.gateway.plist
> ```
>
> **Step 4: 测试网关**
> ```bash
> openclaw gateway --port 18789 --verbose
> # 看到 "[gateway] listening on ws://127.0.0.1:18789" 即为成功
> ```
>
> **配置文件位置**: `~/.openclaw/openclaw.json`
>
> **Next, I need from you:**
> 1. 你想接入哪个消息平台？（Telegram/Slack/Discord 配置步骤不同）
> 2. 是否需要从手机远程访问？（需要额外配置 Tailscale）

### 9.2 Telegram Channel Integration

**User:** "我想把 OpenClaw 接入 Telegram，怎么配置 Bot？"

**OpenClaw Ops Expert:**
> **Telegram Bot 配置 — 3 步完成**
>
> **Step 1: 创建 Telegram Bot**
> ```
> 1. 在 Telegram 搜索 @BotFather
> 2. 发送 /newbot
> 3. 输入 Bot 名称（例如 "My OpenClaw"）
> 4. 输入 Bot 用户名（必须以 _bot 结尾，例如 myopenclaw_bot）
> 5. 复制返回的 Bot Token（格式：1234567890:AAXXXXXXXX）
> ```
>
> **Step 2: 添加到 OpenClaw 配置**
> ```bash
> # 方式一：通过向导（推荐）
> openclaw onboard --add-channel telegram
> # 按提示输入 Bot Token
>
> # 方式二：直接编辑配置文件
> # 编辑 ~/.openclaw/openclaw.json，添加：
> ```
> ```json
> {
>   "channels": [
>     {
>       "type": "telegram",
>       "token": "1234567890:AAXXXXXXXX",
>       "dmPolicy": "pairing"
>     }
>   ]
> }
> ```
>
> **Step 3: 重启并测试**
> ```bash
> # 重启网关（守护进程模式下）
> launchctl unload ~/Library/LaunchAgents/ai.openclaw.gateway.plist
> launchctl load ~/Library/LaunchAgents/ai.openclaw.gateway.plist
>
> # 或者临时前台运行查看日志
> openclaw gateway --verbose
> # 看到 "[telegram] connected" 即成功
> ```
>
> **安全提示**: `dmPolicy: "pairing"` 是默认值，陌生用户必须输入配对码才能与 Bot 交互。
> 查看当前配对码: `openclaw pairing-code`

### 9.3 Diagnosing Gateway Crash

**User:** "OpenClaw 网关突然停了，Telegram 消息没有回应，怎么排查？"

**OpenClaw Ops Expert:**
> **网关故障 5 分钟诊断手册**
>
> **Step 1: 确认网关状态**
> ```bash
> # macOS
> launchctl list | grep openclaw
> # 输出有 PID 数字 = 在运行；输出 "-" = 已停止
>
> # Linux
> systemctl status openclaw
> ```
>
> **Step 2: 查看最近错误日志**
> ```bash
> # macOS
> tail -50 ~/Library/Logs/openclaw/gateway.log | grep -i "error\|crash\|fatal"
>
> # Linux
> journalctl -u openclaw -n 50 --no-pager | grep -i "error\|crash\|fatal"
> ```
>
> **Step 3: 常见原因速查**
>
> | 错误信息 | 原因 | 修复方法 |
> |---------|------|---------|
> | `EADDRINUSE :18789` | 端口被占用 | `lsof -i :18789` 找到占用进程并终止 |
> | `ECONNREFUSED` on channel | Channel token 失效 | 重新生成 Bot Token 并更新配置 |
> | `Cannot find module` | npm 包损坏 | `npm install -g openclaw@latest` 重装 |
> | `Node.js v20.x` in log | Node 版本不足 | `nvm use 22` 后重启守护进程 |
>
> **Step 4: 重启守护进程**
> ```bash
> # macOS
> launchctl unload ~/Library/LaunchAgents/ai.openclaw.gateway.plist
> launchctl load ~/Library/LaunchAgents/ai.openclaw.gateway.plist
>
> # Linux
> systemctl restart openclaw
>
> # 验证恢复
> openclaw channels list
> ```
>
> **Step 5: 若仍失败 — 前台调试模式**
> ```bash
> # 直接前台运行，查看完整错误
> openclaw gateway --port 18789 --verbose
> # 此时发送 Telegram 消息，观察实时日志
> ```

### 9.4 Setting Up Remote Access

**User:** "我想在手机上通过 Telegram 访问家里运行的 OpenClaw，怎么实现安全的远程连接？"

**OpenClaw Ops Expert:**
> **推荐方案: Tailscale Serve（安全、无需开放公网端口）**
>
> Telegram Bot 本身是云端的，你的 OpenClaw 通过 WebSocket 长连接拉取消息，
> **无需远程访问网关**即可在任何网络下接收 Telegram 消息。
>
> ✅ **Telegram（及 WhatsApp、Discord、Slack）已经支持手机访问** — 因为消息
> 由云平台中转，OpenClaw 主动轮询/连接云端，而非等待入站连接。
>
> ⚠️ **只有以下场景才需要配置远程网关访问:**
> - 使用 Web UI
> - iMessage、Signal 等设备依赖渠道的桥接管理
> - 多设备节点配对
>
> **如果确实需要远程网关访问（Tailscale 方案）:**
> ```bash
> # 1. 安装 Tailscale
> brew install tailscale  # macOS
> # 或 curl -fsSL https://tailscale.com/install.sh | sh  # Linux
>
> # 2. 登录 Tailscale
> tailscale up
>
> # 3. 通过 Serve 暴露网关（仅 Tailscale 网络内可访问）
> tailscale serve https / ws://127.0.0.1:18789
>
> # 4. 手机安装 Tailscale app 并登录同一账号
> # 之后可通过 wss://<hostname>.ts.net 访问网关
> ```
>
> **不要使用的方案:**
> - 不要将 gateway.bind 改为 0.0.0.0 + 路由器端口转发 → 公网暴露风险
> - 不要在云服务器上部署 OpenClaw 只为远程访问 → 违背本地优先设计原则

---

