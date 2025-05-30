import asyncio
import json
import re
from datetime import datetime
from telethon import TelegramClient, events
from config import API_ID, API_HASH
from ranker import load_mentions, save_mentions
from poster import post_classifica


# Crea client Telethon con il tuo account personale
client = TelegramClient("sessione", API_ID, API_HASH)

PATTERNS = [
    r"(0x[a-fA-F0-9]{40})",                    # Contract address
    r"(https:\/\/dexscreener\.com\/[^\s]+)",   # Link Dexscreener
]

@client.on(events.NewMessage)
async def handler(event):
    if not event.message.message:
        return

    text = event.message.message
    addresses = set()
    links = set()

    for pattern in PATTERNS:
        addresses.update(re.findall(pattern, text))
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
    print("🎧 Listener attivo...")
    asyncio.create_task(post_classifica())  # spam automatico classifica
    await client.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(client.start())  # avvia il listener
    loop.create_task(post_classifica())  # spam automatico
    loop.run_forever()
    asyncio.run(main())
