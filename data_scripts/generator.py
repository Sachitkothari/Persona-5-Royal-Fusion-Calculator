import requests
from bs4 import BeautifulSoup
import json

ARCANAS = [
    "Fool", "Magician", "Priestess", "Empress", "Emperor", "Hierophant",
    "Lovers", "Chariot", "Justice", "Hermit", "Fortune", "Strength",
    "Hanged_Man", "Death", "Temperance", "Devil", "Tower", "Star",
    "Moon", "Sun", "Judgement", "Faith", "Councillor"
]

BASE = "https://megamitensei.fandom.com/wiki/{}_Arcana"

personas = []

for arcana in ARCANAS:
    url = BASE.format(arcana)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.select("table.table.p5")
    tables = tables[1:]

    for table in tables:
        rows = table.select("tr")[1:]
        for row in rows:
            cols = row.select("td")
            if len(cols) < 2:
                continue

            name = cols[0].get_text(strip=True)
            level_text = cols[1].get_text(strip=True)

            try:
                level = int(level_text)
            except ValueError:
                continue

            personas.append({
                "name": name,
                "arcana": arcana.replace("_", " "),
                "level": level
            })

unique = {}
for p in personas:
    unique[p["name"]] = p

personas = list(unique.values())
# Save to JSON file
with open("persona_list.json", "w", encoding="utf-8") as f:
    json.dump(personas, f, indent=2, ensure_ascii=False)

print("Saved persona_list.json")
