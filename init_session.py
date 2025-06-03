from telethon.sync import TelegramClient

API_ID = 25809275  # ← il tuo API ID
API_HASH = "9281a0935672ff56fffa021990be73eb"  # ← il tuo API HASH
SESSION_NAME = "anon"  # questo crea anon.session

with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
    print("✅ Login completato.")