with open("ranking.json", "rb") as f_in:
    with open("/mnt/ranking.json", "wb") as f_out:
        f_out.write(f_in.read())

print("✅ File 'ranking.json' caricato nel volume.")