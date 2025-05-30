from aiogram import Bot
from aiogram.enums import ParseMode
from config import BOT_TOKEN, CHANNEL_ID
import json
from datetime import datetime

# Inizializza il bot
bot = Bot(token=BOT_TOKEN)  # ✅ OK

async def post_classifica():
    with open("ranking.json", "r") as f:
        data = json.load(f)

    if not data:
        return

    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    messaggio = f"<b>🔥 TOP MENTIONED BSC TOKENS – {now}</b>\n\n"

    for i, entry in enumerate(data, start=1):
        name = entry["name"]
        symbol = entry["symbol"]
        mentions = entry["mentions"]
        messaggio += f"<b>{i}.</b> {name} ({symbol}) – {mentions} mentions\n"

    messaggio += "\nPowered by @ShillTrackBot"

    await bot.send_message(chat_id=CHANNEL_ID, text=messaggio, parse_mode="HTML")  # ✅ OK