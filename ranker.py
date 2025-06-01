import os
import json
import time
from datetime import datetime, timedelta
from collections import Counter
from dateutil.parser import isoparse

VOLUME_DIR = "/mnt/data"
MENTIONS_FILE = os.path.join(VOLUME_DIR, "mentions.json")
RANKING_FILE = os.path.join(VOLUME_DIR, "ranking.json")
TIME_WINDOW_HOURS = 24

# ✅ Se mancano i file, li crea vuoti
def ensure_files_exist():
    if not os.path.exists(MENTIONS_FILE):
        with open(MENTIONS_FILE, "w") as f:
            json.dump([], f)
    if not os.path.exists(RANKING_FILE):
        with open(RANKING_FILE, "w") as f:
            json.dump([], f)

def load_mentions():
    try:
        with open(MENTIONS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_ranking(ranking):
    with open(RANKING_FILE, "w") as f:
        json.dump(ranking, f, indent=2)

def generate_ranking(mentions):
    now = datetime.utcnow()
    cutoff = now - timedelta(hours=TIME_WINDOW_HOURS)
    filtered = [m for m in mentions if isoparse(m["timestamp"]) > cutoff]
    count = Counter([m["address"] for m in filtered])
    final_ranking = [{"address": addr, "mentions": total} for addr, total in count.most_common()]
    return final_ranking

def update_ranking():
    ensure_files_exist()  # ✅ fondamentale per evitare crash
    mentions = load_mentions()
    final_ranking = generate_ranking(mentions)
    save_ranking(final_ranking)