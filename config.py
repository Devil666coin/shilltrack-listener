import os
from dotenv import load_dotenv

load_dotenv()

# Estrai le variabili dalle environment (Railway o .env locale)
API_ID_STR = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "anon")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID_STR = os.getenv("CHANNEL_ID")

# Verifica che siano tutte presenti
if not all([API_ID_STR, BOT_TOKEN, CHANNEL_ID_STR, API_HASH]):
    raise ValueError("❌ Una o più variabili di ambiente mancano nelle env di Railway")

# Parsing sicuro dei numeri
try:
    API_ID = int(API_ID_STR.strip())
    CHANNEL_ID = int(CHANNEL_ID_STR.strip().replace("–", "-"))
except Exception:
    raise ValueError("❌ API_ID o CHANNEL_ID non sono numeri validi (devono essere int)")

# Percorsi dei file
MENTIONS_FILE = "mentions.json"
RANKING_FILE = "ranking.json"