# TEXTE KOMBINIEREN

from pathlib import Path


def kombiniere_dateien(ordner, zielname):
    # Basisordner ist der Ordner dieses Skripts
    basis = Path(__file__).parent

    # Datenordner liegt neben dem Skript
    ordnerpfad = basis / ordner
    ordnerpfad.mkdir(exist_ok=True)

    # Alle .txt-Dateien sammeln
    dateien = sorted(ordnerpfad.glob('*.txt'))

    gesamttext = ''

    for p in dateien:
        # Zieldatei nicht erneut einlesen
        if p.name == zielname:
            continue

        # Dateiinhalt lesen und anhängen
        gesamttext += '-> ' + p.name + ' <-\n' + p.read_text(encoding='utf-8') + '\n'

    # Zieldatei im gleichen Ordner speichern
    zielpfad = ordnerpfad / zielname
    zielpfad.write_text(gesamttext, encoding='utf-8')

    return zielpfad


# TEST
# -------------------------------------------------
print(kombiniere_dateien('daten', 'zusammenfassung.txt'))
