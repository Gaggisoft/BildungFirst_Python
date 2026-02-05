import random

# Dictionary jeweils mit Tuple als Schlüssel und String als Wert
welt = {
    (0, 0) : "leer",
    (1, 0) : "spieler",
    (2, 0) : "dino",
    (1, 1) : "baum"
}
# Startposition
spieler_position = (1, 0)

# mögliche Bewegungen
bewegungen = [(0, 1),
              (0, -1),
              (1, 0),
              (-1, 0)]

for schritt in range(1,11):
    print(f'Der Spieler macht seinen {schritt}. Schritt.')
    # zufällige Bewegung des Spielers erhalten
    aktuelle_bewegung = random.choice(bewegungen)
    # Spielerposition anpassen
    # neues Tuple, keine Änderung des aktuellen!!!
    spieler_position = (spieler_position[0] + aktuelle_bewegung[0],
                        spieler_position[1] + aktuelle_bewegung[1])
    if spieler_position in welt:
        print(f'Der Spieler trifft auf {welt[spieler_position]}.\n')
    else:
        print('Der Spieler ist alleine auf seinem Feld.\n')