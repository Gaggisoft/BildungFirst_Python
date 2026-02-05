import json
from pathlib import Path


# Datentypen sauber halten
daten = {
    'name': 'Lyra',
    'rolle': 'Mentorin',
    'alter': 35
}

pfad = Path(__file__).parent / 'daten.json'


# JSON sicher speichern
with pfad.open('w', encoding='utf-8') as f:
    json.dump(daten, f, ensure_ascii=False, indent=2)

print('✅ Datei erstellt unter:', pfad.resolve())


# Mini-Test: Datei direkt wieder laden
with pfad.open('r', encoding='utf-8') as f:
    geladen = json.load(f)

print('Geladen:', geladen)
print('Alter:', geladen['alter'])