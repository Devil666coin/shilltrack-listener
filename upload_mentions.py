import shutil

# Copia locale → Railway volume
shutil.copyfile("mentions.json", "/mnt/mentions.json")
print("✅ File 'mentions.json' copiato su /mnt/")