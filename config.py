import os
from dotenv import load_dotenv
import json

load_dotenv()

# Caricamento variabili da ambiente
API_ID_STR = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
CHANNEL_ID_STR = os.getenv("CHANNEL_ID")
SESSION_NAME = os.getenv("SESSION_NAME", "anon")
MONITORED_GROUPS_STR = os.getenv("MONITORED_GROUPS", "[]")
MONITORED_GROUPS = json.loads(MONITORED_GROUPS_STR)
# Funzione di pulizia ID
def normalize_id_string(raw: str) -> str:
    return ''.join(c for c in raw if c.isdigit() or c == '-')

# Controllo esistenza
if not all([BOT_TOKEN, CHANNEL_ID_STR, API_ID_STR, API_HASH]):
    raise ValueError("❌ Una o più variabili di ambiente mancano nelle envVars Railway!")

# Parsing sicuro
try:
    print(f"🔍 Parsing API_ID: {API_ID_STR}")
    print(f"🔍 Parsing CHANNEL_ID: {CHANNEL_ID_STR}")
    API_ID = int(normalize_id_string(API_ID_STR))
    CHANNEL_ID = int(normalize_id_string(CHANNEL_ID_STR))
    print(f"✅ Normalized API_ID: {API_ID}")
    print(f"✅ Normalized CHANNEL_ID: {CHANNEL_ID}")
except Exception as e:
    raise ValueError(f"❌ Errore nel parsing API_ID/CHANNEL_ID: {e}")

# File JSON
MENTIONS_FILE = "mentions.json"
RANKING_FILE = "ranking.json"