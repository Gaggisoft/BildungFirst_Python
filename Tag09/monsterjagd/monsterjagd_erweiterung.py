# import des Moduls random
import random

print('--- MONSTERJAGD ---\n')

# Nutzer nach seinem Namen fragen
spieler_name = input('Wie heißt du, mutiger Abenteurer?\n')

# Liste mit Monstern
monster_liste = ['Goblin', 'Vampir', 'Ork', 'Drache', 'Troll']

# Monster-Lexikon
monster_lexikon = {
    'Goblin': 'Kleines, bösartiges Wesen, das in Gruppen angreift.',
    'Vampir': 'Untoter Blutsauger, der sich von Lebenskraft ernährt.',
    'Ork': 'Starkes, kriegerisches Wesen mit grünlicher Haut.',
    'Drache': 'Großes, feuerspeiendes Reptil mit schuppiger Haut.',
    'Troll': 'Großer, dummer Riese, der unter Brücken lebt.'
}

# Lebenspunkte für Spieler und Monster
spieler_hp_max = 20
spieler_hp = spieler_hp_max
monster_hp_max =  None  # wird später abhängig vom Monster gesetzt und für Vampir gebraucht (kann Leben heilen)
monster_hp = monster_hp_max

# Inventar des Spielers
spieler_inventar = []

# mögliche Belohnungen
belohnungen = ['Heiltrank', 'Goldmünzen', 'Magisches Schwert', 'Rüstung', 'Zauberrolle']
# Lexikon für Belohnungen
belohnungen_lexikon = {
    'Heiltrank': 'Heilt 10 Lebenspunkte.',
    'Goldmünzen': 'Gibt dir Gold, das du mit nach Hause nehmen kannst.',
    'Magisches Schwert': 'Erhöht deinen Schaden um 2.',
    'Rüstung': 'Verringert den erlittenen Schaden um 1.',
    'Zauberrolle': 'Erhöht deine maximalen Lebenspunkte um 5.'
}


# Boni durch Gegenstände
spieler_schaden_bonus = 0
spieler_schutz_bonus = 0

# besiegte Monster (für Spielende)
monster_besiegt_anzahl = 0
monster_besiegt_set = set()

# neue Runde starten
spiel_beendet = False

##################################################
# Begrüßung                                      #
##################################################
print(f'\nWillkommen im Zauberwald, {spieler_name}!')

# auf Länge des Namens reagieren
if len(spieler_name) > 5:
    print('Du hast einen mächtigen Namen!\n')
else:
    print('Ein schneller, kurzer Name!\n')

# Wiederholung bis Spieler nicht mehr möchte oder besiegt wurde
while not spiel_beendet:
    # Trenner für Übersicht
    print('################################################')

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

    # Monster-Lexikon-Eintrag anzeigen
    print(f'\nDu schaust in deinem Monster-Lexikon nach:\n{monster_lexikon[monster_aktuell]}')

    # Lebenspunkte des Monsters setzen, Troll ist stärker
    if monster_aktuell == 'Troll':
        monster_hp_max = len(monster_liste) * 2 + 5
    # Lebenspunkte werden nach Position in der Liste (Index) berechnet
    else:
        monster_hp_max = 2*(monster_liste.index(monster_aktuell) + 1) + 5
    # aktuelle Lebenspunkte des Monsters setzen
    monster_hp = monster_hp_max

    ##################################################
    # Kampf beginnt                                  #
    ##################################################

    # Lebenspunkte zum Start anzeigen
    print(f'Du startest mit {spieler_hp} Lebenspunkten. {monster_aktuell} hat {monster_hp} Lebenspunkte.\n')

    ##################################################
    # Inventar anzeigen und nutzen                   #
    ##################################################
    while len(spieler_inventar) > 0:
        # Anzeige des Inventars, wenn nicht leer
        print('\nDu besitzt aktuell folgende Gegenstände:')
        for nummer, gegenstand in enumerate(spieler_inventar, start=1):
            #Gegenstände im Inventar und Beschreibung anzeigen
            print(f'{nummer}.\t{gegenstand}\t-\t{belohnungen_lexikon[gegenstand]}')

        # Inventar nutzen?
        inventar_nummer = input('Wenn Du einen Gegenstand nutzen möchtest, gib die bitte die dazu passende Nummer ein: ')
        if inventar_nummer.isdigit():
            # Cast in Integer
            inventar_nummer = int(inventar_nummer)-1        # bei Aufzählung wurde bei 1 gestartet, Index startet aber bei 0
            if 0 <= inventar_nummer < len(spieler_inventar):
                print(f'Du setzt {spieler_inventar[inventar_nummer]} ein!')
                # Effekt des Gegenstands anwenden
                if spieler_inventar[inventar_nummer] == 'Heiltrank':
                    # Lebenspunkte um 10 erhöhen (Maximum darf nicht überschritten werden)
                    spieler_hp = min(spieler_hp + 10, spieler_hp_max)
                    print(f'Du hast jetzt {spieler_hp} Lebenspunkte.')
                    # Gegenstand aus Inventar entfernen
                    del spieler_inventar[inventar_nummer]
                elif spieler_inventar[inventar_nummer] == 'Goldmünzen':
                    print('Goldmünzen kannst du hier nicht einsetzen.')
                elif spieler_inventar[inventar_nummer] == 'Magisches Schwert':
                    # Bonusschaden erhöhen
                    spieler_schaden_bonus += 2
                    print(f'Du fügst jetzt zusätzlich {spieler_schaden_bonus} Schaden zu.')
                    del spieler_inventar[inventar_nummer]
                elif spieler_inventar[inventar_nummer] == 'Rüstung':
                    # Schaden verringern
                    spieler_schutz_bonus += 1
                    print(f'Du erleidest jetzt {spieler_schutz_bonus} Schaden weniger.')
                    del spieler_inventar[inventar_nummer]
                elif spieler_inventar[inventar_nummer] == 'Zauberrolle':
                    # maximale Lebenspunkte erhöhen
                    spieler_hp_max += 5
                    print(f'Deine maximalen Lebenspunkte sind jetzt {spieler_hp_max}.')
                    del spieler_inventar[inventar_nummer]
                else:
                    print('Der Gegenstand hat keine Wirkung.')
        # Spieler möchte nichts nutzen
        else:
            break


    # Ende wenn Lebenspunkte des Spielers oder Monsters 0 sind
    while spieler_hp > 0 and monster_hp > 0:
        # Spieler greift an
        schaden_spieler = random.randint(1, 4)
        # Schaden des Spielers um Bonus erhöhen und HP des Monsters anpassen
        monster_hp -= max(schaden_spieler + spieler_schaden_bonus, 0)  # Schaden kann nicht negativ werden
        print(f'⚔️ Du greifst an und verursachst {schaden_spieler} Schaden! ⚔️')
        # Drache verbrennt evtl. Rüstung und reduziert Schutzbonus (mit Wahrscheinlichkeit)
        if monster_aktuell == 'Drache' and spieler_schutz_bonus > 0:
            if random.choice([True, False]):  # 1/2 Chance
                spieler_schutz_bonus -= 1
                print('Der Drache hat deine Rüstung teilweise verbrannt! Dein Schutzbonus verringert sich um 1.')
        # Schwert wird bei Ork evtl. stumpf und reduziert Schadenbonus (mit Wahrscheinlichkeit)
        if monster_aktuell == 'Ork' and spieler_schaden_bonus > 0:
            if random.choice([True, False, False]):  # 1/3 Chance
                spieler_schaden_bonus -= 1
                print('Der Ork hat dein Schwert stumpf gemacht! Dein Schadensbonus verringert sich um 1.')
        # Monster wurde besiegt
        if monster_hp <= 0:
            print(f'\n✌️ Du hast {monster_aktuell} besiegt! Herzlichen Glückwunsch! ✌️')
            # besiegtes Monster für Spielende merken
            monster_besiegt_anzahl += 1
            monster_besiegt_set.add(monster_aktuell)
            # Belohnung erhalten
            belohnung = random.choice(belohnungen)
            print(f'Als Belohnung erhältst du: {belohnung}!')
            # Inventar aktualisieren
            spieler_inventar.append(belohnung)
            # neues Spiel starten?
            print(f'\n\n\nDu hast noch {spieler_hp}/{spieler_hp_max} Lebenspunkte.')
            eingabe_neues_spiel = input('Möchtest du ein weiteres Monster bekämpfen? Gib ENDE ein, um nach Hause zu gehen, oder drücke Enter, um weiterzukämpfen.')
            if eingabe_neues_spiel.lower() == 'ende':
                spiel_beendet = True
            break

        # Monster greift an
        schaden_monster = random.randint(1, monster_liste.index(monster_aktuell) + 2)
        # Schaden des Monsters um Bonus verringern und HP des Spielers anpassen
        spieler_hp -= max(schaden_monster - spieler_schutz_bonus, 0)  # Schaden kann nicht negativ werden
        print(f'🩹 {monster_aktuell} greift an und verursacht {schaden_monster} Schaden! 🩹')
        # Vampir erhält Lebenspunkte zurück
        if monster_aktuell == 'Vampir':
            vampir_heilung = schaden_monster // 2  # Vampir heilt die Hälfte des verursachten Schadens
            monster_hp = min(monster_hp + vampir_heilung, monster_hp_max)
            print(f'Der Vampir saugt Lebensenergie und heilt sich um {vampir_heilung} Lebenspunkte!')
        # Spieler wurde besiegt
        if spieler_hp <= 0:
            print('\n🪦 Du wurdest besiegt! Das Abenteuer endet hier. 🪦')
            # Spiel beenden
            spiel_beendet = True
            break
        
        # Ausgabe Lebenspunkte
        print(f'Aktuelle Lebenspunkte:')
        print(f'{spieler_name}: {spieler_hp}/{spieler_hp_max}\n{monster_aktuell}: {monster_hp}/{monster_hp_max}\n')

        # Ausgabe Bonus durch Gegenstände
        print('Bonus durch Gegenstände:')
        print(f'Bonus-Schaden: {spieler_schaden_bonus}\nBonus-Schutz: {spieler_schutz_bonus}')

        # Trenner ausgeben, um mehr Übersicht zu schaffen
        print('-----------------------------------')

##################################################
# Spielende                                      #
##################################################
print('\n\n\n--- SPIEL ENDE ---')
print(f'Du hast insgesamt {monster_besiegt_anzahl} Monster besiegt. Dabei handelte es sich um folgende Monster-Arten: {monster_besiegt_set}.')