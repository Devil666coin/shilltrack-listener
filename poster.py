import json
from config import CHANNEL_ID, BOT_TOKEN
from aiogram import Bot

async def post_classifica():
    try:
        with open("ranking.json", "r") as f:
            data = json.load(f)

        if not data:
            print("⚠️ Classifica vuota.")
            return

        msg = "🔥 Top Shilled Tokens (24h) 🔥\n\n"
        for i, token in enumerate(data[:10], 1):
            symbol = token.get("symbol", "N/A")
            count = token.get("count", 0)
            msg += f"{i}. {symbol} – {count} mentions\n"

        bot = Bot(token=BOT_TOKEN, parse_mode="Markdown")
        await bot.send_message(chat_id=CHANNEL_ID, text=msg)
        print("✅ Classifica inviata")

    except Exception as e:
        print(f"❌ Errore post_classifica: {e}")