
# 🧩 TeamBridge

**TeamBridge** connects Discord teams with their project tools.  
It helps organize and track requests, ideas, and reports directly from chat — improving coordination without leaving your community server.

---

## 🚀 Features
- 🧵 Create and track tasks directly from Discord slash commands  
- ⚙️ Real-time connection with external tools  
- 🔄 Automatic updates for assigned tasks  
- 🔐 Secure by design — no admin or moderation permissions required  
- 🐳 Docker-ready for quick deployment  

---

## 🛠️ Setup

### Requirements
- Python **3.11+**
- A Discord bot token  
- (Optional) API credentials for your chosen backend

---

### ⚙️ Environment setup

Create your `.env` file (or copy `.env.example`) and fill in your tokens and configuration values.

```bash
cp .env.example .env
```
Then edit the `.env` file with your own credentials:
```
DISCORD_TOKEN=your_discord_bot_token
GUILD_IDS=123456789012345678
ZAMMAD_URL=https://your.zammad.instance
ZAMMAD_TOKEN=your_zammad_api_token

# Optional
DEFAULT_GROUP=TicketPersonali
PUBLIC_ANNOUNCE=true
PUBLIC_MENTION_AUTHOR=true
```
Finally, run the bot:
``` bash
python app.py
```
