from pathlib import Path

pfad = Path(__file__).parent / 'personen.txt'
personen = {}

# Datei einlesen
with pfad.open('r', encoding='utf-8') as f:
    for zeile in f:
        zeile = zeile.strip()

        # Leere Zeilen überspringen
        if not zeile:
            continue

        # Nur gültige Zeilen verarbeiten
        if ':' in zeile:
            name, alter = zeile.split(':', 1)

            # Nur Zahlen als Alter akzeptieren
            if alter.strip().isdigit():
                personen[name.strip()] = int(alter.strip())

# Ausgabe
for name, alter in personen.items():
    print(f'{name} ist {alter} Jahre alt')