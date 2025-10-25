import os
import httpx
import discord
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

# === Load .env ===
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
ZAMMAD_URL = os.getenv("ZAMMAD_URL", "").rstrip("/")
ZAMMAD_TOKEN = os.getenv("ZAMMAD_TOKEN", "")
DEFAULT_GROUP = os.getenv("DEFAULT_GROUP", "").strip()

# === Guild configuration ===
GUILD_IDS = os.getenv("GUILD_IDS", "")
GUILD_IDS_LIST = [int(x) for x in GUILD_IDS.split(",") if x.strip().isdigit()]
GUILDS = [discord.Object(id=gid) for gid in GUILD_IDS_LIST]

# === Optional flags ===
PUBLIC_ANNOUNCE = os.getenv("PUBLIC_ANNOUNCE", "true").lower() == "true"
PUBLIC_MENTION_AUTHOR = os.getenv("PUBLIC_MENTION_AUTHOR", "true").lower() == "true"

# === HTTP client ===
http = httpx.AsyncClient(timeout=20)
def zammad_headers():
    return {"Authorization": f"Token token={ZAMMAD_TOKEN}"}

# === Discord bot setup ===
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    """Sync slash commands and confirm connection."""
    try:
        if GUILD_IDS_LIST:
            for gid in GUILD_IDS_LIST:
                cmds = await bot.tree.sync(guild=discord.Object(id=gid))
                print(f"🔁 Synced {len(cmds)} commands to guild {gid}: {[c.name for c in cmds]}")
        else:
            cmds = await bot.tree.sync()
            print(f"🔁 Synced {len(cmds)} global commands: {[c.name for c in cmds]}")
    except Exception as e:
        print("⚠️ Slash command sync error:", e)
    print(f"✅ TeamBridge is online as {bot.user}")

# === Ping test ===
@bot.tree.command(name="ping", description="Check if TeamBridge is online")
@app_commands.guilds(*GUILDS)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong! TeamBridge is active.", ephemeral=True)

# === Ticket creation (Zammad) ===
@bot.tree.command(name="ticket_new", description="Create a new ticket in Zammad")
@app_commands.guilds(*GUILDS)
@app_commands.describe(titolo="Ticket title", descrizione="Describe your issue or request")
async def ticket_new(interaction: discord.Interaction, titolo: str, descrizione: str):
    await interaction.response.defer(ephemeral=True)

    if not (ZAMMAD_URL and ZAMMAD_TOKEN):
        await interaction.followup.send("⚠️ Zammad not configured (ZAMMAD_URL/ZAMMAD_TOKEN).", ephemeral=True)
        return

    group_name = DEFAULT_GROUP or "TicketPersonali"
    login = f"discord:{interaction.user.id}"
    user_payload = {
        "login": login,
        "firstname": interaction.user.display_name,
        "lastname": "",
        "roles": ["Customer"]
    }

    try:
        r = await http.post(f"{ZAMMAD_URL}/api/v1/users", headers=zammad_headers(), json=user_payload)
        if r.status_code in (200, 201):
            user_id = r.json().get("id")
        else:
            s = await http.get(f"{ZAMMAD_URL}/api/v1/users/search?query={login}", headers=zammad_headers())
            user_id = s.json()[0]["id"] if s.status_code == 200 and s.json() else None
    except Exception as e:
        print("❌ Users API error:", repr(e))
        await interaction.followup.send("❌ Connection to Zammad failed (CreateError1-NC).", ephemeral=True)
        return

    if not user_id:
        await interaction.followup.send("❌ Error creating/searching user (CreateError0).", ephemeral=True)
        return

    payload_ticket = {
        "title": titolo[:250],
        "group": group_name,
        "customer_id": user_id,
        "article": {
            "subject": titolo[:250],
            "body": descrizione,
            "type": "note",
            "internal": False,
            "content_type": "text/plain"
        }
    }

    try:
        tr = await http.post(f"{ZAMMAD_URL}/api/v1/tickets", headers=zammad_headers(), json=payload_ticket)
    except Exception as e:
        print("❌ Ticket API error:", repr(e))
        await interaction.followup.send("❌ Connection to Zammad failed (CreateError2-NC).", ephemeral=True)
        return

    if tr.status_code in (200, 201):
        t = tr.json()
        msg = f"✅ Created **#{t['number']}** in **{group_name}**"
        await interaction.followup.send(msg, ephemeral=True)

        # Optional public announce
        if PUBLIC_ANNOUNCE:
            channel = interaction.channel
            author_mention = interaction.user.mention if PUBLIC_MENTION_AUTHOR else ""
            await channel.send(f"🆕 Ticket **#{t['number']}** created by {author_mention}\n> {titolo}")
    else:
        print(f"❌ Ticket creation failed ({tr.status_code}): {tr.text}")
        await interaction.followup.send(f"❌ Zammad returned error ({tr.status_code}).", ephemeral=True)

# === Start bot ===
if __name__ == "__main__":
    if not DISCORD_TOKEN:
        raise SystemExit("⚠️ Missing DISCORD_TOKEN in .env (DiscordToken0)")
    bot.run(DISCORD_TOKEN)
