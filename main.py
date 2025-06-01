import json
import asyncio
from datetime import datetime, timedelta
from telethon import TelegramClient, events
from config import API_ID, API_HASH, SESSION_NAME, MONITORED_GROUPS
from ranker import generate_ranking
from poster import post_classifica
from ranker import update_ranking
update_ranking()

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    try:
        if event.chat_id not in MONITORED_GROUPS:
            return

        text = event.message.message
        if not text:
            return

        # Cerca contract address o link rilevanti
        lowered = text.lower()
        if "bscscan.com/token/" in lowered or "dexscreener.com" in lowered or "0x" in lowered:
            mention = {
                "timestamp": datetime.utcnow().isoformat(),
                "chat_id": event.chat_id,
                "message_id": event.message.id,
                "text": text
            }

            with open("mentions.json", "r+") as f:
                data = json.load(f)
                data.append(mention)
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()

            print("✅ Menzione registrata")
            await update_ranking()

    except Exception as e:
        print(f"❌ Errore handler: {e}")

async def start_spam():
    while True:
        try:
            await post_classifica()
        except Exception as e:
            print(f"❌ Errore nello spam della classifica: {e}")
        await asyncio.sleep(300)  # ogni 5 minuti

async def main():
    asyncio.create_task(start_spam())
    await client.start()
    print("🚀 Listener avviato")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
