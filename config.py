import os
from dotenv import load_dotenv

load_dotenv()

# 🔐 Config sensibili
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "anon")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🛡️ Protezione robusta per CHANNEL_ID
raw_channel_id = os.getenv("CHANNEL_ID")
if not raw_channel_id:
    raise ValueError("❌ Variabile CHANNEL_ID mancante nelle env di Railway")
try:
    CHANNEL_ID = int(raw_channel_id)
except ValueError:
    raise ValueError("❌ CHANNEL_ID non è un numero valido (int)")

# 📁 Path file
MENTIONS_FILE = "mentions.json"