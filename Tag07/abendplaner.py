# Überschrift
print('--- ABENDPLANER ---\n\n')

# Nutzereingaben: Budget, Gutschein, Lust zum Ausgehen
budget = int(input('Wie viel Geld hast du heute Abend?\n'))
gutschein = input('Hast du einen Gutschein (ja / nein)?\n').lower()
lust = input('Möchtest du ausgehen (ja / nein)?').lower()

# Umwandlung von gutschein und lust in Boolean
gutschein = gutschein == 'ja'
lust = lust == 'ja'

# keine Lust vorhanden oder Budget nicht ausreichend => zu Hause bleiben
if not lust or budget < 30:
    print('Bleib zu Hause und mach es dir gemütlich')
# Lust ist vorhanden
else:
    # ausreichend Budget und Gutschein
    if budget >= 50 and gutschein:
        print('Großer Abend: Restaurant oder Kino mit Rabatt')
    # ausreichend Budget ohne Gutschein
    elif budget >= 50:          # gutschein: False, da sonst Zeile 19 True
        print('Großer Abend: Restaurant oder Kino ohne Rabatt')
    # mittleres Budget
    else:           # elif budget < 50 and budget >= 30:
        # mit Gutschein
        if gutschein:
            print('Netter Abend: Essen mit Rabatt')
        # ohne Gutschein
        else:
            print('Bleib zu Hause und mach es dir gemütlich.')