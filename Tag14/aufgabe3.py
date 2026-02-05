import json
from pathlib import Path

# Daten erstellen
personen = {
    'Lyra': {'rolle': 'Mentorin', 'alter': 35},
    'Ava': {'rolle': 'Mentorin', 'alter': 28},
    'Orion': {'rolle': 'Mentor', 'alter': 42}
}

# Pfad zur JSON-Datei
pfad = Path(__file__).parent / 'personen.json'


# JSON schreiben
with pfad.open('w', encoding='utf-8') as f:
    json.dump(
        personen,
        f,
        ensure_ascii=False,
        indent=2
    )

# JSON lesen
with pfad.open('r', encoding='utf-8') as f:
    daten = json.load(f)


# Ausgabe
for name, info in daten.items():
    print(f'{name} ist {info["alter"]} Jahre alt und arbeitet als {info["rolle"]}.')