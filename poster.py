import asyncio
import json
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
from config import BOT_TOKEN, CHANNEL_ID

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

RANKING_FILE = "ranking.json"

def load_ranking():
    try:
        with open(RANKING_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Errore nel caricamento della classifica: {e}")
        return []

def format_ranking(ranking):
    if not ranking:
        return "📊 <b>Nessuna menzione registrata</b>"

    lines = ["🔥 <b>Top Tokens (24h)</b>\n"]
    for i, item in enumerate(ranking, 1):
        ca = item["address"]
        count = item["count"]
        lines.append(f"{i}. <code>{ca}</code> — <b>{count} mentions</b>")
    lines.append("\n📡 Powered by <a href='https://t.me/ShillTrackBot'>ShillTrack</a>")
    return "\n".join(lines)

async def post_classifica():
    while True:
        ranking = load_ranking()
        text = format_ranking(ranking)

        try:
            await bot.send_message(CHANNEL_ID, text)
            logging.info("✅ Classifica inviata su Telegram.")
        except Exception as e:
            logging.error(f"❌ Errore nell'invio: {e}")

        await asyncio.sleep(300)  # 5 minuti

if __name__ == "__main__":
    asyncio.run(post_classifica())