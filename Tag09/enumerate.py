# Beispiel: Obstliste
#obst_liste = ['Apfel', 'Banane', 'Birne', 'Kirsche']

#for index, wert in enumerate(obst_liste):
#    print(f'{index}. {wert}')

#for zahl, wert in enumerate(obst_liste, start=1):
#    print(f'{zahl}. {wert}')

# Beispiel: Code
text = ['Alles okay',
        'Warnung: Speicher knapp',
        'Fehler: Tippfehler gefunden',
        'Alles okay',
        'Fehler: Datei nicht gefunden']

for zeile_nr, inhalt in enumerate(text, start=1):       # start= kann weggelassen werden
    if 'Fehler' in inhalt:
        print(f'!!! Fehler in Zeile {zeile_nr}: {inhalt}')