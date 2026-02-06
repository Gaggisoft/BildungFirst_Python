import json
from pathlib import Path

# Konstante mit Pfad zur JSON-Datei
FILE_PATH = Path(__file__).parent / 'inventory.json'

# Speichern des Dictionary in JSON-Datei
def save_inventory(inventory, path=FILE_PATH):
    with path.open('w', encoding='utf-8') as file:
        json.dump(inventory, file, ensure_ascii=False, indent=2)
    # Rückmeldung über Speicherung
    print('Inventar gespeichert in:', path.name)

# Laden des Dictionary aus einer JSON-Datei
def load_inventory(path=FILE_PATH):
    # Pfad existiert nicht
    if not path.exists():
        print('Datei wurde nicht gefunden.')
        return {}
    
    try:
        # Datei öffnen und Daten laden
        with path.open('r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Daten überprüfen
        if not isinstance(data, dict):
            print('Ungültiges Datenformat. Start mit leerem Inventar.')
            return {}
        
        # korrekte Daten zurückgeben
        print(f'Inventar aus Datei {path.name} geladen.')
        return data
    except (json.JSONDecodeError, UnicodeDecodeError):
        print('JSON beschädigt oder unlesbar. Start mit leerem Inventar.')
        return {}