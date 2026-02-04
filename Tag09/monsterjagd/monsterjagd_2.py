# import des Moduls random
import random

print('--- MONSTERJAGD ---\n')

# Nutzer nach seinem Namen fragen
spieler_name = input('Wie heißt du, mutiger Abenteurer?\n')

# Liste mit Monstern
monster_liste = ['Goblin', 'Vampir', 'Ork', 'Drache', 'Troll']

##################################################
# Begrüßung                                      #
##################################################
print(f'\nWillkommen im Zauberwald, {spieler_name}!')

# auf Länge des Namens reagieren
if len(spieler_name) > 5:
    print('Du hast einen mächtigen Namen!\n')
else:
    print('Ein schneller, kurzer Name!\n')

##################################################
# Monster erscheint                              #
##################################################

# Monster zufällig wählen
monster_aktuell = random.choice(monster_liste)

# Ausgabe des gewählten Monsters
print(f'Ein {monster_aktuell} erscheint!')
# besondere Warnung beim Troll
if monster_aktuell == 'Troll':
    print('Vorsicht! Trolle sind besonders gefährlich!')