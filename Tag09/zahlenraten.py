# Import des Moduls random
import random

# Zufallszahl zwischen 1 und 50 erstellen
ziel = random.randint(1, 50)

# Variable für Tipp (noch leer)
tipp = None

# Anzahl bisheriger Versuche
versuche = 0

# maximale Anzahl Versuche
max_versuche = 7

# Wiederholung bis Zahl erraten oder Versuche aufgebraucht
while tipp != ziel and versuche < max_versuche:
    tipp = int(input('Rate eine Zahl zwischen 1 und 50: '))
    versuche += 1
    
    # Vergleich Tipp mit Ziel
    if tipp < ziel:
        print('Der Tipp ist zu niedrig.')
    elif tipp > ziel:
        print('Der Tipp ist zu hoch.')
    else:
        print(f'Richtig! Du hast {versuche} Versuche gebraucht.')

if tipp != ziel:
    print(f'Leider nicht geschafft, die Maximalanzahl der Versuche wurde erreicht. Die Zahl war {ziel}.')