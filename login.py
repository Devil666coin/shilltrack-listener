from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "anon")

with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
    print("✅ Login completato e sessione salvata.")