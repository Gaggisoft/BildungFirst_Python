from pathlib import Path

# Basisordner festlegen
# __file__ enthält Pfad zur .py Datei
# .parent ist der Ordner, in dem die .py Datei liegt
if '__file__' in globals():
    basis_ordner = Path(__file__).parent
# ___file__ existiert nicht
# Es wird der aktuelle Arbeitsordner verwendet
else:
    basis_ordner = Path.cwd()

# Dateipfad zusammebauen
# / ist ein Operator von pathlib
# Es wird ein neuer Pfad erzeugt, der aus dem Pfad in basis_ordner und dem Dateinamen 'beispiel.txt' besteht
datei_pfad = basis_ordner / 'beispiel.txt'
print('Ich suche die Datei hier:')
print(datei_pfad.resolve())

# Detei öffnen
try:
    # Modus 'r': lesen
    # Encoding: UTF-8
    # geöffnete Datei kann anschließend mit datei angesprochen werden
    with datei_pfad.open('r', encoding='utf-8') as datei:
        inhalt = datei.read()
    
    print('\nDateiinhalt:')
    print(inhalt)
# Datei wurde nicht gefunden
except FileNotFoundError:
    print('\nDatei wurde nicht gefunden.')
    print('Lege \'beispiel.txt\' in denselben Ordner, wie dieses Skript')
# Ecoding-Fehler
except UnicodeDecodeError:
    print('Encoding-Problem')
    print('Bitte speichere die Datei als UTF-8.')