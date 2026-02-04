from pathlib import Path

def kombiniere_dateien(ordner, zielname):
    # Ordner relativ zum Skript finden
    basis = Path(__file__).parent
    # Zielordner liegt im gleichen Ordner, wie die .py Datei
    ordnerpfad = basis / ordner
    ordnerpfad.mkdir(exist_ok=True)

    # .txt einlesen
    dateien = sorted(ordnerpfad.glob('*.txt'))
    
    # Inhalte kombinieren
    gesamttext = ''

    for datei in dateien:
        # Dateiinhalt lesen und anhängen
        text = datei.read_text(encoding='utf-8')
        gesamttext += text + '\n'

    # Zieldatei schreiben
    zielpfad = ordnerpfad / zielname
    zielpfad.write_text(gesamttext, encoding='utf-8')

    # Rückgabe des Zielpfads
    return zielpfad

# Test
print(kombiniere_dateien('daten', 'kombination.txt'))