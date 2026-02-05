import json
from pathlib import Path

# Dictionary erstellen
mentor = {
    'name': 'Ava',
    'rolle': 'Mentorin',
    'punkte': 95
}

# Pfad zur JSON-Datei
pfad = Path(__file__).parent / 'mentor.json'

# Dictionary in JSON schreiben
with pfad.open('w', encoding='utf-8') as datei:
    json.dump(
        mentor,
        datei,
        ensure_ascii=False,
        indent=2
    )

    print('JSON-Datei erstellt:', pfad.name)

# JSON einlesen
with pfad.open('r', encoding='utf-8') as datei:
    geladene_daten = json.load(datei)

print('\nGeladene Daten:')
print(geladene_daten)

print('Name aus JSON:', geladene_daten['name'])

# JSON aus String
text = '{"Lyra":35,"Ava":28,"Orion":42}'
daten = json.loads(text)
print(daten["Lyra"])

# Alternative zum Öffnen (Bitte nicht verwenden!!!!)
pfad = r"PFAD ZUR JSON-DATEI"
with open(pfad, 'r', encoding='utf-8') as datei:
    daten = json.load(datei)
print(daten['name'])