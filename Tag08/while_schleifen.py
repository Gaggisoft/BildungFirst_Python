# while-Schleifen

# Definition der Schleifenvariablen
# hier: Startwert 0
schleifenvariable = 0

# Beginn der while-Schleife
while schleifenvariable < 10:       # nicht: schleifenvariable != 10:
    print(f'Die Schleife läuft noch, die Schleifenvariable ist: {schleifenvariable}.')
    schleifenvariable += 3          # schleifenvariable = schleifenvariable + 1
print('Ende der Schleifendurchführung')

weiter = True
zaehler = 0
while weiter:
    zaehler += 1
    if zaehler >= 10:
        weiter = False
    print(f'Die Schleife läuft noch, Schleifendurchlauf #{zaehler}')
    weiter = True