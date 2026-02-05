# durch KI-Prompt
# Verbessere bitte meinen Code, indem Sonderfälle abgefangen werden.
# veränderter Code
# ursprüngliche Version: daten_strukturieren_vor_ki.py

from pathlib import Path

# Pfad zur Datei
pfad = Path(__file__).parent / 'teilnehmer.txt'

# Dictionary für Ergebnisse
punktetabelle = {}

# Prüfen, ob die Datei existiert
if not pfad.exists():
    print(f"Fehler: Die Datei '{pfad}' wurde nicht gefunden.")
else:
    # Datei einlesen und verarbeiten
    with pfad.open('r', encoding='utf-8') as datei:
        # zeilenweise lesen
        for zeilennummer, zeile in enumerate(datei, start=1):
            # strip() entfernt: \n \r Leerzeichen am Anfang und am Ende
            zeile = zeile.strip()

            # leere Zeile überspringen (mit nächster Zeile weitermachen)
            if not zeile:
                continue
        
            # nur Zeilen mit Trennzeichen verarbeiten (sonst mit nächster Zeile weitermachen)
            if ':' in zeile:
                # Teilen der Zeile in Name und Punktzahl am Doppelpunkt, 1: einmaliges Teilen von rechts
                name, punkte = zeile.rsplit(':', 1)
                
                # Leerzeichen entfernen
                name = name.strip()
                punkte = punkte.strip()
                
                # Prüfen, ob Name und Punktzahl vorhanden sind
                if not name:
                    print(f"Warnung Zeile {zeilennummer}: Kein Name vorhanden - Zeile wird übersprungen.")
                    continue
                
                if not punkte:
                    print(f"Warnung Zeile {zeilennummer}: Keine Punktzahl vorhanden für '{name}' - Zeile wird übersprungen.")
                    continue
                
                # Typumwandlung der Punktzahl in eine Zahl
                try:
                    punktetabelle[name] = int(punkte)
                except ValueError:
                    print(f"Warnung Zeile {zeilennummer}: Ungültige Punktzahl '{punkte}' für '{name}' - Zeile wird übersprungen.")
            else:
                print(f"Warnung Zeile {zeilennummer}: Keine gültige Zeile (fehlendes ':'): '{zeile}'")

# Ergebnis ausgeben
print('\nPunktetabelle:')
print(punktetabelle)