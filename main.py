import asyncio
import json
from datetime import datetime
from telethon import TelegramClient, events
from config import API_ID, API_HASH, CHANNEL_ID, MENTIONS_FILE, RANKING_FILE
from ranker import update_ranking, save_mentions, load_mentions

# Percorso assoluto della sessione salvata nel volume Railway
SESSION_PATH = "/mnt/anon.session"
import os
print(f"📂 Verifica file sessione su Railway: {SESSION_PATH} – Esiste: {os.path.exists(SESSION_PATH)}")

client = TelegramClient(SESSION_PATH, API_ID, API_HASH)


@client.on(events.NewMessage(chats=CHANNEL_ID))
async def handler(event):
    text = event.raw_text
    mentions = load_mentions()
    mentions.append({
        "text": text,
        "timestamp": datetime.utcnow().isoformat()
    })
    save_mentions(mentions)
    print("✅ Menzione registrata")


async def main():
    print(f"✅ Parsing API_ID: {API_ID}")
    print(f"✅ Parsing CHANNEL_ID: {CHANNEL_ID}")
    print(f"✅ Normalized API_ID: {int(API_ID)}")
    print(f"✅ Normalized CHANNEL_ID: {int(CHANNEL_ID)}")

    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Sessione non autorizzata. Autenticarsi in locale.")
        return

    mentions = load_mentions()
    print("📊 Classifica vuota" if not mentions else f"📊 Menzioni caricate: {len(mentions)}")

    # Genera classifica iniziale
    update_ranking()
    print("✅ Ranking aggiornato correttamente.")
    print("🚀 Listener avviato")

    await client.run_until_disconnected()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🔴 Listener interrotto")