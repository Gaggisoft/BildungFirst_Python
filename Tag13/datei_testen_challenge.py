from pathlib import Path

# ZU TESTENDE FUNKTIONEN
# -------------------------------------------------
# Beispiele aus den vorherigen UEs

def lese_datei(dateiname):
    # Pfad relativ zum Skriptordner
    pfad = Path(__file__).parent / dateiname

    # Fehlende Datei abfangen
    if not pfad.exists():
        return 'Datei nicht gefunden'

    # Datei lesen
    try:
        return pfad.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return 'Fehler: Datei kann nicht als UTF-8 gelesen werden'

def kombiniere_dateien(ordnername, zielname):
    # Ordner relativ zum Skriptordner
    ordner = Path(__file__).parent / ordnername
    ordner.mkdir(exist_ok=True)

    # Alle .txt-Dateien sammeln
    dateien = sorted(ordner.glob('*.txt'))

    gesamt = ''
    for p in dateien:
        gesamt += p.read_text(encoding='utf-8') + '\n'

    # Zieldatei im gleichen Ordner speichern
    zielpfad = ordner / zielname
    zielpfad.write_text(gesamt, encoding='utf-8')

    return zielpfad

# TEST SETUP
# -------------------------------------------------
# Wir erstellen einen kleinen Testordner,
# damit Tests unabhängig vom echten daten Ordner laufen.

root = Path(__file__).parent
tordner = root / 'testdaten'
tordner.mkdir(exist_ok=True)

# Testdateien anlegen
(tordner / 'a.txt').write_text('Hallo\nWelt', encoding='utf-8')
(tordner / 'b.txt').write_text('', encoding='utf-8')

# TESTS
# -------------------------------------------------
