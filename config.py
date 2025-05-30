import os
from dotenv import load_dotenv

load_dotenv()

# 🔐 Configurazioni sensibili
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "anon")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🔒 Protezione da crash se CHANNEL_ID è assente o malformato
channel = os.getenv("CHANNEL_ID")
if channel is None:
    raise ValueError("❌ CHANNEL_ID non definito nelle variabili Railway")
CHANNEL_ID = int(channel)

# 📦 File di storage
MENTIONS_FILE = "mentions.json"