import json
import os
import re
import asyncio
from datetime import datetime, timedelta
from telethon import TelegramClient, events
from dotenv import load_dotenv
from poster import post_classifica

# Carica variabili da .env
load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = "session"

# File dove salviamo le menzioni
MENTIONS_FILE = "mentions.json"

# Pattern per riconoscere contract address Ethereum/BSC
CA_PATTERN = re.compile(r"0x[a-fA-F0-9]{40}")

# Pattern link Dexview, Dexscreener, CMC, ecc.
LINK_PATTERNS = [
    r"https://www\.dexview\.com/(eth|bsc)/0x[a-fA-F0-9]{40}",
    r"https://dexscreener\.com/(eth|bsc)/0x[a-fA-F0-9]{40}",
    r"https://coinmarketcap\.com/currencies/[\w\-]+/?"
]

# Funzione per caricare il JSON esistente
def load_mentions():
    try:
        with open(MENTIONS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Funzione per salvare menzioni
def save_mentions(data):
    with open(MENTIONS_FILE, "w") as f:
        json.dump(data, f, indent=2)

# Inizializza client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    text = event.raw_text
    addresses = set(re.findall(CA_PATTERN, text))
    links = set()

    for pattern in LINK_PATTERNS:
        links.update(re.findall(pattern, text))

    if addresses or links:
        mentions = load_mentions()
        mentions.append({
            "timestamp": datetime.utcnow().isoformat(),
            "chat_id": event.chat_id,
            "addresses": list(addresses),
            "links": list(links),
            "text": text
        })
        save_mentions(mentions)
        print(f"Menzione registrata: {addresses} | {links}")

async def main():
    await client.start()
    print("✅ Listener attivo...")
    asyncio.create_task(post_classifica())  # spam classifica ogni 5 min
    await client.run_until_disconnected()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(client.start())         # Listener
    loop.create_task(post_classifica())      # Spam automatico
    loop.run_forever()
    
    import asyncio
    asyncio.run(main())