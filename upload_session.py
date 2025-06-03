import shutil
import os

# File di sessione locale (già valido)
LOCAL_SESSION = "anon.session"

# Percorso corretto nel volume Railway
RAILWAY_SESSION = "/mnt/anon.session"

if os.path.exists(LOCAL_SESSION):
    shutil.copyfile(LOCAL_SESSION, RAILWAY_SESSION)
    print("✅ Sessione copiata su Railway (/mnt/anon.session)")
else:
    print("❌ File locale 'anon.session' non trovato")