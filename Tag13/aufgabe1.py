# DATEIEN SICHER ÖFFNEN

from pathlib import Path


def lese_sicher(dateiname):
    # Pfad relativ zum Skriptordner aufbauen
    pfad = Path(__file__).parent / dateiname

    # Datei existiert nicht
    if not pfad.exists():
        return 'Datei nicht gefunden'

    # Datei lesen
    try:
        return pfad.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return 'Encoding-Fehler'


# TESTS
# -------------------------------------------------
print(lese_sicher('beispiel.txt'))
print(lese_sicher('gibtsnicht.txt'))
