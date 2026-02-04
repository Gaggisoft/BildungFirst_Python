# DATEN ABLEGEN

from pathlib import Path


def speichere_sicher(dateiname, text):
    # Pfad relativ zum Skriptordner
    pfad = Path(__file__).parent / dateiname

    # Existiert die Datei bereits?
    if pfad.exists():
        # Backup-Datei erzeugen
        backup = pfad.with_name(pfad.stem + '_backup' + pfad.suffix)
        pfad.rename(backup)

    # Neuen Inhalt schreiben
    pfad.write_text(text, encoding='utf-8')

    return dateiname + ' gespeichert'


# TESTS
# -------------------------------------------------
print(speichere_sicher('log.txt', 'Erster Inhalt'))
print(speichere_sicher('log.txt', 'Zweiter Inhalt'))
