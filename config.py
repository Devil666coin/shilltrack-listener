import os
from dotenv import load_dotenv

load_dotenv()

# Configurazioni sensibili
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "anon")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# File di storage
MENTIONS_FILE = "mentions.json"