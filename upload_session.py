import os

# CREA LA CARTELLA /mnt SE NON ESISTE
os.makedirs("/mnt", exist_ok=True)

# COPIA IL FILE
with open("anon.session", "rb") as f_in:
    content = f_in.read()

with open("/mnt/anon.session", "wb") as f_out:
    f_out.write(content)

print("✅ File copiato su /mnt/anon.session")