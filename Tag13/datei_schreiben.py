from pathlib import Path

# Basisordner festlegen
# __file__ enthält Pfad zur .py Datei
# .parent ist der Ordner, in dem die .py Datei liegt
# globals() enthält alle globalen Variablen / Funktionen / importierten Module / Spezialvariablen (z. B. __file__)
if '__file__' in globals():
    basis_ordner = Path(__file__).parent
# ___file__ existiert nicht
# Es wird der aktuelle Arbeitsordner verwendet
else:
    basis_ordner = Path.cwd()

pfad = basis_ordner / 'beispiel_schreiben.txt'

# Überprüfung, ob Datei bereits existiert => nicht schreiben
if pfad.exists():
    print('Achtung! Die Datei existiert bereits.')
    print('Nichts wurde überschrieben.')
# Datei existiert noch nicht => kann geschrieben werden
else:
    # Datei mit dem Modus 'w' (schreiben) und Encoding UTF-8 öffnen
    with pfad.open('w', encoding='utf-8') as datei:
        # Inhalt in Datei schreiben
        datei.write('Erster Testinhalt\n')
        datei.write('Noch eine Zeile')
    # Meldung, dass Schreiben abgeschlossen ist
    print('Die Datei wurde erstellt und beschrieben.')

# Ausgaben zu Datei-Infos
print('Datei-Pfad:', pfad.resolve())
print('Datei-Name:', pfad.name)