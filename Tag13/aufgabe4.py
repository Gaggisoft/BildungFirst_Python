# DEIN DATEICODE IM HÄRTETEST

from pathlib import Path

def lese_sicher(dateiname):
    # Datei relativ zum Skriptordner suchen
    pfad = Path(__file__).parent / dateiname

    # Fehlende Datei abfangen
    if not pfad.exists():
        return 'Datei nicht gefunden'

    # Datei lesen
    try:
        return pfad.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return 'Encoding-Fehler'


# TEST SETUP
# -------------------------------------------------
root = Path(__file__).parent
test_ordner = root / 'testdaten'
test_ordner.mkdir(exist_ok=True)

# Testdateien anlegen
(test_ordner / 'leer.txt').write_text('', encoding='utf-8')
# ausführliche Version in drei Zeilen statt einer:
#testpfad = test_ordner / 'leer.txt'
#dateiinhalt = ''
#testpfad.write_text(dateiinhalt, encoding='utf-8')

(test_ordner / 'normal.txt').write_text('Hallo Welt', encoding='utf-8')
(test_ordner / 'sonder.txt').write_text('äöü 😀', encoding='utf-8')

# Unterordner anlegen
unter = test_ordner / 'unterordner'
unter.mkdir(exist_ok=True)
(unter / 'innen.txt').write_text('Innen drin', encoding='utf-8')


# TESTS
# -------------------------------------------------
# 1) Datei fehlt
assert lese_sicher('testdaten/gibtsnicht.txt') == 'Datei nicht gefunden', 'Datei fehlt'

# 2) Datei leer
assert lese_sicher('testdaten/leer.txt') == '', 'Datei leer'

# 3) Normale Datei
assert lese_sicher('testdaten/normal.txt') == 'Hallo Welt', 'Normale Datei'

# 4) Ungewöhnliche Zeichen
assert lese_sicher('testdaten/sonder.txt') == 'äöü 😀', 'Ungewöhnliche Zeichen'

# 5) Datei im Unterordner
assert lese_sicher('testdaten/unterordner/innen.txt') == 'Innen drin', 'Datei im Unterordner'


print('Alle Tests erfolgreich')
