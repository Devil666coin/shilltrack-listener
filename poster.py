import json
import time
import asyncio
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID
from aiogram import Bot, Dispatcher

async def post_ranking():
    bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    while True:
        try:
            with open("ranking.json", "r") as file:
                ranking = json.load(file)

            if not ranking:
                await asyncio.sleep(300)
                continue

            message = "<b>🔥 Top Mentioned Tokens (24h)</b>\n\n"
            for i, item in enumerate(ranking, 1):
                message += f"{i}. <code>{item['address']}</code> — {item['mentions']} mention(s)\n"

            await bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)
            print("✅ Classifica inviata nel canale.")
        except Exception as e:
            print(f"Errore nel posting: {e}")

        await asyncio.sleep(300)  # aspetta 5 minuti

if __name__ == "__main__":
    asyncio.run(post_ranking())