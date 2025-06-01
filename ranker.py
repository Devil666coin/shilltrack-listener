import json
import time
from datetime import datetime, timedelta
from collections import Counter
from dateutil.parser import isoparse

MENTIONS_FILE = "mentions.json"
RANKING_FILE = "ranking.json"
TIME_WINDOW_HOURS = 24

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
    now = time.time()
    cutoff = now - TIME_WINDOW_HOURS * 3600

    filtered = []
    for m in mentions:
        try:
            ts = isoparse(m["timestamp"]).timestamp()
            if ts > cutoff:
                filtered.append(m["address"])
        except Exception:
            continue

    count = Counter(filtered)
    ranking = count.most_common()

    final_ranking = []
    for i, (address, total) in enumerate(ranking, 1):
        final_ranking.append({
            "position": i,
            "address": address,
            "mentions": total
        })

    save_ranking(final_ranking)

def update_ranking():
    mentions = load_mentions()
    generate_ranking(mentions)
