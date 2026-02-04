# import des Moduls random
import random

print('--- MONSTERJAGD ---\n')

# Nutzer nach seinem Namen fragen
spieler_name = input('Wie heißt du, mutiger Abenteurer?\n')

# Liste mit Monstern
monster_liste = ['Goblin', 'Vampir', 'Ork', 'Drache', 'Troll']

# Lebenspunkte für Spieler und Monster
spieler_hp = 20
monster_hp = None  # wird später abhängig vom Monster gesetzt

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

# Lebenspunkte des Monsters setzen, Troll ist stärker
if monster_aktuell == 'Troll':
    monster_hp = len(monster_liste) * 2 + 5
# Lebenspunkte werden nach Position in der Liste (Index) berechnet
else:
    monster_hp = 2*(monster_liste.index(monster_aktuell) + 1) + 5

##################################################
# Kampf beginnt                                  #
##################################################

# Lebenspunkte zum Start anzeigen
print(f'Du startest mit {spieler_hp} Lebenspunkten. {monster_aktuell} hat {monster_hp} Lebenspunkte.\n')

# Ende wenn Lebenspunkte des Spielers oder Monsters 0 sind
while spieler_hp > 0 and monster_hp > 0:
    # Spieler greift an
    schaden_spieler = random.randint(1, 4)
    monster_hp -= schaden_spieler
    print(f'Du greifst an und verursachst {schaden_spieler} Schaden!')
    # Monster wurde besiegt
    if monster_hp <= 0:
        print(f'\nDu hast {monster_aktuell} besiegt! Herzlichen Glückwunsch!')
        continue

    # Monster greift an
    schaden_monster = random.randint(1, monster_liste.index(monster_aktuell) + 1)
    spieler_hp -= schaden_monster
    print(f'{monster_aktuell} greift an und verursacht {schaden_monster} Schaden!')
    # Spieler wurde besiegt
    if spieler_hp <= 0:
        print('\nDu wurdest besiegt! Das Abenteuer endet hier.')
        continue
    
    # Ausgabe Lebenspunkte
    print(f'Aktuelle Lebenspunkte:\n{spieler_name}: {spieler_hp}\n{monster_aktuell}: {monster_hp}\n')

##################################################
# Spielende                                      #
##################################################
print('\n--- SPIEL ENDE ---')