import json
import time
from datetime import datetime, timedelta
from collections import Counter

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

def generate_ranking():
    now = time.time()
    cutoff = now - TIME_WINDOW_HOURS * 3600
    mentions = load_mentions()

    filtered = [m["address"] for m in mentions if m["timestamp"] > cutoff]
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

if name == "__main__":
    while True:
        generate_ranking()
        time.sleep(30)