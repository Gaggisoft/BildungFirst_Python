print('--- MONSTERJAGD ---\n')

# Nutzer nach seinem Namen fragen
spieler_name = input('Wie heißt du, mutiger Abenteurer?\n')

##################################################
# Begrüßung                                      #
##################################################
print(f'\nWillkommen im Zauberwald, {spieler_name}!')

# auf Länge des Namens reagieren
if len(spieler_name) > 5:
    print('Du hast einen mächtigen Namen!')
else:
    print('Ein schneller, kurzer Name!')