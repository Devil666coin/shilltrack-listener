import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID_STR = os.getenv("API_ID")
CHANNEL_ID_STR = os.getenv("CHANNEL_ID")

# ✅ DEBUG: stampa i valori grezzi
print(f"🔍 RAW API_ID: '{API_ID_STR}'")
print(f"🔍 RAW CHANNEL_ID: '{CHANNEL_ID_STR}'")

# Funzione per ripulire da caratteri strani
def normalize_int_string(s):
    return s.strip().replace("–", "-").replace("—", "-").replace(" ", "").replace("\u200b", "")

# ✅ DEBUG: stampa i valori dopo normalizzazione
print(f"✅ Normalized API_ID: '{normalize_int_string(API_ID_STR)}'")
print(f"✅ Normalized CHANNEL_ID: '{normalize_int_string(CHANNEL_ID_STR)}'")

try:
    API_ID = int(normalize_int_string(API_ID_STR))
    CHANNEL_ID = int(normalize_int_string(CHANNEL_ID_STR))
except Exception as e:
    print(f"❌ Errore nel parsing API_ID/CHANNEL_ID: {e}")
    raise ValueError("❌ API_ID o CHANNEL_ID non sono numeri validi (devono essere int)")

# Percorsi dei file
MENTIONS_FILE = "mentions.json"
RANKING_FILE = "ranking.json"