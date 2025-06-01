from telethon.sync import TelegramClient
from config import SESSION_NAME, API_ID, API_HASH

with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
    print("✅ Sessione creata con successo!")