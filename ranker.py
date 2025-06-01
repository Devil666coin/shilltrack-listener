import json
import time
from datetime import datetime, timedelta
from collections import Counter
from dateutil.parser import isoparse
import os

VOLUME_DIR = "/mnt/data"
MENTIONS_FILE = os.path.join(VOLUME_DIR, "mentions.json")
RANKING_FILE = os.path.join(VOLUME_DIR, "ranking.json")
TIME_WINDOW_HOURS = 24

# 🔧 Crea i file vuoti se non esistono
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

    filtered = [
        m for m in mentions
        if datetime.fromisoformat(m["timestamp"]) > cutoff
    ]

    count = Counter([m["address"] for m in filtered])
    final_ranking = []

    for i, (address, total) in enumerate(count.most_common(10), 1):
        final_ranking.append({
            "rank": i,
            "address": address,
            "mentions": total
        })

    return final_ranking

def update_ranking():
    mentions = load_mentions()
    ranking = generate_ranking(mentions)
    save_ranking(ranking)