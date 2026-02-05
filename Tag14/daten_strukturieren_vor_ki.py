from pathlib import Path

# Pfad zur Datei
pfad = Path(__file__).parent / 'teilnehmer.txt'

# Dictionary für Ergebnisse
punktetabelle = {}

# Datei einlesen und verarbeiten
with pfad.open('r', encoding='utf-8') as datei:
    # zeilenweise lesen
    for zeile in datei:
        # strip() entfernt: \n \r Leerzeichen am Anfang und am Ende
        zeile = zeile.strip()

        # leere Zeile überspringen (mit nächster Zeile weitermachen)
        if not zeile:
            continue
    
        # nur Zeilen mit Trennzeichen verarbeiten (sonst mit nächster Zeile weitermachen)
        if ':' in zeile:
            # Teilen der Zeile in Name und Punktzahl am Doppelpunkt, 1: einmaliges Teilen von rechts
            name, punkte = zeile.rsplit(':', 1)
            # Typumwandlung der Punktzahl in eine Zahl
            punktetabelle[name] = int(punkte)

# Ergebnis ausgeben
print('Punktetabelle:')
print(punktetabelle)