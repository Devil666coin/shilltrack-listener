import os
from dotenv import load_dotenv

load_dotenv()

# Carica variabili d'ambiente
API_ID_STR = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_NAME = os.getenv("SESSION_NAME", "anon")
CHANNEL_ID_STR = os.getenv("CHANNEL_ID")

# Controlla che le variabili esistano
if not all([BOT_TOKEN, CHANNEL_ID_STR, API_ID_STR, API_HASH]):
    raise ValueError("❌ Una o più variabili di ambiente mancano nelle env di Railway")

# Conversione sicura
try:
    API_ID = int(API_ID_STR.strip())
    CHANNEL_ID = int(CHANNEL_ID_STR.strip())
except ValueError:
    raise ValueError("❌ API_ID o CHANNEL_ID non sono numeri validi (devono essere int)")

# File di storage
MENTIONS_FILE = "mentions.json"
RANKING_FILE = "ranking.json"