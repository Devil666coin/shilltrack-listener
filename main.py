from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv()  # Carica il file .env

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = os.getenv("SESSION_NAME")

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    if event.is_group:
        message = event.message.message
        if any(x in message.lower() for x in ["dexscreener.com", "pancakeswap.finance", "poocoin.app", "0x"]):
            print(f"[{event.chat.title}] {message}")

client.start()
client.run_until_disconnected()