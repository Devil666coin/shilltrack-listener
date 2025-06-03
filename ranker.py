import os
import json
from datetime import datetime, timedelta
from collections import Counter
from dateutil.parser import isoparse

VOLUME_DIR = "/mnt/data"
MENTIONS_FILE = os.path.join(VOLUME_DIR, "mentions.json")
RANKING_FILE = os.path.join(VOLUME_DIR, "ranking.json")
TIME_WINDOW_HOURS = 24

def ensure_files_exist():
    """Crea mentions.json e ranking.json se non esistono"""
    try:
        os.makedirs(VOLUME_DIR, exist_ok=True)
        if not os.path.exists(MENTIONS_FILE):
            with open(MENTIONS_FILE, "w") as f:
                json.dump([], f)

        if not os.path.exists(RANKING_FILE):
            with open(RANKING_FILE, "w") as f:
                json.dump([], f)
    except Exception as e:
        print("Errore creazione file:", e)

def load_mentions(path=MENTIONS_FILE):
    try:
        with open(MENTIONS_FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            else:
                print("⚠️ Il file mentions.json non è un dizionario.")
                return {}
    except Exception as e:
        print("Errore lettura mentions:", e)
        return {}

def save_mentions(mentions: list, path: str = "mentions.json"):
    import json
    with open(path, "w", encoding="utf-8") as f:
        json.dump(mentions, f, ensure_ascii=False, indent=2)

def save_ranking(ranking):
    try:
        with open(RANKING_FILE, "w") as f:
            json.dump(ranking, f, indent=2)
    except Exception as e:
        print("Errore salvataggio ranking:", e)

# ranker.py
def generate_ranking(mentions, ranking_path):
    try:
        # Conta le occorrenze per ogni contract address
        counts = {}
        for mention in mentions:
            ca = mention.get("contract")
            if ca:
                counts[ca] = counts.get(ca, 0) + 1

        # Ordina per numero di menzioni (discendente) e prendi i top 10
        top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]

        # Salva il ranking su file
        with open(ranking_path, "w") as f:
            json.dump(top, f, indent=2)

        print("✅ Ranking aggiornato correttamente.")

    except Exception as e:
        print("Errore durante la generazione del ranking:", e)

def update_ranking():
    ensure_files_exist()
    mentions = load_mentions()
    generate_ranking(mentions)