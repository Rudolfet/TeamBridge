
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
---
### 🐳 Docker (recommended)

If you prefer Docker, you can build and run TeamBridge in one command:
``` bash
docker compose up --build -d
```

To check logs in real time:
``` bash
docker compose logs -f
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

This project is licensed under the MIT License.

## 🌐 About

TeamBridge is a community-driven initiative to simplify coordination between contributors across multiple Discord servers and projects — uniting communication and task tracking in a single, efficient workflow.
