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
# lese_dateien
# -------------------------------------------------
# Datei fehlt
assert lese_datei('gibt_es_nicht.txt') == 'Datei nicht gefunden'

# Datei vorhanden, Inhalt korrekt
probe = tordner / 'probe.txt'
probe.write_text('Zeile 1\nZeile 2', encoding='utf-8')
assert 'Zeile 2' in lese_datei(str(probe))

# leere Datei
assert lese_datei(str(tordner / 'b.txt')) == ''

# ungewöhnliche Zeichen
assert lese_datei(str(tordner / 'sonder.txt')) == 'äöü 😀'

# falschen Pfad im Unterordner
assert lese_datei('testdaten/gibt_es_auch_nicht.txt') == 'Datei nicht gefunden'

print('\nAlle Tests von lese_dateien waren erfolgreich.\n')

# -------------------------------------------------
# kombiniere_dateien
# -------------------------------------------------
# Zieldatei erstellt
ziel = kombiniere_dateien('testdaten', 'zusammenfassung.txt')
assert ziel.exists()

# Inhalte aus a.txt enthalten
text = ziel.read_text(encoding='utf-8')
assert 'Hallo' in text
assert 'Welt' in text

# leere Dateien stören nicht
assert text.count('\n') >= 1

# Sonderzeichen bleiben erhalten
assert 'äöü' in text
assert '😀' in text

# Ordner ohne .txt-Dateien
leerordner = root / 'leerordner'
leerordner.mkdir(exist_ok=True)
ziel2 = kombiniere_dateien('leerordner', 'out.txt')
assert ziel2.exists()
assert ziel2.read_text(encoding='utf-8') == ''

print('\nAlle Tests von kombiniere_dateien waren erfolgreich.\n')