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
try:
    with pfad.open('w', encoding='utf-8') as datei:
        json.dump(
            mentor,
            datei,
            ensure_ascii=False,
            indent=2
        )
    print('JSON-Datei erstellt:', pfad.name)
except PermissionError:
    print(f'Fehler: Keine Schreibrechte für {pfad}')
except OSError as e:
    print(f'Fehler beim Schreiben der Datei: {e}')

# JSON einlesen
try:
    with pfad.open('r', encoding='utf-8') as datei:
        geladene_daten = json.load(datei)
    
    print('\nGeladene Daten:')
    print(geladene_daten)
    
    # Sicherer Zugriff auf Dictionary-Keys
    if 'name' in geladene_daten:
        print('Name aus JSON:', geladene_daten['name'])
    else:
        print('Warnung: Key "name" nicht in JSON gefunden')
        
except FileNotFoundError:
    print(f'Fehler: Datei {pfad} nicht gefunden')
except json.JSONDecodeError as e:
    print(f'Fehler: Ungültiges JSON-Format - {e}')
except PermissionError:
    print(f'Fehler: Keine Leserechte für {pfad}')

# JSON aus String
text = '{"Lyra":35,"Ava":28,"Orion":42}'
daten = json.loads(text)
print(daten["Lyra"])

# Alternative zum Öffnen (Bitte nicht verwenden!!!!)
pfad = r"PFAD ZUR JSON-DATEI"
with open(pfad, 'r', encoding='utf-8') as datei:
    daten = json.load(datei)
print(daten['name'])