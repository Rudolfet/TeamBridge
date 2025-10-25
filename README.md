## 🧩TeamBridge
_A lightweight integration bot connecting Discord with Zammad and (optionally) Jira for multi-community ticket management._

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

![License](https://img.shields.io/github/license/Rudolfet/TeamBridge)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Status](https://img.shields.io/badge/status-active-success)
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

### 🧩 Example `.env` configuration

Below is an example configuration file (`.env.example`).
Copy it, rename to `.env`, and fill in your credentials.

```env
# === DISCORD TOKEN ===
DISCORD_TOKEN=your_discord_bot_token

# === DISCORD SERVER AUTHORIZED ===
# Optional: leave empty for global registration or list multiple separated by commas
GUILD_IDS=    # Example: 111111111111111111,222222222222222222

# === ZAMMAD SETTINGS ===
ZAMMAD_URL=https://your.zammad.instance
ZAMMAD_TOKEN=your_zammad_api_token

# === JIRA (optional, disabled by default) ===
USE_JIRA=false
# JIRA_URL=https://your.jira.instance
# JIRA_USER=your_jira_user
# JIRA_TOKEN=your_jira_api_token

# === FLAGS ===
PUBLIC_ANNOUNCE=true
PUBLIC_MENTION_AUTHOR=true

# === DEFAULT GROUPS ===
DEFAULT_GROUP=MyGroup
# Optional: Override per server (guild)
GUILD_DEFAULT_GROUP__111111111111111111=MyGroupMain
GUILD_DEFAULT_GROUP__222222222222222222=MyGroupWiki
GUILD_DEFAULT_GROUP__333333333333333333=MyGroupEvents
GUILD_DEFAULT_GROUP__444444444444444444=MyGroupCommunity
```

Finally, run the bot:
``` bash
python app.py
```

[here 2]
---
### 🐳 Run with Docker

```bash
docker compose up --build -d
```
Check logs:
``` bash
docker logs -f teambridge-bot
```
---
### ⚙️ Configuration variables
| Variable                      | Description                              |
| ----------------------------- | ---------------------------------------- |
| `DISCORD_TOKEN`               | Your Discord bot token                   |
| `GUILD_IDS`                   | Discord server IDs separated by commas   |
| `DEFAULT_GROUP`               | Default group name for ticket creation   |
| `ZAMMAD_URL` / `ZAMMAD_TOKEN` | (Optional) Helpdesk backend credentials  |
| `JIRA_URL` / `JIRA_TOKEN`     | (Optional) Jira backend credentials      |
| `PUBLIC_ANNOUNCE`             | If `true`, posts ticket summary publicly |
| `PUBLIC_MENTION_AUTHOR`       | If `true`, mentions the author           |

---

## 🧱 Tech Stack

* Python 3.11+
* discord.py >=2.4.0
* httpx
* python-dotenv
* Docker Compose

## 🪪 License

This project is licensed under the [MIT](LICENSE).

## 🌐 About

TeamBridge is a community-driven initiative to simplify coordination between contributors across multiple Discord servers and projects — uniting communication and task tracking in a single, efficient workflow.
