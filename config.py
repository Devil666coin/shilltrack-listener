import os
from dotenv import load_dotenv

load_dotenv()

API_ID_STR = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID_STR = os.getenv("CHANNEL_ID")

if not all([API_ID_STR, API_HASH, BOT_TOKEN, CHANNEL_ID_STR]):
    raise ValueError("❌ Una o più variabili mancano (verifica su Railway)")

try:
    # Rimuove virgolette e spazi prima di convertire in int
    API_ID = int(API_ID_STR.strip().replace('"', '').replace("'", ''))
    CHANNEL_ID = int(CHANNEL_ID_STR.strip().replace('"', '').replace("'", ''))
except Exception:
    raise ValueError("❌ API_ID o CHANNEL_ID non sono numeri validi (devono essere int)")

# Percorsi dei file
MENTIONS_FILE = "mentions.json"
RANKING_FILE = "ranking.json"