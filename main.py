from telethon import TelegramClient, events
import os

api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
session_name = 'session'  # Il file si chiama session.session

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    if event.is_group:
        message = event.message.message
        if any(x in message.lower() for x in ["dexscreener.com", "pancakeswap.finance", "poocoin.app", "0x"]):
            print(f"[{event.chat.title}] {message}")

client.start()
client.run_until_disconnected()