# Nutzer nach seinem Budget fragen => Variable budget
budget = int(input('Wie viel Geld hast du heute Abend?\n'))

# Nutzer fragen, ob Gutschein vorhanden ist => variable gutschein
gutschein = input('Hast du einen Gutschein (ja / nein)?\n')

if budget >= 30 and gutschein == 'ja':
    print('Restaurantbesuche mit Rabatt möglich')
elif budget >= 30 and gutschein == 'nein':
    print('Restaurantbesuche möglich, aber ohne Rabatt')
elif budget < 30 or gutschein == 'ja':
    print('Mit Gutschein oder kleiner Kasse reicht es zumindest für was Günstiges.')
else:
    print('Nicht genug Budget, lieber zu Hause essen.') # nicht erreichbar (nur bei falscher Eingabe für Gutschein)