import os
from dotenv import load_dotenv

load_dotenv()

# Configurazioni sensibili
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "anon")
BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_ID_RAW = os.getenv("CHANNEL_ID")
if CHANNEL_ID_RAW is None:
    raise ValueError("❌ Variabile CHANNEL_ID mancante nelle env di Railway")
CHANNEL_ID = int(CHANNEL_ID_RAW)

# File di storage
MENTIONS_FILE = "mentions.json"
RANKING_FILE = "ranking.json"