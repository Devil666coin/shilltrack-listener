import os
from dotenv import load_dotenv

load_dotenv()

# ⚙️ Configurazioni sensibili
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "anon")
BOT_TOKEN = os.getenv("BOT_TOKEN")
channel_id_str = os.getenv("CHANNEL_ID")
if channel_id_str is None:
    raise ValueError("❌ Variabile CHANNEL_ID mancante nelle env di Railway")
CHANNEL_ID = int(channel_id_str)

# ✅ Validazione variabili critiche
if not API_ID or not API_HASH or not BOT_TOKEN or not CHANNEL_ID:
    raise ValueError("❌ Una o più variabili di ambiente mancano nelle env di Railway")

try:
    API_ID = int(API_ID)
    CHANNEL_ID = int(CHANNEL_ID)
except ValueError:
    raise ValueError("❌ API_ID o CHANNEL_ID non sono numeri validi (devono essere int)")

# File di storage
MENTIONS_FILE = "mentions.json"
RANKING_FILE = "ranking.json"