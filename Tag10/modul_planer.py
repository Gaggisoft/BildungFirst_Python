# Funktion Planer starten
def planer_starten():
    # Aktivitäten mit Preisen als Dictionary
    kosten = {
        'Spaziergang': 0,
        'Kino': 12,
        'Restaurant': 30,
        'Couch': 0
    }

    # Budget als Zahl einlesen
    try:
        budget = int(input('Budget heute in €: '))
    except ValueError:
        print('Gib bitte eine Zahl ein.')
        # Abbruch bei ungültiger Eingabe
        return None
    # negatives Budget ist nicht möglich => Standardwert 0
    if budget < 0:
        print('Warnung: Budget ist negativ. Setze auf 0.')
        budget = 0
    
    # Energie als Text einlesen
    energie = input('Ist deine Energie hoch oder niedrig: ')

    # Regeln (if/elif/else)
    if energie == 'hoch' and budget >= 30:
        vorschlag = 'Restaurant'
    elif energie == 'hoch' and 12 <= budget < 30:
        vorschlag = 'Kino'
    elif energie == 'hoch':         # and budget < 12:
        vorschlag = 'Spaziergang'
    else:
        vorschlag = 'Couch'

    # Preis bestimmen
    preis = kosten[vorschlag]
    # Vorschlag und Preis ausgeben
    print(f'Vorschlag: {vorschlag}, | Kosten: {preis}')
    
    # Motivation abhängig von Energie ausgeben
    if energie == 'hoch':
        print('Motivation: Nutze die Energie für etwas Schönes.')
    else:
        print('Motivation: Mach es dir gemütlich und erhol dich gut.')

    return vorschlag